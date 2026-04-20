# AMD-2026-015-ADD-006 review package

**Amendment:** [`AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md`](../../amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md) — **`ratified` `1.0.0`** (**[ratification motion](../../amendments/AMD-2026-015-ADD-006-ratification-motion.md)** **2026-04-09**).

**Status:** **Closed for governance purposes.** Round 1 packet artifacts under [`round_1/`](round_1/) are pre-ratification evidence only; normative law is the ratified addendum and its lockstep companion contract.

This review package covers the narrow collector / instrumentation bridge addendum under `AMD-2026-015` for governed capture surfaces, normalization into intake envelopes, and handoff into validator and writer lanes.

## Standard export

When generated, the standard self-contained export for this package is:

- `reviews/peer_review_export__AMD-2026-015-ADD-006__2026-04-09.zip`

Build path:

- `reviews/amd_2026_015_add_006_cani_collector_and_instrumentation_bridge/build_peer_review_export.ps1`

The canonical source of truth remains the governed repo review package and source artifacts. The package-local build script is preserved so the export can be rebuilt when an external/manual review archive is needed.

## Review target

- `amendments/AMD-2026-015-ADD-006-cani-collector-and-instrumentation-bridge.md`
- `reference/implementation/CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001.md`
- `reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md`
- `CHANGELOG.md`
- `DOCUMENT_REGISTRY.md`
- `DOCUMENT_REGISTRY.json`

## What this package does

- defines which governed capture surface classes may emit CANI-relevant signals
- distinguishes raw capture from normalized intake envelopes
- defines pre-validator fail-closed handling for incomplete, ambiguous, or boundary-violating capture candidates
- defines handoff from normalized intake envelopes into validator and then writer lanes without bypassing governance

## Why an addendum is the correct instrument

`AMD-2026-015` already governs the CANI family.

`ADD-004` already governs intake envelopes.

`ADD-005` already governs validator/tooling behavior.

This pass closes the next narrower family gap:

- governed capture-surface eligibility
- normalization discipline before validator handoff
- writer-lane handoff rules without authorizing collectors or autonomy

Context from earlier CANI doctrine may be consulted during review, but those prior doctrine files are not part of this package's modified source scope.

## What this package does not do

- implement collectors
- implement browser instrumentation
- implement event-store or database services
- authorize automatic recommendation execution
- authorize autonomous routing
- modify the approved writer slice
