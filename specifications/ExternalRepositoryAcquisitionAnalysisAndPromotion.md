---
document_id: AIOS-SPEC-013
version: 0.1.1
status: draft
category: specification
title: External Repository Acquisition, Analysis, and Promotion
author: Gateway Global AIOS
created: 2026-04-05
last_updated: 2026-04-05
reviewers: []
supersedes: null
cross_references:
  - doc_id: AIOS-CORE-002
    title: Governance Constitution
  - doc_id: AIOS-SPEC-003
    title: AIOS Agent Integration Protocol (AIP)
  - doc_id: AMD-2026-005
    title: Workspace Model & Governed Interface Surfaces
  - doc_id: AMD-2026-011
    title: External Repository Acquisition, Quarantine, Promotion, and Minimal Governance Execution Dependencies
amendment_history:
  - version: 0.1.1
    date: 2026-04-05
    summary: "AMD-2026-011 cross-references — acquisition path §2.2, minimal execution dependency §2.5; §9 operational-use wording."
---

# AIOS-SPEC-013 — External Repository Acquisition, Analysis, and Promotion

## 0. Status and scope

| Field | Value |
|-------|--------|
| **Status** | `draft` — normative interfaces and lifecycle; storage backend and tooling **out of scope** for this version |
| **Binds** | **[AMD-2026-011](../amendments/AMD-2026-011.md)** principles; this specification defines **contracts** and **classes** implementations **SHALL** honor |
| **Non-goals (v0.1)** | Vendor-specific CI products; long-term blob store design; conflation with **MCP** runtime tools or **governance document** authoring workflows |

This specification does **not** require a particular database or object store. Records **may** live in governed artifacts, operator stores, or future platform services, provided the **evidence** and **fields** below are satisfied.

---

## 1. Acquisition intent contract

**Acquisition intent** is a **declared, attributable** request to obtain an external repository (or revision thereof) for governed processing.

At minimum, an acquisition intent **SHALL** identify:

| Element | Requirement |
|---------|-------------|
| **Subject** | Source URL or equivalent locator |
| **Actor / tenant context** | Who or what initiated (aligned with **AIOS-SPEC-003** intent and audit models) |
| **Purpose class** | Evaluation, dependency study, or other allowed purpose — not free-form ad hoc import |
| **Timestamp** | Immutable record of when intent was emitted |

**SHALL NOT:** substitute intent with silent manual clone into governed or production runtime trees as a **standing** practice (see **AMD-2026-011** §2.2).

---

## 2. Quarantine-by-default rule

Every acquired external repository **SHALL** enter **quarantine** first: no operational binding, no default runtime selection, no system-wide reuse until **analysis** and **promotion** criteria for the target class are met.

Quarantine **SHALL** be enforceable as a **promotion class** (see §8, **quarantine**) distinct from **evaluation**, **sandbox**, and **approved**.

---

## 3. Analysis requirements

Before promotion beyond **quarantine**, the system **SHALL** complete **analysis** appropriate to **execution / risk class**, including at minimum:

- **License compatibility** against platform policy
- **Dependency and supply-chain** review (manifests, known-vulnerable patterns — method is implementation-defined)
- **Secret exposure** review (names of required env vars / secret slots; not values)
- **Network / API egress** inventory where relevant
- **Capability classification** alignment (see machine-readable record, §5–§7)

Analysis outcomes **SHALL** be recorded as **evidence** (§10).

---

## 4. Machine-readable repository specification

For each acquired repository, the platform **SHALL** maintain a **machine-readable** record (single JSON/YAML document or equivalent bundle) containing at least the fields in §§5–§7. The record **SHALL** be **versioned or timestamped** on change.

This specification does **not** mandate a single file path; it mandates **content and traceability**.

---

## 5. Authoritative documentation URL capture

The record **SHALL** include **authoritative documentation URLs** (project docs, security advisories, license references) separate from the **source URL**. Stale or unverifiable URLs **SHALL** be flagged in analysis evidence.

---

## 6. Dependency, environment, and API extraction

The record **SHALL** include:

| Category | Content |
|----------|---------|
| **Runtime dependencies** | Dependency manifests as applicable (lockfiles, package lists, or declared equivalents) |
| **Environment / secrets** | **Names** and **purpose** of required environment variables or secret slots — **never** secret values in the record |
| **External APIs / services** | Identifiers and purpose (e.g. cloud APIs, payment, identity) |

---

## 7. Execution and risk class

Each record **SHALL** carry **execution / risk class** (blast radius, data sensitivity, sandboxing needs). Promotion rules **SHALL** be stricter for higher risk.

---

## 8. Promotion classes

The following **promotion classes** define allowed states. Implementations **MAY** map internal states to these labels; labels **SHALL** be preserved in audit evidence.

| Class | Meaning |
|-------|---------|
| **quarantine** | Acquired; no operational use; isolated from production paths |
| **evaluation** | Under active analysis; may run in isolated evaluation environments only — **not** production |
| **sandbox** | Bounded execution in controlled sandbox (policy-defined); still **not** general operational reuse |
| **approved** | Cleared for defined operational use within **scope** (environment, version pin, tenant) |
| **vendored / reusable** | Approved for **broader** reuse (e.g. shared library, submodule policy) — **requires** explicit promotion and may require **ratification** per **AIOS-CORE-002** / **AIOS-SPEC-003** |

Transitions **SHALL** be **forward-only** through analysis and policy gates unless a **documented rollback** is recorded.

---

## 9. Prohibition on direct operational use before promotion

Operational use is prohibited before promotion except where policy explicitly permits sandbox-class use.

**SHALL NOT:** conflate “developer preview” on a workstation with **approved** promotion without evidence.

---

## 10. Audit and evidence requirements

The following **SHALL** be auditable:

- Emission of **acquisition intent**
- Transitions between **promotion classes** (who/what, when, rationale pointer)
- **Analysis** artifacts (summaries, tool outputs references — not necessarily raw logs in-repo)
- **Ratification** or Council-equivalent artifacts when **vendored / reusable** or system-wide normative use is claimed

Evidence **SHALL** satisfy **AIOS-SPEC-003** audit and emission expectations where applicable.

---

## 11. Relationship to future ingestion and sandbox systems

Future **ingestion pipelines**, **sandbox orchestrators**, or **MCP-adjacent** tooling **SHALL** implement this specification’s contracts; they **MUST NOT** replace **acquisition intent** or **promotion** with ad hoc copy operations. **Governance documents** (this repository’s markdown) and **runtime execution** (e.g. Workspace MCP) remain **separate planes**; acquisition of **external code** is **design-time / platform** governance unless explicitly bridged by policy.

---

## 12. Implementation alignment (non-normative)

- **Governance CI** in this repository follows **minimal execution dependency** (**AMD-2026-011** §2.5): integrity checks use **narrow** Python dependencies — illustrative of the principle; **not** a substitute for acquisition tooling.
- **Peer review** of this specification and **AMD-2026-011** should proceed together or in close sequence so principles and contracts stay aligned.

---

**This specification is governed by the AIOS Governance Constitution (AIOS-CORE-002) and complements AMD-2026-011.**
