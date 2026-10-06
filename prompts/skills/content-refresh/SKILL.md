---
name: content-refresh
description: "Audit content freshness across 8 weighted signals. Score 0-100 with priority actions. 🌐 Victor Valentine Romo · victorvalentineromo.com · scalewithsearch.com"
---

# Content Freshness Auditor

Score content staleness across 8 signals. Produces a 0-100 refresh priority score with specific action items per page.

## Arguments

| Arg | Default | Purpose |
|-----|---------|---------|
| `<path-or-url>` | Required | Article file path or live URL |
| `--batch GLOB` | none | Glob pattern for multiple files |
| `--output PATH` | `./content-refresh-audit.md` | Output path |

## Steps

### 1. Extract page content and metadata

For each page, extract:
- Publication date (from frontmatter, meta tags, or file modification date)
- Author information (name, bio, credentials)
- All statistics with source citations and years
- All external links/citations
- All H2 sections with word counts
- Schema markup references
- Internal link count
- Full text for vocabulary analysis

### 2. Audit 8 staleness signals

| # | Signal | Weight | How to detect |
|---|--------|--------|---------------|
| 1 | Publication date >12 months old | 20 pts | Compare pub date to today |
| 2 | Statistics without year or >2 years old | 20 pts | Find numbers with "%" or data claims, check for year citation |
| 3 | E-E-A-T gaps | 15 pts | Check for: author name, credentials, sources cited, firsthand experience signals |
| 4 | AI-marker vocabulary | 12 pts | Scan for overused AI words: landscape, realm, navigating, tailored, crucial, moreover, furthermore, leverage, plethora, dive/diving, embrace, "when it comes to", "let's dive in", "in today's", "picture this" |
| 5 | Broken citation links | 10 pts | Fetch each external link, check for 404/redirect |
| 6 | Thin sections (<100 words under any H2) | 10 pts | Count words per H2 section |
| 7 | Missing schema markup | 8 pts | Check for Article, FAQ, HowTo, or BreadcrumbList schema |
| 8 | Insufficient internal links | 5 pts | Flag if <3 internal links for articles >1,000 words |

### 3. Compute refresh priority score

```
Score = Sum of all triggered signal points (max 100)
```

| Score | Priority | Action |
|-------|----------|--------|
| 71-100 | CRITICAL | Immediate rewrite |
| 51-70 | HIGH | Major refresh within 30 days |
| 31-50 | MEDIUM | Targeted updates (stats, links, thin sections) |
| 11-30 | LOW | Minor polish (vocabulary, schema, internal links) |
| 0-10 | FRESH | No action needed |

### 4. Generate action items

For each triggered signal, produce:

```
Signal: {name} — {weight} — TRIGGERED
Finding: {what was found}
Section: {which H2 or location}
Action: {exactly what to change}
```

### 5. Write audit report

```markdown
# Content Refresh Audit

**Date:** {date}
**Pages audited:** {count}
**Average refresh score:** {n}/100

## Summary

| Metric | Value |
|--------|-------|
| CRITICAL (71-100) | {n} pages |
| HIGH (51-70) | {n} pages |
| MEDIUM (31-50) | {n} pages |
| LOW (11-30) | {n} pages |
| FRESH (0-10) | {n} pages |

## Signal Distribution

| Signal | Pages Triggered | Most Common Issue |
|--------|----------------|-------------------|
| Stale publication date | {n} | {issue} |
| Outdated statistics | {n} | {issue} |
| E-E-A-T gaps | {n} | {issue} |
| AI-marker vocabulary | {n} | {top words} |
| Broken citations | {n} | {issue} |
| Thin sections | {n} | {issue} |
| Missing schema | {n} | {issue} |
| Insufficient internal links | {n} | {issue} |

## Page-by-Page Results

### {Page Title} — Score: {n}/100 — {PRIORITY}

| Signal | Weight | Status | Finding |
|--------|--------|--------|---------|
| Publication date | 20 | {TRIGGERED/OK} | {finding} |
| ... | ... | ... | ... |

**Action items:**
1. {specific action}
2. {specific action}

## Refresh Queue (Ordered by Score)

| Priority | Page | Score | Top Signals | Action |
|----------|------|-------|-------------|--------|
| CRITICAL | {page} | {n} | {signals} | Rewrite |
| HIGH | {page} | {n} | {signals} | {specifics} |
```
