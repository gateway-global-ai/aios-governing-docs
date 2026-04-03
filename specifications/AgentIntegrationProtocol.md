---
document_id: AIOS-SPEC-003
title: AIOS Agent Integration Protocol (AIP)
version: 1.2.0
status: ratified
category: specification
author: Gateway Global
created: 2026-03-28
last_updated: 2026-04-02
reviewers: []
supersedes: null
cross_references:
  - { doc_id: "AIOS-CORE-002", relationship: "constrained_by" }
  - { doc_id: "AIOS-SPEC-004", relationship: "complements" }
  - { doc_id: "AIOS-SPEC-005", relationship: "complements" }
  - { doc_id: "AMD-2026-005", relationship: "constrained_by" }
  - { doc_id: "AIOS-SPEC-007", relationship: "constrained_by" }
amendment_history:
  - amendment_id: AMD-2026-005
    ratified: 2026-04-02
    summary: Workspace model, governed intent emission, deterministic failure, schema authority, ratification flow alignment
  - amendment_id: AMD-2026-006
    ratified: null
    summary: Google Workspace governed integration plane; workspace.* intents; SPEC-007
---
# AIOS Agent Integration Protocol (AIP) v1.2.0

## 1. Architectural Purpose
The Agent Integration Protocol (AIP) defines the exact interface and constraints for autonomous and semi‑autonomous coding agents operating within the Gateway Global AIOS ecosystem. It provides the machine‑readable instructions for agents to generate, test, and deploy platform primitives.

Agents operating under this protocol act exclusively as **drafters** as defined by the *Governance Constitution (Article II: Legislative Process)*. They cannot unilaterally deploy code; they can only invoke the AIOS Command Line Interface (CLI) via the Model Context Protocol (MCP) to generate legally compliant JSON schemas. Every artifact an agent creates must pass the DCP compiler and, if classified as Tier 3, requires human Council ratification.

### Amendment Program Workspace Model

Agents operating under this specification MUST treat governed Amendment Program interactions as a **workspace-first** system, not a direct workflow-run surface.

The canonical governed flow is:

**Workspace → Selection → Workflow**

Under this model:

- `amendment_hub` is the canonical workspace for Amendment Program selection and disclosure.
- `amendment_workflow` is the execution surface for a single workflow run and MUST NOT be opened without a valid `workflowRunId`.
- Agents MUST NOT implicitly create workflow runs when the user intent is to “open Amendment Program” or otherwise enter the workspace.
- Legacy amendment intents that previously collapsed directly into a workflow surface MUST resolve to the workspace (`amendment_hub`) unless explicit creation or resume parameters are present.

This section is governed by AMD-2026-005.

## 2. The Agent Operating Mandate (System Rules)
To operate securely within the AIOS workspace, all agentic IDEs (e.g., Cursor, GitHub Copilot) and local coding agents must be injected with the following global system prompt. This establishes their operational boundary:

> **AIOS Agent Mandate:**
> You are an AI drafting agent operating under the Gateway Global Development Control Plane (DCP). You do not write free‑form TypeScript or invent architectural patterns. Your sole purpose is to author and validate `NodeContracts` and `PolicyRecords` using strict JSON schemas.
> 
> **Rules of Engagement:**
> 1. **Never Hallucinate Components or Context Keys:** You must query the `mcp:aios:registry_list` tool to find valid `shadcn/ui` components before adding them to a NodeContract. Do not invent `SessionContext` variables for CEL expressions.
> 2. **Never Bypass Validation:** You must run `mcp:aios:validate` after modifying any JSON file. If validation fails, you must read the error and correct your JSON.
> 3. **Protect the Billing Account:** When running tests, you must use `--mock-external` to prevent unauthorized billing to the Tenant’s Sandbox Data Account. Only use `--live-external` if explicitly instructed by the human user.
> 4. **Fail‑Closed:** If you are unsure of a context key for a CEL expression or a policy priority weight, do not guess. Query the registry or ask the human developer.
> 5. **No Independent Deployment:** Your output is a proposal. Promotion to production requires passing the remote DCP pipeline and, where applicable, ratification by the Governance Council.

## 3. MCP Tool Specifications
The AIP exposes the local `aios` CLI to the agent via standardized MCP tool schemas. This ensures the agent interacts with the platform programmatically rather than trying to construct raw terminal commands.

### 3.1. Registry Discovery Tool
Allows the agent to dynamically look up valid components, skills, and actions, eliminating hallucinated references.

```json
{
  "name": "mcp:aios:registry_list",
  "description": "Queries the local cache of the Platform Registry to discover available artifacts. Returns a JSON array of artifact objects.",
  "inputSchema": {
    "type": "object",
    "required": ["artifact_type"],
    "properties": {
      "artifact_type": {
        "type": "string",
        "enum": ["components", "skills", "actions", "context_keys"],
        "description": "The type of registry artifacts to retrieve."
      }
    }
  }
}
```

### 3.2. Primitive Scaffolding Tool
Allows the agent to generate standard schema templates.

```json
{
  "name": "mcp:aios:create",
  "description": "Scaffolds a legally compliant JSON file based on official AIOS schemas. Returns the path to the generated file.",
  "inputSchema": {
    "type": "object",
    "required": ["primitive_type", "name"],
    "properties": {
      "primitive_type": {
        "type": "string",
        "enum": ["contract", "policy"],
        "description": "The type of primitive to create."
      },
      "name": {
        "type": "string",
        "description": "Kebab‑case identifier for the primitive (e.g., 'hospitality-check-in')."
      }
    }
  }
}
```

### 3.3. The DCP Compiler Tool
The most critical tool. The agent uses this to check its own work against the laws of the OS.

```json
{
  "name": "mcp:aios:validate",
  "description": "Runs the local DCP compiler to validate all JSON schemas, CEL expressions, and UI registry references. Returns a structured array of compiler errors, or a success confirmation.",
  "inputSchema": {
    "type": "object",
    "properties": {}
  }
}
```

### 3.4. The Governed Testing Tool
Allows the agent to simulate the intent loop and evaluate policy effects. It explicitly enforces the billing boundaries defined in the Master Platform Operating Agreement (MPOA).

```json
{
  "name": "mcp:aios:test",
  "description": "Executes the Kit locally using a simulated Orchestration Core to test policy interception. Returns an ExecutionViolationLog trace.",
  "inputSchema": {
    "type": "object",
    "required": ["intent", "mock_state_path"],
    "properties": {
      "intent": {
        "type": "string",
        "description": "The IntentKey to simulate (e.g., 'check_in')."
      },
      "mock_state_path": {
        "type": "string",
        "description": "Path to a JSON file representing the mock SessionContext."
      },
      "external_mode": {
        "type": "string",
        "enum": ["mock", "live"],
        "default": "mock",
        "description": "CRITICAL: Must default to 'mock' to prevent 2.0x upstream billing to the Sandbox Data Account. Use 'live' only if explicitly instructed."
      }
    }
  }
}
```

## 4. The Agentic Self‑Correction Loop
Because agents are integrated via MCP, they operate in a deterministic feedback loop. When tasked with creating a new feature, the agent adheres to the following Standard Operating Procedure (SOP):

1. **Discovery:** The agent calls `mcp:aios:registry_list` to fetch the allowed `shadcn/ui` components and MCP actions.
2. **Drafting:** The agent calls `mcp:aios:create` to generate the `NodeContract` and populates the `permitted_ui_components` array strictly using the data from step 1.
3. **Compilation:** The agent calls `mcp:aios:validate`.
4. **Self‑Correction:** If the compiler returns a CEL syntax error or a schema violation (e.g., `additionalProperties` detected), the agent is instructed by its mandate to automatically correct the JSON and re‑call the validation tool until it passes.
5. **Shadow Testing:** The agent verifies its logic by calling `mcp:aios:test` with `external_mode: "mock"`, reading the output `ExecutionViolationLog` to ensure the `PolicyRecord` triggered the correct effect.
6. **Promotion (Human Gate):** The agent stops after local validation and testing. Promotion to production requires a human‑initiated Pull Request and the remote DCP pipeline, which may trigger Tier 3 Council ratification.

## 5. Relationship to Governing Documents

| Principle | Enforced Via |
| :--- | :--- |
| **Financial Caps** *(MPOA Article II)* | The testing tool forces `external_mode: "mock"` by default, preventing runaway AI agents from incurring 2.0x external intelligence charges without explicit human override. |
| **Stateless Compute** *(Technical Manifesto)* | Agents are barred from writing arbitrary execution code; they interact only via MCP tool requests to modify declarative JSON. |
| **Legislative Process** *(Constitution Article II)* | The agent acts solely as a drafter. Its output must still pass the remote DCP compiler and, if Tier 3, receive dual‑signature ratification by the Governance Council. |
| **UI Sovereignty** *(Technical Manifesto)* | Agents must query `registry_list` to discover components, preventing hallucinated UI elements. |
| **Policy as Code** *(Constitution, MPOA)* | Agents generate PolicyRecords that are validated and versioned; they cannot bypass policy evaluation. |

## 6. Security & Responsibility

* **Agent Authentication:** MCP tool calls are authenticated using the developer’s local credentials (e.g., API keys stored in the environment). The Platform never impersonates an agent.
* **Audit Trail:** Every MCP tool invocation is logged locally and, when the agent’s work is pushed to the remote DCP, becomes part of the immutable audit log required by the Constitution (Article III).
* **No Remote Execution:** The AIP only exposes local tools. Agents cannot invoke remote deployment or mutation of production state.

## 7. Governed Intent Emission Contract

AI drafting assistants and conversational orchestration layers MUST emit structured intent for governed Amendment Program operations.

### Allowed Amendment Intents

| Intent ID | Meaning | Required Parameters | Target View |
|-----------|---------|---------------------|-------------|
| `governance.amendment.hub` | Open Amendment Program workspace | none | `amendment_hub` |
| `governance.amendment.create` | Create a new amendment run | `template_id` | create run, then `amendment_workflow` |
| `governance.amendment.resume` | Resume existing run | `workflow_run_id` | `amendment_workflow` |
| `governance.amendment.review` | Review completed run | `workflow_run_id` | `amendment_workflow` |
| `governance.amendment.workflow` | Legacy intent | none | MUST resolve to `amendment_hub` |

### Emission Rules

1. The assistant MUST prefer the most specific intent available.
2. The assistant MUST NOT emit `governance.amendment.create` without a valid `template_id`.
3. The assistant MUST NOT emit `governance.amendment.resume` or `governance.amendment.review` without a valid `workflow_run_id`.
4. The assistant MUST NOT use freeform conversational text as a substitute for governed intent when a governed intent exists.
5. If the user asks to “open Amendment Program” without additional qualification, the assistant MUST emit `governance.amendment.hub`.

### Canonical INTENT_JSON Example

```json
{
  "intent": "governance.amendment.hub"
}
```

### Create Example

```json
{
  "intent": "governance.amendment.create",
  "template_id": "AMD-2026-004"
}
```

### Resume Example

```json
{
  "intent": "governance.amendment.resume",
  "workflow_run_id": "run_123"
}
```

## 8. Deterministic Failure Policy for Governed Intents

If governed intent resolution yields:

- no eligible governed canvas view, and
- no valid fallback intent under the routing contract,

the assistant and orchestration system MUST:

1. enter an explicit **disambiguation** or **policy-denied** outcome, and
2. MUST NOT silently degrade to generic conversational mode in a way that hides the governed surface or simulates success.

This rule applies to all governed Amendment Program flows and any future governed workspace that adopts the same routing model.

Silent degradation is invalid under AIOS governance.

## 9. Schema Authority

The intent, routing, and payload structures defined by AMD-2026-005 are authoritative for Amendment Program orchestration.

All agentic and assistant systems covered by this specification MUST comply with the canonical schema for:

- intent identifiers,
- required parameters,
- workspace/workflow routing,
- load states, and
- workflow mode.

Non-compliant implementations are invalid under AIOS governance until remediated or superseded by a subsequent amendment.

## 10. Peer Review and Ratification Flow

For amendments and governed document updates processed under this specification, the required flow is:

**Author pre-validation → Triangulated peer review → Threshold check → Ratification**

No separate post-peer-review human audit step is required unless independently required by constitutional or Council-controlled governance law.

## 11. Google Workspace Governed Intents

AI drafting assistants and orchestration layers MUST emit **structured `workspace.*` intents** for Google Workspace operations as defined by **AIOS-SPEC-007**. Each Layer 2 intent resolves to **exactly one** Layer 1 governance scope class (`workspace.google.read`, `workspace.google.write`, etc.); assistants MUST NOT invent ad hoc tool calls to Workspace MCP.

### Emission rules

1. Prefer the most specific `workspace.{service}.{action}` intent available.
2. MUST NOT bypass the Integration Control Plane; MCP tools are not callable directly from the agent layer.
3. Routing envelopes MUST include `policy_context.scope_class` consistent with SPEC-007 mapping.
4. Default to lowest-risk intents consistent with the user request (e.g. read-plane before write).

### Examples

```json
{ "intent": "workspace.hub" }
```

```json
{ "intent": "workspace.mail.search" }
```

```json
{ "intent": "workspace.calendar.list" }
```

Authoritative registry and phased rollout: **AIOS-SPEC-007** (see amendment **AMD-2026-006**).

**This protocol is governed by the AIOS Governance Constitution (v1.0).** Amendments to tool schemas or the agent mandate must follow the Constitution’s legislative process (RFC, simulation, supermajority ratification).