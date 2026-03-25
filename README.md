# menu-seo

Restaurant menu SEO analyzer. Checks whether menu items are crawlable text (not trapped in PDFs or images), validates Menu/MenuItem schema, and audits pricing and dietary labels.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
menu-seo https://example-restaurant.com/menu
```

## What It Checks

- PDF menus (not indexable by Google)
- Menu images without alt text
- iframe menus (third-party ordering widgets)
- Visible price count as crawlable text
- Menu/MenuItem/Restaurant schema completeness
- servesCuisine property
- Dietary labels (vegan, gluten-free, halal, etc.)

## Install

```bash
curl -o ~/.local/bin/menu-seo https://raw.githubusercontent.com/b2bvic/menu-seo/main/menu-seo
chmod +x ~/.local/bin/menu-seo
```

## License

MIT
