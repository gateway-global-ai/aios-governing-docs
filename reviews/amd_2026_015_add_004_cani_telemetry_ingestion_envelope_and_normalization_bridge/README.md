# AMD-2026-015-ADD-004 review package

This review package covers the narrow telemetry/intake-envelope addendum under `AMD-2026-015` for CANI signal admission, provenance, sequencing, normalization, and mapping into the existing persisted artifact contract.

## Standard export

The standard self-contained export for this package is:

- `reviews/peer_review_export__AMD-2026-015-ADD-004__2026-04-09.zip`

Build path:

- `reviews/amd_2026_015_add_004_cani_telemetry_ingestion_envelope_and_normalization_bridge/build_peer_review_export.ps1`

This export follows `AIOS-PEER-REVIEW-EXPORT-STANDARD-001`:

- `peer_review_export` means self-contained evidence archive
- repo-relative tree appears at archive root
- zip entry separators are normalized `/`
- review docs plus actual files under review are included
- unrelated repo files are excluded

The canonical source of truth remains the governed repo review package and source artifacts. For external/manual review, the canonical review artifact is the self-contained `peer_review_export__<document_id>__<date>.zip`, produced from the preserved package-local build script.

## Review target

- `amendments/AMD-2026-015-ADD-004-cani-telemetry-ingestion-envelope-and-normalization-bridge.md`
- `amendments/AMD-2026-015-cani-experience-loop-and-victory-lap-formula.md`
- `amendments/AMD-2026-015-ADD-001-governed-knowledge-artifact-registry-and-declared-input-bridge.md`
- `amendments/AMD-2026-015-ADD-002-cani-observation-schema-and-recommendation-routing-bridge.md`
- `amendments/AMD-2026-015-ADD-003-cani-persisted-artifact-taxonomy-and-routing-storage-bridge.md`
- `reference/knowledge_base/articles/CANI-VICTORY-LAP-FORMULA.md`
- `reference/implementation/CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001.md`
- `reference/implementation/CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001.md`
- `reference/implementation/CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001.md`
- `reference/implementation/CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001.md`
- `reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md`
- `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md`

## What this package does

- defines the logical telemetry/intake envelope for CANI signals
- defines provenance, sequence, batch, and causal-linkage fields
- defines normalization rules before persistence
- defines mapping into the canonical persisted observation and recommendation artifacts already governed by `ADD-003`
- preserves explicit non-authority boundaries so this package does not become a second storage architecture or a runtime implementation package

## Why an addendum is the correct instrument

`AMD-2026-015` already governs the CANI family.

`ADD-003` already owns persisted artifact/storage handling.

This pass closes one narrower family gap:

- the intake-envelope boundary before persistence
- the provenance and sequencing fields required for admission
- the normalization bridge into the already-existing persisted artifact contract

This review package also captures one narrow anti-drift clarification pass:

- `payload_ref` is bounded to reviewable intake evidence and must not become a hidden-authority loophole
- normalization prose is aligned to the existing controlled state model by using `rejected` instead of an undefined `unresolved` state

## What this package does not do

- define a new event-store location class
- define a second persistence tree
- implement runtime telemetry collectors
- define browser instrumentation
- define runtime writers
- define database tables or migrations
- authorize automatic recommendation execution
- authorize runtime UI mutation
