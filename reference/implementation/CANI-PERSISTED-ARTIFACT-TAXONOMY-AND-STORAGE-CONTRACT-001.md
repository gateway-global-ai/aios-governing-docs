---
document_id: AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001
version: 0.1.0
status: draft
category: reference
title: CANI persisted artifact taxonomy and storage contract
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
  - doc_id: AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001
    title: CANI observation and recommendation schema
  - doc_id: AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001
    title: CANI telemetry ingestion envelope and normalization contract
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
note: Draft storage-contract and artifact-taxonomy support document for persisted CANI observation and recommendation records. Telemetry/intake-envelope handling that feeds these artifacts is defined separately in AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001. This document defines governed repo locations, persisted artifact classes, and lifecycle/supersession rules only. It does not implement collection, persistence code, or database infrastructure.
---

# AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001

## 1. Storage-contract overview

This document defines the first governed storage contract for persisted CANI records.

It answers the next narrow question after schema framing:

- where persisted CANI records live
- which persisted artifact classes exist
- which of those artifacts need identity, status, events, or handoff separation
- how routing, supersession, and archival are represented without creating runtime implementation

This document does not create runtime telemetry collection.

It does not create an event store implementation.

It does not create database migrations.

## 2. Artifact location classes

Persisted CANI artifacts belong in a governed mutable-process location class, not in `reference/`.

`reference/` remains the home for doctrine, standards, and explanatory knowledge.

Persisted CANI records are governed process artifacts and therefore belong under `reviews/`.

### Governed location roots

| Artifact family | Governed location class | Reason |
|-----------------|-------------------------|--------|
| Observation sets | `reviews/cani/observation_sets/<set_slug>/` | Observation persistence is reviewable process memory, not normative reference text |
| Recommendation packets | `reviews/cani/recommendations/<recommendation_slug>/` | Recommendation persistence carries mutable routing/review state and must remain auditable |

### What makes a location governed

A persisted CANI location is governed only when all of the following are true:

1. it lives under a documented repo path class
2. it uses the storage contract and schema version defined for that artifact class
3. it has stable ids and repo-relative paths
4. it remains subordinate to architect/UI/intake/review governance rather than acting as authority itself

Ad hoc local folders, operator scratch paths, or machine-local exports are not governed storage locations.

## 3. Observation artifact shape and taxonomy

Observation persistence is narrower than recommendation persistence.

Observation sets do not require a full identity/status/events/handoff split by default.

The reason is structural:

- observation records are evidence-like factual signals
- they are intended to be append-only
- they do not, by themselves, carry the same mutable routing lifecycle as recommendation packets

### Observation set path

```text
reviews/cani/observation_sets/<set_slug>/
├── OBSERVATION_SET_IDENTITY.yaml
├── OBSERVATION_SET_EVENTS.yaml
└── HANDOFF_NOTE.md  # optional
```

### `OBSERVATION_SET_IDENTITY.yaml`

Stable set identity only.

Minimum fields:

- `observation_set_id`
- `set_slug`
- `storage_schema_version`
- `set_path`
- `source_schema_document_id`
- `created_at`
- `created_by`

It must not hold workflow routing state.

### `OBSERVATION_SET_EVENTS.yaml`

Append-only process memory for the set.

Top-level fields:

- `storage_schema_version`
- `observation_set_id`
- `set_slug`
- `events`

Each appended event should carry the observation record fields already defined in `AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001`, plus:

- `event_type`
- `event_id`
- optional `supersedes_observation_id`

Allowed observation-set event types:

- `observation_recorded`
- `observation_correction_recorded`
- `observation_set_status_corrected`

### `HANDOFF_NOTE.md`

Optional only.

Use it when a human reviewer needs orientation or interpretation limits summarized.

If present, it is non-authoritative.

YAML wins over prose.

## 4. Recommendation artifact shape and taxonomy

Recommendation persistence does require stronger separation.

The reason is that recommendation artifacts carry mutable routing, review, supersession, and closure state.

### Recommendation packet path

```text
reviews/cani/recommendations/<recommendation_slug>/
├── RECOMMENDATION_IDENTITY.yaml
├── RECOMMENDATION_STATUS.yaml
├── RECOMMENDATION_EVENTS.yaml
└── HANDOFF_NOTE.md
```

### `RECOMMENDATION_IDENTITY.yaml`

Stable recommendation identity only.

Minimum fields:

- `recommendation_id`
- `recommendation_slug`
- `storage_schema_version`
- `recommendation_path`
- `source_schema_document_id`
- `created_at`
- `created_by`
- `source_observation_refs`

It must not hold mutable routing or review status.

### `RECOMMENDATION_STATUS.yaml`

Current workflow truth for the recommendation packet.

Minimum fields:

- `recommendation_id`
- `recommendation_slug`
- `authority_status`
- `routing_target`
- `routing_state`
- `review_status`
- `artifact_health`
- `supersedes`
- `superseded_by`
- `status_updated_at`
- `status_updated_by`

Controlled values:

#### `authority_status`

- `advisory_only`
- `routed_for_review`
- `accepted_for_planning`
- `rejected`
- `superseded`
- `archived`

#### `routing_state`

- `proposed`
- `routed`
- `accepted`
- `rejected`
- `superseded`
- `archived`

#### `review_status`

- `not_started`
- `pending`
- `in_review`
- `accepted`
- `rejected`
- `superseded`
- `archived`

#### `artifact_health`

- `healthy`
- `stale_evidence`
- `routing_mismatch`
- `incomplete_packet`

### `RECOMMENDATION_EVENTS.yaml`

Append-only recommendation process memory.

Top-level fields:

- `storage_schema_version`
- `recommendation_id`
- `recommendation_slug`
- `events`

Each event contains:

- `event_id`
- `timestamp`
- `actor`
- `event_type`
- `from_state`
- `to_state`
- `summary`
- `evidence_paths`

Allowed recommendation event types:

- `recommendation_initialized`
- `recommendation_routed`
- `recommendation_accepted_for_planning`
- `recommendation_rejected`
- `recommendation_superseded`
- `recommendation_archived`
- `recommendation_status_corrected`

### `HANDOFF_NOTE.md`

Required for recommendation packets.

Its role is operator orientation only.

It must not be the exclusive holder of routing or review state.

## 5. Lifecycle / update / supersession rules

Observation sets and recommendation packets do not mutate the same way.

### Observation sets

1. `OBSERVATION_SET_IDENTITY.yaml` is stable after creation.
2. `OBSERVATION_SET_EVENTS.yaml` is append-only.
3. Observation corrections are represented by appending a correction event with `supersedes_observation_id`; prior observation records are not deleted.
4. Observation sets are archival evidence bundles by default once written; this contract does not define a mutable observation-status file.

### Recommendation packets

1. `RECOMMENDATION_IDENTITY.yaml` remains stable after creation.
2. `RECOMMENDATION_STATUS.yaml` is mutable and holds current routing/review/supersession truth.
3. `RECOMMENDATION_EVENTS.yaml` is append-only.
4. Supersession is represented in both places:
   - current truth in `RECOMMENDATION_STATUS.yaml`
   - audit trail in `RECOMMENDATION_EVENTS.yaml`
5. Stale or invalid recommendations must not be deleted silently; they should be marked by `artifact_health`, `review_status`, `authority_status`, and a corresponding append-only event.
6. Archival is represented by status and event, not by deletion.

## 6. Routing link fields

Persisted recommendation packets must be linkable into existing governed lanes.

Minimum routing-link fields:

- `routing_target`
- `linked_amendment_slug`
- `linked_planning_path`
- `linked_intake_path`
- `linked_review_path`
- `routing_note`

Not every field is required for every packet.

But a routed recommendation must expose enough metadata for a reviewer to answer:

- where this recommendation is going
- which governed surface is expected to receive it
- whether it has actually entered that lane yet

Allowed linkage targets remain:

- architect planning
- UI planning
- amendment intake
- review preparation
- manual governance review

## 7. Reviewability / traceability metadata

Minimum metadata across persisted CANI artifacts should include:

- stable record id
- schema/storage version
- created timestamp
- created by / observed by where applicable
- authority status where applicable
- routing target where applicable
- evidence refs
- supersedes / superseded_by where applicable
- review status where applicable

This is enough to make the records reviewable, traceable, routable, and supersedable without creating a full implementation stack in this pass.

## 8. Known limits / not yet implemented

This package does not yet define:

- runtime collection mechanisms
- browser instrumentation
- event-store service implementation
- database schema migrations
- retention automation
- persistence tooling code
- recommendation execution logic

The contract defines where these artifacts belong and how they should be structured if later implementation packages materialize them.
