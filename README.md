# Local business website audit CLI: gbp-audit

Gbp-audit checks public website markup for developers and local search teams. Use its LocalBusiness fields and visible page signals to select content for review.

[Project page](https://scalewithsearch.com/code/gbp-audit)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/gbp-audit
cd gbp-audit
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('local-page-audit')
print(tool["audit"]("LocalBusiness", {"name": "Example"}))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Run the local-page-audit command included in this repository.
- Check configured LocalBusiness types and field profiles.
- Look for visible contact details and an embedded map.

## Limits

- The tool does not connect to a Google Business Profile.
- Field profiles and page matching are project heuristics.
- A missing signal does not prove that business information is incorrect.

## Related repositories

- [citation-check](https://github.com/b2bvic/citation-check)
- [schema-health](https://github.com/b2bvic/schema-health)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 local-page-audit tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
