---
document_id: AIOS-OPS-016
registry_id: AIOS-OPS-016
version: 1.0.0
status: ratified
category: operations
title: Cursor / IDE — Host Activation Handoff
author: Gateway Global AIOS
created: 2026-04-05
last_updated: 2026-04-05
reviewers: []
cross_references:
  - AIOS-OPS-004
  - AIOS-OPS-009
  - AIOS-OPS-011
  - AIOS-OPS-014
  - AIOS-SPEC-012
  - AMD-2026-010
---

# AIOS-OPS-016 — Cursor / IDE — Host Activation Handoff

**Handoff artifact only — not new law.** Binds to **[AIOS-OPS-009](CursorEnforcementContract.md)**, **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)**, and **[AIOS-OPS-014](ActivationExportIndex.md)**.

---

## 1. Files Cursor / IDE must bind to

Use these paths **relative to the governance repository root** (or a **pinned** submodule/checkout of **`gateway-global-ai/aios-governing-docs`**):

| Artifact | Path |
|----------|------|
| **Contract** | **`operations/CursorEnforcementContract.md`** (**AIOS-OPS-009**) |
| **Preflight JSON Schema** | **`reference/schemas/cursor_preflight.schema.json`** |
| **Agent registry** | **`reference/agent_registry.yaml`** |

**Normative law** for behavior remains **AIOS-OPS-004** / **AIOS-SPEC-012**; **AIOS-OPS-009** operationalizes the contract for tooling.

---

## 2. Fail-closed requirements (non-negotiable)

Per **AIOS-OPS-009** §6 and **AIOS-OPS-004** §4.1:

1. **Complete preflight** JSON (schema-valid) **before** writes on governed paths.
2. **`agent_id`** **MUST** resolve to a row in **`reference/agent_registry.yaml`** with **`class`** = **`task_type`** (**AIOS-OPS-004** §2.2).
3. On failure: emit **`aios_enforcement_failure`** JSON; **no** further normative governance writes in that session until resolved.
4. **`registry_generator.py`** / **G-7**: after front-matter edits to scanned paths, registry must be regenerated and committed — align with GitHub **`governance-integrity`** workflow.

---

## 3. Repo-boundary expectations

| `repo_kind` | Expectation |
|-------------|-------------|
| **`governance_repository`** | Edits under `amendments/`, `specifications/`, `core/`, `commercial/`, `reference/`, `legal/`, `operations/` per **AIOS-OPS-004** §2 / §5. |
| **`implementation_repository`** | **No** normative governance authoring; cite **`document_id`** only (**AIOS-OPS-004** §3). |

---

## 4. Remaining manual / operator-side steps (Cursor / IDE)

GitHub admin or repo settings **cannot** install Cursor rules. Operators **SHALL**:

1. Add **project rules** (e.g. **`.cursor/rules/*.mdc`**) or **skills** that **require** Appendix A–shaped preflight and validation against **`cursor_preflight.schema.json`**.
2. Point automation at a **pinned** SHA/tag of this repo for **`agent_registry.yaml`**.
3. Map session identity to a registered **`agent_id`** (e.g. **`aios-gov-agent-drafting-001`** for drafting work in this repo).

See **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)** §§1–7 for validation and rollback.

---

## 5. What GitHub admin access alone cannot activate

| Capability | Why |
|------------|-----|
| **Cursor rule enforcement** | Lives in **local** / **IDE** config and org developer machines, not in GitHub repo settings. |
| **Preflight JSON emission** | Requires IDE/agent integration; not a GitHub feature. |
| **Pinned governance SHA in IDE** | Submodule or clone path is **local** or **CI** in other repos — not set by branch protection. |

**GitHub-side** CI can enforce **G-1 / G-3 / G-7** and registry YAML parse via **`.github/workflows/governance-integrity.yml`**; that **does not** replace Cursor-side preflight.

---

*End of AIOS-OPS-016.*
