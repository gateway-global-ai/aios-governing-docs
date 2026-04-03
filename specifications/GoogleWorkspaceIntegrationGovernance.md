---
document_id: AIOS-SPEC-007
title: Google Workspace Integration Governance
version: 0.1.0
status: draft
category: specification
author: Gateway Global AIOS
created: 2026-04-02
last_updated: 2026-04-02
reviewers: []
cross_references:
  - { doc_id: "AIOS-CORE-001", relationship: "implements" }
  - { doc_id: "AIOS-CORE-002", relationship: "constrained_by" }
  - { doc_id: "AMD-2026-005", relationship: "constrained_by" }
  - { doc_id: "AIOS-SPEC-003", relationship: "complements" }
  - { doc_id: "AIOS-SPEC-006", relationship: "complements" }
amendment_history: []
---

# AIOS-SPEC-007 — Google Workspace Integration Governance (v0.1.0 draft)

## 1. Architectural Purpose

This specification defines the governance model for integrating Google Workspace services into AI OS as a **controlled execution substrate**, not a direct tool surface.

This specification implements **separation of powers** (Technical Manifesto Art. I), **policy supremacy** and **UI sovereignty** (Art. II), and **auditability** (Art. VI). It is subject to the **Governance Constitution** (Art. III — judicial and enforcement process for governed artifacts).

The integration MUST operate through:

**AI OS Intent Layer → Workspace Intent Router → Google Workspace Integration Control Plane → Google Workspace MCP Adapter → Google APIs**

The Google Workspace MCP server SHALL be treated as:

> A governed execution backend that MUST NOT be directly exposed to conversational or UI layers without AI OS mediation.

This specification ensures:

- deterministic intent routing
- policy enforcement prior to execution
- user/tenant-bound authority
- auditability of all actions
- safe exposure of high-risk capabilities

This specification is governed by **AMD-2026-005** (governed interface surfaces, deterministic failure, schema authority).

---

## 2. Integration Model

### 2.1 Control Plane

All Workspace operations MUST pass through an AI OS Integration Control Plane that:

- resolves intent
- validates authority
- enforces policy
- transforms payloads
- dispatches MCP calls

Direct calls to MCP tools from UI or agent layers are **prohibited**.

### 2.2 Execution Boundary

The MCP server is classified as **Execution Layer Only**. It MUST NOT:

- determine user intent
- enforce business logic
- bypass policy constraints
- persist AI OS state identity

### 2.3 Transport Requirements (production)

The integration SHOULD use:

- streamable HTTP transport
- OAuth 2.1 multi-user authentication where the deployment supports it
- bearer token validation per request when using token-based flows

**Single-user mode** (`--single-user`) is **NOT** permitted in **production** environments. It MAY be used only for local development or sandboxed testing under explicit policy.

---

## 3. Identity and Authority Model

### 3.1 Actor Binding

Every Workspace action MUST include:

- `tenant_id`
- user identity (e.g. `user_id` or `user_binding`)
- `actor_type`
- `session_id`
- `authority_level`

### 3.2 Authority levels (normative enum)

| Value | Description |
|-------|-------------|
| `read_only` | Observe-only; no writes |
| `user` | Standard user entitlements |
| `admin` | Elevated tenant administration |
| `system` | Automated platform operations (highest scrutiny) |

### 3.3 Execution modes (capability posture)

| Mode | Description |
|------|-------------|
| `observe` | read-only access |
| `prepare` | draft / staging (default for risky operations where applicable) |
| `execute` | final irreversible or externally visible action |
| `automate` | multi-step or scripted execution |

---

## 4. Capability Classification (Layer 1)

Workspace capabilities MUST be classified using the following **canonical governance scope classes**:

| Class | Description |
|------|-------------|
| `workspace.google.read` | search, list, retrieve, export, inspect |
| `workspace.google.write` | create, update, modify, stage, draft |
| `workspace.google.send` | outbound communication actions such as sending email or messages |
| `workspace.google.share` | permission changes, public links, grants, transfers, sharing state changes |
| `workspace.google.automation` | Apps Script execution, batch operations, multi-step workflow execution |
| `workspace.google.identity` | identity lookup, contact/people resolution, user-binding and auth-context-dependent operations |
| `workspace.google.search` | custom search, discovery, and cross-resource search surfaces where search is the primary governed action |

These scope classes are **governance primitives**. They are distinct from **intent identifiers** (Layer 2) and MAY apply to multiple intents.

**Hard rule — one-to-one resolution:** Every Layer 2 intent identifier MUST resolve to **exactly one** Layer 1 scope class. A single intent MUST NOT be assigned multiple scope classes; policy evaluation MUST use that unique mapping. Implementations MUST enforce this in registry and router code.

Examples:

- `workspace.mail.search` → `workspace.google.read`
- `workspace.mail.send` → `workspace.google.send`
- `workspace.drive.share` → `workspace.google.share`
- `workspace.contacts.search` → `workspace.google.identity`
- `workspace.search.read` or `workspace.search.query` → `workspace.google.search`
- `workspace.automation.execute` → `workspace.google.automation`

The capability classification table in this specification is the **canonical authority** for Workspace governance scopes. Planning documents, implementation notes, and prompts MUST conform to this taxonomy.

---

## 5. Intent Registry (Layer 2)

Operational intents MUST follow:

`workspace.{service}.{action}`

Service domains include: `mail`, `calendar`, `drive`, `docs`, `sheets`, `slides`, `forms`, `chat`, `tasks`, `contacts`, `search`, `automation`.

Action classes include: `hub`, `search`, `read`, `draft`, `create`, `update`, `review`, `share`, `send`, `execute`.

### 5.1 Emission rules

1. Intent MUST be explicit in structured form before control plane execution.
2. Required parameters MUST be present.
3. Freeform execution without resolved intent is prohibited.
4. Assistants MUST default to lowest-risk intent consistent with user ask.

---

## 6. Routing Contract

### 6.1 Routing envelope

All Workspace actions MUST be resolved using an envelope including at minimum:

```json
{
  "intent": "workspace.docs.update",
  "actor_type": "admin",
  "tenant_id": "tenant_123",
  "user_binding": "user@example.com",
  "execution_mode": "prepare",
  "resource_ref": {
    "type": "google_doc",
    "id": "doc_abc"
  },
  "policy_context": {
    "requires_confirmation": true,
    "scope_class": "workspace.google.write"
  }
```

`policy_context.scope_class` MUST equal the **single** Layer 1 scope class resolved from `intent`.

### 6.2 Resolution steps

The system MUST:

1. validate intent
2. validate authority
3. enforce policy (using Layer 1 scope class)
4. map to MCP tool
5. sanitize parameters
6. execute or deny
7. audit

---

## 7. Deterministic Failure Policy

If routing yields no valid tool mapping or policy denial, the system MUST enter an explicit **disambiguation** or **policy-denied** outcome, log the failure, and MUST NOT silently degrade to generic conversational mode in a way that hides governed behavior or simulates success.

---

## 8. MCP Adapter Failure Handling

Failures from the MCP adapter (timeouts, transport errors, expired auth, rate limits) MUST:

1. be logged with intent, actor, and correlation identifiers
2. return an explicit error state to the caller (not empty success)
3. NOT silently retry without policy approval for non-idempotent operations
4. MAY offer retry for idempotent read operations when policy allows

User-visible surfaces SHOULD present a recoverable error state and MAY offer retry when safe.

---

## 9. Policy Framework

### POL-WORKSPACE-001 — Scope minimization

Only OAuth scopes required for enabled tools SHALL be requested. Prefer read-only and granular service permissions by default.

### POL-WORKSPACE-002 — Draft-before-send

Send, share, and high-impact workflow actions default to `prepare` / proposed execution unless the active state identity is explicitly execution-entitled.

### POL-WORKSPACE-003 — Share and permission hard gate

Drive permission changes and public-link creation require confirmation and full audit.

### POL-WORKSPACE-004 — Automation containment

Apps Script execution and automation-class intents are disabled unless the state identity enters an automation-authorized mode.

### POL-WORKSPACE-005 — Data-exfiltration protection

Workspace content retrieved through MCP MUST NOT be silently forwarded or reused outside the entitled session.

### POL-WORKSPACE-006 — Truthful load state

All Workspace views MUST distinguish `ok`, `empty`, and `error`. Error MUST NOT be presented as empty.

---

## 10. Surface Model

Workspace surfaces (examples): `workspace_hub`, `workspace_mail_hub`, `workspace_calendar_hub`, `workspace_drive_hub`, `workspace_doc_editor`, etc.

Workspace **hub** surfaces MUST NOT auto-create execution runs on entry. **Workflow/editor** surfaces MUST require identifiers for concrete resources.

Surfaces MUST declare load states and comply with **AIOS-SPEC-006** registration requirements for governed views.

---

## 11. Audit Requirements

Each operation MUST log: intent id, resolved state identity, tenant/user binding, tool chosen, parameters (safe subset or hash), result outcome, policy decisions, failure mode, and whether the action was proposed vs executed.

---

## 12. Deployment Phases

| Phase | Capabilities |
|-------|----------------|
| 1 — Read plane | Calendar list/get, Gmail search/read, Drive search/read, Docs get/export, Contacts search, Tasks list/get |
| 2 — Draft plane | Gmail drafts, Docs create/modify, constrained Sheets/Slides |
| 3 — Execution plane | Gmail send, Calendar manage, Drive sharing, Chat send, Forms updates |
| 4 — Automation plane | Apps Script, batch, cross-app workflows |

Advancement to a higher phase SHOULD be recorded as a governance decision (Council or delegated authority per Constitution).

---

## 13. Compliance

Implementations that violate intent routing, one-to-one scope mapping, schema requirements, or execution constraints are **invalid** under AI OS governance until remediated.

---

## 14. Notes

The upstream [Google Workspace MCP](https://github.com/taylorwilsdon/google_workspace_mcp) project provides broad service coverage and deployment options. **This specification constrains that surface** into a governed system; AI OS remains the contract boundary.

---

**This specification is governed by the AIOS Governance Constitution (v1.0).** Amendments follow the legislative process.
