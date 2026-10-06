# Course JSON-LD checklist CLI: course-schema

`course-schema` checks Course and ItemList JSON-LD for developers and education content teams. Use its field profiles to select markup for review.

[Project page](https://scalewithsearch.com/code/course-schema)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/course-schema
cd course-schema
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('course-schema')
print(tool["audit_course"]({"name": "Demo", "description": "Example"}, "Course"))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Inspect Course name and description fields.
- Check list length, positions, and unique URLs.
- Report optional schema.org fields separately.

## Limits

- The field profiles are a repository snapshot.
- A passing checklist does not establish current search-engine eligibility.
- Linked course detail pages are not fetched by the list checker.

## Related repositories

- [product-schema](https://github.com/b2bvic/product-schema)
- [schema-health](https://github.com/b2bvic/schema-health)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 course-schema tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
