---
document_id: AIOS-SPEC-012
version: 0.1.0
status: draft
category: specification
title: Workspace Domain Pack v1
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
reviewers: []
ratification_target: null
supersedes: null
cross_references:
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AIOS-SPEC-007
    title: Google Workspace Integration Governance
amendment_history:
  - version: 0.1.0
    date: 2026-04-07
    summary: Skeleton artifact; normative minimums from AMD-2026-007 §7; TypeScript/schema detail deferred to follow-on pass.
---

# AIOS-SPEC-012 — Workspace Domain Pack v1

## 0. Status

| Field | Value |
|-------|--------|
| **Status** | `draft` |
| **Authority** | Normative **minimum** requirements are **[AMD-2026-007 §7](../amendments/AMD-2026-007.md)** (ratified). This file **materializes** that outline for cross-reference; **detailed** field schemas, TypeScript types, and validation rules are **deferred** — see **§2**. |

## 1. Normative outline (from AMD-2026-007 §7)

The following **MUST** be satisfied by a conforming **Domain Pack v1** (standalone or merged into **AIOS-SPEC-007** annexes in a future revision):

| Area | Requirement |
|------|-------------|
| **Menu catalog** | Stable ids, labels, route/intent targets, **section** group, **visibility** expression, **requiresCapability** references. |
| **Session summary** | Fields for canvas view, workspace hub, lane, googleAuth, adapter, capabilities[], lastMilestone; mapping to shell and optional agent context. |
| **Command rail modes** | `default` \| `workspace` \| `operator` semantics; **MUST** preserve **AMD-2026-007** §4.1 fallbacks. |
| **Capability registry** | Rows: id, domain, plane, scopes, policyRef, ui.primaryAllowed, confirmation.required. |
| **Mail read plane** | Structured cards, selection-driven read; **POL-WS-UI-001** compliance. |

**Shell vs skills:** **POL-SHELL-004** — shell state controls **MUST NOT** be modeled as **skills** or **tools**; see **AMD-2026-007** **§11.9** and **AIOS-SPEC-006**.

## 2. Deferred content (explicit)

**Recorded 2026-04-07:** The following are **not** completed in **v0.1.0** of this specification:

- TypeScript-oriented schema descriptions and file layout
- Normative JSON Schema for menu catalog and session summary
- Exhaustive registry column definitions and examples

**Next step:** A follow-on governance pass **SHALL** extend this document (or **AIOS-SPEC-007** annexes) with the above **without** contradicting **AMD-2026-007** **§7**.

---

*End of AIOS-SPEC-012, version 0.1.0.*
