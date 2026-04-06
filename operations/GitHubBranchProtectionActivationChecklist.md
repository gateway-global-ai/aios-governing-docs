---
document_id: AIOS-OPS-008
registry_id: AIOS-OPS-008
version: 1.0.0
status: ratified
category: operations
title: GitHub Branch Protection — Activation Checklist
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
reviewers: []
cross_references:
  - AIOS-OPS-005
  - AIOS-OPS-006
  - AIOS-OPS-010
  - AIOS-OPS-012
  - AMD-2026-010
---

# AIOS-OPS-008 — GitHub Branch Protection — Activation Checklist

**Law:** **[AIOS-OPS-005](GitHubGovernanceGates.md)** (ratified). This checklist is **procedural** (admin configuration), **not** new normative text. Settings **are not** asserted as already applied until a repo admin records them.

**Handoff:** Step-by-step activation → **[AIOS-OPS-010 — GitHub Enforcement Activation Runbook](GitHubEnforcementActivationRunbook.md)**. Review pipeline CI gap → **[AIOS-OPS-012](ReviewPipelineToolingGap.md)**.

---

## 1. Preconditions

- [ ] Workflow **`.github/workflows/governance-integrity.yml`** is present on the default branch.
- [ ] `py -3 scripts/governance_integrity_check.py` passes locally.
- [ ] Org/repo owners agree **Phase** (warn vs block) per **AIOS-OPS-005** / **AIOS-OPS-006** §4–§5.

---

## 2. Required status checks (to add in branch protection)

| Check name (workflow job) | Purpose |
|---------------------------|---------|
| **`governance-integrity`** (job) | **G-1**, **G-3**, **G-7** + YAML parse; see **AIOS-OPS-006** §2 |

**Admin:** In GitHub → **Settings → Branches → Branch protection rule** for `main` (or default branch), under **Status checks that are required**, add the check reported by Actions for this workflow once it has run at least once on the branch.

---

## 3. Branch protection rules (admin)

| Setting | Required for activation |
|---------|-------------------------|
| **Require a pull request before merging** | Yes |
| **Require approvals** | Set per org policy (minimum **1** review is common; **AIOS-OPS-005** does not fix a number—configure to org policy). |
| **Require status checks to pass** | **Phase 2:** yes, for listed checks. **Phase 1:** optional (see §5). |
| **Restrict who can push to matching branches** | Yes — **no direct pushes** to `main` for routine work; use PRs. |
| **Include administrators** | Org policy (often **on** so rules apply to admins). |

**Note:** Exact UI labels vary by GitHub plan (public/private). Features such as **required reviewers** or **required linear history** are **optional** unless org policy mandates them.

---

## 4. Phase 1 — Warn

- Run workflow as **required** or **optional** per org choice; failures **should** surface as **warnings** or **non-blocking** until false positives are resolved.
- **Do not** claim **AIOS-OPS-005** Phase 2 block behavior until **§5** is satisfied.

---

## 5. Phase 2 — Block

- Set **governance-integrity** (or the org’s chosen name for the job) as a **required** status check on the protected branch.
- Merges **SHALL NOT** bypass failing **required** checks except via **AIOS-OPS-005** **governance-exception** process **if** your org adopts that path.

---

## 6. Not in scope for this repo

- **Org-wide** rulesets, **GitHub Enterprise** policy APIs, and **secrets** — configure in **GitHub org settings** by administrators; **not** stored in this repository.

---

*End of AIOS-OPS-008.*
