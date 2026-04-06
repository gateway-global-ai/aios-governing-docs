---
document_id: AIOS-COMM-002
title: Data Privacy & Compliance Addendum
version: 1.0.0
status: draft
category: commercial
author: Gateway Global
created: 2026-04-02
last_updated: 2026-04-02
reviewers: []
supersedes: null
cross_references:
  - { doc_id: "AIOS-CORE-001", relationship: "implements" }
  - { doc_id: "AIOS-CORE-003", relationship: "amends" }
  - { doc_id: "AIOS-CORE-002", relationship: "constrained_by" }
  - { doc_id: "AIOS-SPEC-011", relationship: "complements" }
amendment_history: []
---
# AIOS Data Privacy & Compliance Addendum v1.0.0

## 1. Purpose & Scope

This Addendum supplements the **Master Platform Operating Agreement (MPOA)** and the **Technical Manifesto** by specifying the operational, technical, and organisational measures that Gateway Global implements to protect personal data and comply with applicable privacy laws, including the **General Data Protection Regulation (GDPR)** (EU) and the **California Consumer Privacy Act (CCPA)** (US). It also addresses cross‑border data transfers, data subject rights, breach notification, and independent assurance frameworks (SOC 2, ISO 27001, etc.).

All terms defined in the MPOA (e.g., “Tenant”, “Vendor”, “Cryptographic Shredding”) apply here. In the event of a conflict between this Addendum and the MPOA, the MPOA prevails for liability and economic matters, but this Addendum prevails for specific privacy and compliance obligations.

---

## 2. Relationship to Governing Documents

| Principle | Enforced Via |
|-----------|--------------|
| **Data Sovereignty** (MPOA Art V) | BYOK, data residency, erasure timelines are operationalised here. |
| **Model Training Prohibition** (MPOA Art V) | Explicit restriction on using Tenant data for model training. |
| **Auditability** (Technical Manifesto Art VI) | Privacy‑specific logging and data subject access. |
| **Security & Sandboxing** (Security Model) | Encryption, isolation, and breach prevention. |

---

## 3. Data Processing Roles & Responsibilities

| Role | Definition | Responsibility |
|------|------------|----------------|
| **Gateway Global (Platform)** | Data Processor (for Tenant personal data) and Data Controller (for its own administrative data). | Process Tenant data only on documented instructions; provide security; assist with breaches and subject requests. |
| **Tenant** | Data Controller (for its end‑users’ personal data). | Determine purposes; ensure lawful basis; respond to data subject requests; configure policies. |
| **Vendor** | Sub‑processor (when processing data via Kits). | Must comply with the same security and privacy obligations as Gateway Global, per Marketplace Terms. |

Gateway Global maintains a **public list of sub‑processors** (e.g., cloud infrastructure providers) updated quarterly.

---

## 4. Data Collection, Use, and Retention

### 4.1 Types of Data Collected
- **Session Context**: IntentKeys, transcripts, UI interactions, policy decisions (stored encrypted, retained for 30 days unless otherwise configured).
- **Persistent State**: Tenant‑configured data (e.g., user profiles, preferences) – retained as long as the Tenant account is active.
- **Audit Logs**: Immutable logs of security and policy events – retained for 7 years (regulatory requirement).
- **Shadow Mode Data**: Ephemeral, cryptographically shredded every 72 hours (MPOA Art V).

### 4.2 Purpose Limitation
- The Platform processes Tenant data solely to execute the Tenant’s instructions (i.e., to run the AIOS). It does not use data for any other purpose (e.g., advertising, profiling) without explicit written consent.
- **Model Training Prohibition** (MPOA Art V) is enforced at the database and pipeline level: no Tenant data, even anonymised, enters training datasets.

### 4.3 Retention & Erasure
- Tenants configure retention periods for persistent state via the `PolicyRecord` (e.g., `data_retention_days: 90`).
- Upon termination (MPOA Art VII), the Platform initiates **cryptographic shredding** of all Tenant data after the 30‑day transition period. The shredding process is logged and an erasure certificate is provided.

---

## 5. Data Subject Rights (GDPR Art 15‑22, CCPA)

The AIOS provides mechanisms for Tenants to respond to data subject requests (DSRs) from their end‑users.

| Right | How the AIOS Supports It |
|-------|--------------------------|
| **Access** | Tenant can export all personal data associated with an end‑user via the REST API (`GET /v1/privacy/export/{user_id}`). |
| **Rectification** | Tenant can update user profile data via the `Stateful Shell` or directly via API. |
| **Erasure (Right to be Forgotten)** | Tenant invokes the **global erasure command** (MPOA Art V) for a specific user. The Platform performs cryptographic shredding within 72 hours. |
| **Restriction of Processing** | Tenant can apply a `PolicyRecord` that blocks further processing for a specific user (e.g., `user.data_subject_restriction = true`). |
| **Data Portability** | Exported data is provided in a structured, machine‑readable format (JSON). |
| **Object to Processing** | Tenant configures policies to honour opt‑outs (e.g., no automated decision‑making). |
| **Automated Decision‑Making** | The AIOS’s deterministic execution is always subject to human‑reviewable policies. Tenants can disable high‑risk decisions via policy. |

The Platform charges no additional fee for fulfilling DSRs. Tenants must respond to DSRs within the legal timeframe (e.g., 30 days under GDPR). Gateway Global will assist within 72 hours of a Tenant request.

---

## 6. Data Residency & Cross‑Border Transfers

### 6.1 Default Residency
- Tenant data is stored in the **primary region** selected at onboarding (e.g., `US‑EAST`, `EU‑WEST`, `AP‑SOUTHEAST`). The Platform does not move data between regions without explicit Tenant consent.

### 6.2 Cross‑Border Transfers (EU‑US Data Privacy Framework)
- Gateway Global self‑certifies under the **EU‑US Data Privacy Framework** (or its successor) and the **UK Extension**. Transfers from the EEA/UK to the US are lawful under that framework.
- For transfers to other third countries, the Platform relies on **Standard Contractual Clauses (SCCs)** approved by the European Commission, supplemented by technical safeguards (encryption, BYOK).

### 6.3 Sub‑processor Locations
- All sub‑processors are listed in the public sub‑processor register, including their geographic locations. Tenants may object to new sub‑processors within 30 days of notification.

---

## 7. Security Controls (Supplement to Security Model)

| Control | Implementation |
|---------|----------------|
| **Encryption at Rest** | AES‑256 for all persistent data (including logs). BYOK keys are managed by Tenant. |
| **Encryption in Transit** | TLS 1.3 for all API and MCP traffic. |
| **Access Control** | Role‑based access control (RBAC) for Platform employees; no direct database access without just‑in‑time approval and audit logging. |
| **Pseudonymisation** | Where feasible, personal data is stored with pseudonyms (e.g., hashed user IDs). Direct identifiers (name, email) are separated and encrypted. |
| **Data Minimisation** | The AIOS never requests or stores sensitive data (e.g., social security numbers) unless explicitly required by a Tenant’s `NodeContract`. The DCP rejects contracts that would collect unnecessary data. |

---

## 8. Breach Notification

### 8.1 Definition of Personal Data Breach
A breach is any accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted, stored, or otherwise processed.

### 8.2 Notification to Tenants
- Gateway Global will notify affected Tenants **without undue delay** and in any event **within 72 hours** of becoming aware of a breach.
- The notification will include:
  - Description of the breach.
  - Categories and approximate number of individuals and records affected.
  - Likely consequences.
  - Measures taken to mitigate and prevent recurrence.
  - Contact details for further information.

### 8.3 Notification to Supervisory Authorities
- For breaches likely to result in a risk to the rights and freedoms of natural persons, Gateway Global will notify the relevant supervisory authority (e.g., the Irish DPC) within 72 hours, as required by GDPR Art 33.

### 8.4 Tenant’s Obligations
- Tenants must notify their own end‑users and authorities as required by applicable law. Gateway Global will provide reasonable assistance.

---

## 9. Data Protection Impact Assessments (DPIAs)

Gateway Global conducts DPIAs for any new processing that is likely to result in a high risk to the rights and freedoms of natural persons (e.g., large‑scale processing of health data, use of biometric authentication). DPIAs are reviewed by the **Digital Governance Officers** (Constitution Art I) and made available to supervisory authorities upon request.

Tenants may request a copy of the DPIA (redacted to protect security information) via the Governance Council.

---

## 10. Compliance with Industry Frameworks

The AIOS is designed to support the following certifications. Gateway Global will undergo annual audits:

| Framework | Scope | Status |
|-----------|-------|--------|
| **SOC 2 (Type II)** | Security, Availability, Processing Integrity, Confidentiality, Privacy | Planned for 2026 |
| **ISO 27001** | Information Security Management System | Planned for 2026 |
| **ISO 27701** | Privacy Information Management | Planned for 2027 |
| **PCI DSS** | For payment‑processing Kits (Platform does not store card data; vendors are responsible) | N/A for Platform |

Tenants may request the latest audit reports (subject to a standard NDA).

---

## 11. Data Processing Agreement (DPA)

The MPOA incorporates by reference the **Standard Contractual Clauses** (SCCs) approved by the European Commission (2021/914/EU) for transfers of personal data from the EEA to third countries. The DPA is available as a separate annex. Tenants may request a signed copy.

---

## 12. Amendments & Governing Law

- Amendments to this Addendum follow the **economic amendment process** of the MPOA (Article VI), requiring a 90‑day public comment period and direct notification to all Tenants.
- This Addendum is governed by the laws of the State of Delaware and, for GDPR matters, the laws of the European Union and its Member States as implemented by the supervisory authority of Ireland (Gateway Global’s designated lead supervisory authority).

---

## 13. Appendices

### A. Example Data Subject Request Workflow

1. **Tenant receives a request** from an end‑user to delete their data.
2. **Tenant calls** `POST /v1/privacy/erase` with the user’s `session_id` or `user_id`.
3. **Platform verifies** the Tenant’s authority (API key with `privacy:write` scope).
4. **Platform initiates** cryptographic shredding of all personal data associated with that user across all services (session state, logs, persistent store).
5. **Platform returns** an erasure certificate (JSON) with timestamps and a hash of the shredded data.
6. **Tenant responds** to the end‑user confirming deletion.

### B. BYOK Implementation Summary

- Tenant generates an RSA‑4096 or EC‑256 key pair. The public key is uploaded to the Platform.
- The Platform never holds the private key.
- All persistent state is encrypted with a **data encryption key (DEK)** that is itself encrypted with the Tenant’s public key (wrapped). The wrapped DEK is stored alongside the data.
- On each session, the Tenant’s private key (held by the Tenant’s own key management service) must decrypt the DEK. The Platform never sees the plaintext DEK.
- If the Tenant loses the private key, the data is unrecoverable – the Platform accepts no liability (MPOA Art V).

---

**This Addendum is governed by the AIOS Governance Constitution (v1.0) and the Master Platform Operating Agreement (v3.0).**  
Amendments to privacy controls or breach procedures must follow the MPOA’s 90‑day public comment and notification process.
