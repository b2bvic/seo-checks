# Internal link anchor text suggestions: link-suggest

Link-suggest generates anchor candidates for editors and search teams. Use its token-classification output to select possible internal links for review.

[Project page](https://scalewithsearch.com/code/link-suggest)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/link-suggest
cd link-suggest
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

Install the pinned runtime libraries before using the CLI.

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Quick start

```bash
.venv/bin/python suggest_links.py --help
printf '' | .venv/bin/python suggest_links.py
```

Empty input returns JSON without loading model weights.

## How it works

- Load the configured token-classification model on demand.
- Convert predicted token spans into candidate anchor phrases.
- Optionally match candidates against sitemap URL text.

## Limits

- Analysis downloads model weights when they are absent.
- Suggestions do not prove relevance or establish a search-engine recommendation.
- CI covers preprocessing and syntax rather than model predictions.

## Related repositories

- [sitemap-check](https://github.com/b2bvic/sitemap-check)
- [redirect-trace](https://github.com/b2bvic/redirect-trace)
- [internal-link-audit](https://github.com/b2bvic/internal-link-audit)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 suggest_links.py tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
