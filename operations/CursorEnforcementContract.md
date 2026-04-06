---
document_id: AIOS-OPS-009
registry_id: AIOS-OPS-009
version: 1.0.0
status: ratified
category: operations
title: Cursor Enforcement Contract (activation)
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
reviewers: []
cross_references:
  - AIOS-OPS-004
  - AIOS-OPS-007
  - AIOS-OPS-011
  - AIOS-OPS-013
  - AIOS-SPEC-012
  - AMD-2026-010
---

# AIOS-OPS-009 — Cursor Enforcement Contract (activation)

**Binding law:** **[AIOS-OPS-004](CursorAgentExecutionRules.md)** (ratified). This file is an **activation artifact** that restates the **runtime contract** for Cursor (and equivalent IDE agents). It **does not** add obligations beyond **AIOS-OPS-004**, **AIOS-SPEC-012**, or **AMD-2026-010**.

**Handoff:** **[AIOS-OPS-013 — Enforcement Activation Handoff Summary](EnforcementActivationHandoffSummary.md)** (package entry point); **[AIOS-OPS-011 — Cursor Enforcement Activation Runbook](CursorEnforcementActivationRunbook.md)** (bindings, validation, rollback).

**Schema:** [`reference/schemas/cursor_preflight.schema.json`](../reference/schemas/cursor_preflight.schema.json) **SHALL** validate the **preflight JSON** object (Appendix A keys and enums).

---

## 1. Required preflight object

Before **any** file write, commit suggestion, or governance edit on governed paths, the agent **SHALL** emit a **complete** JSON object that:

1. Conforms to **`reference/schemas/cursor_preflight.schema.json`**.
2. Uses **only** the enum values defined in **AIOS-OPS-004** §2 and Appendix A (same strings as **AIOS-SPEC-012** `class` for `task_type` ↔ registry mapping, **§2.2**).

### 1.1 Required fields (summary)

| Field | Role |
|-------|------|
| **`repo_scope`** | Exact repository URL or path; enables boundary checks. |
| **`repo_kind`** | `governance_repository` or `implementation_repository`. |
| **`task_type`** | Session task; **MUST** equal the registered agent’s **`class`** in **`reference/agent_registry.yaml`**, except **`unknown`** → **stop** (no writes). |
| **`artifact_type`** | Classification of the primary artifact touched this turn. |
| **`governing_document_ids`** | Non-empty array of `document_id` strings, or `["none"]` with **one-line** justification only when truly non-governed. |
| **`lifecycle_state`** | `draft` \| `under_review` \| `ratified` \| `not_applicable` per governed targets. |
| **`allowed_actions`** | Non-empty subset of **AIOS-OPS-004** §2 allowed actions. |

---

## 2. Allowed enums

**SHALL** match **AIOS-OPS-004** §2 and Appendix A exactly (no synonyms).

- **`repo_kind`:** `governance_repository` \| `implementation_repository`
- **`task_type`:** `governance_audit` \| `governance_drafting` \| `implementation` \| `review` \| `migration` \| `documentation_informative` \| `unknown`
- **`artifact_type`:** `amendment` \| `specification` \| `operations` \| `peer_review` \| `application_code` \| `config` \| `other` \| `unknown`
- **`lifecycle_state`:** `draft` \| `under_review` \| `ratified` \| `not_applicable`
- **`allowed_actions`:** `read_only` \| `edit_markdown` \| `run_script` \| `create_commit` \| `no_writes`

---

## 3. Agent registration check

1. Load **`reference/agent_registry.yaml`** at the **pinned** governance revision for the session.
2. Resolve **`agent_id`** (from session configuration or PR body for automation) to **one** row.
3. Confirm **`class`** equals **`task_type`** (**AIOS-OPS-004** §2.2).
4. Confirm **repository** matches **`repo_scope`** and **`authority_scope`** / **AIOS-SPEC-012** §3 rules for that **class**.
5. If **`agent_id`** is missing, unregistered, or **class** mismatches → **fail closed** (**§4**).

---

## 4. Repo boundary check

| `repo_kind` | Requirement |
|-------------|----------------|
| **`governance_repository`** | Governed path edits **only** under this repo’s layout (`amendments/`, `specifications/`, `core/`, `commercial/`, `reference/`, `legal/`, `operations/`, etc.) per **AIOS-OPS-004** §2 / §5. |
| **`implementation_repository`** | **MUST NOT** author **normative** governance; **AIOS-OPS-004** §3.1. |

---

## 5. Artifact classification

Every touched file **SHALL** be classified per **AIOS-OPS-004** §5.2: `normative_governance`, `informative`, `generated_registry`, `implementation`, `test`, `unknown`. **`artifact_type`** in preflight **SHALL** be consistent with paths and task type (**AIOS-OPS-007** §4).

---

## 6. Fail-closed refusal behavior

On **any** **AIOS-OPS-004** §4 condition, incomplete preflight, invalid enum, **registry / registry_generator** failure, or **class** / **scope** mismatch:

1. Emit **`aios_enforcement_failure`** JSON exactly as **AIOS-OPS-004** §4.1 (minimum keys).
2. **Block** writes, commit suggestions, and merge actions for normative governance for the remainder of the turn until resolved.
3. **SHALL NOT** silently continue or rephrase the task to bypass checks.

---

## 7. Governance repo vs implementation repo

| Context | Enforcement |
|---------|-------------|
| **Governance repo** | Full preflight + registry validation; after front-matter edits under scanned paths, **`scripts/registry_generator.py`** **must** succeed and committed **`DOCUMENT_REGISTRY.*`** **must** match (**AIOS-OPS-004** §4 / §5). |
| **Implementation repo** | Preflight **still** required; **no** normative governance trees; cite **`document_id`** for compliance claims. |

---

*End of AIOS-OPS-009.*
