# Architect plan — AMD-2026-008-ADD-004 (pre-human browser review and visual proof gate)

**Date:** 2026-04-08  
**Primary doctrine:** [`amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md`](../../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md) — **`draft` `0.3.0`** (Phase E **`0.2.0`** content + **`0.3.0`** synthesis response: **§0.2**, **§2.1**, **§3.4**, **§11.1**, **§12.4**)  
**Knowledge:** [`reference/implementation/AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001.md`](../../../reference/implementation/AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001.md)

---

## 1. Executive summary

ADD-004 places a **normative gate**: for UI-affecting work, **human approval** must not complete without **browser-visible evidence** when **`required_visual_proofs`** (or policy) applies. Architecture must supply:

1. A **review target** schema (fields in addendum **§6**) storable in policy or repo artifacts (`REVIEW_TARGET.yaml` recommended).
2. A **binding** between **review runs** and **artifact version** (commit, build id, or packet id) for audit (**§11**).
3. **Blocked states** (`blocked_pending_browser_review`, etc.) that **cannot** silently flip to approved (**§9**).

This plan **does not** mandate a specific automation framework; it maps **where** in the control plane the gate attaches (before human sign-off in the planning lifecycle — **[AIOS-AMD-PLAN-001](../../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)**).

---

## 2. Bounded domains

| Domain | Responsibility | ADD-004 touchpoint |
|--------|----------------|---------------------|
| **Review orchestration** | Creates `review_slug`, attaches `required_visual_proofs` | **§6**, **§11** |
| **Evidence capture** | Screenshots, recordings, or test-emitted UI proof | **§7** |
| **Approval state machine** | Human approval blocked until proofs or recorded exception | **§9–§10** |
| **Policy** | UI-affecting classification; extension of scope; risk-shaped proof minima | **§3.3**, **§4**, **§4.1** |

---

## 3. Relationship to ADD-001 / ADD-002 / ADD-003

| Addendum | What it defines | What ADD-004 adds |
|----------|-----------------|-------------------|
| **ADD-001** | Navigation primitives | **Prove** primitives in browser before approval when visual proof required |
| **ADD-002** | Depth, voice, packaging, BOOK | **Prove** those controls and disclosures render |
| **ADD-003** | Composition control plane | **Prove** composition surfaces and gates are understandable |

No **redefinition** of those addenda — **evidence gate only**.

---

## 4. External reference (quarantine)

**[`continuedev/continue`](https://github.com/continuedev/continue)** — informative only; **quarantine** record at [`sources/AMD-2026-008-ADD-004/external_reference_quarantine.md`](../../../sources/AMD-2026-008-ADD-004/external_reference_quarantine.md). Useful for **CI/check** analogies; **not** a required dependency for ADD-004 compliance.

---

## 5. Gaps vs next revision (`0.3.0` / Round 2 candidates)

| Topic | Open point |
|-------|------------|
| **Machine-readable review target** | **§6.1** defers canonical schema to policy/product — still need **ops** or **registry** home for **§11** audit binding |
| **Tooling** | Governed browser automation (e.g. IDE MCP browser) vs manual capture — policy |
| **Product repo** | Where `HUMAN_REVIEW_PACKET.md` / `CAPTURE_CHECKLIST.md` live for `ai-os-voice-interface` |
| **Cross-spec anchors** | Peer review: optional **AIOS-SPEC-006** / **AIOS-SPEC-009** / **MPOA** pointers for transparency and execution context |

---

## 6. Verification checklist (planning)

- [ ] Committee packet acknowledges **§5.1** sequence includes **browser evidence before human approval**.
- [ ] No conflict with **AMD-2026-011** / **AIOS-SPEC-013** for the quarantined reference URL.
- [x] Peer review Round 1 executed on [`AMD-2026-008-ADD-004`](../../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md) with **`--smart-context`** — gate **FAIL** **[AMD-2026-005](../../../amendments/AMD-2026-005.md)**; next revision **`0.3.0`** + Round 2.

---

*Planning baseline for Phase B–D — subject to author revision of normative AMD text.*
