# schema-health

A command-line schema.org completeness linter for selected health-related
types. It uses a project-defined baseline and additional-field profile.

It does not test Google rich-result eligibility. Google does not document
`Physician`, `MedicalCondition`, or `MedicalProcedure` as supported Search
rich-result types.

## Principle cluster

This repository demonstrates **P06 (evidence outranks fluency)** and **P14
(authority is structured coverage over time)** because it reports which
configured schema.org fields are present without turning that lint profile into
a Search eligibility claim.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
./schema-health https://example.com
```

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
