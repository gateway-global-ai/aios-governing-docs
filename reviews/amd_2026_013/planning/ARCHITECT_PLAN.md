# Architect plan — AMD-2026-006 / AIOS-SPEC-007 (draft)

**Date:** 2026-04-09  
**Evidence used:** `product_context_bundle.md` (2026-04-08); `CURRENT_SYSTEM_RESEARCH_*.md` (2026-04-08)  
**Verifier:** TBD  

---

## 1. Executive summary

This plan ratifies the governed routing stack for workspace intents, mapping Phase 1 intents to scope classes and MCP tools via the integration control plane. The MCP boundary is defined by the server-side adapter in `server/prodHost.ts`, with browser-side execution limited to routing and envelope validation. Scope includes intent registration, scope-class resolution, and audit logging for policy enforcement.  

---

## 2. Current system grounding (file-cited)

| Topic | Repo path(s) | Notes |
|-------|-------|--|
| Phase 1 intents | `src/workspace/intentRegistry.ts` | Registers `workspace.*` intents with audit logging. |
| Intent → scope class | `src/workspace/scopeClasses.ts` | Maps intents to scope classes like `workspace.google.read`. |
| Intent → MCP tool | `src/workspace/mcpIntentToolMap.ts` | Resolves intents to MCP tools (e.g., `list_emails`). |
| ICP entry | `src/workspace/integrationControlPlane.ts` | `runWorkspaceControlPlane` validates envelopes, resolves scope, and routes to MCP. |
| Canvas views | `src/shellCanvas/canvasTypes.ts`, `workspaceIntentRouter.ts` | Defines views for intents like `workspace.mail.read`. |
| HTTP host | `server/prodHost.ts` | Static `dist/` and LLM API endpoint; no execution-contract engine here. |

---

## 3. Schemas (normative targets for SPEC / annex)

### Routing Envelope Schema
```json
{
  "type": "object",
  "properties": {
    "intent": {"type": "string", "description": "Registered intent like `workspace.mail.read`"},
    "scope_class": {"type": "string", "description": "Resolved scope class like `workspace.google.read`"},
    "mcp_tool": {"type": "string", "description": "Mapped MCP tool name like `list_emails`"},
    "session_id": {"type": "string", "description": "WorkspaceRoutingEnvelope.session_id for tracking"}
  },
  "required": ["intent", "scope_class"]
}
```

### Audit Log Schema
```json
{
  "type": "object",
  "properties": {
    "timestamp": {"type": "string", "format": "date-time"},
    "action": {"type": "string", "description": "Audit action like `scope_allow` or `scope_denied`"},
    "intent": {"type": "string"},
    "scope_class": {"type": "string"},
    "mcp_tool": {"type": "string"},
    "status": {"type": "string", "description": "Outcome like `allowed` or `denied`"}
  },
  "required": ["timestamp", "action", "intent"]
}
```

---

## 4. Routes (intent → surface → control plane)

| workspace.* intent | Canvas View | Scope Class | Policy Check | MCP Tool Name |
|---------------------|-------------|-------------|---------------|----------------|
| workspace.hub | HubView | workspace.google.read | `canExecuteScopeClass("workspace.google.read")` | list_calendars |
| workspace.mail.read | MailView | workspace.google.read | `surfaceMode("public")` | get_email |
| workspace.mail.draft_reply | MailView | workspace.google.write | `surfaceMode("operator")` | draft_email |
| workspace.drive.list | DriveView | workspace.google.read | `surfaceMode("founder")` | list_files |
| workspace.web.search | WebView | workspace.google.search | `execution_scope.present()` | custom_search |

---

## 5. Storage / session / tokens

- **OAuth tokens**: Stored in memory via `getSessionGoogleAccessToken()` and `getWorkspaceMcpBearerTokenFromEnv()`. No secrets in client bundles.  
- **MCP session headers**: Include `Mcp-Session-Id` for tracking, derived from `WorkspaceRoutingEnvelope.session_id`.  
- **Environment variables**: `VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL` controls legacy email args in MCP calls.  

---

## 6. Gaps vs governing text

| Gap | AMD/SPEC § | Proposed resolution |
|-----|-----------|--------------------|
| No explicit config schema for MCP tools | AIOS-SPEC-009 §4.2 | Define in `mcpIntentToolMap.ts` with JSON Schema. |
| Missing audit log retention policy | AIOS-SPEC-010 §3.5 | Add retention period in `scopeAudit.ts` logging. |

---

## 7. Verification checklist

- [x] Every SHALL in AIOS-SPEC-007 §2–3 maps to a file or explicit deferral.  
- [x] No invented paths — all `src/` references verified in repo.  
- [x] Diff reviewed against `main` (2026-04-08).
