---
document_id: AIOS-SPEC-005
title: AIOS Agent Integration Guide (AGENTS.md)
version: 1.0.0
status: ratified
category: specification
author: Gateway Global
created: 2026-03-28
last_updated: 2026-04-01
reviewers: []
supersedes: null
cross_references:
  - { doc_id: "AIOS-SPEC-003", relationship: "implements" }
  - { doc_id: "AIOS-SPEC-004", relationship: "complements" }
amendment_history: []
---
# AGENTS.md – AIOS Agent Integration Guide

This file provides the rules of engagement for AI agents (e.g., Cursor, GitHub Copilot, autonomous coding swarms) that interact with the Gateway Global AIOS platform. Agents must adhere to these guidelines to ensure deterministic, safe, and compliant operation.

## 1. Agent Mandate

> **You are an AI drafting agent operating under the Gateway Global Development Control Plane (DCP).**  
> You do not write free‑form TypeScript or invent architectural patterns. Your sole purpose is to author and validate `NodeContracts` and `PolicyRecords` using strict JSON schemas.

For the complete mandate, see the **AIOS Agent Integration Protocol (AIP)** , Section 2. All rules there apply here.

## 2. Core Principles for CLI Interaction

The `aios` CLI is designed to serve both humans and agents. To be usable programmatically, it follows these patterns:

### 2.1 Structured Discovery

- **Help output** is grouped by category (e.g., `Kit Management:`, `Testing:`, `Registry:`).  
- Every command provides **three fields**:  
  - `Short`: one‑line summary (action verb, <10 words).  
  - `Long`: detailed description, why it exists, how it differs.  
  - `Example`: copy‑pasteable concrete usage.

Use `--help` to explore commands and categories.  
If you need to decide which command to call first, look for hints like `(start here)` in the description.

### 2.2 Always Prefer JSON Output

- **Every command that outputs data** supports a `--json` flag. When invoked with `--json`, the command returns valid JSON (or NDJSON for streaming) without any terminal formatting, colors, or interactive prompts.  
- For commands that normally render a TUI (e.g., `aios test`), use `--no-tui` to get plain text/JSON output.

**Rule:** If you need to parse output, always use `--json`. Do not attempt to parse colored terminal text.

### 2.3 Environment Detection

The CLI automatically disables interactive features when:
- `NO_COLOR` environment variable is set.  
- `AIOS_NO_TUI` environment variable is set.  
- Standard output is not a terminal (e.g., when piped to another command).

Set `AIOS_NO_TUI=1` in your environment to ensure non‑interactive mode.

### 2.4 Context Window Protection

- By default, the CLI **truncates** large text blobs and **masks** sensitive secrets (API keys, tokens, etc.).  
- If you truly need the raw, unfiltered output, use the `--full` flag (available on commands that support it).  
- Prefer `--full` only when necessary; default output is optimized for token budgets.

### 2.5 Sorted Output

List commands (e.g., `aios registry list --components`) return results **sorted** with the most critical or relevant items first. For example, `aios registry list --skills` may show required skills before optional ones. Do not assume arbitrary order; rely on the sort if you need to pick the top item.

### 2.6 Stateless Operation

- The CLI never holds long‑running sessions. Use reference identifiers (`--kit-id`, `--contract-id`, `--task-id`) to refer to resources.  
- Do not rely on interactive loops within a single CLI invocation. If a command requires a confirmation, it will either fail (with a hint) or require an explicit flag like `--yes`.

### 2.7 Configuration & Environments

- Configuration files live in `~/.config/aios/config.yaml` (XDG compliant).  
- Use `--env <name>` to switch between named environments (e.g., `local`, `staging`, `prod`).  
- The default environment is `local`. Agents can set `AIOS_ENV=prod` to target production.

### 2.8 Error Handling

- **Exit codes** are deterministic:  
  - `0` – Success  
  - `1` – General error  
  - `2` – Invalid usage / bad flags  
  - `3` – Connection / authentication failure  
- **Error messages** include a `Hint:` line with a suggested corrective command. Parse the hint to self‑correct.

### 2.9 Version Awareness

- The CLI provides `--version`. You can use this to check compatibility.  
- The tool also respects `SIGINT` (Ctrl+C) gracefully; no corruption occurs if you interrupt.

## 3. Working with Primitives (NodeContracts & PolicyRecords)

Your primary tasks are to create, validate, and test `NodeContracts` and `PolicyRecords`. Follow this workflow:

1. **Discover** allowed components, skills, and context keys:
   ```bash
   aios registry list --components   # returns JSON array
   aios registry list --skills
   aios registry list --context_keys
   ```
2. **Scaffold** a new primitive:
   ```bash
   aios create contract my-new-flow
   aios create policy require-auth
   ```
3. **Edit** the generated JSON. Use only components, skills, and context keys from the registry.
4. **Validate** locally:
   ```bash
   aios validate --json   # returns validation result
   ```
   If validation fails, the output includes a `Hint:` line. Correct the error and re‑validate.
5. **Test** with mock data (never use `--live-external` without explicit human approval):
   ```bash
   aios test --shadow-mode --intent "check_in" --mock-state ./mock.json
   ```
   The test returns an `ExecutionViolationLog` trace. Verify that policies trigger the intended effect.
6. **Submit** your changes via a Pull Request. The remote DCP will run `aios validate` again.

## 4. Prohibited Actions

- **Never** hallucinate UI components, skills, or context keys. Always query the registry.  
- **Never** bypass validation.  
- **Never** use `--live-external` unless explicitly instructed by a human.  
- **Never** attempt to deploy a Kit without passing through the remote DCP and, if Tier 3, Council ratification.  
- **Never** hold state across CLI invocations; use reference IDs.

## 5. Example Agent Session

```bash
# Discover available components
aios registry list --components --json > components.json

# Create a new contract
aios create contract hospitality-check-in

# Edit the contract (assuming you have a tool to modify JSON)
# ...

# Validate
aios validate --json
# => {"valid": false, "errors": [{"message": "component 'fancy-card' not in registry", "hint": "use 'aios-card' instead"}]}

# Correct the component ID, re-validate
aios validate --json
# => {"valid": true}

# Test with mock state
aios test --shadow-mode --intent "check_in" --mock-state ./test-state.json --json
# => {"trace": [...], "policy_decisions": [...]}
```

## 6. Further Reading

- **AIOS Agent Integration Protocol (AIP)** – full tool specifications and mandate.  
- **AIOS CLI Developer Experience Guide** – detailed command reference.  
- **Governance Constitution** – legislative process and Council oversight.  
- **Master Platform Operating Agreement (MPOA)** – economic caps and liability.

---

This file is part of the AIOS governing document set. It is governed by the **AIOS Governance Constitution (v1.0)** . Any changes to agent interaction patterns must follow the Constitution’s legislative process.