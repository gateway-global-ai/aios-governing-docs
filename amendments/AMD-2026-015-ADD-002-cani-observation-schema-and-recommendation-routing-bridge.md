---
document_id: AMD-2026-015-ADD-002
version: 0.1.0
status: draft
category: amendment
title: CANI Observation Schema and Recommendation Routing Bridge
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
  - doc_id: AIOS-KB-CANI-VICTORY-LAP-001
    title: CANI Experience Loop and Victory Lap Formula
  - doc_id: AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001
    title: CANI Experience Loop technical standard
  - doc_id: AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001
    title: CANI observation and recommendation schema
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Narrow subordinate addendum to AMD-2026-015 for observation-event schema framing, recommendation-record framing, and routing into governed lanes. It does not authorize runtime telemetry implementation or automatic system change.
amendment_history:
  - version: 0.1.0
    date: 2026-04-09
    summary: "Draft — define CANI observation schema framing, recommendation record framing, routing targets into governed lanes, and explicit non-authority boundaries."
---

# AMD-2026-015-ADD-002 — CANI Observation Schema and Recommendation Routing Bridge

## 0. Status

| Field | Value |
|-------|--------|
| Status | `draft` `0.1.0` |
| Parent relationship | Subordinate addendum to `AMD-2026-015` |
| Scope posture | Narrow doctrine bridge for observation and recommendation schema framing. It does not create runtime telemetry, browser instrumentation, an event store, or autonomous optimization authority. |

---

## 1. Purpose and problem statement

`AMD-2026-015` defined the CANI loop, the Victory Lap Formula, and the recommendation non-authority boundary.

A narrower field-level gap remained.

The repo needed an explicit governed bridge for:

- what a CANI observation record is
- what a CANI recommendation record is
- how those records route into existing governed lanes

Without that bridge, the family could describe observation and recommendation conceptually while leaving the record shape too implicit.

This addendum closes that gap without authorizing runtime implementation.

---

## 2. Relationship to AMD-2026-015

This addendum does not replace `AMD-2026-015`.

The parent amendment remains the governing doctrine for:

- the CANI Experience Loop
- the Victory Lap Formula
- the recommendation non-authority rule

This addendum is narrower.

It binds:

- observation schema framing
- recommendation record framing
- routing into governed review/planning lanes

It remains subordinate to the parent amendment and does not widen the CANI family into runtime telemetry or self-modifying execution.

---

## 3. Observation schema bridge

CANI observation records **MAY** exist as governed schema-defined records when they are used to capture experience signals for reviewable recommendation framing.

At minimum, the governed observation shape **SHALL** include fields for:

1. stable observation identity
2. observed timestamp
3. bounded subject or actor context where appropriate
4. intent identifier when known
5. path identifier or path signature
6. observed step or action
7. outcome state
8. fallback occurrence
9. backtrack or reversal occurrence
10. burden indicators
11. repeated-path or familiarity signal fields where applicable
12. evidence/source surface
13. interpretation limits where needed

This addendum does not claim that all such fields are already collected at runtime.

It defines the governed record shape that later implementation packages must follow if they materialize this concept.

---

## 4. Recommendation record bridge

CANI recommendation records **MAY** exist as governed structured records when one or more observations justify a recommendation candidate.

At minimum, the recommendation record shape **SHALL** include fields for:

1. stable recommendation identity
2. source observation or source signal references
3. recommendation category
4. affected surface or lane
5. rationale
6. proposed burden reduction or path-improvement claim
7. authority status
8. routing target
9. human/governance review requirement
10. routing or disposition status

Recommendation records are advisory records.

They are not equivalent to:

- approved implementation work
- approved architect change
- approved UI change
- approved doctrine change

---

## 5. Routing-to-governed-review rule

If a CANI recommendation implies planning, UI, intake, or review work, that recommendation **SHALL** route into an existing governed lane.

Permitted routing targets include:

- architect planning
- UI planning
- amendment intake / planning
- review preparation
- manual governance review where the signal is ambiguous or consequential

These routes must preserve existing authority boundaries under:

- `AIOS-AMD-PLAN-001`
- `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001`
- `AIOS-REVIEW-PACKET-TAXONOMY-001`

No routing record in this addendum authorizes direct runtime action or bypass of human verification, peer review, kernel review, or ratification where those lanes are applicable.

---

## 6. Non-authority boundary

Nothing in this addendum authorizes:

- telemetry collection implementation by itself
- browser instrumentation by itself
- event-store implementation by itself
- database migration design by itself
- recommendation-engine runtime execution
- automatic UI or runtime modification
- silent self-ratification
- silent self-amendment
- approval-lane collapse across architect, UI, review, kernel, or ratification

This addendum governs schema framing and routing discipline only.

---

## 7. Implementation follow-through and affected surfaces

This bridge affects the following surfaces:

- the CANI doctrine family under `AMD-2026-015`
- the new technical schema/support document for observation and recommendation fields
- planning and intake lanes that may later receive CANI recommendation records
- review surfaces that need to distinguish advisory schema records from approved change
- registry and review-package surfaces for discoverable governed documentation

If later packages materialize these schemas in concrete artifacts, they should preserve the structured discipline already used by the intake and review-packet taxonomy standards.

This pass does not create those concrete artifact files.

---

## 8. Out of scope

This addendum does not:

- implement runtime telemetry collection
- define browser instrumentation requirements
- define an event store
- define storage/database contracts
- authorize automatic recommendation execution
- authorize runtime UI mutation
- authorize autonomous self-improvement
- redesign the existing CANI package

---

## 9. Addendum intent summary

The CANI family may now describe observation records and recommendation records in a governed, reviewable way.

Those records remain advisory.

Their route into the system is governed review, not autonomous execution.
