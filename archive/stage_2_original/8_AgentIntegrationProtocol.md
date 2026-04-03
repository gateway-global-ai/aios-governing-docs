# AIOS Agent Integration Protocol (AIP) v1.0.0

## 1. Architectural Purpose
The Agent Integration Protocol (AIP) defines the exact interface and constraints for autonomous and semi‑autonomous coding agents operating within the Gateway Global AIOS ecosystem. It provides the machine‑readable instructions for agents to generate, test, and deploy platform primitives.

Agents operating under this protocol act exclusively as **drafters** as defined by the *Governance Constitution (Article II: Legislative Process)*. They cannot unilaterally deploy code; they can only invoke the AIOS Command Line Interface (CLI) via the Model Context Protocol (MCP) to generate legally compliant JSON schemas. Every artifact an agent creates must pass the DCP compiler and, if classified as Tier 3, requires human Council ratification.

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

**This protocol is governed by the AIOS Governance Constitution (v1.0).** Amendments to tool schemas or the agent mandate must follow the Constitution’s legislative process (RFC, simulation, supermajority ratification).