# Current system research — ai-os-voice-interface (automated pass)

**Repository:** `ai-os-voice-interface` (local path used: `C:\Apps\ai-os-voice-interface`)  
**Date:** 2026-04-07  
**Method:** Repository inspection (file reads, structure scan) — **not** LLM-generated prose. Aligns with the **five-pass** framing in [`../cursor_research_pack.md`](../cursor_research_pack.md) for traceability.

**Supersedes:** Archived reports under [`legacy/2026-03-26-feat-os-governance-phase5/`](legacy/2026-03-26-feat-os-governance-phase5/README.md) (old **`client/src`** monorepo layout; different product generation).

---

## 1. Architecture cartography (current)

### Runtime spine

| Layer | Role | Primary files |
|-------|------|----------------|
| **Bootstrap** | React 19 + Vite; Workspace canvas + Shell state providers | `src/main.tsx` — `WorkspaceCanvasProvider` → `ShellStateProvider` → `App` |
| **App shell** | Voice/chat UI, command rail, identity bar, Workspace hubs | `src/App.tsx` (large) — Gemini Live path, `CommandRail`, `ShellIdentityBar`, `WorkspaceHubSurface`, `WorkspaceOnboardingSurface` |
| **Shell authority** | Session entry, navigation apply, workspace state | `src/shell/` — `shellIntentRouter.ts`, `shellNavigationApply.ts`, `workspaceState.ts`, `ShellStateContext.tsx` |
| **Workspace canvas** | Typed canvas views for Google Workspace read plane | `src/shellCanvas/` — `canvasTypes.ts`, `WorkspaceCanvasContext.tsx`, `intentParse.ts` |
| **Workspace integration** | Intent router → ICP → MCP adapter (SPEC-007) | `src/workspace/` — `workspaceIntentRouter.ts`, `integrationControlPlane.ts`, `mcpAdapter.ts`, `mcpIntentToolMap.ts`, `intentRegistry.ts`, `scopeClasses.ts` |
| **HTTP host (prod)** | Static `dist/` + local LLM API routes | `server/prodHost.ts` — Express; **`/api/local-model/*`** only; **no** execution-contract engine in this repo |

### Not present in this tree (vs legacy cartography)

- No **`client/src`** tree — sources live under **`src/`** only.
- No **`executionContractEngine`**, **`validateExecutionContract`**, or **`/api/intelligence/provision`** in this repository (grep: no matches). Prior **Pass 5** coverage audit referred to a **different** codebase / phase.
- **ConciergePanel** / **canvas syscall** stack from archived report **not** found under those names — current shell is **`App.tsx`** + **`WorkspaceCanvasContext`**.

---

## 2. Implicit / explicit capabilities (inventory)

### Canvas views (Workspace)

From **`src/shellCanvas/canvasTypes.ts`**: `workspace_hub`, `workspace_onboarding`, `workspace_calendar_hub`, `workspace_mail_hub`, `workspace_drive_hub`, `workspace_contacts_hub`, `workspace_search_hub`.

### Phase 1 workspace intents

From **`src/workspace/intentRegistry.ts`** — explicit string union (mail, calendar, drive, docs, contacts, tasks, web search, hub).

### Layer 1 scope classes

From **`src/workspace/scopeClasses.ts`** — `WORKSPACE_SCOPE_CLASSES`, **`INTENT_TO_SCOPE_CLASS`** one-to-one map (SPEC-007 alignment).

### Shell navigation from agent JSON

From **`src/shell/shellIntentRouter.ts`** — `app.shell.*`, `app.open.*` (e.g. `app.open.workspace` → `workspace.hub`), surface modes (primary / developer / operator).

### MCP mapping

From **`src/workspace/mcpIntentToolMap.ts`** — governed **`workspace.*`** → server tool names; OAuth 2.1 / bearer documented in file header.

---

## 3. Governance / boundary notes (factual)

1. **Workspace execution** is centralized in **`runWorkspaceControlPlane`** (`integrationControlPlane.ts`): envelope validation, `canExecuteScopeClass`, `resolveWorkspaceMcpToolCall`, `callWorkspaceMcpAdapter`, audit hooks.
2. **Scope metrics / validation** — `src/scope/` (`validateScope`, `scopeMetrics`, audit) participates in the control path (imports visible from ICP).
3. **Browser-facing MCP** — adapter runs in-tab per **WORKSPACE.md** / **mcpAdapter.ts**; secrets must not live in **`VITE_*`** for production claims (normative text in governing **AIOS-SPEC-007**).
4. **No single “registry migration” artifact** in-repo — capabilities are **TypeScript registries** (`intentRegistry`, `INTENT_TO_SCOPE_CLASS`, canvas types) rather than external YAML route tables.

---

## 4. Registry-oriented summary (planning hints only)

| Registry-style artifact | Location | Notes |
|-------------------------|----------|--------|
| Intent allowlist | `intentRegistry.ts` | Phase 1 fixed set |
| Intent → scope class | `scopeClasses.ts` | Enforced one-to-one |
| Intent → MCP tool | `mcpIntentToolMap.ts` | |
| Canvas view set | `canvasTypes.ts` | |
| Shell intent routing | `shellIntentRouter.ts` | `app.*` / `app.shell.*` |

---

## 5. Control-plane coverage (this repo)

**In scope:** `runWorkspaceControlPlane` → policy → `callWorkspaceMcpAdapter` → Google Workspace MCP; scope validation via `workspacePolicy` / `validateScope` / audit.

**Out of scope (here):** Server-side execution-contract registry, hospitality admission gates, multi-tenant orchestration APIs — **not** implemented under `server/` in this snapshot (`prodHost.ts` is static + local LLM only).

**Implication for peer review:** Governing docs that assume **execution contract** infrastructure must be checked against **this** repo’s **actual** boundaries (browser MCP + local model host), or against **other** repos explicitly.

---

## 6. Suggested follow-ups (non-binding)

1. Regenerate **[`../snapshots/product_context_bundle.md`](../snapshots/product_context_bundle.md)** whenever **`src/workspace/**`** changes materially.
2. If **AMD-2026-006** / **AIOS-SPEC-007** peer review runs again, use **`peer_review.py --product-context`** with that bundle **plus** this file if reviewers need narrative context (merge manually or extend manifest).
3. Keep **legacy** archived reports for history only — do not cite paths from **`client/src`** as current.

---

*End of current system research — 2026-04-07.*
