---
document_id: AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001
version: 0.1.2
status: draft
category: reference
title: Browser review gate — R&D and knowledge capture (AMD-2026-008-ADD-004)
author: Gateway Global AIOS
created: 2026-04-08
last_updated: 2026-04-17
cross_references:
  - doc_id: AMD-2026-008
  - doc_id: AMD-2026-008-ADD-004
  - doc_id: AIOS-AMD-PLAN-001
  - doc_id: AMD-2026-011
  - doc_id: AIOS-SPEC-013
  - doc_id: AMD-2026-008-ADD-005
    title: Voice-First Rendered Session Proof and Artifact Checks
note: Informative knowledge capture alongside ADD-004 doctrine; not ratified law.
amendment_history:
  - version: 0.1.2
    date: 2026-04-17
    summary: Added alignment note for the newer voice-first rendered-session-proof family so browser review knowledge capture now explicitly distinguishes pre-human approval proof from per-session rendered verification in generated-UI voice lanes.
  - version: 0.1.1
    date: 2026-04-08
    summary: Aligned narrative to amendment 0.2.0 — §7.2 test-capture rules partially answer “automated UI proof” open question; §9.4 remediation; planning artifacts refreshed.
  - version: 0.1.0
    date: 2026-04-08
    summary: Initial capture — problem frame, minimum proof types, relationship to planning lifecycle and quarantined external reference.
---

# Browser review gate — R&D and knowledge capture (001)

## Purpose

Capture **informative** context for **[AMD-2026-008-ADD-004](../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md)**: why **rendered truth** must precede **human approval** on UI-affecting work, and how **review targets** with **`required_visual_proofs`** close the gap between **intent** (plans, diffs, doctrine) and **observed behavior** (browser).

**Related planning (non-normative):** [`reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/planning/ARCHITECT_PLAN.md`](../../reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/planning/ARCHITECT_PLAN.md), [`UI_PLAN.md`](../../reviews/amd_2026_008_add_004_pre_human_browser_review_and_visual_proof_gate/planning/UI_PLAN.md).

---

## Problem frame

| Failure mode | Symptom | ADD-004 response |
|--------------|---------|------------------|
| **Plan substitution** | Approval from architecture/UI memo without render | **§2**, **§7.3** — insufficient evidence |
| **Diff substitution** | “Green CI” without visible shell | **§7** — minimum browser evidence set |
| **Stale or wrong surface** | Screenshot from another build | **§8.5** — evidence integrity |
| **Silent skip** | Ambiguous UI scope → no review | **§4** — default browser review or explicit exception |

---

## Minimum proof concepts (aligned to addendum §7)

1. **Surface** — correct route/shell region loaded.
2. **State** — user-visible mode matches the work item (draft vs send, blocked, etc.).
3. **Control** — buttons/inputs/gates that must exist are visible; forbidden actions absent or disabled per policy.
4. **Behavior** — transitions, blocks, disclosures behave as specified (short capture or recording).
5. **Checklist + packet pointer** — auditable tie from evidence to **`review_slug`**.

---

## External reference (quarantine)

**`https://github.com/continuedev/continue`** is registered for **quarantine** study only — see **[`sources/AMD-2026-008-ADD-004/external_reference_quarantine.md`](../../sources/AMD-2026-008-ADD-004/external_reference_quarantine.md)**. Useful **ideas** (checks in repo, CI enforcement) **SHALL NOT** be conflated with **AI OS** browser proof artifacts until **AIOS-SPEC-013** promotion criteria are met.

---

## Open questions (for peer review / Phase E)

- How **`REVIEW_TARGET.yaml`** maps to product issue IDs and CI job names.
- **Automated** UI proof — **§7.2** now **SHALL**-constrains **test-captured** proof. The repo now includes a first sovereign Playwright harness under **`AIOS-SOVEREIGN-PLAYWRIGHT-PROOF-HARNESS-001`**; remaining gap is policy-approved runtime-target registration and packet integration for specific product paths.
- Interaction with **cursor-ide-browser** (or similar) **governed** automation vs ad-hoc agent claims.

## Alignment note

`AMD-2026-008-ADD-004` remains the primary **pre-human approval** browser-proof doctrine.

The later draft `AMD-2026-008-ADD-005` extends the same family for **voice-first generated UI sessions**, where rendered session proof and artifact checks may be required after meaningful sessions rather than only at a final approval boundary.

---

*End of AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001 v0.1.2.*
