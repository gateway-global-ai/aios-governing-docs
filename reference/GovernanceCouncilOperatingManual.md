---
document_id: AIOS-REF-011
title: Governance Council Operating Manual
version: 1.0.0
status: draft
category: reference
author: Gateway Global
created: 2026-04-02
last_updated: 2026-04-02
reviewers: []
supersedes: null
cross_references:
  - { doc_id: "AIOS-CORE-002", relationship: "operationalizes" }
  - { doc_id: "AIOS-SPEC-009", relationship: "complements" }
  - { doc_id: "AIOS-COMM-002", relationship: "complements" }
amendment_history: []
---
# AIOS Governance Council Operating Manual v1.0.0

## 1. Purpose

This Operating Manual defines the **day‑to‑day procedures** of the AIOS Governance Council, as established by the **Governance Constitution (Article I)** . It translates the Constitution’s high‑level mandates (quorum, voting, audits, emergency powers) into actionable workflows. All Council members, Tenants, Vendors, and Platform operators may refer to this manual to understand how governance decisions are made and how to engage with the Council.

The manual is a living document. Amendments follow the same legislative process as the Constitution (Article VI), with the exception of purely procedural updates (e.g., meeting template changes) that may be approved by a simple Council majority.

---

## 2. Council Composition & Terms (Constitution Art I)

| Branch | Seats | Term | Appointment / Election |
|--------|-------|------|------------------------|
| **OS Kernel Team** | 3 | 2 years, staggered | Appointed by Gateway Global CEO, confirmed by Council majority. |
| **Digital Governance Officers** | 3 | 2 years, staggered | Appointed by Gateway Global CISO/CLO, confirmed by Council majority. |
| **Enterprise Consortium** | Up to 5 | 1 year | Elected annually by active Tenants (one vote per Tenant). |

- **Staggered terms**: For the Kernel Team and Governance Officers, one seat expires every 8 months. Initial appointments are for 2, 16, and 24 months to create the stagger.
- **Vacancies**: Filled within 60 days (Constitution Art V). Interim members serve the remainder of the original term.
- **Removal**: A three‑quarters vote of the remaining members (excluding the member in question) for gross negligence, conflict of interest, or persistent absence (missing 3 consecutive meetings without excuse).

---

## 3. Meetings & Quorum

### 3.1 Regular Meetings
- **Cadence**: Weekly, 60 minutes, via secure video conference.
- **Time**: Wednesdays at 15:00 UTC (rotating to accommodate global members).
- **Agenda**: Published 48 hours in advance on the Council’s private channel (and, for non‑confidential items, a public‑facing summary).

### 3.2 Special Meetings
- Called by any two Council members, or by the Chair, with 24 hours’ notice.
- Purpose: emergency response (Section 7), urgent policy patches, or interim audits.

### 3.3 Quorum & Voting
- **Quorum**: At least two‑thirds of all voting members (Constitution Art I). For a 9‑member Council (3+3+3), quorum is 6.
- **Voting**: Simple majority of members present, unless the Constitution requires a supermajority (e.g., amendments, removal, override of Enterprise veto).
- **Proxy voting**: Not allowed. Members may attend remotely but must be present for the vote.
- **Abstention**: Counts as a “no” for quorum purposes but does not affect the majority calculation.

### 3.4 Meeting Minutes & Transparency
- Formal minutes are recorded, including all votes (individual member votes are anonymised in public summaries but preserved in the internal audit log).
- Within 5 business days, a **public summary** (excluding security‑sensitive details) is published to the `transparency_log` (Section 8).
- Full minutes are stored in the immutable audit log (Technical Manifesto Art VI) and retained for 7 years.

---

## 4. Decision‑Making Workflows

### 4.1 Standard Decisions (e.g., Tier 3 ratification, vendor audit, hotfix approval)
1. **Proposal** – Submitted by any Council member (or via a formal request from a Tenant/Vendor) using the standard template (Appendix A).
2. **Review** – The relevant branch lead assigns a primary reviewer. For technical proposals, the Kernel Team leads; for policy proposals, the Governance Officers.
3. **Discussion** – During a regular meeting (or asynchronous over 48 hours if non‑urgent).
4. **Vote** – Simple majority of members present, with quorum.
5. **Execution** – The decision is documented, and the relevant Platform team (e.g., DCP operators) is notified to implement.

### 4.2 Emergency Actions (Constitution Art IV)
- **Automated circuit breakers** – Triggered by the Policy Engine; Council is notified within 15 minutes.
- **Global Halt** – Requires two‑key authorization (one Kernel Team member + one Governance Officer). The halting members must convene an emergency meeting within 1 hour.
- **Emergency policy patch** – May be deployed by a simple majority of the Governance Officers alone (with immediate notification to the Kernel Team). The patch is time‑bound (max 7 days) and must be converted to a standard amendment or rolled back.

### 4.3 Constitutional Amendments (Constitution Art VI)
- **RFC** – Submitted to the Council public mailing list. Includes simulation results (breaking‑change analysis).
- **Enterprise Consortium comment period** – 30 days.
- **Vote** – Two‑thirds supermajority of the Council (all branches combined). If the Consortium vetoes (two‑thirds of Consortium members), override requires three‑quarters of the remaining branches.
- **Ratification** – Document version is incremented, and the change is published with a 90‑day effective notice (for economic/liability amendments, per MPOA Art VI).

---

## 5. Conflict of Interest (Constitution Art V)

### 5.1 Disclosure
- Upon joining the Council and annually thereafter, each member files a **Conflict of Interest Disclosure Form** (Appendix B) listing:
  - Any financial interest (equity, consulting fees, grants) in a Vendor or Tenant.
  - Any family relationship with a Vendor or Tenant executive.
  - Any other affiliation that could reasonably bias their decisions.
- Disclosures are maintained by the Council Secretary (a non‑voting administrative role).

### 5.2 Recusal
- A member must recuse themselves from any vote, audit, or discussion that directly involves an entity in which they have a disclosed interest.
- The recusal is recorded in the minutes. The remaining members still count toward quorum.
- Failure to recuse when required is grounds for removal (Section 2).

### 5.3 Annual Review
- The Council’s compliance with conflict rules is audited by an independent third party (e.g., a law firm) once per year. The audit report (redacted) is published in the transparency log.

---

## 6. Vendor & Tenant Engagement

### 6.1 Vendor Audits (Constitution Art III)
- The Council may audit any Vendor Kit at any time. Audits are conducted by the Digital Governance Officers, with technical assistance from the Kernel Team if needed.
- **Procedure**:
  1. Notice sent to Vendor (except when immediate security threat exists).
  2. Vendor has 14 days to provide evidence of compliance (code, logs, third‑party attestations).
  3. If violations are found, the Council issues a remediation deadline (typically 14 days).
  4. If remediation fails, the Council may revoke the Kit’s signature (following due process).

### 6.2 Tenant Requests & Appeals
- Tenants may submit formal requests (e.g., for a policy variance, or to challenge a Council decision) via the Governance Council portal.
- The Council must acknowledge within 5 business days and provide a written decision within 30 days.
- Appeals of Kit revocation or other adverse actions go to independent arbitration as per MPOA Art IX.

### 6.3 Annual Enterprise Consortium Election
- **Eligibility**: Any Tenant that has been active for at least 3 months and has paid all outstanding fees.
- **Election timeline**:
  - November 1: Call for nominations.
  - November 15: Ballots sent to all eligible Tenants (one vote per Tenant).
  - December 1: Polls close. The top 5 candidates (by vote count) become the Consortium for the following calendar year.
  - December 15: Inaugural meeting of the new Consortium.
- **Term**: January 1 – December 31.

---

## 7. Emergency Response Playbook

This section operationalises Constitution Article IV (Emergency Powers).

### 7.1 Severity Levels

| Level | Description | Response |
|-------|-------------|----------|
| **Level 1 – Minor** | Single vendor API timeout, no customer impact. | Automated circuit breaker; notification to Council (no meeting required). |
| **Level 2 – Moderate** | Multiple vendors affected; some users see fallback UI. | Emergency meeting within 4 hours. Council may issue a hotfix. |
| **Level 3 – Severe** | Potential data breach, ongoing denial‑of‑wallet attack, or Global Halt triggered. | Immediate Global Halt (if not already activated). Full Council meeting within 30 minutes. Post‑mortem mandatory. |

### 7.2 Step‑by‑Step for a Level 3 Incident

1. **Detection** – Policy Engine or monitoring system alerts the on‑call Council member (rotating weekly).
2. **Triage** – On‑call member assesses severity. If Level 3, they invoke the **Global Halt** (requires a second member’s key).
3. **Containment** – The Halt pauses all Kit executions, and the UI shows “System Maintenance.” Forensic snapshots are taken.
4. **Emergency Meeting** – All Council members join a secure bridge. The Kernel Team lead presents evidence.
5. **Decision** – Options:
   - **Rollback** to a previous known‑good state (using immutable rollback).
   - **Apply a hotfix** (policy patch or vendor blacklist).
   - **Remain halted** until root cause is understood (max 24 hours, renewable by supermajority).
6. **Restoration** – Once the threat is neutralised, the Council votes to lift the Halt (simple majority).
7. **Post‑Mortem** – Within 14 days, the Council publishes an incident report (redacted for security) covering:
   - Timeline.
   - Root cause.
   - Impact (data, financial, operational).
   - Remediation steps and long‑term prevention.
   - Any changes to the Constitution or procedures.

### 7.3 On‑Call Rotation
- A roster of Council members (one from each branch) serves as the **primary on‑call** for a given week.
- The on‑call member has the authority to convene an emergency meeting and initiate a Level 2 response. A Level 3 response always requires a second member (two‑key).

---

## 8. Transparency Log

The Council maintains a **public transparency log** at `{{GATEWAY_TRANSPARENCY_URL}}`. The log is append‑only and cryptographically signed. It includes:

| Entry Type | Contents | Publication Delay |
|------------|----------|-------------------|
| **Meeting summaries** | Date, agenda, decisions, votes (anonymised). | Within 5 business days. |
| **Tier 3 ratifications** | Which Kit or policy was ratified, by whom (role, not name). | Within 7 days. |
| **Audit reports** | Vendor audit outcomes (sanitised). | Within 30 days of completion. |
| **Incident reports** | Post‑mortem for Level 2 and 3 incidents. | Within 14 days of incident closure. |
| **Conflict disclosures** | Aggregate statistics (e.g., “3 members recused from Vendor X votes”). | Annually. |

The log is accessible to all Tenants, Vendors, and the public. It does not contain personal data or trade secrets.

---

## 9. Appendices

### Appendix A – Proposal Template (Standard Decision)

```markdown
**Proposal ID:** `P-YYYY-MM-DD-XXX`
**Title:** [Short description]
**Type:** [Ratification | Audit | Hotfix | Policy Change | Other]
**Submitted by:** [Name, Branch]
**Date:** YYYY-MM-DD
**Affected documents/artifacts:** [e.g., Kit ID, NodeContract, PolicyRecord]
**Summary:** [2‑3 sentences]
**Rationale:** [Why this is needed]
**Impact assessment:** [Security, economics, backward compatibility]
**Proposed resolution:** [Exact text of the decision or change]
**Vote deadline:** [If asynchronous, date; else “meeting of date”]
```

### Appendix B – Conflict of Interest Disclosure Form (Template)

```markdown
**Disclosure ID:** `COI-{member}-{year}`
**Member name:** [Name, Branch]
**Date:** YYYY-MM-DD

**I declare the following relationships with AIOS Tenants, Vendors, or competitors:**

- **Entity name:** [Name]
- **Nature:** [Equity, consulting, employment, family, other]
- **Value:** [If financial, approximate range: <$10k, $10k‑$100k, >$100k]
- **Date of acquisition/start:** YYYY-MM-DD

**I understand that I must recuse myself from any Council matter directly involving the above entities.**
**Signature:** [Digital signature or verified email]
```

### Appendix C – Emergency Contact List (Internal)

| Role | Name | Secure Contact (Signal / PGP) |
|------|------|-------------------------------|
| Council Chair (rotating annually) | (to be filled) | |
| Kernel Team on‑call | (to be filled) | |
| Governance Officer on‑call | (to be filled) | |
| Incident Response Coordinator | (Platform CISO) | |

*(This appendix is not published in the transparency log.)*

---

**This Operating Manual is governed by the AIOS Governance Constitution (v1.0).**  
Procedural amendments (e.g., meeting cadence, form templates) may be approved by a simple Council majority. Substantive changes (e.g., modification of voting thresholds, emergency powers) require a constitutional amendment.
