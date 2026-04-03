---
document_id: AIOS-CORE-003
title: Gateway Global AIOS Master Platform Operating Agreement
version: 3.0.0
status: ratified
category: core
author: Gateway Global
created: 2026-03-15
last_updated: 2026-04-01
reviewers:
  - { reviewer: "DeepSeek R1", date: "2026-03-20", review_path: "reviews/master_platform_operating_agreement/round_1/review_001_deepseek.md" }
supersedes: archive/master_plan_operating_agreement_0.md
cross_references:
  - { doc_id: "AIOS-CORE-001", relationship: "incorporates" }
  - { doc_id: "AIOS-CORE-002", relationship: "constrained_by" }
amendment_history: []
---

You are completely right. I moved too fast and left critical enterprise exposures in the document. A contract without a governing law clause, mutual indemnification, or clearly defined liability caps is a draft, not a legally binding agreement. 

By applying these surgical peer-review updates—specifically the 12-month liability cap, the pass-through vendor terms, the Delaware arbitration clause, and the expanded data privacy protections—we close every remaining loophole. 

Here is the fully hardened, enterprise-ready **Gateway Global AIOS Master Platform Operating Agreement v3.0**.

***

# GATEWAY GLOBAL AIOS: MASTER PLATFORM OPERATING AGREEMENT

## Preamble
This Master Platform Operating Agreement ("Agreement") governs the rights, liabilities, and economic obligations of all parties interacting within the Gateway Global AI Operating System (the "AIOS"). This Agreement establishes the legal boundaries between Gateway Global (the "Platform"), Enterprise Customers (the "Tenants"), and third-party API and Kit developers (the "Vendors"). 

The *AIOS Technical Manifesto (v1.0)* and the *AIOS Governance Constitution (v1.0)* as of the Effective Date are incorporated herein by reference. Amendments to those documents follow their own independent processes and do not amend this Agreement unless explicitly stated.

---

## Article I: Core Definitions
To ensure absolute clarity in economic and operational execution, the following terms are strictly defined:
* **Gross Transaction Value (GTV):** The total monetary value processed by a specific Vendor Kit during a single intent execution, excluding taxes and routing fees. In multi-Kit workflows, GTV is calculated discretely per Vendor Kit to strictly prevent double-counting.
* **Flat API Request Rate:** An alternative to the percentage-based toll, negotiated directly between the Tenant and Vendor, subject to Platform routing minimums.
* **Business Hours SLA:** References to "72 business hours" shall be strictly interpreted as three (3) consecutive standard business days.
* **Cryptographic Shredding:** The permanent, verifiable deletion of the encryption keys securing a data payload, rendering the associated ciphertext permanently unrecoverable.
* **WCAG Compliance:** Refers strictly to the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standard.

---

## Article II: Platform Economics & Fee Caps
All financial interactions within the AIOS are strictly bound by the following caps:
* **The External Intelligence Multiplier:** Any action requiring external intelligence compute (e.g., premium model generation, live web search) executed via platform-managed keys will be billed to the Tenant’s Funded Data Account at exactly **2.0x the direct upstream vendor cost**. 
* **The "Thin Slice" Transaction Toll:** For business-logic execution utilizing third-party Kits, Gateway Global charges a platform routing fee not to exceed **2.5% of the Gross Transaction Value (GTV)** or the agreed Flat API Request Rate.
(The thin‑slice model mirrors successful B2B marketplace practices—such as AWS Marketplace and Atlassian—where low single‑digit platform fees maximize ecosystem participation. This structure prioritizes ecosystem growth over short‑term revenue extraction.)
* **Shadow Mode Exception:** Tenants deploying Kits in "Shadow Mode" incur zero transaction tolls. *However*, actions utilizing external intelligence compute during Shadow Mode will still debit the Tenant's Funded Data Account at the standard 2.0x multiplier to cover raw upstream API costs.

---

## Article III: Liability Boundaries & Execution Immunity
Because the AIOS separates reasoning (LLMs) from state mutation (the Kernel), liability is strictly compartmentalized based on the point of failure:
* **Vendor API Failure:** If the AIOS Kernel successfully routes a mathematically valid payload to a Vendor's endpoint and the Vendor's system fails or returns corrupted data, liability is governed strictly by the Vendor's own Terms of Service. The Platform assumes no liability for Vendor outages or consequential damages but will pass through any applicable Vendor service credits to the Tenant.
* **Policy Enforcement Immunity:** If a Compute Kernel Worker (LLM) hallucinates a malicious action, and the AIOS Policy Engine successfully catches and drops the directive, no liability is incurred. 
* **Kernel Failure Liability (Default Cap):** If the AIOS Kernel executes a state mutation that explicitly violates an active, compiled NodeContract or Tenant Policy, Platform liability is strictly capped at **an amount not to exceed the total fees paid by the Tenant to the Platform in the twelve (12) months preceding the incident**.
* **Tenant Configuration Liability (No Duty to Warn):** If a Tenant authorizes a flawed Policy that results in undesired business outcomes, the Tenant assumes full liability. The Platform may, but is under no obligation to, flag self-contradictory policies.

---

## Article IV: State Conflict Resolution & Judicial Escalation
* **Tenant-Defined Priority Matrix:** In the event of a state conflict, the Kernel automatically defers to the Kit with the higher priority weight as defined by the Tenant.
* **Deterministic Deadlock & Escalation:** If priority weights are equal, the Kernel defaults to a "Fail-Closed" posture. Deadlocks are immediately escalated to the AIOS Governance Council.
* **Rollback Guarantee:** In the event of a resolved conflict resulting in undesired state, the system guarantees commercially reasonable efforts to execute a cryptographic rollback to the pre-conflict state, subject to technical limitations introduced by subsequent, dependent state mutations.

---

## Article V: Data Sovereignty, Privacy, and Erasure
* **Model Training Prohibition:** Gateway Global strictly prohibits the use of *any* Tenant data—whether ephemeral Shadow Data or live Production Data, anonymized or otherwise—for the training of foundational AI models without the explicit, written consent of the Tenant.
* **Right to Erasure:** Executing a global erasure command triggers the cryptographic shredding of all associated extracted entities, session context, and audit logs within **72 hours**, subject only to mandatory, documented Legal Holds.
* **Bring Your Own Key (BYOK):** Tenants utilizing BYOK are solely responsible for key lifecycle management. The loss or destruction of a Tenant-managed key will render the encrypted state permanently unrecoverable, for which the Platform accepts no liability.

---

## Article VI: Vendor Marketplace Certification & UI SLAs
* **Kit Certification:** To be listed in the Marketplace, Vendors must pass the AIOS Security Attestation, provide a guaranteed support SLA, and ensure their APIs strictly conform to the Model Context Protocol (MCP).
* **UI Component SLA:** If a Vendor submits a custom UI component to the global registry, the Platform is legally bound to review and test for WCAG 2.1 Level AA compliance, issuing an approval or explicit rejection within three (3) consecutive business days.

---

## Article VII: Term, Termination, and Transition
* **Termination for Convenience/Cause:** Either party may terminate this Agreement with 30 days written notice. In the event of a material breach, the non-breaching party may terminate immediately following a 15-day uncured cure period.
* **Transition & Data Export:** Upon termination, Tenants are granted a 30-day Transition Period during which they may export all persistent session state, policies, and audit logs via standard API formats. Following the 30-day period, all Tenant data will undergo mandatory cryptographic shredding.

---

## Article VIII: Representations, Warranties, & Indemnification
* **Mutual Representations:** Each party warrants they have the legal authority to enter this Agreement and comply with all applicable laws. The Platform warrants that the OS Kernel operates materially as described in the *Technical Manifesto*.
* **Mutual Indemnification:** The Platform shall indemnify and defend the Tenant against third-party claims alleging that the AIOS infringes upon intellectual property rights. The Tenant shall indemnify the Platform against claims arising from Tenant-uploaded data, self-authored policies, or violations of applicable data privacy laws. Both parties mutually indemnify each other against confirmed data breaches resulting from their respective gross negligence.

---

## Article IX: Governing Law & Dispute Resolution
* **Choice of Law:** This Agreement shall be governed by and construed in accordance with the laws of the State of Delaware, without regard to its conflict of law principles.
* **Binding Arbitration:** Any dispute, controversy, or claim arising out of or relating to this Agreement shall be settled by binding, confidential arbitration administered by the American Arbitration Association (AAA) under its Commercial Arbitration Rules, with the seat of arbitration in Wilmington, Delaware.

---

## Article X: Supremacy, Incorporation, & Amendments
* **The Supremacy Clause:** In the event of a direct inconsistency between the governing documents:
    * The **Governance Constitution** prevails for matters of human oversight, voting, and ecosystem governance.
    * This **Master Platform Operating Agreement (MPOA)** prevails for matters of liability, indemnification, economics, and data sovereignty.
    * The **Technical Manifesto** prevails for matters of system architecture and deterministic execution logic.
* **Economic Amendments:** Any changes to the economic, liability, or indemnification terms of this MPOA require a **90-day public comment period** and direct written notification to all active Tenants and Vendors prior to enactment.