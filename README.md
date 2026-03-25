# spec-sheet

Technical spec sheet SEO analyzer for manufacturing websites. Detects whether product specs are crawlable HTML or trapped in downloadable PDFs. Validates Product schema with technical properties.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
spec-sheet https://example-manufacturer.com/products/widget-500
```

## What It Checks

- PDF spec sheets linked from page (specs Google can't index)
- HTML spec content: keyword count, unit measurements, spec tables
- Product schema with additionalProperty, material, manufacturer, weight

## Why It Matters

Manufacturing companies often have extensive spec sheets — tolerances, dimensions, materials, certifications — locked inside PDFs. Google can't reliably extract that data for search results. An HTML version of the same specs makes them indexable, linkable, and eligible for rich results.

## Install

```bash
curl -o ~/.local/bin/spec-sheet https://raw.githubusercontent.com/b2bvic/spec-sheet/main/spec-sheet
chmod +x ~/.local/bin/spec-sheet
```

## License

MIT
