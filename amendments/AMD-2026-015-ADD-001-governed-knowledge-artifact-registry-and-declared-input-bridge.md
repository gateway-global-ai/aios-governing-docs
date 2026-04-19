---
document_id: AMD-2026-015-ADD-001
version: 0.1.0
status: draft
category: amendment
title: Governed Knowledge Artifact Registry and Declared-Input Bridge
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
ratification_target: null
supersedes: null
cross_references:
  - doc_id: AMD-2026-015
    title: CANI Experience Loop and Victory Lap Formula
  - doc_id: AIOS-KB-CANI-VICTORY-LAP-001
    title: CANI Experience Loop and Victory Lap Formula
  - doc_id: AIOS-CANI-EXPERIENCE-LOOP-TECHNICAL-STANDARD-001
    title: CANI Experience Loop technical standard
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy (identity, status, events, handoff)
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
note: Narrow bridge addendum to AMD-2026-015 for governed knowledge-artifact eligibility, registry visibility, and declared-input discipline. No runtime telemetry or autonomous optimization authority is granted here.
amendment_history:
  - version: 0.1.0
    date: 2026-04-09
    summary: "Draft — bridge governed knowledge-artifact eligibility, registry/discoverability visibility, and declared-input discipline for architect/UI/Ollama-assisted runs."
---

# AMD-2026-015-ADD-001 — Governed Knowledge Artifact Registry and Declared-Input Bridge

## 0. Status

| Field | Value |
|-------|--------|
| Status | `draft` `0.1.0` |
| Parent relationship | Subordinate addendum to `AMD-2026-015` |
| Scope posture | Narrow bridge addendum. It does not create telemetry contracts, runtime recommendation engines, browser instrumentation, or autonomous system optimization. |

---

## 1. Purpose and problem statement

`AMD-2026-015` established the CANI experience package as governed knowledge, technical framing, and doctrine.

A narrow gap remained:

- a governed knowledge artifact may exist on disk
- that artifact may be conceptually eligible for later architect, UI, or Ollama-assisted use
- but current registry/discovery tooling may not surface that artifact cleanly

This addendum bridges that gap.

It defines how governed knowledge artifacts become eligible for agent use, how registry/discoverability must align with that use, and how declared-input discipline remains explicit and reviewable.

---

## 2. Relationship to AMD-2026-015

This addendum does not replace `AMD-2026-015`.

`AMD-2026-015` remains the parent doctrine for:

- the CANI Experience Loop
- the Victory Lap Formula
- the recommendation non-authority boundary

This addendum is narrower.

It clarifies the bridge between:

- governed knowledge artifacts on disk
- registry/schema/discovery visibility
- declared-input eligibility for architect, UI, and Ollama-assisted runs

---

## 3. Governed knowledge-artifact eligibility rule

Governed knowledge artifacts, including knowledge-base articles, **MAY** be used as agent inputs only when all of the following are true:

1. the artifact exists as a governed repo artifact under a stable repo path
2. the artifact has stable document identity or equivalent governed discoverability metadata
3. the artifact is explicitly declared in the manifest or equivalent declared-input mechanism for the run
4. the artifact remains subordinate to repo truth and higher-governance documents where those control the same subject

Eligibility on disk is not the same as default authority.

These artifacts are valid declared inputs only when explicitly selected for the run.

---

## 4. Registry and discoverability bridge rule

If a governed knowledge artifact is intended to be used by architect, UI, or Ollama-assisted runs, it **SHALL** be visible to the registry/schema/discovery layer.

This addendum does not pretend the current tooling was already fully aligned.

At the time of this addendum:

- governed knowledge-base article artifacts could exist on disk
- current registry tooling did not cleanly surface `reference/knowledge_base/articles/`

Therefore the bridge rule is:

1. governed knowledge artifacts intended for declared-input use must be registry-visible or equivalently discoverable by the repo’s governed tooling
2. when tooling visibility lags behind artifact creation, that mismatch must be treated as a governance/tooling alignment gap, not ignored as if discoverability were already solved
3. registry/discovery tooling must be brought into alignment so declared-input eligibility is reviewable rather than hidden

This is a discoverability bridge, not a runtime authorization.

---

## 5. Declared-input rule

Discussion-derived insights are not valid required inputs until converted into governed repo artifacts with stable paths.

Declared inputs for architect, UI, and Ollama-assisted runs **SHALL** be:

- explicit
- reviewable
- traceable by path and/or document identity
- bounded by the selected run manifest or equivalent declared-input surface

These artifacts do not become hidden default authority merely by existing in the repo.

They remain subordinate to:

- planning templates
- repo truth
- human verification
- committee, peer review, kernel review, and ratification flow where applicable

---

## 6. Non-authority and non-runtime-expansion boundary

Nothing in this addendum authorizes:

- hidden knowledge injection
- undeclared discussion as required knowledge
- silent runtime mutation
- automatic telemetry authorization
- automatic recommendation-engine deployment
- automatic architect or UI approval

This addendum governs eligibility, discoverability, and declared-input discipline only.

---

## 7. Implementation follow-through and affected surfaces

The bridge affects the following surfaces:

- `reference/knowledge_base/articles/` as a valid governed knowledge-artifact location
- `scripts/registry_generator.py` and generated registry outputs for discoverability alignment
- manifest-driven architect, UI, and Ollama-assisted runs that need explicit declared-input reviewability
- amendment/review surfaces for the `AMD-2026-015` package

This addendum does not require a telemetry schema, event store, or runtime scoring engine in the current pass.

---

## 8. Out of scope

This addendum does not:

- define runtime telemetry events
- define a CANI event-store contract
- define browser instrumentation
- define recommendation-engine execution logic
- authorize autonomous self-optimization
- widen `AMD-2026-015` into a broader platform package

---

## 9. Addendum intent summary

Governed knowledge artifacts may become valid agent inputs, but only when they are governed on disk, visible to repo discovery surfaces, and explicitly declared for the run.

Discoverability is part of governance hygiene.

Hidden artifacts are not a valid substitute for declared input authority.
