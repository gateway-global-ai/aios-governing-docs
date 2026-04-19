# AMD-2026-015-ADD-005 review package

This review package covers the narrow validator/tooling addendum under `AMD-2026-015` for CANI persisted artifacts and telemetry/intake-envelope artifacts.

## Standard export

The standard self-contained export for this package is:

- `reviews/peer_review_export__AMD-2026-015-ADD-005__2026-04-09.zip`

Build path:

- `reviews/amd_2026_015_add_005_cani_validator_and_tooling_bridge/build_peer_review_export.ps1`

This export follows `AIOS-PEER-REVIEW-EXPORT-STANDARD-001`:

- `peer_review_export` means self-contained evidence archive
- repo-relative tree appears at archive root
- zip entry separators are normalized `/`
- review docs plus actual files under review are included
- unrelated repo files are excluded

The canonical source of truth remains the governed repo review package and source artifacts. For external/manual review, the canonical review artifact is the self-contained `peer_review_export__<document_id>__<date>.zip`, produced from the preserved package-local build script.

## Review target

- `amendments/AMD-2026-015-ADD-005-cani-validator-and-tooling-bridge.md`
- `amendments/AMD-2026-015-cani-experience-loop-and-victory-lap-formula.md`
- `amendments/AMD-2026-015-ADD-001-governed-knowledge-artifact-registry-and-declared-input-bridge.md`
- `amendments/AMD-2026-015-ADD-002-cani-observation-schema-and-recommendation-routing-bridge.md`
- `amendments/AMD-2026-015-ADD-003-cani-persisted-artifact-taxonomy-and-routing-storage-bridge.md`
- `amendments/AMD-2026-015-ADD-004-cani-telemetry-ingestion-envelope-and-normalization-bridge.md`
- `reference/implementation/CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001.md`
- `reference/implementation/CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001.md`
- `reference/implementation/CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001.md`
- `reference/implementation/CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001.md`
- `reference/implementation/CANI-VALIDATOR-AND-TOOLING-CONTRACT-001.md`
- `reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md`
- `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md`

## What this package does

- defines CANI validator/tooling responsibilities in governance terms
- defines what must be validated for persisted observation artifacts
- defines what must be validated for persisted recommendation artifacts
- defines what must be validated for telemetry/intake-envelope artifacts
- defines validator outcomes and how validator results can route into governed lanes without becoming execution authority

## Why an addendum is the correct instrument

`AMD-2026-015` already governs the CANI family.

`ADD-003` and `ADD-004` already define storage and intake-envelope handling.

This pass closes the next narrower family gap:

- validator/tooling expectations across those already-defined surfaces
- validator outcomes and routing of validator results
- governance-preserving integrity checks without runtime implementation

## What this package does not do

- implement runtime validators
- define browser instrumentation
- define event-store implementation
- define database schema or migrations
- define runtime writers
- authorize automatic recommendation execution
- authorize runtime UI mutation
