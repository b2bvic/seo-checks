# Product JSON-LD field checker: product-schema

Product-schema checks Product JSON-LD fields for developers and search teams. Use its checklist to review structured data before changing product pages.

[Project page](https://scalewithsearch.com/code/product-schema)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/product-schema
cd product-schema
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('product-schema')
print(tool["audit_product"]({"@type": "Product", "name": "Demo"}))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Find Product objects, including objects inside a graph.
- Check product, offer, rating, and review fields.
- Calculate a project-defined completeness score.

## Limits

- The score does not establish search-engine eligibility.
- The parser expects conventional object shapes.
- Field presence does not verify that values represent the product correctly.

## Related repositories

- [course-schema](https://github.com/b2bvic/course-schema)
- [schema-health](https://github.com/b2bvic/schema-health)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 product-schema tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
