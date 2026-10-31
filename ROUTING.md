# Skill routing and shared references

Choose the owner from the requested deliverable, not a shared word such as “design”. The user's explicit skill choice and approved project design take priority. Supporting skills supply only their relevant expertise; they do not start a second process or override the owner's platform constraints.

| Task | Primary owner | Optional support and boundary |
|---|---|---|
| Web page, dashboard or browser component | `interface-craft` | `genjutsu` for an art-direction/finishing pass; `apple-design` only for requested Apple-like web interaction |
| Native iOS/Android screen or mobile flow | `mobile-interface-craft` | Native platform requirements take priority; `apple-design` is web-translated guidance, not a replacement for native APIs/HIG |
| Logo, lettering, identity or brand application system | `brand-system` | `design-dna` can extract an existing reference; ordinary page styling stays with the surface owner |
| Extract/compare visual tokens and design rules from supplied references | `general-skills:design-dna` | Observed properties remain distinct from new design choices; do not silently redesign the reference |
| Cross-medium visual concept or finishing critique | `general-skills:genjutsu` | Use the surface/format skill for implementation and delivery checks; it does not replace the approved identity |
| Apple-like gestures, springs and physical motion on the web | `apple-design` | `interface-craft` still owns the working web interface; apply only when relevant/requested |

For example, an iPhone form stays with Mobile Interface Craft; a web settings page stays with Interface Craft; extracting an existing palette uses Design DNA; a new logo uses Brand System. Add Genjutsu only when direction or finish needs its separate expertise. No fixed style rule overrides the user's approved design or a platform requirement.

## PDF and OpenAI documentation: choose one provider

| Capability | Prefer when available | Standalone fallback |
|---|---|---|
| PDF artifacts | Official managed `pdf:pdf` with its supported runtime | `skills/pdf` when the managed package is unavailable |
| OpenAI/Codex documentation | Codex system `openai-docs` | `skills/openai-docs` in an environment without that managed skill |

Avoid installing/enabling the standalone fallback together with its managed counterpart. Identify the loaded path/provider when the display name is the same. Do not assume equal names mean equal tools or instructions. On a machine already using both, compare its configured capabilities and disable only the redundant standalone copy through the host's supported skill settings; do not delete system skills. This maintenance documents the choice and does not silently alter an existing user's settings.

The portable fallbacks stay in this library for other environments. `managed-skills.json` is an inventory, not an instruction to install an additional duplicate.

## Shared reference ownership

- Typography: `skills/interface-craft/references/typography.md`.
- Brand positioning: `skills/editorial-copy/references/brand-positioning.md`.

`reference-groups.json` lists the bundled copies. Edit the named source, then run `python3 scripts/sync_references.py --write` and review the diff. Default `--check` reports drift without writing. Packages keep real local copies, so an independently installed skill remains self-contained. Update the affected manifest hashes after an intentional change; CI checks both hashes and copy equality. Do not use symlinks to another installed package or fetch these references at runtime.
