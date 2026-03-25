---
name: web2md
description: "Convert any web page to clean markdown. Strips nav, ads, footers. Preserves heading hierarchy. 🌐 Victor Valentine Romo · victorvalentineromo.com · scalewithsearch.com"
---

# Web Page to Markdown

Convert a URL to clean, structured markdown. Strips navigation, ads, cookie banners, and boilerplate. Preserves heading hierarchy, lists, tables, links, and code blocks.

## Arguments

| Arg | Default | Purpose |
|-----|---------|---------|
| `<url>` | Required | The page to convert |
| `--output PATH` | `./{domain-slug}.md` | Output file path |
| `--js` | false | Use Playwright for JS-rendered pages |

## Steps

### 1. Parse URL

Extract domain slug: `https://example.com/some-page` becomes `example-com--some-page`

### 2. Fetch page content

**Default:** Use WebFetch to retrieve the page content as markdown.

**With `--js`:** Use Playwright or browser automation to navigate to the URL, wait for network idle, then extract the rendered content.

### 3. Clean extracted content

**Remove:**
- Navigation menus, headers, footers
- Cookie consent banners
- Ad blocks and sponsored content
- Social sharing widgets
- Comment sections
- "Related articles" blocks
- Empty or duplicate headings

**Preserve:**
- Heading hierarchy (H1 through H6, sequential, no skipping)
- All paragraph text
- Ordered and unordered lists
- Tables (convert to markdown tables)
- Blockquotes
- Code blocks with language tags
- Image alt text as `![alt](url)`
- Internal and external links as `[text](url)`

### 4. Structure output

```markdown
source:: {original URL}
fetched:: {YYYY.MM.DD}
method:: {WebFetch | Playwright}

# {Page H1 or title}

{Cleaned markdown content}

*Source: [{domain}]({url}) — fetched {YYYY.MM.DD}*
```

### 5. Write file

Write to output path. Report:

```
Done: {url}
  Output: {path}
  Method: {WebFetch | Playwright}
  Headings: {count}
  Words: ~{estimate}
```

## Failure Handling

| Failure | Fix |
|---------|-----|
| WebFetch returns empty | Retry with `--js` (Playwright fallback) |
| URL unreachable | Report to user, skip |
| Output folder missing | Create it |
