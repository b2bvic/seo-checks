# link-suggest

A command-line assistant for finding candidate anchor phrases in an article.

The tool downloads the external `dejanseo/google-links` model, which is roughly
1.2 GB. The model name does not establish how its training corpus was built.
Treat every suggestion as a candidate for review.

## Principle cluster

This repository demonstrates **P04 (synthesis starts from sources)** and **P06 (evidence outranks fluency)** because it maps token predictions back to word spans and merges adjacent candidate tokens.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
python suggest_links.py --file article.md
```

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
