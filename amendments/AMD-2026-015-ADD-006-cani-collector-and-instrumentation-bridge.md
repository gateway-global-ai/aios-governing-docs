---
document_id: AMD-2026-015-ADD-006
version: 0.1.0
status: draft
category: amendment
title: CANI Collector and Instrumentation Bridge
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
ratification_target: null
supersedes: null
cross_references:
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
note: Narrow subordinate addendum to AMD-2026-015 for governed capture surfaces, normalization into intake envelopes, and handoff into validator and writer lanes. It does not authorize collector implementation, browser instrumentation implementation, database/event-store work, or execution authority.
amendment_history:
  - version: 0.1.0
    date: 2026-04-09
    summary: "Draft — define governed capture surface classes, raw-capture versus normalized-intake distinction, fail-closed pre-validator handling, and handoff into validator and writer lanes."
---

# AMD-2026-015-ADD-006 — CANI Collector and Instrumentation Bridge

## 0. Status

| Field | Value |
|-------|--------|
| Status | `draft` `0.1.0` |
| Parent relationship | Subordinate addendum to `AMD-2026-015` |
| Scope posture | Narrow doctrine bridge for capture surfaces, intake-envelope normalization, and validator/writer handoff. It does not create collector implementations, browser instrumentation implementations, database/event-store services, or execution authority. |

---

## 1. Purpose and problem statement

`AMD-2026-015` established the CANI doctrine family.

`ADD-004` established the intake-envelope bridge.

`ADD-005` established the validator/tooling bridge.

A next capture-boundary gap remained.

The repo still needed a governed answer for:

- which capture surfaces are allowed to emit CANI-relevant signals
- what distinguishes raw capture from normalized intake
- how signals normalize into intake envelopes before validator handoff
- how validated normalized envelopes may hand off into the persisted-artifact writer lane without bypassing governance

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

It remains subordinate to the parent amendment and to `ADD-004` / `ADD-005` for intake-envelope and validator behavior.

---

## 3. Governed capture-surface bridge rule

Only governed and reviewable capture surfaces **MAY** emit CANI-relevant signals for normalization.

The allowed surface classes are:

1. shell/operator flow
2. UI surface observations
3. planning artifacts
4. review artifacts
5. bounded operator notes

Signals outside those classes are not eligible for clean automatic normalization.

They must fail or block rather than being silently treated as governed intake.

---

## 4. Raw-capture and normalization rule

Raw capture is the pre-envelope signal candidate.

Normalized intake is the governed envelope defined by `ADD-004`.

The normalization rule is:

1. capture surfaces may emit bounded raw capture only
2. raw capture becomes governed intake only when it satisfies the intake-envelope contract
3. normalization must preserve provenance, evidence basis, sequence, and boundary discipline
4. normalization must not invent routing, authority, approval, or hidden external support

This addendum does not create a second storage universe for raw capture.

---

## 5. Validator and writer handoff rule

The handoff sequence **SHALL** be:

1. eligible capture candidate identified
2. normalized intake envelope constructed
3. envelope handed to validator/tooling
4. only if validator outcome permits and policy/routing conditions are satisfied may the envelope hand off into the writer lane for persisted artifacts under `ADD-003`

Collectors or instrumentation must not:

- write persisted observation artifacts directly
- write persisted recommendation artifacts directly
- bypass validator
- invent recommendation authority
- decide routing acceptance or planning acceptance

---

## 6. Fail-closed outcome rule before validator handoff

Before validator handoff, capture normalization must already distinguish:

- `pass`
- `fail`
- `blocked`
- `advisory_warning`

Use:

- `fail` for boundary escape, disallowed source classes, hidden authority dependence, or invented fields
- `blocked` for missing required evidence, unresolved source class, or missing required sequence/provenance needed for clean normalization
- `advisory_warning` for bounded but caution-bearing interpretation where the signal remains reviewable
- `pass` only when the normalized intake envelope can be constructed without violating boundary or integrity rules

The bridge must fail closed.

It must not silently downgrade hard boundary violations into soft warnings.

---

## 7. Non-authority boundary

Nothing in this addendum authorizes:

- collector implementation by itself
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
- the new technical support document for capture-surface and normalization handoff
- future intake-envelope construction helpers under the existing `ADD-004` contract
- existing validator and writer lanes as downstream recipients of valid normalized intake envelopes
- registry, tracker, and review-package surfaces for discoverable governed documentation

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
- redesign the approved writer slice
- redesign the existing CANI family

---

## 10. Addendum intent summary

The CANI family may now define which capture surfaces are governed, how raw capture becomes normalized intake, and how valid intake envelopes hand off into validator and writer lanes.

Those bridges remain governance-preserving seams, not autonomy or execution authority.
