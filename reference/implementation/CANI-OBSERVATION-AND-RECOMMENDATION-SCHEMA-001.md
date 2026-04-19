---
document_id: AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001
version: 0.1.2
status: draft
category: reference
title: CANI observation and recommendation schema
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
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
  - doc_id: AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001
    title: CANI Experience Loop technical standard
  - doc_id: AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001
    title: CANI persisted artifact taxonomy and storage contract
  - doc_id: AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001
    title: CANI telemetry ingestion envelope and normalization contract
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Draft schema/support document for CANI observation and recommendation records. Persisted artifact/storage handling is defined separately in AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001, and telemetry/intake-envelope handling is defined separately in AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001. This document defines field shapes and routing semantics only. It does not implement collection, storage, or runtime execution.
---

# AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001

## 1. Schema overview

This document defines the first field-level schema framing for CANI observation records and CANI recommendation records.

It exists to answer a narrow question:

- if the CANI family is allowed to observe, score, and recommend
- what is the governed shape of those observations and recommendations

This document does not create runtime telemetry collection.

It does not create an event store.

It does not create a database contract.

It defines the schema surfaces only.

Persisted artifact location and lifecycle handling are defined separately in `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001`.

Telemetry/intake-envelope handling is defined separately in `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001`.

## 2. Observation event fields

The observation event is the conceptual record of an experience signal.

Minimum observation event shape:

| Field | Required | Meaning |
|-------|----------|---------|
| `observation_id` | yes | Stable observation identity |
| `observed_at` | yes | Timestamp of the recorded observation |
| `subject_context` | optional | Bounded actor/subject context if appropriate for the signal |
| `intent_id` | optional | Intent identifier when known or resolvable |
| `path_signature` | yes | Stable path identifier or path signature for the observed route |
| `step_action` | yes | The step, action, or transition being recorded |
| `outcome_state` | yes | Result state for the observed step or path |
| `fallback_occurred` | yes | Whether fallback happened in the observed path |
| `backtrack_occurred` | yes | Whether reversal/backtrack happened in the observed path |
| `burden_summary` | yes | Summary surface for burden indicators |
| `repeat_path_signal` | optional | Repeated-path signal summary where applicable |
| `evidence_surface` | yes | Source surface or evidence surface for the observation |
| `interpretation_confidence` | optional | Confidence in the interpretation of the signal |
| `notes` | optional | Human-readable bounded note for ambiguity or context |

### Controlled values

#### `outcome_state`

- `success`
- `partial_success`
- `failed`
- `abandoned`
- `unknown`

#### `evidence_surface`

- `shell`
- `ui_surface`
- `planning_artifact`
- `review_artifact`
- `operator_note`
- `unknown`

#### `interpretation_confidence`

- `low`
- `medium`
- `high`

## 3. Burden / fallback / backtrack fields

Burden is represented as a bounded field model rather than a vague narrative.

### `burden_summary`

Suggested shape:

| Field | Required | Meaning |
|-------|----------|---------|
| `visible_burden_level` | yes | Overall screen or visible interaction burden |
| `context_burden_level` | yes | How much contextual scaffolding was required |
| `explanation_burden_level` | yes | How much extra explanation or clarification was required |
| `path_efficiency_state` | yes | Whether the route was direct, detoured, recovered, or stalled |

Controlled values:

#### `visible_burden_level`

- `low`
- `medium`
- `high`
- `unknown`

#### `context_burden_level`

- `low`
- `medium`
- `high`
- `unknown`

#### `explanation_burden_level`

- `low`
- `medium`
- `high`
- `unknown`

#### `path_efficiency_state`

- `direct`
- `detoured`
- `recovered`
- `stalled`
- `unknown`

### Fallback fields

| Field | Required | Meaning |
|-------|----------|---------|
| `fallback_occurred` | yes | Whether fallback happened |
| `fallback_type` | optional | What kind of fallback occurred |
| `fallback_count` | optional | Count of fallback occurrences if known |

Controlled values for `fallback_type`:

- `manual_fallback`
- `broader_path_fallback`
- `explanation_fallback`
- `surface_fallback`
- `unknown`

### Backtrack fields

| Field | Required | Meaning |
|-------|----------|---------|
| `backtrack_occurred` | yes | Whether reversal/backtrack happened |
| `backtrack_count` | optional | Count of reversals if known |
| `reversal_marker` | optional | Marker for restart, undo, or reverse navigation behavior |

Controlled values for `reversal_marker`:

- `restart`
- `undo`
- `reverse_navigation`
- `repeat_attempt`
- `unknown`

## 4. Familiarity / repeat-path signal fields

The familiarity signal is represented as a governed recorded-action signal.

It is not:

- hidden memory
- mysticism
- a literal timer requirement

It is a representation of repeated successful path patterns.

Suggested field shape:

| Field | Required | Meaning |
|-------|----------|---------|
| `repeat_path_observed` | yes | Whether a materially similar path has been observed before |
| `repeat_path_count` | optional | Count of materially similar successful paths if known |
| `repeat_path_success_rate_hint` | optional | Qualitative success-rate hint for the repeated path |
| `familiarity_state` | optional | Governed familiarity signal for recommendation framing |

Controlled values:

#### `repeat_path_success_rate_hint`

- `low`
- `mixed`
- `high`
- `unknown`

#### `familiarity_state`

- `none`
- `emerging`
- `engrained`
- `unknown`

## 5. Recommendation record fields

The recommendation record is the conceptual record created from one observation or a set of observations.

Minimum recommendation record shape:

| Field | Required | Meaning |
|-------|----------|---------|
| `recommendation_id` | yes | Stable recommendation identity |
| `created_at` | yes | Timestamp of recommendation creation |
| `source_observation_refs` | yes | Observation ids or equivalent source-signal references |
| `recommendation_category` | yes | Category of recommendation |
| `affected_surface` | yes | Surface or lane affected by the recommendation |
| `rationale` | yes | Why the recommendation exists |
| `proposed_improvement_claim` | yes | Claimed burden reduction or path-improvement outcome |
| `authority_status` | yes | Explicit authority posture |
| `routing_target` | yes | Where the recommendation should go next |
| `governance_review_required` | yes | Whether human/governance review is required |
| `routing_state` | yes | Current routing lifecycle state |
| `notes` | optional | Bounded explanatory note |

Controlled values:

#### `recommendation_category`

- `architect_candidate`
- `ui_candidate`
- `planning_candidate`
- `intake_candidate`
- `review_preparation_candidate`
- `manual_review_candidate`

#### `affected_surface`

- `architect_lane`
- `ui_lane`
- `planning_packet`
- `intake_packet`
- `review_packet`
- `mixed`
- `unknown`

#### `authority_status`

- `advisory_only`
- `routed_for_review`
- `accepted_for_planning`
- `rejected`
- `superseded`

#### `routing_target`

- `architect_planning`
- `ui_planning`
- `amendment_intake`
- `review_preparation`
- `manual_governance_review`

#### `routing_state`

- `proposed`
- `routed`
- `accepted`
- `rejected`
- `superseded`

## 6. Routing targets / routing states

Recommendation records must route into existing governed lanes.

### Allowed routing targets

| Routing target | Existing lane |
|----------------|---------------|
| `architect_planning` | `AIOS-AMD-PLAN-001` architect lane |
| `ui_planning` | `AIOS-AMD-PLAN-001` UI lane |
| `amendment_intake` | `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001` intake/state surface |
| `review_preparation` | Review preparation surface before binding review |
| `manual_governance_review` | Human/operator/governance review when signals are ambiguous or consequential |

### Routing rule

No recommendation record in this schema authorizes:

- direct runtime action
- direct browser modification
- automatic architect execution
- automatic UI execution
- automatic ratification or doctrine mutation

The schema defines how a recommendation is described and where it is sent, not permission to execute the recommendation.

## 7. Authority status model

The authority model is intentionally narrow.

1. `advisory_only` is the default
2. `routed_for_review` means the recommendation has entered a governed lane
3. `accepted_for_planning` means a human-governed lane has accepted it as planning input
4. `rejected` and `superseded` remain governance outcomes, not model self-judgments

This model prevents the schema from being mistaken for an approval engine.

## 8. Known limits / not yet implemented

This package does not yet define:

- runtime collection mechanisms
- browser instrumentation
- an event store or persistence implementation
- database migrations
- automatic recommendation generation logic
- automatic recommendation execution logic

If these schemas are later embodied in governed artifacts, they should preserve the structured-discipline patterns already used in `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001` and `AIOS-REVIEW-PACKET-TAXONOMY-001`.
