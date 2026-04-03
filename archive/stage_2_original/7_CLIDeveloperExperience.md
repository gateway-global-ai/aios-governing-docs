You're absolutely right about the billing trap. A developer or CI pipeline running frequent shadow‑mode tests should not be penalized for good testing practices. I’ll incorporate the distinction between **mock** and **live** external calls.

Below is the final, refined CLI guide with that addition. After this, we’re ready to draft the **Agent Integration Protocol (AIP)** .

---

# AIOS CLI Developer Experience Guide v1.0.0 (Final)

## 1. Architectural Purpose

The `aios` Command Line Interface (CLI) is the **local enforcement arm** of the Development Control Plane (DCP). It serves as the primary developer interface—for both human engineers and AI coding agents—to build, test, and package Execution Kits for the Gateway Global AIOS.

The CLI ensures that **no malformed primitive can ever be committed to version control**. By shifting governance to the local development environment, the CLI enforces:

- JSON schema compliance (against the canonical `NodeContract` and `PolicyRecord` schemas)
- UI registry cross‑referencing (against the live `shadcn/ui` Platform Registry)
- CEL expression linting (syntax, infinite loops, valid context keys)

For AI coding agents, the CLI acts as a **physical sandbox**: agents do not write arbitrary code; they execute `aios` commands to generate legally compliant JSON.

---

## 2. Core Command Reference

### `aios init <kit-name>`
Initializes a new Kit workspace.

- **Outputs:** `contracts/`, `policies/`, `skills/`, `kit-manifest.json`
- **Validation:** Enforces kebab‑case, alphanumeric naming.

### `aios create <primitive-type> <name>`
Scaffolds a compliant JSON template.

- **Primitive Types:** `contract`, `policy` (more coming)
- **Behavior:** Pre‑populates all required fields, eliminating syntax hallucinations.

### `aios registry list [--components|--skills|--actions]`
Queries the local cache of the Platform Registry.

- **Example:** `aios registry list --components` → JSON array of approved `shadcn/ui` components with variants.
- **Purpose:** Enables developers and agents to discover valid IDs without guessing.

### `aios validate`
The local DCP compiler, identical to remote CI/CD.

- **Checks:**
  1. JSON schema conformance
  2. UI component registry cross‑reference
  3. CEL expression linting & context key validation
- **Enforcement:** Bound to `pre-commit`; blocks commits on failure.

### `aios test --shadow-mode`
Executes the Kit locally using a simulated Orchestration Core.

**Usage:**  
`aios test --shadow-mode --intent "check_in" --mock-state ./tests/mock-auth.json`

**Modes (critical):**
- **`--mock-external` (default):** All external MCP tool calls (e.g., live search, premium models) return deterministic, pre‑recorded mock responses. **Cost: $0.00.**  
- **`--live-external`:** Actually invokes live vendor APIs. This uses real upstream resources and debits the developer’s **Sandbox Data Account** at the standard 2.0× multiplier.

**Output:** An `ExecutionViolationLog` trace showing which policies evaluated to `allow`, `deny`, or `require_confirmation`.

**Economic Boundary (MPOA Article II):** Shadow Mode never mutates production state. Live external calls are billed only when explicitly opted in.

### `aios build && aios sign`
Compiles and cryptographically signs the Kit.

- `aios build`: Minifies JSON primitives, bundles them, computes a content hash.
- `aios sign`: Attaches the developer’s (or tenant’s) private key to the manifest. Keys are managed by the tenant/vendor; the Platform never holds private keys (BYOK, MPOA Article V).
- **Governance Link:** The signature enables provenance tracking and liability boundaries (MPOA Article II).

---

## 3. The Governed Workflow (Human & Agent)

### Step 1: Initialization & Scaffolding
```bash
aios init vip-upgrade-kit
cd vip-upgrade-kit
aios create contract vip-upgrade-flow
aios create policy require-vip-status
```

### Step 2: Drafting & Local Validation
Edit the JSON, then run:
```bash
aios validate
```
If an agent uses an invalid component, CLI errors with the exact missing ID. The agent can query `aios registry list --components` to correct.

### Step 3: Shadow Testing (Mock by Default)
```bash
aios test --shadow-mode --intent "request_upgrade" --mock-state ./tests/mock-vip.json
```
The CLI runs entirely offline, using mock responses. No cost, no external API calls.

To test real integration (e.g., to validate a new vendor API endpoint), the developer explicitly uses:
```bash
aios test --shadow-mode --live-external --intent "request_upgrade" ...
```
This triggers billing, but is used sparingly (e.g., before final release).

### Step 4: Promotion to the Remote DCP
```bash
aios build
aios sign --key ./keys/tenant-private.pem
git push origin main
```
The remote DCP re‑runs `aios validate`. If the contract contains `risk_level: "high"` or touches Tier‑3 areas, the PR is frozen until the Governance Council provides dual‑signature ratification (Constitution Article II, Section 2).

---

## 4. MCP Integration (For AI Agents)

The CLI exposes its commands as **Model Context Protocol (MCP) Tools**. An AI agent (e.g., in Cursor) can call:

- `mcp:aios:init`
- `mcp:aios:create`
- `mcp:aios:registry_list`
- `mcp:aios:validate`
- `mcp:aios:test` (with parameters for `--mock-external` / `--live-external`)
- `mcp:aios:build`
- `mcp:aios:sign`

This creates a closed‑loop system where the OS tooling physically governs the AI’s ability to write code. The agent cannot bypass validation; it can only request the CLI to perform actions that comply with the governing schemas.

*(For the complete technical specification on tool discovery, invocation, and response schemas, refer to the **Agent Integration Protocol (AIP)** document.)*

---

## 5. Relationship to Governing Documents

| Document | Section | How the CLI Enforces It |
|----------|--------|--------------------------|
| **Technical Manifesto** | Art III (DCP), Art II (UI Sovereignty) | `aios validate` enforces component registry and stateless compute boundaries. |
| **MPOA** | Art II (Shadow Mode), Art V (BYOK) | `aios test` respects billing boundaries (mock default); `aios sign` aligns with BYOK. |
| **Governance Constitution** | Art II (Legislative Process), Art III (Judicial) | CLI detects Tier‑3 changes and flags for Council ratification. |

---

**This guide is governed by the AIOS Governance Constitution (v1.0).**  
Changes to CLI commands or validation rules must follow the Constitution’s legislative process (RFC, simulation, supermajority ratification).