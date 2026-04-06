---
document_id: AIOS-OPS-010
registry_id: AIOS-OPS-010
version: 1.0.0
status: ratified
category: operations
title: GitHub Enforcement — Activation Runbook
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
reviewers: []
cross_references:
  - AIOS-OPS-005
  - AIOS-OPS-006
  - AIOS-OPS-008
  - AIOS-OPS-013
  - AIOS-OPS-014
  - AIOS-OPS-015
  - AMD-2026-010
---

# AIOS-OPS-010 — GitHub Enforcement — Activation Runbook

**Normative law:** **[AIOS-OPS-005](GitHubGovernanceGates.md)**. This runbook is **procedural** only. Pair with **[AIOS-OPS-008](GitHubBranchProtectionActivationChecklist.md)** (checklist) and **[AIOS-OPS-006](GitHubGovernanceGatesImplementationPlan.md)** (implementation plan).

**Package summary:** **[AIOS-OPS-013 — Enforcement Activation Handoff Summary](EnforcementActivationHandoffSummary.md)** (narrative handoff); **[AIOS-OPS-014 — Activation Export Index](ActivationExportIndex.md)** (operator index); **[AIOS-OPS-015 — Activation Command Checklist](ActivationCommandChecklist.md)** (commands).

---

## 1. What you are enabling

| Artifact | Purpose |
|----------|---------|
| **`.github/workflows/governance-integrity.yml`** | Runs **`scripts/governance_integrity_check.py`** on PR/push to `main` / `master`. |
| **Branch protection** | Controls whether failing checks **block** merge (**Phase 2**) or only **warn** (**Phase 1**). |

**Required status check (GitHub UI name):** the workflow **`Governance integrity`** / job **`governance-integrity`** (exact label may include org/repo prefix; pick the check that maps to this workflow).

---

## 2. Required GitHub settings (repository or org)

1. **Actions enabled** for this repository (Settings → Actions → General).
2. **Workflow permissions:** default `contents: read` in the workflow is sufficient; no extra secrets required for the integrity job.
3. **Branch protection** on the **default branch** (`main` or `master`): configure per §3.

**Org-level:** If the org uses **rulesets**, map the same requirements (required checks, no direct pushes) there instead of classic branch rules.

---

## 3. Branch protection sequence (recommended order)

1. Merge **`.github/workflows/governance-integrity.yml`** to the default branch so the workflow appears in the Actions tab.
2. Open a **no-op or docs-only PR** (or push an empty commit) to trigger the workflow once; confirm the job **governance-integrity** appears green or fails for an expected, fixable reason.
3. **Settings → Branches → Add rule** (or edit existing) for `main` / `master`:
   - Enable **Require a pull request before merging**.
   - Set **required reviewers** per org policy (not fixed by AIOS-OPS-005).
   - **Do not** yet require the governance check if you are still in **Phase 1** (warn).
4. After trust in the workflow, add **Require status checks to pass** and select **`governance-integrity`** (or the exact name GitHub shows).
5. Enable **Restrict who can push** (or equivalent) so routine work uses PRs.

---

## 4. Phase 1 (warn) → Phase 2 (block)

| Phase | Branch protection | Expected behavior |
|-------|-------------------|-------------------|
| **1 — Warn** | Do **not** list governance integrity as **required** (or use a separate optional check / org policy that does not block merge). | Failures are **visible** in PR checks; merges may still proceed while triaging false positives. |
| **2 — Block** | Add **`governance-integrity`** (or equivalent) to **Required status checks**. | Failing integrity **blocks** merge until fixed or **AIOS-OPS-005** **governance-exception** process applies (if adopted). |

**Transition steps:** (1) Resolve or document any false positives from Phase 1. (2) Record org agreement to enforce (internal memo or amendment appendix per org practice). (3) Flip **required** check on for the protected branch.

---

## 5. Validation after activation

| Step | Pass criteria |
|------|----------------|
| Local | `py -3 scripts/governance_integrity_check.py` prints **`governance_integrity_check: OK`**. |
| CI | PR shows **Governance integrity** workflow run; job **governance-integrity** completes. |
| Registry | After front-matter edits to governed docs, `py -3 scripts/registry_generator.py` and commit **`DOCUMENT_REGISTRY.*`** so **G-7** passes. |
| Protection | A test PR with an intentional registry drift **cannot** merge when Phase 2 is on (check fails). |

---

## 6. Rollback / temporary disable

| Need | Action |
|------|--------|
| **Stop blocking merges** | Remove **`governance-integrity`** from **required** status checks (revert to Phase 1). Optionally disable workflow via **Actions → workflow → disable** (use only for emergencies). |
| **Hotfix without CI** | Org owners may use **admin bypass** if enabled — **document** bypass reason per org policy; **not** a substitute for **governance-exception** if law requires it. |
| **Restore** | Re-enable workflow; re-add required check; confirm green run on `main`. |

---

## 7. Out of scope (this runbook does not configure)

- **`scripts/ci_governance_dry_run.py`** / peer-review dry-run pipeline — see **[ReviewPipelineToolingGap.md](ReviewPipelineToolingGap.md)**.
- **Secrets**, **environments**, **deployment** protection rules.

---

*End of AIOS-OPS-010.*
