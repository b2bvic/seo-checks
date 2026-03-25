# schema-health

Healthcare schema.org validator. Checks MedicalBusiness, Physician, Dentist, Hospital, MedicalCondition, MedicalProcedure, and MedicalClinic schema against Google's requirements for healthcare rich results.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
schema-health https://example-clinic.com
schema-health https://example-clinic.com --json-output
```

## What It Checks

- MedicalBusiness: name, address, telephone, openingHours, medicalSpecialty
- Physician: name, medicalSpecialty, hospitalAffiliation
- MedicalCondition: associatedAnatomy, cause, possibleTreatment, signOrSymptom
- MedicalProcedure: bodyLocation, howPerformed, preparation, procedureType

## Install

```bash
curl -o ~/.local/bin/schema-health https://raw.githubusercontent.com/b2bvic/schema-health/main/schema-health
chmod +x ~/.local/bin/schema-health
```

## License

MIT
