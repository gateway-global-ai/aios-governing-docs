# GATEWAY GLOBAL AIOS: MARKETPLACE TERMS & VENDOR ONBOARDING (v1.0.0)

## 1. Ecosystem Purpose & Preamble

The Gateway Global AIOS Marketplace is not a traditional “App Store.” It is a **governed registry of Execution Kits**—versioned, cryptographically signed bundles of `NodeContracts`, `PolicyRecords`, and `Skills`.

Vendors do not upload standalone applications; they expose their backend APIs to the AIOS via the **Model Context Protocol (MCP)**, relying on the AIOS Orchestration Core (Stateful Shell) to manage user intent, UI rendering, and policy enforcement. These Marketplace Terms establish the commercial, security, and operational requirements for third‑party Vendors looking to list Kits, distribute capabilities, and monetize their software on the Gateway Global platform.

All Vendors, by participating in the Marketplace, agree to be bound by the foundational governing documents: the **AIOS Technical Manifesto**, the **Governance Constitution**, and the **Master Platform Operating Agreement (MPOA)** . These Terms are a supplement to those documents and are governed by the MPOA’s amendment process (Article VI).

---

## 2. Phase 1: Vendor Certification & Identity

Before a Vendor can publish an Execution Kit to the Marketplace, they must establish verified, cryptographically secure standing within the ecosystem.

- **Identity Verification (KYB/KYC):** Vendors must complete standard business identity verification to ensure accountability for the APIs and schemas they publish.
- **Cryptographic Identity Registration:** Vendors must generate a public/private key pair. The Platform registers the public key. The Vendor retains the private key and uses it to cryptographically sign every Kit compilation (`aios sign`). The Platform never holds the Vendor’s private key, consistent with the **Bring Your Own Key (BYOK)** principle (MPOA Article V).
- **Security Attestation:** Vendors must sign a legal attestation that their connected MCP endpoints comply with industry‑standard encryption (TLS 1.3+), implement robust rate‑limiting, and isolate cross‑tenant data.

---

## 3. Phase 2: Kit Submission & Technical Certification

To be listed in the Marketplace, an Execution Kit must physically pass the laws of the OS.

- **DCP Compiler Validation:** All submitted Kits must perfectly pass the Development Control Plane (DCP) compiler (`aios validate`). Any JSON schema violations, unapproved UI components, or malformed CEL expressions will result in automatic rejection of the listing.
- **UI Component SLA:** If a Vendor’s Kit requires a custom UI component not currently in the global `shadcn/ui` Platform Registry, they must submit the component for approval. The Gateway Global UI/UX Governance Board guarantees a review for **WCAG 2.1 Level AA** compliance and an approval/rejection within **three (3) consecutive business days** (as defined in MPOA Article I).
- **Stateless Tooling (MCP):** Kits may not contain remote code execution payloads. They may only declare `NodeContracts` and `PolicyRecords` that invoke the Vendor’s externally hosted MCP tools. This enforces the **Stateless Compute** principle (Technical Manifesto).

---

## 4. Phase 3: Commercial Terms & The “Frictionless Funnel”

The AIOS Marketplace utilizes a **Deploy‑to‑Test** economic model designed to maximize enterprise adoption and Vendor lead generation.

- **Shadow Mode (The Free Trial):** Enterprise Tenants may install any Vendor Kit in “Shadow Mode.” In this mode, the Kit intercepts live intent to prove its efficacy but is barred from mutating production state. Shadow Mode incurs **zero transaction tolls**, acting as a frictionless sales funnel for the Vendor (MPOA Article II).
- **The “Thin Slice” Revenue Share:** Once a Tenant promotes a Kit to Production, Gateway Global charges a platform routing toll. As defined in the MPOA (Article I), this fee shall not exceed **2.5% of the Gross Transaction Value (GTV)** processed by the Kit, or a pre‑negotiated Flat API Request Rate.
- **External Intelligence Constraints:** If a Vendor Kit is poorly optimized and forces the AIOS to make excessive outbound calls to platform‑managed external intelligence APIs (e.g., live web searches), those calls are billed to the Tenant’s Funded Data Account at the standard **2.0× multiplier** (MPOA Article I). Vendors are encouraged to optimize their `NodeContracts` to rely on internal MCP data whenever possible to protect Tenant budgets.
- **Payouts:** Gateway Global facilitates billing and remits Vendor revenue on standard **Net‑30 terms**, minus the routing toll.

---

## 5. Phase 4: Operational SLAs & Liability

Because the AIOS separates reasoning from state mutation, liability is strictly compartmentalized.

- **Vendor Endpoint Uptime:** Vendors are expected to maintain a **99.9% uptime SLA** for their external MCP endpoints. If an endpoint repeatedly times out or exhibits anomalous error rates, the AIOS Policy Engine may automatically trigger a circuit breaker (Technical Manifesto Article IV) to protect the OS, temporarily suspending the Kit.
- **Liability Pass‑Through:** If the AIOS Kernel successfully routes a mathematically valid payload to a Vendor’s MCP endpoint and the Vendor’s backend crashes, leaks data, or fails to execute, liability is governed by the Vendor’s own Terms of Service, and the Platform will pass through any applicable service credits to the Tenant (MPOA Article III). The AIOS acts strictly as the governed messenger.

---

## 6. Phase 5: Audits, Due Process, & Termination

Gateway Global strictly regulates the Marketplace to protect Enterprise Tenants from malicious or degraded software.

- **Governance Council Audits:** The Governance Council (Constitution Article III) actively monitors the `ExecutionViolationLog`. If a Vendor Kit exhibits anomalous error rates, attempts to bypass MCP constraints, or consistently violates Tenant policies, it will be flagged for audit.
- **Due Process & Remediation:** Before a Kit is delisted or a Vendor’s cryptographic signature is revoked, the Council must provide the Vendor with **written notice and a 14‑day remediation period** to push a patched version of the Kit (Constitution Article III, Section 2; MPOA Article V).
- **Emergency Kill Switch:** In the event of an active, systemic security threat or data breach originating from a Vendor API, the Governance Council reserves the right to execute an immediate **Emergency Halt**, suspending the Kit instantly without the 14‑day notice (Constitution Article IV).
- **Right to Appeal:** Vendors maintain the right to appeal any revocation or delisting to an **independent arbitrator**, as outlined in the MPOA (Article V).

---

## 7. Relationship to Governing Documents

By registering as a Vendor on the AIOS Marketplace, the Vendor explicitly agrees to be bound by the platform’s foundational laws:

| Document | Relevant Provisions |
|----------|---------------------|
| **Governance Constitution** | Human oversight, legislative process, Council audit powers, emergency procedures. |
| **Master Platform Operating Agreement (MPOA)** | Liability boundaries, economic caps, data sovereignty, indemnification, dispute resolution. |
| **Technical Manifesto** | Stateless compute, UI sovereignty, MCP integration, circuit breakers, versioning. |

Amendments to these Marketplace Terms follow the **economic amendment process** defined in the MPOA (Article VI), requiring a **90‑day public notice period** prior to enactment.

---

## 8. Next Steps for Vendors

Vendors interested in joining the Marketplace should:

1. **Review** the Technical Manifesto, Governance Constitution, and MPOA.
2. **Complete** identity verification and cryptographic key registration via the Vendor Portal.
3. **Develop** Kits using the `aios` CLI and the NodeContract/PolicyRecord schemas.
4. **Test** thoroughly in Shadow Mode to validate behavior without incurring tolls.
5. **Submit** the Kit for technical certification (automated DCP validation).
6. **Publish** to the Marketplace after certification.

For questions or onboarding support, contact **vendor@gatewayglobal.ai**.

---

**These Marketplace Terms are governed by the AIOS Governance Constitution (v1.0) and the Master Platform Operating Agreement (v3.0).**  
Amendments to these Terms follow the MPOA’s 90‑day public comment and notification process.