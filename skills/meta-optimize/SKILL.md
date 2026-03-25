---
name: meta-optimize
description: "Audit and optimize meta titles (<60 chars) and descriptions (<155 chars) with SERP competition analysis. 🌐 Victor Valentine Romo · victorvalentineromo.com · scalewithsearch.com"
---

# Meta Title & Description Optimizer

Audit existing meta tags, generate optimized alternatives, and analyze SERP competition patterns.

## Arguments

| Arg | Default | Purpose |
|-----|---------|---------|
| `<path-or-url>` | Required | Article file or live URL |
| `--batch GLOB` | none | Glob pattern for multiple files |
| `--output PATH` | `./meta-optimization-audit.md` | Output path |

## Steps

### 1. Extract current meta from each page

**For local files:**
- Title: first H1 or `title` in frontmatter
- Description: first paragraph or `description` in frontmatter
- URL slug: filename or `slug` in frontmatter

**For live URLs:**
- Fetch the page and extract `<title>`, meta description, H1, first 3 H2s, URL path

### 2. Generate optimized meta

**Title optimization (max 60 characters):**
- Lead with primary keyword
- Include a power word or number
- End with brand name or modifier
- Avoid AI-marker vocabulary (no: landscape, realm, crucial, embrace, leverage, dive, navigating)
- Character count MUST be 60 or under

**Description optimization (max 155 characters):**
- Open with action verb or benefit
- Include primary + secondary keyword
- End with CTA or value proposition
- Avoid AI-marker vocabulary
- Character count MUST be 155 or under

### 3. SERP competition check

For each page's primary keyword, search and extract from the top 3 results:
- Their title tag (text + character count)
- Their meta description (text + character count)
- Common patterns (numbers, brackets, year, power words)

### 4. Build comparison table

For each page:

```markdown
### {Page Title}

| Element | Current | Chars | Recommended | Chars | Delta |
|---------|---------|-------|-------------|-------|-------|
| Title | {current} | {n} | {optimized} | {n} | {+/-} |
| Description | {current} | {n} | {optimized} | {n} | {+/-} |

**Primary keyword:** {keyword}
**SERP pattern:** {what competitors use}
**Changes:** {what was improved and why}
```

### 5. Write audit report

```markdown
# Meta Optimization Audit

**Date:** {date}
**Pages audited:** {count}

## Summary

| Metric | Value |
|--------|-------|
| Titles over 60 chars | {n} |
| Descriptions over 155 chars | {n} |
| Titles missing primary keyword | {n} |
| AI-marker vocabulary found | {n} |

## Page-by-Page Results

{comparison tables}

## SERP Competition Analysis

| Keyword | #1 Title Pattern | #2 Title Pattern | #3 Title Pattern | Our Approach |
|---------|-----------------|-----------------|-----------------|--------------|

## Implementation Priority

| Priority | Page | Issue | Action |
|----------|------|-------|--------|
| HIGH | {page} | {issue} | {change} |
```
