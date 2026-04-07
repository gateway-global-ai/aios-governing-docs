---
document_id: AIOS-OPS-018
registry_id: AIOS-OPS-018
version: 1.0.0
status: ratified
category: operations
title: Cursor / IDE Host Activation — Result Record
author: Gateway Global AIOS
created: 2026-04-06
last_updated: 2026-04-06
reviewers: []
cross_references:
  - AIOS-OPS-009
  - AIOS-OPS-011
  - AIOS-OPS-013
  - AIOS-OPS-014
  - AIOS-OPS-015
  - AIOS-OPS-016
  - AIOS-OPS-017
---

# AIOS-OPS-018 — Cursor / IDE Host Activation — Result Record

**Operational record — not law.** Documents **in-repository** preparation for **Cursor (or equivalent IDE)** enforcement and what **still requires** operator/host configuration outside this repo.

**GitHub-side** Phase 2 enforcement is **already active** on **`main`** per **[AIOS-OPS-017](GitHubHostActivationResult.md)**. **Cursor-side** behavioral enforcement is **not** switched on by commits in this repository alone.

---

## 1. Record date

**2026-04-06**

---

## 2. Source files used (authoritative in this repo)

| Document / artifact | ID / path |
|---------------------|-----------|
| **[AIOS-OPS-009](CursorEnforcementContract.md)** | Runtime contract (preflight, enums, fail-closed) |
| **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)** | Bindings, validation, rollback |
| **[AIOS-OPS-013](EnforcementActivationHandoffSummary.md)** | Narrative handoff and boundaries |
| **[AIOS-OPS-014](ActivationExportIndex.md)** | Operator index |
| **[AIOS-OPS-015](ActivationCommandChecklist.md)** | Commands |
| **[AIOS-OPS-016](CursorHostActivationHandoff.md)** | Files to bind, operator steps (handoff) |
| **Preflight JSON Schema** | **`reference/schemas/cursor_preflight.schema.json`** |
| **Agent registry** | **`reference/agent_registry.yaml`** |

**Normative behavior** remains **[AIOS-OPS-004](CursorAgentExecutionRules.md)** and **[AIOS-SPEC-012](../specifications/AgentClassRegistrationAndAuthorityModel.md)**; the table above is the **activation package** surface.

---

## 3. Exact files Cursor / IDE must bind to

Paths **relative to the governance repository root** (or a **pinned** clone/submodule of **`gateway-global-ai/aios-governing-docs`**), per **AIOS-OPS-011** §1 and **AIOS-OPS-016** §1:

| Binding role | Path |
|--------------|------|
| Human-readable contract | **`operations/CursorEnforcementContract.md`** |
| Machine validation | **`reference/schemas/cursor_preflight.schema.json`** |
| Agent identity / class | **`reference/agent_registry.yaml`** |

Optional but referenced for governance edits: **`scripts/registry_generator.py`** (aligns with **G-7** and GitHub **`governance-integrity`** workflow).

**AIOS-OPS-011** §1 states **project rules** (e.g. **`.cursor/rules/*.mdc`**) as the **example** pattern for requiring preflight — not a product guarantee that Cursor loads any path by default.

---

## 4. Required fail-closed expectations

Per **AIOS-OPS-009** §6 and **AIOS-OPS-011** §4:

1. **Schema-valid** preflight JSON **before** writes on governed paths (keys/enums per schema and **AIOS-OPS-004** Appendix A).
2. **`agent_id`** resolves in **`reference/agent_registry.yaml`** with **`class`** = **`task_type`** (**AIOS-OPS-004** §2.2).
3. On failure: emit **`aios_enforcement_failure`** JSON (**AIOS-OPS-004** §4.1); **block** further normative governance writes for that turn/session until resolved — **not** advisory-only behavior once activated.

---

## 5. Required repo-boundary behavior

Per **AIOS-OPS-009** §§3–4, **7** and **AIOS-OPS-011** §5:

| `repo_kind` | Requirement |
|-------------|-------------|
| **`governance_repository`** | Governed edits only under this repo’s governed layout (e.g. `amendments/`, `specifications/`, `core/`, `commercial/`, `reference/`, `legal/`, `operations/`) per **AIOS-OPS-004** §2 / §5. |
| **`implementation_repository`** | **No** normative governance authoring; **`document_id`** citation only (**AIOS-OPS-004** §3). |

**Workspace URL/path detection** is **configuration**; this repo does not prescribe a vendor-specific format (**AIOS-OPS-011** §5).

---

## 6. What has been prepared in-repo

| Item | Status |
|------|--------|
| Contract, schema, registry paths | **Present** at paths in §3 |
| Runbooks, handoff summary, export index, command checklist | **Ratified** — **AIOS-OPS-011**, **013**, **014**, **015**; handoff narrative **AIOS-OPS-016** |
| **Minimal operator checklist** | **`operations/CursorActivationChecklist.md`** (**AIOS-OPS-019**) |
| GitHub CI integrity gate | **Live** on **`main`** — **AIOS-OPS-017** |

---

## 7. What still requires host / IDE-side configuration

| Item | Notes |
|------|--------|
| **Project rules / skills** that **enforce** (not merely cite) preflight + schema + registry | Operator installs per **AIOS-OPS-011** §1; Cursor **does not** auto-load AIOS enforcement (**AIOS-OPS-013** §1). |
| **Pinned governance revision** (SHA/tag) for automation | Local submodule, clone path, or org-standard pin — **AIOS-OPS-011** §3. |
| **Session → `agent_id` mapping** | e.g. **`aios-gov-agent-drafting-001`** for drafting — **AIOS-OPS-011** §3. |
| **Validation tooling** | JSON Schema validator against **`cursor_preflight.schema.json`** — **AIOS-OPS-011** §2 (**AIOS-OPS-015** lists commands that exist in-repo). |

---

## 8. Cursor-side enforcement — truthful statement

- **Not yet live** in the IDE **unless** operators have installed bindings that **hard-stop** on preflight/registry failure per **AIOS-OPS-011** §4. Committing this repo **does not** by itself activate those bindings.
- **Ready for host/IDE activation** in the sense that **authoritative paths and procedures** are **in-repo** and **indexed** (**AIOS-OPS-014**), and **GitHub** already enforces integrity on **`main`** — **provided** operators follow **AIOS-OPS-011** and **`operations/CursorActivationChecklist.md`**.

---

## 9. Remote repository sync (operational)

If **direct push** to **`origin/main`** is **declined** by the **protected branch** hook (pull request and required checks), operators **SHALL** land commits via a **pull request** from a **topic branch** (for example: push `HEAD` to **`sync/main-followthrough-2026-04-06`** and merge after **`Governance integrity / governance-integrity`** passes). This record **does not** replace that merge workflow.

---

## 10. Rollback / disable

Per **AIOS-OPS-011** §7: disable or rename enforcing **rules** / **skills**; humans may edit without agent tooling; GitHub CI remains separate. **Do not** use rollback to bypass org policy.

---

*End of AIOS-OPS-018.*
