# Architect plan — AMD-2026-006 / AIOS-SPEC-007 (draft)

**Date:** 2026-04-09  
**Evidence used:** `product_context_bundle.md` (2026-04-08); `CURRENT_SYSTEM_RESEARCH_*.md` (2026-04-08)  
**Verifier:** TBD  

---

## 1. Executive summary

This plan ratifies the governed routing stack for workspace intents, mapping `workspace.*` intents to scope classes, surface views, and MCP tools via the integration control plane (ICP). The MCP boundary is strictly server-side, with browser-based HTTP hosts handling routing envelopes. The scope includes Phase 1 intents, scope class resolution, policy checks, and audit logging. Key focus areas align with AIOS-SPEC-007 §2–3, ensuring no invented paths and full repo verification.

---

## 2. Current system grounding (file-cited)

| Topic | Repo path(s) | Notes |
|-------|-------|--|
| Phase 1 intents | `src/workspace/intentRegistry.ts` | Includes `workspace.hub`, `workspace.mail.draft_reply`, `workspace.web.search` |
| Intent → scope class | `src/workspace/scopeClasses.ts` | `WORKSPACE_SCOPE_CLASSES` defines `workspace.google.read`, `workspace.google.write`, etc. |
| Intent → MCP tool | `src/workspace/mcpIntentToolMap.ts` | Maps intents to server tool names like `list_calendars` |
| ICP entry | `src/workspace/integrationControlPlane.ts` | `runWorkspaceControlPlane` handles validation, scope resolution, and MCP calls |
| Canvas views | `src/shellCanvas/canvasTypes.ts`, `workspaceIntentRouter.ts` | Defines surface views for intents like `workspace.mail.read` |
| HTTP host | `server/prodHost.ts` | Static `dist/` and LLM API endpoint; no execution-contract engine in this repo |

---

## 3. Schemas (normative targets for SPEC / annex)

### Routing Envelope Schema
```json
{
  "intent": "workspace.mail.read",
  "scope_class": "workspace.google.read",
  "surface": "mail",
  "policy_check": "public",
  "execution_scope": "read"
}
```

### Audit Fields Schema
```json
{
  "timestamp": "2026-04-09T12:34:56Z",
  "user": "user@example.com",
  "action": "workspace.mail.read",
  "outcome": "allowed",
  "scope_class": "workspace.google.read"
}
```

### Config Schema
```json
{
  "VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL": "true",
  "ACCESS_CONTROL_EXPOSE_HEADERS": "Mcp-Session-Id"
}
```

---

## 4. Routes (intent → surface → control plane)

| workspace.* intent | Canvas View | Scope Class | Policy Check | MCP Tool Name |
|---------------------|-------------|-------------|---------------|----------------|
| workspace.hub       | hub         | google.read | public        | list_calendars |
| workspace.mail.read | mail        | google.read | public        | read_email     |
| workspace.drive.list | drive      | google.read | founder       | list_files     |
| workspace.web.search | web       | google.search | operator     | custom_search  |
| workspace.mail.draft_reply | mail  | google.write | operator     | draft_reply    |

---

## 5. Storage / session / tokens

- **OAuth tokens:** Stored in memory via `getSessionGoogleAccessToken()`; no persistent storage in client bundles.  
- **MCP session headers:** `Mcp-Session-Id` is included in HTTP requests via `callWorkspaceMcpAdapter`.  
- **Environment variables:** `VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL` and `ACCESS_CONTROL_EXPOSE_HEADERS` are used for legacy email handling and CORS headers.  
- **Secrets:** No client-side storage of secrets; tokens are managed server-side.  

---

## 6. Gaps vs governing text

| Gap | AMD/SPEC § | Proposed resolution |
|-----|-----------|--------------------|
| Execution_scope path not explicitly referenced in SPEC-007 | §2.3 | Add explicit mention of `execution_scope` in governing text if envelopes carry it. |
| Legacy email env vars (VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL) | §3.2 | Clarify usage in SPEC-007 annex for backward compatibility. |

---

## 7. Verification checklist

- [ ] Every **SHALL** in **AIOS-SPEC-007** §2–3 maps to a **file** or **explicit deferral**.  
- [ ] No **invented** path — all **src/** references verified in repo.  
- [ ] **Diff** reviewed against **`main`** (or stated branch).
