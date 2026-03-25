---
name: cannibalize
description: "Detect keyword cannibalization across your content. Weighted overlap scoring + cluster analysis. 🌐 Victor Valentine Romo · victorvalentineromo.com · scalewithsearch.com"
---

# Keyword Cannibalization Detector

Find pages competing for the same keywords. Uses a 6-element weighted fingerprint per page, pairwise overlap matrix, connected-component clustering, and actionable recommendations.

## Arguments

| Arg | Default | Purpose |
|-----|---------|---------|
| `<folder-or-site>` | Required | Folder of content files or site URL |
| `--threshold` | `0.6` | Overlap score above which pairs are flagged |
| `--output PATH` | `./cannibalization-report.md` | Output path |

## Steps

### 1. Collect all pages

**Local folder:** Glob for `**/*.md` or `**/*.html`

**Live site:** Fetch sitemap.xml, extract all `<loc>` URLs. Sample if >50 pages.

### 2. Extract per-page fingerprint

For each page, extract 6 elements:

| Element | Weight |
|---------|--------|
| Meta title / H1 | 0.25 |
| Top-10 keyword phrases (by frequency) | 0.25 |
| H2 headings (all) | 0.20 |
| URL slug keywords | 0.15 |
| Search intent (info / commercial / transactional / nav) | 0.10 |
| Meta description | 0.05 |

**Top-10 keyword extraction:**
1. Strip stop words
2. Extract 2-3 word phrases by frequency
3. Rank by occurrence count
4. Take top 10

### 3. Compute pairwise overlap matrix

For every pair (A, B):

```
overlap(A, B) =
    0.25 × title_similarity(A, B) +
    0.25 × keyword_overlap(A, B) +
    0.20 × h2_overlap(A, B) +
    0.15 × slug_similarity(A, B) +
    0.10 × intent_match(A, B) +
    0.05 × description_similarity(A, B)
```

Each component is 0.0 to 1.0:
- **title_similarity**: Jaccard similarity of title words
- **keyword_overlap**: % of shared top-10 phrases
- **h2_overlap**: % of shared H2 topic words
- **slug_similarity**: Jaccard similarity of slug segments
- **intent_match**: 1.0 if same intent, 0.0 if different
- **description_similarity**: Jaccard similarity of description words

### 4. Flag pairs above threshold

Any pair scoring above `--threshold` (default 0.6) is flagged.

### 5. Group into clusters

Use connected-component grouping: if A overlaps B and B overlaps C, they form cluster {A, B, C}.

### 6. Recommend actions

For each cluster:

| Action | When |
|--------|------|
| **Merge** | Pages cover identical topic, no unique angle. Combine into one authoritative page. |
| **Differentiate** | Pages could target different intents or angles. Adjust titles, H2s, keywords. |
| **Redirect** | Weaker page 301s to stronger page. Consolidate link equity. |
| **Keep** | Overlap is intentional (hub + spoke). No action. |

### 7. Write report

```markdown
# Cannibalization Report

**Date:** {date}
**Pages analyzed:** {count}
**Threshold:** {threshold}
**Clusters found:** {count}

## Summary

| Metric | Value |
|--------|-------|
| Flagged pairs | {n} |
| Clusters | {n} |
| Merge recommended | {n} |
| Differentiate recommended | {n} |
| Redirect recommended | {n} |

## Clusters

### Cluster 1: "{shared topic}" — Overlap: {score}

| Page | Title | Primary Keyword | Intent | Overlap |
|------|-------|-----------------|--------|---------|
| A | {title} | {kw} | {intent} | {score} |
| B | {title} | {kw} | {intent} | {score} |

**Overlap breakdown:**

| Element | Score |
|---------|-------|
| Title | {n} |
| Keywords | {n} |
| H2s | {n} |
| Slug | {n} |
| Intent | {n} |
| Description | {n} |
| **Total** | **{n}** |

**Recommendation:** {action}
**Specific changes:** {details}

## Implementation Priority

| Priority | Cluster | Action | Pages | Impact |
|----------|---------|--------|-------|--------|
| HIGH | {cluster} | {action} | {n} | {why} |
```
