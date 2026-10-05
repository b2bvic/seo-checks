# Healthcare metadata privacy review tool: hipaa-meta

Hipaa-meta flags possible identifiers for developers and healthcare content reviewers. Use its HTML findings to select metadata for human privacy review.

[Project page](https://scalewithsearch.com/code/hipaa-meta)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/hipaa-meta
cd hipaa-meta
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('hipaa-meta')
print(tool["check_meta_tags"](__import__("bs4").BeautifulSoup('<meta name="description" content="demo@example.com">', "lxml"), "https://example.com"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Match identifier patterns in metadata and image alt text.
- Check selected URL query parameter names.
- Inspect review JSON-LD for configured identifier patterns.

## Limits

- Pattern matches can produce false positives or miss identifiers.
- The tool makes no compliance or legal determination.
- Returned findings can contain sensitive source text.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 hipaa-meta tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
