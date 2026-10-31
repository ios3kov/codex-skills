# Identity and shot state

## Compact character record

Give the character a stable ID and an approved reference version. Record only relevant, supported traits:

- Face/head: proportions, eye/brow shape and spacing, nose/mouth/jaw, facial hair, freckles, scars or markings.
- Hair: cut, length, parting, texture, color and accessories.
- Body: silhouette, proportions, posture and age impression where specified.
- Costume: cut, materials, palette and specific details such as fasteners, pattern or approved logo asset.
- Signature items: shape, scale, placement, handedness and permitted absence.
- Style: medium and rendering rules, separately from identity so style changes do not silently redesign the person.

For each important trait mark **locked**, **scene-flexible**, or **story-dependent**. A permitted emotional expression is not permission to change facial structure. A story change needs its triggering scene and new state; do not carry it into earlier shots.

Use character-left/right for body details and frame-left/right for composition. Record mirroring explicitly; a scar or asymmetric prop must not silently flip. Lighting may change perceived color, so compare identity under comparable views rather than demanding identical pixel values.

## Reference pack and prompt handoff

Start with the lightest pack sufficient for the requested shots: approved portrait and full-body view, additional angles when needed, relevant expressions, costume/prop detail and known wrong variants. Generated auxiliary views are candidates until checked against the canonical reference.

Keep the identity anchor stable. Separate scene action, camera, expression, clothing state and style in the prompt or production packet. Avoid adding unrelated changes during a repair. With an available masked edit, preserve surrounding approved content; otherwise select a suitable reference-based workflow and state its limits.

Record actual model/version, reference IDs and settings when exposed. A missing seed is `not_provided`, not a guessed value. Changing a provider, model, seed or reference requires renewed comparison; deterministic reuse across such changes cannot be assumed. Choose a rigged/vector asset when the task needs deterministic repeated animation and that approach fits the brief.

## Shot continuity and repair

Associate each shot with character reference version, costume/prop state, expression/action, scene chronology and any approved exception. Compare adjacent shots for recognizable face, hair, silhouette, age impression, outfit, handedness and style. For video inspect visible transitions, occlusion recovery, head turns, hands, hair motion and accessory drift.

Separate identity defects from anatomy, scene-state or styling defects. Fix the affected feature with the narrowest available operation, then recheck the feature and nearby regions. Do not accept a corrected jacket with a newly changed face. Log rejected variants when they explain a recurring failure; preserve approved originals and recovery material.

A new canonical appearance is a redesign decision. Record the user's approval and which future assets it applies to; do not retroactively relabel old approved variants as the new identity. When supplied usage permissions matter, retain their stated scope with the reference record instead of inferring them from an image's availability.
