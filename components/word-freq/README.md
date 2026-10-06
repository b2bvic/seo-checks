# Word frequency analyzer CLI: word-freq

`word-freq` counts filtered tokens for writers and search teams. Use its term and phrase reports to inspect repetition in content.

[Project page](https://scalewithsearch.com/code/word-freq)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/word-freq
cd word-freq
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python - <<'PY'
import runpy
tool = runpy.run_path('word-freq')
print(tool["ngrams"](tool["tokenize"]("The river and the river flow."), 2))
PY
```

This example uses synthetic input without fetching a website.

## How it works

- Read text files or extract text from HTML.
- Remove stop words before counting terms.
- Build bigrams and trigrams from the filtered token sequence.

## Limits

- Density uses the filtered token count.
- Phrase terms can span words removed from the original text.
- Token matching is limited to lowercase English letters.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 word-freq tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
