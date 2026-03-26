# internal-link-audit

Find orphan pages and analyze internal link structure. Crawls from sitemap, counts inbound links per page, reports distribution.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
internal-link-audit https://example.com/sitemap.xml
internal-link-audit https://example.com/sitemap.xml --limit 100
```

## Install

```bash
curl -o ~/.local/bin/internal-link-audit https://raw.githubusercontent.com/b2bvic/internal-link-audit/main/internal-link-audit
chmod +x ~/.local/bin/internal-link-audit
```

## License

MIT
