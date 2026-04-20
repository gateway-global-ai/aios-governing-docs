# AMD-2026-015-ADD-003 review package

This review package covers the narrow storage-contract addendum under `AMD-2026-015` for persisted CANI observation artifacts and recommendation artifacts.

## Standard export

The standard self-contained export for this package is:

- `reviews/peer_review_export__AMD-2026-015-ADD-003__2026-04-09.zip`

Build path:

- `reviews/amd_2026_015_add_003_cani_persisted_artifact_taxonomy_and_routing_storage_bridge/build_peer_review_export.ps1`

This export follows `AIOS-PEER-REVIEW-EXPORT-STANDARD-001`:

- `peer_review_export` means self-contained evidence archive
- repo-relative tree appears at archive root
- zip entry separators are normalized `/`
- review docs plus actual files under review are included
- unrelated repo files are excluded

The canonical source of truth remains the governed repo review package and source artifacts. For external/manual review, the canonical review artifact is the self-contained `peer_review_export__<document_id>__<date>.zip`, produced from the preserved package-local build script.

## Review target

- `amendments/AMD-2026-015-ADD-003-cani-persisted-artifact-taxonomy-and-routing-storage-bridge.md`
- `amendments/AMD-2026-015-cani-experience-loop-and-victory-lap-formula.md`
- `amendments/AMD-2026-015-ADD-001-governed-knowledge-artifact-registry-and-declared-input-bridge.md`
- `amendments/AMD-2026-015-ADD-002-cani-observation-schema-and-recommendation-routing-bridge.md`
- `reference/knowledge_base/articles/CANI-VICTORY-LAP-FORMULA.md`
- `reference/implementation/CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001.md`
- `reference/implementation/CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001.md`
- `reference/implementation/CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001.md`
- `reference/implementation/AIOS-AMENDMENT-INTAKE-SCAFFOLD-001.md`
- `reference/implementation/AIOS-REVIEW-PACKET-TAXONOMY-001.md`
- `reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md`

## What this package does

- defines the governed repo location class for persisted CANI observation artifacts
- defines the governed repo location class for persisted CANI recommendation artifacts
- defines the persisted artifact taxonomy choice for each class
- defines update, supersession, archival, and routing-linkage rules
- preserves explicit non-authority boundaries so persisted CANI records do not become runtime execution authority

## Why an addendum is the correct instrument

`AMD-2026-015` already governs the CANI family.

`ADD-001` and `ADD-002` already resolved declared-input and schema framing gaps.

This pass closes the next narrower family gap:

- where persisted CANI records belong
- how persisted observation and recommendation artifacts are separated
- how routing and supersession are represented without authorizing runtime implementation

## What this package does not do

- implement telemetry collection
- define browser instrumentation
- define an event-store implementation
- define database migrations
- define persistence code
- authorize automatic recommendation execution
- authorize runtime UI mutation
- authorize autonomous self-improvement
