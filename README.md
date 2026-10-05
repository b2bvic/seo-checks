# Internal link audit CLI: internal-link-audit

Internal-link-audit counts observed links for developers and search teams. Use its bounded sitemap crawl to find pages that need link review.

[Project page](https://scalewithsearch.com/code/internal-link-audit)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/internal-link-audit
cd internal-link-audit
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('internal-link-audit')
print(tool["normalize_url"]("https://example.com/page/#section", "example.com"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Read a bounded set of sitemap URLs.
- Count observed internal inbound links.
- Report sitemap pages with no inbound links in the sampled crawl.

## Limits

- A sampled orphan is not proof of a site-wide orphan.
- Failed page fetches are skipped.
- Normalization removes query strings, fragments, and trailing slashes.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 internal-link-audit tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
