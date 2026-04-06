---
document_id: AIOS-OPS-017
registry_id: AIOS-OPS-017
version: 1.1.0
status: ratified
category: operations
title: GitHub Host Activation — Result Record
author: Gateway Global AIOS
created: 2026-04-05
last_updated: 2026-04-06
reviewers: []
cross_references:
  - AIOS-OPS-008
  - AIOS-OPS-010
  - AIOS-OPS-014
  - AIOS-OPS-015
---

# AIOS-OPS-017 — GitHub Host Activation — Result Record

**Operational record — not law.** Documents **repo-level** branch protection applied to **`gateway-global-ai/aios-governing-docs`** via GitHub REST API (**Phase 2** posture per **AIOS-OPS-008** / **AIOS-OPS-010**).

---

## 1. Activation date

**2026-04-06** — branch protection applied and verified via API readback.

---

## 2. Branch targeted

**`main`** (default branch; confirmed via `GET /repos/gateway-global-ai/aios-governing-docs`).

---

## 3. Local repo verification (pre-activation)

| Check | Result |
|-------|--------|
| **`py -3 scripts/registry_generator.py`** | Run completed |
| **`py -3 scripts/governance_integrity_check.py`** | **`governance_integrity_check: OK`** (after committing registry timestamp drift) |
| Working tree | **Not fully clean** (unrelated local edits/untracked files possible); validation run against **committed** state |

**Workflow inspection (repo source of truth):**

| Field | Value |
|-------|--------|
| File | **`.github/workflows/governance-integrity.yml`** |
| Workflow `name` (display) | **`Governance integrity`** |
| Job id | **`governance-integrity`** |
| **Required status check context used** | **`Governance integrity / governance-integrity`** (GitHub Actions convention: workflow display name + `/` + job id; matches **AIOS-OPS-010** §1) |

**Check name discovery note:** `GET .../commits/{sha}/check-runs` and **Actions workflow runs** list returned **403** (“Resource not accessible by personal access token”) — fine-grained token **lacks Actions read** scopes. The required context was taken from **`.github/workflows/governance-integrity.yml`** + **AIOS-OPS-010** / **AIOS-OPS-008**, not from live check-run enumeration.

---

## 4. GitHub state before activation

| Item | Value |
|------|--------|
| **Default branch** | `main` |
| **Actions** | **Enabled** (`GET .../actions/permissions` → `enabled: true`) |
| **Branch protection on `main`** | **Absent** (`GET .../branches/main/protection` → **404** “Branch not protected”) |

---

## 5. Settings applied (`PUT .../branches/main/protection`)

| Setting | Applied value | Rationale (runbooks) |
|---------|----------------|----------------------|
| **Required status checks** | **Strict** = true; contexts = **`Governance integrity / governance-integrity`** | **AIOS-OPS-008** §5 Phase 2 block; **AIOS-OPS-010** §4 |
| **Require pull request reviews** | **1** approving review | **AIOS-OPS-008** §3 (minimum 1 common; org policy not fixed) |
| **Dismiss stale reviews** | false | — |
| **Require code owner reviews** | false | Not mandated by docs |
| **Require last push approval** | false | — |
| **Enforce admins** | **true** | **AIOS-OPS-008** §3 — include administrators so rules apply to admins |
| **Required conversation resolution** | **true** | Supported by API; aligns with merge quality (not explicit in checklist table; recorded here) |
| **Required linear history** | false | Optional per **AIOS-OPS-008** |
| **Allow force pushes** | false | |
| **Allow deletions** | false | |
| **Block creations** | false | |
| **Push restrictions (users/teams)** | **None** (`restrictions: null`) | **AIOS-OPS-008** “Restrict who can push” is **org/UI**-dependent; classic API `restrictions: null` = no extra user/team allowlist. **PR required + reviews** enforces governed merge path for routine work. |

**Org-level rulesets:** **Not** configured (per **AIOS-OPS-008** §6).

---

## 6. Settings verified after activation (`GET .../branches/main/protection`)

| Item | Verified |
|------|----------|
| Protection present on **`main`** | **Yes** |
| **`enforce_admins`** | **true** |
| **`required_approving_review_count`** | **1** |
| **`required_conversation_resolution`** | **true** |
| **`required_status_checks.strict`** | **true** |
| **Required context** | **`Governance integrity / governance-integrity`** |
| **`allow_force_pushes`** | **false** |

---

## 7. Exact required check name used

**`Governance integrity / governance-integrity`**

---

## 8. Remaining manual / blockers

| Item | Status |
|------|--------|
| **Push local commits** | Clone was **ahead of `origin/main`** before activation; **push** `main` so remote workflow and branch protection align with local governance commits (operator action). |
| **Actions read on token** | **403** on check-runs / workflow-runs — add **Actions: Read** (fine-grained) if future automation must **list** runs to discover check names. **Not** required for protection already applied. |
| **Verify check appears on PRs** | Open a PR or use existing PR to confirm **Governance integrity** runs and the required check turns green when integrity passes. |

---

## 9. GitHub-side governance enforcement live?

**Yes — for `main`,** with **Phase 2** posture: merges **require** a **passing** required check **`Governance integrity / governance-integrity`**, **1** approval, **conversation resolution**, and **admin enforcement** — **subject to** GitHub applying checks to the merge path (if the check has **never** run on the repo, GitHub may not list it until the workflow has executed at least once on a PR; if merges are blocked unexpectedly, confirm the workflow has run and the context string matches the **Checks** tab).

---

*End of AIOS-OPS-017.*
