# citation-check

Local business citation consistency checker. Searches major directories for your business and flags NAP (Name, Address, Phone) inconsistencies that hurt local SEO rankings.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
citation-check --name "Example Dental" --city "Raleigh NC"
citation-check --name "Example Dental" --city "Raleigh NC" --phone "9195551234" --address "123 Main St"
citation-check --name "Example Dental" --city "Raleigh NC" --json-output
```

## Directories Checked

- Yelp
- BBB
- Yellow Pages

## Install

```bash
curl -o ~/.local/bin/citation-check https://raw.githubusercontent.com/b2bvic/citation-check/main/citation-check
chmod +x ~/.local/bin/citation-check
```

## License

MIT
