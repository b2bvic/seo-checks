# Image alt text checker CLI: alt-audit

`alt-audit` classifies image alt attributes for developers and search teams. Use its HTML findings to select images for accessibility review.

[Project page](https://scalewithsearch.com/code/seo-checks#alt-audit)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd components/alt-audit
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('alt-audit')
print(tool["audit_images"]('<img src="demo.png" alt="">', "https://example.com"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Distinguish missing, empty, generic, short, and long alt values.
- Report whether width and height attributes are present.
- Return image records as JSON when requested.

## Limits

- Empty alt text can be appropriate for decorative images.
- Length thresholds are project heuristics.
- The tool does not determine whether a description represents an image correctly.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 alt-audit tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
