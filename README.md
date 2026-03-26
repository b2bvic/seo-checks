# redirect-trace

Redirect chain tracer. Follows every hop from origin to destination. Detects loops, chains, HTTP/HTTPS downgrades.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
redirect-trace https://example.com/old-page
```

## Install

```bash
curl -o ~/.local/bin/redirect-trace https://raw.githubusercontent.com/b2bvic/redirect-trace/main/redirect-trace
chmod +x ~/.local/bin/redirect-trace
```

## License

MIT
