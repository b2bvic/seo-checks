# gbp-audit

Google Business Profile schema auditor. Validates LocalBusiness schema completeness plus on-page signals (visible phone, address, map embed) that affect local search rankings.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
gbp-audit https://example-business.com
```

## What It Checks

**Schema:** LocalBusiness + 25 subtypes (Restaurant, Dentist, RealEstateAgent, etc.)
- Required: name, address, telephone
- Recommended: openingHours, geo, image, priceRange, review, aggregateRating
- Address completeness (street, city, state, zip)
- Geo coordinates (latitude/longitude)

**Page signals:**
- Google Maps embed present
- Phone number visible on page
- Physical address visible on page

## Install

```bash
curl -o ~/.local/bin/gbp-audit https://raw.githubusercontent.com/b2bvic/gbp-audit/main/gbp-audit
chmod +x ~/.local/bin/gbp-audit
```

## License

MIT
