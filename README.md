# seo-checks

Run 20 SEO page checks from one command. `seo-checks robots`, `seo-checks redirects`, `seo-checks schema-product`, and 17 more read a URL or a local file and return a report. Every check can emit JSON.
Each check is a small Python script with its own tests, and the dispatcher passes your arguments through unchanged.

[Project page](https://scalewithsearch.com/code/seo-checks)

A site audit before a launch takes a dozen single-purpose scripts that each need their own install.
This repository packages them as one CLI, keeps each script's source and tests in `components/`, and adds six Claude Code prompts for content review in `prompts/`.

## Quick start

Use Python 3.11 or later. The install pulls Click, Requests, Beautiful Soup, lxml, and certifi.

```bash
git clone https://github.com/b2bvic/seo-checks.git
cd seo-checks
python3 -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/seo-checks --help
```

Check a live site:

```bash
.venv/bin/seo-checks robots https://example.com
.venv/bin/seo-checks redirects https://example.com
.venv/bin/seo-checks sitemap https://example.com/sitemap.xml --check-urls --limit 20
.venv/bin/seo-checks schema-product https://example.com/product --json-output
```

Analyze a local file without a network request:

```bash
.venv/bin/seo-checks readability article.txt --json-output
.venv/bin/seo-checks word-freq article.txt --top 10 --json-output
.venv/bin/seo-checks citations --name "Example business" --city "Example City" --json-output
```

`seo-checks <subcommand> --help` prints the component's own options. Crawling checks stop at a URL limit: 50 for `sitemap` and `internal-links`, 100 for `thin-product`. Set `--limit` before you point them at a large site.
You can also run `.venv/bin/python seo_checks.py <subcommand>` from the checkout without installing.

## Commands

| Command | Component | Purpose |
| --- | --- | --- |
| `sitemap` | [sitemap-check](#sitemap-check) | Parse XML sitemaps and optionally check URLs. |
| `robots` | [robots-check](#robots-check) | Inspect robots.txt directives and blocking rules. |
| `redirects` | [redirect-trace](#redirect-trace) | Trace HTTP redirects, loops, and HTTPS downgrades. |
| `headings` | [heading-audit](#heading-audit) | Check HTML heading order and empty headings. |
| `alt` | [alt-audit](#alt-audit) | Classify image alt text and dimension attributes. |
| `og` | [og-check](#og-check) | Check Open Graph and Twitter Card metadata. |
| `readability` | [readability](#readability) | Estimate Flesch readability from a URL or file. |
| `word-freq` | [word-freq](#word-freq) | Count filtered words and phrases in a URL or file. |
| `internal-links` | [internal-link-audit](#internal-link-audit) | Count internal links in a bounded sitemap crawl. |
| `thin-product` | [thin-product](#thin-product) | Find sampled pages below a unique-word threshold. |
| `link-suggest` | [link-suggest](#link-suggest) | Suggest anchor phrases with an optional downloaded model. |
| `citations` | [citation-check](#citation-check) | Generate directory search links for manual review. |
| `gbp` | [gbp-audit](#gbp-audit) | Check public local-business website markup. |
| `schema-product` | [product-schema](#product-schema) | Check Product JSON-LD fields. |
| `schema-course` | [course-schema](#course-schema) | Check Course and ItemList JSON-LD fields. |
| `schema-health` | [schema-health](#schema-health) | Check configured healthcare JSON-LD field profiles. |
| `hipaa-meta` | [hipaa-meta](#hipaa-meta) | Flag possible identifiers in metadata for human review. |
| `menu` | [menu-seo](#menu-seo) | Inspect restaurant menu markup and visible prices. |
| `spec-sheet` | [spec-sheet](#spec-sheet) | Inspect product specification markup and PDF links. |
| `saas-onboard` | [saas-onboard](#saas-onboard) | Check SaaS indexing directives and canonical paths. |
| Prompts only | [sws-skills](#sws-skills) | Six Claude Code prompts for content review. |

## What the checks do not do

- URL checks fetch public pages over HTTP. They do not execute JavaScript or render previews.
- Field and length thresholds are project heuristics. A pass does not establish search-engine eligibility, accessibility conformance, or legal compliance.
- `hipaa-meta` output can contain the sensitive source text it flags. Treat its reports as private.
- `citations` writes links for you to open. It does not fetch or verify a directory listing.

Each component README lists its own limits.

## Optional link model

Every check except `link-suggest` runs without machine-learning libraries.
`link-suggest` analysis needs PyTorch, Transformers, and RapidFuzz, and downloads the `dejanseo/google-links` weights (about 1.2 GB) on the first analysis. Without the libraries, the command prints the install instruction and exits with status 2. `--help` works without them.

```bash
.venv/bin/python -m pip install ".[link-suggest]"
export HF_HOME="$PWD/.model-cache"
.venv/bin/seo-checks link-suggest --file article.md --format table
```

The model has its own upstream terms. Read its model card before you use the weights. Suggestions do not prove relevance.

## Test

```bash
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/test_components.py
```

The first suite runs 24 dispatcher tests. The second runs the 21 component suites from their own folders and writes logs, pytest XML, and `summary.json` to `.test-results/`. A missing test dependency marks a suite skipped with the reason; a failed suite exits with status 1.

## Model assistance

Codex prepared this rollup's dispatcher, packaging, tests, and documentation. The component READMEs keep their own disclosures.
The `prompts/` folder holds Markdown instructions for Claude Code; the prompts call no model themselves, and their findings need human review.

## License

All 21 components use MIT licenses with the same copyright holder. The top-level [LICENSE](LICENSE) and each component license remain in place.

## Components

<a id="sitemap-check"></a>

### sitemap-check

`seo-checks sitemap` parses an XML sitemap and, with `--check-urls`, requests each URL up to `--limit`. Nested sitemap indexes are not followed. [README](components/sitemap-check/README.md)

<a id="robots-check"></a>

### robots-check

`seo-checks robots` lists robots.txt user-agent blocks and the rules that block crawlers. A blocking rule can be intentional. [README](components/robots-check/README.md)

<a id="redirect-trace"></a>

### redirect-trace

`seo-checks redirects` records each redirect hop and reports loops and HTTPS-to-HTTP downgrades. [README](components/redirect-trace/README.md)

<a id="heading-audit"></a>

### heading-audit

`seo-checks headings` checks heading order and empty headings in returned HTML. [README](components/heading-audit/README.md)

<a id="alt-audit"></a>

### alt-audit

`seo-checks alt` classifies image alt attributes and dimension attributes so you can select images for review. [README](components/alt-audit/README.md)

<a id="og-check"></a>

### og-check

`seo-checks og` extracts Open Graph and Twitter Card fields and checks presence and length. It does not fetch the image URLs. [README](components/og-check/README.md)

<a id="readability"></a>

### readability

`seo-checks readability` computes Flesch reading ease and grade level from a URL or text file. [README](components/readability/README.md)

<a id="word-freq"></a>

### word-freq

`seo-checks word-freq` counts filtered words, bigrams, and trigrams with density percentages. [README](components/word-freq/README.md)

<a id="internal-link-audit"></a>

### internal-link-audit

`seo-checks internal-links` crawls up to `--limit` sitemap pages and counts inbound internal links to find orphan candidates. [README](components/internal-link-audit/README.md)

<a id="thin-product"></a>

### thin-product

`seo-checks thin-product` samples sitemap pages and reports pages below a unique-word threshold. [README](components/thin-product/README.md)

<a id="link-suggest"></a>

### link-suggest

`seo-checks link-suggest` runs a token-classification model over text and proposes anchor phrases for internal links. See [Optional link model](#optional-link-model). [README](components/link-suggest/README.md)

<a id="citation-check"></a>

### citation-check

`seo-checks citations` builds directory search URLs for a business name and city so you can compare listings by hand. [README](components/citation-check/README.md)

<a id="gbp-audit"></a>

### gbp-audit

`seo-checks gbp` checks LocalBusiness JSON-LD fields and visible page signals on a public site. It does not connect to Google Business Profile. [README](components/gbp-audit/README.md)

<a id="product-schema"></a>

### product-schema

`seo-checks schema-product` checks Product JSON-LD fields against a checklist and reports a score. [README](components/product-schema/README.md)

<a id="course-schema"></a>

### course-schema

`seo-checks schema-course` checks Course and ItemList JSON-LD fields. The list checker does not fetch linked course pages. [README](components/course-schema/README.md)

<a id="schema-health"></a>

### schema-health

`seo-checks schema-health` checks selected healthcare JSON-LD types against project-defined field profiles. [README](components/schema-health/README.md)

<a id="hipaa-meta"></a>

### hipaa-meta

`seo-checks hipaa-meta` flags metadata that matches identifier patterns for human privacy review. Matches can be false positives. [README](components/hipaa-meta/README.md)

<a id="menu-seo"></a>

### menu-seo

`seo-checks menu` inspects restaurant menu markup, visible prices, and dietary terms in HTML. It does not read PDF menus. [README](components/menu-seo/README.md)

<a id="spec-sheet"></a>

### spec-sheet

`seo-checks spec-sheet` inspects product specification markup, unit mentions, and PDF links in HTML. It does not read PDF contents. [README](components/spec-sheet/README.md)

<a id="saas-onboard"></a>

### saas-onboard

`seo-checks saas-onboard` checks indexing directives and canonical paths on a SaaS onboarding flow. `--deep` also checks discovered auth pages. [README](components/saas-onboard/README.md)

<a id="sws-skills"></a>

### sws-skills

`prompts/skills/` holds six Claude Code prompts: `anti-slop`, `cannibalize`, `content-refresh`, `meta-optimize`, `video-script`, and `web2md`. Copy a folder into `~/.claude/skills/` to use it. [README](prompts/README.md)
