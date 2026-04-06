---
document_id: AIOS-OPS-017
registry_id: AIOS-OPS-017
version: 1.0.0
status: ratified
category: operations
title: GitHub Host Activation — Result Record
author: Gateway Global AIOS
created: 2026-04-05
last_updated: 2026-04-05
reviewers: []
cross_references:
  - AIOS-OPS-008
  - AIOS-OPS-010
  - AIOS-OPS-014
  - AIOS-OPS-015
  - AMD-2026-010
---

# AIOS-OPS-017 — GitHub Host Activation — Result Record

**Operational record — not law.** Intended to capture **what was actually done** on the GitHub host. This revision was produced in an environment where **automated GitHub API access was not available**.

---

## 1. Date

**2026-04-05** — record created (handoff / agent execution).

---

## 2. Branch targeted

**`main`** — per **[AIOS-OPS-010](GitHubEnforcementActivationRunbook.md)** and remote **`origin`** (`https://github.com/gateway-global-ai/aios-governing-docs.git`). **Default branch name was not verified** via GitHub API in this session.

---

## 3. Local repo verification (pre-flight)

| Check | Result |
|-------|--------|
| **`py -3 scripts/registry_generator.py`** | Run completed |
| **`py -3 scripts/governance_integrity_check.py`** | **`governance_integrity_check: OK`** |
| Working tree | **Not clean** (local modifications and untracked files present in clone); integrity check still passed against **committed** `DOCUMENT_REGISTRY.*` after regeneration |

---

## 4. Tooling attempted for GitHub host inspection / change

| Attempt | Result |
|---------|--------|
| **`gh` CLI** (`gh auth status`, API calls) | **`gh` not found** on PATH (Windows PowerShell) |
| **`GITHUB_TOKEN` / `GH_TOKEN`** | **Not set** in environment |
| **GitHub REST API** (curl) | **Not invoked** — no bearer token available |

**Conclusion:** No read or write of GitHub repository settings (Actions, branch protection, required checks) could be performed from this session.

---

## 5. Settings found before activation

**Not retrieved.** The following could **not** be queried without authenticated access:

- Whether **GitHub Actions** is enabled for the repository
- **Default branch** name (assumed `main` from docs + typical remote)
- **Branch protection** on `main` (rules, required reviews, required checks)
- Whether check **`governance-integrity`** / workflow **Governance integrity** is **required**
- **Restrict pushes** / **admin bypass** flags

---

## 6. Settings changed via this session

**None.** No `gh api`, GraphQL, or REST calls were executed with credentials.

---

## 7. Settings verified after activation

**N/A** — no host changes applied from this session.

---

## 8. Settings that could not be changed or verified (blocker)

| Desired action (per **AIOS-OPS-008** / **AIOS-OPS-010**) | Blocker |
|----------------------------------------------------------|---------|
| Enable Actions (if off) | Requires GitHub UI or API with **`repo`** scope |
| Add branch protection rule on `main` | Requires **admin** on repo or org ruleset API |
| Require PR before merge | Same |
| Restrict direct pushes | Same |
| Add **required** status check **`governance-integrity`** | Requires protection rule API after workflow has produced a check run at least once |
| Read back protection JSON | Requires **`gh api repos/:owner/:repo/branches/:branch/protection`** or equivalent with auth |

---

## 9. Exact manual steps still required (admin)

1. Install **[GitHub CLI](https://cli.github.com/)** and run **`gh auth login`** with a user/token that has **admin** on **`gateway-global-ai/aios-governing-docs`**, **or** use the GitHub **web UI**: **Settings → General → Actions** (enable if needed).
2. Confirm workflow **`.github/workflows/governance-integrity.yml`** is on **`main`** and trigger at least one run (push or PR) so the **`governance-integrity`** check appears.
3. **Settings → Branches** → add/edit rule for **`main`** per **[AIOS-OPS-008](GitHubBranchProtectionActivationChecklist.md)** and **[AIOS-OPS-010](GitHubEnforcementActivationRunbook.md)** §§3–4 (Phase 1 warn vs Phase 2 block).
4. Optional verification:  
   `gh api repos/gateway-global-ai/aios-governing-docs/branches/main/protection`

---

## 10. Is GitHub-side governance enforcement “live”?

**Cannot be asserted from this session.** After an admin completes §9, enforcement is **live** only when:

- Branch protection matches **Phase 2** posture (required **governance-integrity** if blocking), **or** **Phase 1** (non-blocking) per org choice — and  
- **`governance_integrity_check.py`** passes on the protected branch’s commits.

Update this file or add a dated addendum when host work is done.

---

*End of AIOS-OPS-017.*
