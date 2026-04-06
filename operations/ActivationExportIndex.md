---
document_id: AIOS-OPS-014
registry_id: AIOS-OPS-014
version: 1.0.0
status: ratified
category: operations
title: Activation — Export Index
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
reviewers: []
cross_references:
  - AIOS-OPS-008
  - AIOS-OPS-009
  - AIOS-OPS-010
  - AIOS-OPS-011
  - AIOS-OPS-012
  - AIOS-OPS-013
  - AIOS-OPS-015
  - AMD-2026-010
---

# AIOS-OPS-014 — Activation — Export Index

**Packaging artifact only — not new law.** Use this page as the **single operator-facing index** to turn on enforcement. Narrative context: **[AIOS-OPS-013 — Enforcement Activation Handoff Summary](EnforcementActivationHandoffSummary.md)**.

**Enforcement is not live** until a **host admin** applies GitHub settings and **operators** bind Cursor (or equivalent) per the runbooks. Committing these files to the repo **does not** by itself enable branch protection or IDE enforcement.

---

## GitHub activation entrypoint

| Read first | Role |
|------------|------|
| **[AIOS-OPS-013](EnforcementActivationHandoffSummary.md)** | Status, boundaries, rollback pointers |
| **[AIOS-OPS-010](GitHubEnforcementActivationRunbook.md)** | Branch protection sequence, Phase 1 vs 2, validation |
| **[AIOS-OPS-008](GitHubBranchProtectionActivationChecklist.md)** | Checklist for protection rules |

| Deploy | Path |
|--------|------|
| **Workflow** | **`.github/workflows/governance-integrity.yml`** |
| **CI script** | **`scripts/governance_integrity_check.py`** |
| **Required check (job ID)** | **`governance-integrity`** |
| **Workflow display name** | **`Governance integrity`** |

---

## Cursor activation entrypoint

| Read first | Role |
|------------|------|
| **[AIOS-OPS-011](CursorEnforcementActivationRunbook.md)** | Bindings, validation, rollback |
| **[AIOS-OPS-009](CursorEnforcementContract.md)** | Runtime contract (preflight, fail-closed) |

| Artifact | Path |
|----------|------|
| **Contract** | **`operations/CursorEnforcementContract.md`** |

---

## Branch protection checklist

- **[AIOS-OPS-008 — GitHub Branch Protection — Activation Checklist](GitHubBranchProtectionActivationChecklist.md)**

---

## Tooling gap note

- **[AIOS-OPS-012 — Review Pipeline Tooling Gap](ReviewPipelineToolingGap.md)** — **`ci_governance_dry_run` / `automated_review_pipeline.py`** must **not** be wired into CI until resolved.

---

## Schema path

| File | Path |
|------|------|
| **Preflight JSON Schema** | **`reference/schemas/cursor_preflight.schema.json`** |

---

## Registry path

| File | Path |
|------|------|
| **Agent registry (YAML)** | **`reference/agent_registry.yaml`** |

---

## Required validation command(s)

Run from **repository root** (same as **[AIOS-OPS-013](EnforcementActivationHandoffSummary.md)** §2):

```bash
py -3 scripts/registry_generator.py
py -3 scripts/governance_integrity_check.py
```

Success: terminal prints **`governance_integrity_check: OK`**. Commit **`DOCUMENT_REGISTRY.md`** and **`DOCUMENT_REGISTRY.json`** whenever `registry_generator.py` changes them.

Detailed operator steps: **[AIOS-OPS-015 — Activation Command Checklist](ActivationCommandChecklist.md)**.

---

*End of AIOS-OPS-014.*
