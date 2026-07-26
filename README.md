# course-schema

A command-line checker for Google Course-list markup and schema.org Course
completeness.

The Google check requires a page-level `ItemList` with at least three
`ListItem` entries, positions, unique URLs, and Course `name` and `description`
where Course data is present. `provider` is reported as recommended. Other
schema.org fields are reported separately and do not affect the Google contract.

## Principle cluster

This repository demonstrates **P06 (evidence outranks fluency)** and **P14
(authority is structured coverage over time)** because it separates Google's
documented Course-list contract from optional schema.org completeness fields.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
./course-schema https://example.com/course
```

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
