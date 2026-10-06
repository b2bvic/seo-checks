# Restaurant menu SEO checker: menu-seo

`menu-seo` inspects restaurant page markup for developers and content teams. Use its HTML findings to select menu content for review.

[Project page](https://scalewithsearch.com/code/seo-checks#menu-seo)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd components/menu-seo
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('menu-seo')
print(tool["check_menu_accessibility"](__import__("bs4").BeautifulSoup('<a href="menu.pdf">Menu</a>', "lxml"), "https://example.com/menu")[0])
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Flag menu PDF links, menu images, and selected embedded ordering frames.
- Count dollar-denominated prices in visible text.
- Inspect Menu JSON-LD and match dietary label terms.

## Limits

- The tool does not read PDF or embedded frame contents.
- Price and dietary term matching are heuristics.
- Matched labels do not verify ingredients or dietary safety.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 menu-seo tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
