# sitemap-check

Sitemap.xml validator and URL checker. Parses XML structure, handles sitemap indexes, optionally verifies each URL returns 200.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
sitemap-check https://example.com
sitemap-check https://example.com/sitemap.xml --check-urls
```

## Install

```bash
curl -o ~/.local/bin/sitemap-check https://raw.githubusercontent.com/b2bvic/sitemap-check/main/sitemap-check
chmod +x ~/.local/bin/sitemap-check
```

## License

MIT
