# AMD-2026-015-ADD-002 review package

This review package covers the narrow schema-and-routing addendum under `AMD-2026-015` for CANI observation records and CANI recommendation records.

## Standard export

The standard self-contained export for this package is:

- `reviews/peer_review_export__AMD-2026-015-ADD-002__2026-04-09.zip`

Build path:

- `reviews/amd_2026_015_add_002_cani_observation_schema_and_recommendation_routing_bridge/build_peer_review_export.ps1`

This export follows `AIOS-PEER-REVIEW-EXPORT-STANDARD-001`:

- `peer_review_export` means self-contained evidence archive
- repo-relative tree appears at archive root
- zip entry separators are normalized `/`
- review docs plus actual files under review are included
- unrelated repo files are excluded

The canonical source of truth remains the governed repo review package and source artifacts. For external/manual review, the canonical review artifact is the self-contained `peer_review_export__<document_id>__<date>.zip`, produced from the preserved package-local build script.

## Review target

- `amendments/AMD-2026-015-ADD-002-cani-observation-schema-and-recommendation-routing-bridge.md`
- `amendments/AMD-2026-015-cani-experience-loop-and-victory-lap-formula.md`
- `amendments/AMD-2026-015-ADD-001-governed-knowledge-artifact-registry-and-declared-input-bridge.md`
- `reference/knowledge_base/articles/CANI-VICTORY-LAP-FORMULA.md`
- `reference/implementation/CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001.md`
- `reference/implementation/CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001.md`
- `reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md`
- `reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md`
- `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md`
- `reference/implementation/AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001.md`

## What this package does

- defines the first governed field-level shape for CANI observation records
- defines burden, fallback, backtrack, and path-efficiency fields in a bounded way
- defines repeat-path and familiarity-signal fields as recorded-action signals rather than hidden memory
- defines recommendation record fields, routing targets, routing states, and authority-status semantics
- binds those records to existing architect/UI/intake/review lanes without authorizing direct runtime action

## Why an addendum is the correct instrument

`AMD-2026-015` already governs the CANI / Victory Lap family.

This pass does not create a new platform package.

It closes one narrower family gap:

- how CANI observations are represented as governed records
- how CANI recommendations are represented as governed records
- how those records route into existing governed lanes

## What this package does not do

- implement telemetry collection
- define browser instrumentation
- define an event store
- define database migrations
- authorize automatic recommendation execution
- authorize runtime UI mutation
- authorize autonomous self-improvement
