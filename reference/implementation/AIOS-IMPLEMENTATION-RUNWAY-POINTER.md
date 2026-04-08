---
document_id: AIOS-REF-013
title: Implementation runway pointer (product conformance)
version: 1.6.0
status: draft
category: reference
author: Gateway Global
created: 2026-04-06
last_updated: 2026-04-07
reviewers: []
supersedes: null
cross_references:
  - { doc_id: "AIOS-MASTER-IMPL-001", relationship: "references" }
  - { doc_id: "AIOS-IMPL-LEDGER-001", relationship: "references" }
  - { doc_id: "AIOS-ADR-001", relationship: "references" }
  - { doc_id: "AIOS-COUNCIL-BRIEF-001", relationship: "references" }
  - { doc_id: "AIOS-COUNCIL-BRIEF-002", relationship: "references" }
  - { doc_id: "AIOS-COUNCIL-BRIEF-003", relationship: "references" }
  - { doc_id: "AIOS-DEV-PROC-001", relationship: "references" }
  - { doc_id: "AIOS-SPEC-006", relationship: "references" }
  - { doc_id: "AIOS-SPEC-007", relationship: "references" }
  - { doc_id: "AIOS-SPEC-008", relationship: "references" }
  - { doc_id: "AIOS-SPEC-009", relationship: "implements" }
  - { doc_id: "AMD-2026-007", relationship: "references" }
  - { doc_id: "AMD-2026-009", relationship: "references" }
  - { doc_id: "AMD-2026-010", relationship: "references" }
amendment_history:
  - version: 1.6.0
    date: 2026-04-07
    summary: AIOS-DEV-PROC-001 + AIOS-COUNCIL-BRIEF-003 — development conformance process (peer review + council ratification); reviews/aios_dev_conformance_process.
  - version: 1.5.0
    date: 2026-04-07
    summary: Link to AIOS-COUNCIL-BRIEF-002 (interface implementation control program — council review before execution approval).
  - version: 1.4.0
    date: 2026-04-07
    summary: Link to AIOS-COUNCIL-BRIEF-001 (council review brief).
  - version: 1.3.0
    date: 2026-04-07
    summary: Master program draft pending council; ledger draft; ADR proposed — not approved for execution without review.
  - version: 1.2.0
    date: 2026-04-07
    summary: Links to ledger (AIOS-IMPL-LEDGER-001) and ADR-001 (core vs interface).
  - version: 1.1.0
    date: 2026-04-07
    summary: Link to AIOS-MASTER-IMPLEMENTATION-PROGRAM (cross-repo master program).
---

# Implementation runway pointer (product conformance)

## Purpose

This repository entry is a **council-traceable pointer** to the **product-side implementation runway** for **ratified** AIOS requirements. It does **not** duplicate execution planning; it records **where** that planning lives so conformance work stays discoverable from governing docs.

## Master program (cross-repo)

**Authoritative implementation program (layers, phases, master backlog):**  
`reference/implementation/AIOS-MASTER-IMPLEMENTATION-PROGRAM.md` (**AIOS-MASTER-IMPL-001**, **`draft`** — **council review** required before **approved for execution**)

**Implementation ledger + anti-drift loop:**  
`reference/implementation/AIOS-IMPLEMENTATION-LEDGER.md` (**AIOS-IMPL-LEDGER-001**, **`draft`**)

**Core vs interface ADR:**  
`reference/implementation/ADR-001-core-shell-vs-interface-boundaries.md` (**AIOS-ADR-001**, **`proposed`**)

**Council review brief (master program + ADR):**  
`reference/implementation/COUNCIL-REVIEW-BRIEF-AIOS-MASTER-IMPL-001.md` (**AIOS-COUNCIL-BRIEF-001**)

**Council review brief (interface control program — product spine):**  
`reference/implementation/COUNCIL-REVIEW-BRIEF-AIOS-INTERFACE-CONTROL-001.md` (**AIOS-COUNCIL-BRIEF-002**, **`draft`** — **committee approval** required before **`ai-os-voice-interface`** treats **AIOS-IMPL-CONTROL-001** as **execution-approved**)

Repo-local plans (e.g. `ai-os-voice-interface/docs/implementation/AIOS-IMPLEMENTATION-CONTROL-PROGRAM.md`) are **child workstreams** — not substitutes for the master program; **AIOS-COUNCIL-BRIEF-002** governs whether that child plan is **authorized** to run as the **official** interface conformance process.

**Development conformance (triangulation — governing reference):**  
`reference/implementation/AIOS-DEVELOPMENT-CONFORMANCE-PROCESS.md` (**AIOS-DEV-PROC-001**, **`draft`** until peer review + council)  
**Council brief:** `reference/implementation/COUNCIL-REVIEW-BRIEF-AIOS-DEV-PROC-001.md` (**AIOS-COUNCIL-BRIEF-003**)  
**Peer review packet:** `reviews/aios_dev_conformance_process/`  
**Ratification motion:** `reference/implementation/RATIFICATION-MOTION-AIOS-DEV-PROC-001.md` (**AIOS-RAT-MOTION-DEV-PROC-001**)

Product operational detail remains **`ai-os-voice-interface`** **AIOS-DEV-TRI-001**; **ratified** **AIOS-DEV-PROC-001** makes that process **binding** in governance.

## Canonical location

**Primary artifact (execution memo):**  
`ai-os-voice-interface/docs/implementation-runway-memo.md`  
(in the **ai-os-voice-interface** product repository)

## Scope

- **Non-normative:** sequencing, backlog, and acceptance criteria for delivery belong in the product memo, not here.
- **Does not supersede** specifications, amendments, or council motions. If this pointer’s description and ratified text diverge, **ratified governing documents win**.

## Governing references (normative)

Implementation work should remain traceable to clauses in (including where surfaces overlap):

| Document | Role |
|----------|------|
| **AIOS-SPEC-009** | Intent primitive, execution model, disclosure, lifecycle (primary cross-cutting law for the spine) |
| **AIOS-SPEC-007** | Workspace integration governance, control-plane expectations |
| **AIOS-SPEC-006** | UI component registry (where shell / surfaces register) |
| **AIOS-SPEC-008** | Intent discovery and onboarding (where UX maps to intent) |
| **AMD-2026-007** | Shell affordances, session disclosure, Workspace pack alignment (where referenced by product paths) |
| **AMD-2026-009** | External knowledge / web retrieval gates (expansion phase) |
| **AMD-2026-010** | Kernel / shadow pilot lane (advisory until promoted) |

## Maintenance rule

Update **this pointer file** only when the **canonical path**, **ownership**, or **stated execution scope** of the runway memo **materially** changes. Routine memo edits stay in the product repo; do **not** mirror the full memo here.
