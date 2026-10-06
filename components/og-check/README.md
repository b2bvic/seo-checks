# Open Graph meta tag checker: og-check

`og-check` extracts social metadata for developers and content teams. Use its field checklist to review sharing markup before publishing a page.

[Project page](https://scalewithsearch.com/code/seo-checks#og-check)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd components/og-check
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('og-check')
print(tool["audit"](tool["extract_meta"]('<meta property="og:title" content="Demo">')))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Extract Open Graph and Twitter Card fields.
- Report absent fields from project-defined lists.
- Flag long titles or descriptions and non-HTTP image locations.

## Limits

- The tool does not render social platform previews.
- It does not verify that image URLs are reachable.
- Field and length checks are project heuristics.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 og-check tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
