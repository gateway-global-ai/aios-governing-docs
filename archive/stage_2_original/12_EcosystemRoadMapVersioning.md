# AIOS Ecosystem Roadmap & Versioning Policy v1.0.0

## 1. Purpose

The AIOS is a living platform. To maintain trust and predictability for Tenants, Vendors, and Developers, changes to the platform’s APIs, primitives (NodeContract, PolicyRecord), component registry, and governance processes must follow a **clear, versioned, and deprecation‑aware policy**. This document defines:

- **Semantic versioning** for all platform components.
- **Deprecation lifecycle** and sunset timelines.
- **Public roadmap** and Request for Comments (RFC) process.
- How the roadmap interacts with the Constitution’s amendment process and the MPOA’s economic amendment rules.

All stakeholders (enterprise Tenants, Vendors, AI agents) can rely on this policy to plan their own development and adoption cycles.

---

## 2. Relationship to Governing Documents

| Principle | Enforced Via |
|-----------|--------------|
| **Semantic Governance** (Technical Manifesto Art IX) | Explicit versioning rules for APIs, schemas, and component registry. |
| **Amendment Process** (Constitution Art VI) | Major changes (breaking, new features) require RFC and supermajority ratification. |
| **Economic Amendments** (MPOA Art VI) | Changes to fee structures, caps, or liability follow a separate 90‑day notice. |
| **Marketplace Terms** | Vendors must adapt to deprecated APIs within the grace period; failure may lead to delisting. |

---

## 3. Versioning Scheme

All platform components use **Semantic Versioning 2.0.0** (`MAJOR.MINOR.PATCH`). The following table maps each component to its versioning scope.

| Component | Version Location | MAJOR change | MINOR change | PATCH change |
|-----------|------------------|--------------|--------------|--------------|
| **AIOS Core Documents** (Manifesto, Constitution, MPOA) | Front matter `version:` | Structural reorganisation, new articles, changed supremacy clause. | New sections that do not alter existing obligations. | Typos, formatting, non‑substantive clarifications. |
| **NodeContract JSON Schema** | `$id` URL + file version | Incompatible field changes, removed required fields, altered validation rules. | New optional fields, additional `enum` values. | Clarifications, bug fixes to schema description. |
| **PolicyRecord JSON Schema** | Same as above | Same rules as NodeContract. | Same as above. | Same as above. |
| **UI Component Registry** | Each component’s `version` field | Removed variant, changed behaviour. | New variant, new optional property. | Bug fix, accessibility improvement (no API change). |
| **MCP Tools & REST API** | API endpoint path (`/v1/`) and OpenAPI spec | New major version endpoint (e.g., `/v2/`). | New optional fields, new endpoints, non‑breaking additions. | Bug fixes, documentation. |
| **CLI (`aios`)** | `aios --version` | Breaking command changes, removed flags, changed output format. | New commands, new flags, added `--json` fields. | Bug fixes, performance improvements. |

**Rule**: A change is **breaking** if it would cause a correctly written Kit (or integration) to fail at compile time or runtime without modification. The DCP and Policy Engine treat any reference to a deprecated or removed field as a validation error.

---

## 4. Deprecation Lifecycle

### 4.1 Deprecation Notice Periods

| Component | Minimum Notice Before Removal |
|-----------|-------------------------------|
| **Core Documents** (Manifesto, Constitution, MPOA) | 6 months (with supermajority Council approval) |
| **NodeContract / PolicyRecord schema field** | 3 months |
| **UI Component** | 90 days (must provide replacement) |
| **MCP API endpoint** | 6 months (for `/v1/` endpoints; `/v2/` can be introduced immediately) |
| **CLI command or flag** | 3 months |

### 4.2 Deprecation Process

1. **Announcement** – The Governance Council publishes a **Deprecation Notice** in the public roadmap and the transparency log (Governance Council Operating Manual Section 8). The notice includes:
   - The component or field being deprecated.
   - The reason for deprecation.
   - The recommended alternative (if any).
   - The **sunset date** (end of life).

2. **Grace Period** – During the notice period, the deprecated feature continues to function normally, but warnings are emitted:
   - In DCP compiler logs (for schema fields).
   - In CLI output (e.g., `Warning: flag --old is deprecated, use --new`).
   - In the UI Component Registry (component marked `deprecated: true`).

3. **Sunset** – On the sunset date, the Platform removes the feature. Any Kit or integration that still relies on it will fail validation (for schemas) or runtime (for APIs). The DCP rejects such Kits, and they must be updated before they can be promoted.

4. **Emergency Extension** – In exceptional cases (e.g., critical vendor still migrating), the Council may grant a one‑time extension of up to 30 days by majority vote.

### 4.3 Backward Compatibility Guarantee (Technical Manifesto Art IX)

- **PATCH** and **MINOR** versions never break existing Kits. The Platform guarantees that a Kit that worked on version `1.2.3` will continue to work on any `1.x.y` release.
- **MAJOR** version upgrades may introduce breaking changes, but the Platform will maintain the previous major version for **at least 6 months** after the new major version is released, giving Vendors time to migrate.

---

## 5. Public Roadmap & RFC Process

### 5.1 Public Roadmap

The AIOS public roadmap is hosted at `https://roadmap.aios.dev`. It is updated monthly by the Governance Council and includes:

| Column | Description |
|--------|-------------|
| **Now** (current quarter) | Features, schema changes, or policies being actively developed. |
| **Next** (next quarter) | Planned items with high confidence. |
| **Future** (two‑four quarters) | Under consideration; may change. |
| **Deprecations** | Features scheduled for removal with sunset dates. |

The roadmap is **not a binding commitment** but a transparent communication tool. Tenants and Vendors may subscribe to change notifications.

### 5.2 Request for Comments (RFC) Process (Constitution Art VI)

Any significant change to the platform – including new major features, schema extensions, new governance rules, or deprecations with notice shorter than the minimum – must go through the **RFC process**.

**RFC Workflow**:

1. **Draft** – Anyone (Tenant, Vendor, developer, Council member) submits an RFC using the template in Appendix A. The draft is posted to the public `rfcs@aios.dev` mailing list and the GitHub repository (under `rfcs/`).

2. **Comment Period** – Minimum 30 days for technical RFCs, 60 days for governance or economic changes. The Governance Council may extend the period.

3. **Simulation** – For changes affecting the DCP or schemas, the proposer must provide simulation results (e.g., a staging environment test showing that existing Kits are not broken).

4. **Council Review** – The Council assigns a primary reviewer (from the relevant branch). The Council votes:
   - Simple majority for non‑breaking changes.
   - Two‑thirds supermajority for breaking changes, deprecations, or any change that affects the Constitution or MPOA.

5. **Approval & Implementation** – If approved, the change is scheduled on the roadmap with a target version. The implementation must follow the versioning and deprecation rules.

6. **Rejection** – The Council provides a written explanation. The proposer may resubmit after addressing concerns.

### 5.3 Fast‑Track for Security Patches

Critical security fixes (e.g., schema validation bypass) may bypass the RFC comment period but must be ratified by the Council within 7 days after deployment (Constitution Art IV). The post‑mortem includes the rationale for fast‑tracking.

---

## 6. Versioning of the Governing Documents Themselves

The trilogy (Technical Manifesto, Governance Constitution, MPOA) follows the same semantic versioning rules. In addition:

- The **MPOA’s economic terms** (Article I, II) are subject to the 90‑day public comment period before any version change that alters fees, caps, or liability.
- The **Constitution’s amendment process** (Article VI) requires a two‑thirds supermajority and simulation before ratification.
- The **Technical Manifesto’s architectural invariants** (e.g., stateless compute, UI sovereignty) cannot be changed without a full constitutional amendment; they are considered immutable.

All ratified versions of the documents are stored in `archive/` with the version in the filename. The latest version is always available at the standard URL (e.g., `/core/technical_manifesto.md`).

---

## 7. Ecosystem Lifecycle for Vendors & Kits

Vendors must align with the versioning policy to remain compatible:

- **Kit Manifest** includes `aios_api_version` (e.g., `"1"`). When the Platform introduces a new major version, Vendors have 6 months to update their Kits.
- **Deprecated UI components** – The Vendor must update the Kit’s `permitted_ui_components` to use the replacement before the sunset date, otherwise the Kit will be automatically delisted from the Marketplace (after a warning period).
- **Security‑only updates** – The Platform may backport critical security fixes to older API versions for up to 12 months after a new major version is released.

---

## 8. Roadmap Communication & Change Logs

- **Changelog** – Every release of the Platform (including DCP, CLI, API, registry) includes a machine‑readable `CHANGELOG.md` (or `CHANGELOG.json`) following [Keep a Changelog](https://keepachangelog.com/) format.
- **Notification** – Tenants and Vendors can subscribe to release notifications via email or webhook. Deprecation notices are also sent 30 days before the sunset date.
- **Governance Council Transparency Log** – All roadmap decisions, RFC outcomes, and deprecation approvals are recorded in the transparency log (Council Operating Manual Section 8).

---

## 9. Appendices

### Appendix A – RFC Template

```markdown
**RFC ID:** `RFC-YYYY-MM-DD-XXX`
**Title:** [Short description]
**Type:** [Technical | Governance | Economic | Deprecation]
**Author(s):** [Name, affiliation]
**Date:** YYYY-MM-DD
**Affected components:** [e.g., NodeContract schema, MCP API, CLI, Marketplace Terms]
**Summary:** [One paragraph]
**Motivation:** [Why is this change needed? What problem does it solve?]
**Proposed change:** [Detailed description, including before/after examples]
**Impact assessment:**
  - Backward compatibility? [Yes / No – if no, describe migration path]
  - Security implications?
  - Economic implications?
**Alternatives considered:** [What else was considered? Why this approach?]
**Simulation results:** [Link to staging test or data]
**Required vote:** [Simple majority / supermajority]
```

### Appendix B – Example Deprecation Notice

```markdown
**DEPRECATION NOTICE** – AIOS Component: `aios-confirmation-dialog` variant `destructive`

- **Reason:** Replaced by `aios-alert-dialog` with clearer accessibility semantics.
- **Recommended alternative:** `aios-alert-dialog` (variant `danger`).
- **Sunset date:** 2026‑10‑01 (90 days from today).
- **Action required:** Update any NodeContract referencing `aios-confirmation-dialog` with `variant: "destructive"` to use the new component. The DCP will issue warnings starting 2026‑07‑01.

Questions: contact governance@aios.dev
```

### Appendix C – Versioning Cheat Sheet for Developers

| I want to... | Version increment | Backward compatible? |
|--------------|------------------|----------------------|
| Fix a bug in a Skill (no API change) | PATCH | Yes |
| Add an optional field to NodeContract | MINOR | Yes |
| Remove a required field from PolicyRecord | MAJOR | No – Kits will break |
| Add a new MCP endpoint | MINOR | Yes (existing endpoints unchanged) |
| Change the fee cap from 2.5% to 3% | MAJOR (MPOA) | No – requires 90‑day notice |
| Deprecate a UI component | MINOR (mark `deprecated`) | Yes (still works for 90 days) |

---

**This policy is governed by the AIOS Governance Constitution (v1.0) and the Master Platform Operating Agreement (v3.0).**  
Amendments to versioning rules or the RFC process require a constitutional amendment (Constitution Art VI). Amendments to deprecation timeframes require a simple Council majority.
```