---
document_id: AIOS-OPS-019
registry_id: AIOS-OPS-019
version: 1.0.0
status: ratified
category: operations
title: Cursor / IDE — Activation Checklist (operators)
author: Gateway Global AIOS
created: 2026-04-06
last_updated: 2026-04-06
reviewers: []
cross_references:
  - AIOS-OPS-009
  - AIOS-OPS-011
  - AIOS-OPS-014
  - AIOS-OPS-015
  - AIOS-OPS-016
  - AIOS-OPS-018
  - AMD-2026-010
---

# AIOS-OPS-019 — Cursor / IDE — Activation Checklist (operators)

**Procedural checklist only — not new law.** Pair with **[AIOS-OPS-011 — Cursor Enforcement Activation Runbook](CursorEnforcementActivationRunbook.md)** and **[AIOS-OPS-014 — Activation Export Index](ActivationExportIndex.md)**.

---

## 1. Repo-grounded paths (governance repo root)

| Item | Path |
|------|------|
| **Contract** | **`operations/CursorEnforcementContract.md`** (**AIOS-OPS-009**) |
| **Preflight schema** | **`reference/schemas/cursor_preflight.schema.json`** |
| **Agent registry** | **`reference/agent_registry.yaml`** |

---

## 2. Fail-closed requirement

- Preflight JSON **must** validate against **`reference/schemas/cursor_preflight.schema.json`** before writes on governed paths.
- **`agent_id`** **must** resolve in **`reference/agent_registry.yaml`** with **`class`** equal to preflight **`task_type`**.
- On failure: emit **`aios_enforcement_failure`** per **AIOS-OPS-004** §4.1; **stop** normative governance writes for that session until resolved — **AIOS-OPS-009** §6, **AIOS-OPS-011** §4.

---

## 3. Repo-boundary requirement

- Set **`repo_kind`** and **`repo_scope`** correctly; **implementation** repos **must not** author normative governance — **AIOS-OPS-009** §§3–4, **7**; **AIOS-OPS-011** §5.

---

## 4. Bindings (implementation-neutral)

- Install **project rules** or **skills** that **require** the contract + schema + registry at a **pinned** revision — **AIOS-OPS-011** §1 cites **`.cursor/rules/*.mdc`** as an **example** pattern only; this checklist does **not** assert IDE-specific menus or product behavior beyond what those runbooks state.

---

## 5. Validation expectations

| Step | Pass |
|------|------|
| Sample preflight object validates against **`cursor_preflight.schema.json`** | **AIOS-OPS-011** §6, **AIOS-OPS-015** |
| **`agent_id`** in use appears in **`agent_registry.yaml`** with matching **`class`** | **AIOS-OPS-011** §§3–6 |
| After governed front-matter edits: `py -3 scripts/registry_generator.py` then `py -3 scripts/governance_integrity_check.py` → **`governance_integrity_check: OK`** | **AIOS-OPS-014**, **AIOS-OPS-015** |
| Failure path: invalid preflight → refusal JSON and **no** governed write | **AIOS-OPS-011** §6 |

---

## 6. Rollback / disable

- **Pause IDE enforcement:** disable or rename the rules/skills that enforce preflight — **AIOS-OPS-011** §7.
- **Restore:** re-enable rules; confirm one successful validated preflight path — **AIOS-OPS-011** §7.

---

*End of AIOS-OPS-019.*
