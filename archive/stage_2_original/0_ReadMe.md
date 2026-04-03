Below is a comprehensive **README** that serves as the entry point to the AIOS governing document set. It introduces the trilogy, explains the audience and purpose, provides links to each document, and outlines how they interconnect.

---

# AIOS Governing Documents – The Foundation of a Governed Operating System

Welcome to the Gateway Global AI Operating System (AIOS). This repository contains the complete set of governing documents that define the architecture, legal terms, and human oversight of the platform.

The AIOS is not merely software; it is a **governed execution environment** where deterministic law meets human intent. These documents ensure that every participant—enterprise customers, vendors, developers, and AI agents—operates under a common, transparent, and binding framework.

---

## Audience

| Role | What to Read First |
|------|--------------------|
| **Enterprise Customers** | MPOA + Constitution |
| **Vendors & Developers** | Technical Manifesto + Constitution |
| **Legal & Compliance** | MPOA + Constitution |
| **Coding Agents (AI)** | Technical Manifesto + (upcoming) Agent Integration Protocol |

---

## The Trilogy

The AIOS governing framework consists of three core documents. Each addresses a distinct dimension of the system.

| Document | Version | Focus |
|----------|--------|-------|
| [**Technical Manifesto**](./TECHNICAL_MANIFESTO.md) | v1.0 | Architecture, determinism, developer primitives |
| [**Master Platform Operating Agreement (MPOA)**](./MPOA.md) | v3.0 | Economics, liability, data sovereignty, legal terms |
| [**Governance Constitution**](./GOVERNANCE_CONSTITUTION.md) | v1.0 | Human oversight, Council structure, legislative & judicial processes |

---

## How They Fit Together

```
┌─────────────────────────────────────────────────────────────┐
│                     Governance Constitution                  │
│      (Who decides, how decisions are made, emergency        │
│                  powers, amendment process)                  │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                │ establishes & constrains
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                     Technical Manifesto                      │
│        (How the system works: separation of powers,         │
│        UI sovereignty, stateless compute, versioning)        │
└───────────────────────────────┬─────────────────────────────┘
                                │
                                │ is executed under
                                ▼
┌─────────────────────────────────────────────────────────────┐
│               Master Platform Operating Agreement            │
│   (Economic terms, liability caps, data rights, vendor      │
│           certification, indemnification, law)               │
└─────────────────────────────────────────────────────────────┘
```

**Supremacy Clause** (per MPOA and Constitution):  
- **Governance Constitution** prevails for human oversight, voting, and ecosystem governance.  
- **MPOA** prevails for liability, economics, indemnification, and data sovereignty.  
- **Technical Manifesto** prevails for system architecture and deterministic execution logic.

---

## Additional Resources (In Development)

The following documents will be added to complete the developer and agent experience:

- **NodeContract & Policy Specification** – The schema for authoring deterministic laws (machine‑readable).  
- **CLI Developer Experience Guide** – Full reference for the `aios` CLI.  
- **Agent Integration Protocol (AIP)** – MCP‑based tools for coding agents.  
- **UI Component Registry Standard** – Rules for contributing to the global component library.  
- **Marketplace Terms & Vendor Onboarding** – Rules for listing Kits.  
- **Security & Sandboxing Model** – Deep dive on tenant isolation, attestations, and supply chain.  
- **Data Privacy & Compliance Addendum** – GDPR/CCPA specifics, BYOK implementation.  
- **Governance Council Operating Manual** – Internal procedures for the Council.  
- **Ecosystem Roadmap & Versioning Policy** – Deprecation timelines and public roadmap.

---

## Getting Started

1. **For Enterprises** – Begin with the [MPOA](./MPOA.md) to understand economic terms, liability boundaries, and your data rights. Then read the [Governance Constitution](./GOVERNANCE_CONSTITUTION.md) to see how decisions are made and how you can participate through the Enterprise Consortium.

2. **For Vendors & Developers** – Start with the [Technical Manifesto](./TECHNICAL_MANIFESTO.md) to understand the architecture and the primitives (`NodeContracts`, `Policies`, `Skills`). Then review the [MPOA](./MPOA.md) for commercial terms and the [Constitution](./GOVERNANCE_CONSTITUTION.md) for the due process you can expect.

3. **For Legal & Compliance Teams** – The [MPOA](./MPOA.md) contains the binding legal terms (governing law, arbitration, indemnification). The [Constitution](./GOVERNANCE_CONSTITUTION.md) provides the governance structure and amendment process.

4. **For AI Coding Agents** – The [Technical Manifesto](./TECHNICAL_MANIFESTO.md) describes the development control plane and the constraints you must operate within. The upcoming **Agent Integration Protocol** will provide the MCP tools to generate and test primitives.

---

## Versioning & Amendments

All three core documents are versioned and governed by the amendment processes described in the Constitution and MPOA. Key principles:

- **Economic/liability amendments** require a 90‑day public comment period (MPOA Art VI).
- **Constitutional amendments** require simulation, Enterprise Consortium comment, and supermajority ratification (Constitution Art VI).
- **Manifesto amendments** follow the RFC process defined in the Constitution and are subject to the same governance oversight.

---

## Contributing

The AIOS governing documents are maintained by the AIOS Governance Council. Feedback from the community—especially Tenants and Vendors—is welcome through the formal **Request for Comments (RFC)** process outlined in the Constitution.

---

## License & Copyright

© Gateway Global. All rights reserved. These documents define the legal and operational terms for participation in the AIOS ecosystem. Unauthorized modification or distribution is prohibited.

---

## Next Steps

If you are ready to engage with the AIOS platform, please contact **onboarding@gatewayglobal.ai** to begin the onboarding process. For technical inquiries, refer to the [Technical Manifesto](./TECHNICAL_MANIFESTO.md) and watch for the upcoming developer tooling documentation.

---

*Last updated: April 2026 – All core documents at stable v1.0 (MPOA v3.0).*