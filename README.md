# Codex skills

Canonical Git repository for our personal skill library. It started from an installed-file snapshot on 2026-10-31 and has since received repository maintenance changes. The current HEAD is a maintained library, not an unchanged copy of that installation.

## Included

- **30 standalone skills** in `skills/`.
- **12 skills in two owned plugins** in `plugins/`: General Skills 1.3.6 and Product Intelligence 1.0.5.
- Full supporting references, scripts, assets and license notices. `manifest.json` records every payload file with its SHA-256.
- `managed-skills.json` accounts for the other **12 system/provider-managed skills** reported by the local loader. Their provider runtimes are not copied into this public repository. Restore them through Codex and the official plugins.

## Original snapshot and current repository

| Scope | Meaning |
|---|---|
| Original installed payload | **373 files**, copied and verified against the local installation on 2026-10-31 at commit `20e6eebeaea29343919e498b0e5b3fae4fbf2d8f`. This is historical evidence for that snapshot only. |
| Package maintenance | **576 added files** since the original snapshot; existing documentation, metadata and fixtures were also updated. The exact delta is in `verification.json`. |
| Current payload manifest | **949 entries** covering current `skills/` and `plugins/` files. |
| Repository maintenance outside the payload | Root documentation, routing, integrity scripts, regression tests, CI and repository records are tracked by Git but are not entries in the payload manifest. |

Full byte parity of all 37 personal skills was freshly verified across local installation, saved cloud packages and Git payload on 2026-11-01. See `synchronization_2026_11_01` in `verification.json` for the exact scope. The later license synchronization re-exported the 12 changed standalone skills and Product Intelligence 1.0.5, and compared all 417 personal payload files with the local installation; see `license_sync_2026_11_01`. Other cloud packages were not re-exported in that pass. The approved instruction-density update subsequently re-exported its five changed standalone packages and compared all 420 current payload files with the local installation; see `skill_density_sync_2026_11_01` for exact scope and the cloud editor’s iOS version-field limitation. Later changes require a fresh comparison; CI or Git readback alone cannot renew parity. See [verification.json](verification.json) for separate historical snapshot evidence and current repository boundaries.

## Skills

| Skill | Location |
|---|---|
| `hyperframes` | [skills/hyperframes/SKILL.md](skills/hyperframes/SKILL.md) |
| `hyperframes-cli` | [skills/hyperframes-cli/SKILL.md](skills/hyperframes-cli/SKILL.md) |
| `hyperframes-registry` | [skills/hyperframes-registry/SKILL.md](skills/hyperframes-registry/SKILL.md) |
| `media-use` | [skills/media-use/SKILL.md](skills/media-use/SKILL.md) |
| `brag` | [skills/brag/SKILL.md](skills/brag/SKILL.md) |
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

For design responsibilities, overlapping triggers and PDF/OpenAI provider choices, read [skill routing](ROUTING.md).

## Use and maintain

For a standalone skill, use the existing Codex skill installer with this repository and the corresponding `skills/<name>` path. Inspect and back up an existing installation before merging; do not overwrite local changes blindly.

For the two plugin packages, register this repository as a marketplace with the supported Codex plugin workflow, then select the desired plugin. The marketplace is named `ios3kov-codex-skills`. Keep already installed copies until the new source has been verified; avoid enabling duplicate packages. A Git push does not refresh an existing plugin cache or a ChatGPT cloud skill.

Keep plugin directories intact: their skills share references and scripts outside individual skill folders. Copying only their `SKILL.md` files loses those resources.

Future personal skill changes should be merged into this repository together with any local or cloud edits, and verified by fresh payload hashes. The older `production-engineering` repository is retained as a read-only archive. Its full Git history, historical GitHub issues and pull requests remain in that original archive. Full history was not republished into this public repository. This repository is the consolidated skill source.

Repository maintenance does not automatically update installed local or cloud copies. Historical provenance links retain their original repository; active installation links use this repository. It does not change tool accounts, install dependencies, configure MCP, transfer credentials or deploy anything. Context7 and other services still require the target environment’s own connection and authorization.

## Verification and boundaries

The original installed snapshot was checked against its source bytes and a fresh remote Git readback. Later repository checks verify their recorded scope/revision; they do not renew installed-copy parity. Skill format and local-reference checks are recorded in `verification.json`. Structural checks do not prove that every script, native simulator, external API, visual workflow or application works on another machine.

Generated Python bytecode and OS caches are excluded. No authentication files, account configuration, conversation history or memories are part of this library.

## License

Original repository-maintenance contributions use the scoped [MIT license](LICENSE). Twelve formerly unresolved packages now have package-level MIT grants with retained third-party terms; see each `LICENSE-SCOPE.md`. Agentation retains an upstream self-labeled, abridged PolyForm Shield variant, not the canonical 1.0.0 text, and is not an open-source package. The [NOTICE](NOTICE) and [license inventory](license-inventory.json) record upstream pointers and unresolved package status. The packages still marked file-level have no package-wide reuse grant established by these records. This is a collection with multiple upstream licenses, not a relicensing of all content. Preserve the notices and licenses inside each skill/plugin. Provider-managed skills are listed by identity only; reinstall them through the provider.

## Tests and migrated history

Run `python -B -m unittest discover -s skills/production-engineering/scripts/tests -v`, `python -B -m unittest discover -s tests -v`, and `node --test skills/production-engineering/integrations/visual-refinement/tests/story.test.mjs`. Standard tests run in CI. The five specialized browser/REA qualification workflows are retained as manual opt-ins; they may acquire large external tools and are not triggered automatically.

The admitted REA workflow reads the bundled checksum-verified runtime archive, avoiding an expiring artifact in the old repository. Historical SHA/source references are preserved.

## Library maintenance checks

Run `python3 scripts/check_library.py` and `python3 scripts/sync_references.py --check` from the repository root. CI checks the payload manifest, local Markdown targets, declared shared-reference copies, current package versions and active installation pointers. License checks cover package and skill inventory completeness, duplicate entries, allowed statuses, safe existing notice paths, pinned source-license hashes, standard MIT grant/disclaimer text for packages claiming MIT, and exact package/status agreement with `NOTICE`. The frozen `snapshot-baseline.json` records the original 373 payload entries from commit `20e6eebeaea29343919e498b0e5b3fae4fbf2d8f`; offline checks compare current additions, removals and modified-file counts against it. These checks establish content/accounting consistency, not rights ownership, license enforceability or source authenticity. The routing guide is a repository selection/installation guide; installed skill instructions are unchanged by this documentation maintenance.

## Commit-bound CI evidence

`verification.json` keeps the historical `snapshot_payload_commit` separate from `repository_ci_evidence`. Every CI or smoke record names its tested commit, workflow/run URL and result. Records do not attest to a newer HEAD: publishing a record creates another commit. For the current HEAD, resolve the checkout SHA and inspect the matching GitHub Actions run. This avoids pretending a source file can contain its own final commit hash.

The portable symlink-parent regression runs in the normal Ubuntu Python matrix: it constructs a linked temporary parent and invokes the actual REA test fixtures, checking their canonical roots and real adapter/verifier calls. Native macOS execution remains separate evidence; runtime symlink rejection is unchanged.

Recorded scoped smoke: [REA admitted runtime qualification](https://github.com/ios3kov/codex-skills/actions/runs/41253159365) passed at `6e8f8edf7931bec037ef08033244631df0ff4f3f`. It verified the exact bundled Linux runtime and one owned JavaScript fixture with execution networking disabled. It does not certify application correctness or the other specialized workflows; see the commit-bound receipt in `verification.json`.

Design QA [run 41253687766](https://github.com/ios3kov/codex-skills/actions/runs/41253687766) passed at `ff0eabf1d339aadd6e8dffbea06f9744112c5fd2`. Both the owned browser-fixture lane and isolated Obscura pilot completed; this does not admit Obscura for general use or establish application quality.

## Refreshing bookkeeping

After a payload edit, run `python3 -B scripts/update_library.py --write`, then `python3 -B scripts/update_library.py --check` and the applicable tests. Without `--write`, the command only reports drift. Exit codes are 0 for current/refreshed, 1 for stale, and 2 for an error; errors report completed writes. No hooks are installed.

The updater refreshes file hashes, sizes, executable flags, snapshot counts and the README count rows. Skill identities and license decisions remain curated. Payload changes invalidate current local/cloud parity pointers; historical evidence remains unchanged. The command does not create test results or installation evidence. CI checks for drift on every normal run.

## Portability and scoped trials

| Capability | Requirement |
| --- | --- |
| Instructions and offline Python helpers | A host that loads the package; Python 3.11+ for these helpers |
| Model selection, agents and persistent state | Matching host tools and permissions; instructions alone do not provide them |
| iOS Simulator workflows | macOS, compatible Xcode and the tools required by the selected workflow |
| Context7, media and other connected services | Your own supported connection and authorization |

Run `python3 -B scripts/trial_helpers.py` for eight reproducible checks on owned temporary fixtures. They exercise project-map build/search, reciprocal candidate calls, unsupported-format fallback, frontmatter edits, stale output limits, deleted files, and task-plan conflict/dependency validation. The [recorded receipt](evidence/helper-trials-2026-11-01.json) binds results to helper hashes. These are helper CLI checks, not proof of model judgment or whole-skill effectiveness. No agents, simulator or media generation run. Character Continuity generation remains **NOT RUN**; it needs real reference assets, generated output and visual review.

## Brag launch-video skill

`brag` is installed as a separate skill from latent-spaces/brag at `669ab9286aa28b6c3ee30e75f181ee74319d012a`, with its complete bundled assets and retained notices. Its full workflow uses the four separately installed core dependency skills (`hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`) and CLI 0.8.230. A local owned render and media-use audio-helper check passed on this Mac; this does not certify a particular product video or cloud-account tools. See `hyperframes_dependencies_2026_11_02` in verification.json. Bundled music keeps the CC BY 4.0 attribution in `skills/brag/assets/music/README.md`. OpenCode reads the same local repository skill directory.
