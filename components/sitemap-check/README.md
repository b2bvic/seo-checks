# XML sitemap validator CLI: sitemap-check

`sitemap-check` parses XML sitemaps for search teams and developers. Use its bounded URL checks to inspect crawl inputs before changing a website.

[Project page](https://scalewithsearch.com/code/seo-checks#sitemap-check)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd components/sitemap-check
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('sitemap-check')
print(tool["parse_sitemap"]("<broken", "https://example.com/sitemap.xml"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Parse namespaced URL sets and sitemap indexes.
- Fetch up to five child sitemaps from an index.
- Optionally send HEAD requests and report failures.

## Limits

- The parser does not validate every sitemap protocol rule.
- URL checks flag HTTP errors and request failures, rather than requiring exactly HTTP 200.
- Nested sitemap indexes are not followed recursively.

## Related repositories

- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 sitemap-check tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
