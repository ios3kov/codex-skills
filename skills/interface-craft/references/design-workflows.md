# Reusable design workflows

Use only the section needed by the task. These local instructions are an independent synthesis, not an installation of upstream skills or their launchers. Existing brand, approved content, project conventions and task scope take priority. External links below are provenance, not runtime dependencies.

## Extract and retain a project's design system

Use when asked to document a visual system, continue design across sessions, or reconcile an existing implementation. First look for the project's current DESIGN.md, design.md, tokens and component documentation. Update that source rather than introducing a competing memory file. Create a compact DESIGN.md only when a durable record helps the authorized task.

Inspect the package manifest, theme/token files, global styles and representative component usages. Follow the actual stack: CSS variables and media queries; Tailwind configuration or CSS theme declarations; scoped Vue/Svelte styles; CSS-in-JS theme objects. Do not execute configuration files just to read them.

Record each important value with its semantic role, exact existing identifier/value, source file and line, theme/scope and evidence status: source-declared, browser-measured or inferred. Include typography roles and loaded faces, spacing, layout widths/breakpoints, motion, component variants and important states. Preserve near-duplicate colors until their separate meaning and scope are understood; extraction does not authorize consolidation. Mark dynamic expressions, unresolved aliases and incomplete coverage explicitly. Source declarations do not prove the computed appearance.

A useful compact record contains: purpose and authoritative sources; evidence date/revision and dirty state; token roles with source locations; component patterns and states; responsive/theme rules; decisions and reasons; exceptions; unknowns and checks still needed. Separate the current observed system from proposed changes. On resuming work, check affected sources for drift before reusing the record. Do not require a document update for every small edit.

If the app cannot run, produce a source-based draft with visual verification marked NOT RUN. When it can run, compare representative rendered components and real content at relevant widths. Where requested, make a local component specimen using the project's own components and assets, showing important variants and states; this is an optional project artifact, not a new global skill. No source upload to Stitch or another service is needed for extraction.

## Plan a new page around its real material and job

Inventory available facts, approved claims, product screenshots, imagery and missing proof. Choose the visitor's concrete action and arrange sections around completing it. A booking page needs a usable booking path; a product page needs the real product and offer. Do not fabricate metrics, testimonials, customer logos or working form submissions.

When direction is open, compare a small relevant set of compositions using the existing local design catalog and real references if available. Decide type, color roles, density, image treatment and motion together. Explain only consequential choices. Random theme selection and a mandatory house style are unnecessary. Preserve existing design for a polish request. Treat aesthetic patterns as contextual choices, not universal bans.

Use the existing typography, implementation and browser-verification references for the actual checks. Separate functional/accessibility defects, brand mismatches and stylistic judgments. A clean automated scan cannot establish visual quality or conversion.

## Inspect component states together

For a complex component or recurring UI defect, use an isolated temporary preview or the project's existing story/test setup. Show representative normal, loading, empty, error, disabled and recovery states, plus long/localized text, narrow width and relevant themes. Choose states the component actually supports rather than inventing product behavior.

Use mock data without secrets. Prevent production requests and real mutations. Verify keyboard/focus and the outcome of relevant actions separately from screenshots. Keep a reusable specimen only if it belongs in the project's conventions; otherwise remove temporary artifacts after recording the findings. Existing preview tooling is preferred over installing a new framework.

## shadcn-specific work

Apply only if shadcn/ui is present or explicitly requested. Read components.json, package.json/lockfile, aliases, theme tokens and existing component source first. Determine the installed primitive base (for example Radix or Base UI) from code/config; their trigger composition APIs differ. Do not assume a current online example matches this project's version.

Reuse installed components and supported variants before custom markup. Preserve semantic color tokens and project styling conventions. Verify local exports/types and representative usage before introducing component names or props. Dialogs need accessible names, controls need labels and error states, and focus must work in the actual composition. Test nested overlays and keyboard behavior when changed.

If a needed component is absent, inspect the supported CLI/documentation for the chosen project version and package manager. A CLI add or preset change can overwrite customized source: inspect the proposed diff and preserve local edits. Do not run @latest, initialize, migrate, install packages or query community registries merely because this reference was loaded. Use permitted tools only when the task needs them; offline work can inspect local source and report missing documentation. These instructions grant no additional tool permissions.

## Source register and adaptation boundaries

Reviewed 2026-10-30. Selected mechanisms are independently worded here. No upstream executable, hooks, binary, photo library, font files or full skill text is bundled by this update. Previously adapted resources keep their existing provenance and notices in sources.json and catalog-provenance.json.

- Anthropic Frontend Design: https://github.com/anthropics/skills/tree/main/skills/frontend-design — subject-specific direction; existing visual-direction guidance remains authoritative.
- Impeccable: https://github.com/pbakaus/impeccable — surface modes, bounded rendered review; no launcher or binary download.
- Taste: https://github.com/Leonxlnx/taste-skill — direction alternatives and page/app distinction; no random dealing, inspector or mandatory house style.
- Hallmark: https://github.com/Nutlope/hallmark — material inventory and visitor-job anatomy; no theme install, CSS stamp, hook or Together API.
- UI UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill — existing bounded local catalog; no duplicate generator or automatic fonts/imports.
- Hue: https://github.com/dominikmartn/hue — reusable brand specification and component specimen; no promise of identical output or automatic skill generation.
- Extract DESIGN.md: https://github.com/google-labs-code/stitch-skills/tree/main/plugins/stitch-design/skills/extract-design-md — source-first system documentation; no Stitch dependency/upload, automatic token merging or renamed source tokens.
- shadcn/ui: https://github.com/shadcn-ui/ui/tree/main/skills/shadcn — project-aware composition; no imported allowed-tools, dynamic command execution or forced latest CLI.
- Interface Design: https://github.com/Dammyjay93/interface-design — durable project decisions; no Claude-only hooks or automatic loading claim.
- Better Typography and component-state workflows: https://github.com/jakubkrehel/skills — role-based typography (existing typography reference) and isolated state previews; numeric heuristics are not universal acceptance rules.
