---
document_id: AIOS-MASTER-IMPL-001
version: 1.2.4
status: draft
category: reference
title: AIOS Master Implementation Program (cross-repo)
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
cross_references:
  - doc_id: AIOS-COUNCIL-BRIEF-001
  - doc_id: AIOS-COUNCIL-BRIEF-002
  - doc_id: AIOS-COUNCIL-BRIEF-003
  - doc_id: AIOS-DEV-PROC-001
  - doc_id: AMD-2026-012
  - doc_id: AIOS-SPEC-009
  - doc_id: AMD-2026-007
  - doc_id: AIOS-SPEC-007
  - doc_id: AIOS-POLICY-INDEX
  - doc_id: AIOS-REF-013
  - doc_id: AIOS-IMPL-LEDGER-001
  - doc_id: AIOS-ADR-001
amendment_history:
  - version: 1.2.4
    date: 2026-04-07
    summary: Cross-reference AIOS-COUNCIL-BRIEF-003 and AIOS-DEV-PROC-001 — development conformance triangulation (governing ratification path).
  - version: 1.2.3
    date: 2026-04-07
    summary: Cross-reference AIOS-COUNCIL-BRIEF-002 — interface implementation control program subject to council before execution approval in product repo.
  - version: 1.2.2
    date: 2026-04-07
    summary: Part 3 gap — SPEC-009 §12.2 predicates in ai-os-voice-interface src/core/compliance (presentation remains interface).
  - version: 1.2.1
    date: 2026-04-07
    summary: Council review brief (AIOS-COUNCIL-BRIEF-001); Part 1 evidence note for ai-os-voice-interface src/core/shell pilot.
  - version: 1.2.0
    date: 2026-04-07
    summary: Correction — removed premature approved-for-execution; council review required before formal execution approval (not amendment ratification).
  - version: 1.1.0
    date: 2026-04-07
    summary: Superseded — incorrectly marked approved for execution without council review.
  - version: 1.0.0
    date: 2026-04-07
    summary: Initial master program — layer model, inventory, child reclassification, phased backlog.
---

# AIOS Master Implementation Program (cross-repo)

**Normative law:** `aios-governing-docs` only.  
**This document:** non-normative **master execution program** — defines architectural layers, phased order, backlog, evidence, and child workstreams. It does **not** amend specifications.

## Council review gate (required before execution approval)

| Field | Value |
|-------|--------|
| **Program document status** | **`draft`** — **not** approved for execution until **council review** completes. |
| **Execution approval** | **Distinct from amendment ratification** — but still **requires council** (or delegated body) **review and explicit approval** before the program is treated as **authorized to run** as the cross-repo authority. |
| **Premature approval** | A prior **`approved_for_execution`** label **without council review** was **rescinded** (v1.2.0). |
| **Draft artifacts (for review)** | [**Implementation ledger**](AIOS-IMPLEMENTATION-LEDGER.md) (**AIOS-IMPL-LEDGER-001**); [**ADR-001: Core vs interface boundaries**](ADR-001-core-shell-vs-interface-boundaries.md) (**AIOS-ADR-001**, **proposed**). |
| **Interface child program gate** | [**AIOS-COUNCIL-BRIEF-002**](COUNCIL-REVIEW-BRIEF-AIOS-INTERFACE-CONTROL-001.md) — committee **approval** of **AIOS-IMPL-CONTROL-001** before the product repo treats that plan as **execution-approved** (operational spine; failure mode if bypassed). |
| **Development conformance gate** | [**AIOS-COUNCIL-BRIEF-003**](COUNCIL-REVIEW-BRIEF-AIOS-DEV-PROC-001.md) + [**AIOS-DEV-PROC-001**](AIOS-DEVELOPMENT-CONFORMANCE-PROCESS.md) — **peer review** (`reviews/aios_dev_conformance_process/`) then **council ratification** of **development triangulation** (not optional for **ratified** process law). |

**Downstream child (repo-local, not authoritative for scope):**  
`ai-os-voice-interface/docs/implementation/AIOS-IMPLEMENTATION-CONTROL-PROGRAM.md` (**AIOS-IMPL-CONTROL-001**) — **see** [**AIOS-COUNCIL-BRIEF-002**](COUNCIL-REVIEW-BRIEF-AIOS-INTERFACE-CONTROL-001.md).

**Companion:** `reference/implementation/AIOS-IMPLEMENTATION-RUNWAY-POINTER.md` (**AIOS-REF-013**) — pointer to product memos; **this master program** supersedes those memos for **cross-repo** sequencing authority.

---

## Mis-scoping assessment (required correction)

The repo-local control document correctly traces tasks to **AMD-2026-012**, **AIOS-SPEC-009**, and **AIOS-SPEC-007**, but it implicitly treats **`ai-os-voice-interface` as the center of gravity** for shell law. That is **mis-scoped** relative to the founder’s architecture:

| Issue | Why it matters |
|-------|----------------|
| **Shell session authority**, **outcome family (§7)**, **PolicyRecord-aligned disclosure**, and **integration control-plane** semantics are **kernel / control-plane** responsibilities under ratified law — not “UI details.” |
| Implementing them **only** inside a React application risks **conflating** product chrome with **runtime truth** and makes **tenant** and **second interface** consumers impossible without fork or copy-paste. |
| **Google Workspace** MCP and OAuth paths are a **subordinate tool plane**; they must not become the place where **fallback authority** or **primary outcome** is defined. |

**What stays valid:** The child document’s backlog items are **useful** as **interface-layer tasks** *once* the core contracts exist, or as **provisional** implementations **explicitly labeled** as embedded in the interface repo until extracted.

**What must change:** **Master progress** is measured by **core shell / kernel / control-plane** solidity first; **interface** conformance is **downstream**. Repo-local “Sprint 2” (e.g. disclosure wiring) must **not** be treated as satisfying the overall program until core ownership is clear.

---

# PART 1 — Layer model

Four layers; each has **decisions that belong** and **decisions that do not**.

### 1 — Governing docs layer

| | |
|--|--|
| **Repository** | `aios-governing-docs` |
| **Role** | **Normative source of truth only** — law, specs, amendments, policy index, ratification artifacts. |
| **Decisions that belong** | Definitions of Shell, intent, PolicyRecord, POL-* IDs, integration routing **rules**, conformance language. |
| **Decisions that do not** | Application code, tenant business rules, MCP server vendor secrets, UI pixel choices. |

### 2 — Core shell / kernel / control-plane layer

| | |
|--|--|
| **Role** | **Runtime truth** for session authority, shell law, voice-first entry, identity as presented, fallback selection within the §7 family, transparency minima, permissions/readiness, **intent resolution → routing**, **outcome ↔ PolicyRecord / SessionContext mapping**, **tool subordination** at the policy boundary. |
| **Decisions that belong** | Contracts and services that **any** interface (web, voice, future device) **consumes**; deterministic mapping from governance objects to “what the session **is**.” |
| **Decisions that do not** | Branding, React components, CSS, marketing copy; **tenant-specific** workflows; **direct** MCP tool strings exposed to untrusted layers. |
| **Evidence (current)** | **Partial:** `ai-os-voice-interface` now has **`src/core/shell/`** for law-aligned modules (outcomes, session entry) with thin **`src/shell/`** re-exports — **pilot** toward **AIOS-ADR-001**; ICP, intent, compliance still **to** migrate. **google-workspace-mcp** = adapter/tool plane. Full **package** extraction remains optional. |

### 3 — AI OS interface layer

| | |
|--|--|
| **Repository** | `ai-os-voice-interface` (primary consumer in scope) |
| **Role** | **Product surface** that **renders** shell/kernel/control-plane state: voice/chat chrome, idle orientation, disclosure **presentation**, Workspace panels **after** routing. |
| **Decisions that belong** | Layout, accessibility, component structure, client-side persistence of **presentation** flags, mapping **core** state → UI. |
| **Decisions that do not** | **Defining** the §7 outcome family, PolicyRecord fields, or ICP bypass rules **without** a core contract; inventing **shell law** in components. |

### 4 — Tenant / workspace layer

| | |
|--|--|
| **Role** | **Downstream** tenant-specific skills, configuration, optional branding, business workflows, org policies **within** law. |
| **Decisions that belong** | Tenant config, allowed integrations, feature flags **subordinate** to Shell and control plane. |
| **Decisions that do not** | Redefining Shell authority, default entry, or global outcome taxonomy; **promoting** Workspace above Shell. |

---

# PART 2 — Governing source inventory

Paths are relative to `aios-governing-docs` unless noted. **Ratified** / **draft** reflects **file front matter** where checked; **policy index** may reference versions that differ — **reconcile in governing layer** (implementation risk: **B-GOV-001**).

| Doc ID | Title | Status | Law it creates | Primary layer(s) governed | Repos affected | Significance |
|--------|--------|--------|----------------|----------------------------|----------------|--------------|
| **AMD-2026-012** | Shell Authority and Voice-First Entry (`amendments/AMD-2026-012.md`) | **ratified** v1.0.0 | Single governed entry; voice-first; new/returning; §7 outcomes; subordinate tools; §4.4 fallback via §7 only | **Core** (authority, outcomes), **Interface** (presentation), **Governing** | Interface (embedded core), MCP (subordinate) | **5** |
| **AIOS-SPEC-009** | Intent Primitive and Execution Model (`specifications/IntentPrimitiveAndExecutionModel.md`) | **ratified** v0.5.5 | Intent lifecycle, shell vs domain, execution gates, **§12** disclosure | **Core** (dominant), **Interface** | Interface, MCP adapter | **5** |
| **AIOS-SPEC-002** | PolicyRecord Specification (`specifications/PolicyRecord.md`) | **ratified** v1.0.0 | Execution readiness, policy records | **Core** | Core + all consumers | **5** |
| **AIOS-SPEC-007** | Google Workspace Integration Governance (`specifications/GoogleWorkspaceIntegrationGovernance.md`) | **draft** in YAML | Intent → router → ICP → MCP; no bypass | **Core** (routing + ICP), **Tool plane** (MCP) | Interface, `google-workspace-mcp` | **5** (binding in program until YAML reconciled) |
| **AMD-2026-007** | Intent primitive, shell affordances, POL-* (`amendments/AMD-2026-007.md`) | **draft** in file; **AIOS-POLICY-INDEX** cites **POL-*** from §5 | POL-INTENT-*, POL-SHELL-*, primary vs operator | **Core** + **Interface** | Interface | **4** |
| **AIOS-POLICY-INDEX** | Policy Identifier Index (`reference/AIOS_POLICY_INDEX.md`) | **ratified** v1.2.0 | Registers POL-* IDs | **Governing** (registry) | All implementation | **4** |
| **AIOS-SPEC-006** | UI Component Registry Standard (governed path in repo) | **ratified** (verify in registry) | Shell vs domain UI registration | **Interface** + **Core** (affordance contracts) | Interface | **3** |
| **AIOS-SPEC-008** | Intent Discovery and Onboarding (cross-ref from SPEC-009) | per registry | Maps discovery UX to intent | **Interface** (heavy), **Core** (gates) | Interface | **3** |
| **AMD-2026-010** | Kernel Engineer / shadow lane | **ratified** (per index) | Non-blocking kernel review process | **Process** (not product law) | Optional CI/tooling | **2** |
| **AMD-2026-005** | Workspace model & governed surfaces (if referenced by SPEC-007) | per file | Integration surface rules | **Core** / **Tool** | Interface, MCP | **3** |
| **AIOS-REF-013** | Implementation runway pointer | **draft** | Discovery only | — | — | **1** |

---

# PART 3 — Current-state implementation map

Evidence: **repos in workspace** (`ai-os-voice-interface`, `aios-governing-docs`, `google-workspace-mcp`). Status: **implemented** | **partial** | **not implemented** | **wrong layer** | **unclear**.

| Source | Topic | Status | Evidence / notes |
|--------|--------|--------|-------------------|
| **AMD-2026-012** §4–§7 authority & outcomes | Session authority as **runtime truth** distinct from UI | **partial** + **wrong layer risk** | Outcome types and session classification implemented **in interface repo** (`shellPrimaryOutcome.ts`, `sessionEntryClassification.ts`) without a **separate core package** — correct **semantics**, **mis-scoped physically** for multi-consumer future. |
| **AIOS-SPEC-009** §12 | Primary disclosure | **partial** | §12.2 **predicates** in **`src/core/compliance/spec009DisclosurePredicates.ts`**; **presentation** in `src/compliance/spec009PrimaryDisclosure.ts` + `ShellIdentityBar`; **`resolvedIntentRequiresLocalModel`** policy wiring still **open** (child BL-004 / **MBL-006**). |
| **AIOS-SPEC-002** | PolicyRecord in live session | **unclear / partial** | Interface predicates readiness; **full** PolicyRecord object may not flow end-to-end — **needs evidence** audit (**MBL-008**). |
| **AIOS-SPEC-007** §2 | ICP-only routing | **partial** | `integrationControlPlane.ts`, `callWorkspaceMcpAdapter` guard tests — **adapter** in MCP repo must match (**MBL-012**). |
| **AMD-2026-007** POL-* | Named policies in code | **partial** | Comments/tests reference POL-SHELL / interim authority; **draft** file vs **index** — **governing reconciliation** (**B-GOV-001**). |
| **Governance-manager** | End-user runtime | **not present in interface `src/`** | Archived — **aligned**. |

**Work started in `ai-os-voice-interface` that should live in core shell/kernel/control-plane (or a shared package) per architecture:**

| Current location | Should be |
|------------------|-----------|
| `src/shell/shellAuthority.ts`, `shellBootstrap.ts`, `ShellStateContext.tsx` | **Core** contracts + platform bindings; UI provider thin in interface. |
| `src/shell/shellPrimaryOutcome.ts` | **Core** — outcome taxonomy and mapping to SessionContext/PolicyRecord (**not** only React). |
| `src/shell/sessionEntryClassification.ts` | **Core** model + **interface** storage driver (browser/localStorage is one adapter). |
| `src/workspace/integrationControlPlane.ts` | **Core** control-plane entry (Workspace lane). |
| `src/compliance/spec009PrimaryDisclosure.ts` | Split: **predicates** → core; **strings/layout** → interface. |

---

# PART 4 — Existing work reclassification (child control document)

**Source reviewed:** `ai-os-voice-interface/docs/implementation/AIOS-IMPLEMENTATION-CONTROL-PROGRAM.md` (AIOS-IMPL-CONTROL-001).

### Phases P0–P5 (child)

| Child phase | Verdict | Master mapping |
|-------------|---------|----------------|
| **P0** Program control | **Keep as child** | Maps to **Master Phase 0**; child doc is **not** the program authority — **relabel** as “interface child” only. |
| **P1** Shell session semantics | **Mixed** | **Core-first** (Master Phase 1–3); child P1 items are **subtasks** of **MBL-001–MBL-004**, not standalone “spine complete.” |
| **P2** Transparency + identity | **Core-heavy** | Master Phase 2; interface wiring is **Phase 4** surface. |
| **P3** Workspace conformance | **Tool + core** | Master Phase 5 after core routing stable. |
| **P4–P5** | **Keep** | Maps to Master **6–7** / expansion gates. |

### Backlog items BL-001 — BL-006

| ID | Title | Classification | Notes |
|----|--------|----------------|-------|
| **BL-001** | Session entry classification | **Core model** + **Interface** implementation (browser persistence + copy) | **Keep as child** under **MBL-002**; **elevate** contract to core package when created. |
| **BL-002** | Shell primary outcome model | **Core** (canonical) — current file is **provisional in wrong repo** | **Reclassify:** **MBL-003** owns semantics; interface **consumes**. Not discarded. |
| **BL-003** | §8.4 word-budget test | **Interface** | **Keep as child**; depends on **core** copy contract optional. |
| **BL-004** | `resolvedIntentRequiresLocalModel` wiring | **Core** execution policy + **Interface** bar | **MBL-006**; child BL-004 = interface portion. |
| **BL-005** | Workspace hub subordination | **Interface** + **conformance** | **MBL-010**; ensure hub never default entry. |
| **BL-006** | Fallback audit | **Core** routing/guards + **Interface** error UX | **MBL-005** / **MBL-011**. |

### Sprints 1–3 (child)

| Sprint | Verdict | Master note |
|--------|---------|-------------|
| **Sprint 1** (BL-001/002) | **Partially mis-scoped** — treated spine as done for interface repo | **Reclassify** as **pilot** implementation of **MBL-002–MBL-003** (core-led); **freeze** claiming “shell law complete.” |
| **Sprint 2** (BL-004, BL-003) | **Interface-biased order** | **MBL-006** (policy wiring) should follow **MBL-004** (core disclosure predicates) where possible — **do not** run as default “next” without master alignment. |
| **Sprint 3** (BL-005/006) | **Acceptable** as **workspace/tool** track | Belongs under **Master Phase 5–6** after Phases 1–4 exit criteria defined. |

---

# PART 5 — Master phased backlog

| Phase | Objective | Why this order | Dependencies | Layers / repos | Exit criteria |
|-------|-----------|----------------|--------------|----------------|---------------|
| **0** | Program governance: this document, ledger, anti-drift, child links | Without it, repos confuse authority | None | Governing + all | **Council** approves program for execution; ledger (**AIOS-IMPL-LEDGER-001**) + proposed **AIOS-ADR-001**; child docs reference **AIOS-MASTER-IMPL-001** |
| **1** | **Core** authority model: what “Shell” and “session” mean in **code contracts** (packages/modules), interim vs future control plane | Law must compile to **one** runtime truth | Phase 0 | Core (extract or package from interface), Interface consumes | Written API/types for session mode, elevation, entry classification **interfaces** |
| **2** | Session identity, fallback, transparency, permissions **predicates** (SPEC-009 §12, SPEC-002) | Disclosure must be **policy-backed**, not string-only | Phase 1 | Core + Interface | Predicates unit-tested in **core**; UI only binds |
| **3** | Outcome family **↔** PolicyRecord / SessionContext mapping (**AMD-2026-012 §7**) | Stops UI-only outcomes | Phase 1–2 | Core | Mapping table + tests; **no** primary outcome without backing field path |
| **4** | **Interface** conformance: React app uses **only** core contracts | Downstream of truth | Phase 1–3 | `ai-os-voice-interface` | No ad hoc shell law in components; conformance checklist green |
| **5** | Tool/skill subordination; Workspace **positioning**; ICP + MCP alignment (**SPEC-007**) | Tools after Shell stable | Phase 3–4 | Core + MCP + Interface | ICP-only; hub not default entry |
| **6** | Tenant/workspace alignment | Customization without authority drift | Phase 5 | Tenant configs / future repos | No tenant redefines Shell |
| **7** | Conformance verification, probes, archive cleanup | Prove end-to-end | Phase 1–6 | All | Trace matrix + archived legacy quarantined |

---

# PART 6 — Backlog items (master)

**Status:** `open` | `in_progress` | `done` | `blocked` | `deferred`

| ID | Title | Governing source(s) | Layer | Repo(s) | Objective | Why it exists | Depends on | Acceptance criteria | Evidence | Status |
|----|-------|----------------------|-------|---------|-----------|---------------|------------|---------------------|----------|--------|
| **MBL-000** | Adopt master program + freeze interface-as-center | AIOS-MASTER-IMPL-001 | Governing / program | All | Single authority for sequencing | Founder scope correction | — | **Council** approves master program + ledger for execution; child docs cite master | [**AIOS-IMPL-LEDGER-001**](AIOS-IMPLEMENTATION-LEDGER.md) draft | **pending_council** |
| **MBL-001** | Define **core** module boundaries (package or repo) for shell + control plane | AMD-2026-012, AIOS-SPEC-009 | Core | Interface (extract), future `aios-shell-core` or equivalent | Physical separation of law vs chrome | Prevents perpetual UI-centric shell | MBL-000 | **AIOS-ADR-001** **accepted** after council; CI/import enforcement = follow-up in repos | [**AIOS-ADR-001**](ADR-001-core-shell-vs-interface-boundaries.md) **proposed** | **open** (ADR pending acceptance) |
| **MBL-002** | Session entry classification **contract** (new/returning) | AMD-2026-012 §5 | Core | Core + Interface | Portable model; storage = adapter | First classification step is law | MBL-001 | Interface uses **only** core type + adapter | Tests in core | **partial** (interface pilot exists — **must** map to MBL-001) |
| **MBL-003** | §7 outcome family **canonical** model + mapping | AMD-2026-012 §7; AIOS-SPEC-009 §12 | Core | Core | Outcomes not UI-only | §7 normative mapping | MBL-001 | Mapping doc + tests; SessionContext/PolicyRecord linkage plan | Test output, trace table | **partial** |
| **MBL-004** | Disclosure **predicates** (SPEC-009 §12.2) in core | AIOS-SPEC-009, AIOS-SPEC-002 | Core | Core | Readiness is policy-backed | Stops inference in components | MBL-001 | Predicate API stable; UI imports results | `src/core/compliance/spec009DisclosurePredicates.ts` + tests | **partial** (predicates migrated; PolicyRecord object path still **MBL-008**) |
| **MBL-005** | Fallback routing audit (**§4.4**) | AMD-2026-012 §4.4, §7 | Core | Core + Interface | No independent fallbacks | Agent/tool error paths reviewed | MBL-003 | Documented routing; no silent persona swap | Trace + test | **open** |
| **MBL-006** | Execution policy → `requiresLocalModel` (or equivalent) **wiring** | AIOS-SPEC-009 §12.2 | Core + Interface | Interface + core | Disclosure matches policy | Child BL-004 | MBL-004 | Bar shows line iff policy says | Component test / trace | **open** |
| **MBL-007** | §8.4 presentation budgets (optional automated lint) | AMD-2026-012 §8.4 | Interface | `ai-os-voice-interface` | Enforce interim copy limits | Cosmetic law | MBL-004 (soft) | Test on idle copy | CI test | **open** |
| **MBL-008** | PolicyRecord **presence** audit in live paths | AIOS-SPEC-002 | Core | Core | Readiness fields real | Disclosure integrity | MBL-004 | Gap report or implementation plan | Audit doc | **open** |
| **MBL-009** | Governing reconciliation: AMD-2026-007 vs POL-INDEX vs file YAML | Governing process | Governing | `aios-governing-docs` | Single source for POL-* | Policy traceability | — | Tracker closed when YAML/index aligned | [**MBL-009 tracker**](MBL-009-tracker-amd-2026-007-policy-index.md) | **open** (parallel) |
| **MBL-010** | Workspace hub subordination | AMD-2026-012 §9; AIOS-SPEC-007 §2 | Interface + Tool | Interface, MCP | Hub never default Shell | Child BL-005 | MBL-001 | Manual + routing trace | Conformance note | **open** |
| **MBL-011** | MCP adapter parity with ICP | AIOS-SPEC-007 | Tool plane | `google-workspace-mcp` | Server obeys scope intent model | No raw tool escape | MBL-001 | Contract tests / checklist | Test logs | **open** |
| **MBL-012** | Tenant boundary review (no Shell redefinition) | AMD-2026-012, tenant policy | Tenant | TBD | Config only | Prevents future drift | Phase 5–6 | Written rules for tenant packs | Doc | **deferred** |

**Risk if skipped (summary):** Without **MBL-001–MBL-004**, the interface repo will continue to **embody** shell law **implicitly**, causing **fork drift** and **non-portable** tenant/interfaces.

---

# PART 7 — Anti-drift controls

| Control | Rule |
|---------|------|
| **Council gate** | **No** **`approved_for_execution`** (or equivalent) without **documented council review** of this program and supporting artifacts (ledger, ADR). |
| **Law citation** | Every master backlog item lists **governing source(s)**; child tasks must map to an **MBL-*** or label **non-binding experiment**. |
| **No interface-only shell law** | Components **must not** define outcome taxonomy, fallback policy, or ICP rules — **consume** core. |
| **No tenant shell law** | Tenant/workspace layers **must not** redefine Shell authority or §7 outcomes. |
| **Governance-manager** | **Not** reintroduced to end-user runtime (archive-only). |
| **Tool hierarchy** | Skills/tools **subordinate** — no Workspace-first default entry. |
| **Repo-local ≠ master** | `AIOS-IMPL-CONTROL-001` progress **does not** count as master completion unless **mapped** to **MBL-*** items. |
| **Child workstreams** | Each child document **must** state: *Child of **AIOS-MASTER-IMPL-001**; not authoritative for cross-repo scope.* |

---

# PART 8 — Child workstreams

| Workstream | Owner (suggested) | Document / artifact | Role |
|------------|-------------------|---------------------|------|
| **Core shell / kernel / control-plane** | Platform engineering | ADR + repo/package under org | Contracts, ICP, outcomes, disclosure predicates |
| **AI OS interface** | Product UI | `AIOS-IMPL-CONTROL-001` (updated) | Chrome, voice UX, consumes core |
| **Tenant / workspace** | Customer / solutions | TBD per tenant | Configuration, skills, **no** shell redefinition |
| **Governance implementation verification** | Council / tech lead | `aios-governing-docs` issues | SPEC/AMD YAML reconciliation (**MBL-009**), registry |

---

# PART 9 — First three master execution sprints

### Master Sprint 1 — Core boundaries + contracts freeze

| Field | Content |
|-------|---------|
| **Objective** | Establish **where** shell/kernel/control-plane code **lives** and **import rules**; freeze “interface as owner of law.” |
| **Work items** | **MBL-000**, **MBL-001**, **MBL-009** (open governing issue if needed) |
| **Layer / repo** | Core program + `aios-governing-docs` |
| **Acceptance** | ADR (or equivalent) merged; **MBL-002–MBL-003** contract ownership clear; child doc header updated to reference master |
| **Evidence** | ADR PDF/markdown; PR links |
| **Done means** | Team agrees **core extraction or modularization path**; no ambiguity that interface sprint is **downstream** |

### Master Sprint 2 — Predicates + PolicyRecord path

| Field | Content |
|-------|---------|
| **Objective** | Implement or formalize **MBL-004** and **MBL-008** so disclosure is **not** component-inferred. |
| **Work items** | **MBL-004**, **MBL-008**, start **MBL-006** |
| **Layer / repo** | Core (+ interface only as consumer) |
| **Acceptance** | Predicate API + gap report on PolicyRecord fields |
| **Evidence** | Core unit tests; short audit markdown in governing or core repo |
| **Done means** | **MBL-006** can be completed without inventing policy in React |

### Master Sprint 3 — Outcome mapping + fallback audit

| Field | Content |
|-------|---------|
| **Objective** | Complete **MBL-003** mapping to SessionContext/PolicyRecord; **MBL-005** audit. |
| **Work items** | **MBL-003**, **MBL-005** |
| **Layer / repo** | Core + interface error paths |
| **Acceptance** | Trace table: every user-visible primary outcome → backing field path **or** explicit gap with plan |
| **Evidence** | Table + tests |
| **Done means** | **AMD-2026-012 §7** “not UI-only” is **demonstrable** in core |

---

# PART 10 — Recommended immediate action

| Action | Detail |
|--------|--------|
| **Council review** | **First** — review **AIOS-MASTER-IMPL-001**, [**AIOS-IMPL-LEDGER-001**](AIOS-IMPLEMENTATION-LEDGER.md), and [**AIOS-ADR-001**](ADR-001-core-shell-vs-interface-boundaries.md); then issue **explicit execution approval** (and ADR **accepted** status) if appropriate. **Not** amendment ratification — still a **governance gate**. |
| **Pending** | **MBL-000** / **MBL-001** remain **open** until that review; draft artifacts exist for **discussion only**. |
| **Parallel** | **MBL-009** — [**tracker**](MBL-009-tracker-amd-2026-007-policy-index.md) (not Sprint 1 product blocker). |
| **Freeze / hold** | **Interface** work stays **child** status until **core** predicates (**MBL-004**) land per **accepted** ADR. **Do not** promote **BL-004**-style wiring to **mainline**. |
| **After approval** | **MBL-002–MBL-004** (contracts, outcomes, disclosure predicates in **core**) + import boundaries in `ai-os-voice-interface`. |
| **Do not** | Harden shell semantics **only** in React by default; **do not** treat child backlog completion as **master** completion; **do not** label the program **approved for execution** without **council review**. |

---

## Cross-reference: child document

`ai-os-voice-interface/docs/implementation/AIOS-IMPLEMENTATION-CONTROL-PROGRAM.md` **must** retain a clear **child-of-master** statement under **Purpose** (updated with **AIOS-MASTER-IMPL-001**).

## Cross-reference: council review

[**COUNCIL-REVIEW-BRIEF-AIOS-MASTER-IMPL-001.md**](COUNCIL-REVIEW-BRIEF-AIOS-MASTER-IMPL-001.md) (**AIOS-COUNCIL-BRIEF-001**) — one-page brief for scheduling **council** approval of execution + **ADR-001** acceptance.

---

*End of AIOS Master Implementation Program v1.2.2.*
