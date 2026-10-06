# Flesch readability scorer CLI: readability

`readability` estimates reading difficulty for writers and search teams. Use its text statistics to find passages that need editorial review.

[Project page](https://scalewithsearch.com/code/seo-checks#readability)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/seo-checks
cd seo-checks
cd components/readability
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('readability')
print(tool["analyze"]("The cat sat. The dog ran."))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Extract text from HTML or read a local file.
- Estimate syllables with a vowel-group heuristic.
- Calculate Flesch Reading Ease and Flesch-Kincaid grade estimates.

## Limits

- Syllable counts are heuristic.
- Sentence counting excludes fragments with two words or fewer.
- Scores do not measure factual accuracy or writing quality.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 readability tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
