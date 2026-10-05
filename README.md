# Healthcare JSON-LD field checker: schema-health

Schema-health checks selected healthcare JSON-LD types for developers and content teams. Use its field profiles to inspect missing structured data.

[Project page](https://scalewithsearch.com/code/schema-health)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/schema-health
cd schema-health
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('schema-health')
print(tool["audit"]("MedicalCondition", {"name": "Demo"}))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Recognize configured medical and healthcare types.
- Apply baseline and additional field lists.
- Map configured aliases to their field profiles.

## Limits

- Field profiles are project-defined.
- Results do not establish search-engine eligibility.
- The tool does not validate medical content.

## Related repositories

- [product-schema](https://github.com/b2bvic/product-schema)
- [course-schema](https://github.com/b2bvic/course-schema)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 schema-health tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
