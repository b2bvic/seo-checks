# product-schema

Product page schema.org validator for e-commerce SEO. Checks Product, Offer, AggregateRating, Review, and BreadcrumbList schema completeness against Google's rich result requirements.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
product-schema https://example.com/product-page
product-schema https://example.com/product-page --json-output
```

## What It Checks

- Product: name, image, description, sku, brand, offers
- Offer: price, priceCurrency, availability, itemCondition
- AggregateRating: ratingValue, reviewCount
- Review: author, reviewRating

## Install

```bash
curl -o ~/.local/bin/product-schema https://raw.githubusercontent.com/b2bvic/product-schema/main/product-schema
chmod +x ~/.local/bin/product-schema
```

## License

MIT
