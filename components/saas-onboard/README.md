# SaaS website SEO checker: saas-onboard

`saas-onboard` inspects website markup for developers and software content teams. Use its page checks to review indexing directives and canonical paths.

[Project page](https://scalewithsearch.com/code/seo-checks#saas-onboard)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd components/saas-onboard
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('saas-onboard')
print(tool["check_noindex"]("<html></html>", "https://example.com/login")[0])
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Look for noindex metadata on URL paths that resemble authentication pages.
- Compare canonical URL paths.
- Inspect selected SoftwareApplication fields and optionally discover linked authentication pages.

## Limits

- URL matching is heuristic.
- The canonical comparison checks paths rather than full URL identity.
- Discovery can include external links, and returned HTML does not include JavaScript rendering.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 saas-onboard tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
