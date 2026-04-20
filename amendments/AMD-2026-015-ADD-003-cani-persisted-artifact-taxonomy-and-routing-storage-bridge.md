---
document_id: AMD-2026-015-ADD-003
version: 0.1.0
status: draft
category: amendment
title: CANI Persisted Artifact Taxonomy and Routing Storage Bridge
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
  - doc_id: AIOS-KB-CANI-VICTORY-LAP-001
    title: CANI Experience Loop and Victory Lap Formula
  - doc_id: AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001
    title: CANI Experience Loop technical standard
  - doc_id: AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001
    title: CANI observation and recommendation schema
  - doc_id: AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001
    title: CANI persisted artifact taxonomy and storage contract
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Narrow subordinate addendum to AMD-2026-015 for persisted CANI artifact locations, persisted taxonomy choices, routing linkage, and storage-contract boundaries. It does not authorize runtime persistence implementation or automatic system change.
amendment_history:
  - version: 0.1.0
    date: 2026-04-09
    summary: "Draft — define persisted CANI artifact location classes, observation/recommendation taxonomy, update and supersession rules, and routing-linkage storage boundaries."
---

# AMD-2026-015-ADD-003 — CANI Persisted Artifact Taxonomy and Routing Storage Bridge

## 0. Status

| Field | Value |
|-------|--------|
| Status | `draft` `0.1.0` |
| Parent relationship | Subordinate addendum to `AMD-2026-015` |
| Scope posture | Narrow doctrine bridge for persisted CANI artifact taxonomy and storage contract. It does not create runtime telemetry, browser instrumentation, database migrations, or autonomous optimization authority. |

---

## 1. Purpose and problem statement

`AMD-2026-015` established the CANI doctrine family.

`ADD-001` established governed knowledge-artifact eligibility and discoverability discipline.

`ADD-002` established field-level schema framing for observations and recommendations.

A next storage-contract gap remained.

The repo still needed a governed answer for:

- where persisted CANI observation records live
- where persisted CANI recommendation records live
- which persisted artifacts need identity, status, events, or handoff separation
- how routing, supersession, and archival are represented without pretending runtime implementation already exists

This addendum closes that gap without authorizing runtime persistence implementation.

---

## 2. Relationship to AMD-2026-015

This addendum does not replace `AMD-2026-015`.

The parent amendment remains the governing doctrine for:

- the CANI Experience Loop
- the Victory Lap Formula
- the recommendation non-authority rule

This addendum is narrower.

It binds:

- persisted artifact location classes
- persisted artifact taxonomy choices
- update and supersession storage rules
- routing linkage into existing governed lanes

It remains subordinate to the parent amendment and does not widen the CANI family into runtime storage implementation or self-modifying execution.

---

## 3. Persisted-artifact and storage bridge rule

Persisted CANI records **MAY** exist as governed repo artifacts only when they live under a documented mutable-process location class inside the governed repo.

The bridge rule is:

1. explanatory doctrine and support standards remain under `reference/`
2. persisted CANI process artifacts belong under a governed process-artifact class under `reviews/`
3. ad hoc local storage, machine-local caches, and undeclared exports are not governed persisted artifact locations

This pass defines the location contract only.

It does not implement the persistence generator or runtime writer.

---

## 4. Taxonomy rule

Persisted CANI artifacts do not all require the same split.

The taxonomy rule is deliberately asymmetric:

1. observation persistence uses stable set identity plus append-only event storage
2. recommendation persistence uses identity, status, events, and handoff separation

This difference is intentional.

Observation records are evidence-like signals and do not, by themselves, carry the same mutable routing lifecycle as recommendation packets.

Recommendation records do carry mutable routing, review, supersession, and closure state.

Therefore the governing storage pattern is:

- observation sets: identity + append-only events, with optional handoff note
- recommendation packets: identity + status + events + handoff note

This addendum does not require the full four-file split where mutable workflow truth is absent.

---

## 5. Update and supersession rule

Observation and recommendation persistence **SHALL NOT** be silently rewritten as if prior records never existed.

The governing update rule is:

1. observation records are append-only through their containing observation-set events artifact
2. observation corrections are represented by successor/correction events rather than deletion
3. recommendation identity remains stable
4. recommendation current truth is represented in status
5. recommendation audit history is append-only in events
6. supersession and archival must be represented explicitly rather than by silent removal

Stale or invalid recommendations must be marked as such through the recommendation status surface and corresponding append-only events.

---

## 6. Routing-linkage rule

If a persisted CANI recommendation is intended to influence design, planning, intake, or review work, it **SHALL** expose routing linkage into an existing governed lane.

Permitted linkage targets include:

- architect planning
- UI planning
- amendment intake
- review preparation
- manual governance review

These links must remain subordinate to:

- `AIOS-AMD-PLAN-001`
- `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001`
- `AIOS-REVIEW-PACKET-TAXONOMY-001`

No persisted CANI artifact in this addendum authorizes direct runtime action, direct UI mutation, automatic architect execution, automatic recommendation execution, or bypass of human verification, peer review, kernel review, or ratification.

---

## 7. Non-authority boundary

Nothing in this addendum authorizes:

- telemetry collection implementation by itself
- browser instrumentation by itself
- event-store runtime deployment
- database schema migration design by itself
- automatic recommendation execution
- runtime UI modification
- silent self-ratification
- silent self-amendment
- approval-lane collapse across architect, UI, review, kernel, or ratification

This addendum governs persisted artifact location, taxonomy, and storage-contract discipline only.

---

## 8. Implementation follow-through and affected surfaces

This bridge affects the following surfaces:

- the CANI doctrine family under `AMD-2026-015`
- the new technical support document for persisted artifact taxonomy and storage contract
- future `reviews/cani/...` process-artifact surfaces if later implementation packages materialize them
- planning, intake, and review lanes that may receive routed CANI recommendation packets
- registry, tracker, and review-package surfaces for discoverable governed documentation

This pass does not create runtime storage writers, validators, or database code.

---

## 9. Out of scope

This addendum does not:

- implement runtime telemetry collection
- define browser instrumentation requirements
- define an event-store implementation
- define database migrations
- define persistence code
- authorize automatic recommendation execution
- authorize runtime UI mutation
- authorize autonomous self-improvement
- redesign the existing CANI family

---

## 10. Addendum intent summary

The CANI family may now define where persisted observation and recommendation artifacts belong, how they are separated, and how they route into governed lanes.

Those artifacts remain governed records, not runtime authority.
