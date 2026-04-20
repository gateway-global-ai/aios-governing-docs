---
document_id: AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001
version: 1.0.0
status: ratified
category: reference
title: CANI capture surface and normalization handoff contract
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
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
  - doc_id: AMD-2026-015-ADD-006
    title: CANI Collector and Instrumentation Bridge
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
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Ratified capture-surface and normalization-handoff contract for CANI. This document defines allowed governed capture surfaces, raw-capture versus normalized-intake distinction, pre-envelope boundary rules, and handoff from normalized intake envelopes into validator and writer lanes. It does not implement collectors, browser instrumentation, database/event-store services, or execution authority.
amendment_history:
  - version: 1.0.0
    date: 2026-04-09
    summary: "Ratified in lockstep with AMD-2026-015-ADD-006 v1.0.0; substantive content frozen from v0.1.3 support-contract revision."
  - version: 0.1.3
    date: 2026-04-09
    summary: "Add non-normative example of non-normalized repo-local reviewable evidence and align support-contract references with the final ADD-006 seam-tightening pass."
---

# AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001

## 1. Contract overview

This document defines the next narrow bridge in the CANI family:

- which governed capture surfaces are eligible to emit CANI-relevant signals
- how those signals become normalized intake envelopes
- how valid normalized intake envelopes hand off into validator and writer lanes

This document does not implement collectors.

It does not implement browser instrumentation.

It does not implement database or event-store services.

## 2. Allowed capture surface classes

Only the following governed capture surface classes are eligible to emit CANI-relevant signals for intake-envelope construction:

| Surface class | Source surface value | Typical evidence basis | Authority posture |
|---------------|----------------------|------------------------|-------------------|
| Shell/operator flow | `shell` | repo-local shell/session evidence, governed command traces, operator-reviewed shell artifacts | advisory until normalized, validated, and reviewed |
| UI surface observation | `ui_surface` | operator-observed UI evidence, governed screenshots, reviewable UI artifacts | advisory only in this pass; no browser instrumentation implementation is authorized |
| Planning artifacts | `planning_artifact` | repo-local planning documents, architect/UI plans, planning packets | may contribute authoritative evidence basis when the artifact itself is governed and reviewable |
| Review artifacts | `review_artifact` | peer-review packets, review synthesis, governed review docs | may contribute authoritative evidence basis when the artifact itself is governed and reviewable |
| Operator note | `operator_note` | bounded, reviewable operator-authored note or handoff artifact | human/operator evidence may be authoritative about observation context when explicitly recorded and reviewable |

`unknown` remains a boundary classification only.

It is not an eligible capture surface for clean automatic normalization.

If the source surface cannot be resolved beyond `unknown`, the signal SHALL be classified as `normalization_blocked` for manual review and SHALL NOT be normalized automatically.

## 3. Raw capture versus normalized intake

The distinction is strict:

1. raw capture is the pre-envelope signal candidate emitted from an allowed capture surface
2. normalized intake is the governed envelope produced under `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001`

Raw capture is not yet a governed persisted CANI artifact.

Raw capture may exist only as bounded reviewable evidence referenced by `payload_ref` and `evidence_refs`.

This contract does not create a new canonical storage universe for raw capture.

The existing intake-envelope contract remains the first governed storage and routing boundary.

## 4. Minimum pre-envelope capture requirements

Before an intake envelope may be constructed, the capture candidate must preserve enough information to satisfy the envelope contract without inventing fields later.

Minimum pre-envelope requirements:

- eligible capture surface class
- source-surface classification
- signal-family candidate
- signal-type candidate
- repo-local reviewable payload reference candidate
- repo-local evidence basis candidate
- admitted-by candidate
- sequence context sufficient to derive `stream_key` and `sequence_id`, or the signal SHALL be classified as `normalization_blocked` when sequence cannot be proven

These minimums are the inputs required to construct a compliant intake envelope without inventing required fields later.

They do not convert optional intake-envelope fields into mandatory fields unless omission would require fabrication or would break reviewable provenance.

If these minimums are absent, the signal is not eligible for clean normalization into an intake envelope.

Non-normative example: a repo-local markdown handoff note or shell transcript excerpt retained for human review may remain non-normalized reviewable evidence when these minimums are missing, but it is not an intake envelope or a persisted CANI artifact.

## 5. Provenance and evidence preservation

Capture surfaces must preserve provenance before validator handoff.

At minimum, the normalization bridge must preserve:

- who observed or admitted the signal where known
- the evidence basis used to justify envelope construction
- repo-local `payload_ref`
- repo-local `evidence_refs`
- interpretation limits where ambiguity exists

Instrumentation remains subordinate to human/operator evidence when:

- evidence interpretation is ambiguous
- boundary classification is uncertain
- the capture candidate depends on judgment rather than direct recorded structure

The capture surface may report.

It may not silently claim authority.

## 6. Sequence and causal-linkage expectations

This bridge preserves sequence and causal linkage without inventing database or event-store dependencies.

Rules:

1. if the capture surface can prove a stream and order, it should preserve enough information to derive `stream_key` and `sequence_id`
2. if a batch exists, it may preserve a batch grouping hint
3. if a causal parent is known, it may preserve a causal-link hint
4. if sequence or causal linkage cannot be proven, the bridge must not invent them

When sequence or causal linkage is missing but optional, the envelope may still normalize with explicit limits.

When the missing linkage makes the envelope materially incomplete for routing or interpretation, the bridge should block rather than fabricate.

## 7. Ineligible capture and fail-closed handling

The bridge must fail closed before validator handoff when capture data is incomplete, ambiguous, or boundary-violating.

Pre-validator classification must use provisional normalization statuses rather than authoritative validator outcomes:

### `normalization_fail`

Use when:

- the capture surface is outside the allowed governed classes
- `payload_ref` or evidence references escape the repo boundary
- external or hidden authority is required to interpret the signal
- normalization would require invented provenance, routing, or approval state

### `normalization_blocked`

Use when:

- required evidence basis is missing
- sequence or causal linkage required for clean interpretation cannot be proven
- source-surface classification remains `unknown`
- the signal cannot yet satisfy the minimum intake-envelope contract

### `normalization_advisory_warning`

Use when:

- the signal is bounded and reviewable
- the evidence is sufficient for intake-envelope construction
- but interpretation limits or confidence cautions should remain attached for downstream review

### `normalization_pass`

Use only when:

- the capture candidate is eligible
- the envelope can be constructed without inventing boundary-sensitive fields
- repo-local evidence and provenance are preserved cleanly

## 8. Handoff into validator and writer lanes

The handoff sequence is:

1. eligible capture candidate identified
2. normalization bridge constructs an intake envelope under `ADD-004`
3. intake envelope is handed to validator/tooling under `ADD-005`
4. only if validator/tooling returns authoritative validator outcome `pass`, the normalized envelope may hand off into the persisted-artifact writer lane governed by `ADD-003`

Hard rules:

- collectors or instrumentation must not write persisted observation or recommendation artifacts directly
- collectors or instrumentation must not bypass validator
- collectors or instrumentation must not invent recommendation authority or routing outcomes
- writer-lane materialization remains subordinate to the persisted-artifact contract and validator outcome
- validator outcome `advisory_warning` does not authorize writer-lane materialization under this contract

## 9. Human/operator authority and review seams

Human/operator evidence remains authoritative for:

- operator notes explicitly recorded as reviewable repo artifacts
- manual interpretation of ambiguous UI or shell observations
- adjudicating boundary questions that instrumentation cannot resolve cleanly

Instrumentation remains advisory.

It may surface signals and preserve structure.

It does not decide:

- recommendation authority
- routing acceptance
- planning acceptance
- review or ratification outcomes

## 10. Seam to future collector implementation work

This bridge exists to make the next implementation slice obvious without authorizing it prematurely.

What a future implementation package may build on top of this bridge:

- deterministic intake-envelope construction from one governed capture surface class
- bounded collector implementation for one already-authorized surface class

What remains out of scope here:

- browser hooks
- telemetry daemons
- event ingestion services
- persistence backends outside the governed repo tree
- autonomous routing or execution authority

This document defines the bridge only.
