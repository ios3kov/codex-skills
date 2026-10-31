# Evidence-led visual refinement and optional presentation tools

Use for an authorized cleanup of a visual surface, or a requested before/after presentation. Existing brand, approved wording, functionality and task scope remain authoritative. This supplements the existing workflow; it is not a new skill or compulsory redesign.

## Review as a change ledger

For each material observed problem, keep a compact record: source/surface location, visible effect and user impact, intended repair, and relevant verification. Group repeated causes rather than listing every instance as a separate issue. Separate defects from stylistic judgments; a gradient, emoji, bold face or spring is not inherently wrong. Recheck the affected items against the original evidence before completion.

When several layers need work, fix related issues coherently across the authorized surface. Choose order from dependencies: content length may constrain typography and layout; layout affects imagery and motion. Do not force nine passes or full-screen work for a local correction. Stop once the required result is verified, not at an arbitrary screenshot count.

Consider where visual attention belongs. Controls should remain discoverable while content and meaningful actions lead. Strong imagery or expressive chrome can be correct when the brief calls for it; do not force neutral surfaces, one accent, a prescribed font or a single bright object.

For product previews shown together, cross-check names, item IDs, amounts, currencies, dates and statuses. Use the same underlying sample record where useful. Keep mock data clearly illustrative; a believable preview is not proof that a product feature exists. Preserve exact approved claims and original assets.

## Optional tools

Tools live in `scripts/unslop/` inside this skill. Resolve the actual installed skill path. They never install dependencies or connect services. Their upstream source is credited below; these are modified local tools, not the full Unslop workflow.

For an authorized public or local page snapshot:

`node <skill-dir>/scripts/unslop/snapshot.mjs <http(s)-url> <fresh-output-directory> [--dark|--light] [--width=1440] [--height=900]`

Use an existing project runtime with Playwright/Playwright Core and a permitted Chromium executable. It opens a fresh browser context without the user's login session. The target page itself executes during capture; use trusted targets or isolated fixtures. Source capture may make normal page/resource network requests but never sends source to an AI API. Do not point it at a private account or include secrets in a URL without the task's authorization. Where the host requires its browser tool, use that permitted workflow; this helper does not override host controls.

Outputs: original.live.png, inert original.html and coverage.json. Existing output directories are rejected. Read gaps, unresolved resources and readiness before using the result. Canvas, shadow content, active forms, video, animation state and inaccessible assets are not faithfully retained. The export disables scripts/navigation/forms and strips form values; it is not a general privacy scrubber or functional/offline site backup. Text, metadata and image pixels may still contain private information. Compare the saved appearance with the original at the same viewport. The script does not claim pixel parity or accessibility certification. A fresh context may render a login page instead of the desired route; verify identity.

For a requested short explanatory before/after story, use `story.mjs --help` and the local [story contract](story-tool.md). Keep the story file separate from delivered production code. Labels should explain observed changes, not call a preferred aesthetic an objective defect. The last state must match the accepted delivered UI; verify output dimensions, fps, duration and representative frames. A smooth story is presentation evidence, not proof of runtime performance or working interactions.

## Attribution and limits

Adapted from Unslop by Damir Sokolovsky (@heydamir), https://github.com/heydamir/unslop at commit 4652254daff586ff4739849395a127b56f7f8cc7, reviewed 2026-10-31. Upstream material is CC BY 4.0; [full license](../scripts/unslop/LICENSE-CC-BY-4.0.txt). Local changes include scope-preserving guidance, no universal style bans, inert capture with coverage/budgets, and repaired file serving, temporary storage and export controls. Preserve this attribution and identify further modifications when redistributing. Source links are provenance, not required runtime resources. No upstream reference images or font files are installed.
