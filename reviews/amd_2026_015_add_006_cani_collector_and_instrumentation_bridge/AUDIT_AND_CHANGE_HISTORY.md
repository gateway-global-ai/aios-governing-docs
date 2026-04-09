# Audit and change history

## Gap being bridged

The CANI family already defined:

- doctrine and knowledge-input discipline under `AMD-2026-015` and `ADD-001`
- schema framing under `ADD-002`
- persisted artifact/storage handling under `ADD-003`
- telemetry/intake-envelope handling under `ADD-004`
- validator/tooling discipline under `ADD-005`

The missing governed layer was the capture-surface and normalization-handoff bridge across those surfaces.

Without that layer, the family had intake envelopes, validator rules, and persisted-artifact rules, but no explicit governance rule for:

- which capture surfaces are allowed to emit CANI-relevant signals
- what distinguishes raw capture from normalized intake
- what must block or fail before validator handoff
- how normalized intake may hand off into validator and then writer lanes without bypassing governance

## Why a subordinate addendum is correct

This is not a new CANI family.

It is a bounded continuation of `AMD-2026-015` and depends directly on `ADD-004` and `ADD-005`.

The collector / instrumentation bridge is therefore correctly represented as `AMD-2026-015-ADD-006`.

## Changes applied

1. Added `amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md`.
2. Added `reference/implementation/CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001.md`.
3. Updated tracker, changelog, registry, and review surfaces for the ADD-006 package.
4. Added the package-local export script so a self-contained `peer_review_export` archive can be rebuilt when needed.

## Hard controls preserved

- No collector implementation was added.
- No browser instrumentation implementation was added.
- No database schema or migrations were added.
- No event-store implementation was added.
- No execution authority was added.
- No autonomous routing was authorized.
- No second storage universe was created.
- The approved writer slice was left untouched in this pass.
