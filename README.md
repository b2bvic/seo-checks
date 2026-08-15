# word-freq

A command-line word-frequency and phrase-frequency analyzer.

## Principle cluster

This repository demonstrates **P06 (evidence outranks fluency)** because it tokenizes source text, removes stop words, and counts the remaining terms.

Bigrams and trigrams are built after stop-word removal. Their terms might not
have been adjacent in the original source. Density uses the filtered token
count, not the full word count.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
./word-freq article.md
```

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
