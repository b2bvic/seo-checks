# hipaa-meta

HIPAA-safe meta tag auditor for healthcare websites. Scans for potential PHI (Protected Health Information) exposure in meta descriptions, image alt text, URL parameters, and review schema.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
hipaa-meta https://example-medical.com
hipaa-meta https://example-medical.com --json-output
```

## What It Detects

- Phone numbers in meta descriptions
- Email addresses in meta content
- SSN patterns anywhere in markup
- Date of birth patterns in meta tags
- Patient names in image alt text (near medical terms)
- PII in URL query parameters (patient, name, email, dob, ssn, mrn)
- Medical details alongside names in review schema

## Install

```bash
curl -o ~/.local/bin/hipaa-meta https://raw.githubusercontent.com/b2bvic/hipaa-meta/main/hipaa-meta
chmod +x ~/.local/bin/hipaa-meta
```

## License

MIT
