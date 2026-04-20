# Audit and change history — AMD-2026-015-ADD-004

## Gap being bridged

1. `AMD-2026-015` defined the CANI doctrine family.
2. `ADD-001` defined governed knowledge-artifact eligibility and discoverability discipline.
3. `ADD-002` defined observation/recommendation schema framing.
4. `ADD-003` defined the canonical persisted artifact/storage contract.
5. A remaining gap persisted at the intake boundary:
   - how telemetry-like signals are admitted before persistence
   - what provenance and sequencing metadata they require
   - how they normalize into the existing persisted artifact contract without creating a second one

## Why an addendum is the correct instrument

The parent CANI doctrine already exists under `AMD-2026-015`.

The remaining problem is not a new storage architecture and not a runtime implementation package.

It is a narrower bridge question inside the same family:

- telemetry/intake envelopes
- provenance and sequencing
- normalization into the existing `ADD-003` persisted artifact contract

That is subordinate doctrine, not a new amendment family.

## Changes applied

| Area | Change |
|------|--------|
| Addendum doctrine | Added `AMD-2026-015-ADD-004` for telemetry/intake-envelope framing, provenance, sequence/batch/causal-linkage, normalization, and mapping into `ADD-003` |
| Technical support | Added `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001` for the logical intake envelope, provenance metadata, sequencing fields, normalization rules, and mapping boundaries |
| Family alignment | Cross-referenced the addendum from the parent CANI amendment and aligned the schema/storage docs so `ADD-003` remains the canonical persisted artifact contract |
| Tracker/review surface | Updated the amendment review tracker and created this review package |
| Export path | Added a package-local `build_peer_review_export.ps1` and canonical `peer_review_export__AMD-2026-015-ADD-004__2026-04-09.zip` build path so the review can be carried as one governed evidence archive |
| Changelog | Recorded the narrowed telemetry/intake-envelope bridge and the review/export surface |

## Clarification pass applied

This package received one narrow anti-drift clarification pass only.

1. `payload_ref` is now explicitly bounded to reviewable intake evidence or governed/review-package artifacts and must not become a loophole for hidden authority or undeclared external material.
2. Normalization-state prose now matches the controlled state model by using `rejected` instead of an undefined `unresolved` state.

## Hard controls preserved

- `ADD-003` remains the canonical persisted artifact/storage contract
- no second storage tree or location class was introduced
- no runtime telemetry collector authority was added
- no browser instrumentation authority was added
- no runtime writer, event-store service, or database migration authority was added
- no automatic recommendation execution authority was added
- no architect, UI, review, kernel, or ratification authority was collapsed
