---
document_id: AMD-2026-015-ADD-006
version: 1.0.0
status: ratified
category: amendment
title: CANI Collector and Instrumentation Bridge
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
ratification_date: 2026-04-09
supersedes: null
cross_references:
  - doc_id: AMD-2026-015-ADD-006-RATIFICATION-MOTION
    title: Ratification motion — AMD-2026-015-ADD-006
    relationship: ratification_motion
  - doc_id: AMD-2026-015
    title: CANI Experience Loop and Victory Lap Formula
  - doc_id: AMD-2026-015-ADD-001
    title: Governed Knowledge Artifact Registry and Declared-Input Bridge
  - doc_id: AMD-2026-015-ADD-002
    title: CANI Observation Schema and Recommendation Routing Bridge
  - doc_id: AMD-2026-015-ADD-003
    title: CANI Persisted Artifact Taxonomy and Routing Storage Bridge
  - doc_id: AMD-2026-015-ADD-004
    title: CANI Telemetry Ingestion Envelope and Normalization Bridge
  - doc_id: AMD-2026-015-ADD-005
    title: CANI Validator and Tooling Bridge
  - doc_id: AIOS-KB-CANI-VICTORY-LAP-001
    title: CANI Experience Loop and Victory Lap Formula
  - doc_id: AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001
    title: CANI Experience Loop technical standard
  - doc_id: AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001
    title: CANI observation and recommendation schema
  - doc_id: AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001
    title: CANI persisted artifact taxonomy and storage contract
  - doc_id: AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001
    title: CANI telemetry ingestion envelope and normalization contract
  - doc_id: AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001
    title: CANI validator and tooling contract
  - doc_id: AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001
    title: CANI capture surface and normalization handoff contract
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Ratified subordinate addendum to AMD-2026-015 for governed capture surfaces, normalization into intake envelopes, and handoff into validator and writer lanes. It does not authorize collector implementation, browser instrumentation implementation, database/event-store work, or execution authority.
amendment_history:
  - version: 1.0.0
    date: 2026-04-09
    summary: "Ratified per AMD-2026-015-ADD-006-RATIFICATION-MOTION v1.0.0; substantive basis draft v0.1.6 with approved-with-changes convergence across the final review set and no doctrine-blocking defects."
  - version: 0.1.6
    date: 2026-04-09
    summary: "Add explicit source-surface mapping language, further bound failed raw-capture evidence as intake-adjacent review material only, simplify the support-contract crosswalk, and mark writer lane as a locally defined term."
  - version: 0.1.5
    date: 2026-04-09
    summary: "Add amendment-over-support-contract precedence, clarify failed-normalization evidence retention boundaries, tighten writer-lane materialization limits, and bind implementation-facing controlled values to the support contract."
  - version: 0.1.4
    date: 2026-04-09
    summary: "Align Section 3 with provisional normalization status naming, tighten section crosswalk language, and remove residual ambiguity around advisory-warning post-validator handling."
  - version: 0.1.3
    date: 2026-04-09
    summary: "Remove ambiguous advisory-warning persistence admission, rename provisional normalization statuses to avoid validator-outcome collision, and tighten support-contract citation language."
  - version: 0.1.2
    date: 2026-04-09
    summary: "Make unknown-surface handling mandatory, define writer-lane authority in the operative handoff rule, and clarify that pre-validator outcomes remain provisional normalization classifications."
  - version: 0.1.1
    date: 2026-04-09
    summary: "Tighten capture-surface classification, minimum pre-envelope requirements, validator/writer handoff conditions, and doctrinal crosswalk to the capture-surface support contract."
  - version: 0.1.0
    date: 2026-04-09
    summary: "Draft — define governed capture surface classes, raw-capture versus normalized-intake distinction, fail-closed pre-validator handling, and handoff into validator and writer lanes."
---

# AMD-2026-015-ADD-006 — CANI Collector and Instrumentation Bridge

## 0. Status

| Field | Value |
|-------|--------|
| Status | `ratified` `1.0.0` |
| Parent relationship | Subordinate addendum to `AMD-2026-015` |
| Scope posture | Narrow doctrine bridge for governed capture surfaces, intake-envelope normalization, and validator-cleared handoff into persisted CANI artifact materialization under `AMD-2026-015-ADD-003`. It does not authorize collector implementation, browser instrumentation implementation, database or event-store services, or execution authority. |

---

## 1. Purpose and problem statement

`AMD-2026-015` established the CANI doctrine family.

`AMD-2026-015-ADD-004` established the intake-envelope bridge.

`AMD-2026-015-ADD-005` established the validator/tooling bridge.

A next capture-boundary gap remained.

The repo still needed a governed answer for:

- which capture surfaces are allowed to emit CANI-relevant signals
- what distinguishes raw capture from normalized intake
- how signals normalize into intake envelopes before validator handoff
- how validator-cleared normalized envelopes may hand off into the persisted-artifact writer lane without bypassing governance

This addendum establishes the amendment-layer bridge rule.

`AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.3` provides the corresponding technical support contract. It elaborates capture-surface classes, pre-envelope requirements, fail-closed handling, and validator/writer handoff expectations, but it does not create independent execution authority.

This addendum closes that gap without authorizing collector implementation.

---

## 2. Relationship to AMD-2026-015

This addendum does not replace `AMD-2026-015`.

The parent amendment remains the governing doctrine for:

- the CANI Experience Loop
- the Victory Lap Formula
- the recommendation non-authority rule

This addendum is narrower.

It binds:

- governed capture-surface eligibility
- normalization into intake envelopes
- handoff from normalized intake into validator and writer lanes

It remains subordinate to `AMD-2026-015-ADD-004 — CANI Telemetry Ingestion Envelope and Normalization Bridge` for intake-envelope behavior and to `AMD-2026-015-ADD-005 — CANI Validator and Tooling Bridge` for validator behavior.

`AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` version `0.1.3` provides technical detail for this bridge as follows:

- Section 2: capture-surface classification
- Sections 3-6: raw capture and pre-envelope requirements
- Section 7: fail-closed pre-validator handling
- Section 8: validator and writer handoff expectations

This addendum governs those bridges at the amendment layer and does not enlarge the authority granted by `AMD-2026-015`, `AMD-2026-015-ADD-004`, or `AMD-2026-015-ADD-005`.

If this amendment and `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` are read in tension, this amendment controls at the doctrine layer, and the support contract must be interpreted narrowly so as not to expand authority beyond `AMD-2026-015`, `AMD-2026-015-ADD-004`, or `AMD-2026-015-ADD-005`.

---

## 3. Governed capture-surface bridge rule

Only governed and reviewable capture surfaces **MAY** emit CANI-relevant signals for intake-envelope construction.

The allowed surface classes are:

1. shell/operator flow
2. UI surface observation
3. planning artifacts
4. review artifacts
5. operator note

For avoidance of doubt, these amendment-layer classes map to the implementation-facing `source_surface` values in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` as follows: shell/operator flow -> `shell`; UI surface observation -> `ui_surface`; planning artifacts -> `planning_artifact`; review artifacts -> `review_artifact`; operator note -> `operator_note`.

Implementation-facing controlled values must remain consistent with that support contract and must not introduce additional eligible classes without amendment.

`unknown` is a boundary classification only.

It is not an eligible capture surface for automatic normalization.

If the source surface cannot be resolved beyond `unknown`, the signal **SHALL** be classified as `normalization_blocked` for manual review and **SHALL NOT** be normalized automatically.

No capture surface outside the classes listed in this section is eligible for intake-envelope construction under this addendum.

Pre-validator classification in this section uses the provisional normalization statuses defined in Section 6, not the authoritative validator outcomes defined by `AMD-2026-015-ADD-005`.

---

## 4. Raw-capture and normalization rule

Raw capture is the pre-envelope signal candidate.

Normalized intake is the governed envelope defined by `AMD-2026-015-ADD-004`.

The normalization rule is:

1. capture surfaces may emit bounded raw capture only
2. raw capture becomes governed intake only when it satisfies the intake-envelope contract
3. normalization must preserve provenance, evidence basis, sequence, and boundary discipline
4. normalization must not invent routing, authority, approval, or hidden external support

Raw capture is not yet a governed persisted CANI artifact.

It may exist only as bounded reviewable evidence suitable for later `payload_ref` and `evidence_refs` handling under `AMD-2026-015-ADD-004`.

Before normalization, the capture candidate must preserve all of the following:

- source-surface classification
- signal-family candidate
- signal-type candidate
- repo-local reviewable payload reference
- repo-local evidence basis
- admitted-by attribution
- sequence context sufficient to derive `stream_key` and `sequence_id`, or the signal **SHALL** be classified as `normalization_blocked` when sequence cannot be proven

These elements are the minimum pre-envelope inputs required to construct a compliant intake envelope without inventing required fields.

This section does not convert optional intake-envelope fields under `AMD-2026-015-ADD-004` into mandatory fields unless they are necessary to avoid fabrication or to preserve reviewable provenance.

If any required element is absent, the bridge **SHALL NOT** normalize the signal and **SHALL** classify the signal using the provisional normalization statuses in Section 6, as applicable.

This addendum does not create a second storage universe for raw capture.

A signal that fails these minimum pre-envelope requirements may remain only as non-normalized repo-local reviewable evidence; it must not be treated as a governed intake envelope, a persisted CANI artifact, or a valid writer-lane input.

Such failed or blocked evidence remains intake-adjacent review material only and must not acquire routing, authority, or lifecycle state reserved for intake envelopes or persisted artifacts under `AMD-2026-015-ADD-003` and `AMD-2026-015-ADD-004`.

---

## 5. Validator and writer handoff rule

For purposes of this addendum, the locally defined term `writer lane` means the non-authoritative downstream materialization surface that writes persisted CANI artifacts under the storage contract defined by `AMD-2026-015-ADD-003` and `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001` version `0.1.0`.

The writer lane is not an independent authority surface and remains subordinate to validator outcomes and downstream governance rules.

The writer lane may materialize only the artifact classes, fields, and lifecycle surfaces already authorized by `AMD-2026-015-ADD-003`, `AMD-2026-015-ADD-004`, and their support contracts; it must not create new authority-bearing fields, new persisted location classes, or new routing states.

The handoff sequence **SHALL** be:

1. eligible capture candidate identified
2. normalized intake envelope constructed
3. envelope handed to validator/tooling
4. envelope may proceed to the writer lane only when validator/tooling returns authoritative validator outcome `pass`

Collectors or instrumentation must not:

- write persisted observation artifacts directly
- write persisted recommendation artifacts directly
- bypass validator
- invent recommendation authority
- decide routing acceptance or planning acceptance

A collector, instrumentation surface, or normalization bridge **SHALL NOT** treat validator outcome `advisory_warning` as writer-lane admission.

Under this addendum, validator outcome `advisory_warning` remains within validator-governed review handling and does not authorize writer-lane materialization.

Routing acceptance, planning acceptance, and review acceptance remain governed by the downstream lane documents that own those decisions.

---

## 6. Fail-closed outcome rule before validator handoff

Before validator handoff, capture normalization must already distinguish provisional normalization statuses:

- `normalization_pass`
- `normalization_fail`
- `normalization_blocked`
- `normalization_advisory_warning`

These statuses are pre-validator normalization results only.

They exist to control fail-closed handling before formal validator review and do not replace, mirror, or override the authoritative validator outcomes defined by `AMD-2026-015-ADD-005` and `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001` version `0.1.0`.

The normalization bridge **SHALL** use:

- `normalization_fail` for boundary escape, disallowed source classes, hidden authority dependence, or invented fields
- `normalization_blocked` for missing required evidence, unresolved source class, or missing sequence or provenance data required by the intake-envelope contract to construct a reviewable envelope without invention
- `normalization_advisory_warning` for bounded but caution-bearing interpretation where the signal remains reviewable before validator review
- `normalization_pass` only when the normalized intake envelope can be constructed without violating boundary or integrity rules

Once validator/tooling begins authoritative review, these provisional normalization statuses must not be emitted as final validator outcomes and must be superseded by the outcome model governed by `AMD-2026-015-ADD-005`.

The bridge must fail closed.

It must not silently downgrade hard boundary violations into soft warnings.

---

## 7. Non-authority boundary

Nothing in this addendum authorizes:

- collector implementation
- browser instrumentation implementation
- database schema or migrations
- event-store implementation
- persistence backends outside the governed repo tree
- automatic recommendation execution
- runtime UI modification
- autonomous routing decisions
- silent self-ratification
- silent self-amendment
- approval-lane collapse across architect, UI, review, kernel, or ratification

This addendum governs capture eligibility, normalization discipline, and handoff only.

---

## 8. Implementation follow-through and affected surfaces

This bridge affects the following surfaces:

- the CANI doctrine family under `AMD-2026-015`
- `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001` as the technical support document for capture-surface classification, minimum pre-envelope requirements, and normalization handoff
- future intake-envelope construction helpers under the existing `AMD-2026-015-ADD-004` contract
- validator surfaces governed by `AMD-2026-015-ADD-005` and downstream persisted-artifact materialization surfaces subordinate to `AMD-2026-015-ADD-003` as recipients of valid normalized intake envelopes
- registry, tracker, and review-package surfaces that record discoverability and review state for this amendment package

This pass does not create collectors, browser hooks, background services, storage backends, or execution code.

---

## 9. Out of scope

This addendum does not:

- implement browser/runtime collectors
- define browser instrumentation hooks
- define event-store or database services
- define persistence backends
- authorize automatic recommendation execution
- authorize autonomous routing
- redesign the persisted-artifact materialization path governed by `AMD-2026-015-ADD-003`
- redesign the existing CANI family

---

## 10. Addendum intent summary

The CANI family may now define which capture surfaces are governed, how raw capture becomes normalized intake, and how normalized intake envelopes progress through validator and writer-lane handoff under existing governance boundaries.

Those bridges remain governance-preserving seams, not autonomy or execution authority.
