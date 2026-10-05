# Sitemap thin content checker: thin-product

`thin-product` counts page words for developers and search teams. Use its sitemap sample to select low-content pages for review.

[Project page](https://scalewithsearch.com/code/thin-product)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/thin-product
cd thin-product
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('thin-product')
print(tool["count_content_words"]("<main>River river flows</main>"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Fetch a bounded set of sitemap URLs.
- Count visible words and case-normalized unique words.
- Report pages below the unique-word threshold alongside fetch failures.

## Limits

- The tool does not classify product pages.
- Navigation removal and word counting are heuristics.
- Review fetch failures separately from low-content findings.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 thin-product tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
