# course-schema

Course/education schema.org validator. Checks Course, CourseInstance, and EducationalOrganization schema against Google's requirements for education rich results.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
course-schema https://example-university.com/program
```

## What It Checks

- Course: name, description, provider, courseCode, educationalLevel, offers
- CourseInstance: courseMode, startDate, endDate, instructor, courseWorkload
- EducationalOrganization: name, address, accreditation, department
- Tuition/price in offers schema
- Nested CourseInstance validation

## Install

```bash
curl -o ~/.local/bin/course-schema https://raw.githubusercontent.com/b2bvic/course-schema/main/course-schema
chmod +x ~/.local/bin/course-schema
```

## License

MIT
