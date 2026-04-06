---
document_id: AIOS-OPS-012
registry_id: AIOS-OPS-012
version: 1.0.0
status: ratified
category: operations
title: Review Pipeline Tooling Gap
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
reviewers: []
cross_references:
  - AIOS-OPS-005
  - AIOS-OPS-006
---

# AIOS-OPS-012 — Review Pipeline Tooling Gap

**This is an operational gap record, not new law.** It explains why **PR dry-run** integration is **not** enabled in this repository’s CI today.

---

## 1. What references `automated_review_pipeline.py`

| Location | Reference |
|----------|-----------|
| **`scripts/ci_governance_dry_run.py`** | Expects **`scripts/automated_review_pipeline.py`** with `--document` and `--dry-run` (see source lines ~118–135). |
| **`prompts/automated_openai_revision.md`** | Header states assembly by **`scripts/automated_review_pipeline.py`**. |
| **`.github/workflows/governance-integrity.yml`** | Comment **TODO**: optional hook for **`ci_governance_dry_run`** when pipeline exists. |
| **`reviews/LIFECYCLE_SYSTEM_MIGRATION_REPORT.md`** | Notes missing script (operational). |

**There is no `automated_review_pipeline.py` in `scripts/` in this repository.**

---

## 2. Why this blocks dry-run enablement

- **`ci_governance_dry_run.py`** **exits non-zero** if the pipeline file is missing when it would otherwise invoke it (changed-doc path).
- Enabling that script in **GitHub Actions** without a real implementation would produce **false failures** or require a **fake** stub that invents behavior — **not** acceptable for this governance repo.
- **AIOS-OPS-005** / **AIOS-OPS-006** describe broader checks (e.g. **G-5** review claims); the repo currently implements **G-1**, **G-3**, **G-7**, and YAML parse via **`governance_integrity_check.py`** only.

---

## 3. Correct next action (chosen disposition)

| Option | Disposition |
|--------|-------------|
| Stub placeholder | **Rejected** — would invent or simulate pipeline behavior. |
| Re-point dry-run only | **No safe target** — nothing else in-repo exposes the same `--dry-run` / `ready_for_full_run` contract. |
| **Formal gap note** | **Accepted** — this document, plus truthful comments in workflow and **`ci_governance_dry_run.py`**. |

---

## 4. What implementation is still needed

To enable **`ci_governance_dry_run.py`** in CI **truthfully**, a maintainer **SHALL** either:

1. **Add** `scripts/automated_review_pipeline.py` that implements the interface implied by **`ci_governance_dry_run.py`** (document path, `--dry-run`, exit codes / reports as documented in that caller), **or**
2. **Refactor** `ci_governance_dry_run.py` to call an **existing** pipeline entry point that is actually shipped in this repo, and update **`prompts/automated_openai_revision.md`** accordingly.

Until then, **do not** add **`ci_governance_dry_run.py`** to **`governance-integrity.yml`** unless the dependency exists.

---

## 5. What is already activation-ready without this pipeline

- **`scripts/governance_integrity_check.py`** (G-1, G-3, G-7, agent registry YAML parse, schema JSON validity).
- **`operations/GitHubEnforcementActivationRunbook.md`** (**AIOS-OPS-010**).

---

*End of AIOS-OPS-012.*
