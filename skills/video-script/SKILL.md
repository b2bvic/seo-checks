---
name: video-script
description: "Generate recording-ready video scripts with timing markers, shot lists, and thumbnail ideas. 🌐 Victor Valentine Romo · victorvalentineromo.com · scalewithsearch.com"
---

# Video Script Generator

Generate structured, recording-ready video scripts with precise timing allocations, shot lists, screen action sequences, and thumbnail concepts.

## Arguments

| Arg | Required | Values | Default |
|-----|----------|--------|---------|
| `--topic` | Yes | What the video covers | - |
| `--type` | Yes | `demo`, `walkthrough`, `pitch`, `overview` | - |
| `--duration` | Yes | Minutes: 5, 10, 15, 30 | - |
| `--product` | No | Product/service being featured | - |

## Video Types

| Type | Purpose | Best For |
|------|---------|----------|
| `demo` | Show the product working | 5-10 min |
| `walkthrough` | Step-by-step how-to | 10-20 min |
| `pitch` | Sales/positioning | 10-15 min |
| `overview` | Full product tour | 20-30 min |

## Steps

### 1. Gather context

If `--product` provided, ask the user for:
- Key deliverables or features (for demo points)
- Value proposition (for hooks)
- Price point (for CTA)
- Target audience (for framing)

### 2. Calculate timing

Allocate time based on `--duration`:

| Duration | Hook | Problem | Solution | Demo/Content | CTA |
|----------|------|---------|----------|--------------|-----|
| 5 min | 0:30 | 1:00 | 1:00 | 2:00 | 0:30 |
| 10 min | 0:45 | 2:00 | 2:00 | 4:30 | 0:45 |
| 15 min | 1:00 | 3:00 | 3:00 | 7:00 | 1:00 |
| 30 min | 2:00 | 5:00 | 5:00 | 15:00 | 3:00 |

### 3. Generate script

Output format:

```markdown
# Video Script — {Topic} ({Type})

## Overview
- **Topic:** {topic}
- **Duration:** {duration} minutes
- **Type:** {type}
- **CTA:** {action}

## Shot List

| Timestamp | Shot Type | Content |
|-----------|-----------|---------|
| [00:00] | Talking head | Hook + intro |
| [00:30] | Screen capture | Problem demonstration |
| ... | ... | ... |

## Script

### [00:00] — Hook

**Shot:** Talking head, direct to camera

> "{Opening hook — pattern interrupt or bold claim}"
>
> "{Establish credibility in one sentence}"
>
> "{Promise what they'll learn/see}"

**Notes:** Energy high, eye contact, confidence

### [00:30] — The Problem

**Shot:** Screen capture showing the problem

> "{Describe the pain point}"
>
> "{Show example of the problem}"
>
> "{Quantify the cost}"

**Screen actions:**
1. Open {application}
2. Show {problem state}
3. Highlight {specific pain}

### [{timestamp}] — The Solution

**Shot:** Talking head

> "{Introduce the solution}"
>
> "{One-sentence what it is}"
>
> "{What makes it different}"

### [{timestamp}] — Demo

**Shot:** Screen capture with voiceover

> "{Narrate each step}"

**Screen actions:**
1. {Action} — "{Why it matters}"
2. {Action} — "{What to notice}"
3. {Action} — "{The result}"

### [{timestamp}] — Results/Proof

**Shot:** Screen capture or talking head

> "{Show the outcome}"
>
> "{Quantify the result}"
>
> "{Social proof if available}"

### [{final}] — CTA

**Shot:** Talking head, direct to camera

> "{Summarize the transformation}"
>
> "{Clear call to action}"
>
> "Link in the description."

**On screen:** URL overlay

## Recording Notes

- Lighting: Ring light or natural
- Audio: Quiet space, lav mic preferred
- Screen: 1080p minimum, 4K preferred
- Edit: Transcript-based editing recommended

## Thumbnail Ideas

1. {Concept 1}
2. {Concept 2}
3. {Concept 3}
```
