# HTML heading hierarchy checker: heading-audit

`heading-audit` inspects HTML heading structure for developers and search teams. Use its findings to review an outline before changing page markup.

[Project page](https://scalewithsearch.com/code/heading-audit)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/heading-audit
cd heading-audit
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('heading-audit')
print(tool["audit_headings"]("<h1>Start</h1><h3>Detail</h3>"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Collect H1 through H6 elements in document order.
- Report missing or repeated H1 elements.
- Flag skipped levels, empty headings, and an unexpected first heading.

## Limits

- The tool reads returned HTML without executing JavaScript.
- Its heading rules are a project checklist.
- Results do not establish accessibility conformance.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 heading-audit tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
