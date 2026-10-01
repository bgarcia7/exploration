---
name: exploration
description: Steer open-ended creative and exploratory work with real randomness so results escape predictable defaults. Generates a random string in the shell, reads it for patterns and special numbers, turns those into a concrete direction for whatever is genuinely open in the task, then builds it with full craft while fixed requirements stay untouched. Can make several independent variants and compare them, and generates images, video, music, sound, voice and 3D with fal when a direction needs them. Has guides for design, architecture, marketing, idea generation, writing and editing, naming, research, and media. Use whenever the user wants exploration, fresh or unexpected directions, "surprise me", alternatives or options to compare, or an open-ended piece without a stated direction — especially when earlier results felt generic or samey, or they mention a random seed. Skip it when the direction is already decided and the job is just to execute it.
license: MIT
compatibility: Needs a shell with python3 (or a POSIX shell) to generate seeds. Generated media is optional and uses the fal MCP server.
metadata:
  author: bgarcia7
  version: "1.0.0"
---

# Exploration

Asked to "be creative," a model reaches for the same favorites every time: the same palettes, architectures, campaign angles, name shapes, and story beats. Picking "at random" in its head doesn't help, because that pick isn't random either. This skill brings in real randomness from outside and then has you *interpret* it, the way a designer treats a found object as a brief. The result lands somewhere you wouldn't have gone by default, and your judgment keeps it good.

The seed decides **where** to go. It never excuses work that isn't good, and it never decides what's true.

## 1. Frame the task

Sort the task into two lists before generating anything.

**Fixed:** what must hold no matter what. This includes the user's stated requirements; any design system, brand guide, or style rules in the project (check design-system docs, AGENTS.md / CLAUDE.md, existing tokens); correctness, accessibility, budget, honesty, platform rules, and real facts. The seed never touches these.

**Open:** choices that are genuinely free and would otherwise fall to your defaults. This is what the seed steers. Aim for three to six. For anything visual, imagery is always one of them (see the imagery menu in `design.md`), so it can't silently default to none.

If almost nothing is open because the user specified everything, there's nothing for the seed to do. Just do the task.

## 2. Load the domain guide

Read the guide (or guides) that match the task, from `references/` in this skill's base directory. Each guide lists what's usually fixed and open in that domain, menus of real options for the seed to choose from, how to build the result well, and what to deliver.

| Task | Guide |
|---|---|
| Landing pages, UI, visual identity, icons, slides, data-viz styling, motion | `design.md` |
| System design, data models, APIs, picking between technical approaches | `architecture.md` |
| Positioning, campaigns, ad angles, launch plans, growth experiments | `marketing.md` |
| Brainstorming product, feature, business, or solution ideas | `ideation.md` |
| Stories, essays, scripts, copy, and **editing** existing text | `writing.md` |
| Names, taglines, slogans | `naming.md` |
| Research plans, hypotheses, literature and competitive exploration | `research.md` |
| Images, video, music, sound, voice, 3D: prompts, storyboards, art direction | `media.md` (plus `fal.md` to generate) |

Combine guides when a task spans domains: a landing page uses `design.md` plus `writing.md` for its copy, and a campaign uses `marketing.md` plus `media.md`. For a task none of them cover, use the core method here and borrow menus from the closest guide.

**Variants:** make one unless the user asks for options or names a number (`x3`, "a few"), or the guide says comparison is the point. Architecture and marketing default to three. Use one seed per variant.

## 3. Generate the seed

Run the bundled script from this skill's base directory. Don't invent the string yourself:

```bash
python3 <skill-base-dir>/scripts/seed.py        # one seed
python3 <skill-base-dir>/scripts/seed.py -n 3   # one per variant
```

Each seed comes with a digest of facts about it: composition, digit sum and digital root, missing digits, the digit sequence, frequent characters, multi-digit numbers and primes, runs, repeats, palindromes, hex-like runs, the longest letter runs, and the first, middle, and last characters. If `python3` isn't available, use `LC_ALL=C tr -dc 'A-Za-z0-9' </dev/urandom | head -c 64` and compute any count you rely on in the shell.

## 4. Read it for a direction

There are two ways to read a seed. Each guide says which to lean on.

- **Associative reading** works where taste leads (visual style, voice, sound). Look past the surface: a digit sum that becomes a column count or a tempo; a number that means something elsewhere (a year, a ratio, an angle); symmetry, runs, and case rhythm as structure; hex-like runs as color; letter runs that suggest a word, place, mood, or texture; and what's *missing*, such as an unused digit.
- **Indexing** works where options are discrete (architecture, angles, lenses). Walk the digit sequence and let each digit pick entry 0–9 from the guide's next menu. If a pick repeats one already made for this variant, or contradicts a fixed requirement, skip to the next digit and note the skip. That keeps the seed in charge without forcing nonsense.

Most tasks mix both, so index the structure and read the tone.

Write a short **direction brief** for each variant: a name for the direction and, for each open dimension, the decision plus what in the seed drove it. Each decision should be one you wouldn't have made without the seed. Check every pattern against the digest or the shell. A direction built on a pattern that isn't there is just the default in disguise.

With several variants, write every brief before building any of them, then compare them. If two drift toward the same idea, re-read one seed until it goes somewhere else. Variants should differ in kind, not by a shade.

## 5. Build it with judgment

Execute as well as you can, following the guide's building notes. The brief sets the direction, and craft refines it.

- Raw seed values are starting points. A color that fails contrast moves within its hue family; an architecture pick gets its strongest version, not a strawman; an unpronounceable name gets reshaped while keeping its sound.
- Fixed requirements win every conflict. When one forces a change, keep the spirit of the direction.
- Don't drift back to the default. If the direction is unusual, follow it through, because the safe version is what the user is trying to get away from. The most common failure is quietly regressing halfway through, so when you finish, check the result against the brief.
- In analytical domains (architecture, research, marketing tests), the seed chooses what to explore, and the evidence chooses what to recommend. A recommendation of the conventional option, made after a real comparison, is a success.

**Generated media.** When a direction needs media that code can't make well, generate it with the fal MCP. That covers photography and illustration, video loops and shots, music, sound effects, voiceover, 3D models, and edits or upscales. Read `references/fal.md` first. It covers what not to generate, choosing the highest-quality models (the default unless the user says otherwise about cost), prompting each medium from the direction brief, inspecting every result, and getting the files into the deliverable. Check your available tools before deciding fal is missing: they may carry a server prefix, need loading first, or still be starting up.

**Without fal.** If no fal tools are available, keep the media in the direction rather than dropping it. Build what code can make well (CSS, SVG, canvas or Web Audio treatments that suit the direction); for the rest, use a clearly marked placeholder and hand over a prompt that is ready to run. Tell the user which pieces were skipped and that connecting the fal MCP server would generate them. Don't quietly switch to a different paid generation service. Offer it and let the user decide.

Build icons, charts, diagrams, UI, logos and anything containing text in code instead.

## 6. Deliver

Keep the seed out of the deliverable: no string in copy, code comments, filenames, alt text, metadata, prompts, or commit messages. It's scaffolding, and the work should stand on its own.

In your reply, give each variant a direction name and the two to four decisions that most shaped it. Share the full seed-to-decision mapping only if the user asks. With several variants, compare them in a few lines and recommend one. Offer a re-roll, since a new seed gives a genuinely new direction rather than a revision.
