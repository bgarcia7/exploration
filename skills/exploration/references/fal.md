# Generated media with fal: images, video, audio, 3D

Use this guide whenever a direction needs media that code can't make well. That covers photography and illustration, motion footage, music, sound effects, voiceover, 3D models, and edits or upscales of existing media. All of it goes through the **fal MCP server**. fal's model catalog changes monthly, so treat every model name here as a starting point and confirm it with discovery each time.

## Contents
1. What to generate, and what not to
2. Check the tools
3. Plan the media
4. Choose a model
5. Quality and cost
6. Prompting from the direction brief, by medium
7. Run, download, inspect
8. Put the media in the deliverable
9. Report

## 1. What to generate, and what not to

| Medium | Generate it for | Build or source it another way |
|---|---|---|
| **Image** | Photography, painterly, print-style or 3D illustration, product-in-context scenes, textures, style frames | Icons, logos, charts, diagrams, UI, anything with words or numbers (build in code) |
| **Video** | Hero loops, ad spots, short product-in-context shots, motion studies of a direction | UI walkthroughs (screen-record the real product), animated type and charts (CSS, canvas or Remotion) |
| **Music** | Beds for videos and ads, a sonic direction for a brand, intros and stings | Anything that must imitate a named artist or a specific song |
| **Sound effects** | UI sounds, transitions, ambience, impacts | |
| **Voice** | Voiceover for scripts and ads, hearing a draft or a name list read aloud | A real person's voice, unless that person has given explicit consent |
| **3D** | Product or object models for turntables or interactive viewers | Precise CAD or engineering geometry |
| **Edit and upscale** | Extending, restyling, removing backgrounds, upscaling images or video | Changing what's in a real photo in a way that misleads |

**Never generate** media that poses as evidence. That means:
- No real person's likeness or voice.
- No other brand's products or logos.
- No "customer" photos, clips or voices attached to names or quotes.
- No before-and-after shots, certificates, badges, or experts who seem to endorse something.

Anonymous lifestyle footage is fine. Presenting the person in it as a real customer is not.

**How much:** generate what the direction needs to feel finished, at full quality. A sensible default per variant is a hero piece in the medium that carries the direction (an image, a loop, a music sting) plus the supporting pieces that keep the rest of the deliverable from falling back to placeholders, all in the same style. Don't trim media to save money unless the user has said something about cost.

## 2. Check the tools

The fal tools are `search_models`, `recommend_model`, `get_model_schema`, `get_pricing`, `run_model`, `submit_job`, `check_job`, `get_job_result`, `upload_file` and `search_docs`. Depending on the agent, they may carry a server prefix (for example `mcp__fal-ai__run_model`). If your agent loads tools on demand (Claude Code's ToolSearch, for example), load them all in one call.

If the fal server is still connecting or starting up, wait for it or search for its tools anyway. Don't treat "connecting" as unavailable.

If no fal tools are available in the session:
- Tell the user the fal MCP server isn't connected. Adding it to their agent's MCP configuration, with their own fal API key, enables generated media. Most agents only pick up a new server in a new session.
- Carry on without generated media. Use a CSS, SVG, canvas or Web Audio treatment that suits the direction, a clearly marked placeholder, or prompts that are ready to run.
- Don't quietly switch to a different paid generation service. Offer it and let the user decide.

## 3. Plan the media

List every piece per variant before making any paid call. For each one, note:

- The medium and its purpose: where it sits and what job it does.
- The specs: aspect ratio and display size for visuals; duration for video and audio; whether it loops; whether it plays with sound.
- What it must show or sound like, and what must stay out of it.

Make each variant's media serve that variant's direction. A page that is a printed object may need no photograph. A quiet direction may need silence. Leaving a medium out is a valid design decision.

## 4. Choose a model

Default to the highest-quality option: the top-tier model for the medium, at its highest resolution and quality settings, and the full duration the piece needs. Choose a cheaper or faster model only if the user has said something about cost or speed. Find current options with `recommend_model` (describe the task) or `search_models`. Read `get_model_schema` before the first call to any model: it lists the parameters, sizes, durations, how many outputs one call returns, and whether the model takes reference inputs or a numeric seed.

Starting points as of late 2026. Verify them every time.

| Medium | Search terms | Strong families |
|---|---|---|
| Image | "text to image", "image edit" | Nano Banana (Gemini image), Seedream, FLUX pro tiers, GPT-image. Use an edit model to change or extend an existing image. |
| Video | "image to video", "text to video" | Veo 3.1 (realism, first and last frame), Kling 3.0 (motion, people, stylized), Seedance 2.x (product and commercial, reference images), Wan |
| Music | "music" | ElevenLabs Music (instrumental switch, section control), Lyria, Stable Audio, MiniMax Music, ACE-Step for very cheap drafts |
| Sound effects | "sound effects" | ElevenLabs sound effects |
| Voice | "tts", "voice design" | ElevenLabs TTS: v3 (expressive), multilingual v2 (steadiest), turbo (cheap and fast). Most return word timestamps if asked. |
| Speech to text | "speech to text" | ElevenLabs Scribe, Whisper. Use these to check a voiceover's words. |
| 3D | "image to 3d", "text to 3d" | Check the current listings. Most return GLB. |
| Upscale and edit | "upscale", "background removal", "video upscale" | Check the current listings. |

- **Consistency within a variant:** once the hero piece is approved, pass its fal URL as a reference input (a reference image, a first frame, a voice) so the supporting pieces match it.
- **Reproducibility:** if a model takes a numeric seed, derive it from the variant's digit sequence. A re-run then reproduces the result, and the seed string stays out of everything you publish.

## 5. Quality and cost

**Default: highest quality, regardless of cost.** Unless the user has said something about cost, budget or credits in this conversation, don't ask for approval before paid calls, don't show an estimate first, and don't draft with cheap or turbo models. Go straight to the best model at full quality.

**If the user has raised cost**, follow what they said. Without a specific instruction, do this:
1. Call `get_pricing` for every model in the plan.
2. Show an itemized estimate: pieces × variants × unit price, plus one retry per piece.
3. Get a yes before the first paid call, unless they already approved a budget.
4. If spending would go more than about 20% over the estimate, stop and ask.

Either way, log every job's cost (see section 9) so you can report the total.

## 6. Prompting from the direction brief, by medium

Every variant gets one **style prefix**, built from its brief and reused for every visual piece in that variant: medium and technique, lighting, framing (from the menus in `media.md` if the brief hasn't settled them), the palette as named colors with hex values, the era or reference point, the texture, and the mood. Be concrete, because concrete prompts avoid the stock look. "A kitchen" produces stock. "A narrow galley kitchen at 7:40 am, low winter sun through a steamed window, 35 mm, shallow depth of field" produces a picture.

**Images**
- Write the style prefix, then the subject, the action, the composition (including where empty space goes for type), and the aspect ratio.
- Always add: "no text, no letters, no logos, no watermark". Set any words in HTML on top.

> Two-color risograph print, fluorescent orange (#FF6C2F) and green (#00A95C) inks on off-white paper, visible grain, slight misregistration, flat shapes, no gradients. Hands opening a small cardboard kit on a kitchen table, seen from directly above, objects arranged with space on the left third for a headline, 4:3. No text, no letters, no logos, no watermark.

**Video**
- Start from an approved still (a style frame), then run image to video. That way the look is locked before you add motion.
- Write the style prefix, then camera language and **one clear action**: "slow push-in, shallow depth of field, a sealed envelope slides into a mailbox slot, cold dawn light, 35 mm, subtle handheld".
- Keep shots to 3–5 seconds and generate at the target aspect ratio. Turn native audio off when music or sound will be added separately.
- Keep product UI, readable text and logos out of generated video. Composite them in afterward.

**Music**
- Let the brief set the genre, instrumentation and energy. The seed can set the tempo (the digit sum mapped into 60–180 BPM, as in `media.md`).
- Describe the structure with times and say whether it has vocals: "minimal marimba and sub bass, 92 BPM, sparse for 4 s, lifts at 6 s, steady groove, clean button ending at 30 s, instrumental".
- Make it as long as the piece it scores, plus about 3 seconds. Never ask for a named artist's sound or a specific song.

**Sound effects**
- Be specific and short: "soft paper envelope slide, 0.6 s, dry, no reverb tail".
- Make a small, consistent kit per variant rather than one-offs.

**Voice**
- Let the brief pick the voice's character (age, warmth, pace, register).
- Audition two or three voices on one line and let the user choose before generating the full read.
- Generate the whole script in one take, with word timestamps if the deliverable needs captions.
- Fix mispronunciations by respelling the word in the TTS text only. Fix a wrong pace by rewriting the script, not by time-stretching the audio.

**3D**
- Start from an approved image of the object, shot clean on a plain background, then run image to 3D.
- Ask for the format the deliverable uses (usually GLB) and a polygon budget that suits the web.

## 7. Run, download, inspect

**Run**
- Quick jobs (images, TTS, sound effects) use `run_model`. If it comes back as `processing`, keep the `request_id` and poll it with `check_job`.
- Slow jobs (video, music, 3D, upscales) use `submit_job` from the start, then `check_job` and `get_job_result`.
- Never call `run_model` or `submit_job` again to check progress, because each call is a new paid job.
- For several pieces, submit them all, then collect the results.

**Download every result right away**, because fal's URLs aren't permanent. Name files by variant, slot and version, next to the deliverable: `curl -sL -o media/<variant>-<slot>-v1.<ext> "<url>"`.

**Inspect every piece.** Never ship something you haven't checked.
- **Images:** read the file and look for warped hands, faces or objects, stray or fake text, palette drift, the wrong aspect ratio, and a generic stock feel.
- **Video:** pull a frame grid and read it, looking for the same flaws plus morphing between frames. Check duration and resolution with ffprobe.
  ```bash
  ffmpeg -v error -i media/hero-v1.mp4 -vf "fps=2,scale=360:-1,tile=4x3" -frames:v 1 media/hero-v1-grid.png
  ffprobe -v error -show_entries format=duration:stream=width,height,codec_name -of compact media/hero-v1.mp4
  ```
- **Audio:** check duration and loudness. For voice, run speech to text on it and compare the transcript with the script. You can't judge how music actually sounds, so say so and ask the user to listen before you build on it.
  ```bash
  ffprobe -v error -show_entries format=duration -of default=nw=1 media/bed-v1.mp3
  ffmpeg -v info -i media/bed-v1.mp3 -af ebur128 -f null - 2>&1 | grep -E "I:|LRA:" | tail -2
  ```
- **3D:** check the file size and polygon count, and render a still or open it in a viewer if you can.

**Retry at most once per piece**, with a corrected prompt. If it's still wrong, show the user and ask rather than looping.

**With several variants**, make every hero piece first and compare them side by side before making the supporting pieces. If two heroes feel alike, rework one variant's style prefix before spending more.

## 8. Put the media in the deliverable

**Images.** Resize to about twice the displayed width and compress:
```bash
python3 -c "from PIL import Image; im=Image.open('media/hero-v1.png'); im.thumbnail((2400,2400)); im.save('media/hero.webp','WEBP',quality=82)"
```
Without PIL, use `sips -s format jpeg -s formatOptions 82 -Z 2400 in.png --out out.jpg` on macOS. Give each image alt text that says what it shows, and an `aspect-ratio` box with `object-fit: cover`.

**Video.** Transcode to H.264 MP4 and keep hero loops small, ideally under about 4 MB:
```bash
ffmpeg -v error -i media/hero-v1.mp4 -an -vf "scale=1600:-2" -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -movflags +faststart media/hero.mp4
ffmpeg -v error -ss 0 -i media/hero.mp4 -frames:v 1 -q:v 3 media/hero-poster.jpg
```
For a hero loop, use `<video autoplay muted loop playsinline poster="...">`. Under `prefers-reduced-motion`, show only the poster.

**Audio.** Encode to MP3 or AAC at a sensible bitrate. Never autoplay sound. Give the user a clear play control and start playback from a click, because browsers block sound until the viewer interacts.

**3D.** Serve the GLB next to the page and show it with `<model-viewer>`, loaded from an allowed CDN with a pinned version. Include a poster image, so the page is complete before the model loads.

**Hosted and sandboxed pages.** Never link to fal URLs: they expire, and pages with a strict security policy (Claude Artifacts, for example) block outside media hosts anyway. Ship the downloaded files with the deliverable, or through the host's own file or asset upload, compressed first.

**Everywhere.** The seed never goes in filenames, alt text, captions, prompts you share, or metadata.

## 9. Report

In the reply, list what you generated by medium (for example "4 images, 2 video loops, 1 music bed"), the models used, and the total spend. Keep a running list of jobs (model, request ID, purpose, cost, output file) in a scratch file, so the total is exact and nothing is paid for twice.
