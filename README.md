# saas-onboard

SaaS onboarding flow SEO checker. Validates noindex on auth pages, SoftwareApplication schema, canonical handling, and marketing-to-app internal linking.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
saas-onboard https://example-saas.com
saas-onboard https://example-saas.com --deep    # Also checks discovered auth pages
```

## What It Checks

- Auth/app pages without noindex (login, signup, dashboard, settings)
- Canonical tag presence and correctness
- SoftwareApplication schema (offers, applicationCategory, rating)
- Internal link balance between marketing and app pages
- Auto-discovers auth page URLs from marketing site links

## Why It Matters

SaaS companies leak SEO equity when login/signup/dashboard pages get indexed. Google wastes crawl budget on auth pages and may dilute the marketing site's topical authority. This tool catches those issues before they compound.

## Install

```bash
curl -o ~/.local/bin/saas-onboard https://raw.githubusercontent.com/b2bvic/saas-onboard/main/saas-onboard
chmod +x ~/.local/bin/saas-onboard
```

## License

MIT
