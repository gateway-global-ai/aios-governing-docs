---
document_id: AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001
version: 0.1.0
status: draft
category: reference
title: CANI validator and tooling contract
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
  - doc_id: AMD-2026-015-ADD-005
    title: CANI Validator and Tooling Bridge
  - doc_id: AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001
    title: CANI Experience Loop technical standard
  - doc_id: AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001
    title: CANI observation and recommendation schema
  - doc_id: AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001
    title: CANI persisted artifact taxonomy and storage contract
  - doc_id: AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001
    title: CANI telemetry ingestion envelope and normalization contract
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Draft validator/tooling contract for CANI persisted artifacts and intake-envelope artifacts. This document defines validation responsibilities, validation scope, validator outcomes, and routing of validator results only. It does not implement runtime validators, collectors, writers, or database infrastructure.
---

# AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001

## 1. Validator and tooling overview

This document defines the validator/tooling contract for the CANI family.

Its purpose is narrow:

- preserve artifact integrity
- prevent drift between intake-envelope and persisted artifact layers
- enforce required fields and controlled values
- enforce routing-link consistency
- enforce update and supersession discipline
- surface violations for governed review instead of silently correcting authority-bearing records

This document does not create runtime validator code.

It defines the validator/tooling contract only.

## 2. Persisted observation validation requirements

Persisted observation validation applies to the observation-set artifacts defined by `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001`.

Minimum validation responsibilities:

1. verify stable identity fields in `OBSERVATION_SET_IDENTITY.yaml`
2. verify required metadata such as `observation_set_id`, `set_slug`, `storage_schema_version`, `set_path`, and source-schema references
3. verify append-only event/history integrity in `OBSERVATION_SET_EVENTS.yaml`
4. verify that observation corrections are represented by successor/correction events rather than silent deletion
5. verify any routing-link fields if present
6. verify any supersession or archival indicators if present

Observation sets are allowed to be corrected only through append-only correction recording.

Validators must treat silent deletion or silent rewrite of prior observation events as a failure condition.

## 3. Persisted recommendation validation requirements

Persisted recommendation validation applies to the recommendation packet artifacts defined by `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001`.

Minimum validation responsibilities:

1. verify integrity across `RECOMMENDATION_IDENTITY.yaml`, `RECOMMENDATION_STATUS.yaml`, `RECOMMENDATION_EVENTS.yaml`, and `HANDOFF_NOTE.md`
2. verify identity fields and source-observation linkage in `RECOMMENDATION_IDENTITY.yaml`
3. verify controlled authority-status, routing-target, routing-state, review-status, and artifact-health values in `RECOMMENDATION_STATUS.yaml`
4. verify recommendation lifecycle and supersession consistency between current status and append-only events
5. verify rejection, supersession, and archival consistency
6. verify evidence-linkage consistency where evidence refs are claimed
7. verify that `HANDOFF_NOTE.md` is non-authoritative and does not become the sole holder of routing or review truth

Validators must fail when mutable workflow truth contradicts append-only history or when recommendation current truth is incomplete or structurally inconsistent.

## 4. Intake-envelope validation requirements

Intake-envelope validation applies to the telemetry/intake envelopes defined by `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001`.

Minimum validation responsibilities:

1. verify stable envelope identity
2. verify required provenance fields
3. verify sequence, batch, and causal-linkage fields where present
4. verify `normalization_state` against the controlled values
5. verify `payload_ref` boundary compliance
6. verify mapping references into persisted artifacts where mapping is claimed
7. verify rejection handling for invalid or unsupported intake envelopes

Validators must treat the following as failure conditions:

- missing required provenance
- invalid normalization-state values
- `payload_ref` used as a hidden-authority surface
- claimed mapping into persisted artifacts without valid target references

## 5. Validator outcome model

The validator outcome model is intentionally narrow.

Allowed outcomes:

| Outcome | Meaning | Effect |
|---------|---------|--------|
| `pass` | No blocking integrity issue detected | Artifact or envelope may proceed to the next governed step |
| `fail` | A blocking integrity or policy violation exists | Persistence, routing, or review advancement must not proceed as if valid |
| `blocked` | Validation cannot be completed because required inputs or references are missing | Human/governed review is required before advancement |
| `advisory_warning` | Non-blocking issue or caution exists | Does not authorize automatic correction; human/operator judgment may continue with awareness |

Authoritative outcomes are `pass`, `fail`, and `blocked`.

`advisory_warning` is informative only.

Issues that alter authority-bearing records, routing truth, or supersession truth require governed review rather than automatic correction.

## 6. Routing and linkage of validator results

Validator results may link into existing governed lanes, but they do not replace those lanes.

Permitted routing targets include:

- architect planning
- UI planning
- amendment intake
- review preparation
- manual governance review

Minimum routing expectations:

1. a `fail` or `blocked` result may block routing or persistence where integrity cannot be proven
2. a validator result may be attached as evidence to intake, planning, or review surfaces
3. validator results may inform manual governance review when a contradiction or policy risk is detected
4. validator results must not authorize direct runtime action, direct UI mutation, or automatic recommendation execution

## 7. Reviewability and traceability expectations

Validator/tooling outputs should be reviewable and traceable.

Minimum metadata should include:

- target artifact or envelope id
- validator contract version
- validation timestamp
- validation outcome
- summary of blocking or advisory issues
- relevant evidence refs

Validator/tooling should preserve the distinction between:

- current workflow truth
- append-only history
- non-authoritative operator prose

## 8. Known limits / not yet implemented

This package does not yet define:

- runtime validator implementations
- browser instrumentation validation
- event-store service validation
- database schema validation
- automatic record rewriting
- automatic recommendation execution

The contract defines validator/tooling expectations only.
