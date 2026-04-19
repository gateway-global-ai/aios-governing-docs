---
document_id: AMD-2026-015
version: 0.1.6
status: draft
category: amendment
title: CANI Experience Loop and Victory Lap Formula
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
ratification_target: null
supersedes: null
cross_references:
  - doc_id: AMD-2026-005
    title: Workspace Model & Governed Interface Surfaces
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
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
  - doc_id: AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001
    title: CANI Experience Loop technical standard
  - doc_id: AIOS-KB-CANI-VICTORY-LAP-001
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
amendment_history:
  - version: 0.1.6
    date: 2026-04-09
    summary: "Cross-reference ADD-006 collector/instrumentation bridge addendum for governed capture-surface eligibility, normalization into intake envelopes, and handoff into validator and writer lanes."
  - version: 0.1.5
    date: 2026-04-09
    summary: "Cross-reference ADD-005 validator/tooling bridge addendum for validation responsibilities, validation scope, validator outcomes, and routing of validator results."
  - version: 0.1.4
    date: 2026-04-09
    summary: "Cross-reference ADD-004 intake-envelope bridge addendum for telemetry/intake envelopes, provenance, normalization, and mapping into the existing ADD-003 persisted artifact contract."
  - version: 0.1.3
    date: 2026-04-09
    summary: "Cross-reference ADD-003 storage bridge addendum for persisted CANI artifact locations, taxonomy choices, and routing/supersession storage discipline."
  - version: 0.1.2
    date: 2026-04-09
    summary: "Cross-reference ADD-002 schema bridge addendum for CANI observation-record framing, recommendation-record framing, and routing into governed lanes."
  - version: 0.1.1
    date: 2026-04-09
    summary: "Cross-reference ADD-001 bridge addendum for governed knowledge-artifact eligibility, registry visibility, and declared-input discipline."
  - version: 0.1.0
    date: 2026-04-09
    summary: "Draft — define the CANI experience loop, Victory Lap Formula, familiarity signal, governed recommendation boundary, and declared knowledge-input discipline."
---

# AMD-2026-015 — CANI Experience Loop and Victory Lap Formula

## 0. Status

| Field | Value |
|-------|--------|
| Status | `draft` `0.1.6` |
| Scope posture | Narrow doctrine package for governed experience observation, scoring, and recommendation. It does not authorize runtime automation, browser instrumentation, or autonomous self-modification. |

---

## 1. Purpose

This amendment defines how AI OS may reason about experience improvement without collapsing governance authority into a self-modifying loop.

The package formalizes three things:

- the CANI Experience Loop
- the Victory Lap Formula
- the governance boundary between recommendation and approved change

The intent is straightforward:

- observe how users pursue outcomes
- identify where burden appears
- recommend improvements
- require those improvements to pass through the existing governed process

---

## 2. Scope

**In scope**

- governed observation of intent, path, repeated paths, backtracks, fallback events, outcome status, and explanation/context burden
- a scoring philosophy for experience quality
- familiarity and engrained-path interpretation based on recorded repeated success
- recommendation generation as advisory output
- declared knowledge-input rules for architect, UI, and Ollama-assisted runs

**Out of scope**

- runtime telemetry implementation
- browser instrumentation
- silent product mutation
- silent doctrine mutation
- replacement of architect, UI, committee, peer review, kernel review, or ratification authority
- media or Voicebox runtime behavior

---

## 3. Normative decisions

### 3.1 Governed experience observation rule

AI OS experience-improvement logic **MAY** observe the following experience dimensions:

- user intent
- path taken
- repeated paths
- backtracks or reversals
- fallback events
- outcome success or failure
- explanation and context burden

These observations are governed signals only. They are not self-approving authority.

### 3.2 CANI loop rule

The CANI Experience Loop **SHALL** be interpreted as:

1. observe
2. score
3. recommend
4. route to governed review

It **SHALL NOT** be interpreted as:

1. observe
2. score
3. self-modify
4. self-ratify

### 3.3 Victory Lap Formula rule

The Victory Lap Formula **SHALL** be the preferred scoring philosophy for governed experience review.

Under this formula, the best path is the one with:

- the lowest required screen and context burden
- the highest intent-to-outcome ratio
- the lowest fallback and backtrack burden
- the highest repeat-path fluency

This formula is a governance-facing evaluation philosophy. It is not, by itself, a ratified runtime metric engine.

### 3.4 Familiarity signal rule

Repeated successful paths **MAY** be interpreted as a familiarity signal.

That familiarity signal **SHALL** be based on recorded actions and repeated successful routes, not on a literal timer alone.

A familiar path should generally imply:

- less explanation burden
- less context burden
- fewer fallbacks
- higher repeat-path fluency

### 3.5 Recommendation non-authority rule

The system **MAY** observe, score, and recommend.

It **MUST NOT**:

- silently self-ratify
- silently self-amend doctrine
- treat a recommendation as approved change
- collapse architect, UI, committee, peer review, kernel review, or ratification authority into the recommendation engine

Recommendation output is advisory only until it enters the governed process and is reviewed through the proper lane.

### 3.6 Governance-entry rule

If a CANI or Victory Lap recommendation implies product, planning, UI, or doctrine change, that recommendation **SHALL** enter the existing governance process.

Relevant paths include:

- planning and architect/UI lanes under `AIOS-AMD-PLAN-001`
- intake/state recording under `AIOS-AMENDMENT-INTAKE-SCAFFOLD-001`
- review evidence under `AIOS-REVIEW-PACKET-TAXONOMY-001`
- normal committee, peer review, kernel, and ratification lanes where applicable

### 3.7 Knowledge-input discipline rule

Architect, UI, and Ollama-assisted runs **SHALL** use declared and traceable knowledge inputs when they consume experience-loop concepts.

This means:

- `reference/knowledge_base/articles/CANI-VICTORY-LAP-FORMULA.md`
- `reference/implementation/CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001.md`
- this amendment

become required knowledge only when explicitly declared for a run.

Discussion-derived insight **SHALL NOT** become required knowledge until converted into governed repo artifacts with stable paths.

### 3.8 Read-only governance boundary

Nothing in this amendment authorizes:

- silent architect-lane mutation
- silent UI-lane mutation
- automatic amendment editing
- automatic specification editing
- automatic ratification motion generation as final authority

This amendment authorizes governed recommendation only.

---

## 4. Relationship to existing governance

| Instrument | Relationship |
|------------|--------------|
| AMD-2026-005 | Ratification and binding peer-review law remain unchanged. Experience recommendations do not bypass them. |
| AMD-2026-007 / AIOS-SPEC-009 | Intent remains the governing execution concept. This amendment adds experience-review framing around intent paths, not a replacement intent model. |
| AMD-2026-013 | Declared repo paths and architecture/builder path authority remain binding. Experience concepts become required knowledge only through governed repo artifacts. |
| AIOS-AMD-PLAN-001 / intake scaffold | Architect and UI remain the draft-producing lanes for recommendations that imply design change. Human verification remains mandatory. |
| AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001 | Ollama-assisted reasoning about these concepts must remain manifest-declared, traceable, and subordinate to repo truth. |

---

## 5. Required implementation references

The initial governed package for this amendment consists of:

- `reference/knowledge_base/articles/CANI-VICTORY-LAP-FORMULA.md`
- `reference/implementation/CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001.md`
- `amendments/AMD-2026-015-cani-experience-loop-and-victory-lap-formula.md`

These documents define the first governed knowledge and doctrine surface for the concept.

They do not, by themselves:

- create runtime collection
- create automatic recommendation deployment
- create autonomous self-improvement

---

## 6. Non-goals

This amendment does not:

- implement telemetry infrastructure
- implement browser review or media features
- modify the architect lane
- modify the authoring package
- create a silent optimization engine

---

## 7. Amendment intent summary

AI OS may learn from repeated paths, burden, and outcomes.

It may score that learning through the Victory Lap Formula.

It may generate recommendations from that learning.

It may not silently turn those recommendations into approved change.
