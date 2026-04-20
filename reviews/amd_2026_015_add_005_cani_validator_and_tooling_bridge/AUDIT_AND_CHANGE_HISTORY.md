# Audit and change history

## Gap being bridged

The CANI family already defined:

- doctrine and knowledge-input discipline under `AMD-2026-015` and `ADD-001`
- schema framing under `ADD-002`
- persisted artifact/storage handling under `ADD-003`
- telemetry/intake-envelope handling under `ADD-004`

The missing governed layer was validator/tooling discipline across those surfaces.

Without that layer, the family had schema and storage contracts but no explicit governance rule for:

- what validator/tooling is allowed to do
- what it must validate
- what outcomes it may emit
- how those outcomes may block or route governed work without silently correcting authority-bearing records

## Why a subordinate addendum is correct

This is not a new CANI family.

It is a bounded continuation of `AMD-2026-015` and depends directly on `ADD-003` and `ADD-004`.

The validator/tooling bridge is therefore correctly represented as `AMD-2026-015-ADD-005`.

## Changes applied

1. Added `amendments/AMD-2026-015-ADD-005-cani-validator-and-tooling-bridge.md`.
2. Added `reference/implementation/CANI-VALIDATOR-AND-TOOLING-CONTRACT-001.md`.
3. Updated the parent CANI amendment to cross-reference `ADD-005`.
4. Updated the main CANI technical standard to point to the new validator/tooling support document.
5. Updated tracker, changelog, registry, and review surfaces.
6. Added the package-local export script and canonical `peer_review_export` zip.

## Hard controls preserved

- Validator/tooling remains non-runtime in this pass.
- Validator/tooling does not become automatic rewrite authority.
- No browser instrumentation was added.
- No event-store implementation was added.
- No database schema or migrations were added.
- No automatic recommendation execution was authorized.
- No UI/runtime mutation authority was granted.
