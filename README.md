# SEO checks

Use `seo-checks` to run twenty Python tools for sitemaps, metadata, content, links, and structured data.
You also get six Markdown prompts for content workflows in `prompts/`.
Each component keeps its source code, tests, license, and full Git history.

[Project page](https://scalewithsearch.com/code/seo-checks)

## Install

Use Python 3.11 or later. The dispatcher uses the Python standard library.
The normal tools require Click, Requests, Beautiful Soup, lxml, and certifi.
The package install includes those libraries. Model libraries remain optional.

```bash
git clone https://github.com/b2bvic/seo-checks.git
cd seo-checks
python3 -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/seo-checks --help
```

For development, use `.venv/bin/python -m pip install -e ".[dev]"`.
You can also run `.venv/bin/python seo_checks.py <subcommand> [args]` from this checkout.
Installed wheels include component scripts and prompt files under your environment's `share/seo-checks/` directory.

## Quick start

List the available commands and inspect component options:

```bash
.venv/bin/seo-checks robots --help
.venv/bin/seo-checks redirects --help
.venv/bin/seo-checks schema-product --help
```

Generate review links without fetching a website:

```bash
.venv/bin/seo-checks citations --name "Example business" --city "Example City" --json-output
```

Analyze a local text file:

```bash
.venv/bin/seo-checks readability article.txt --json-output
.venv/bin/seo-checks word-freq article.txt --top 10 --json-output
```

Pass arguments after the subcommand exactly as you would to the component.
The dispatcher preserves standard input, output, exit status, and your current directory.
URL checks can fetch public pages. Use `--help` to inspect crawl limits before running them.

## Components

| Command | Source component | Entry file | Purpose |
| --- | --- | --- | --- |
| `sitemap` | [sitemap-check](components/sitemap-check/README.md) | `sitemap-check` | Parse XML sitemaps and optionally check URLs. |
| `robots` | [robots-check](components/robots-check/README.md) | `robots-check` | Inspect robots.txt directives and blocking rules. |
| `redirects` | [redirect-trace](components/redirect-trace/README.md) | `redirect-trace` | Trace HTTP redirects, loops, and HTTPS downgrades. |
| `headings` | [heading-audit](components/heading-audit/README.md) | `heading-audit` | Check HTML heading order and empty headings. |
| `alt` | [alt-audit](components/alt-audit/README.md) | `alt-audit` | Classify image alt text and dimension attributes. |
| `og` | [og-check](components/og-check/README.md) | `og-check` | Check Open Graph and Twitter Card metadata. |
| `readability` | [readability](components/readability/README.md) | `readability` | Estimate Flesch readability from a URL or file. |
| `word-freq` | [word-freq](components/word-freq/README.md) | `word-freq` | Count filtered words and phrases in a URL or file. |
| `internal-links` | [internal-link-audit](components/internal-link-audit/README.md) | `internal-link-audit` | Count internal links in a bounded sitemap crawl. |
| `thin-product` | [thin-product](components/thin-product/README.md) | `thin-product` | Find sampled pages below a unique-word threshold. |
| `link-suggest` | [link-suggest](components/link-suggest/README.md) | `suggest_links.py` | Suggest anchor phrases with an optional downloaded model. |
| `citations` | [citation-check](components/citation-check/README.md) | `directory-search-links` | Generate directory search links for manual review. |
| `gbp` | [gbp-audit](components/gbp-audit/README.md) | `local-page-audit` | Check public local-business website markup. |
| `schema-product` | [product-schema](components/product-schema/README.md) | `product-schema` | Check Product JSON-LD fields. |
| `schema-course` | [course-schema](components/course-schema/README.md) | `course-schema` | Check Course and ItemList JSON-LD fields. |
| `schema-health` | [schema-health](components/schema-health/README.md) | `schema-health` | Check configured healthcare JSON-LD field profiles. |
| `hipaa-meta` | [hipaa-meta](components/hipaa-meta/README.md) | `hipaa-meta` | Flag possible identifiers in metadata for human review. |
| `menu` | [menu-seo](components/menu-seo/README.md) | `menu-seo` | Inspect restaurant menu markup and visible prices. |
| `spec-sheet` | [spec-sheet](components/spec-sheet/README.md) | `spec-sheet` | Inspect product specification markup and PDF links. |
| `saas-onboard` | [saas-onboard](components/saas-onboard/README.md) | `saas-onboard` | Check SaaS indexing directives and canonical paths. |
| Prompts only | [sws-skills](prompts/README.md) | `prompts/skills/*/SKILL.md` | Six content workflow prompts. |

## Optional link model

You can use every normal tool without the link model or its ML libraries.
`seo-checks link-suggest --help` reads the component's argument parser without importing those libraries.
For analysis, install the optional runtime:

```bash
.venv/bin/python -m pip install ".[link-suggest]"
.venv/bin/seo-checks link-suggest --file article.md
```

The component downloads `dejanseo/google-links` model weights on the first analysis of nonempty text.
Its setup script estimates a download of about 1.2 GB. Download size can vary.
Set a cache path if you want weights to stay in the checkout:

```bash
export HF_HOME="$PWD/.model-cache"
.venv/bin/seo-checks link-suggest --file article.md --format table
```

The portable component tests cover preprocessing and syntax. They do not download weights or test predictions.

## Test

Install the development dependencies, then run the dispatcher tests and all twenty-one imported suites:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/test_components.py
```

The component runner runs each suite from its imported folder.
It saves commands, counts, pytest XML, and logs in `.test-results/`.
If test dependencies are missing, it records the suite as skipped with the reason and the number of tests not run.
A failed suite makes the runner exit with status one. Review `summary.json` for skipped suites.

## Model assistance

Codex prepared this rollup's dispatcher, packaging, tests, and documentation.
The imported READMEs retain their model references and disclosures.
`sws-skills` contains Markdown prompts for content teams using Claude Code.
These are patterns a team can adapt for hosted-model writing and search workflows.
Generated findings need human review.
`link-suggest` loads the configured token-classification model on demand.
Analysis downloads model weights when they are absent.
Suggestions do not prove relevance or establish a search-engine recommendation.

## License

All twenty-one imported repositories use MIT licenses with the same copyright holder.
The top-level [LICENSE](LICENSE) and each imported license remain available.
The optional downloaded model has separate upstream terms. Review its model card before using the weights.

## Component details

<a id="sitemap-check"></a>

### sitemap-check

`sitemap-check` parses XML sitemaps for search teams and developers. Use its bounded URL checks to inspect crawl inputs before changing a website.

Run `seo-checks sitemap --help` to inspect its options.

- The parser does not validate every sitemap protocol rule.
- URL checks flag HTTP errors and request failures, rather than requiring exactly HTTP 200.
- Nested sitemap indexes are not followed recursively.

See the [component README](components/sitemap-check/README.md) for setup, examples, and tests.

<a id="robots-check"></a>

### robots-check

`robots-check` inspects robots.txt directives for developers and search teams. Use its findings to review crawler configuration before editing a website.

Run `seo-checks robots --help` to inspect its options.

- The parser does not implement complete crawler rule matching.
- Consecutive user-agent directives become separate blocks.
- A blocking rule can be intentional.

See the [component README](components/robots-check/README.md) for setup, examples, and tests.

<a id="redirect-trace"></a>

### redirect-trace

`redirect-trace` records HTTP redirect hops for search teams and developers. Use its loop and downgrade reports to inspect routing problems before changing redirects.

Run `seo-checks redirects --help` to inspect its options.

- Servers can handle HEAD and GET differently.
- The iteration cap can stop a chain before its final destination.
- Results describe observed responses, rather than browser navigation.

See the [component README](components/redirect-trace/README.md) for setup, examples, and tests.

<a id="heading-audit"></a>

### heading-audit

`heading-audit` inspects HTML heading structure for developers and search teams. Use its findings to review an outline before changing page markup.

Run `seo-checks headings --help` to inspect its options.

- The tool reads returned HTML without executing JavaScript.
- Its heading rules are a project checklist.
- Results do not establish accessibility conformance.

See the [component README](components/heading-audit/README.md) for setup, examples, and tests.

<a id="alt-audit"></a>

### alt-audit

`alt-audit` classifies image alt attributes for developers and search teams. Use its HTML findings to select images for accessibility review.

Run `seo-checks alt --help` to inspect its options.

- Empty alt text can be appropriate for decorative images.
- Length thresholds are project heuristics.
- The tool does not determine whether a description represents an image correctly.

See the [component README](components/alt-audit/README.md) for setup, examples, and tests.

<a id="og-check"></a>

### og-check

`og-check` extracts social metadata for developers and content teams. Use its field checklist to review sharing markup before publishing a page.

Run `seo-checks og --help` to inspect its options.

- The tool does not render social platform previews.
- It does not verify that image URLs are reachable.
- Field and length checks are project heuristics.

See the [component README](components/og-check/README.md) for setup, examples, and tests.

<a id="readability"></a>

### readability

`readability` estimates reading difficulty for writers and search teams. Use its text statistics to find passages that need editorial review.

Run `seo-checks readability --help` to inspect its options.

- Syllable counts are heuristic.
- Sentence counting excludes fragments with two words or fewer.
- Scores do not measure factual accuracy or writing quality.

See the [component README](components/readability/README.md) for setup, examples, and tests.

<a id="word-freq"></a>

### word-freq

`word-freq` counts filtered tokens for writers and search teams. Use its term and phrase reports to inspect repetition in content.

Run `seo-checks word-freq --help` to inspect its options.

- Density uses the filtered token count.
- Phrase terms can span words removed from the original text.
- Token matching is limited to lowercase English letters.

See the [component README](components/word-freq/README.md) for setup, examples, and tests.

<a id="internal-link-audit"></a>

### internal-link-audit

`internal-link-audit` counts observed links for developers and search teams. Use its bounded sitemap crawl to find pages that need link review.

Run `seo-checks internal-links --help` to inspect its options.

- A sampled orphan is not proof of a site-wide orphan.
- Failed page fetches are skipped.
- Normalization removes query strings, fragments, and trailing slashes.

See the [component README](components/internal-link-audit/README.md) for setup, examples, and tests.

<a id="thin-product"></a>

### thin-product

`thin-product` counts page words for developers and search teams. Use its sitemap sample to select low-content pages for review.

Run `seo-checks thin-product --help` to inspect its options.

- The tool does not classify product pages.
- Navigation removal and word counting are heuristics.
- Review fetch failures separately from low-content findings.

See the [component README](components/thin-product/README.md) for setup, examples, and tests.

<a id="link-suggest"></a>

### link-suggest

`link-suggest` generates anchor candidates for editors and search teams. Use its token-classification output to select possible internal links for review.

Run `seo-checks link-suggest --help` to inspect its options.

- Analysis downloads model weights when they are absent.
- Suggestions do not prove relevance or establish a search-engine recommendation.
- CI covers preprocessing and syntax rather than model predictions.

See the [component README](components/link-suggest/README.md) for setup, examples, and tests.

<a id="citation-check"></a>

### citation-check

`citation-check` generates directory search links for local search teams. Use those links to inspect listings and compare business details manually.

Run `seo-checks citations --help` to inspect its options.

- The tool does not open or inspect directory listings.
- A generated link does not prove that a listing exists.
- Supplied contact details are not independently verified.

See the [component README](components/citation-check/README.md) for setup, examples, and tests.

<a id="gbp-audit"></a>

### gbp-audit

`gbp-audit` checks public website markup for developers and local search teams. Use its LocalBusiness fields and visible page signals to select content for review.

Run `seo-checks gbp --help` to inspect its options.

- The tool does not connect to a Google Business Profile.
- Field profiles and page matching are project heuristics.
- A missing signal does not prove that business information is incorrect.

See the [component README](components/gbp-audit/README.md) for setup, examples, and tests.

<a id="product-schema"></a>

### product-schema

`product-schema` checks Product JSON-LD fields for developers and search teams. Use its checklist to review structured data before changing product pages.

Run `seo-checks schema-product --help` to inspect its options.

- The score does not establish search-engine eligibility.
- The parser expects conventional object shapes.
- Field presence does not verify that values represent the product correctly.

See the [component README](components/product-schema/README.md) for setup, examples, and tests.

<a id="course-schema"></a>

### course-schema

`course-schema` checks Course and ItemList JSON-LD for developers and education content teams. Use its field profiles to select markup for review.

Run `seo-checks schema-course --help` to inspect its options.

- The field profiles are a repository snapshot.
- A passing checklist does not establish current search-engine eligibility.
- Linked course detail pages are not fetched by the list checker.

See the [component README](components/course-schema/README.md) for setup, examples, and tests.

<a id="schema-health"></a>

### schema-health

`schema-health` checks selected healthcare JSON-LD types for developers and content teams. Use its field profiles to inspect missing structured data.

Run `seo-checks schema-health --help` to inspect its options.

- Field profiles are project-defined.
- Results do not establish search-engine eligibility.
- The tool does not validate medical content.

See the [component README](components/schema-health/README.md) for setup, examples, and tests.

<a id="hipaa-meta"></a>

### hipaa-meta

`hipaa-meta` flags possible identifiers for developers and healthcare content reviewers. Use its HTML findings to select metadata for human privacy review.

Run `seo-checks hipaa-meta --help` to inspect its options.

- Pattern matches can produce false positives or miss identifiers.
- The tool makes no compliance or legal determination.
- Returned findings can contain sensitive source text.

See the [component README](components/hipaa-meta/README.md) for setup, examples, and tests.

<a id="menu-seo"></a>

### menu-seo

`menu-seo` inspects restaurant page markup for developers and content teams. Use its HTML findings to select menu content for review.

Run `seo-checks menu --help` to inspect its options.

- The tool does not read PDF or embedded frame contents.
- Price and dietary term matching are heuristics.
- Matched labels do not verify ingredients or dietary safety.

See the [component README](components/menu-seo/README.md) for setup, examples, and tests.

<a id="spec-sheet"></a>

### spec-sheet

`spec-sheet` inspects product specification markup for developers and manufacturing content teams. Use its page findings to review technical content before editing it.

Run `seo-checks spec-sheet --help` to inspect its options.

- The tool does not read PDF contents.
- Keyword and unit matching are heuristics.
- It does not verify equipment specifications or search eligibility.

See the [component README](components/spec-sheet/README.md) for setup, examples, and tests.

<a id="saas-onboard"></a>

### saas-onboard

`saas-onboard` inspects website markup for developers and software content teams. Use its page checks to review indexing directives and canonical paths.

Run `seo-checks saas-onboard --help` to inspect its options.

- URL matching is heuristic.
- The canonical comparison checks paths rather than full URL identity.
- Discovery can include external links, and returned HTML does not include JavaScript rendering.

See the [component README](components/saas-onboard/README.md) for setup, examples, and tests.

<a id="sws-skills"></a>

### sws-skills

`sws-skills` contains Markdown prompts for content teams using Claude Code. These are patterns a team can adapt for hosted-model writing and search workflows.

Read the six prompts in `prompts/skills/`. These files contain instructions rather than an automated SEO runtime.

- The repository contains instructions rather than an automated SEO runtime.
- Skills require the tools and source access named in each prompt.
- Generated findings need human review.

See the [component README](prompts/README.md) for setup, examples, and tests.
