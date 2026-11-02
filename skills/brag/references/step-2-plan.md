# Step 2: Write the brag plan

Write `<output-dir>/brag-plan.md`. One focused page. This is the creative north star for the entire video.

The plan should specify what the video must communicate and what project material must be used. It should not prescribe low-level Hyperframes implementation details. Hyperframes will decide the concrete composition structure, animation mechanics, and render workflow from the brief in Step 3.

## Choose the concept before the storyboard

For a new video concept, develop three short candidates grounded in the inspected product. Each must use a different way of communicating its value, not merely a different colour, font, tone preset, or transition. For each, note the viewer takeaway, story mechanism, real product evidence, and why it suits the audience and available duration.

Possible mechanisms include an uninterrupted cause-and-effect demonstration, a contrast between an existing problem and its resolution, or a visual explanation of the product's underlying idea. These are examples, not three required templates: choose mechanisms that fit this product. Metaphors may frame real behaviour but must not imply unverified capabilities.

Compare the candidates for product specificity, clarity to a new viewer, strength of available evidence, and feasibility with the available assets. Choose the strongest yourself. Keep the comparison and a brief reason for selection in `brag-plan.md`; present options to the user only when requested or when their decision is necessary. If one missing fact truly blocks progress, ask the main question; otherwise work from known material without inventing facts.

For small corrections or an approved concept, keep the established direction. User dissatisfaction alone does not require a new concept. When previous outputs are available, check that the new concept does not merely repeat their narrative with different styling; do not claim a comparison when none was inspected.

## Create the output directory

```bash
mkdir -p <output-dir>
```

## Structure of brag-plan.md

Use this as a record of decisions, not a required scene order. Adapt or omit hook, middle, and ending fields to fit the selected concept.

```markdown
# Brag Plan: [App Name]

## What is this app?
[One sentence. What it does, what makes it funny or impressive.]

## Concept comparison and selection
[Three distinct mechanisms, their product evidence, and the reason for choosing one.
For a small revision or approved concept, record that the existing direction is retained.]

## The angle
[The creative premise. The joke, the hook, the claim.
What makes this video specific to this project and not generic.]

## Hook (first 2-3 seconds)
[The opening moment. This is the most important decision.
What word, image, or motion earns the next 20 seconds?]

## Product evidence and story moments
[The concrete product moments needed by the selected concept.
Bullet points. Specific. "The altitude meter counting up." 
Not "feature callouts."]

## Ending
[How does the chosen story resolve? A slogan or logo ending is optional.]

## User flow worth showing
[The 2–3 beats of *using* the product (entry → key action → result), pulled from
Step 1 question 9. Use this evidence where it serves the chosen concept; it does not impose a scene sequence. If the project is
landing-page-only, write "none — landing-page only" and rely on Key moments instead.]

## Tone
- Preset: [default / polished / yc-parody / chaotic / deadpan / cinematic / app-store]
- Creative direction: [freeform phrase, inferred or user-provided]
- Interpretation: [one sentence on how this affects pacing, writing, visual energy, and restraint]

## Format: [landscape / vertical / square] — [width]x[height]
## Duration: [target seconds]

## Visual identity (from the project)
- Background: [exact color value]
- Accent: [exact color value]
- Text: [exact color value]
- Display font: [name]
- Body font: [name]
- Strongest visual element: [what from the site to reference]

## Share copy (draft)
[One sentence for Twitter/X/LinkedIn/Discord. Punchy. Not corporate.]

## Audio direction
- Role: [warm bed / sparse professional accents / cinematic support / dense rhythmic layer / intentional silence]
- Music: [candidate track / mood / none only if disabled, missing, or intentionally silent]
- Music treatment: [start time, volume posture, fade-in/out intent, beat/swell notes]
- Music cue guidance: [preset cue file read / unavailable; list 1-3 strongCue timestamps for major moments; list beat-grid windows for sequential events]
- Audio-reactive treatment: [none / subtle / expressive; what visual qualities may respond to music energy]
- SFX posture: [sparse / moderate / dense; motion-matched; professional restraint]
- Audio-coupled moments: [visual ideas that should consider sound, e.g. typed text, beat reveal, count-up, card sequence]
- Restraint rule: [what audio must not do]

## Storyboard

### Scene 1 — [name] — [duration]s
[What's on screen. What text appears. What product material must be referenced.]
Sequential/interaction: [yes — describe what appears one by one or what interaction is simulated, e.g. "3 stat cards arrive one by one" or "cursor clicks the match button"; or none]
Audio intent: [what the sound should do emotionally]
Audio-coupled idea: [typed text, beat-aligned reveal, counter ticks, card-by-card sequence, simulated tap/swipe/type — or none]
Music: [mood, or "none" only if disabled / missing / intentionally silent]
Transition mood: [clean / hard / dramatic / soft / chaotic] → Scene 2

### Scene 2 — [name] — [duration]s
[...]
Sequential/interaction: [yes — describe it; or none]
Audio intent: [what the sound should do emotionally]
Audio-coupled idea: [type or none]
Transition mood: [mood] → Scene 3

[... continue for all scenes]

**Music mood for this video:** [upbeat / cinematic / chaotic / deadpan / parody / none only if disabled / missing / intentionally silent]
**Audio summary:** [one sentence describing the full audio arc]
```

## Planning the scenes

Build the scene order from the chosen concept. A continuous demonstration may need one evolving shot; another idea may need a contrast or a reveal. Use only the scenes needed to communicate the intended takeaway. Do not fill a fixed feature quota or add a slogan ending by default.

Tone shapes delivery, not story structure. The tone reference offers optional expression choices, not required scene counts or transition recipes.

## Duration guidance

Scene durations must sum to the user's target. Without a specified target, aim for 15–25 seconds. Reduce the amount of information to fit; do not add scenes just to reach a default length.

## Reading time (keep the pace, not at text's expense)

High pace comes from fast motion, fast transitions, and tight cuts — NOT from pulling text off screen before it can be read. Every text element a viewer must read needs enough fully-visible, settled time (entered, not yet exiting) to actually read it:

- Short label or 1-3 word line: about 0.8s settled.
- Headline or full sentence: about 0.3s per word, minimum ~1.2s. The hook line gets the most.

Plan that floor, then keep everything else fast: entrances and transitions stay snappy (0.3-0.6s) and motion stays energetic. A line can SLAM in fast and then HOLD — fast-in plus an adequate hold reads as punchy AND legible.

Two failure modes to design out at the plan stage:

- **Too much text for the scene length.** A 4s scene lands maybe 2-3 short reads at the floor, not 6. If a scene carries more text than its duration allows, cut copy or split the scene — do not speed it up.
- **Sequential text snapped onto a fast beat.** Beat-grid reveals can land ~0.5s apart at 110+ BPM (this is what rushed the bicycles spec rows). That spacing is fine for accents (glows, dots, ticks) but too fast for readable lines. For sequential TEXT, hold each item to the floor: snap to every other beat, or reveal them quickly and hold the full set on screen afterward. Flag any sequential text reveal in the storyboard with its intended hold.

## Choosing what to show

Every brag video must show something real from the product. Options, in preferred order:

1. **Recreate a working-app moment** — the upload screen, the result view, the dashboard with real-looking content. Use real source from `app/`, `pages/`, or routed components — not just the landing page. This is the most compelling option whenever the product has a flow. The product *doing* its thing beats the product *describing* its thing.
2. **Recreate a UI element in HTML** — a hero card, swipe UI, progress meter, stat block. Strong when there is no flow to show.
3. **Animate the core concept** — if the product is "taxis for taxis", animate two taxis where one is in the other. Pure graphic but grounded in the idea.
4. **Text-forward sequence** — if the product is copy-driven (Psychologists for Chatbots), let the copy be the visual. Giant display type, minimal chrome.

Never fill scenes with abstract patterns, color washes, or generic motion graphics that could belong to any video.

## Bias the storyboard toward the user flow

If Step 1 question 9 identified a real user flow, prefer showing its actual behaviour over marketing claims. Fit that evidence into the selected story rather than requiring the full flow as a fixed middle section.

Good (working-app scenes):
- "Upload screen — cursor drops a video file. Filename appears. Progress bar fills 0→100% in 1.2s."
- "Three result thumbnails pop in: 0:15, 0:23, 0:31. Each shows a vertical clip frame with a real-looking caption."
- "Inbox row appears, gets a green 'resolved' badge, slides off the top of the list."

Avoid (marketing-only scenes when a flow exists):
- "16:9 → 9:16 transform diagram" — that's a *diagram of what the product does*, not the product doing it.
- "Three stat cards: 10x faster / 0 cuts / 3 clips" — that's the landing page's social-proof row, not the product.

Stat cards, headline blocks, and the landing-page hero still have a place — but at most one of them, used as a frame around the flow, not as a substitute. The centerpiece is the working app.

If the project has no app (landing-page-only static site), skip this section and recreate the landing-page strongest visual instead.

## Look for interaction and sequential reveal moments

Before writing the storyboard, ask: **does this product have things that can appear one by one, or actions that can be simulated?**

Use these only when they help the selected story. Neither typing nor a simulated cursor is a default opening. Consider:

- **Sequential reveals** — use them when order or accumulation communicates something. A set of cards does not need staggered entrances merely because it can have them.
- **Simulated interaction** — show a swipe, click, typed input, selection, or toggle when the action helps explain the product. A cursor clicking a button, a swipe gesture on a card, or text being typed into a field turns a static mockup into a demonstration. Sound matches the action automatically when the gesture is in the storyboard.

If a scene has either of these, commit to it explicitly in the scene description:
- Good: "3 horse profiles slide in one by one, each with a card sound"
- Good: "Simulate a right-swipe on Thunder's profile card"
- Good: "The hook line types out character by character with keyboard sounds"
- Avoid: leaving it vague and hoping Hyperframes adds rhythm on its own

Hyperframes can implement both patterns well — but only if the plan specifies what's appearing, in what order, and that interaction is being simulated. The plan is the contract.

## Audio planning

Choose the music direction in the plan. Leave exact SFX file selection and exact timestamps to Hyperframes during composition, because SFX should match the actual visual implementation.

Default posture: include audio. Pick a music bed and a few tasteful SFX unless the user passed `--no-music` / `--no-sfx`, the assets are missing, or silence is explicitly part of the concept.

For each scene, note the intended audio role and likely audio-coupled opportunities:

Format: `Audio-coupled idea: type the hook with subtle key ticks if Hyperframes uses a typing animation.`

For audio-reactive visuals, say what should respond and how restrained it should be. Example: `Audio-reactive treatment: subtle; use music RMS/bass to make the hero glow and product card presence breathe, not to add waveform bars.`

Do not require exact SFX filenames in `brag-plan.md` unless the user explicitly requested a specific sound or the mapping is unavoidable. Prefer moment types and intent.

Hyperframes has creative freedom to choose exact files, density, and timestamps that make the video feel smooth and professional.

Do not over-specify audio if the tone asks for restraint. For `yc-parody` or `deadpan`, use fewer and quieter cues, but prefer polished restraint over no audio.

## Music cue guidance

Beat/cue sync is available for any track now (see `audio.md` → "Beat and cue sources"): bundled tracks have precomputed presets; custom tracks get cues at composition time via `analyze_music_cues.py` (rich, needs Python) or `npx hyperframes beats` (simple, zero-dep). When the plan chooses music, add a compact `Music cue guidance` section to `brag-plan.md`:

- The track and, if a preset exists, its tempo.
- 1-3 strong-cue timestamps to target for major visual moments — from the preset if bundled, otherwise note "to be detected at composition time."
- Beat-grid windows for any sequential reveals in the storyboard.
- A restraint note when the tone is deadpan, yc-parody, or otherwise quiet.

See `audio.md` for the cue sources, JSON schema, and beat-sync tolerances.

If SFX are enabled, note likely sound opportunities but leave exact filenames to Hyperframes. Hyperframes should use the skill's `sfx-analysis.md` during composition.

## Handoff posture

- Good: "Recreate the swipe card with Thunder's profile and hay tags."
- Good: "Use the source site's amber/dark palette and serif headline feel."
- Good: "The stat reveal should feel like a deadpan startup metric slide."
- Avoid: "Use a GSAP timeline with this selector and this easing."
- Avoid: "Use this exact HTML structure."
- Avoid: "Load this specific runtime URL."

## Transitions

Choose transitions for continuity, contrast, and readability in the selected story. Use `tones.md` only as optional expression guidance, not a fixed recipe.
