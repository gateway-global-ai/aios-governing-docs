---
document_id: AIOS-SPEC-007
version: 1.0.1
status: ratified
category: specification
title: Google Workspace Integration Governance
author: Gateway Global AIOS
created: 2026-04-03
last_updated: 2026-04-09
reviewers: []
ratification_target: "2026-04-08"
supersedes: null
cross_references:
  - doc_id: AMD-2026-006-RATIFICATION-MOTION
    title: Ratification motion — AMD-2026-006 / AIOS-SPEC-007
  - doc_id: AMD-2026-006
    title: Google Workspace Governed Integration Plane
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
  - doc_id: AIOS-SPEC-010
    title: Execution Scope Envelope
  - doc_id: AIOS-SPEC-006
    title: UI Component Registry Standard
  - doc_id: AMD-2026-009
    title: Intent-Scoped Web Retrieval and Governed Website Review (ratified 1.0.0)
  - doc_id: AMD-2026-009-RATIFICATION-MOTION
    title: Ratification motion — AMD-2026-009
  - path: WORKSPACE.md
    note: Informative operator and capability notes (repository root)
amendment_history:
  - version: 1.0.1
    date: 2026-04-09
    summary: AMD-2026-009 ratified 1.0.0 per AMD-2026-009-RATIFICATION-MOTION v1.0.0; §3 alignment reaffirmed with ratified amendment and ADD-001 1.0.0.
  - version: 1.0.0
    date: 2026-04-08
    summary: Ratified per AMD-2026-006-RATIFICATION-MOTION v1.0.0; substantive basis peer-reviewed as v0.2.0 (Round 2 PASS); frozen as ratified line 1.0.0.
  - version: 0.2.0
    date: 2026-04-08
    summary: Normative envelope §5, control plane outcomes §6, canvas routing §7, execution scope §8; Round 2 candidate after AMD-2026-006 Phase E.
  - version: 0.1.1
    date: 2026-04-03
    summary: §3 retrieval backends — PSE optional; policy-registered alternatives per AMD-2026-009-ADD-001.
  - version: 0.1.0
    date: 2026-04-03
    summary: Initial repository copy; routing model; web search / PSE alignment with AMD-2026-009 §10.
---

# AIOS-SPEC-007 — Google Workspace Integration Governance

## 0. Status

| Field | Value |
|-------|--------|
| **Status** | `ratified` (**1.0.1**) |
| **Framing** | Normative requirements for how the AI OS **voice / agent layer** integrates with **Google Workspace** via **MCP** and governed **intent** routing. Informative deployment and env detail **MAY** live in **`WORKSPACE.md`** (repository root); this spec states **SHALL** / **MUST** rules products **MUST** satisfy to claim compliance. |

**Non-normative — legal:** Commercial terms, liability allocation, and enforceability between parties **MAY** be addressed in **MPOA**, council instruments, or operator agreements. This specification defines **technical governance** and **integration behavior**, not standalone contractual obligations.

## 1. Purpose

1. Ensure **intent** is the **only** governed entry point for Workspace capability execution from the product UI — not ad hoc tool strings or direct MCP exposure to untrusted layers.
2. Align the **integration control plane** and **MCP adapter** with **AIOS-SPEC-009** (intent primitive, execution, audit expectations) and **AIOS-SPEC-010** when **execution scope** is present on the routing envelope.
3. Bind **web retrieval** to **policy** and **[AMD-2026-009](../amendments/AMD-2026-009.md)** (including **[ADD-001](../amendments/AMD-2026-009-ADD-001-retrieval-backend-neutrality.md)** where ratified) — **not** unconstrained public browsing. **Programmable Search Engine / Custom Search** is **one** permitted backend; **others** **SHALL** be **policy-registered**.

## 2. Normative routing model

### 2.1 Mandatory integration chain

1. The **browser or client** **SHALL** invoke Workspace capabilities **only** through the product’s **Workspace Intent Router → Integration Control Plane → MCP Adapter** (or equivalent names); it **MUST NOT** call Google Workspace MCP **tools** directly with arbitrary method names bypassing **intent** resolution and **scope class** mapping.
2. **Intent** identifiers **SHALL** conform to **AIOS-SPEC-009** and the product’s **Phase 1** (or successor) **workspace.\*** registry model.
3. **Layer 2** operational intents **SHALL** map to **exactly one** **Layer 1** **workspace.google.\*** **scope class** per the product’s governed mapping table (e.g. `workspace.google.read`, `workspace.google.write`, `workspace.google.identity`, `workspace.google.search`). **Implementations** **MUST** reject ambiguous or many-to-one mappings at build or startup where asserted.
4. **OAuth** access tokens and MCP **transport** session handling **SHALL** follow the security model described in **`WORKSPACE.md`** (informative) for this repository’s implementation; **secrets** for MCP hosts **SHALL NOT** be embedded in client bundles (e.g. no **`VITE_*`** PSE API keys for production claims).

### 2.2 Routing envelope and control plane

Before any MCP **`tools/call`**, a **Workspace routing envelope** (**§5**) **SHALL** be assembled and validated. The **Integration Control Plane** **SHALL** return **deterministic** failure outcomes (**§6**) when validation, policy, scope, or adapter calls fail — not unstructured errors alone.

### 2.3 MCP tool resolution

The **agent or voice layer** **MUST NOT** bind to raw MCP tool names. **Intent → MCP tool name and arguments** **SHALL** be resolved in one governed module (e.g. an **mcp intent tool map**), consistent with **§5**.

## 3. Web search and external retrieval (PSE)

This section incorporates **[AMD-2026-009](../amendments/AMD-2026-009.md)** (**`ratified` `1.0.0`**) and, where applicable, **[ADD-001](../amendments/AMD-2026-009-ADD-001-retrieval-backend-neutrality.md)** (**`ratified` `1.0.0`**) at the **integration** layer.

1. Workspace MCP tools that invoke **Programmable Search Engine (PSE)** / **Custom Search JSON API** (e.g. **`search_custom`**) **SHALL** be **policy-scoped**: the effective **search scope class** (AMD-2026-009 §4) **SHALL** be determined by **intent → capability → policy**, not by ad hoc client parameters alone.
2. Implementations **SHALL** reference **POL-WEB-SCOPE-001** (or successor in the organization policy register) for which **search scope classes** are allowed per tenant or intent.
3. The product **SHALL NOT** treat **public web search** as an unconstrained default; **`web.search.broad_public`** **SHALL** follow AMD-2026-009 §4 trigger rules (explicit intent classification, user/operator confirmation, or policy-defined escalation).
4. **PSE credentials** (**`GOOGLE_PSE_*`**, engine id, API keys) **SHALL** reside on the **MCP server** environment; they **MUST NOT** appear in browser bundles or **`VITE_*`** client env for production deployments claiming this spec.

## 4. Relationship to other documents

| Document | Role |
|----------|------|
| **AIOS-SPEC-009** | Intent primitive, execution plan, proposal/approval — **MUST** be enforced at integration boundaries; primary-surface disclosure presentation **SHALL** align with **§12** where applicable. |
| **AIOS-SPEC-010** | **Execution Scope Envelope** — when **`execution_scope`** is set on the routing envelope, the control plane **SHALL** validate scope **before** adapter dispatch (**§8**). |
| **AIOS-SPEC-006** | **UI Component Registry** — Workspace **canvas view** identifiers and shell boundaries **SHALL** be registered per product registry rules (**§7**). |
| **AMD-2026-009** | Bounded external knowledge acquisition, review modes, audit minimums. |
| **WORKSPACE.md** | Informative: operator setup, CORS, MCP URLs, troubleshooting. |

## 5. Workspace routing envelope (normative)

Products claiming compliance **SHALL** use a **typed routing envelope** at the Integration Control Plane boundary with **at least** the following fields. Field names **MAY** match the reference implementation (`WorkspaceRoutingEnvelope` in product **`src/workspace/types.ts`**); semantics below are **normative**.

| Field | Requirement | Notes |
|-------|-------------|--------|
| **`intent`** | **SHALL** be present | **Layer 2** `workspace.\*` id validated against the governed intent set. |
| **`actor_type`** | **SHALL** be present | Identifies the acting principal class for policy. |
| **`tenant_id`** | **SHALL** be present | Tenant isolation key. |
| **`user_binding`** | **SHALL** be present | Stable user/session binding for audit. |
| **`execution_mode`** | **SHALL** be present | One of `observe` \| `prepare` \| `execute` \| `automate` (or product-defined superset **if** mapped). |
| **`policy_context.scope_class`** | **SHALL** be present | **MUST** equal the **single** scope class resolved from **`intent`**. |
| **`policy_context.requires_confirmation`** | **MAY** be present | When true, control plane **SHALL** enforce confirmation gates per product policy. |
| **`resource_ref`** | **MAY** be present | Message/thread/calendar identifiers for read/write tools as required by **`intent`**. |
| **`session_id`** | **MAY** be present | Correlation for audit. |
| **`query`** | **MAY** be present | **SHALL** be used only where **`intent`** defines query semantics (e.g. mail search). |
| **`execution_scope`** | **MAY** be present | **If** present, **AIOS-SPEC-010** validation **SHALL** run before MCP dispatch (**§8**). |
| **`calendar_time_range`** | **MAY** be required per **`intent`** | **SHALL** be present when **`intent`** is **`workspace.calendar.events.list`** (or equivalent) — RFC3339 window. |
| **`contacts_page_token`** | **MAY** be present | Pagination for contacts list intents when supported. |

**SHALL NOT:** Ad hoc parallel fields that bypass **`intent`** or **`policy_context.scope_class`** for the same operation.

## 6. Integration control plane — deterministic outcomes

When the Integration Control Plane returns **failure**, products **SHALL** classify the result using **at least** one of the following **codes** (string identifiers), in addition to a human-readable **message** and audit correlation where available:

| Code | Meaning (normative minimum) |
|------|-----------------------------|
| **`policy_denied`** | Policy engine denied the operation. |
| **`invalid_intent`** | Intent shape or registry validation failed. |
| **`adapter_error`** | MCP adapter or transport failure (sub-class **MAY** be surfaced as `adapterCode`). |
| **`not_configured`** | Required host, URL, or capability missing. |
| **`auth_required`** | Valid OAuth/token not available. |
| **`scope_denied`** | Execution scope (**§8**) or scope-class check failed. |

**Success** responses **SHALL** include auditable correlation (e.g. **`auditId`**) where the product implements audit.

## 7. Canvas surfaces and intent routing (AIOS-SPEC-006)

1. Workspace **UI** **SHALL** register **canvas view** identifiers with the product’s **UI Component Registry** per **AIOS-SPEC-006** (footer, load states, exit contracts as required by that spec).
2. **Intent → canvas view** mapping **SHALL** be deterministic in the **Workspace Intent Router**. **Representative** mappings **SHALL** include dedicated hubs for **calendar** (list/get), **mail**, **drive**, **contacts**, and **web search** where the product implements them.
3. **Fallback:** Phase 1 intents **without** a dedicated canvas branch **MAY** resolve to the **main Workspace hub** view (e.g. **`workspace_hub`**) while still executing the same **`intent`** through the Integration Control Plane — **documented** **MVP** behavior for **events list**, **docs**, **tasks**, and similar until dedicated surfaces are added.

## 8. Execution scope envelope (AIOS-SPEC-010)

When **`execution_scope`** is present on the **Workspace routing envelope**, the Integration Control Plane **SHALL** validate the resolved MCP operation against that envelope **before** calling the MCP adapter. **Normative detail** of the envelope **SHALL** follow **AIOS-SPEC-010**; products **MUST NOT** treat **`execution_scope`** as decorative metadata.

## Informative Annex A — Reference implementation pointers

The following paths are **non-normative** but **verified** for the **AI OS voice interface** product (see **[AIOS-REF-013](../reference/implementation/AIOS-IMPLEMENTATION-RUNWAY-POINTER.md)**) at planning freeze **2026-04-08**:

| Concern | Path |
|---------|------|
| Routing envelope types | `src/workspace/types.ts` |
| Intent router / canvas | `src/workspace/workspaceIntentRouter.ts` |
| Scope classes | `src/workspace/scopeClasses.ts` |
| MCP tool map | `src/workspace/mcpIntentToolMap.ts` |
| Control plane | `src/workspace/integrationControlPlane.ts` |
| Canvas views | `src/shellCanvas/canvasTypes.ts` |
| Workspace payload / ICP | `src/shellCanvas/loadWorkspacePayload.ts` |

---

*End of AIOS-SPEC-007, version 1.0.1 (ratified).*
