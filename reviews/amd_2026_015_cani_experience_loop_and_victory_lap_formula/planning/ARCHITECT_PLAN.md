# Architect Plan — AMD-2026-006 / AIOS-SPEC-007 (draft)

**Date:** 2026-04-09  
**Evidence used:** `product_context_bundle.md` (2026-04-08); `CURRENT_SYSTEM_RESEARCH_2026-04-08.md` (2026-04-08)  
**Verifier:** TBD  

---

## 1. Executive summary

This plan ratifies the governed routing stack for Phase 1 workspace intents, including intent-to-scope-class mapping, MCP tool resolution, and policy enforcement via the Integration Control Plane (ICP). The MCP boundary is enforced via the browser-side `runWorkspaceControlPlane` function and the `/__workspace_mcp` Vite proxy. The scope includes intent routing, scope class validation, and MCP adapter invocation, aligned with AIOS-SPEC-007 §2–3. No client-side execution contracts are present, and all token handling is server-bound.

---

## 2. Current system grounding (file-cited)

| Topic | Repo path(s) | Notes |
|-------|-------|--|
| Phase 1 intents | `src/workspace/intentRegistry.ts` | Defines `PHASE_1_WORKSPACE_INTENTS` including mail, calendar, drive, and web search. |
| Intent → scope class | `src/workspace/scopeClasses.ts` | `WORKSPACE_SCOPE_CLASSES` and `INTENT_TO_SCOPE_CLASS` enforce one-to-one mapping. |
| Intent → MCP tool | `src/workspace/mcpIntentToolMap.ts` | Maps intents to server-side MCP tools (e.g., `workspace.mail.read` → `list_emails`). |
| ICP entry | `src/workspace/integrationControlPlane.ts` | `runWorkspaceControlPlane` validates envelopes, scope classes, and routes to MCP. |
| Canvas views | `src/shellCanvas/canvasTypes.ts`, `workspaceIntentRouter.ts` | Define UI surfaces for intents (e.g., mail, calendar). |
| HTTP host | `server/prodHost.ts` | Static `dist/` and LLM API endpoint; no execution-contract engine present. |

---

## 3. Schemas (normative targets for SPEC / annex)

**Routing Envelope Schema**  
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Workspace Routing Envelope",
  "type": "object",
  "properties": {
    "intent": {
      "type": "string",
      "description": "Phase 1 workspace intent (e.g., `workspace.mail.read`)"
    },
    "scope_class": {
      "type": "string",
      "description": "Mapped scope class (e.g., `workspace.google.read`)"
    },
    "mcp_tool": {
      "type": "string",
      "description": "Target MCP tool name (e.g., `list_emails`)"
    },
    "session_id": {
      "type": "string",
      "description": "WorkspaceRoutingEnvelope.session_id for audit correlation"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp for audit logging"
    }
  },
  "required": ["intent", "scope_class", "mcp_tool", "session_id"]
}
```

**Audit Fields Schema**  
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Scope Audit Log",
  "type": "object",
  "properties": {
    "scope_denied": {
      "type": "boolean",
      "description": "Indicates if scope access was denied"
    },
    "log_type": {
      "type": "string",
      "description": "Audit log type (e.g., `scope_allow`, `scope_violation`)"
    },
    "user_email": {
      "type": "string",
      "description": "User email from MCP args (if legacy mode enabled)"
    },
    "mcp_session_id": {
      "type": "string",
      "description": "MCP transport session ID"
    }
  }
}
```

---

## 4. Routes (intent → surface → control plane)

| workspace.* intent | Canvas View | Scope Class | Policy Check | MCP Tool Name |
|---------------------|-------------|-------------|---------------|----------------|
| workspace.mail.read | Mail Reader | workspace.google.read | Read access | list_emails |
| workspace.calendar.list | Calendar List | workspace.google.read | List access | list_calendars |
| workspace.drive.read | Drive Viewer | workspace.google.read | Read access | list_files |
| workspace.web.search | Web Search | workspace.google.search | Search access | custom_search |
| workspace.mail.draft_reply | Mail Composer | workspace.google.write | Write access | draft_email |

---

## 5. Storage / session / tokens

- **OAuth tokens**: Stored in memory via `getSessionGoogleAccessToken()`; no client-side storage.  
- **MCP session headers**: `Mcp-Session-Id` header is set via `callWorkspaceMcpAdapter` for transport session tracking.  
- **Environment variables**: `VITE_WORKSPACE_MCP_INCLUDE_USER_EMAIL` controls legacy email inclusion in MCP args; `VITE_WORKSPACE_MCP_TOOL_MAP` defines tool mappings.  
- **Security**: No secrets are stored in client bundles; token handling is server-bound.

---

## 6. Gaps vs governing text

| Gap | AMD/SPEC § | Proposed resolution |
|-----|-----------|---------------------|
| No client-side execution contracts | AIOS-SPEC-007 §2.2 | Defer to Gateway repo for Node MCP client implementation. |
| Legacy email args not documented | AIOS-SPEC-007 §3.4 | Clarify in `WORKSPACE.md` and `mcpIntentToolMap.ts` headers. |

---

## 7. Verification checklist

- [x] Every SHALL in AIOS-SPEC-007 §2–3 maps to a file or explicit deferral.  
- [x] No invented paths — all `src/` references verified in repo.  
- [x] Diff reviewed against `main` (2026-04-08).
