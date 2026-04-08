# Architect plan — AMD-2026-006 / AIOS-SPEC-007 (draft)

**Date:** 2026-04-08  
**Evidence used:** [`product_context_bundle.md`](../../../reference/knowledge_base/snapshots/product_context_bundle.md) (**Generated:** 2026-04-08); [`CURRENT_SYSTEM_RESEARCH_2026-04-08.md`](../../../reference/knowledge_base/cursor_research_outputs/CURRENT_SYSTEM_RESEARCH_2026-04-08.md)  
**Verifier:** _pending human review_

---

## 1. Executive summary

This ratification package must bind **AIOS-SPEC-007** (normative **SHALL** / **MUST** for Workspace integration) to the **implemented** path in **`ai-os-voice-interface`**: **Workspace Intent Router** (`workspaceIntentRouter.ts`) → **Integration Control Plane** (`runWorkspaceControlPlane` in `integrationControlPlane.ts`) → **MCP adapter** (`mcpAdapter.ts` / `callWorkspaceMcpAdapter`). **Layer 2** intents are enumerated in **`intentRegistry.ts`**; **Layer 1** scope classes and **one-to-one** mapping live in **`scopeClasses.ts`**. The **MCP** layer is **not** exposed as raw tool names to the voice/agent layer; **`mcpIntentToolMap.ts`** resolves governed intent → server tool **name** and **arguments**. **OAuth 2.1** bearer for **`tools/call`** is obtained via **`getSessionGoogleAccessToken()`** or dev **`getWorkspaceMcpBearerTokenFromEnv()`** (**`integrationControlPlane.ts`**). **Execution scope** (**AIOS-SPEC-010**, `execution_scope` on **`WorkspaceRoutingEnvelope`**) is validated in **`runWorkspaceControlPlane`** via **`validateScopeOperation`** when present. In scope for **AMD-2026-006**: prove **SPEC-007** §§1–4 (and cross-refs) against this tree; **author revision** after committee will align amendment text and **SPEC-007** annexes, not this planning draft.

---

## 2. Current system grounding (file-cited)

| Topic | Repo path(s) | Notes |
|-------|--------------|--------|
| Phase 1 intents | `src/workspace/intentRegistry.ts` | `PHASE_1_WORKSPACE_INTENTS` — includes mail thread/draft, `workspace.web.search`, `workspace.calendar.events.list`, docs, tasks. |
| Intent → scope class | `src/workspace/scopeClasses.ts` | `INTENT_TO_SCOPE_CLASS` + `workspace.google.search` for web search; runtime `assertOneToOneMapping()`. |
| Intent → MCP tool | `src/workspace/mcpIntentToolMap.ts` | `resolveWorkspaceMcpToolCall`; OAuth / legacy email env documented in file header. |
| ICP entry | `src/workspace/integrationControlPlane.ts` | `runWorkspaceControlPlane` — envelope validation, policy, optional `execution_scope` branch, adapter. |
| Routing types | `src/workspace/types.ts` | `WorkspaceRoutingEnvelope` — **SPEC-007** comment §6; `execution_scope?: ExecutionScopeEnvelope` (**SPEC-010**). |
| Canvas → intent | `src/workspace/workspaceIntentRouter.ts` | `workspaceIntentToCanvasView`, `routeWorkspaceIntent`. |
| Canvas views | `src/shellCanvas/canvasTypes.ts` | `CanvasView` union + `ALL_CANVAS_VIEWS`. |
| Scope validation | `src/scope/validateScope.ts`, `scopeRouting.ts`, `scopeAudit.ts`, `scopeMetrics.ts` | Used from ICP when `execution_scope` set. |
| Product contract | `WORKSPACE.md` (repo root) | MCP streamable HTTP, CORS, proxy, transport vs audit `session_id`. |
| HTTP host | `server/prodHost.ts` | Static + local LLM; **no** execution-contract engine in this repo. |

---

## 3. Schemas (normative targets for SPEC / annex)

| Construct | Source of truth (implementation) | Governing alignment |
|-----------|-----------------------------------|----------------------|
| **Workspace routing envelope** | `WorkspaceRoutingEnvelope` in `src/workspace/types.ts` (`intent`, `policy_context.scope_class`, `execution_mode`, `resource_ref`, `query`, `calendar_time_range`, `contacts_page_token`, `execution_scope`, …) | **AIOS-SPEC-007** normative routing model §2; cross-**AIOS-SPEC-009** intent primitive. |
| **Control plane result** | `WorkspaceControlPlaneResult` — `ok: false` codes: `policy_denied`, `invalid_intent`, `adapter_error`, `not_configured`, `auth_required`, `scope_denied` | Deterministic failure surface for peer review / **AMD-2026-005** alignment. |
| **Execution scope** | `ExecutionScopeEnvelope` imported from `src/scope/executionScopeTypes.ts`; validated in **`runWorkspaceControlPlane`** | **AIOS-SPEC-010**; Round 1 “completeness” — **SPEC-007** body should **§**-reference when envelope is required. |

**Author revision target:** Add an **Annex** or **§** table in **AIOS-SPEC-007** that pins **field-level** envelope requirements to **`types.ts`** (or explicitly defers to **SPEC-009**/**010** for execution scope) — addresses **Round 1** “Annex A / normative depth” theme.

---

## 4. Routes (intent → surface → control plane)

**Policy:** `canExecuteScopeClass` in `workspacePolicy.ts` (surface mode). **Scope class:** `resolveScopeClass` / `INTENT_TO_SCOPE_CLASS`. **MCP** tool: `resolveWorkspaceMcpToolCall` → **server** `tool` string.

| Representative `workspace.*` intent | Canvas view (`workspaceIntentToCanvasView`) | Scope class (from `scopeClasses.ts`) | MCP resolution |
|-------------------------------------|---------------------------------------------|----------------------------------------|----------------|
| `workspace.hub` | `workspace_hub` | `workspace.google.read` | (hub — no MCP in same pattern) |
| `workspace.calendar.list` | `workspace_calendar_hub` | `workspace.google.read` | `mcpIntentToolMap` |
| `workspace.calendar.events.list` | **`workspace_hub`** (fallback — **not** in calendar `if`) | `workspace.google.read` | `mcpIntentToolMap` |
| `workspace.mail.search` | `workspace_mail_hub` | `workspace.google.read` | e.g. `search_gmail_messages` |
| `workspace.mail.draft_reply` | `workspace_mail_hub` | `workspace.google.write` | draft tool |
| `workspace.drive.list` | `workspace_drive_hub` | `workspace.google.read` | list tool |
| `workspace.contacts.list` | `workspace_contacts_hub` | `workspace.google.identity` | list contacts |
| `workspace.web.search` | `workspace_search_hub` | `workspace.google.search` | PSE / search tool per MCP |
| `workspace.docs.read` | **`workspace_hub`** (fallback) | `workspace.google.read` | docs tool |

**Finding:** **`workspace.calendar.events.list`** and **`workspace.docs.*`** (and similar) **do not** receive dedicated canvas hubs in **`workspaceIntentToCanvasView`** — they fall through to **`workspace_hub`**. **UI_PLAN** (Phase C) should decide whether that is intentional or a UX gap.

---

## 5. Storage / session / tokens

| Concern | Implementation reference |
|---------|---------------------------|
| **Google OAuth** | `getSessionGoogleAccessToken()` — `workspaceSessionAuth.ts`; used in **`runWorkspaceControlPlane`** before adapter. |
| **Dev bearer** | `getWorkspaceMcpBearerTokenFromEnv()` — `VITE_WORKSPACE_MCP_BEARER_TOKEN` (see **`integrationControlPlane.ts`** error path). |
| **MCP transport** | `callWorkspaceMcpAdapter` — **`mcpAdapter.ts`**; **`Mcp-Session-Id`** / streamable HTTP per **WORKSPACE.md**. |
| **Legacy email in args** | **`mcpIntentToolMap.ts`** — `VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL`, `getWorkspaceGoogleUserEmail()`. |
| **Secrets in client** | **WORKSPACE.md** + **AIOS-SPEC-007** §3 — PSE keys **MUST NOT** be **`VITE_*`** for production claims. |

---

## 6. Gaps vs governing text

| Gap | AMD/SPEC § | Proposed resolution |
|-----|------------|---------------------|
| **AMD-2026-006** is a **stub**; no inlined annexes | AMD §2–3 | **Round 1 theme** — **author revision** expands **§** pointers or short annex; **peer review** targets **SPEC-007** + amendment as **coordinator merged package** for Round 2. |
| **SPEC-007** short (v0.1.1); **SHALL** list vs **types.ts** field matrix | **AIOS-SPEC-007** §§1–4 | Add **§** “Implementation mapping” table or **Annex A** listing **envelope** fields **SHALL** / **MAY**; cite **`types.ts`**. |
| **Canvas routing** mismatch for some Phase 1 intents | **AIOS-SPEC-006** surface registration (AMD Change 3) | **UI** plan (Phase C): align **`canvasTypes`** / `workspaceIntentToCanvasView` with **hub** UX expectations; **SPEC-006** registry rows. |
| **Web search** policy **POL-WEB-SCOPE-001** | **AIOS-SPEC-007** §3 | **Verify** policy index / tenant story; **defer** if org policy not yet registered — document **non-blocking** in committee packet. |
| **Liability** language | Round 1 **Legal Enforceability** | **Defer** to **MPOA** / council legal review or **SPEC-007** non-normative **note** — not invented in architect plan. |

---

## 7. Verification checklist

- [ ] Every **SHALL** in **AIOS-SPEC-007** §2–3 maps to a **file** or **explicit deferral**.
- [ ] No **invented** path — all **`src/`** references verified in repo.
- [ ] **Diff** reviewed against **`main`** (or stated branch) — **human verifier**.

---

## 8. Round 1 synthesis response

| Theme | Address in this plan |
|-------|----------------------|
| **Stub vs spec** | §6 — amendment defers to **SPEC-007** + **typed** `WorkspaceRoutingEnvelope`; Round 2 target document = **SPEC-007** or merged per **REVIEW_SYNTHESIS** coordinator note. |
| **Normative depth / Annex A** | §3 — envelope + **Annex** target for author revision. |
| **Cross-document** | **SPEC-009**/**010** hooks on **`execution_scope`** and **`types.ts`** comments. |

---

*Draft — pending human verification against `ai-os-voice-interface` before Phase C.*
