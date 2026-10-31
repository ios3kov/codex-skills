# Stage, navigation and export

## Geometry

Author content in one fixed stage coordinate system and scale the entire stage with `min(viewportWidth/stageWidth, viewportHeight/stageHeight)`. Letterboxing is acceptable. Internal slide layouts should not reflow into a different composition on a phone unless the user explicitly requests a separate responsive reading mode.

For speaking, use less text and stronger focus. Reading decks need sufficient standalone context and can carry more structured evidence. Neither mode permits clipped panels, hidden required text or unreadably small type.

Use a coherent hierarchy and reusable slide layouts with deliberate variation. Preserve supplied fonts and brand tokens; do not reject an established font because an upstream aesthetic list calls it common. Embed or package assets when offline portability is required; disclose dependencies on remote font/image loading.

## Interaction and motion

Provide obvious previous/next navigation, keyboard support and a current-position indicator when useful. Keep only the active slide interactive; visibility/opacity/pointer-events or a consistent hidden-state system must not be overridden by layout classes. Remove inactive interactive content from focus and accessibility navigation. Avoid intercepting keys while a user types into a control.

Motion should support focus and ordering. Provide reduced-motion behavior, a complete readable static state and no mandatory perpetual movement. Printing/export should make all slides visible in stable final states rather than preserve an intermediate reveal.

## Verification

At intended presentation size, a smaller desktop viewport and a phone viewport, inspect actual screenshots for overflow, clipping, font fallback, text readability and overlapping panels. Dimension/scroll-height checks alone do not prove visual correctness. Check keyboard navigation, active-slide controls and focus behavior. Verify asset availability in the promised delivery mode.

During conversion compare slide-by-slide text, visual assets, chart content, order and notes against the source. Preserve notes in retrievable form and keep a mapping for split slides. Report any authorized editorial changes separately from faithful conversion.

## Export

HTML remains the interactive source. A screenshot-based PDF is raster output: animation and interaction are lost, text may not be searchable and accessible structure is not retained. For a vector/searchable/accessible PDF requirement, choose an appropriate export path and verify that actual property. Do not claim those properties solely because a PDF file exists. Inspect exported pages and reconcile their count/content with the deck.
