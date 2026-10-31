# Durable task state

Use when the work must survive a context refresh, handoff or later session. Keep one task-owned checkpoint in the established workspace, with the requirements and fields already defined in the skill entrypoint. Store decisions with their reason, applicability and source identity; separate approved facts from hypotheses and superseded choices.

Update the checkpoint after a material decision, failed attempt, accepted artifact or changed dependency. Preserve raw evidence at reachable paths and link to it instead of repeatedly copying large logs. Write a replacement atomically when practical, and inspect the saved bytes before calling the checkpoint complete. Do not assume a cloud chat can read a local path: use a permitted durable file/Page destination or give the complete handoff text if saving is unavailable, clearly marking persistence as unverified.

On resume, confirm the selected project/task, current user steering, artifact existence, current source state and relevant access. Use the recorded next step only while its prerequisites still apply. Refresh stale facts rather than turning an old decision into a universal instruction. Keep unknown side effects and unresolved conflicts explicit.

Task checkpoints do not grant permission to write platform memory, a profile, cross-project instructions or a shared memory service. Permanent memory changes still need an explicit request and the host's supported storage workflow. Keep credentials and unnecessary personal data out of both checkpoints and memory; retain only what the task needs. Deletion, retention changes and sharing follow the user's scope and applicable permissions.

This mechanism uses ordinary authorized persistence. It makes no promise of automatic recall, vector search, cross-account transfer or model training.
