---
document_id: AMD-2026-014
version: 1.0.0
status: ratified
category: amendment
title: Governed Authoring Knowledge Inputs and Bounded Author-Like Drafting
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
ratification_target: '2026-04-09'
supersedes: null
cross_references:
  - doc_id: AMD-2026-014-RATIFICATION-MOTION
    title: Ratification motion — AMD-2026-014
    relationship: ratification_motion
  - doc_id: AMD-2026-005
    title: Workspace Model & Governed Interface Surfaces
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AMD-2026-009
    title: Intent-Scoped Web Retrieval and Governed Website Review
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
amendment_history:
  - version: 1.0.0
    date: 2026-04-09
    summary: "Ratified per AMD-2026-014-RATIFICATION-MOTION v1.0.0; substantive freeze at draft 0.1.2 after Round 2 triad PASS."
  - version: 0.1.2
    date: 2026-04-09
    summary: "Narrow author revision after completed Round 1 expanded review — defined run record expectations, tightened reviewable traceability requirements, hardened non-compliant output handling, and clarified the authority relationship to the designated support standard."
  - version: 0.1.1
    date: 2026-04-09
    summary: "Narrow author revision after Round 1 gate fail — added definitions, violation consequences, clearer governance cross-references, minimum command-surface disclosure, and a governing-standard-first Section 5."
  - version: 0.1.0
    date: 2026-04-09
    summary: "Draft — declare bounded author-like knowledge inputs, author identity boundaries, manifest discipline, and non-authority rules for governed drafting support."
---

# AMD-2026-014 — Governed Authoring Knowledge Inputs and Bounded Author-Like Drafting

## 0. Status

| Field | Value |
|-------|--------|
| Status | `ratified` `1.0.0` |
| Scope posture | Narrow drafting-governance amendment. It governs author-like knowledge inputs and boundaries. It does not redesign architect/UI planning flow, peer review, committee authority, or ratification. |

---

## 1. Purpose

This amendment defines how bounded author-like drafting support may be used in the AI OS governance repository without collapsing authority into a simulated persona.

The problem is simple:

- style guidance can improve drafting quality
- undeclared or freeform persona simulation can drift into invented authority

This amendment allows the first and blocks the second.

---

## 2. Scope

**In scope**

- declared style cards used as governed knowledge inputs
- declared authoring manifests
- bounded mode definitions
- author identity boundaries
- use of those inputs in designated local drafting tools, including the initial Ollama-based implementation surface
- use of those inputs by architect and UI planning runs only when explicitly declared

**Out of scope**

- automatic doctrine mutation
- ratification shortcuts
- replacing architect or UI templates
- replacing peer review
- replacing committee judgment
- replacing any other governed review or approval lane

---

## 3. Definitions

For this amendment:

- **Author-like drafting support** means governed drafting assistance that may reflect declared repository artifacts for tone, structure, or style, but remains advisory and non-authoritative.
- **Declared knowledge input** means a governed repo artifact explicitly selected for a drafting run by manifest or by another explicit declared input set recorded for that run.
- **Explicit declared input set** means a bounded, reviewable list of repo-relative governed paths recorded in an auditable run record when a manifest is not the selection mechanism.
- **Authoring manifest** means a governed repo artifact that designates required and optionally allowed inputs for a bounded author-like run.
- **Style card** means a governed repo artifact that captures bounded stylistic guidance without becoming doctrine or governance authority.
- **Run record** means the persisted or reviewable execution metadata for a drafting run that records, at minimum, the selected mode, the selected manifest or explicit declared input set, any override identifier, tool invocation identity, and a reviewable timestamp or execution reference.
- **Mode family** means the bounded run family that controls which manifests and style inputs may be paired together, as defined by the designated support standard in Section 6. For the current governed surface, `editorial` and `technical` are one family, and `narration` and `book` are one family.
- **Declared repo truth** means the governed repo artifacts and higher-tier instruments already adopted in this repository, including the Governance Constitution, ratified amendments, and ratified specifications, which remain authoritative over style guidance or generated prose.

---

## 4. Normative decisions

### 4.1 Declared-input rule

Author-like drafting runs **SHALL** use declared knowledge inputs.

Those inputs **SHALL** be:

- inside the governed repo tree
- selected by an authoring manifest or an explicit declared input set recorded for the run
- traceable by path

### 4.2 Discussion-to-artifact rule

Discussion, chat, or private notes **SHALL NOT** become required knowledge for governed author-like runs until they are converted into repo artifacts with stable governed paths.

### 4.3 Bounded author identity rule

Author-like drafting support **MAY** reproduce tone, cadence, and rhetorical structure reflected in declared repo artifacts.

It **SHALL NOT** claim:

- personal memory
- unpublished strategic intent
- private conversations
- governance authority by imitation

### 4.4 Non-authority rule

Generated prose from author-like tools is advisory drafting output only.

It **MUST NOT**:

- self-ratify doctrine
- self-amend doctrine
- self-approve architect output
- self-approve UI output
- bypass committee, peer review, or ratification lanes

### 4.5 Architect and UI planning relationship

Architect and UI planning lanes **MAY** use bounded author-like inputs only when those inputs are explicitly declared for the run.

When used:

- the planning template remains authoritative for output shape
- manifest declaration remains required
- human verification remains required
- style guidance remains subordinate to declared repo truth

### 4.6 Command-surface traceability

Local author-like drafting command surfaces **SHALL** record the following fields in a reviewable run record and **MAY** additionally display them in the command surface:

- selected mode
- selected manifest, or explicit declared input set identifier when no manifest is used
- any override identifier used for optional declared inputs
- tool invocation identity
- a reviewable timestamp or execution reference

They **SHALL NOT** rely on undeclared hidden context as if it were governed knowledge.

If a command surface allows manifest override, that override **SHALL** remain compatible with the selected mode family rather than silently crossing from editorial-family inputs into narration-family inputs, or vice versa.

### 4.7 Non-compliant run consequence

If a run violates the declared-input rule, the discussion-to-artifact rule, the non-authority rule, or the command-surface traceability rule, the resulting output **SHALL** be treated as non-compliant drafting output.

Non-compliant drafting output **SHALL NOT** be treated as:

- governed authority
- a required knowledge input
- architect approval evidence
- UI approval evidence
- committee evidence
- ratification evidence

It may become usable only after a compliant rerun, or after separate governed conversion into an eligible repo artifact under the applicable amendment, specification, or repository-control process.

Non-compliant drafting output **SHALL NOT** be cited as authoritative evidence in planning packets, committee packets, peer-review packets, or ratification materials.

---

## 5. Relationship to existing governance

| Instrument | Relationship |
|------------|--------------|
| AMD-2026-005 §§3, 6 | Supersession, peer-review thresholds, and ratification requirements are unchanged. Author-like drafting support does not bypass those gates. |
| AMD-2026-007 §§11.8-11.9 | Governance enforcement and shell-state authority remain unchanged. This amendment governs bounded drafting inputs, not shell or intent authority. |
| AIOS-SPEC-009 §§9, 12.4, 15.6 | Execution authority, operator trace, and promotion/verification rules remain authoritative. This amendment does not create a parallel execution or approval model. |
| AMD-2026-009 §§6, 9 | External knowledge remains bounded and auditable. Raw external discussion is not silently imported into authoring authority. |
| AMD-2026-013 §§2.1-2.2, 6.1 | Declared repository paths remain architecture/builder-controlled and accountability remains human-assigned. Authoring inputs must use governed paths rather than hidden stores. |
| AIOS-AMD-PLAN-001 — Phase map and Rules | Architect and UI planning remain template-bound draft-producing lanes with human verification. This amendment only constrains optional author-like inputs used inside those lanes. |
| AIOS-AMENDMENT-INTAKE-SCAFFOLD-001 §§1, 5, 8 | Binding posture, human verification, and doctrine-mutation rules remain unchanged. This amendment does not authorize silent mutation or verification bypass. |

---

## 6. Initial designated support standard and implementation surface

The initial designated support standard for this amendment is the governed repo document with document_id `AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001`, currently located at:

- `reference/implementation/AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001.md`

For the purposes of this amendment, that support standard provides implementation guidance for bounded author-like drafting only to the extent that it remains consistent with this amendment. This amendment remains controlling authority if any later draft change to the support standard conflicts with the normative decisions above.

The initial designated implementation surface under that support standard is:

- `reference/knowledge_base/agents/style/JT_EDITORIAL_STYLE_CARD.md`
- `reference/knowledge_base/agents/style/JT_NARRATION_STYLE_CARD.md`
- `reference/knowledge_base/agents/style/JT_AUTHORING_MODE_BOUNDARIES.md`
- `reference/knowledge_base/agents/style/JT_EDITORIAL_REQUIRED_KNOWLEDGE_MANIFEST.yaml`
- `reference/knowledge_base/agents/style/JT_NARRATION_REQUIRED_KNOWLEDGE_MANIFEST.yaml`

These artifacts define the bounded input surface. They do not by themselves ratify any generated text.

Successor standards or replacement implementation artifacts **MAY** be designated only by later governed amendment, ratified standard revision, or another governed repository-control update that explicitly preserves this amendment's rules and authority boundaries.

---

## 7. Non-goals

This amendment does not:

- authorize impersonation of any natural person
- authorize attribution of personal memory, unpublished intent, or private communications to a drafting system
- substitute generated prose for human review or approval
- authorize hidden memory, hidden style injection, or undeclared context as governed authority

---

## 8. Amendment intent summary (non-normative)

The AI OS may use bounded author-like drafting support, but only when the knowledge inputs are declared, traceable, and governed. Style may support drafting. Style may not become authority.
