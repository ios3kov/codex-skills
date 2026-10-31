# Local implementation reference

The existing implementation, typography and browser-verification references contain the working design and review rules. External links in those files are source credits or optional updates, not required reading.

## Web API baseline

Use semantic elements, visible labels and keyboard-operable controls. Preserve focus after dialogs and asynchronous operations. For WCAG 2.2 AA review, normal text generally needs 4.5:1 contrast, large text 3:1; meaningful controls/graphics need 3:1 against adjacent colors. Target size has exceptions: do not turn 24 CSS pixels into a universal fixed button dimension. Apply the actual criterion and exceptions before a compliance claim; these notes alone are not certification.

`font-variant-numeric: tabular-nums` aligns changing digits where the font supports it. `font-synthesis: none` suppresses synthesized faces but cannot supply a missing weight. Variable axes exist only if the font contains them; use normal font-weight/style/stretch first. Text balancing and pretty wrapping are progressive enhancements: retain readable ordinary wrapping. Do not rely on nonstandard font smoothing to fix poor type selection.

## Fonts without a download dependency

The local catalog preserves font names and selection guidance, not a mandatory font library. Use existing licensed project fonts or an appropriate system font stack. Named families are optional recommendations. The catalog emits no Google Fonts imports or CDN requests.

When a project explicitly requires a particular face, obtain and package its licensed files in that project, record the version and check glyph coverage/rendering. Do not silently substitute a different face for approved brand typography. If those files are unavailable, report that project-specific gap; ordinary skill use does not depend on downloading fonts.

## Browser checks

Prefer role/label locators over DOM-position selectors. Perform an action, assert its actual state or behavior, then take a screenshot. With a compatible Playwright version, `await expect(locator).toBeVisible()` retries; an immediate boolean read does not. `await locator.click()` alone proves no business outcome. Keep screenshot baselines tied to a stable browser, viewport, fonts and data. Inspect changed pixels before accepting a baseline. If the installed API differs, inspect local declarations/examples instead of guessing or upgrading.

Snapshot reviewed 2026-10-20. Original operational summary; source credits remain in the existing references.
