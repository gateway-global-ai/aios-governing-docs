---
document_id: AMD-2026-008-ADD-001
parent_amendment: AMD-2026-008
parent_version: 1.0.0
version: 0.1.0
status: draft
category: amendment_addendum
title: Base Shell Navigation Primitives and Start-Here Control
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
cross_references:
  - doc_id: AMD-2026-008
    title: Sovereign Voice and Local Runtime Lanes (Incorporation by Reference)
  - doc_id: AMD-2026-008-ADD-002
    title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
addendum_history:
  - version: 0.1.0
    date: 2026-04-09
    summary: Initial draft — navigation classes (START_HERE, CONTINUE, CHOOSE, SINGLE_INPUT, MULTI_INPUT); alert/continue/choose/single/multi primitives; cross-ref ADD-002 for output depth and shell voice controls.
---

# AMD-2026-008-ADD-001 — Base Shell Navigation Primitives and Start-Here Control

## 0. Status and intent

| Field | Value |
|-------|--------|
| **Status** | **`draft` `0.1.0`** — addendum to **[AMD-2026-008](AMD-2026-008.md)** **1.0.0** |
| **Does not replace** | **AMD-2026-008** remains the parent framework for **sovereign voice** and **local runtime lanes**. This addendum defines the **navigation** axis of the shell control plane. **Output depth**, **shell voice output controls**, and **packaging** are governed by **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)**. |

---

## 1. Purpose

This addendum defines **base shell navigation primitives**—including **start-here** and **continuation** behavior—so that session flow, choice, and input capture are **shell-governed**, not improvised by model habit or ad hoc agent skills.

## 2. Governing principle

The shell **SHALL** expose **deterministic navigation classes** for how the user moves through a session. **Navigation** governs **where the user is in the flow**; it **SHALL NOT** be conflated with **how much** is said (**ADD-002** output depth), **how** speech is delivered or interrupted (**ADD-002** shell voice controls), or **export format** (**ADD-002** packaging).

## 3. Navigation classes

The following **navigation classes** are **normative labels** for shell-level routing. Implementations **MAY** surface them under product-specific names; behavior **SHALL** remain mappable to these classes.

| Class | Meaning |
|-------|--------|
| **START_HERE** | Initial orientation: where to begin, what the session is for, or recovery to a known entry point. |
| **CONTINUE** | Proceed along the current thread without forcing a new branch or capture shape. |
| **CHOOSE** | Discrete selection among presented options (list, tiles, voice enumeration, or equivalent). |
| **SINGLE_INPUT** | One primary free-form input (utterance, prompt, or single field). |
| **MULTI_INPUT** | Structured capture of **multiple** fields, slots, or sequential answers in one governed interaction. |

## 4. Core primitives (mapping)

These **primitives** **SHALL** be realizable as **shell affordances** (voice, touch, or equivalent), not only as model behaviors:

| Primitive | Role |
|-----------|------|
| **Alert** | Interruptive or high-priority notice; **SHALL** be distinguishable from routine continuation and **SHALL NOT** silently replace structured choice or input capture. |
| **Continue** | Maps to **CONTINUE** — advance or resume without redefining capture shape. |
| **Choose** | Maps to **CHOOSE** — pick among explicit options. |
| **Single input** | Maps to **SINGLE_INPUT** — one primary response channel for the active step. |
| **Multi input** | Maps to **MULTI_INPUT** — multiple fields or steps under one governed pattern. |

## 5. Shell obligations (navigation)

The shell **SHALL**:

1. Make the **active navigation class** **observable** to the user when ambiguity would cause mis-routing (e.g. choose vs free-form).
2. **NOT** treat **navigation** as interchangeable with **verbosity** or **export**; those are **ADD-002**.
3. Preserve **auditability** of **branching** and **selection** consistent with **AIOS-SPEC-009** session and intent boundaries where applicable.

## 6. Non-goals

This addendum does not define:

- output depth, narration density, or **shell voice output controls** (**ADD-002**)
- output packaging or export formats (**ADD-002**)
- visual styling tokens or chrome layout
- workspace tool routing or **AIOS-SPEC-007** integration detail

---

*End of AMD-2026-008-ADD-001, version 0.1.0 (draft).*
