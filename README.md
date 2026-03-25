# SWS Skills

AI agent skills for SEO, content production, and output quality. Works with Claude Code, Gemini CLI, Cursor, and any client supporting the [Agent Skills Standard](https://agentskills.io).

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Skills

| Skill | What it does |
|-------|-------------|
| **anti-slop** | AI output quality gate. Detect sycophancy, filler, hedging, and AI-marker vocabulary. 10 drift patterns with regex + calibration prompts. |
| **web2md** | Convert any URL to clean markdown. Strips nav, ads, footers. Preserves heading hierarchy. |
| **video-script** | Generate recording-ready video scripts with timing markers, shot lists, and thumbnail ideas. |
| **content-refresh** | Audit content freshness across 8 weighted signals. Score 0-100 with prioritized actions. |
| **meta-optimize** | Audit and optimize meta titles and descriptions with SERP competition analysis. |
| **cannibalize** | Detect keyword cannibalization. Weighted overlap scoring, cluster analysis, merge/differentiate/redirect recommendations. |

## Install

### Claude Code

Add this marketplace to your Claude Code installation:

```bash
# Clone the repo
git clone https://github.com/b2bvic/sws-skills.git ~/.claude/skills/sws-skills

# Or copy individual skills
cp -r sws-skills/skills/anti-slop ~/.claude/skills/
```

### Other AI Clients

Copy the `skills/` directory to your client's skills location. See [Agent Skills Standard](https://agentskills.io) for client-specific paths.

## Usage

Once installed, use the skills as slash commands:

```
/anti-slop          — Check AI output for drift patterns
/web2md <url>       — Convert page to markdown
/video-script       — Generate a video script
/content-refresh    — Audit content freshness
/meta-optimize      — Optimize meta tags
/cannibalize        — Find keyword cannibalization
```

## License

MIT
