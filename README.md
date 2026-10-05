# HTTP redirect chain tracer: redirect-trace

Redirect-trace records HTTP redirect hops for search teams and developers. Use its loop and downgrade reports to inspect routing problems before changing redirects.

[Project page](https://scalewithsearch.com/code/redirect-trace)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/redirect-trace
cd redirect-trace
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python redirect-trace --help
.venv/bin/python -m pytest -q
```

## How it works

- Send HEAD requests without automatic redirect handling.
- Resolve relative locations against the current URL.
- Stop after a repeated URL or twenty iterations.

## Limits

- Servers can handle HEAD and GET differently.
- The iteration cap can stop a chain before its final destination.
- Results describe observed responses, rather than browser navigation.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 redirect-trace tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
