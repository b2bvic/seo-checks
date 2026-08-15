# thin-product

A command-line checker for low-content sitemap URLs.

The tool does not detect page type or Product markup. It evaluates every URL in
the supplied sitemap. Fetch failures are reported with the low-content results,
so review those failures separately.

## Principle cluster

This repository demonstrates **P06 (evidence outranks fluency)** and **P14 (authority is structured coverage over time)** because it reads URLs from a sitemap and compares unique-word counts against a threshold.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
./thin-product https://example.com/sitemap.xml
```

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
