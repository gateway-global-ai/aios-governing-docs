---
document_id: AIOS-OPS-015
registry_id: AIOS-OPS-015
version: 1.0.0
status: ratified
category: operations
title: Activation — Command Checklist
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
reviewers: []
cross_references:
  - AIOS-OPS-013
  - AIOS-OPS-014
---

# AIOS-OPS-015 — Activation — Command Checklist

**Procedural checklist only — not new law.** Pair with **[AIOS-OPS-014 — Activation Export Index](ActivationExportIndex.md)** and **[AIOS-OPS-013 — Enforcement Activation Handoff Summary](EnforcementActivationHandoffSummary.md)**.

All commands assume **repository root** and **Python 3** available as `py -3` (Windows) or `python3` (Unix). Only commands that exist in this repo are listed — **no** `ci_governance_dry_run` / **`automated_review_pipeline.py`** (see **[AIOS-OPS-012](ReviewPipelineToolingGap.md)**).

---

## Before activation (local verification)

| Step | Command or check |
|------|-------------------|
| 1 | `cd` to repo root (`aios-governing-docs` clone). |
| 2 | **Registry generation:** `py -3 scripts/registry_generator.py` |
| 3 | If step 2 changed `DOCUMENT_REGISTRY.md` / `DOCUMENT_REGISTRY.json`, **commit** those files before continuing (required for **G-7**). |
| 4 | **Integrity:** `py -3 scripts/governance_integrity_check.py` — must output **`governance_integrity_check: OK`** |
| 5 | **Workflow file present:** path **`.github/workflows/governance-integrity.yml`** exists in the tree (verify in editor or file manager). |
| 6 | **Schema file present:** **`reference/schemas/cursor_preflight.schema.json`** |
| 7 | **Agent registry present:** **`reference/agent_registry.yaml`** |

---

## After GitHub settings (host)

| Step | Action |
|------|--------|
| 1 | Confirm **Actions** shows workflow **Governance integrity** ran on a PR or push to `main` / `master`. |
| 2 | Re-run locally: `py -3 scripts/governance_integrity_check.py` on the same commit the branch uses. |
| 3 | After enabling **required** check **`governance-integrity`**, open a test PR that intentionally skips registry regen — merge **should** be blocked in Phase 2 (see **[AIOS-OPS-010](GitHubEnforcementActivationRunbook.md)**). |

---

## After Cursor bindings (operator)

| Step | Action |
|------|--------|
| 1 | Confirm project rules/skills cite **AIOS-OPS-009** and paths under **`reference/`** per **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)**. |
| 2 | Run one **sample** preflight JSON through a JSON Schema validator against **`reference/schemas/cursor_preflight.schema.json`**. |
| 3 | Re-run: `py -3 scripts/governance_integrity_check.py` before pushing governance doc changes. |

---

## Rollback verification

| Step | Command or check |
|------|-------------------|
| 1 | `py -3 scripts/governance_integrity_check.py` — still **OK** on a clean tree after disabling a host-side toggle (does not remove repo scripts). |

---

*End of AIOS-OPS-015.*
