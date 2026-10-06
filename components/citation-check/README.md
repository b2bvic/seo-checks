# Local citation search link generator: citation-check

`citation-check` generates directory search links for local search teams. Use those links to inspect listings and compare business details manually.

[Project page](https://scalewithsearch.com/code/seo-checks#citation-check)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd components/citation-check
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python directory-search-links --name "Example business" --city "Example City" --json-output
```

The command generates links without fetching directory listings.

## How it works

- Run the directory-search-links command included in this repository.
- Encode supplied business and location terms into directory URLs.
- Label each link as requiring manual review.

## Limits

- The tool does not open or inspect directory listings.
- A generated link does not prove that a listing exists.
- Supplied contact details are not independently verified.

## Related repositories

- [gbp-audit](https://github.com/b2bvic/gbp-audit)
- [schema-health](https://github.com/b2bvic/schema-health)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 directory-search-links tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
