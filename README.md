# exploration

An agent skill that steers open-ended creative work with real randomness, so results escape the same predictable defaults.

**[See the landing page →](https://bgarcia7.github.io/exploration/)**

Asked to "be creative," a model reaches for the same palettes, architectures, campaign angles and story beats every time. This skill generates a random seed in the shell, reads it for patterns, turns those into a concrete direction for whatever is genuinely open in the task, and then builds that direction with full craft. Your fixed requirements are never touched.

It includes guides for design, architecture, marketing, idea generation, writing and editing, naming, research, and media. It can make several variants and compare them.

Works with any agent that supports the open [Agent Skills](https://agentskills.io) format, including Claude Code, Claude.ai, Codex, Cursor and others.

## Install

**With the skills CLI (any agent):**

```bash
npx skills add bgarcia7/exploration
```

Add `-g` to install it for all your projects instead of the current one. The CLI needs Node 22 or newer.

**Manually:** copy `skills/exploration` into your agent's skills folder, for example `~/.claude/skills/` for Claude Code.

**Claude.ai or the Claude desktop app:** download `exploration.zip` from the [latest release](https://github.com/bgarcia7/exploration/releases/latest) and upload it under Skills in Claude's settings. Code execution needs to be on.

## Connect fal (recommended)

With the [fal](https://fal.ai) MCP server connected, the skill generates the images, video, music, sound, voice and 3D each direction calls for, using the strongest current model, and puts the files in your project. Without it, directions that need photography or illustration fall back to code and placeholders. The [landing page](https://bgarcia7.github.io/exploration/#examples) shows the same brief with and without the skill.

1. Create a key at [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys).
2. Add the server. In Claude Code:

   ```bash
   claude mcp add --transport http --scope user fal-ai https://mcp.fal.ai/mcp --header "Authorization: Bearer YOUR_FAL_KEY"
   ```

   For Cursor, Windsurf, ChatGPT/Codex and other clients, see the [setup steps on the landing page](https://bgarcia7.github.io/exploration/#install) or [fal's MCP docs](https://fal.ai/docs/documentation/setting-up/mcp).
3. Start a new session and ask: "Use fal to search for image generation models. Do not run a model."

The MCP server is free. You pay only for the model runs you trigger.

## Use

Ask for exploration, fresh directions, options to compare, or "surprise me", or call the skill by name. Ask for a number of variants ("x3", "give me a few") to get several independent directions with a comparison.

```
/exploration landing page for a bike repair app x3
```

## Requirements

- A shell with `python3` to generate seeds. Without Python, it falls back to a POSIX shell one-liner.
- **Recommended:** the fal MCP server (see above) for generated media. Without it, the skill builds what it can in code and hands over ready-to-run prompts for the rest.

## What's inside

```
skills/exploration/
├── SKILL.md            the core method
├── scripts/seed.py     seed generator with a digest of patterns
└── references/         domain guides: design, architecture, marketing,
                        ideation, writing, naming, research, media, fal
```

## License

MIT
