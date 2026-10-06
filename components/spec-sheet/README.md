# Product specification SEO checker: spec-sheet

`spec-sheet` inspects product specification markup for developers and manufacturing content teams. Use its page findings to review technical content before editing it.

[Project page](https://scalewithsearch.com/code/seo-checks#spec-sheet)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd components/spec-sheet
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('spec-sheet')
print(tool["check_pdf_specs"](__import__("bs4").BeautifulSoup('<a href="spec.pdf">Technical specifications</a>', "lxml"), "https://example.com/product"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Identify PDF links with specification-like text or paths.
- Count specification-like terms, units, and tables in HTML.
- Check selected Product JSON-LD properties.

## Limits

- The tool does not read PDF contents.
- Keyword and unit matching are heuristics.
- It does not verify equipment specifications or search eligibility.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 spec-sheet tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
