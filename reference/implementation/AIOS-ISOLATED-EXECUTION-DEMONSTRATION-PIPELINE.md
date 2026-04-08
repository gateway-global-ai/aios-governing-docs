---
document_id: AIOS-EXEC-DEMO-001
version: 0.1.3
status: draft
category: reference
title: Isolated execution demonstration pipeline (draft proposal)
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-08
cross_references:
  - doc_id: AIOS-AMD-PLAN-001
  - doc_id: AMD-2026-005
  - doc_id: AIOS-REF-013
amendment_history:
  - version: 0.1.3
    date: 2026-04-08
    summary: Schema 1.2.0 operator_disclosures (binding vs packet-only, validation proof honesty); HUMAN_REVIEW_PACKET navigation-first; sample packets under reviews/demo_exec_packet_*; runner 0.3.0.
  - version: 0.1.2
    date: 2026-04-07
    summary: Transaction schema 1.1.0 — product_repo_path, ISO timestamps, artifacts index, failure_stage, human_review_status; runner 0.2.0; optional --source-repo-url.
  - version: 0.1.1
    date: 2026-04-07
    summary: MVP runner `scripts/run_isolated_execution_demo.py` — execution packet under `reviews/<slug>/execution/`, git worktree + npm validation, schema fields for governance path and runner version; templates `VALIDATION_COMMANDS.example.json`.
  - version: 0.1.0
    date: 2026-04-07
    summary: Initial draft — transition framing from pre-ratification planning automation to branch-isolated execution lane; gap analysis, MVP sequence, transaction schema, branch procedure; system prompt in prompts/.
---

# Isolated execution demonstration pipeline (draft proposal)

**Purpose:** **Non-normative** proposal for a **governed execution lane** that sits **after** the existing **pre-ratification planning** stack (**[AIOS-AMD-PLAN-001](AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** phases B–C) and **before** committee promotion and binding peer review. **Binding law** for ratification remains **[AMD-2026-005](../amendments/AMD-2026-005.md)** — this document does **not** create new ratification rules.

**Related:** Local Ollama planning (`build_agent_kb.py`, `ollama_planning_agent.py`) — [`reference/knowledge_base/agents/README.md`](../knowledge_base/agents/README.md). **MVP runner** — [`scripts/run_isolated_execution_demo.py`](../../scripts/run_isolated_execution_demo.py) (see **Annex E**). **System prompt** for the proposed execution agent — [`prompts/isolated_execution_demonstration_system.md`](../../prompts/isolated_execution_demonstration_system.md). **Machine schema** — [`reference/schemas/execution_transaction.schema.json`](../schemas/execution_transaction.schema.json).

---

## Title

**Transition from pre-ratification planning automation to isolated execution demonstration pipeline**

---

## Status and scope

| Field | Value |
|-------|--------|
| **Status** | Draft proposal |
| **Scope** | Extend the current local Ollama planning system into a **governed execution process** that produces **branch-isolated, visually reviewable output** instead of planning text alone |
| **Basis** | Today’s system automates **Phase B (Architect)** and **Phase C (UI)** planning drafts only; **human verification** remains mandatory; **Phases D–F** are not automated |

---

## 1. Current state

The current system is a **pre-ratification planning workbench**, not a full implementation control plane.

It currently does the following well:

- Builds a **merged knowledge bundle** from a declared manifest of governing documents, snapshots, and research.
- Executes **Architect** and then **UI** in **strict order**.
- Writes **draft** planning outputs under **`reviews/<slug>/planning/`**.
- Makes clear that outputs are **drafts** and must be checked against **actual repo truth** before influencing amendments or specifications.

Therefore the current system has:

| Capability | Present |
|------------|---------|
| Governed inputs | Yes |
| Ordered generation | Yes |
| Draft outputs | Yes |
| Mandatory human verification | Yes (documented) |

| Gap | Present |
|-----|---------|
| Isolated execution against a feature branch | No |
| Reproducible implementation proofs | No |
| Visual or behavioral demonstrations of proposed work | No |
| Machine-enforced traceability from plan to code to output | No |
| Automated promotion from draft plan to reviewable implementation packet | No |

---

## 2. Problem statement

The present planning stack produces **intelligible planning text**, but not yet **intelligible implementation evidence**.

That gap creates three recurring problems:

1. **Operator dependency** — The human operator still carries **system coherence** by deciding whether evidence is stale, whether the manifest is sufficient, whether the plan is grounded, and whether repo truth supports the output.

2. **Weak closure between docs and execution** — The process ends with **“human verification”** rather than a **governed execution transaction** that proves the plan in **code, behavior, and UI**.

3. **Low-feedback artifact quality** — Plans are useful, but humans give materially better feedback when they can inspect a **running surface**, **screenshots**, **behavioral traces**, **changed files**, and **explicit claims tied to visible results**.

---

## 3. Governing conclusion

The next system should **not** be framed as “more planning agents.”

It should be framed as an **Isolated Execution Demonstration Lane** that sits **after planning** and **before** committee or peer-review promotion.

That lane should convert:

**governing docs + evidence + plan drafts**  
into  
**branch-isolated, visually reviewable implementation evidence**

---

## 4. Missing control-plane pieces

The following pieces are **not** present in the planning stack today and are proposed as **governed components** for Phase X.

### 4.1 Planning transaction envelope

Every run should have a **structured execution record**, not only markdown outputs.

Minimum required fields (see **Annex C** and [`execution_transaction.schema.json`](../schemas/execution_transaction.schema.json)):

| Field | Role |
|-------|------|
| `review_slug` | Traceability to `reviews/<slug>/` |
| `source_repo` | Target repository (URL or path) |
| `source_branch` | Branch the work derives from |
| `working_branch` | Isolated feature branch or worktree |
| `governing_manifest_version` | Bundle / manifest identity |
| `evidence_bundle_hash` | Integrity of merged KB inputs |
| `architect_plan_hash` | Integrity of `ARCHITECT_PLAN.md` |
| `ui_plan_hash` | Integrity of `UI_PLAN.md` |
| `execution_scope` | Bounded scope identifier |
| `allowed_surfaces` | UI / route / canvas surface allowlist |
| `required_visual_proofs` | What must be captured |
| `verification_status` | Repo-truth validation state |
| `promotion_status` | Human gate state |

This becomes the **unit of traceability**.

### 4.2 Branch-isolated workspace

The system must be able to:

- Pull the target repo.
- Check out the **target source branch**.
- Create or reset a **feature branch** (or **git worktree**).
- Perform work **only** inside that branch/worktree.
- Record **exact commit SHA** before and after.

**Mandatory:** No direct work on shared branches without explicit governed exception recorded in the transaction.

### 4.3 Execution contract

Planning output must be compiled into a **machine-usable execution contract** defining:

| Topic | Content |
|-------|---------|
| Objective | One sentence outcome |
| In-scope files | Allowlist |
| Forbidden files | Denylist |
| Required tests | Commands / expectations |
| Required visual surfaces | Routes / components |
| Acceptance checks | Pass/fail criteria |
| Evidence to collect | Screenshots, logs, traces |
| Policy exceptions | Any override, disclosed |

Without this contract, the system drifts from **narrative planning** into **open-ended coding**.

### 4.4 Demonstration requirement

A planning run that touches **UI**, **shell**, **canvas**, **routing**, or **flow logic** must produce at least one of:

- Screenshot set  
- Short walkthrough artifact  
- Route/surface map  
- Video or GIF  
- HTML or markdown review deck  
- **Live local preview instructions** with **captured output**

The point is to review **behavior**, not prose alone.

### 4.5 Repo-truth validation

The lane must validate generated claims against **actual code** and **runtime evidence**:

- Changed file list  
- Test results  
- Build results  
- Screenshots  
- Route availability  
- Logs or traces where relevant  

This is the bridge from **documents** to **actual output**.

### 4.6 Promotion gate

No output should advance to committee or peer review **merely** because a plan was generated or code was written.

**Promotion** should require:

- Planning artifacts present  
- Execution contract present  
- Isolated branch evidence present  
- Visual proofs attached (when UI-affecting)  
- Repo validation passed  
- **Human review summary** written  

---

## 5. Proposed next implementation phase

**Phase name:** **Phase X — Isolated execution demonstration pipeline**  
**Goal:** Convert planning drafts into **branch-isolated, visually demonstrable** implementation evidence.

### 5.1 Phase X objectives

Build a governed process that:

1. Accepts a **review slug** and **target repo/branch**.  
2. Assembles the planning/evidence bundle (reuse existing KB build where applicable).  
3. Generates or consumes **Architect/UI** outputs.  
4. Compiles them into an **execution contract**.  
5. Creates an **isolated worktree or branch**.  
6. Applies implementation work **within scope**.  
7. Builds / runs / tests the result.  
8. Captures **visual proof**.  
9. Writes a **review packet** for human evaluation.  

### 5.2 Required artifacts (under `reviews/<slug>/execution/`)

| Path | Purpose |
|------|---------|
| `EXECUTION_TRANSACTION.json` | Structured record (schema) |
| `EXECUTION_CONTRACT.md` | Human-readable contract |
| `WORKLOG.md` | Chronological run log |
| `CHANGED_FILES.md` | Paths + diffs summary |
| `VALIDATION_RESULTS.md` | Build, test, lint, route |
| `VISUAL_EVIDENCE/` | Screenshots, captures, optional media |
| `HUMAN_REVIEW_PACKET.md` | Single entry point for reviewers |

See [`templates/execution_packet/README.md`](../../templates/execution_packet/README.md).

### 5.3 Required automation steps (order)

1. Validate evidence and planning inputs.  
2. Create **execution transaction** (JSON).  
3. Prepare **isolated branch/worktree**.  
4. Compile **execution contract**.  
5. Run **implementation agent** under contract (or human-driven steps with same contract).  
6. Run **build / test / route** checks.  
7. Collect **visual evidence**.  
8. Write **review packet**.  
9. **Stop** and await **human decision**.  

### 5.4 Initial hard rules

| Rule | Statement |
|------|-----------|
| No implementation without a working branch | Block if isolation cannot be established |
| No UI-affecting output without visual proof | Block promotion |
| No promotion without repo-truth validation | Block promotion |
| No silent exclusions from manifest or contract | Disclose any omission |
| Force/override paths must be disclosed | In transaction and review packet |

---

## 6. Recommendation

**Do not** treat this as “replace the current planner.”

**Do** treat it as:

- **Keep** the current planning stack.  
- **Add** execution transaction + isolated branch lane.  
- **Require** visual proof for UI-affecting work.  
- **Require** repo-truth validation.  
- **Then** let **human review** output before any ratification path.  

That is the intended path from **document-governed intent** to **inspectable implementation**.

---

## Annex A — Gap report (current planning vs required pipeline)

| Dimension | Current planning (`build_agent_kb.py` + `ollama_planning_agent.py`) | Required Phase X lane |
|-----------|----------------------------------------------------------------------|------------------------|
| **Inputs** | YAML manifest + repo files | Same + **transaction** + **target repo/branch** binding |
| **Outputs** | `ARCHITECT_PLAN.md`, `UI_PLAN.md` | Same **plus** `execution/*` artifacts |
| **Isolation** | None (text-only) | **Mandatory** branch or worktree |
| **Traceability** | File paths in prose | **Hashes + JSON** + commit SHAs |
| **Contract** | Implicit in templates | **EXECUTION_CONTRACT.md** + enums |
| **Build/test** | None | **Recorded** in `VALIDATION_RESULTS.md` |
| **Visual proof** | None | **VISUAL_EVIDENCE/** + disclosure rules |
| **Promotion** | Human reads drafts | **Gated** checklist + `HUMAN_REVIEW_PACKET.md` |
| **Automation** | Python + Ollama chat | **Future:** scripts orchestrating git + build + capture |

**Narrowest gap to close first:** **Structured transaction + execution folder layout + contract template** in the **governance repo**, plus a **documented branch/worktree procedure** (Annex D). **Second:** a thin **orchestrator script** in **`ai-os-voice-interface`** (or a small `execution_runner` repo) that enforces branch isolation and runs `npm run build` / tests. **Third:** **visual capture** hooks (Playwright, manual screenshot checklist, or scripted Vite preview).

---

## Annex B — Smallest viable implementation sequence (MVP)

1. **Artifacts only (governance repo)**  
   - Add `templates/execution_packet/` with README + empty `EXECUTION_CONTRACT.md` template sections.  
   - Publish [`execution_transaction.schema.json`](../schemas/execution_transaction.schema.json).  
   - Operators **manually** copy the folder to `reviews/<slug>/execution/` and fill JSON/MD after a local run.

2. **Branch procedure (documented)**  
   - Follow **Annex D** using **git worktree** for `ai-os-voice-interface`.  
   - Record `base_commit_sha` and `head_commit_sha` in `EXECUTION_TRANSACTION.json`.

3. **Minimal validation script (product repo)**  
   - One script: `npm ci` or `npm install`, `npm run build`, `npm test` (if present), exit codes → append to `VALIDATION_RESULTS.md` template.  
   - No LLM required.

4. **Visual proof v0**  
   - Manual screenshots into `VISUAL_EVIDENCE/screenshots/` + short `CAPTURES.md` listing routes.  
   - Optional: `npm run dev` + printed URL + “capture checklist” in `HUMAN_REVIEW_PACKET.md`.

5. **LLM-assisted contract compilation (optional)**  
   - Second Ollama prompt: inputs = `ARCHITECT_PLAN.md` + `UI_PLAN.md` → draft `EXECUTION_CONTRACT.md` **only**; human must **sign** before implementation.

6. **Promotion gate**  
   - Coordinator checklist: all required files exist; hashes match; **no** promotion until human sign-off in packet.

---

## Annex C — Execution contract schema

### C.1 JSON — `EXECUTION_TRANSACTION.json`

Normative JSON Schema: **[`reference/schemas/execution_transaction.schema.json`](../schemas/execution_transaction.schema.json).

### C.2 Markdown — `EXECUTION_CONTRACT.md` (logical sections)

| Section | Required |
|---------|----------|
| Objective | Yes |
| User-visible outcome | Yes |
| In-scope files (glob or path list) | Yes |
| Out-of-scope / forbidden paths | Yes |
| Validation steps (commands) | Yes |
| Visual proof requirements | If UI-affecting |
| Known risks | Yes |
| Stop conditions | Yes |

---

## Annex D — Branch isolation procedure (reference)

**Applies to:** `ai-os-voice-interface` (or any target Git repo). **Prerequisites:** clean working tree on **source branch**, **fetch** remote, **no** uncommitted work on shared branches.

### D.1 Preferred — `git worktree`

1. **Choose paths:** e.g. `../ai-os-voice-interface-exec-<slug>` as worktree.  
2. `cd` to parent of main clone.  
3. `git fetch origin`  
4. `git worktree add -b execution/<slug>/<short-id> ../ai-os-voice-interface-exec-<slug> origin/<source-branch>`  
5. `cd` into worktree; record `git rev-parse HEAD` as **base_commit_sha**.  
6. All implementation and validation **only** in this directory.  
7. On completion: `git rev-parse HEAD` as **head_commit_sha**; push branch or export bundle per team policy.

### D.2 Alternative — branch in same clone

1. `git fetch origin`  
2. `git checkout <source-branch>`  
3. `git pull`  
4. `git checkout -b execution/<slug>/<short-id>`  
5. Record SHAs as above.  
6. **Never** commit to `main` without separate review.

### D.3 Forbidden

- Committing directly to **`main`** or shared release branches **without** PR and review.  
- **Force-push** without disclosure in `EXECUTION_TRANSACTION.json` (`overrides_disclosed: true` + narrative).

---

## Annex E — MVP runner (implemented)

**Location:** [`scripts/run_isolated_execution_demo.py`](../../scripts/run_isolated_execution_demo.py) (Python 3; runner **v0.3.0**; stdlib + PyYAML for manifest label). **Sample outputs:** [`reviews/demo_exec_packet_samples/README.md`](../../reviews/demo_exec_packet_samples/README.md).

**What it does (deterministic):**

1. Requires **`reviews/<slug>/planning/ARCHITECT_PLAN.md`** (draft from **[AIOS-AMD-PLAN-001](AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** phase B or a coordinator copy from the template).
2. Creates **`reviews/<slug>/execution/`** and copies **`EXECUTION_CONTRACT.md`** from [`templates/execution_packet/EXECUTION_CONTRACT_TEMPLATE.md`](../../templates/execution_packet/EXECUTION_CONTRACT_TEMPLATE.md) when missing; copies **`VALIDATION_COMMANDS.example.json`** for reference.
3. Writes **`EXECUTION_TRANSACTION.json`** (**schema 1.2.0**): hashes of architect/UI plans; **`product_repo_path`** (local path, first-class; **`not_applicable`** only for **`--no-git`** — see **`operator_disclosures`**); **`source_repo`** (defaults to that path, or **`--source-repo-url`**); **`created_at` / `updated_at`**; **`validation_started_at` / `validation_completed_at`** when npm runs; **`artifacts`** (canonical index relative to this folder); **`operator_disclosures`** (**`execution_lane_posture`**, **`validation_proof_available`**, **`validation_non_proof_reason`**, **`visual_capture_automated`**); **`failure_stage`** on failure (`git_fetch`, `worktree_creation`, `install`, `build`, `test`, `validation_skipped`, …); **`human_review_status`** (runner seeds **`pending`** — separate from **`promotion_status`**); manifest label from `agent_kb_manifest.yaml` when PyYAML is available.
4. **`--no-git`:** skips product repo; sets `isolation_mode` **`none`**; **`base_commit_sha`** placeholder **`0000000`**; validation section documents skip.
5. **Default (with `--product-repo`):** `git fetch origin <source-branch>`, **`git worktree add`** to a sibling folder `aios-exec-<slug>-<UTC>` under `--worktree-parent` (default: parent of product repo), records **`base_commit_sha`**, runs **`npm ci`** (or **`npm install`** without lockfile) / **`npm run build`** / **`npm test`** unless overridden by **`VALIDATION_COMMANDS.json`** in the execution folder or **`--validation-config`**. Logs go to **`VALIDATION_RESULTS.md`**.
6. Writes **`WORKLOG.md`**, **`CHANGED_FILES.md`** (no product edits by the runner), **`VISUAL_EVIDENCE/CAPTURE_CHECKLIST.md`**, **`VISUAL_EVIDENCE/screenshots/`**, **`HUMAN_REVIEW_PACKET.md`** (navigation + **`artifacts`** table first, then binding/proof callouts).

**What it does not do:** screenshots, browser automation, LLM implementation, autonomous code mutation, amendment edits, or ratification. The runner remains an **execution lane initializer and bounded validation / evidence collector** — not an implementation agent.

**CLI summary:**

| Argument | Purpose |
|----------|---------|
| `--review-slug` | Required. |
| `--product-repo` | Path to implementation repo (required unless `--no-git`). |
| `--source-repo-url` | Optional remote URL / identity for **`source_repo`** (defaults to **`product_repo`** path). |
| `--source-branch` | Default `main`. |
| `--worktree-parent` | Directory for new worktree folder. |
| `--working-branch` | Override auto branch name `execution/<slug>/runner-<UTC>`. |
| `--validation-config` | Path to `VALIDATION_COMMANDS.json`. |
| `--no-git` | Packet + stubs only. |
| `--skip-validation` | Worktree only; no npm commands. |

**Implementation plan (MVP — done):** one script + schema/template tweaks; no separate orchestration service.

---

## Appendix — Agent system prompt

The **operating system prompt** for a future **isolated execution demonstration** agent is maintained in:

**[`prompts/isolated_execution_demonstration_system.md`](../../prompts/isolated_execution_demonstration_system.md)**

It is **not** normative law; it is **operator guidance** for tooling and humans.

---

*End of AIOS-EXEC-DEMO-001 v0.1.3 draft.*
