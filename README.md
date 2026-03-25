# link-suggest

ML-powered anchor text predictor. Uses DeBERTa v3 trained on 10,273 Google Blog posts to predict which words in your content should be hyperlinks.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## What It Does

Feed it any article or web page. The model performs **token-level binary classification** to identify words that Google's editorial patterns suggest should be hyperlinked. Optional sitemap cross-referencing suggests destination URLs.

Based on the [dejanseo/google-links](https://huggingface.co/dejanseo/google-links) model by Dan Petrovic.

## Install

```bash
git clone https://github.com/b2bvic/link-suggest.git
cd link-suggest
bash setup.sh
```

Setup creates a venv and pre-downloads the model (~1.2GB on first run, cached after).

## Usage

```bash
# Analyze a markdown file
./run.sh --file article.md

# Analyze a live URL
./run.sh --url https://example.com/blog-post

# Pipe from stdin
cat article.md | ./run.sh

# Match anchors against your sitemap
./run.sh --file article.md --sitemap https://example.com/sitemap.xml

# Adjust confidence threshold (default: 0.5)
./run.sh --file article.md --threshold 0.4

# Output as markdown table
./run.sh --file article.md --format table
```

## Output

### JSON (default)

```json
{
  "source": "article.md",
  "threshold": 0.5,
  "candidates": [
    {
      "anchor": "internal linking",
      "confidence": 0.8934,
      "char_start": 142,
      "char_end": 158,
      "context": "...the importance of internal linking for SEO performance..."
    }
  ]
}
```

### Table (`--format table`)

```
## Anchor Text Candidates

| Anchor | Confidence | Context |
|--------|------------|---------|
| internal linking | 0.89 | ...the importance of internal linking for SEO... |
| page authority | 0.76 | ...distributes page authority through the site... |
```

### With Sitemap Matching (`--sitemap`)

```
## Sitemap Matches

| Anchor | Confidence | Suggested URL | Match Method | Match Score |
|--------|------------|---------------|--------------|-------------|
| internal linking | 0.89 | https://example.com/internal-linking-guide | slug_substring | 95 |
```

## How It Works

1. **Input** — Accepts markdown files, URLs, or stdin. Strips formatting, extracts raw text.
2. **Tokenization** — DeBERTa v3 tokenizer splits text into sub-word tokens.
3. **Sliding Window** — 512-token windows with 128-token stride. Overlapping windows have their logits averaged for stable predictions.
4. **Classification** — Binary per-token: link or no-link. Trained on Google's own editorial linking decisions.
5. **Reconstruction** — Sub-word predictions merged back to word-level anchor spans. Consecutive link tokens form phrases. Word boundary snapping.
6. **Deduplication** — Same anchor appearing multiple times keeps highest confidence instance.
7. **Sitemap Matching** — Optional fuzzy matching of anchor candidates against sitemap slugs/titles using rapidfuzz.

## Requirements

- Python 3.9+
- ~1.2GB disk for model (auto-cached by HuggingFace)
- CPU only (no GPU required)

## Dependencies

```
torch
transformers
requests
beautifulsoup4
lxml
rapidfuzz
```

## License

MIT
