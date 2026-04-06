---
document_id: AIOS-OPS-011
registry_id: AIOS-OPS-011
version: 1.0.0
status: ratified
category: operations
title: Cursor Enforcement — Activation Runbook
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
reviewers: []
cross_references:
  - AIOS-OPS-009
  - AIOS-OPS-013
  - AIOS-OPS-014
  - AIOS-OPS-015
---

# AIOS-OPS-011 — Cursor Enforcement — Activation Runbook

**Normative law:** **[AIOS-OPS-004](CursorAgentExecutionRules.md)**. This runbook is **procedural** only. Pair with **[AIOS-OPS-009](CursorEnforcementContract.md)** (contract) and **[AIOS-OPS-007](CursorAgentExecutionRulesImplementationPlan.md)** (implementation plan).

**Package summary:** **[AIOS-OPS-013 — Enforcement Activation Handoff Summary](EnforcementActivationHandoffSummary.md)** (narrative handoff); **[AIOS-OPS-014 — Activation Export Index](ActivationExportIndex.md)** (operator index); **[AIOS-OPS-015 — Activation Command Checklist](ActivationCommandChecklist.md)** (commands).

---

## 1. Required Cursor-side enforcement bindings

Cursor (or equivalent IDE) does **not** auto-enforce AIOS by default. The org **SHALL** install **bindings** that reference this repo’s artifacts:

| Binding type | What to point at |
|--------------|------------------|
| **Project rules** (e.g. `.cursor/rules/*.mdc`) | Require preflight JSON; cite **AIOS-OPS-009** and **`reference/schemas/cursor_preflight.schema.json`**. |
| **Skills** (optional) | Same contract; load schema and registry paths from the **pinned** clone or submodule. |

**Authoritative sources in this repository:**

| Artifact | Path |
|----------|------|
| **Preflight schema (JSON Schema)** | `reference/schemas/cursor_preflight.schema.json` |
| **Agent registry (YAML)** | `reference/agent_registry.yaml` |
| **Enforcement contract (human-readable)** | `operations/CursorEnforcementContract.md` (**AIOS-OPS-009**) |
| **Registry generator** | `scripts/registry_generator.py` |

---

## 2. Preflight schema source

- **Validate** agent output against **`reference/schemas/cursor_preflight.schema.json`** using a JSON Schema validator (e.g. `jsonschema` in Python, or IDE-side validation if available).
- **Enums and keys** **MUST** match **AIOS-OPS-004** Appendix A; the schema file encodes those enums — **do not** extend enums without a governed amendment.

---

## 3. Agent registry source

- **Load** **`reference/agent_registry.yaml`** at the **pinned** commit SHA or tag for the governance repo (submodule, sparse checkout, or documented clone path).
- **Before writes:** resolve **`agent_id`** → row; **`class`** **MUST** equal **`task_type`** in preflight (**AIOS-OPS-004** §2.2).
- **Controlled rows** in this repo use **`agent_id`** values **`aios-gov-agent-audit-001`**, **`aios-gov-agent-drafting-001`**, **`aios-gov-agent-review-001`** — use exactly one registered identity per automation session.

---

## 4. Fail-closed behavior (activation requirement)

On **any** of: invalid preflight, enum mismatch, unregistered **`agent_id`**, **`registry_generator.py`** failure or **G-7** drift, or **AIOS-OPS-004** §4 condition:

1. Emit **`aios_enforcement_failure`** JSON (**AIOS-OPS-004** §4.1).
2. **Do not** apply further writes to normative governance paths in that session until resolved.

Rules/skills **SHALL** treat these as **hard stops**, not suggestions.

---

## 5. Repo boundary rules

| `repo_kind` | Rule |
|---------------|------|
| **`governance_repository`** | Governed paths include `amendments/`, `specifications/`, `core/`, `commercial/`, `reference/`, `legal/`, `operations/` per **AIOS-OPS-004** §2 / §5. |
| **`implementation_repository`** | **No** normative governance authoring; compliance by reference to **`document_id`** only (**AIOS-OPS-004** §3). |

Workspace detection (URL/path) is **configuration**; the runbook does not prescribe a vendor format.

---

## 6. Validation after activation

| Step | Pass criteria |
|------|----------------|
| **Preflight** | Sample turn emits JSON that validates against **`cursor_preflight.schema.json`**. |
| **Registry** | **`agent_id`** in use appears in **`reference/agent_registry.yaml`** with matching **`class`**. |
| **Governance edits** | After front-matter changes, `py -3 scripts/registry_generator.py` run and **G-7** satisfied before merge (aligns with GitHub workflow). |
| **Failure path** | Deliberately invalid preflight → refusal JSON and **no** file write. |

---

## 7. Rollback / temporary disable

| Need | Action |
|------|--------|
| **Pause IDE enforcement** | Disable or rename the Cursor **rules** / **skills** that enforce preflight (revert to advisory-only text if needed). |
| **Emergency editing** | Humans may edit files without agent tooling; **CI** on GitHub still enforces integrity when Phase 2 is on. **Do not** use rollback to bypass org policy. |
| **Restore** | Re-enable rules; confirm one successful validated preflight path. |

---

## 8. Relationship to GitHub CI

- **GitHub** enforces **G-1 / G-3 / G-7** (and YAML parse) via **`governance_integrity_check.py`**.
- **Cursor** enforces **behavioral** preflight and registry alignment **before** local writes. Both layers are complementary; neither replaces the other.

---

*End of AIOS-OPS-011.*
