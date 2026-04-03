---
document_id: AIOS-SPEC-001
title: AIOS NodeContract Specification
version: 1.0.0
status: ratified
category: specification
author: Gateway Global
created: 2026-03-25
last_updated: 2026-04-01
reviewers: []
supersedes: null
cross_references:
  - { doc_id: "AIOS-CORE-001", relationship: "implements" }
  - { doc_id: "AIOS-CORE-002", relationship: "constrained_by" }
  - { doc_id: "AIOS-SPEC-002", relationship: "extends" }
amendment_history: []
---
# AIOS NodeContract Specification v1.0.0

## 1. Architectural Purpose

The `NodeContract` is the primary unit of **declarative law** within the AIOS. It defines a bounded interaction node: the intents it serves, the Skills it may invoke, the UI components it may render, and the policies that govern its execution.  

A NodeContract is **not** a script or a workflow; it is a **declarative specification** that the Stateful Shell compiles into runtime behavior. By enforcing strict boundaries at the schema level, the NodeContract prevents AI hallucinations, UI fragmentation, and unauthorized tool access—turning the Constitution’s principles into machine‑enforced rules.

Every NodeContract is a **proposal** in the legislative pipeline defined by the **Governance Constitution** (Article II). It is drafted by a human developer or an AI coding agent acting under the **Development Control Plane (DCP)**, and it must pass the DCP’s deterministic compiler before it can be merged into a Kit and deployed.

---

## 2. Relationship to Governing Documents

| Principle | Enforced Via |
|-----------|--------------|
| **Separation of Powers** | NodeContracts are authored by the Lawmaking Authority (via DCP) but cannot execute until the Judicial Authority (Policy Engine) evaluates them at runtime. |
| **UI Sovereignty** | `permitted_ui_components` whitelists only components from the canonical `shadcn/ui` registry. Unlisted components are rejected at compile time. |
| **Stateless Compute** | NodeContracts reference `required_skills`, which are stateless primitives that return typed results and own no session state. |
| **Deterministic Execution** | All fields are bounded; `additionalProperties: false` ensures the NodeContract cannot contain undeclared properties that would introduce non‑determinism. |
| **State Conflict Resolution** | `state_conflict_weight` determines priority when multiple Kits attempt to mutate the same state object. |
| **Policy as Code** | `policy_tags` are evaluated by the Policy Engine to apply risk tiers, compliance rules, and confirmation requirements. |

---

## 3. The JSON Schema Definition

This schema is hosted at `{{GATEWAY_SCHEMA_BASE_URL}}/node-contract.json` and is used by the DCP compiler to validate all incoming NodeContract proposals. **No NodeContract may be merged into a Kit without passing this validation.**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "{{GATEWAY_SCHEMA_BASE_URL}}/node-contract.json",
  "title": "AIOS Node Contract",
  "description": "Defines the strictly bounded execution environment for a specific intent.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "node_id",
    "version",
    "supported_intents",
    "participating_roles",
    "required_skills",
    "allowed_actions",
    "permitted_ui_components",
    "voice_modes",
    "expected_outcome",
    "performance_budget",
    "telemetry_hooks",
    "policy_tags",
    "state_conflict_weight"
  ],
  "properties": {
    "node_id": {
      "type": "string",
      "pattern": "^[a-z0-9][a-z0-9\\-\\.]{2,80}$",
      "description": "Stable, globally unique node identifier (e.g., hospitality-check-in-v1)."
    },
    "version": {
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$",
      "description": "Semantic version of the node contract."
    },
    "description": { 
      "type": "string", 
      "maxLength": 2000 
    },
    "supported_intents": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/IntentRef" },
      "description": "The exact IntentKeys this node can lawfully handle."
    },
    "participating_roles": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/RoleRef" },
      "description": "Roles authorized to participate when this node is active."
    },
    "required_skills": {
      "type": "array",
      "items": { "$ref": "#/$defs/SkillRef" },
      "description": "Computational capabilities required to produce outcomes."
    },
    "allowed_actions": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/ActionRef" },
      "description": "MCP endpoints and system actions permitted under this node."
    },
    "required_knowledge_sources": {
      "type": "array",
      "items": { "$ref": "#/$defs/KnowledgeSourceRef" },
      "description": "Strict whitelist of data sources the node may access."
    },
    "permitted_ui_components": {
      "type": "array",
      "items": { "$ref": "#/$defs/UIComponentRef" },
      "description": "Whitelisted shadcn/ui components the Stateful Shell may render. Unlisted components are rejected at compile time."
    },
    "voice_modes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "enum": ["voice_ptt", "voice_handsfree", "chat_only", "hybrid_voice_canvas"]
      },
      "description": "Voice and chat modes this node physically supports."
    },
    "expected_outcome": {
      "$ref": "#/$defs/OutcomeSpec"
    },
    "performance_budget": {
      "$ref": "#/$defs/PerformanceBudget"
    },
    "telemetry_hooks": {
      "$ref": "#/$defs/TelemetryHooks"
    },
    "policy_tags": {
      "type": "array",
      "items": { 
        "type": "string", 
        "maxLength": 64 
      },
      "description": "Tags evaluated by the Policy Engine (e.g., pii, write_action, external_comm)."
    },
    "state_conflict_weight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 100,
      "description": "Priority weight used by the OS State Conflict Resolution Protocol to resolve deadlocks."
    },
    "journey_phase_constraints": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["discovery", "consideration", "conversion", "post_sale", "support"]
      },
      "description": "Specific phases where this node is valid."
    }
  },
  "$defs": {
    "IntentRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["intent_id"],
      "properties": {
        "intent_id": { "type": "string", "pattern": "^[a-z0-9][a-z0-9_\\-]{2,60}$" },
        "min_confidence": { "type": "number", "minimum": 0, "maximum": 1, "default": 0.75 }
      }
    },
    "RoleRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["role_id"],
      "properties": {
        "role_id": { "type": "string", "pattern": "^[a-z0-9][a-z0-9_\\-]{2,60}$" },
        "side": { "type": "string", "enum": ["customer", "agent", "system"] }
      }
    },
    "SkillRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["skill_id"],
      "properties": {
        "skill_id": { "type": "string", "pattern": "^[a-z0-9][a-z0-9_\\-]{2,80}$" },
        "version_range": { "type": "string" }
      }
    },
    "ActionRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["action_id", "effect"],
      "properties": {
        "action_id": { "type": "string", "pattern": "^[a-z0-9][a-z0-9_\\-\\.]{2,120}$" },
        "effect": { "type": "string", "enum": ["read", "write", "delete", "invoke", "render"] },
        "requires_confirmation": { "type": "boolean", "default": false },
        "risk_level": { "type": "string", "enum": ["low", "medium", "high"], "default": "low" }
      }
    },
    "KnowledgeSourceRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["source_id", "access"],
      "properties": {
        "source_id": { "type": "string", "pattern": "^[a-z0-9][a-z0-9_\\-\\.]{2,80}$" },
        "access": { "type": "string", "enum": ["none", "read", "write"], "default": "read" }
      }
    },
    "UIComponentRef": {
      "type": "object",
      "additionalProperties": false,
      "required": ["component_id"],
      "properties": {
        "component_id": { "type": "string", "description": "Canonical shadcn registry item name." },
        "variants_allowed": { "type": "array", "items": { "type": "string" } }
      }
    },
    "OutcomeSpec": {
      "type": "object",
      "additionalProperties": false,
      "required": ["outcome_id", "success_criteria"],
      "properties": {
        "outcome_id": { "type": "string", "pattern": "^[a-z0-9][a-z0-9_\\-]{2,80}$" },
        "success_criteria": { "type": "array", "minItems": 1, "items": { "type": "string", "maxLength": 200 } },
        "failure_modes": { "type": "array", "items": { "type": "string", "maxLength": 240 } }
      }
    },
    "PerformanceBudget": {
      "type": "object",
      "additionalProperties": false,
      "required": ["p95_end_to_end_ms", "p95_first_canvas_ms", "max_bundle_kb"],
      "properties": {
        "p95_end_to_end_ms": { "type": "integer", "minimum": 50, "maximum": 60000 },
        "p95_first_canvas_ms": { "type": "integer", "minimum": 50, "maximum": 60000 },
        "max_bundle_kb": { "type": "integer", "minimum": 50, "maximum": 5000 },
        "max_tool_calls": { "type": "integer", "minimum": 0, "maximum": 50, "default": 8 }
      }
    },
    "TelemetryHooks": {
      "type": "object",
      "additionalProperties": false,
      "required": ["events"],
      "properties": {
        "events": { "type": "array", "minItems": 1, "items": { "type": "string", "pattern": "^[a-z0-9][a-z0-9_\\-\\.]{2,80}$" } },
        "metrics": { "type": "array", "items": { "type": "string" } },
        "traces": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

---

## 4. Reference Implementation

Below is a valid `NodeContract` for a hospitality check‑in flow. This example demonstrates how a developer or an AI coding agent would author a compliant proposal under the DCP.

```json
{
  "node_id": "hospitality-check-in-v1",
  "version": "1.0.0",
  "description": "Governs the customer check-in intent, verifying identity and issuing a digital room key via Cloudbeds.",
  "supported_intents": [
    { "intent_id": "check_in", "min_confidence": 0.85 }
  ],
  "participating_roles": [
    { "role_id": "customer", "side": "customer" }
  ],
  "required_skills": [
    { "skill_id": "verify_identity", "version_range": "^2.0.0" },
    { "skill_id": "mcp_cloudbeds_booking", "version_range": "^1.1.0" }
  ],
  "allowed_actions": [
    { 
      "action_id": "mcp.cloudbeds.reservation.read", 
      "effect": "read", 
      "risk_level": "low" 
    },
    { 
      "action_id": "mcp.cloudbeds.reservation.checkin", 
      "effect": "write", 
      "requires_confirmation": true, 
      "risk_level": "high" 
    }
  ],
  "required_knowledge_sources": [],
  "permitted_ui_components": [
    { "component_id": "aios-check-in-form", "variants_allowed": ["default"] },
    { "component_id": "aios-confirmation-dialog", "variants_allowed": ["destructive", "default"] }
  ],
  "voice_modes": ["hybrid_voice_canvas", "chat_only"],
  "expected_outcome": {
    "outcome_id": "check_in_complete",
    "success_criteria": ["Reservation status updated to 'Checked In'", "Digital key provisioned"],
    "failure_modes": ["Reservation not found", "Identity verification failed"]
  },
  "performance_budget": {
    "p95_end_to_end_ms": 2500,
    "p95_first_canvas_ms": 800,
    "max_bundle_kb": 150,
    "max_tool_calls": 4
  },
  "telemetry_hooks": {
    "events": ["checkin.started", "checkin.identity_verified", "checkin.completed", "checkin.failed"]
  },
  "policy_tags": ["requires_pii", "financial_transaction"],
  "state_conflict_weight": 90,
  "journey_phase_constraints": ["conversion"]
}
```

---

## 5. Compiler Enforcement (DCP Pipeline)

When a NodeContract proposal is submitted as part of a Pull Request (or through an AI agent’s automated draft), the Development Control Plane (DCP) executes the following deterministic checks:

1. **Schema Validation**  
   The JSON must strictly validate against the `node-contract.json` schema. Any `additionalProperties` will cause rejection.

2. **Registry Cross‑Reference**  
   Every component listed in `permitted_ui_components` is verified against the canonical `shadcn/ui` component registry. If a component does not exist, the build fails.

3. **Skill & Action Resolution**  
   All referenced `skill_id` and `action_id` values are checked against the Platform’s registered Skills and MCP endpoints. Unregistered references are rejected.

4. **Tier 3 Elevation Check**  
   If any `ActionRef` has `risk_level: "high"` or if the node touches Voice Runtime, credential brokers, or core Kernel mutation logic, the proposal is automatically classified as **Tier 3**.  
   – The merge is frozen.  
   – The proposal requires **dual‑signature ratification** by at least one OS Kernel Team member AND one Digital Governance Officer, as mandated by the Governance Constitution (Article II, Section 2).

5. **Performance Budget Validation**  
   The `performance_budget` values are compared against platform‑wide defaults; overly permissive budgets may trigger additional review (e.g., if `max_bundle_kb` exceeds 500 KB, the DCP may flag it for architectural review).

6. **Immutable Logging**  
   Every validation result, including rejections and approvals, is recorded in the DCP’s immutable audit log. This log is accessible to the Governance Council and forms part of the system’s transparency guarantees.

---

## 6. Relationship to Kits

A `NodeContract` is always part of a **Kit**—a versioned, signed bundle that may also contain Policies and Skills. The Kit is the distributable unit that is listed in the Marketplace and installed by Tenants. The NodeContract alone is not deployable; it must be included in a Kit with a valid manifest and cryptographic provenance.

For Kit certification requirements, see the **Marketplace Terms & Vendor Onboarding** document (in development). For the Policy schema, see the forthcoming **PolicyRecord Specification**.

---

**This specification is governed by the AIOS Governance Constitution (v1.0).**  
Amendments to the schema or validation rules must follow the Constitution’s legislative process, including simulation, public comment, and supermajority ratification.