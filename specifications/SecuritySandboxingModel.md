---
document_id: AIOS-SPEC-011
title: Security & Sandboxing Model
version: 1.0.0
status: draft
category: specification
author: Gateway Global
created: 2026-04-02
last_updated: 2026-04-02
reviewers: []
supersedes: null
cross_references:
  - { doc_id: "AIOS-CORE-001", relationship: "implements" }
  - { doc_id: "AIOS-CORE-002", relationship: "constrained_by" }
  - { doc_id: "AIOS-COMM-001", relationship: "enforced_by" }
  - { doc_id: "AIOS-SPEC-006", relationship: "extends" }
  - { doc_id: "AIOS-SPEC-005", relationship: "complements" }
amendment_history: []
---
# AIOS Security & Sandboxing Model v1.0.0

## 1. Architectural Purpose

The AIOS Security & Sandboxing Model defines the **deterministic, layered defenses** that protect the platform, its Tenants, and their data from malicious or accidental harm. Because the AIOS executes untrusted code (vendor Kits, LLM outputs, external MCP endpoints), security cannot be an afterthought – it must be embedded in the architecture as a **constitutional invariant**.

This document expands on the **Technical Manifesto Article VIII** (Security & Threat Model) and the **Clean Room quarantine system** (import governance). It covers:
- Tenant isolation (logical and physical).
- Cryptographic identity and supply‑chain integrity.
- MCP endpoint security and circuit breakers.
- Runtime sandboxing for Kits and Skills.
- The Clean Room quarantine pipeline for external code.
- Incident response and the emergency “kill switch.”

All security controls are **fail‑closed** by default: if a control cannot verify trust, the system denies execution.

---

## 2. Relationship to Governing Documents

| Principle | Enforced Via |
|-----------|--------------|
| **Supply‑Chain Integrity** (Technical Manifesto Art VIII) | The Clean Room quarantine system and cryptographic attestations. |
| **Separation of Powers** (Constitution Art I, Appendix) | The Kernel (executive) cannot bypass policy (judicial); Lawmaking controls registries. |
| **Emergency Powers** (Constitution Art IV) | The Global Halt and circuit breakers are defined here. |
| **Vendor Certification** (Marketplace Terms Phase 2) | Security attestations and MCP conformance checks. |
| **Data Sovereignty** (MPOA Art V) | Isolation and BYOK are operationalised. |

---

## 3. Tenant Isolation

### 3.1 Logical Isolation
- Every Tenant operates in a separate **namespace** within the Stateful Shell and the Kernel.
- Session state, audit logs, and policy evaluations are tagged with a `tenant_id`. The Kernel rejects any cross‑tenant data access.
- The Policy Engine enforces that a `NodeContract` from Tenant A cannot reference a `Skill` or `KnowledgeSource` belonging to Tenant B.

### 3.2 Physical Isolation (High‑Sensitivity Tenants)
- For Tenants requiring regulatory compliance (e.g., healthcare, finance), the Platform offers **dedicated deployment zones** (separate Kubernetes clusters, encrypted at rest with Tenant‑managed keys).
- BYOK (MPOA Art V) is mandatory for physical isolation tiers. The Platform never has access to the Tenant’s private keys.

### 3.3 Network Isolation
- MCP endpoints are called from a **signed, rate‑limited gateway**. The Kernel never exposes internal network interfaces to vendor code.
- All outbound calls are proxied through the Integration Bus, which enforces strict timeouts and circuit breakers (Technical Manifesto Art IV).

---

## 4. Cryptographic Identity & Supply‑Chain Integrity

### 4.1 Vendor & Kit Signing
- Every Vendor generates a **private key** (never shared with the Platform). The public key is registered during onboarding (Marketplace Terms Phase 1).
- Kits are signed using `aios sign`. The signature covers:
  - The full manifest (`kit-manifest.json`).
  - All included `NodeContract`, `PolicyRecord`, and `Skill` JSON files.
  - A content hash of any bundled static assets (e.g., UI components).
- The DCP verifies the signature before any Kit is promoted to the Marketplace or installed by a Tenant.

### 4.2 Clean Room Quarantine (External Code & SDKs)
- **No external code may be executed without passing through the Clean Room quarantine system**.
- The quarantine pipeline (described in the internal implementation documents) performs:
  1. **Isolation**: The code is placed in a disposable container with no network egress (except to a read‑only registry).
  2. **Static & dynamic scanning**: Scans for `eval`, `exec`, credential exfiltration, prototype pollution, etc.
  3. **Extraction**: Only the minimal necessary logic (pure functions, type definitions, API adapters) is extracted.
  4. **Certification**: The extracted artifacts become “unverified knowledge.” A human must clear the quarantine before the code can be referenced in a Kit.
- This process is **mandatory** for all third‑party libraries and SDKs. Violations trigger a Tier 3 security event (Constitution Art II).

### 4.3 Registry Integrity
- The `shadcn/ui` component registry is mirrored from an official, signed source. Custom components (UI Component Registry Standard) are signed by the vendor and verified by the Governance Board.
- The DCP rejects any Kit that references a component not in the registry or whose signature is invalid.

---

## 5. MCP Endpoint Security

### 5.1 Authentication & Authorization
- Each MCP endpoint is associated with a **registered Vendor** and a specific `action_id`.
- The Kernel enforces that the endpoint is called only when a `NodeContract` explicitly lists that `action_id` and a `PolicyRecord` allows it.
- All MCP calls carry a **signed JWT** that includes:
  - `tenant_id`
  - `session_id`
  - `turn_id`
  - `allowed_scopes` (read/write/delete)
- Vendors must validate the JWT signature and scope before processing the request.

### 5.2 Rate Limiting & Circuit Breakers
- The Integration Bus enforces per‑Vendor and per‑endpoint rate limits (configurable in the Marketplace Terms).
- If an endpoint returns an error rate >5% over 1 minute, the circuit breaker opens, and subsequent calls fail fast (with a fallback UI). After 30 seconds, a single probe is allowed; if successful, the circuit closes.
- Repeated failures trigger a **Governance Council audit** (Constitution Art III).

### 5.3 Payload Validation
- The Kernel validates every outgoing payload against the `ActionRef` schema (type, required fields, size limits).
- Incoming responses are validated against the declared output schema. Non‑conforming responses are rejected, and the failure is logged.

---

## 6. Runtime Sandboxing for Kits & Skills

### 6.1 Stateless Compute (Technical Manifesto Art I)
- `SkillPrimitives` are invoked as **stateless functions**. They receive a strictly typed `ExecutionPacket` and return a `ExecutionResult`. They have no access to session state or the UI Surface.
- The Kernel executes each Skill in a **separate, short‑lived container** (or secure sandbox) that is destroyed after the response. No persistent storage is available.

### 6.2 Permission Boundaries
- A `NodeContract` declares exactly which `allowed_actions` and `required_skills` it needs. The Kernel injects these permissions as **capabilities** – the Skill cannot request additional actions.
- Any attempt to call an undeclared action results in a runtime `POLICY_VIOLATION` and termination of the turn.

### 6.3 Resource Limits
- Each Skill has a **performance budget** (from `NodeContract.performance_budget`): max CPU time, memory, and number of tool calls.
- The Kernel enforces these limits at the OS level (e.g., cgroups, ulimits). Exceeding the budget kills the Skill process and returns a `FAILURE` result.

---

## 7. Auditability & Immutable Logs

- Every security‑relevant event is written to the **immutable audit log** (Technical Manifesto Art VI):
  - Tenant login and role assignment.
  - Quarantine pipeline actions (scan results, extraction, clearance).
  - Kit signing and promotion.
  - Policy evaluations (allow/deny) and circuit breaker trips.
  - Global Halt activation and deactivation.
- Logs are stored in a **write‑once, read‑many (WORM)** storage system, cryptographically signed, and replicated across three availability zones.
- Tenants can export their logs via the API during the termination transition period (MPOA Art VII).

---

## 8. Incident Response & Emergency Kill Switch

### 8.1 Automated Circuit Breakers (Constitution Art IV)
- In addition to MCP circuit breakers, the Policy Engine has a **global risk counter** that monitors:
  - Sudden spike in policy violations (e.g., >100 denies per minute).
  - Unusual token consumption patterns (possible Denial of Wallet attack).
  - Anomalous component rendering errors.
- When the threshold is crossed, the Policy Engine automatically transitions the OS to **secure fallback mode** (internal‑only workflows, no external intelligence or vendor Kits). A notification is sent to the Governance Council.

### 8.2 Manual Global Halt
- Any Digital Governance Officer plus any OS Kernel Team member (two‑key authorization) can trigger a **Global Halt**.
- The halt instantly:
  - Revokes all active compute privileges.
  - Pauses all Kit executions.
  - Renders a “System Maintenance” UI across all sessions.
  - Takes a forensic snapshot of the system state.
- The halt expires after 24 hours unless renewed by a supermajority vote (Constitution Art IV). A post‑mortem report is required within 14 days.

### 8.3 Vulnerability Disclosure & Patch Process
- Security researchers and Vendors may report vulnerabilities via a dedicated HackerOne program (or equivalent).
- The Governance Council has a **7‑day SLA** to acknowledge the report and a **30‑day SLA** to deploy a patch (or issue a mitigation).
- Critical zero‑day patches may bypass the normal amendment process but must be ratified retroactively at the next Council meeting.

---

## 9. Compliance & Assurance Frameworks

The AIOS Security & Sandboxing Model is designed to support independent audits against:

- **SOC 2 (Type II)** – Security, Availability, Processing Integrity, Confidentiality, Privacy.
- **ISO 27001** – Information security management.
- **PCI DSS** – For any Kit handling payment card data (the Platform itself never stores card data; vendors must comply separately).
- **FedRAMP / HIPAA** – For government or healthcare deployments (available on request with enhanced isolation).

The Platform will produce an annual **Security Transparency Report** summarising incidents, audit results, and improvement metrics.

---

## 10. Appendices

### A. Quarantine Pipeline Summary (from internal implementation)

| Phase | Description |
|-------|-------------|
| 1. Quarantine | Code is copied to an isolated, disposable container. No network egress. |
| 2. Static Scan | Regex‑based search for dangerous patterns (`eval`, `exec`, `child_process`, `localStorage`, credential strings). |
| 3. Dynamic Scan | Run in a sandbox with mock APIs; detect anomalous behaviour (e.g., infinite loops, excessive memory). |
| 4. Extraction | Only pure functions, type definitions, and API call adapters are extracted. |
| 5. Documentation | Extracted artifacts are annotated with source provenance and usage instructions. |
| 6. Certification | A human reviewer (or designated Council member) marks the extracted code as “cleared” or “rejected.” |
| 7. Incineration | The original quarantine directory is cryptographically shredded after 72 hours. |

### B. Example Incident Response Workflow

1. **Detection** – Circuit breaker trips due to a vendor endpoint returning 500 errors for 2 minutes.
2. **Containment** – The Kernel suspends that vendor’s Kit; a `POLICY_VIOLATION` event is logged.
3. **Investigation** – The Governance Council reviews the logs and contacts the vendor.
4. **Remediation** – The vendor pushes a fixed version of the Kit; the DCP validates and signs it.
5. **Restoration** – The Council re‑enables the Kit for affected Tenants.
6. **Post‑Mortem** – A report is published (redacted for security) in the transparency log.

---

**This standard is governed by the AIOS Governance Constitution (v1.0).**  
Amendments to security controls or incident response procedures must follow the Constitution’s legislative process (RFC, simulation, supermajority ratification).
