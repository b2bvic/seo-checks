#!/usr/bin/env python3
"""
Anchor text link suggester powered by dejanseo/google-links (DeBERTa v3).

Performs token-level binary classification to predict which words in text
should be hyperlinks — reverse-engineering Google's editorial linking patterns.

Usage:
    python suggest_links.py --file article.md
    python suggest_links.py --url https://example.com/page
    cat article.md | python suggest_links.py
    python suggest_links.py --file article.md --sitemap https://example.com/sitemap.xml
"""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import requests
import torch
from bs4 import BeautifulSoup
from transformers import AutoModelForTokenClassification, AutoTokenizer

MODEL_ID = "dejanseo/google-links"
WINDOW_SIZE = 512
STRIDE = 128
CONTEXT_CHARS = 40  # chars of surrounding context in output


def load_model():
    """Lazy-load model and tokenizer from HuggingFace cache."""
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForTokenClassification.from_pretrained(MODEL_ID)
    model.eval()
    return tokenizer, model


def strip_markdown(text: str) -> str:
    """Remove YAML frontmatter and markdown formatting, preserve raw text."""
    # Strip YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n?", "", text, flags=re.DOTALL)
    # Strip inline properties (field:: value)
    text = re.sub(r"^\w[\w\s]*?::\s.*$", "", text, flags=re.MULTILINE)
    # Strip images
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # Strip links but keep text: [text](url) → text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Strip HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Strip markdown emphasis markers
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)
    # Strip heading markers
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # Collapse whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_from_url(url: str) -> str:
    """Fetch URL and extract body text."""
    resp = requests.get(url, timeout=15, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) link-suggester/1.0"
    })
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")
    # Remove script/style/nav/footer
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    # Prefer article or main content
    body = soup.find("article") or soup.find("main") or soup.find("body")
    return body.get_text(separator="\n", strip=True) if body else ""


def sliding_window_inference(text: str, tokenizer, model, threshold: float):
    """
    Run inference with sliding window over text.

    DeBERTa's context window is 512 tokens. For longer texts, we slide a
    window with stride overlap, then aggregate predictions at each token
    position by averaging logits across all windows that see that token.
    """
    encoding = tokenizer(
        text,
        return_offsets_mapping=True,
        add_special_tokens=False,
        return_tensors=None,
    )
    input_ids = encoding["input_ids"]
    offset_mapping = encoding["offset_mapping"]
    total_tokens = len(input_ids)

    # Accumulate logits per token position (for averaging overlapping windows)
    logit_sums = torch.zeros(total_tokens, 2)
    logit_counts = torch.zeros(total_tokens)

    # Slide window
    for start in range(0, total_tokens, STRIDE):
        end = min(start + WINDOW_SIZE, total_tokens)
        window_ids = input_ids[start:end]

        # Wrap with CLS/SEP for DeBERTa
        cls_id = tokenizer.cls_token_id
        sep_id = tokenizer.sep_token_id
        wrapped_ids = [cls_id] + window_ids + [sep_id]
        input_tensor = torch.tensor([wrapped_ids])
        attention_mask = torch.ones_like(input_tensor)

        with torch.no_grad():
            outputs = model(input_ids=input_tensor, attention_mask=attention_mask)
            # Strip CLS/SEP logits → shape [1, window_len, 2]
            window_logits = outputs.logits[0, 1:-1, :]

        # Accumulate into global arrays
        for i, logit in enumerate(window_logits):
            global_idx = start + i
            if global_idx < total_tokens:
                logit_sums[global_idx] += logit
                logit_counts[global_idx] += 1

        if end >= total_tokens:
            break

    # Average logits and compute probabilities
    avg_logits = logit_sums / logit_counts.unsqueeze(1).clamp(min=1)
    probs = torch.softmax(avg_logits, dim=-1)

    return probs, offset_mapping


def reconstruct_anchors(text: str, probs, offset_mapping, threshold: float):
    """
    Map sub-word token predictions back to word-level spans.
    Merge consecutive LINK-predicted tokens into anchor phrases.

    The model outputs per-token probabilities. We need to:
    1. Identify tokens above threshold
    2. Merge consecutive link tokens into contiguous spans
    3. Snap span boundaries to word boundaries
    4. Extract the anchor text and surrounding context
    """
    link_label = 1  # Binary: 0=no-link, 1=link
    candidates = []
    current_span = None

    for idx, (prob_vec, offset) in enumerate(zip(probs, offset_mapping)):
        char_start, char_end = offset
        confidence = prob_vec[link_label].item()

        if confidence >= threshold:
            if current_span is None:
                current_span = {
                    "char_start": char_start,
                    "char_end": char_end,
                    "max_conf": confidence,
                    "conf_sum": confidence,
                    "token_count": 1,
                }
            else:
                # Extend span — allow small gaps (1-2 chars, e.g. spaces between sub-words)
                # But NEVER bridge across newlines or markdown separators
                gap = char_start - current_span["char_end"]
                gap_text = text[current_span["char_end"]:char_start]
                if gap <= 3 and "\n" not in gap_text:
                    current_span["char_end"] = char_end
                    current_span["max_conf"] = max(current_span["max_conf"], confidence)
                    current_span["conf_sum"] += confidence
                    current_span["token_count"] += 1
                else:
                    # Gap too large — finalize previous span
                    candidates.append(current_span)
                    current_span = {
                        "char_start": char_start,
                        "char_end": char_end,
                        "max_conf": confidence,
                        "conf_sum": confidence,
                        "token_count": 1,
                    }
        else:
            if current_span is not None:
                candidates.append(current_span)
                current_span = None

    if current_span is not None:
        candidates.append(current_span)

    # Build structured output with anchor text and context
    results = []
    for span in candidates:
        cs, ce = span["char_start"], span["char_end"]
        anchor = text[cs:ce].strip()
        if not anchor or len(anchor) < 2:
            continue

        # Snap to word boundaries — expand to include partial words, stop at newlines
        while cs > 0 and text[cs - 1] not in " \n\t.,;:!?()[]{}\"'-":
            cs -= 1
        while ce < len(text) and text[ce] not in " \n\t.,;:!?()[]{}\"'-":
            ce += 1
        anchor = text[cs:ce].strip().strip("()-")
        if not anchor:
            continue

        # Context window
        ctx_start = max(0, cs - CONTEXT_CHARS)
        ctx_end = min(len(text), ce + CONTEXT_CHARS)
        context = ("..." if ctx_start > 0 else "") + text[ctx_start:ctx_end] + ("..." if ctx_end < len(text) else "")

        avg_conf = span["conf_sum"] / span["token_count"]
        results.append({
            "anchor": anchor,
            "confidence": round(avg_conf, 4),
            "char_start": cs,
            "char_end": ce,
            "context": context,
        })

    # Deduplicate: if same anchor appears multiple times, keep highest confidence
    seen = {}
    for r in results:
        key = r["anchor"].lower()
        if key not in seen or r["confidence"] > seen[key]["confidence"]:
            seen[key] = r

    deduped = sorted(seen.values(), key=lambda x: -x["confidence"])
    return deduped


def fetch_sitemap(sitemap_url: str):
    """Fetch sitemap XML and extract URLs + last path segments as pseudo-titles."""
    resp = requests.get(sitemap_url, timeout=15, headers={
        "User-Agent": "Mozilla/5.0 link-suggester/1.0"
    })
    resp.raise_for_status()

    pages = []
    root = ET.fromstring(resp.content)
    # Handle namespace
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    # Check if sitemap index
    sitemaps = root.findall(".//sm:sitemap/sm:loc", ns)
    if sitemaps:
        # Recurse into child sitemaps (limit to first 5)
        for sm_loc in sitemaps[:5]:
            try:
                pages.extend(fetch_sitemap(sm_loc.text.strip()))
            except Exception:
                continue
        return pages

    # Regular sitemap
    for url_el in root.findall(".//sm:url/sm:loc", ns):
        url = url_el.text.strip()
        parsed = urlparse(url)
        slug = parsed.path.rstrip("/").split("/")[-1] if parsed.path.rstrip("/") else ""
        # Convert slug to pseudo-title: "my-cool-page" → "my cool page"
        title = slug.replace("-", " ").replace("_", " ").strip()
        pages.append({"url": url, "slug": slug, "title": title})

    return pages


def match_anchors_to_sitemap(candidates, sitemap_pages):
    """
    Fuzzy-match anchor candidates against sitemap page titles/slugs.
    Uses rapidfuzz for fast approximate string matching.
    """
    from rapidfuzz import fuzz

    matches = []
    titles = [p["title"] for p in sitemap_pages]

    for cand in candidates:
        anchor_lower = cand["anchor"].lower()
        best_score = 0
        best_page = None
        match_method = None

        for page in sitemap_pages:
            # Exact substring match in slug
            if anchor_lower.replace(" ", "-") in page["slug"].lower():
                score = 95
                method = "slug_substring"
            else:
                # Fuzzy match against title
                score = fuzz.token_sort_ratio(anchor_lower, page["title"].lower())
                method = "fuzzy_title"

            if score > best_score:
                best_score = score
                best_page = page
                match_method = method

        if best_score >= 60 and best_page:
            matches.append({
                "anchor": cand["anchor"],
                "confidence": cand["confidence"],
                "suggested_url": best_page["url"],
                "match_score": best_score,
                "match_method": match_method,
            })

    return sorted(matches, key=lambda x: (-x["confidence"], -x["match_score"]))


def format_table(candidates, sitemap_matches=None):
    """Render results as a markdown table."""
    lines = ["## Anchor Text Candidates", ""]
    lines.append("| Anchor | Confidence | Context |")
    lines.append("|--------|------------|---------|")
    for c in candidates:
        ctx = c["context"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {c['anchor']} | {c['confidence']:.2f} | {ctx} |")

    if sitemap_matches:
        lines.extend(["", "## Sitemap Matches", ""])
        lines.append("| Anchor | Confidence | Suggested URL | Match Method | Match Score |")
        lines.append("|--------|------------|---------------|--------------|-------------|")
        for m in sitemap_matches:
            lines.append(
                f"| {m['anchor']} | {m['confidence']:.2f} | {m['suggested_url']} | {m['match_method']} | {m['match_score']} |"
            )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Predict anchor text candidates using dejanseo/google-links model"
    )
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument("--file", "-f", help="Path to markdown/text file")
    input_group.add_argument("--url", "-u", help="URL to fetch and analyze")
    parser.add_argument("--sitemap", "-s", help="Sitemap URL for cross-referencing anchors to pages")
    parser.add_argument("--threshold", "-t", type=float, default=0.5, help="Confidence threshold (default: 0.5)")
    parser.add_argument("--format", choices=["json", "table"], default="json", help="Output format (default: json)")
    args = parser.parse_args()

    # --- Acquire text ---
    source = "stdin"
    if args.file:
        source = args.file
        raw = Path(args.file).read_text(encoding="utf-8")
        text = strip_markdown(raw)
    elif args.url:
        source = args.url
        text = extract_from_url(args.url)
    else:
        if sys.stdin.isatty():
            parser.print_help()
            sys.exit(1)
        raw = sys.stdin.read()
        text = strip_markdown(raw)

    if not text.strip():
        print(json.dumps({"source": source, "error": "No text extracted", "candidates": []}))
        sys.exit(0)

    # --- Load model & run inference ---
    tokenizer, model = load_model()
    probs, offset_mapping = sliding_window_inference(text, tokenizer, model, args.threshold)
    candidates = reconstruct_anchors(text, probs, offset_mapping, args.threshold)

    # --- Sitemap matching ---
    sitemap_matches = []
    if args.sitemap:
        try:
            pages = fetch_sitemap(args.sitemap)
            if pages:
                sitemap_matches = match_anchors_to_sitemap(candidates, pages)
        except Exception as e:
            print(f"Warning: Sitemap fetch failed: {e}", file=sys.stderr)

    # --- Output ---
    if args.format == "table":
        print(format_table(candidates, sitemap_matches if sitemap_matches else None))
    else:
        output = {
            "source": source,
            "threshold": args.threshold,
            "candidates": candidates,
        }
        if sitemap_matches:
            output["sitemap_matches"] = sitemap_matches
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
