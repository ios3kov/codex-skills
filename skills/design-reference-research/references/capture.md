# Dated capture bundles

Use the project's established destination and article format. Without one, place a requested saved bundle under the workspace's user-facing outputs, in a date-named folder. Do not assume an `articles/` repository, index, Git workflow, or schedule exists.

## Select and capture

Read relevant past manifests before selecting new items. The user determines count; absent a count, five is a useful initial budget for a daily batch. Report a smaller well-supported set if access/quality prevents the target, rather than filling slots with duplicates or weak thumbnails.

Prefer inspectable live sources for website/motion study. Marketplace or portfolio previews are discovery leads; inspect the real page when possible and retain both URLs. A blocked/login-gated source may yield a labeled static fallback, or be replaced by a stronger source.

For each selected live website:

1. Capture the first viewport and inspect meaningful sections through the footer. Record viewport, route, theme, date, and observed interactions.
2. Scroll through lazy/reveal content before a full-page capture. Wait for the actual state to settle; two seconds is a useful initial wait, not proof of readiness. A page may need longer or never settle.
3. Save a full-page image if the tool supports it. Inspect for blank lazy sections, duplicate sticky headers, seams, clipping, and missing footer. If stitched, record the method and limitations. If only viewport captures are possible, label them as such and mark full-page coverage incomplete.
4. Derive section crops from that same full image. Record image-pixel bounds, source file, label, order, and height. In an archive that promises exhaustive coverage, use adjacent half-open ranges `[start,end)` covering the entire height, including whitespace. Focus crops are a separate artifact and do not prove exhaustive coverage. Sticky overlap needs an explanation.
5. Record video when supported and useful: initial state, intentional slow scroll, relevant hover/click/sticky/reveal behavior. Extract representative progression frames if video succeeds. Four frames are a helpful starting budget, not evidence of smooth playback.
6. Record fallback reasons per missing artifact. Do not infer motion from a static image or claim a video exists because a recording attempt succeeded.

## Minimal manifest

Use one manifest as the factual index; prose interprets those facts without duplicating every field. Add fields required by the project, rather than generating empty placeholders.

```json
{
  "schemaVersion": 1,
  "date": "2026-10-10",
  "mode": "capture",
  "requestedCount": 5,
  "historyScope": [],
  "items": [
    {
      "id": "ref-01",
      "title": "An inspected source's actual title",
      "sourceUrl": "https://example.org/source",
      "pageUrl": "https://example.org/",
      "inspectedAt": "2026-10-10T10:00:00+02:00",
      "viewport": {"width": 1440, "height": 900, "deviceScaleFactor": 1},
      "evidenceType": "live-page",
      "role": "scroll continuity",
      "observation": "Only the behavior actually observed",
      "take": "One reusable mechanism",
      "assets": [],
      "videoFallbackReason": "Recording not available",
      "coverageLimit": "No full-page image captured"
    }
  ]
}
```

This is a schema illustration, not real reference evidence. For each real asset use `path`, `kind`, and, when useful, `sha256`; `kind` is `still`, `full-page`, `section`, `video`, or `motion-frame`. Section assets also record `sourceImage`, `yStart`, and `yEnd`. Video frames record `sourceVideo` and timestamp. Paths are relative to the manifest folder. Hash actual bytes, not the URL string.

## Duplicate policy

Use [../scripts/check_duplicates.py](../scripts/check_duplicates.py) for source/media identity checks:

```bash
python3 scripts/check_duplicates.py /path/to/current/manifest.json --history /path/to/prior/manifest.json
```

The script strips tracking parameters and ordinary section anchors, normalizes host/scheme case and query-key ordering, and preserves meaningful queries, repeated-value order, hash-router routes, and case-sensitive paths. It checks landing/source URL aliases and actual media bytes across distinct reference items. Repeated files within one item can be intentional, e.g. a hero crop also used as the representative still. Common titles are warnings, not proof of identity. Different URLs can still be the same template; visually inspect nearest neighbors and their transferable mechanisms.

Without supplied history, deduplication is only within the current batch. Record the scope and do not claim archive-wide novelty. For an intentional revisit, annotate the item and report the duplicate openly; do not weaken the checker to make it pass.

## Useful article and verification

Write a brief pattern summary, then each source's visual evidence, what works for this task, observed motion, concrete adaptation brief, and any access/coverage gap. Preserve image order and show images directly when the delivery format supports them. A long prompt is justified by complex behavior, not by a fixed length.

Check count against the request, source scope, actual media existence/decodability, full-page coverage, crop derivation/ranges, video playback, and fidelity of motion notes. Inspect the rendered article or board at its intended reading size if one is delivered. A zero-duplicate result covers identities only; semantic variety, asset integrity, and visual quality require their own checks.
