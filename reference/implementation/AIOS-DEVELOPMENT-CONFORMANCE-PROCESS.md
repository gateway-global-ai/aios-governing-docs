---
document_id: AIOS-DEV-PROC-001
version: 1.0.0
status: draft
category: reference
title: AI OS development conformance — triangulated peer review
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
cross_references:
  - doc_id: AMD-2026-005
  - doc_id: AMD-2026-012
  - doc_id: AIOS-SPEC-009
  - doc_id: AIOS-SPEC-007
  - doc_id: AIOS-MASTER-IMPL-001
  - doc_id: AIOS-COUNCIL-BRIEF-002
  - doc_id: AIOS-COUNCIL-BRIEF-003
  - doc_id: AIOS-RAT-MOTION-DEV-PROC-001
  - doc_id: AIOS-REF-013
amendment_history:
  - version: 1.0.0
    date: 2026-04-07
    summary: Initial draft — product development triangulation mirrors governance reviews; pending peer review and council ratification.
---

# AI OS development conformance — triangulated peer review

**Purpose:** This **governing** reference establishes the **binding** (once **ratified**) process for **implementation conformance** in the **reference AI OS interface** repository — **`ai-os-voice-interface`** — using **triangulated peer review** aligned with **`aios-governing-docs/reviews/`** practice. It is **not** a simulation: **ratification** requires **peer review artifacts**, **synthesis**, and **council** decision per **AIOS-COUNCIL-BRIEF-003**.

**Canonical product specification (operational detail):**  
`ai-os-voice-interface/docs/implementation/AIOS-DEVELOPMENT-TRIANGULATION-PROCESS.md` — **AIOS-DEV-TRI-001**

**Peer review packet (this repo):**  
`reviews/aios_dev_conformance_process/`

---

## Authority and scope

| Field | Value |
|-------|--------|
| **Normative law** | Amendments and specifications in **`aios-governing-docs`** — unchanged by this reference. |
| **This document** | Defines **how** the product team **proves** conformance during development — **process law** for the reference UI workstream **after ratification**. |
| **Does not** | Replace **AMD-2026-005** (governing document peer review); **aligns** numerical thresholds for **scored** dimensions. |

---

## Committee knowledge base (must be available before ratification vote)

Council **cannot** ratify in ignorance. The following **must** be present and **version-pinned** for the vote packet:

| # | Artifact | Role |
|---|----------|------|
| 1 | **AIOS-DEV-PROC-001** (this file) | Governing **text** under review. |
| 2 | **AIOS-DEV-TRI-001** (product) | Executable process: agents, KB bundle, diagrams, artifacts. |
| 3 | **AIOS-IMPL-CONTROL-001** (product) | Interface control program, backlog **BL-007** / **BL-008**. |
| 4 | **Peer review round** | `reviews/aios_dev_conformance_process/round_1/` (minimum) with **triangulated** reviews. |
| 5 | **Synthesis + gate** | `REVIEW_SYNTHESIS.md`, `RATIFICATION_GATE_REPORT.md` when **READY_FOR_RATIFICATION**. |
| 6 | **Ratification motion** | [`RATIFICATION-MOTION-AIOS-DEV-PROC-001.md`](RATIFICATION-MOTION-AIOS-DEV-PROC-001.md) |

---

## Binding effect upon ratification

When **`status: ratified`** (and **`version`** frozen):

1. **Product** **SHALL** run **material** implementation changes through **AIOS-DEV-TRI-001** or document an explicit **waiver** in **`SCOPE.md`** with council **trail**.
2. **Triangulation** **SHALL** include **DeepSeek**, **OpenAI**, and **Gemini** for binding rounds; **Ollama** **SHALL** run as the **UI parallel lane** where **UI or intent workflow** is in scope.
3. **Knowledge base bundle** **SHALL** be **identical** across reviewers per run (manifest required).
4. **BL-008** validation (**`dev_triangulation_check.py`**) **SHOULD** pass for completed review packages before merge to **protected** branches when program enables CI.

---

## Relationship to interface control program

**AIOS-IMPL-CONTROL-001** owns backlog and **BL-007**/**BL-008**. **AIOS-DEV-PROC-001** is **governing** recognition that the **development triangulation** process is **lawful** for the product — **after** council ratifies this reference.

---

## On ratification — maintainer actions

1. Set **AIOS-DEV-PROC-001** **`status: ratified`**, update **`amendment_history`**, **`last_updated`**.
2. Record motion in **`RATIFICATION-MOTION-AIOS-DEV-PROC-001.md`** execution section.
3. Update **AIOS-COUNCIL-BRIEF-003** execution record.
4. **CHANGELOG**; **`py -3 scripts/registry_generator.py`**.
5. Product repo: pin **`AIOS-DEV-TRI-001`** header with **governing ratification date** and doc ID.

---

*End of AIOS-DEV-PROC-001 v1.0.0 — **draft** pending peer review and council.*
