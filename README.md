# Robots.txt validator CLI: robots-check

Robots-check inspects robots.txt directives for developers and search teams. Use its findings to review crawler configuration before editing a website.

[Project page](https://scalewithsearch.com/code/robots-check)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/robots-check
cd robots-check
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('robots-check')
print(tool["parse_robots"]("User-agent: *\nDisallow: /\nSitemap: https://example.com/sitemap.xml"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Collect user-agent blocks and allow or disallow rules.
- Report sitemap directives.
- Flag malformed lines and a rule that blocks the entire site.

## Limits

- The parser does not implement complete crawler rule matching.
- Consecutive user-agent directives become separate blocks.
- A blocking rule can be intentional.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 robots-check tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
