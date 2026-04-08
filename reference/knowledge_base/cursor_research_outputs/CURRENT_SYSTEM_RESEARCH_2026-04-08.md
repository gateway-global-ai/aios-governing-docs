# Current system research — ai-os-voice-interface (repository inspection pass)

**Repository:** `ai-os-voice-interface` (local path used: `C:\Apps\ai-os-voice-interface`)  
**Date:** 2026-04-08  
**Method:** Repository inspection (file reads, targeted structure review) — aligns with [`../cursor_research_pack.md`](../cursor_research_pack.md). **AMD-2026-006** Phase A **Option B** (successor to [`CURRENT_SYSTEM_RESEARCH_2026-04-07.md`](CURRENT_SYSTEM_RESEARCH_2026-04-07.md)).

**Supersedes for operational use:** [`CURRENT_SYSTEM_RESEARCH_2026-04-07.md`](CURRENT_SYSTEM_RESEARCH_2026-04-07.md) — retain prior file for history; cite **this** file for current tree.

---

## 1. Architecture cartography (current)

### Runtime spine

| Layer | Role | Primary files |
|-------|------|----------------|
| **Bootstrap** | React + Vite; Workspace canvas + Shell state | `src/main.tsx` — `WorkspaceCanvasProvider` (`onPolicyDenied` → speak) → `ShellStateProvider` → `App` |
| **App shell** | Voice/chat, command rail, identity, Workspace surfaces | `src/App.tsx` — `CommandRail`, `ShellIdentityBar`, `WorkspaceHubSurface`, `WorkspaceOnboardingSurface`, Gemini path |
| **Shell authority** | Session entry, navigation, workspace state | `src/shell/` — `shellIntentRouter.ts`, `shellNavigationApply.ts`, `workspaceState.ts`, `ShellStateContext.tsx` |
| **Workspace canvas** | Typed views (Google Workspace read plane) | `src/shellCanvas/` — `canvasTypes.ts`, `WorkspaceCanvasContext.tsx`, `intentParse.ts` |
| **Workspace integration** | Intent router → ICP → MCP adapter (**AIOS-SPEC-007**) | `src/workspace/` — `workspaceIntentRouter.ts`, `integrationControlPlane.ts`, `mcpAdapter.ts`, `mcpIntentToolMap.ts`, `intentRegistry.ts`, `scopeClasses.ts`, `workspacePolicy.ts`, `workspaceAudit.ts` |
| **Scope subsystem** | Validation + metrics + audit hooks used from ICP | `src/scope/` — `validateScope.ts`, `scopeRouting.ts`, `scopeAudit.ts`, `scopeMetrics.ts` |
| **HTTP host (prod)** | Static `dist/` + local LLM API | `server/prodHost.ts` — **no** execution-contract engine in this repo |

### Not present (reconfirmed)

- No **`client/src`** — sources under **`src/`** only.
- **`grep`** — no **`executionContractEngine`**, **`validateExecutionContract`** in this repo.
- Legacy **ConciergePanel** naming not used for current shell (see **04-07** archive note).

---

## 2. Phase 1 workspace intents (verbatim source)

From **`src/workspace/intentRegistry.ts`** — `PHASE_1_WORKSPACE_INTENTS` includes (non-exhaustive highlights vs **04-07** summary):

- Hub / calendar: `workspace.hub`, `workspace.calendar.list`, `workspace.calendar.events.list`, `workspace.calendar.get`
- Mail: `workspace.mail.search`, `workspace.mail.read`, `workspace.mail.thread.read`, **`workspace.mail.thread.summarize`**, **`workspace.mail.draft_reply`**
- Drive/docs: `workspace.drive.list`, `workspace.drive.search`, `workspace.drive.read`, `workspace.docs.read`, `workspace.docs.export`
- Contacts/tasks: `workspace.contacts.list`, `workspace.contacts.search`, `workspace.tasks.list`, `workspace.tasks.get`
- Web: **`workspace.web.search`** (Google Custom Search / PSE — MCP host env)

**Implication:** Peer-review narratives that list only a short mail/calendar/drive subset are **stale** relative to this registry.

---

## 3. Layer 1 scope classes and one-to-one map

From **`src/workspace/scopeClasses.ts`:**

- **`WORKSPACE_SCOPE_CLASSES`:** `workspace.google.read`, `workspace.google.write`, `workspace.google.send`, `workspace.google.share`, `workspace.google.automation`, `workspace.google.identity`, **`workspace.google.search`**
- **`INTENT_TO_SCOPE_CLASS`:** every `Phase1WorkspaceIntent` maps to **exactly one** scope class; **`workspace.web.search` → `workspace.google.search`**; **`workspace.mail.draft_reply` → `workspace.google.write`**; runtime **`assertOneToOneMapping()`** on load.

---

## 4. Integration control plane (`runWorkspaceControlPlane`)

From **`src/workspace/integrationControlPlane.ts`** (inspected):

1. **`validateEnvelope`** — intent registered, Phase 1 allowlist, **`policy_context.scope_class`** matches **`resolveScopeClass(intent)`**.
2. **`canExecuteScopeClass`** — surface mode (`public` | `founder` | `operator` | `customer`).
3. **`resolveWorkspaceMcpToolCall`** — governed intent → MCP tool name + args; failure paths include **legacy email** env misconfiguration (`VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL`, etc.).
4. **`execution_scope` branch** — if present: **`routingEnvelopeToScopeTarget`** → **`validateScopeOperation`** → allow/deny with **`scope_denied`** / audit (**`logScopeViolation`** / **`logScopeAllow`**). This is **additional** to the **04-07** description (narrower envelope-only story).
5. **Bearer** — **`getSessionGoogleAccessToken()`** or **`getWorkspaceMcpBearerTokenFromEnv()`**; explicit **`auth_required`** path if missing.
6. **`callWorkspaceMcpAdapter`** — streamable HTTP client (see **`mcpAdapter.ts`**, **WORKSPACE.md**).

---

## 5. MCP mapping and OAuth notes

From **`src/workspace/mcpIntentToolMap.ts`** header and **`resolveWorkspaceMcpToolCall`:**

- Tools are **server names** (`list_calendars`, …), not raw `workspace.*` strings.
- **OAuth 2.1:** account via **`Authorization: Bearer`**; **`user_google_email` in JSON-RPC args** can break FastMCP (**unexpected_keyword_argument**) unless legacy mode **`VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL=true`** + email envs.

---

## 6. WORKSPACE.md (product contract vs SPEC-007)

**WORKSPACE.md** documents: **Intent Router → ICP → MCP Adapter**; browser **`runWorkspaceControlPlane` → `callWorkspaceMcpAdapter`**; **`/__workspace_mcp`** Vite proxy; **CORS** / **`Access-Control-Expose-Headers`** / **`Mcp-Session-Id`** troubleshooting; distinction between **MCP transport session** and **`WorkspaceRoutingEnvelope.session_id`**; reference to **Gateway** server-side adapter pattern (*out of tree*).

---

## 7. Governance / peer-review implications (factual)

| Topic | Finding |
|-------|---------|
| **AMD-2026-006 / SPEC-007 alignment** | Code implements routed ICP + scope classes + MCP adapter; **execution_scope** path must appear in governing text if **envelope** carries it. |
| **Stub vs spec (Round 1 theme)** | Amendment remains short; **AIOS-SPEC-007** + this research + **`product_context_bundle.md`** should be triangulated for **Round 2** target document choice. |
| **Product bundle** | Regenerate **[`../snapshots/product_context_bundle.md`](../snapshots/product_context_bundle.md)** when **`src/workspace/**`** changes; last bundle run **2026-04-08** per governing repo. |

---

## 8. Suggested follow-ups (non-binding)

1. **Peer review:** Prefer **`--product-context`** with **bundle** + **this file** (or merged prompt) for **AMD-2026-006** / **SPEC-007** runs.
2. **Gateway repo:** Normative claims about **Node** MCP client belong in **that** codebase’s docs — **WORKSPACE.md** already marks browser vs server boundary.
3. **Legacy:** Do not cite **04-07** as latest; use **this** file for **2026-04-08** snapshot.

---

*End of current system research — 2026-04-08.*
