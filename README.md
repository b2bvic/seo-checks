# thin-product

Detect thin product pages on e-commerce sites. Fetches pages from a sitemap, counts unique content words (excluding boilerplate), flags pages under a configurable threshold.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
thin-product https://example.com/sitemap.xml
thin-product https://example.com/sitemap.xml --threshold 150
thin-product https://example.com/sitemap.xml --limit 50 --json-output
```

## Install

```bash
curl -o ~/.local/bin/thin-product https://raw.githubusercontent.com/b2bvic/thin-product/main/thin-product
chmod +x ~/.local/bin/thin-product
```

## License

MIT
