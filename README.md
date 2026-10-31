# Codex skills

Canonical Git repository for our personal skill library. This snapshot was copied from the actual installed files on 2026-10-31.

## Included

- **25 standalone skills** in `skills/`.
- **12 skills in two owned plugins** in `plugins/`: General Skills 1.3.4 and Product Intelligence 1.0.2.
- Full supporting references, scripts, assets and license notices. `manifest.json` records every payload file with its SHA-256.
- `managed-skills.json` accounts for the other **12 system/provider-managed skills** reported by the local loader. Their provider runtimes are not copied into this public repository. Restore them through Codex and the official plugins.

## Skills

| Skill | Location |
|---|---|
| `agent-orchestrator` | [skills/agent-orchestrator/SKILL.md](skills/agent-orchestrator/SKILL.md) |
| `agentation` | [skills/agentation/SKILL.md](skills/agentation/SKILL.md) |
| `apple-design` | [skills/apple-design/SKILL.md](skills/apple-design/SKILL.md) |
| `audio-production` | [skills/audio-production/SKILL.md](skills/audio-production/SKILL.md) |
| `brand-system` | [skills/brand-system/SKILL.md](skills/brand-system/SKILL.md) |
| `character-continuity` | [skills/character-continuity/SKILL.md](skills/character-continuity/SKILL.md) |
| `codebase-understanding` | [skills/codebase-understanding/SKILL.md](skills/codebase-understanding/SKILL.md) |
| `context-discipline` | [skills/context-discipline/SKILL.md](skills/context-discipline/SKILL.md) |
| `design-reference-research` | [skills/design-reference-research/SKILL.md](skills/design-reference-research/SKILL.md) |
| `develop-web-game` | [skills/develop-web-game/SKILL.md](skills/develop-web-game/SKILL.md) |
| `editorial-copy` | [skills/editorial-copy/SKILL.md](skills/editorial-copy/SKILL.md) |
| `html-slide-decks` | [skills/html-slide-decks/SKILL.md](skills/html-slide-decks/SKILL.md) |
| `independent-reviewer` | [skills/independent-reviewer/SKILL.md](skills/independent-reviewer/SKILL.md) |
| `interface-craft` | [skills/interface-craft/SKILL.md](skills/interface-craft/SKILL.md) |
| `ios-simulator-skill` | [skills/ios-simulator-skill/SKILL.md](skills/ios-simulator-skill/SKILL.md) |
| `media-production-control` | [skills/media-production-control/SKILL.md](skills/media-production-control/SKILL.md) |
| `mobile-interface-craft` | [skills/mobile-interface-craft/SKILL.md](skills/mobile-interface-craft/SKILL.md) |
| `motion-storytelling` | [skills/motion-storytelling/SKILL.md](skills/motion-storytelling/SKILL.md) |
| `openai-docs` | [skills/openai-docs/SKILL.md](skills/openai-docs/SKILL.md) |
| `pdf` | [skills/pdf/SKILL.md](skills/pdf/SKILL.md) |
| `production-engineering` | [skills/production-engineering/SKILL.md](skills/production-engineering/SKILL.md) |
| `remotion-video` | [skills/remotion-video/SKILL.md](skills/remotion-video/SKILL.md) |
| `smart-router` | [skills/smart-router/SKILL.md](skills/smart-router/SKILL.md) |
| `to-questionnaire` | [skills/to-questionnaire/SKILL.md](skills/to-questionnaire/SKILL.md) |
| `visual-diagrams` | [skills/visual-diagrams/SKILL.md](skills/visual-diagrams/SKILL.md) |
| `general-skills:brainstorming` | [plugins/general-skills/skills/brainstorming/SKILL.md](plugins/general-skills/skills/brainstorming/SKILL.md) |
| `general-skills:design-dna` | [plugins/general-skills/skills/design-dna/SKILL.md](plugins/general-skills/skills/design-dna/SKILL.md) |
| `general-skills:fact-check` | [plugins/general-skills/skills/fact-check/SKILL.md](plugins/general-skills/skills/fact-check/SKILL.md) |
| `general-skills:genjutsu` | [plugins/general-skills/skills/genjutsu/SKILL.md](plugins/general-skills/skills/genjutsu/SKILL.md) |
| `general-skills:gsap` | [plugins/general-skills/skills/gsap/SKILL.md](plugins/general-skills/skills/gsap/SKILL.md) |
| `general-skills:motion-design` | [plugins/general-skills/skills/motion-design/SKILL.md](plugins/general-skills/skills/motion-design/SKILL.md) |
| `general-skills:research-methodology` | [plugins/general-skills/skills/research-methodology/SKILL.md](plugins/general-skills/skills/research-methodology/SKILL.md) |
| `general-skills:threejs` | [plugins/general-skills/skills/threejs/SKILL.md](plugins/general-skills/skills/threejs/SKILL.md) |
| `general-skills:write-russian-ui` | [plugins/general-skills/skills/write-russian-ui/SKILL.md](plugins/general-skills/skills/write-russian-ui/SKILL.md) |
| `product-intelligence:competitor-recon` | [plugins/product-intelligence/skills/competitor-recon/SKILL.md](plugins/product-intelligence/skills/competitor-recon/SKILL.md) |
| `product-intelligence:customer-voice` | [plugins/product-intelligence/skills/customer-voice/SKILL.md](plugins/product-intelligence/skills/customer-voice/SKILL.md) |
| `product-intelligence:feature-parity` | [plugins/product-intelligence/skills/feature-parity/SKILL.md](plugins/product-intelligence/skills/feature-parity/SKILL.md) |

## Use and maintain

For a standalone skill, use the existing Codex skill installer with this repository and the corresponding `skills/<name>` path. Inspect and back up an existing installation before merging; do not overwrite local changes blindly.

For the two plugin packages, register this repository as a marketplace with the supported Codex plugin workflow, then select the desired plugin. The marketplace is named `ios3kov-codex-skills`. Keep already installed copies until the new source has been verified; avoid enabling duplicate packages. A Git push does not refresh an existing plugin cache or a ChatGPT cloud skill.

Keep plugin directories intact: their skills share references and scripts outside individual skill folders. Copying only their `SKILL.md` files loses those resources.

Future personal skill changes should be merged into this repository together with any local or cloud edits, and verified by fresh payload hashes. The older `production-engineering` repository remains intact; this repository is the consolidated skill source.

This synchronization preserves installed content. Existing upstream README links may still point to their original repository. It does not change tool accounts, install dependencies, configure MCP, transfer credentials or deploy anything. Context7 and other services still require the target environment’s own connection and authorization.

## Verification and boundaries

The copy is checked against source bytes and a fresh remote Git readback. Skill format and local-reference checks are recorded in `verification.json`. Structural checks do not prove that every script, native simulator, external API, visual workflow or application works on another machine.

Generated Python bytecode and OS caches are excluded. No authentication files, account configuration, conversation history or memories are part of this snapshot.

## License

This is a collection with multiple upstream licenses, not a relicensing of all content. Preserve the notices and licenses inside each skill/plugin. Provider-managed skills are listed by identity only; reinstall them through the provider.
