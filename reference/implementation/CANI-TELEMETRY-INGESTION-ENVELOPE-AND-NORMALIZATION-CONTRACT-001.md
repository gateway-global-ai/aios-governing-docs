---
document_id: AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001
version: 0.1.1
status: draft
category: reference
title: CANI telemetry ingestion envelope and normalization contract
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
  - doc_id: AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001
    title: CANI persisted artifact taxonomy and storage contract
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Draft telemetry/intake envelope contract for CANI signals. This document defines the pre-persistence ingestion envelope, provenance metadata, sequencing/batching/causal-linkage fields, normalization rules, and mapping into the persisted artifacts already governed by AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001. It does not define a second storage architecture or any runtime implementation.
---

# AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001

## 1. Contract overview

This document defines the telemetry/intake bridge for CANI signals before they become persisted governed artifacts.

Its purpose is narrow:

- define the logical ingestion envelope
- define provenance and sequencing fields
- define normalization rules
- define how admitted envelopes map into the persisted observation and recommendation artifacts already governed by `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001`

This document does not define a second storage tree.

It does not define runtime collectors.

It does not define database tables or migrations.

## 2. Relationship to persisted governed artifacts

The distinction is strict:

1. persisted governed CANI artifacts are the canonical stored records defined by `ADD-003`
2. telemetry/intake envelopes are pre-persistence admission records that feed those stored artifacts

Telemetry/intake envelopes do not replace persisted artifacts.

They are the governed bridge into them.

## 3. Ingestion envelope

Every admitted CANI telemetry/intake signal should use a common envelope.

Minimum envelope fields:

| Field | Required | Meaning |
|-------|----------|---------|
| `ingestion_envelope_id` | yes | Stable envelope identity |
| `envelope_schema_version` | yes | Version of the ingestion-envelope contract |
| `recorded_at` | yes | Time the envelope was admitted into governed intake handling |
| `signal_family` | yes | High-level signal family |
| `signal_type` | yes | Specific signal type |
| `source_surface` | yes | Surface from which the signal originated |
| `source_artifact_ref` | optional | Repo-relative source artifact when applicable |
| `provenance` | yes | Provenance metadata block |
| `sequence` | yes | Sequencing metadata block |
| `normalization_state` | yes | Current normalization posture |
| `payload_ref` | yes | Reference to the raw or normalized signal body |
| `evidence_refs` | yes | Evidence paths or source references |
| `notes` | optional | Bounded explanatory note |

### Controlled values

#### `signal_family`

- `observation_intake`
- `recommendation_intake`
- `governance_correction`

#### `source_surface`

- `shell`
- `ui_surface`
- `planning_artifact`
- `review_artifact`
- `operator_note`
- `unknown`

#### `normalization_state`

- `raw_captured`
- `normalized`
- `mapped_to_persisted_artifact`
- `rejected`

### `payload_ref` boundary

`payload_ref` is a reviewable reference only.

It may point to:

- a governed repo artifact
- a review-package artifact
- a bounded intake-evidence artifact captured for review

It must not be treated as governing authority by itself.

If `payload_ref` points to raw or not-yet-governed intake material, that material is intake evidence only.

It does not become valid governing authority merely because the envelope points to it.

Normalized and persisted CANI artifacts governed by `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001` remain authoritative over the intake envelope.

Undeclared external material must not become hidden authority through `payload_ref`.

## 4. Provenance fields

The provenance block exists so a signal can be reviewed before and after normalization.

Minimum provenance fields:

| Field | Required | Meaning |
|-------|----------|---------|
| `observed_by` | optional | Actor or surface that observed the signal |
| `admitted_by` | yes | Actor or governed process that admitted the envelope |
| `confidence` | optional | Confidence in the interpretation |
| `interpretation_limit` | optional | Known ambiguity or limitation |
| `evidence_basis` | yes | Short statement of what evidence supports admission |

Controlled values for `confidence`:

- `low`
- `medium`
- `high`

## 5. Sequence, batch, and causal linkage fields

The intake envelope must support ordering and relationship tracking without defining a runtime event-store service.

Minimum sequence/linkage fields:

| Field | Required | Meaning |
|-------|----------|---------|
| `stream_key` | yes | Logical stream identifier for the intake sequence |
| `sequence_id` | yes | Monotonic order within the logical stream |
| `batch_id` | optional | Batch identity when multiple envelopes are admitted together |
| `causal_parent_id` | optional | Prior envelope or signal that causally led to this one |
| `related_observation_set_id` | optional | Existing observation set target if already known |
| `related_recommendation_id` | optional | Existing recommendation target if already known |

Rules:

1. `sequence_id` must increase monotonically within a `stream_key`
2. `batch_id` is optional and does not replace sequence order
3. `causal_parent_id` is for lineage only and does not imply approval or authority

## 6. Normalization rules

Normalization is the governed conversion of an intake envelope into the already-defined CANI schema and persisted artifact surfaces.

The normalization rule is:

1. a raw or lightly structured signal may be admitted as an intake envelope
2. normalization converts that envelope into the field model defined by `AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001`
3. mapping then places the normalized result into the persisted artifact classes defined by `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001`

Normalization must not silently invent provenance, routing, or approval status.

If support is insufficient, the envelope should remain `rejected` rather than being force-normalized.

## 7. Mapping into existing persisted artifacts

This contract maps into the existing `ADD-003` storage contract only.

### Observation mapping

Observation-intake envelopes map into:

- `reviews/cani/observation_sets/<set_slug>/OBSERVATION_SET_EVENTS.yaml`

Mapping output:

- normalized observation fields from `AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001`
- append-only observation-set event admission under the `ADD-003` persisted contract

### Recommendation mapping

Recommendation-intake envelopes map into:

- `reviews/cani/recommendations/<recommendation_slug>/RECOMMENDATION_IDENTITY.yaml`
- `reviews/cani/recommendations/<recommendation_slug>/RECOMMENDATION_STATUS.yaml`
- `reviews/cani/recommendations/<recommendation_slug>/RECOMMENDATION_EVENTS.yaml`

Mapping output:

- normalized recommendation fields from `AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001`
- persisted recommendation current truth and append-only history under the `ADD-003` persisted contract

This document does not add any new persisted location class beyond those already defined by `ADD-003`.

## 8. Known limits / not yet implemented

This package does not yet define:

- runtime telemetry collectors
- browser instrumentation
- runtime writers
- event-store services
- database schemas or migrations
- automatic recommendation execution

The contract defines the governed intake envelope only.
