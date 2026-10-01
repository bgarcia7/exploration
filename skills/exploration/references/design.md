# Design

Covers landing pages, app screens and flows, visual identity, marks and icons, illustration style, slide and document styling, data-viz styling, and motion.

## Fixed vs open

**Usually fixed:** an existing design system or tokens, brand assets, accessibility (WCAG AA contrast, tap targets, reduced motion), real product facts and content, platform conventions users rely on, and responsive behavior.

**Usually open:** palette, type pairing and scale, grid and composition, density, shape language (corner radius, stroke weight), imagery and illustration style, motion character, texture, copy voice (read `writing.md` for that part), and the **signature move**, the one thing someone remembers.

When a design system exists, the seed steers only what the system leaves open: composition, imagery, motion, and the signature move. It doesn't touch the system's tokens.

## Reading the seed

Lean associative. Design rewards a felt reading over a lookup table.

- **Color:** hex-like runs used literally or as starting hues. Digit sum mod 360 gives a base hue. The digital root can set the palette size or harmony (1 monochrome, 2 complementary, 3 triadic, and so on).
- **Type:** case rhythm suggests typographic contrast. Long lowercase stretches read quiet and humanist; clusters of capitals suggest display caps, condensed faces, or a hard grotesk. Many digits can mean tabular figures or a mono accent.
- **Space and structure:** numbers become column counts, a baseline unit, a type-scale ratio, a corner radius, or a rotation angle. Palindromes suggest symmetry, and having none suggests deliberate asymmetry. Runs and repeats become a recurring motif.
- **Mood:** the longest letter runs suggest a place, era, or material (a run like "qYRSQ" might read as hard-edged and industrial).
- **Sequence:** split the string into thirds to get the page's sections and the order they arrive in.

**Imagery** is always an open dimension for visual work, and it's the one that quietly defaults to "none" if nothing steers it. Index it like a menu: take the next unused digit.

0 type and shape only, no imagery · 1 documentary photography of people in the moment · 2 studio still life of the product and its objects · 3 macro and texture (materials and surfaces up close) · 4 illustration (painterly, print or line) · 5 photo collage or cut paper · 6 short muted video loop · 7 3D render · 8 environmental portrait series · 9 abstract or generative image (light, fluid, pattern)

Picks 1–9 are generated with fal (see `fal.md`). Without fal, follow the fallback in `SKILL.md` and still honor the pick as far as code allows. A page with no imagery is a valid result only when the seed lands on 0, never because it was easier to build.

Don't map literally when the result would be ugly. Treat the mapping as an argument for a direction, then design the direction well.

## Building

- Start with the signature move and make everything else support it.
- Tune seed colors until they pass contrast, in dark mode too if the product has one. Keep the hue family when you adjust.
- Pick real fonts that are actually available (Google Fonts, system stacks, or the project's own) and that fit the brief.
- Steer away from generic tells unless the brief truly points there: a centered hero over three feature cards, a purple-to-blue gradient blob, Inter for everything, emoji as icons, a stock dashboard mockup.
- When the imagery pick is 1–9, generate it with fal by following `fal.md`, and make it carry the direction: a hero piece plus the supporting images that make the page feel finished, all in one style. A short muted video loop can carry a hero where motion is the point. Don't settle for grey placeholder boxes or stock-looking filler. Keep all text out of the images and set it in HTML on top.
- Check the layout at phone width.
- Render it and look at it, using a screenshot if you can, before calling it done. Compare it against the brief, because drift back to the default shows up visually first.

## Variants

Make variants differ on at least two big axes: color temperature and value; layout logic (editorial, modular grid, single-column scroll, poster); type genre (serif, grotesk, mono, display); and imagery. Use the same content in every variant so the comparison is fair.

When fal is available (check your tools before deciding it isn't, since it may need loading or still be connecting), generated media must be part of the set. With two or three variants, at least one carries generated media as a core part of its direction; with four or more, at least two do, and they use different imagery picks (for example people photography in one and a video loop in another). If the seeds land on 0 too often, take the next digit for the variants that need media and note the skip.

## Deliverable

Working files per variant (HTML/CSS, SVG, Figma, or whatever the project uses), plus screenshots when you can make them. In the reply, give the direction name, the signature move, and the key choices.
