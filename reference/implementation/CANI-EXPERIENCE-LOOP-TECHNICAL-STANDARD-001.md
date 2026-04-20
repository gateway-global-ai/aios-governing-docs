---
document_id: AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001
version: 0.1.5
status: draft
category: reference
title: CANI Experience Loop technical standard
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
  - doc_id: AMD-2026-015-ADD-006
    title: CANI Collector and Instrumentation Bridge
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
  - doc_id: AIOS-KB-CANI-VICTORY-LAP-001
    title: CANI Experience Loop and Victory Lap Formula
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
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
note: Draft implementation framing for governed experience observation, scoring, and recommendation. Detailed field-level observation and recommendation shapes are defined separately in AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001, persisted artifact/storage handling is defined separately in AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001, telemetry/intake-envelope handling is defined separately in AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001, validator/tooling expectations are defined separately in AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001, and capture-surface / normalization-handoff discipline is defined separately in AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001. This document does not implement runtime telemetry or authorize autonomous change.
---

# AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001

## Purpose

Define the implementation support model for a governed experience loop that can observe interaction burden, score experience quality, and generate recommendations without silently modifying product behavior or governance doctrine.

This document is deliberately narrow.

It defines:

- what the loop observes
- how the loop scores experience
- what kind of recommendation output is allowed
- how those recommendations enter existing governance lanes

Detailed field-level observation and recommendation shapes are defined in `AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001`.

Persisted CANI artifact location and lifecycle handling are defined in `AIOS-CANI-PERSISTED-ARTIFACT-TAXONOMY-AND-STORAGE-CONTRACT-001`.

Telemetry/intake-envelope handling and normalization into that persisted contract are defined in `AIOS-CANI-TELEMETRY-INGESTION-ENVELOPE-AND-NORMALIZATION-CONTRACT-001`.

Validator/tooling expectations across those surfaces are defined in `AIOS-CANI-VALIDATOR-AND-TOOLING-CONTRACT-001`.

Capture-surface eligibility and handoff into intake, validator, and writer lanes are defined in `AIOS-CANI-CAPTURE-SURFACE-AND-NORMALIZATION-HANDOFF-CONTRACT-001`.

It does not implement the runtime loop.

## Scope

**In scope**

- governed observation dimensions for experience review
- experience-scoring vocabulary
- familiarity and repeat-path interpretation
- recommendation classes
- authority boundaries for recommendation use
- declared-input discipline for architect, UI, and Ollama-assisted runs

**Out of scope**

- telemetry infrastructure
- browser/runtime instrumentation
- autonomous UI change
- autonomous architect change
- silent doctrine mutation
- committee, peer review, kernel review, or ratification replacement

## Core loop contract

The CANI experience loop is:

1. **observe**
2. **score**
3. **recommend**
4. **route to governed review**

It is not:

1. observe
2. score
3. modify the system automatically

## Observation dimensions

The loop observes experience through recorded interaction structure.

Minimum observation dimensions:

| Dimension | Meaning | Notes |
|-----------|---------|-------|
| `intent` | The declared or inferred user goal being pursued | Aligns conceptually with the intent model in `AIOS-SPEC-009` |
| `path_taken` | The sequence of surfaces, steps, or tool-mediated actions used to pursue the goal | This is the core journey record |
| `repeated_paths` | Reappearance of materially similar successful paths | Used for familiarity and fluency signals |
| `backtracks` | Reversals, restarts, or returns to a prior step | Indicates friction or failed expectation |
| `fallback_events` | A drop to a broader, less direct, or more manual path | Indicates the preferred path did not hold |
| `outcome_status` | Whether the intended outcome was achieved, partially achieved, or failed | Needed for any recommendation legitimacy |
| `explanation_burden` | How much extra explanation, context, disclosure, or clarification the path demanded | This is event-based burden, not mere elapsed time |

## Burden model

This standard treats burden as the amount of interaction overhead required to reach the outcome.

Relevant burden types include:

- screen burden
- context burden
- explanation burden
- fallback burden
- backtrack burden

The loop should prefer concrete event-based signals over vague feelings.

Examples of useful burden indicators:

- extra screen or surface changes required to finish the task
- repeated clarification prompts
- explicit fallback to a broader path
- repeated undo / restart behavior
- successful completion only after additional explanatory scaffolding

## Victory Lap Formula

The Victory Lap Formula is the scoring philosophy for the loop.

The strongest experience is the one with:

- the lowest required screen/context burden
- the highest intent-to-outcome ratio
- the lowest fallback/backtrack burden
- the highest repeat-path fluency

### Scoring interpretation

| Signal | Better state | Worse state |
|--------|--------------|-------------|
| Screen/context burden | Fewer required surfaces and less explanatory scaffolding | Many required steps just to stay oriented |
| Intent-to-outcome ratio | Direct route from intent to successful result | Multiple detours before the same result |
| Fallback/backtrack burden | Few or no reversals and few manual fallback steps | Repeated reversals, retries, or fallback paths |
| Repeat-path fluency | The same successful route repeats with lower burden | Similar tasks still need heavy re-explanation |

This is a scoring philosophy, not a ratified runtime metric suite.

## Familiarity and engrained paths

This standard allows a familiarity signal based on repeated successful paths.

Rules:

1. familiarity is inferred from recorded repeated success
2. familiarity is not inferred from a literal timer alone
3. a familiar path should generally require less explanation burden than an unfamiliar path
4. a repeated path is only positive if the repeated path is also successful

An engrained path is therefore a path that:

- appears repeatedly
- remains materially similar
- succeeds repeatedly
- shows lower burden than unfamiliar or first-time routes

## Allowed recommendation outputs

The loop may produce recommendations only.

Allowed recommendation classes:

| Class | Meaning | Required downstream lane |
|-------|---------|--------------------------|
| `architect_candidate` | A recommendation that path burden may reflect architecture/control-plane shape | Architect planning / intake wrapper |
| `ui_candidate` | A recommendation that path burden may reflect surface or disclosure design | UI planning / intake wrapper |
| `copy_or_explanation_candidate` | A recommendation that explanatory burden is too high | Drafting / authoring support, then review |
| `knowledge_candidate` | A recommendation that a repeat insight should become a governed knowledge artifact | New reference/article/implementation note or amendment |
| `manual_review_candidate` | A recommendation that the signal is too consequential or ambiguous for automation | Human coordinator or committee intake |

## Non-authority rule

Recommendation output is not authority.

The loop must not:

- mark its own recommendation as approved
- treat a recommendation as ratified policy
- silently rewrite architect or UI plans
- silently edit amendments or specifications
- collapse architect, UI, committee, peer review, kernel, or ratification into one scoring surface

## Governance insertion rule

When recommendations imply change, they must enter an existing governance lane.

The path is:

- recommendation observed
- recommendation documented
- recommendation routed into planning or intake
- human review performed
- normal committee / peer review / ratification rules preserved where applicable

Relevant existing surfaces:

- `AIOS-AMD-PLAN-001` for planning flow
- `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001` for intake/state recording
- `AIOS-REVIEW-PACKET-TAXONOMY-001` for structured review evidence when a proposal reaches review

## Knowledge-input discipline

If architect, UI, or Ollama-assisted runs use this concept set, those runs must use declared and traceable repo inputs.

This means:

1. `CANI-VICTORY-LAP-FORMULA.md`, this technical standard, and `AMD-2026-015` may become required inputs only by explicit manifest declaration
2. discussion-derived insights must be converted into governed repo artifacts before becoming required knowledge
3. undeclared chat summaries, private notes, or silent operator memory must not be treated as authoritative inputs
4. author-like inputs remain subordinate to repo truth and do not override planning templates or human review

## Relationship to existing intent/control-plane governance

This standard does not replace the intent model.

Instead:

- `AIOS-SPEC-009` remains the governing concept for intent, execution, and auditable behavior
- `AMD-2026-013` remains the governance anchor for declared repo structure and path authority
- `AIOS-AMD-PLAN-001` and `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001` remain the lanes through which architect or UI changes must travel

The CANI loop therefore sits above implementation learning and below governance approval.

It can identify experience friction.

It cannot approve the fix.

## Current limits

This repository does not yet define all of the following:

- a ratified telemetry schema for runtime collection
- a ratified event store for experience-loop observations
- a ratified metric-calculation engine for Victory Lap scoring
- ratified policy identifiers specific to CANI recommendation routing

Those are future implementation questions, not permissions granted by this document.
