# hipaa-meta

A command-line heuristic that flags possible identifiers in healthcare-page
metadata for human privacy review.

This is not a HIPAA compliance tool, legal opinion, PHI determination, or
substitute for review by qualified privacy and security professionals.

## Principle cluster

This repository demonstrates **P06 (evidence outranks fluency)** and **P09
(agency is governed)** because it reports the exact pattern and location that
triggered review without claiming that a regex match proves a HIPAA violation.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
./hipaa-meta https://example.com
```

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
