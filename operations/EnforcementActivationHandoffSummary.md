---
document_id: AIOS-OPS-013
registry_id: AIOS-OPS-013
version: 1.0.0
status: ratified
category: operations
title: Enforcement Activation — Handoff Summary
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-06
reviewers: []
cross_references:
  - AIOS-OPS-004
  - AIOS-OPS-005
  - AIOS-OPS-008
  - AIOS-OPS-009
  - AIOS-OPS-010
  - AIOS-OPS-011
  - AIOS-OPS-012
  - AIOS-OPS-014
  - AIOS-OPS-015
  - AIOS-OPS-016
  - AIOS-OPS-017
  - AIOS-OPS-018
  - AIOS-OPS-019
  - AMD-2026-010
---

# AIOS-OPS-013 — Enforcement Activation — Handoff Summary

**This document is a handoff package, not new law.** It points to ratified standards and procedural runbooks already in this repository.

**Operator export index:** **[AIOS-OPS-014 — Activation Export Index](ActivationExportIndex.md)** (single page index). **Commands:** **[AIOS-OPS-015 — Activation Command Checklist](ActivationCommandChecklist.md)**. **GitHub host result record:** **[AIOS-OPS-017](GitHubHostActivationResult.md)**. **Cursor handoff:** **[AIOS-OPS-016](CursorHostActivationHandoff.md)**. **Cursor activation result / checklist:** **[AIOS-OPS-018](CursorHostActivationResult.md)**, **[AIOS-OPS-019](CursorActivationChecklist.md)**.

---

## 1. Current status

### What is ratified

- **Amendment:** **[AMD-2026-010](../amendments/AMD-2026-010.md)** (Governance Enforcement Package v1), with motion **[AMD-2026-010-ratification-motion.md](../amendments/AMD-2026-010-ratification-motion.md)** as recorded.
- **Operations / specification (package):** **[AIOS-OPS-004](CursorAgentExecutionRules.md)**, **[AIOS-OPS-005](GitHubGovernanceGates.md)**, **[AIOS-SPEC-012](../specifications/AgentClassRegistrationAndAuthorityModel.md)**.
- **Implementation plans (non-normative):** **[AIOS-OPS-006](GitHubGovernanceGatesImplementationPlan.md)**, **[AIOS-OPS-007](CursorAgentExecutionRulesImplementationPlan.md)**.
- **Activation artifacts (procedural):** **[AIOS-OPS-008](GitHubBranchProtectionActivationChecklist.md)** through **[AIOS-OPS-012](ReviewPipelineToolingGap.md)**; this summary (**AIOS-OPS-013**); export packaging **[AIOS-OPS-014](ActivationExportIndex.md)**, **[AIOS-OPS-015](ActivationCommandChecklist.md)**.

### What is activation-ready (in-repo)

| Layer | Artifacts |
|-------|-----------|
| **GitHub CI** | **`.github/workflows/governance-integrity.yml`** → **`scripts/governance_integrity_check.py`** |
| **Cursor / IDE** | **[AIOS-OPS-009](CursorEnforcementContract.md)**, **`reference/schemas/cursor_preflight.schema.json`**, **`reference/agent_registry.yaml`** |
| **Procedure** | **[AIOS-OPS-010](GitHubEnforcementActivationRunbook.md)**, **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)**, **[AIOS-OPS-014](ActivationExportIndex.md)**, **[AIOS-OPS-015](ActivationCommandChecklist.md)** |

### What is not yet live (host-side)

| Item | Notes |
|------|--------|
| **Branch protection + required checks** | **May be live** on **`main`** — see **[AIOS-OPS-017](GitHubHostActivationResult.md)**. |
| **Cursor rules / skills** | Must reference **AIOS-OPS-009** and the schema/registry paths; **Cursor does not auto-load** AIOS enforcement. |
| **Review-pipeline dry-run in CI** | **Not** enabled — **`automated_review_pipeline.py`** is absent; see **§4**. |

---

## 2. GitHub activation steps

| Item | Value |
|------|--------|
| **Workflow file** | **`.github/workflows/governance-integrity.yml`** |
| **Workflow name (Actions UI)** | **`Governance integrity`** |
| **Job ID (status check)** | **`governance-integrity`** — select this name (or the GitHub-displayed equivalent that maps to this job) under **Required status checks** after the workflow has run at least once. |
| **Triggers** | Pull requests and pushes to **`main`** / **`master`** |
| **Local validation** | `py -3 scripts/governance_integrity_check.py` → must print **`governance_integrity_check: OK`** |

**Branch protection requirements** (detail): **[AIOS-OPS-008](GitHubBranchProtectionActivationChecklist.md)**; sequence and phases: **[AIOS-OPS-010](GitHubEnforcementActivationRunbook.md)** §§2–4.

**Rollback path:** **[AIOS-OPS-010](GitHubEnforcementActivationRunbook.md)** §6 (remove required check, optionally disable workflow, restore).

---

## 3. Cursor activation steps

| Item | Path / document |
|------|-----------------|
| **Contract (human-readable)** | **`operations/CursorEnforcementContract.md`** (**AIOS-OPS-009**) |
| **Preflight schema (JSON Schema)** | **`reference/schemas/cursor_preflight.schema.json`** |
| **Agent registry (YAML)** | **`reference/agent_registry.yaml`** |
| **Runbook** | **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)** |

**Fail-closed requirements:** Preflight JSON must validate to the schema; **`agent_id`** must resolve in the registry with **`class`** = **`task_type`**; on failure emit **`aios_enforcement_failure`** per **AIOS-OPS-004** §4.1 — see **AIOS-OPS-009** §6 and **AIOS-OPS-011** §4.

**Rollback path:** **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)** §7 (disable or relax Cursor rules/skills; humans may still edit; GitHub CI remains separate).

---

## 4. Known tooling gap (**AIOS-OPS-012**)

- **`scripts/ci_governance_dry_run.py`** expects **`scripts/automated_review_pipeline.py`**, which **does not exist** in this repository.
- **Do not** add **`ci_governance_dry_run`** to **`governance-integrity.yml`** until a real pipeline ships or **`ci_governance_dry_run.py`** is refactored to call an in-repo entry point — see **[ReviewPipelineToolingGap.md](ReviewPipelineToolingGap.md)** (**AIOS-OPS-012**).
- **Explicit:** review-pipeline **dry-run is not to be enabled** in CI under the current repo contents.

---

## 5. Activation decision boundary

### What a host admin / operator must do

- **GitHub:** Enable Actions; merge workflow to default branch; configure **branch protection** and **required** status check **`governance-integrity`** (or UI equivalent) when moving to Phase 2 block — **[AIOS-OPS-010](GitHubEnforcementActivationRunbook.md)**.
- **Cursor (or equivalent):** Install **project rules** / **skills** that bind to **AIOS-OPS-009**, **`cursor_preflight.schema.json`**, and **`agent_registry.yaml`** at a **pinned** governance revision — **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)**.
- **Process:** Agree Phase 1 vs Phase 2 timing; document emergency bypass policy per org (not rewritten here).

### What remains outside this governance repository

- **GitHub.com / Enterprise** org and repo settings UI, **rulesets**, **secrets**, **bot accounts**, **team review** policies.
- **Cursor** (or other IDE) **product configuration** and **local** developer machines.
- **Implementation / product repositories** and their CI — only **reference** this repo’s law and registry; normative governance **does not** live there (**AIOS-OPS-004** §3).

---

*End of AIOS-OPS-013.*
