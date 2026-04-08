---
document_id: AIOS-COUNCIL-BRIEF-001
version: 1.0.1
status: draft
category: reference
title: Council review brief — AIOS Master Implementation Program
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
cross_references:
  - doc_id: AIOS-MASTER-IMPL-001
  - doc_id: AIOS-IMPL-LEDGER-001
  - doc_id: AIOS-ADR-001
  - doc_id: AIOS-COUNCIL-BRIEF-002
amendment_history:
  - version: 1.0.1
    date: 2026-04-07
    summary: Cross-reference AIOS-COUNCIL-BRIEF-002 (interface control program committee gate).
  - version: 1.0.0
    date: 2026-04-07
    summary: Initial council brief for master program, ledger, and ADR-001.
---

# Council review brief — AIOS Master Implementation Program

**Purpose:** Single page for **council** (or delegated body) to decide whether to **approve the master implementation program for execution** and **accept ADR-001**. This is **not** amendment ratification; it is **governance of implementation sequencing and architecture**.

---

## What you are approving (two decisions)

| # | Artifact | Document ID | Question for council |
|---|----------|-------------|------------------------|
| 1 | **Master program** | **AIOS-MASTER-IMPL-001** | Approve **cross-repo** phased backlog, layer model (governing / core / interface / tenant), and **MBL-*** backlog as the **authoritative** program (pending: set **`execution_status`** or bump **`status`** per your convention). |
| 2 | **Core vs interface ADR** | **AIOS-ADR-001** | **Accept** the architectural boundary: shell law and control-plane **contracts** are not owned solely by the React UI repo; interface **renders** and **adapts**. |

| Supporting | Document ID | Role |
|------------|-------------|------|
| **Implementation ledger** | **AIOS-IMPL-LEDGER-001** | Anti-drift operating loop; what counts as master vs child progress. |

**Paths (this repo):**

- [`AIOS-MASTER-IMPLEMENTATION-PROGRAM.md`](AIOS-MASTER-IMPLEMENTATION-PROGRAM.md)
- [`AIOS-IMPLEMENTATION-LEDGER.md`](AIOS-IMPLEMENTATION-LEDGER.md)
- [`ADR-001-core-shell-vs-interface-boundaries.md`](ADR-001-core-shell-vs-interface-boundaries.md)

**Related (child workstream approval):** [`COUNCIL-REVIEW-BRIEF-AIOS-INTERFACE-CONTROL-001.md`](COUNCIL-REVIEW-BRIEF-AIOS-INTERFACE-CONTROL-001.md) (**AIOS-COUNCIL-BRIEF-002**) — committee review of **`ai-os-voice-interface`** **AIOS-IMPL-CONTROL-001** before that plan is **execution-approved** in the product repo.

---

## Why this matters

- Without council approval, the program remains **`draft`** / **proposed** — implementation teams should **not** treat **`approved_for_execution`** as given.
- **Execution approval** prevents **every repo** from becoming the **center of gravity** for shell law (especially `ai-os-voice-interface`).
- **ADR acceptance** unlocks **MBL-001** closure on the **record** and allows **enforced** import boundaries in code (CI) without inventing architecture ad hoc.

---

## Suggested review checklist

- [ ] Layer model (Part 1 of master program) matches council intent for **core shell / kernel / control-plane** vs **interface**.
- [ ] **MBL-*** backlog is complete enough to schedule work without constant founder triage.
- [ ] **Child workstream** rule is acceptable: `ai-os-voice-interface` docs are **not** authoritative for cross-repo scope.
- [ ] **ADR-001** import rules (core must not import React) are acceptable; extraction to `packages/*` remains **optional**.
- [ ] **MBL-009** (AMD-2026-007 vs policy index) can stay **parallel** — not a blocker to approving execution.

---

## On approval — record (secretary / maintainer)

1. Update **AIOS-MASTER-IMPL-001**: council approval date, **`status`** or **`execution_status`** field per convention; remove ambiguity with **`draft`**.
2. Update **AIOS-ADR-001**: **`status: accepted`**, **`amendment_history`**.
3. Update **AIOS-IMPL-LEDGER-001**: **`status`** if ledger is formally **live**.
4. Update **MBL-000** / **MBL-001** rows in master Part 6 to **`done`** with evidence (this brief + date).
5. **CHANGELOG** in `aios-governing-docs`.

---

## On rejection or deferral

- Capture **reasons** and **required changes** in council minutes or issue.
- Keep documents **`draft`** / **`proposed`** until revised and re-reviewed.

---

*End of council brief v1.0.0.*
