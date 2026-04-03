---
document_id: AIOS-SPEC-002
title: AIOS PolicyRecord Specification
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
  - { doc_id: "AIOS-CORE-003", relationship: "implements" }
  - { doc_id: "AIOS-SPEC-001", relationship: "complements" }
amendment_history: []
---
Below is the revised **PolicyRecord Specification**, rewritten to align with your governing documents and vision. Changes include:

- Removed references to “coding swarms” and reframed PolicyRecords as artifacts authored by developers or AI agents under the **Development Control Plane (DCP)**.
- Explicitly tied to the **Governance Constitution** (Judicial Authority, Legislative Process) and the **MPOA** (liability, data sovereignty).
- Clarified the role of the **Policy Engine** as the central enforcement point.
- Updated terminology to match the glossary (e.g., “Stateful Shell”).
- Strengthened the explanation of `failure_mode: fail_open` restrictions and Tier 3 elevation.
- Added a note on policy precedence and relationship to Kits.

The JSON schema remains largely intact but its descriptions have been refined for consistency.

---

# AIOS PolicyRecord Specification v1.0.0

## 1. Architectural Purpose

The `PolicyRecord` is the primary instrument of the **Judicial Authority** within the AIOS. While a `NodeContract` defines *what* is computationally possible for a given intent, the `PolicyRecord` defines *whether* that computation is permitted at runtime—considering identity, role, risk tier, context, and compliance requirements.

Policies are evaluated by the **Policy Engine**, a centralized control plane that intercepts every execution packet before it reaches the Compute Kernel. The Policy Engine operates on a **default‑deny, fail‑closed** posture: if a policy evaluation fails (due to missing context, a syntax error, or an explicit `deny`), the execution is halted, the LLM is bypassed, and the system deterministically falls back to a safe UI.

This architecture implements the **Policy Supremacy** principle from the Technical Manifesto: no compute occurs unless explicitly authorized by the governing policies.

---

## 2. Relationship to Governing Documents

| Principle | Enforced Via |
|-----------|--------------|
| **Policy Supremacy** (Technical Manifesto) | The Policy Engine evaluates `PolicyRecord` before any payload reaches the Compute Kernel. An LLM cannot circumvent a policy block. |
| **Liability Boundaries** (MPOA Article III) | If a Vendor Kit requests an action that a `PolicyRecord` blocks, the Platform incurs zero liability—the system operated as designed. |
| **Data Sovereignty & Audit** (MPOA Article V) | `audit_level` controls what data is written to the immutable ExecutionViolationLog, enabling PII redaction and compliance with GDPR/CCPA. |
| **Judicial Authority** (Governance Constitution Article III) | PolicyRecords are the primary tool for the Judicial Authority to interpret and enforce the law. |
| **Legislative Process** (Governance Constitution Article II) | PolicyRecords are authored via the DCP. Any policy targeting core Kernel logic or using `failure_mode: fail_open` triggers Tier 3 mandatory ratification (dual‑signature). |

---

## 3. The JSON Schema Definition

This schema is hosted at `{{GATEWAY_SCHEMA_BASE_URL}}/policy-record.json` and is strictly enforced by the Development Control Plane (DCP) compiler.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "{{GATEWAY_SCHEMA_BASE_URL}}/policy-record.json",
  "title": "AIOS Governance Policy Record",
  "description": "Defines the strictly bounded rules under which Contracts and Actions are permitted to execute.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "policy_id",
    "version",
    "targets",
    "conditions",
    "effect",
    "priority",
    "audit_level",
    "failure_mode"
  ],
  "properties": {
    "policy_id": {
      "type": "string",
      "pattern": "^[a-z0-9][a-z0-9\\-\\.]{2,80}$",
      "description": "Stable, globally unique policy identifier (e.g., finance-require-auth-v1)."
    },
    "version": {
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$",
      "description": "Semantic version of the policy record."
    },
    "description": {
      "type": "string",
      "maxLength": 2000,
      "description": "Human‑readable explanation of the policy’s purpose and scope."
    },
    "targets": {
      "type": "object",
      "additionalProperties": false,
      "description": "The exact scope to which this policy applies. At least one array must be populated.",
      "properties": {
        "node_ids": {
          "type": "array",
          "items": { "type": "string" },
          "description": "List of NodeContract IDs this policy applies to."
        },
        "action_ids": {
          "type": "array",
          "items": { "type": "string" },
          "description": "List of action IDs (MCP endpoints or system actions) this policy applies to."
        },
        "policy_tags": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Tags (e.g., 'financial_transaction') that this policy matches."
        }
      }
    },
    "conditions": {
      "type": "object",
      "additionalProperties": false,
      "required": ["cel_expression"],
      "properties": {
        "cel_expression": {
          "type": "string",
          "description": "Common Expression Language (CEL) string evaluated against the OS SessionContext. Must return a boolean."
        },
        "required_context_keys": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Variables the Policy Engine must inject into the CEL evaluator (e.g., 'session.is_authenticated')."
        }
      }
    },
    "effect": {
      "type": "string",
      "enum": ["allow", "deny", "require_confirmation", "escalate_to_hitl"],
      "description": "The deterministic outcome if the CEL expression evaluates to true."
    },
    "priority": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000,
      "description": "Resolution weight. If multiple policies match, the highest priority dictates the final effect."
    },
    "audit_level": {
      "type": "string",
      "enum": ["minimal", "standard", "verbose", "strict_redaction"],
      "description": "Controls what data is written to the immutable ExecutionViolationLog. 'strict_redaction' ensures PII is excluded."
    },
    "failure_mode": {
      "type": "string",
      "enum": ["fail_closed", "fail_open"],
      "default": "fail_closed",
      "description": "System behavior if the CEL expression crashes or required context keys are missing. fail_open is highly restricted and triggers Tier 3 review."
    },
    "fallback_directive": {
      "type": "object",
      "additionalProperties": false,
      "required": ["ui_component"],
      "properties": {
        "ui_component": {
          "type": "string",
          "description": "Canonical UI component to render when the policy denies or escalates."
        },
        "tts_message": {
          "type": "string",
          "description": "Optional text‑to‑speech message to accompany the fallback UI."
        }
      },
      "description": "Optional safe fallback state if the effect is 'deny' or escalation occurs."
    }
  }
}
```

---

## 4. Reference Implementation

Below is a valid `PolicyRecord` designed to intercept any NodeContract executing an action tagged with `financial_transaction` (like the `hospitality-check-in-v1` node we defined earlier). It ensures that the action cannot proceed unless the user is fully authenticated and explicitly confirms the action.

```json
{
  "policy_id": "global-finance-auth-gate-v1",
  "version": "1.0.0",
  "description": "Ensures any action tagged as a financial transaction requires strict authentication and user confirmation.",
  "targets": {
    "node_ids": [],
    "action_ids": [],
    "policy_tags": ["financial_transaction"]
  },
  "conditions": {
    "cel_expression": "session.is_authenticated == true && session.auth_assurance_level >= 2",
    "required_context_keys": ["session.is_authenticated", "session.auth_assurance_level"]
  },
  "effect": "require_confirmation",
  "priority": 900,
  "audit_level": "strict_redaction",
  "failure_mode": "fail_closed",
  "fallback_directive": {
    "ui_component": "aios-auth-gate-overlay",
    "tts_message": "For your security, please verify your identity to complete this transaction."
  }
}
```

---

## 5. Compiler Enforcement (DCP Pipeline)

When a `PolicyRecord` is submitted as part of a Pull Request (or an AI agent’s automated draft), the Development Control Plane (DCP) executes the following deterministic checks:

1. **Schema Validation**  
   The JSON must strictly validate against `policy-record.json`. Any `additionalProperties` will cause rejection.

2. **CEL Syntax Linting**  
   The DCP parses the `cel_expression` using a standard CEL compiler to ensure:
   - No syntax errors.
   - All variables used are either built‑in or listed in `required_context_keys`.
   - The expression returns a boolean.

3. **Context Key Verification**  
   The `required_context_keys` array is cross‑referenced against the Platform’s allowed `SessionContext` schema. If a policy requests a key that the OS does not track (e.g., `session.user_social_security_number`), compilation fails.

4. **Failure Mode Auditing**  
   If a policy declares `failure_mode: "fail_open"`, the Pull Request is automatically flagged as a **Tier 3 security event**. It triggers a mandatory review and **dual‑signature ratification** by at least one OS Kernel Team member AND one Digital Governance Officer, as required by the Governance Constitution (Article II, Section 2).

5. **Target Resolution**  
   If `targets.node_ids` or `targets.action_ids` are populated, the compiler verifies that those identifiers exist in the respective registries. Attempting to attach a policy to an unregistered NodeContract or action will fail the build.

6. **Priority Conflict Check**  
   The DCP performs a static analysis to detect overlapping policies with identical priority that could lead to ambiguous outcomes. If such a conflict is found, the build is rejected and the developer must resolve it.

7. **Immutable Logging**  
   Every validation result—including rejections, approvals, and Tier 3 elevations—is recorded in the DCP’s immutable audit log, accessible to the Governance Council.

---

## 6. Policy Precedence and Composition

When multiple policies match a given execution packet, the Policy Engine:

1. Collects all applicable `PolicyRecord` instances (by `node_ids`, `action_ids`, or `policy_tags`).
2. Orders them by `priority` (highest first).
3. Evaluates each policy’s `conditions.cel_expression` against the current `SessionContext`.
4. The **first policy whose conditions evaluate to `true`** determines the final `effect`.

If no policy matches (or all conditions evaluate to `false`), the default system behavior is **`deny`** (fail‑closed). This ensures that ungoverned actions are never executed.

---

## 7. Relationship to Kits

A `PolicyRecord` is always part of a **Kit**—a versioned, signed bundle that may also contain NodeContracts and Skills. The Kit is the distributable unit listed in the Marketplace and installed by Tenants. A PolicyRecord alone cannot be deployed; it must be included in a Kit with a valid manifest and cryptographic provenance.

For Kit certification requirements, see the forthcoming **Marketplace Terms & Vendor Onboarding**. For the NodeContract schema, refer to the **NodeContract Specification**.

---

**This specification is governed by the AIOS Governance Constitution (v1.0).**  
Amendments to the schema or validation rules must follow the Constitution’s legislative process, including simulation, public comment, and supermajority ratification.