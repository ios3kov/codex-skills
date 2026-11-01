---
name: html-slide-decks
description: Create, edit or convert browser-based slide decks as portable HTML with consistent stage geometry and preserved content. Use for HTML presentations; use the presentations skill for a PowerPoint or Google Slides deliverable.
---


# HTML slide decks

Use for a deck the user wants to read or present in a browser, including an explicitly requested PPTX-to-HTML conversion. Do not turn an ordinary presentation request into HTML without resolving its output format.

1. Resolve purpose, audience, source content, speaker-led versus reading-first use, output format and existing visual direction from the brief.
2. Inventory supplied text, images, charts and speaker notes. Preserve required content and order during conversion; distribute dense material over more slides rather than shrinking it until unreadable.
3. Choose a visual direction from the brand and references. When direction is materially undecided, show a small set of distinct previews; an already chosen direction needs no repeated style-selection gate.
4. Build a portable HTML deck with inline CSS/JS and local or embedded assets according to delivery constraints. Default to a 1920×1080 stage scaled uniformly to fit; use the user's specified aspect and dimensions when provided.
5. Read [stage and verification](references/stage-verification.md) for navigation, fitting and export. Inspect every slide in rendered output, including dense slides and small viewport behavior.

This skill owns browser-deck geometry and navigation. Use `editorial-copy` only when prose editing is authorized; use `visual-diagrams` for complex diagram semantics. Use the existing presentations/PDF workflows when those output formats are requested. Hosting is a separate authorized action.

Do not copy upstream templates or claim extractor/exporter scripts are available unless they actually are. No build system is needed for a simple self-contained deck; an existing application stack can be retained when the user asks to improve it.

Provenance: [sources.json](sources.json), adapted from Frontend Slides.

For slide titles, numeric tables and captions, consult the shared [typography reference](references/shared/interface-craft/references/typography.md) when needed. Evaluate its suggestions at the deck's actual stage and viewing scale, preserving the slide-specific fitting and export checks.

For image/text balance and reading rhythm across a deck, consult the shared [editorial layout reference](references/shared/interface-craft/references/editorial-layout.md) when needed. Preserve source completeness, the requested order and the deck's stage geometry.
