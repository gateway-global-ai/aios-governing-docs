# Manual peer review packet — **AMD-2026-008-ADD-003** **`draft` `0.14.5`**

## How to use this file

1. **Upload this entire file** to ChatGPT (or another reviewer) as a single attachment.
2. Ask the model to follow **Round 1**, **light rubric**, **editorial + governance** focus (same role as automated OpenAI in `peer_review.py`).
3. **Output** must be **paste-back ready** for the repo: **YAML front matter** (see template below) + **scorecard table** + **short narrative**.

## Reviewer focus (editorial / cross-document coherence)

- Check cross-references and seams (**ADD-001**, **ADD-002**, **MPOA**, **OPS-020** where bundled).
- Terminology and **SHALL**/**MUST** discipline; ambiguity; density where it blocks understanding.
- You still **score every dimension** in the light rubric below.

## Output template (copy and fill)

```yaml
---
review_id: REV-AMD-2026-008-ADD-003-MANUAL-002
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.5
reviewer: OpenAI
review_source: manual_chatgpt
review_date: YYYY-MM-DD
review_round: 1
review_type: editorial
disposition: approved_with_changes | major_revision_required | approved
composite_score: 0.0
---
```

Then: **`## Grading Scorecard (light rubric)`** table (5 dimensions + composite mean), **`## Overall assessment`**, **`## Top actions`** (if any).

**Gate context (informational):** [AMD-2026-005](https://github.com/gateway-global-ai/aios-governing-docs/blob/main/amendments/AMD-2026-005.md) expects composite **≥ 3.5** and **no dimension below 3** for triangulated review.

---

## Grading rubric (light)

# AIOS Peer Review Grading Rubric (Light)

This is the lightweight 5-dimension rubric for specification and reference documents. For core documents (Manifesto, Constitution, MPOA), use the full 11-dimension rubric.

---

## Scale Definition (All Dimensions)

| Score | Label | Meaning |
|:-----:|-------|---------|
| **5** | Exemplary | Sets the standard. No issues found. Could be cited as a reference for other documents. |
| **4** | Strong | Meets all requirements with only minor stylistic or editorial suggestions. No substantive gaps. |
| **3** | Acceptable | Functionally sound but has identifiable gaps, ambiguities, or inconsistencies that should be addressed before ratification. |
| **2** | Major Issues | Significant problems that undermine the document's purpose. Requires substantial revision in this dimension. |
| **1** | Critical Failure | Fundamentally broken in this dimension. Contains contradictions, missing critical sections, or actively conflicts with other governing documents. |

---

## Dimension Definitions

### 1. Cross-Document Consistency

Does this document use terminology, defined terms, and structural patterns consistent with the governing set? Does it reference other documents by correct title, Article, and Section? Does it use the canonical glossary from the Technical Manifesto Appendix without inventing new terms or redefining existing ones?

**Score 5:** Every term matches the glossary. Every cross-reference cites the correct Article/Section.
**Score 3:** Most terms are correct but 2-3 inconsistencies exist.
**Score 1:** Invents new terms that conflict with the glossary. References documents by wrong names.

### 2. Completeness

Does this document cover everything its entry in the document plan promises? Are there sections that the plan describes but the document omits? Are edge cases addressed? Are failure modes defined?

**Score 5:** Covers every item described in the plan. Edge cases addressed. Failure modes defined.
**Score 3:** Covers the core requirements but omits 2-3 items. Some edge cases unaddressed.
**Score 1:** Missing entire sections promised by the plan. No failure mode definitions.

### 3. Practical Operability

Could a real developer, enterprise customer, or AI agent actually follow these rules? Are SLAs specific (numbers, not "timely")? Are processes step-by-step? Are thresholds defined?

**Score 5:** Every rule is actionable. SLAs have specific numbers. Ready for day-one use.
**Score 3:** Most rules are actionable but 2-3 provisions are too abstract to implement.
**Score 1:** Rules are aspirational rather than operational. SLAs are vague.

### 4. Conflict Freedom

Does this document contradict any other governing document? Does it respect the Supremacy Clause (Constitution for governance, MPOA for liability/economics, Manifesto for architecture)?

**Score 5:** No contradictions with any other document. Supremacy Clause respected.
**Score 3:** No direct contradictions but 1-2 provisions create tension.
**Score 1:** Direct contradictions with other governing documents.

### 5. Style & Clarity

Does the writing follow the Style Guide? Is it precise and unambiguous? Free of marketing language in specification contexts? Correct heading hierarchy?

**Score 5:** Perfect adherence to the Style Guide. Precise, unambiguous, well-structured.
**Score 3:** Generally follows the Style Guide but has 3-5 formatting inconsistencies.
**Score 1:** Does not follow the Style Guide. Marketing language in specifications.

---

## Composite Score Calculation

The composite score is the arithmetic mean of all 5 dimension scores, rounded to one decimal place.

## Disposition Rules

| Disposition | Criteria |
|-------------|----------|
| **Approved** | No dimension below 4. Composite >= 4.0. |
| **Approved with Changes** | No dimension below 3. Composite >= 3.5. |
| **Major Revision Required** | Any dimension at 1, OR two or more dimensions at 2, OR composite below 3.0. |

---

**This rubric is governed by the AIOS Governance Constitution (v1.0).**


---

## Primary document — **AMD-2026-008-ADD-003** **`0.14.5`**

---
document_id: AMD-2026-008-ADD-003
parent_amendment: AMD-2026-008
parent_version: 1.0.0
version: 0.14.5
status: draft
category: amendment_addendum
title: Composition Control Plane for Messages, Invites, and Documents
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008
    title: Sovereign Voice and Local Runtime Lanes (Incorporation by Reference)
  - doc_id: AMD-2026-008-ADD-001
    title: Base Shell Navigation Primitives and Start-Here Control
  - doc_id: AMD-2026-008-ADD-002
    title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
  - doc_id: MPOA
    title: Master Platform Operating Agreement
    note: Commercial tiers, entitlements, and liability for send/publish actions.
  - doc_id: AIOS-COMPOSITION-CONTROL-RD-NOTES-001
    title: Composition control plane — R&D and knowledge capture (AMD-2026-008 addendum track)
    note: Informative; non-normative intake / process capture.
  - doc_id: AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001
    title: Composition control plane — architecture memo (bounded domains and addendum seams)
    note: Informative; doctrinal seams and dependency map.
  - doc_id: AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001
    title: Shell and composition — surface grammar and user-state memo (AMD-2026-008 addendum track)
    note: Informative; doctrine-to-surface mapping.
  - doc_id: AMD-2026-008-ADD-003-ANNEX-A
    title: ADD-003 Annex A — Informative composition and knowledge-basis examples
    note: Informative JSON; moved from §5.7 and §18.9.
  - doc_id: ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD
    title: Originality and Source-Boundary Verification (Implementation Home)
    note: AIOS-OPS-020 — metrics, thresholds, evaluation record schema, DCP; default home for §19.4(b)/§19.10.
addendum_history:
  - version: 0.14.5
    date: 2026-04-10
    summary: §5.9 fail-closed → default DCP codes (AIOS-OPS-020 §13 COMP_* + ORIG_REJECT_MISSING_EVAL); keeps doctrine thin, ops binding concrete.
  - version: 0.14.4
    date: 2026-04-10
    summary: §16.7 seam — ADD-002 owns depth/VC; shell applies settings without §16 “owning” enforcement; §18.11 OPS record ties to artifact/knowledge basis; §19.2 policy silence fail-closed; §19.10 minimum AIOS-OPS-020 conformance surface (§§6–10, Appendix A, policy_pack_id).
  - version: 0.14.3
    date: 2026-04-10
    summary: §9.4.0 professional-use trigger determinism (subclass/policy/precedence); §17.7 measurement accuracy vs MPOA liability; §1 Purpose split for readability (Gemini-style polish).
  - version: 0.14.2
    date: 2026-04-10
    summary: Seam hardening — §18 vs §19 scope; §18.11 pointer to OPS-020 §6–§9; §19.10 conformance names OPS version; §20.14 adherence does not bypass §19/OPS thresholds.
  - version: 0.14.1
    date: 2026-04-10
    summary: §19.2 bridge to §19.9 (non-waiver vs enforcement); §19.4/§19.10 bind default implementation home ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD (AIOS-OPS-020); YAML last_updated aligned with created (metadata hygiene).
  - version: 0.14.0
    date: 2026-04-08
    summary: §19 enforcement posture—channel evaluation, bounded outcomes, policy threshold/spec handoff (§19.10); §5.9 fail-closed rejection semantics; internal_only state in §19.5.
  - version: 0.13.0
    date: 2026-04-10
    summary: §16.7 seam hardening (language does not alter depth/VC); §9.4.3(5) export disclosure block/warn; §19.4 external stricter SHALL + §19.9 non-dilution; §5.9 normative field/validation table; §2/§5 density trim.
  - version: 0.12.0
    date: 2026-04-10
    summary: §2.1 addendum seams vs ADD-001/ADD-002; §16.7 de-duplicate depth/VC (ADD-002 owns definitions); §18.11 gate stack A/B; Annex A for informative JSON; aligns AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.
  - version: 0.11.0
    date: 2026-04-10
    summary: §0/§1 informative grounding pointers to AIOS-COMPOSITION-CONTROL-RD-NOTES-001, AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001, AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001; cross_references YAML.
  - version: 0.10.0
    date: 2026-04-10
    summary: Reference adherence controls (§20.11–§20.15) — not model temperature; 1–10 scale; optional structure/style split; innovation_mode; §19 safeguard at max adherence.
  - version: 0.9.0
    date: 2026-04-10
    summary: Reference-guided composition (§20) — template vs reference vs authority; R1–R3 roles; reference_documents/mode/role; ties to §5/§18/§19/§9.4; twelve-axis table.
  - version: 0.8.0
    date: 2026-04-10
    summary: Originality & source-boundary gate (§19) — non-reproduction verification; not copyright guarantee; internal vs external thresholds; verification states; KB extraction rule; eleven-axis table.
  - version: 0.7.0
    date: 2026-04-10
    summary: Knowledge basis & discovery gating (§18) — sufficiency states; discovery-before-creation; creation mode; grounding tiers; ten-axis table; aligns with §5/§17/§9.4/BOOK.
  - version: 0.6.0
    date: 2026-04-10
    summary: Measurement contract (§17) — method, unit, basis, precision; mandatory confirmation for material quantities; scaffold/estimate paths; nine-axis table.
  - version: 0.5.0
    date: 2026-04-10
    summary: Language, localization, authoritative version (§16) — L0–L3 modes; translation_mode; authoritative_language; professional translation review; shell/voice; eight-axis table.
  - version: 0.4.0
    date: 2026-04-10
    summary: Professional-use draft disclosure (§9.4) — licensed-professional document classes; mandatory disclosure text; SHALL NOT finality; export preservation; metadata fields; MPOA alignment.
  - version: 0.3.0
    date: 2026-04-10
    summary: Composition contract — responsive vs procedural vs composed; mandatory role/intent/outcome for Class 3; scaffold-only when ambiguous; EMAIL/invite/research/book special cases; JSON examples informative; seven-axis summary table.
  - version: 0.2.0
    date: 2026-04-10
    summary: Expanded composition plane — EMAIL, CALENDAR_INVITE; DOCUMENT subclasses; publication classes; action semantics (draft/send/publish vs export); action-bearing vs file outputs; shell controls per class; cross-ref ADD-002 depth/VC/packaging/BOOK gates.
  - version: 0.1.0
    date: 2026-04-10
    summary: Prior scope — publication-oriented artifact labels (A0–A5); superseded as primary structure by 0.2.0 family taxonomy; substance retained under §6–§7.
---

# AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## 0. Status and intent

| Field | Value |
|-------|--------|
| **Status** | **`draft` `0.14.5`** — addendum to **[AMD-2026-008](AMD-2026-008.md)** **1.0.0** |
| **Does not replace** | **[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)** (navigation), **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** (output depth, shell voice controls, **packaging classes**, **BOOK** workflow, **premium** gates). This addendum defines **what** is being composed, **composition contracts** (**role**/**intent**/**outcome**), and **which actions** may execute—**not** interchangeable freeform text. |
| **Informative grounding** (**not** **law** **here**) | **[AIOS-COMPOSITION-CONTROL-RD-NOTES-001](../reference/implementation/AIOS-COMPOSITION-CONTROL-RD-NOTES-001.md)** (R&D / process capture), **[AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001](../reference/implementation/AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.md)** (bounded domains / seams), **[AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001](../reference/implementation/AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001.md)** (shell / surface mapping). |

---

## 1. Purpose

This addendum defines the **composition control plane** for governed **artifact creation** on AI OS surfaces: **messages**, **calendar invites**, **documents** (including **subclasses**), and **publication**/**distribution** artifacts. It specifies **responsive** vs **procedural** vs **composed** output classes and the **composition contract** (**role**, **intent**, **outcome**) for **non-trivial** composition (**Section 5**).

It **SHALL** also govern **professional-use draft disclosure** for **licensed-professional** document classes (**§9.4**); **language**, **localization**, and **authoritative** multilingual version rules (**§16**); **measurement contracts** for **quantified** claims (**§17**); **knowledge basis** and **discovery** **gating** before **substantive** creation (**§18**); **originality**, **source-boundary**, and **non-reproduction** verification for **source-derived** composed artifacts (**§19**); and **reference-guided** composition—**example**, **template**, or **authority** materials used to shape **spirit**, **structure**, and **form** without authorizing **wholesale** **reproduction** (**§20**; **reference** **adherence**/**conformity** **controls** **§20.11**–**§20.15**, **not** **model** **temperature**).

It **SHALL** be read with **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** for **depth**, **voice controls**, **packaging**, and **BOOK**-specific gates. **Informative** **only** **(no** **additional** **SHALL**/**MUST** **obligations**)**:** **AIOS-COMPOSITION-CONTROL-RD-NOTES-001**, **AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001**, **AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001** **(§0** **table**)** **—** **context** **for** **partitioning** **and** **surface** **grounding**.

## 2. Governing principle

**Artifact generation** **SHALL** follow **composition** **class**, **structure**, and **action** **semantics**—**not** **generic** **length**-scaled **text**. The runtime **SHALL** **keep** **message**, **invite**, **document**, and **publication** **artifacts** **distinct**.

**Composition** **class** **SHALL** **not** **be** **inferred** **from** **packaging** **alone**. **Output** **depth** (**[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§4**) **remains** **orthogonal** **to** **composition** **class** **(this** **addendum** **owns** **class** **labels**).**

For **action-bearing** **artifacts**, **composition** **SHALL** **stay** **separate** **from** **execution** (**draft**/**review**/**approve** **vs** **send**/**publish**).**

### 2.1 Addendum seams (normative for authors)

- **Output depth** (**RESPONSE** … **BOOK**), **shell** **voice** **controls** (**VC0**–**VC5**), and **packaging** **classes** **SHALL** **be** **used** **as** **defined** **in** **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§4**, **§5**, **§7**; **this** **addendum** **SHALL** **not** **redefine** **those** **labels** **or** **ladder** **semantics**.
- **Navigation** **primitives** **SHALL** **follow** **[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**; **this** **addendum** **SHALL** **not** **redefine** **them**.
- **Composition** **classes**, **composition** **contracts**, **and** **action** **semantics** **for** **artifacts** **SHALL** **be** **owned** **here** (**or** **policy** **downstream**); **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **SHALL** **not** **define** **composition** **class** **taxonomies** (**see** **[AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001](../reference/implementation/AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.md)** **bounded** **domains** **table**).

## 3. Composition class versus packaging and execution

| Dimension | Role |
|-----------|------|
| **Composition class** | What kind of artifact (email vs report vs book); **structure** and **action** semantics |
| **Packaging / export** (**ADD-002** §7) | **TXT**, **MD**, **PDF**, **DOCX**, **JSON**, **HTML** — **file** or render form |
| **Execution / action** | **Send email**, **create invite**, **publish post** — **not** merely a file save |

Example: a **RESEARCH_REPORT** **MAY** export as **MD**, **PDF**, or **DOCX**. An **EMAIL**’s **primary** path is **message action** (draft/send); exporting text to **PDF** **MAY** exist but **SHALL NOT** substitute for **send** semantics. A **CALENDAR_INVITE** is a **scheduled coordination artifact**, not primarily a document export.

## 4. Responsive, procedural, and composed outputs

The runtime **SHALL** distinguish **responsive** and **procedural** outputs from **composed artifacts**. This section is **normative** for **gating** (Section 5).

### 4.1 Class 1 — Responsive outputs

**Direct answers**, **summaries**, **short explanations**, **procedural next steps**, **quick recommendations**. These **MAY** often be produced **without** a full **composition contract** (Section 5) when the **request** is **immediate**, **bounded**, and **non-persistent**.

Examples (illustrative): answer, summary, explanation, step list, procedural instruction.

### 4.2 Class 2 — Procedural outputs

**Checklists**, **task steps**, **intake sequences**, **navigation prompts**, **setup guidance**. These **MAY** require **partial** contract (**intent**, **outcome**) depending on **stakes** and **policy**; **role** **MAY** be lighter than for **Class 3**.

### 4.3 Class 3 — Composed artifacts

**Emails**, **calendar invites**, **documents** and **subclasses**, **articles**, **blogs**, **research reports**, **proposals**, **policies**, **business plans**, **books**, **marketing assets**, **investor updates**, and other **non-trivial** **persistent** or **action-bearing** artifacts.

**Class 3** **SHALL** require an explicit **composition contract** (Section 5) before **substantive** drafting, **send**, **publish**, or **export as formal artifact**—except **scaffold-only** output per **Section 5.4**.

## 5. Composition contract requirements

For outputs **beyond** **responsive** or **procedural** classes—or when **policy** requires it—the runtime **SHALL** establish a **composition contract** before **drafting beyond** the **minimum viable scaffold** (**Section 5.4**).

### 5.1 The triad: role, intent, outcome

| Field | Meaning |
|-------|--------|
| **Role** | **Who** is speaking or authoring (e.g. founder, operator, policy author, analyst, executive assistant, brand voice). Governs **authority**, **tone**, and **responsibility**. |
| **Intent** | **Why** the artifact exists (e.g. inform, request, persuade, document, analyze, propose, coordinate, approve, publish, teach). Reduces **generic** overproduction. |
| **Outcome** | **What completed state** the artifact **SHALL** drive (e.g. meeting booked, stakeholder approves, reader understands, policy ratified, manuscript reaches chapter gate). Prevents **well-formed** text that **does not move** the situation. |

**Optional** fields (often useful): **audience**, **tone**, **distribution target**, **approval level**, **action mode** (e.g. **DRAFT_ONLY** for email). For **professional-use** artifacts, **§9.4.5** fields (**professional_review_required**, **professional_domain**, **artifact_status**) **SHALL** apply when **policy** or **classification** triggers **§9.4**.

### 5.2 Normative doctrine

**Composed** **artifacts** (**§4.3**) **SHALL** **have** **role**, **intent**, **and** **desired** **outcome** **(or** **bounded** **provisional** **derivation**)** **before** **substantive** **drafting** **beyond** **§5.4** **scaffold**. **Responsive**/**procedural** **outputs** **MAY** **omit** **a** **full** **contract** **when** **§4.1**/**§4.2** **and** **policy** **allow**.

If **role**/**intent**/**outcome** **are** **ambiguous**, **the** **runtime** **SHALL** **clarify**, **derive** **a** **tight** **provisional** **contract**, **or** **stay** **at** **scaffold** **—** **SHALL** **not** **ship** **false** **finality**.

### 5.3 When the contract is required (composed outputs)

Before **full** drafting, **send**, **publish**, **export as formal artifact**, or **book**/**report**/**article** generation, the **composition contract** **SHALL** be **satisfied** for **Class 3** (Section 4.3), except **scaffold** paths (**Section 5.4**).

### 5.4 Scaffold-only boundary

If the contract is **missing** or **incomplete**, the system **MAY** still produce **useful** output **only** at **scaffold** level, including (illustrative): proposed **subject lines**, **outline**, **invite purpose**, **article angles**, **book TOC** proposal, and **measurement** placeholders when **§17** applies—**SHALL NOT** present such output as **final** or **send-ready** without contract resolution.

### 5.5 Special cases — EMAIL and CALENDAR_INVITE

**EMAIL** and **CALENDAR_INVITE** **SHALL** include, at minimum, **role**, **intent**, **outcome**, and **recipient**/**meeting** context (**meeting purpose** for invites). They are **transactional** artifacts (**Section 3**), not plain text blobs.

### 5.6 Special cases — RESEARCH_REPORT and BOOK

**RESEARCH_REPORT** and **BOOK** **SHALL** require **role**, **intent**, **outcome**, **audience**, **scope**, and **approval path** (or pointer to **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **BOOK** gates) before **substantive** composition—**policy** **MAY** add fields.

### 5.7 Informative composition contract object (non-normative)

Products **MAY** serialize the contract (e.g. JSON). **Illustrative** **examples** **(non-normative)** **—** **[Annex A](AMD-2026-008-ADD-003-ANNEX-A-informative-composition-examples.md)** **§1**.

### 5.8 Drift risks (informative)

Without a contract, implementations risk **tonal drift** (wrong **role**), **intent drift** (explain vs persuade vs request), and **outcome drift** (polished text that does not achieve the **end state**).

### 5.9 Normative fields and validation posture (compact)

**Products** **SHALL** **map** **these** **conceptual** **fields** **to** **implementation** **identifiers** **as** **needed**. **Policy** **SHALL** **define** **when** **missing** **or** **invalid** **fields** **block** **send**/**publish**/**export** **or** **force** **scaffold**/**review**.

| Domain | Minimum conceptual fields | Validation posture (normative intent) |
|--------|---------------------------|----------------------------------------|
| **Composition contract** (**§5**) | **role**, **intent**, **desired outcome**; **optional** per **§5.1** | **SHALL** **not** **treat** **Class** **3** **as** **send-ready**/**publish-ready** **without** **satisfied** **contract** **or** **explicit** **§5.4** **scaffold** **path**. |
| **Professional-use disclosure** (**§9.4.5**) | **`professional_review_required`**, **`professional_domain`**, **`artifact_status`** **when** **§9.4** **applies** | **SHALL** **not** **omit** **metadata** **or** **§9.4** **disclosure** **surface** **where** **required**; **export** **SHALL** **follow** **§9.4.3(5)**. |
| **Reference-guided composition** (**§20**) | **`reference_documents`**, **`reference_mode`**, **`reference_role`** **when** **references** **apply**; **adherence** **fields** **per** **§20.4** | **SHALL** **resolve** **or** **record** **disposition** **per** **§18.11** **step** **4** **before** **substantive** **drafting** **when** **references** **are** **in** **scope**; **§19** **before** **external** **publish**/**send**/**export** **when** **policy** **requires**. |

**This** **table** **does** **not** **replace** **JSON** **Schema**/**DCP** **in** **product** **—** **it** **states** **minimum** **governed** **field** **and** **gate** **expectations** **for** **auditable** **behavior**.

#### Fail-closed rejection semantics (normative)

**When** **policy** **or** **artifact** **class** **requires** **the** **corresponding** **fields** **or** **gates**, **the** **runtime** **SHALL** **fail** **closed** **as** **follows** **(not** **silent** **pass-through**)**:**

| Condition | Enforcement outcome |
|-----------|---------------------|
| **Mandatory** **composition** **contract** **fields** **missing** **or** **invalid** **where** **§5** **requires** **them** | **SHALL** **not** **proceed** **to** **substantive** **drafting** **except** **via** **explicit** **§5.4** **scaffold**/**outline** **path**. |
| **Professional-use** **disclosure** **metadata** **or** **§9.4** **surface** **missing** **where** **§9.4** **applies** | **SHALL** **not** **send**, **publish**, **or** **export** **as** **a** **professional-use** **draft** **without** **remediation** **or** **explicit** **policy** **exception** **where** **policy** **allows** **one** **;** **§9.4.3(5)** **applies** **to** **export**. |
| **Originality**/**source-boundary** **verification** **outcome** **missing**, **unknown**, **or** **not** **permitted** **for** **the** **target** **channel** **where** **§19.2** **requires** **a** **gate** **before** **release** | **SHALL** **not** **publish**, **send**, **or** **formally** **export** **to** **that** **channel** **until** **§19.5** **permits** **it** **per** **policy**. |
| **Knowledge** **basis** **insufficiency** **where** **§18** **requires** **grounding** **or** **discovery** **before** **full** **draft** **or** **external** **release** | **SHALL** **remain** **scaffold-only**, **blocked**, **or** **discovery-required** **per** **§18.5**/**§18.6** **—** **not** **silent** **promotion** **to** **full** **draft** **or** **external** **release**. |

**Exact** **error** **codes**, **serialized** **schemas**, **and** **DCP** **transport** **SHALL** **bind** **in** **implementation** **artifacts** **as** **policy** **defines** **(§19.10** **;** **default** **home** **AIOS-OPS-020)** **.** **Default** **DCP** **code** **names** **for** **the** **fail-closed** **rows** **above** **—** **[ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD](../operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md)** **§13** **(**`aios.dcp.composition`** **and** **§10** **originality** **cross-reference**)** **unless** **policy** **registers** **extensions** **.**

## 6. Control-plane axes (twelve axes summary)

| # | Axis | Governed by |
|---|------|-------------|
| **1** | **Navigation** | **[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)** |
| **2** | **Output depth** | **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** §4 (RESPONSE … BOOK) |
| **3** | **Shell voice controls** | **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** §5 (VC0–VC5) |
| **4** | **Packaging / export** | **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** §7–§8 |
| **5** | **Composition class** | **This addendum** §§7–10 — family + class identifiers |
| **6** | **Document subclass** | **This addendum** §9.2 — when the active class is **DOCUMENT** or document-shaped |
| **7** | **Composition contract** | **This addendum** §5 — role, intent, outcome (for composed artifacts) |
| **8** | **Language / localization** | **This addendum** §16 — output language, translation mode, authoritative version |
| **9** | **Measurement / quantified claims** | **This addendum** §17 — method, unit, basis, precision |
| **10** | **Knowledge basis / discovery** | **This addendum** §18 — sufficiency, discovery-before-creation, creation mode |
| **11** | **Originality / source-boundary** | **This addendum** §19 — non-reproduction verification, quote/quoting posture |
| **12** | **Reference-guided composition** | **This addendum** §20 — reference vs template vs authority; **adherence**/**conformity** to **shape** (not model **sampling**); **§20.11**–**§20.15** |

**BOOK**-depth workflow, **TOC**/**chapter** gates, and **premium** **BOOK** paths: **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** §10–§10.11.

## 7. Composition families

| Family | Description |
|--------|-------------|
| **Messages** | **Action-bearing** text; **send**/**draft** semantics (**§8.1**) |
| **Invites** | **Calendar** (and future: **task reminder** — not defined here) (**§8.2**) |
| **Documents** | Structured **internal**/**business** artifacts; **subclasses** (**§9**) |
| **Publications** | **POST**, **BLOG**, **ARTICLE**, **NEWSLETTER**, **REPORT** (public-facing), **BOOK** (**§10**) |

## 8. Message and invite classes

### 8.1 EMAIL

**EMAIL** **SHALL** support, at minimum, the following **conceptual fields** (product **MAY** map labels):

- **subject**
- **recipients** (to/cc/bcc as policy allows)
- **body** (with **body class** or template as policy defines)
- **tone** class or policy binding
- **thread context** for **reply** vs **new** message

**Action semantics** — the shell **SHALL** expose **distinct** controls for:

| Action | Meaning |
|--------|--------|
| **Compose draft** | Create or edit without sending |
| **Prepare reply** | Reply in thread per policy |
| **Request review / approve** | Where policy requires approval before send |
| **Send** | Execute delivery |
| **Schedule send** | Deferred send |
| **Archive / discard** | No send; exit without external delivery |

The system **SHALL NOT** conflate **draft** with **send**. **Send** **SHALL** require **explicit** invocation unless **policy** defines unattended automation.

### 8.2 CALENDAR_INVITE

**CALENDAR_INVITE** **SHALL** support, at minimum:

- **title**
- **attendees**
- **date**/**time** and **timezone**
- **location** and/or **meeting link**
- **description**
- **response** behavior (accept/decline/tentative) as provider allows

**Action semantics** — the shell **SHALL** distinguish:

| Action | Meaning |
|--------|--------|
| **Propose** / **draft invite** | No external issuance |
| **Send invite** | Issue to attendees |
| **Revise invite** | Update after issuance per provider rules |
| **Publish to calendar** | Place on calendar per product semantics |

### 8.3 Future message types (non-normative)

**SMS**, **CHAT_MESSAGE**, **INTERNAL_NOTE** **MAY** be added by future revision; this version **SHALL NOT** require implementations to support them.

## 9. Document composition

### 9.1 DOCUMENT (top-level)

**DOCUMENT** denotes **document-shaped** work products that are **not** primarily **EMAIL**, **CALENDAR_INVITE**, or **publication** **POST**/**BLOG**/**ARTICLE** in the same session—**policy** **MAY** map hybrids. **DOCUMENT** **SHALL** be refined by **subclass** (§9.2).

### 9.2 Document subclasses (normative identifiers)

Implementations **SHALL** map product types to these identifiers or extend only by **policy**-registered extensions.

| Subclass | Typical use |
|----------|-------------|
| **MEMO** | Internal decision memo |
| **LETTER** | Formal correspondence |
| **PROPOSAL** | Offer or plan of action |
| **BUSINESS_PLAN** / **PLAN** | Structured plan (product naming **MAY** vary) |
| **SPEC** | Technical or requirements specification |
| **POLICY** | Policy statement |
| **RESEARCH_REPORT** | Evidence-led analysis (see also **§10** if public) |
| **CHECKLIST** | Executable checklist |
| **MEETING_NOTES** / **MINUTES** | Notes or minutes |
| **AGENDA** | Meeting agenda |
| **BRIEF** | Short decision brief |
| **PACKET** | Bundled review packet |
| **CONTRACT_SUMMARY** | Non-substitute summary of legal text — **SHALL NOT** replace counsel; **§9.4** disclosure when professional-use |
| **SOP** | Standard operating procedure |
| **REPORT** | General report (non-research or internal) |
| **BOOK** | **Normative** **BOOK** process: **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** §10–§10.11 |

Each subclass **SHALL** have **required** and **optional** sections defined by **policy** or **template**; this addendum defines **identifiers** and **governance posture**, not full templates.

### 9.3 Subclass expectations (summary)

For each **subclass**, **policy** **SHALL** define minimum **structure**, **review** level, **one-pass** eligibility vs **gated** drafting, and default **packaging** (**ADD-002** §7). **RESEARCH_REPORT**, **POLICY**, **CONTRACT_SUMMARY**, and **BOOK** **SHALL** default to **stricter** review than **MEMO** or **CHECKLIST** unless **policy** relaxes for a tenant.

### 9.4 Professional-use draft disclosure

This subsection is a **mandatory disclosure rule** for a **class of composed outputs**, not an informal safety reminder. **§9.4.0** defines **how** **professional-use** **treatment** **is** **determined**. **Where** **that** **treatment** **applies**, **§9.4** **covers** **artifacts** **including** (illustrative): **legal** or **agreement** drafts, **CONTRACT_SUMMARY**, **POLICY** drafts, **compliance** memos, **filing-support** drafts, and **licensed-professional work-product** support documents.

#### 9.4.0 When professional-use applies (trigger determinism)

Whether an artifact **SHALL** be treated as **professional-use** **SHALL** be determined by **policy** using **evidence** in the following **order** unless **policy** defines a different **precedence** **with** **audit** **visibility**:

1. **Explicit classification** — user or tenant **declared** posture, **document subclass** (**§9.2**), and **composition** metadata such as **`professional_review_required`**, **`professional_domain`**, **`artifact_status`** (**§9.4.5**);
2. **Policy mapping** — **rules** that **bind** **subclasses**, **templates**, or **workflows** (e.g. **CONTRACT_SUMMARY**, **POLICY**, **RESEARCH_REPORT**) to **licensed-professional** contexts;
3. **Platform signals** — **prompt**, **template**, **workflow**, or **content** patterns **policy** **recognizes** as **professional-use**.

When **signals** **conflict** or **remain** **ambiguous** after **reasonable** **classification**, the runtime **SHALL** **apply** **§9.4** **draft** **posture** **and** **disclosure** **rather** **than** **assuming** **non-professional** use — **unless** **policy** **records** **a** **narrower** **rule** **with** **audit** **visibility**.

#### 9.4.1 Doctrine: three levels of assistance

The runtime **SHALL** distinguish:

| Level | Meaning |
|-------|--------|
| **General drafting assistance** | Ordinary composition help not positioned as professional instrument. |
| **Draft prepared for use by a licensed professional** | Output **positioned** for review by counsel, CPA, PE, clinician, etc. |
| **Final professional instrument** | **Approved** work product or **authoritative** instrument — **outside** default AI OS posture. |

AI OS **SHALL** operate only in the **first two** levels. AI OS **SHALL NOT** **represent** its output as the **third** solely on the basis of **AI generation**.

#### 9.4.2 Normative principle

AI OS **generates** professional-use documents as **drafts** for **review**. AI OS **does not** **guarantee** their **legal validity**, **enforceability**, **completeness**, **regulatory sufficiency**, or **fitness for use**, and **does not** **recommend** their **use** without **review** and **approval** by the **appropriate licensed professional**.

For any document generated for **potential use** by a **legal** professional or **other licensed** professional, the system **SHALL** **classify** the output as a **draft for professional review** unless a **separately governed workflow** (e.g. human sign-off, enterprise policy) **provides otherwise** and is **recorded** in **audit** surfaces.

The runtime **SHALL NOT** represent a **professional-use draft** as **final legal advice**, **final professional work product**, or **approved-for-use** documentation **solely** on the basis of **AI generation**.

#### 9.4.3 Runtime obligations

When an artifact **SHALL** be treated as **professional-use** per **§9.4.0**, **policy**, or **§9.4**, the runtime **SHALL**:

1. **mark** the artifact as a **draft** (not a final instrument);
2. **include** a **visible** **Professional Review Required** disclosure (§9.4.4);
3. **avoid** representing the artifact as **final** or **validated** by AI OS;
4. **avoid** **recommending** direct **reliance** or **use** without **licensed-professional** approval;
5. **preserve** the **§9.4** **disclosure** **in** **exported** **artifacts** **when** **the** **export** **format** **can** **carry** **it** **(e.g.** **MD**, **PDF**, **DOCX**, **HTML**)**; **when** **the** **chosen** **format** **or** **channel** **cannot** **embed** **or** **attach** **the** **disclosure** **in** **a** **governed** **way**, **the** **runtime** **SHALL** **either** **block** **the** **export** **or** **require** **an** **explicit** **blocking** **warning** **and** **user** **acknowledgment** **that** **downstream** **use** **without** **disclosure** **is** **the** **user’s** **responsibility** **before** **proceeding** **—** **SHALL** **not** **silently** **strip** **§9.4** **protections**.

#### 9.4.4 Mandatory disclosure text

**Default** (full) disclosure — **SHALL** be **available** and **SHALL** be used unless **policy** **narrows** wording without **weakening** the **obligations** in **§9.4.3**:

> **Professional Review Required**  
> This document was generated by AI OS as a draft prepared for review and possible use by a licensed professional. It has not been approved by an attorney or other licensed professional. AI OS does not guarantee the legal validity, enforceability, completeness, or fitness of this document for any particular use. Do not rely on or use this document without review and approval by the appropriate licensed professional.

**Compact** (header/footer) form — **MAY** be used where **UI** or **space** requires **if** the product **still** surfaces the **full** text or a **clear** link to it:

> **Draft for Professional Review Only.** Generated by AI OS for review by a licensed professional. Not guaranteed valid or fit for use without attorney or licensed-professional approval.

#### 9.4.5 Policy and composition metadata

**Policy** **SHALL** support, at minimum, the following **conceptual** fields so the **shell** and **export** layer **MAY** apply disclosure **automatically**:

| Field | Purpose |
|-------|--------|
| `professional_review_required` | **true** when **§9.4** applies |
| `professional_domain` | e.g. **legal**, **tax**, **compliance**, **medical**, **engineering**, **other_licensed** |
| `artifact_status` | e.g. **draft_for_professional_review** |

These **MAY** extend the **composition contract** (**§5**).

#### 9.4.6 Relationship to **MPOA** and product terms

**Commercial**, **liability**, and **tenant** terms **SHALL** remain subject to **[MPOA](../core/master_platform_operating_agreement.md)** and **product** agreements; **§9.4** states **minimum** **governance** and **disclosure** expectations for the **composition plane**.

## 10. Publication and distribution classes

| Class | Notes |
|-------|--------|
| **POST** | Short publishable surface (social/community) |
| **BLOG** | Long-form informal–semi-formal post |
| **ARTICLE** | Editorial / professional article |
| **NEWSLETTER** | Subscription or campaign publication |
| **REPORT** | Public or external **report** (distinct from internal **DOCUMENT.REPORT** when policy distinguishes) |
| **BOOK** | **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **BOOK** workflow |

**Premium** **enhancement** (images, layout), **publishing**, and **distribution** **SHALL** follow **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** §**10.11** by **class** and **entitlement**.

## 11. Publication-oriented labels (continuity from v0.1.0)

The following **A0**–**A5** labels remain **valid** aliases for **publication-shaped** content where products already use them; **SHALL** map to **§10** classes:

| Label | Maps to |
|-------|---------|
| **A0 POST** | **POST** |
| **A1 BLOG** | **BLOG** |
| **A2 ARTICLE** | **ARTICLE** |
| **A3 RESEARCH_REPORT** | **RESEARCH_REPORT** (document or publication per context) |
| **A4 BRIEF** | **BRIEF** subclass or short **ARTICLE**/**REPORT** per policy |
| **A5 BOOK** | **BOOK** + **ADD-002** §10 |

## 12. Action semantics (cross-cutting)

The runtime **SHALL** support **distinct** **action** types where applicable; **SHALL NOT** collapse them into a single “generate” button without **shell** clarity.

| Action | Typical use |
|--------|-------------|
| **draft** | Compose without external effect |
| **review** | Human or policy review step |
| **approve** | Authorization to proceed or send |
| **send** | **EMAIL**/**invite** delivery |
| **publish** | Public or channel publication |
| **export** | **File** output (**ADD-002** packaging) |
| **archive** | Retain without send/publish |

### 12.1 Action-bearing outputs (not “just files”)

These **SHALL** be modeled as **executions**, not only as **export** formats:

- **send_email** / **create_draft_email**
- **create_calendar_invite** / **update_calendar_invite**
- **publish_post** / **publish_article** / **publish_book** (subject to **§10** and **ADD-002** §10.11)

## 13. Shell controls (illustrative)

| Composition class | Illustrative shell controls |
|-------------------|----------------------------|
| **EMAIL** | Draft, Revise, Approve (if required), Send, Schedule, Add recipients, Change tone, Summarize thread |
| **CALENDAR_INVITE** | Propose meeting, Edit date/time, Add attendees, Add location/link, Send invite |
| **RESEARCH_REPORT** | Define scope, Build outline, Draft sections, Review findings, Export PDF/DOCX |
| **BOOK** | Approve TOC, Draft chapter, Review chapter, Assemble, Export/publish if entitled (**ADD-002**) |

## 14. Review, approval, and paid gates

- **EMAIL**/**CALENDAR_INVITE**: **policy** **MAY** require **approval** before **send**/**issue**; **SHALL** be enforceable via **shell** and **audit** surfaces.
- **RESEARCH_REPORT**/**BOOK**/**public REPORT**: **SHALL** align with **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** review and **premium** rules where applicable.
- **Image** insertion, **publishing** pipeline, **designed** PDF, **public distribution**: **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** §**10.11**.

## 15. Packaging defaults (informative)

**Policy** **SHALL** associate default **ADD-002** **packaging** with **class** (e.g. **EMAIL** → **HTML**/provider-native; **MEMO** → **DOCX**/PDF; **POST** → **HTML**/MD). **SHALL NOT** assume every class supports every format as a **primary** path.

## 16. Language, localization, and authoritative version control

**Language** **governs** **how** **meaning** **is** **expressed** **and** **which** **version** **is** **authoritative** **in** **multilingual** **settings** **(§16** **fields**)**.** **It** **does** **not** **replace** **composition** **class** **or** **ADD-002** **depth**/**VC** **(§16.7)**.

### 16.1 Governing principle

**Language** selection, **translation**, and **multilingual** rendering for **composed communication artifacts** **SHALL** be treated as **governed output controls**. The runtime **SHALL** distinguish **original-language composition**, **direct translation**, **localized adaptation**, and **parallel multilingual** output. **SHALL NOT** treat **language switching** as a merely **cosmetic** transformation for **non-trivial** artifacts.

### 16.2 Control fields (normative intent)

**Policy** **SHALL** support explicit fields so the **shell** and **runtime** can record and enforce language posture, including at minimum the following **conceptual** identifiers (product **MAY** map names):

| Field | Purpose |
|-------|--------|
| `source_language` | Language of **input** or **prior** version |
| `target_language` | Intended language of **output** for translation/localization |
| `output_language` | Active language of the **artifact** being composed or displayed |
| `multilingual_mode` | Whether **parallel** versions exist |
| `authoritative_language` | Which version is **binding** when multiple exist |
| `translation_mode` | See **§16.4** |
| `audience_locale` | Regional/locale framing (with **L2**) |
| `formality_level` | Register (often **L2**) |
| `professional_translation_review_required` | When **high-stakes** or **§9.4** applies to a **translated** version |

### 16.3 Language modes (L0–L3)

| Mode | Name | Meaning |
|------|------|--------|
| **L0** | **Same-language composition** | Artifact authored **directly** in one language (e.g. email in Spanish, report in French). |
| **L1** | **Direct translation** | **Translate** an existing artifact into another language with **minimal** structural change unless **policy** requires more. |
| **L2** | **Localized adaptation** | Beyond **L1**: **idiom**, **formality**, **audience framing**, **regional** wording, **CTA** style, **professional** conventions. |
| **L3** | **Parallel multilingual output** | **Multiple** language versions **maintained** (brochure EN/ES, bilingual onboarding). **SHALL** define **authoritative** version when **policy**, **workflow**, or **professional-use** context requires (**§16.5**). |

### 16.4 Translation mode values

| `translation_mode` | Meaning |
|--------------------|--------|
| `compose_original` | **L0** — no translation step |
| `translate_direct` | **L1** |
| `localize_adapt` | **L2** |
| `parallel_multilingual` | **L3** |

### 16.5 Authoritative language

Where **multiple** language versions of the **same** artifact exist—especially **legal**, **policy**, **compliance**, **contract**, or **official** notices—the runtime **SHALL** **identify** the **authoritative** version when **required** by **policy**, **workflow**, or **professional-use** context (**§9.4**). **Non-authoritative** versions **SHALL** be labeled as **translated** or **localized** **renditions** **where appropriate**. **SHALL NOT** imply that every **translation** is **equally binding** without **explicit** **authoritative_language** selection.

### 16.6 Review and disclosure by stakes

- **Lighter** handling **MAY** apply for **simple** content (e.g. **POST**, **BLOG**, basic **EMAIL**, internal notes)—**policy** defines thresholds.
- **Professional** or **high-stakes** documents (**§9.4**, legal/tax/medical/compliance, external **contractual** communications) **SHALL** use **explicit** `target_language`, **`authoritative_language`** when multilingual, **`professional_translation_review_required`** when **policy** demands, and **§9.4** disclosure on **each** language version that **qualifies** as **professional-use**—including **translated** renditions.

### 16.7 Shell and voice-first behavior (seam with ADD-002)

**§16** **governs** **only** **language** **mode**, **`output_language`**, **`translation_mode`**, **`authoritative_language`**, **and** **related** **§16**/**§9.4** **flags** **—** **not** **output** **depth** **class** **or** **VC** **semantics** **(those** **are** **owned** **by** **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§4** **and** **§5**)**.**

- **Language** **or** **locale** **selection** **SHALL** **not** **change** **the** **active** **output** **depth** **step** (**RESPONSE** … **BOOK**) **or** **redefine** **VC0**–**VC5** **meaning** **;** **depth** **and** **VC** **definitions** **remain** **authoritative** **only** **in** **ADD-002**.
- **The** **shell** **SHALL** **track** **`output_language`** **for** **editing** **and** **voice** **delivery** **and** **SHALL** **apply** **the** **current** **depth** **and** **VC** **settings** **established** **under** **ADD-002** **to** **the** **active** **language** **surface** **(e.g.** **read-aloud**, **summarize** **in** **another** **language**) **without** **altering** **ADD-002’s** **definitions** **of** **depth** **or** **VC.**

**§2.1** **addendum** **seams.**

### 16.8 Examples (informative)

| Scenario | Posture |
|----------|---------|
| **EMAIL** | Compose EN; produce ES translation; **English authoritative** for contract negotiation. |
| **CALENDAR_INVITE** | Title/body in FR; **structured** fields remain provider-valid; **locale** for attendee-facing text. |
| **Legal draft** | EN for attorney; ES **convenience** translation; **EN authoritative**; **both** carry **§9.4** disclosure. |
| **BLOG** / **ARTICLE** | EN original; **L2** **localized** ES-LA; **CTA** may differ by locale. |

## 17. Measurement contract and quantified claims

**Measurements**—**quantities**, **dimensions**, **rates**, **calculated values**—**SHALL NOT** be treated as **neutral text** when they **matter** to **meaning**, **compliance**, **safety**, **price**, **fit**, **scope**, or **execution**. They **SHALL** be governed as a **measurement contract** (explicit or derived) before **substantive** drafting **asserts** them as facts.

### 17.1 Governing principle

For **documents** that **materially** rely on **measurements**, **quantities**, **dimensions**, **rates**, or **calculated** values, the system **SHALL** **confirm**, **derive**, or **explicitly declare** the **measurement method** before **substantive** drafting proceeds—**unless** the method is **already authoritative** in the **provided** **source** context (e.g. pasted contract, **certified** survey, **validated** dataset).

The runtime **SHALL NOT** present **materially significant** measurements as **settled document facts** unless their **method**, **unit**, and **basis** are **confirmed**, **derived** from an **authoritative** source, or **explicitly disclosed** as **estimates**.

### 17.2 What must be confirmed or declared

When **policy** or **context** triggers **§17**, the runtime **SHALL** record or surface **at least** the following **conceptual** dimensions (product **MAY** map field names):

| Dimension | Meaning |
|-----------|--------|
| **Measurement subject** | **What** is being measured (space, item, obligation, population, etc.) |
| **Unit system** | e.g. **SI**, **US customary**, **currency**, **%** basis |
| **Measurement method** | How the figure was obtained or computed (e.g. **gross** vs **net rentable** area, **straight-line** vs **road** distance, **nominal** vs **actual** size) |
| **Reference point** | Datum, baseline, or definition (e.g. **interior**-only, **conditioned** space) |
| **Precision / rounding** | Exact, rounded, **significant figures**, **band** |
| **Estimate vs verified** | **Estimated**, **field-measured**, **imported**, **third-party**, **certified** |

### 17.3 When confirmation is mandatory

**Strong** confirmation posture **SHALL** apply when the document **affects** or **may affect** (illustrative): **legal** terms, **contracts**, **construction** / **scope of work**, **property** descriptions, **compliance** / **safety**, **engineering** / **technical specs**, **invoices** / **bids** / **estimates**, **research** reports, **investor** or **financial** documents, **medical** / **scientific** material.

### 17.4 Lighter handling

For **casual** or **low-stakes** writing, **approximate** language **MAY** suffice **if** **clearly disclosed** (e.g. “about 10 minutes,” “roughly 2 miles”).

For **formal** or **high-stakes** documents, **approximation** **SHALL NOT** substitute for **method** disclosure **unless** the document **explicitly** states **approximate**/**estimated** posture and **§17.1** is satisfied for **material** figures.

### 17.5 If method is missing

The runtime **SHALL** do **one** of:

1. **Confirm** — request or derive the **method** when the **workflow** allows; or  
2. **Scaffold** — use placeholders (e.g. `[measurement method to confirm]`, `[verify net rentable square footage]`) consistent with **§5.4**; or  
3. **Disclose uncertainty** — state that the figure is **approximate**, **pending confirmation**, or **unverified**.

### 17.6 Why this matters (informative)

The **same number** can mean different things by **method** (e.g. **square footage**: gross, net, rentable, usable; **distance**: straight-line vs walking; **weight**: shipping vs dry; **rates**: APR vs nominal; **yield**: trailing vs projected). **Polished** text with **wrong** implicit method **SHALL** be treated as a **governance failure**.

### 17.7 Accuracy, reliance, and MPOA

The obligations in **§17** define **procedural** requirements for **quantified** claims and **measurements**. They **do** **not** **warrant** or **guarantee** the **factual** **accuracy** of any **number**, **measurement**, or **derived** **value** produced by the system. **Commercial** terms, **remedies**, and **liability** for **reliance** on **generated** content **SHALL** be governed **exclusively** by **[MPOA](../core/master_platform_operating_agreement.md)** and applicable **product** agreements — **not** by **§17** alone.

## 18. Knowledge basis and discovery gating

Missing **knowledge** is a **state problem**, not a **stylistic** gap. The runtime **SHALL NOT** **draft before grounding** or **compose before discovery** for **non-trivial** outputs when **§18** applies.

**Principle:** **Discover before create.** **Ground before draft.** **Scaffold** when knowledge is **incomplete**.

**Seam** **with** **§19** **:** **§18** **governs** **knowledge** **sufficiency**, **discovery**, **and** **creation** **mode** **before** **substantive** **drafting** **—** **not** **release-time** **originality**, **overlap**, **or** **external** **publish**/**send**/**export** **source-boundary** **determination**, **which** **are** **§19** **when** **§19.2** **applies** **.** **§18** **SHALL** **not** **be** **read** **as** **waiving** **§19** **or** **as** **the** **sole** **gate** **for** **external** **distribution** **risk** **.**

**§19** **SHALL** **not** **substitute** **for** **§18** **grounding** **where** **§18** **applies** **(see** **§18.11** **B** **step** **6** **)** **.**

### 18.1 Governing rule

For **composed artifacts** and **other non-trivial** outputs (**§4**), the runtime **SHALL** determine whether a **sufficient knowledge basis** exists before **substantive** creation proceeds. Where the required knowledge basis is **incomplete**, **stale**, **ambiguous**, or **unverified**, the system **SHALL** perform or request **bounded discovery**, or **remain at scaffold level** (**§5.4**) rather than producing a **falsely complete** artifact.

The runtime **SHALL NOT** produce **materially complete** composed artifacts when the required knowledge basis is **missing**, **stale**, **conflicted**, or **unverified**, unless the artifact is **explicitly** marked **provisional**, **scaffold-only**, or **assumption-based** and **policy** allows that posture.

For artifact classes that **require** external context, **file-backed** context, **professional** references, **operational** records, **measurements** (**§17**), or **current-state** data, **discovery** **SHALL** **precede** substantive drafting **unless** the necessary knowledge basis is **already established** in **authoritative** context (e.g. pasted source text, **verified** attachments, **governed** repository facts).

### 18.2 Responsive vs composed posture

| Output class | Knowledge posture (normative intent) |
|--------------|--------------------------------------|
| **Responsive** (**§4.1**) | **MAY** proceed with **local** session context alone—**quick** answer, summary, explanation, procedural guidance. |
| **Procedural** (**§4.2**) | **MAY** need **partial** basis; **policy** defines. |
| **Composed** (**§4.3**) | **SHALL** undergo **knowledge basis check** (**§18.3**–**§18.6**) before **full** drafting when **§18.10** grounding tier is **medium** or **high**. |

### 18.3 Knowledge basis requirement

Before **substantive** drafting, the runtime **SHALL** identify **what knowledge** the artifact **depends** on, including (illustrative): **internal**/**user** facts, **structured** records, **uploaded** files, **repo**/**governing** docs, **calendar**/**email** context, **external** sources (where **policy** permits), **measurements** (**§17**), **professional** references, **current** operational state.

### 18.4 Discovery-before-creation

If **required** knowledge is **not** yet established, the runtime **SHALL** trigger **bounded discovery** before **substantive** drafting—**unless** the **workflow** **explicitly** allows **scaffold-only** or **assumption-labeled** output.

**Discovery** may include: searching **connected** knowledge (per **policy**), reading **referenced** files, checking **current** state, collecting **required** fields, **confirming** missing facts, **minimum** clarifying questions, and **remaining** at **outline**/scaffold level when discovery is **incomplete**.

### 18.5 Knowledge sufficiency states

**Policy** **SHALL** support classification of **readiness**, including at least the following **meanings** (exact identifiers **MAY** differ):

| State | Meaning |
|-------|--------|
| `sufficient` | Basis adequate for **policy**-allowed drafting. |
| `partial` | Some gaps; **partial** draft or **targeted** discovery **SHALL** follow. |
| `insufficient` | **Not** enough for substantive claims; **scaffold** or **blocked**. |
| `stale` | Known **out-of-date** relative to required freshness. |
| `conflicted` | **Inconsistent** sources; **SHALL NOT** assert single truth without resolution. |
| `unverified` | **Unconfirmed**; **SHALL** be labeled or **blocked** per **policy**. |

### 18.6 Creation mode (gating)

When **knowledge_state** is not `sufficient`, the runtime **SHALL** select or expose **creation mode**, including:

| Mode | Meaning |
|------|--------|
| **full_draft** | **Allowed** when **sufficient** (and **composition contract** satisfied). |
| **partial_draft** | **Allowed** when **partial** and **policy** permits **bounded** claims. |
| **scaffold_only** | **Outlines**, placeholders, **§5.4**—no **false** completeness. |
| **blocked_pending_discovery** | **No** substantive drafting until **discovery** resolves or **user** accepts **explicit** assumptions. |

### 18.7 Fallbacks when knowledge is incomplete

The runtime **SHALL** prefer **outline**, **placeholders**, **assumptions** block (explicitly labeled), **discovery checklist**, **evidence request**, or **draft pending verification** over **polished** prose that **implies** completeness.

### 18.8 Connection to other controls

**§18** **SHALL** be applied **together** with **composition contract** (**§5**), **measurement** contract (**§17**), **language**/**authoritative** version (**§16**), **professional-use** disclosure (**§9.4**), **reference-guided** composition (**§20**) when **references** **apply**, **originality**/**source-boundary** (**§19**) when **source-derived** **outputs** **apply**, and **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **BOOK** gates (**§10** **there**). **Creation** **SHALL NOT** **outrun** **grounding**.

### 18.9 Informative control-plane object (non-normative)

**Illustrative** **JSON** **(non-normative)** **for** **knowledge**/**discovery** posture: **[Annex A](AMD-2026-008-ADD-003-ANNEX-A-informative-composition-examples.md)** **§2**.

### 18.10 Grounding need by artifact class (illustrative)

| Tier | Typical artifact classes | Expectation |
|------|-------------------------|-------------|
| **Low** | **POST**, generic **BLOG**, casual **SUMMARY** | **Lighter** **§18**; **policy** may still require **checks**. |
| **Medium** | **EMAIL** reply with facts, **MEMO**, **ARTICLE**, **PROPOSAL** | **Knowledge basis check**; **discovery** **often** required. |
| **High** | **RESEARCH_REPORT**, **professional** drafts (**§9.4**), **POLICY**, **scope of work**, **investor** memo, **BOOK** with **factual** claims | **Strong** **discovery**; **full_draft** **SHALL NOT** **outrun** **grounding**. |

### 18.11 Recommended sequence (non-trivial creation)

**A — Before substantive drafting (when applicable)**

1. **Composition contract** — **role**, **intent**, **outcome** (**§5**).  
2. **Knowledge basis check** — **§18.3**–**§18.5**.  
3. **Discovery** — **§18.4**.  
4. **Reference disposition** — **§20** when **reference_documents** or **reference_role** applies (**SHOULD** resolve **structure**/**tone**/**style**/**authority** posture **before** **substantive** drafting).  
5. **Creation mode** — **§18.6** (and **§17**, **§16**, **§9.4** as applicable).

**B — Before external publish, send, or formal export (when applicable)**

6. **Originality / source-boundary** — **§19** when **policy** or **artifact** **class** **requires** **verification** **before** **publish**/**send**/**export**; **§19** **SHALL** **not** **substitute** **for** **§18** **grounding** **where** **§18** **applies** **(ground** **first**)**.

**Parallel** **obligations** **(same** **artifact** **may** **trigger** **several**)**:** **professional** **disclosure** (**§9.4**); **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **BOOK**/**TOC**/**chapter**/**premium** **gates** **where** **BOOK**/**export** **path** **applies**.

**Thresholds**, **metric** **mapping**, **evaluation** **record** **shape**, **and** **DCP** **outcome** **codes** **for** **§19** **default** **to** **[ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD](../operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md)** **(AIOS-OPS-020)** **§6**–**§9** **unless** **policy** **registers** **a** **replacement** **artifact** **.**

**Implementation** **posture** **:** **§18** **discovery**/**knowledge** **states** **and** **§19** **release-time** **verification** **SHALL** **be** **implementable** **as** **explicit** **state** **transitions** **.** **When** **§19.2** **applies**, **an** **`OriginalityEvaluationRecordV1`** **per** **AIOS-OPS-020** **§9** **SHALL** **refer** **to** **the** **same** **composed** **artifact** **identifier** **(and** **record** **knowledge-basis** **metadata** **when** **§18** **also** **applied**)** **so** **grounding** **and** **originality** **results** **are** **joinable** **in** **audit** **.**

## 19. Originality, source-boundary, and non-reproduction verification

This section **imposes** **runtime** **SHALL**/**MUST** **NOT** **behavior** **for** **overlap**, **extraction**, **and** **publish**/**send**/**export** **gates** **below**. **It** **defines** **required** **verification** **states**, **channel** **threshold** **posture**, **and** **enforcement** **outcomes** **—** **risk-reduction** **and** **policy** **enforcement**, **not** **a** **legal** **guarantee** **of** **non-infringement** **(§19.9)**. **Disclaimer** **of** **absolute** **legal** **outcomes** **(§19.9)** **does** **not** **relax** **those** **obligations** **or** **excuse** **skipping** **verification** **when** **§19.2** **applies**. **Implementation** **methods**, **scores**, **and** **transport** **bindings** **SHALL** **have** **a** **traceable** **home** **per** **§19.10**.

**§18** **and** **§19** **are** **distinct** **:** **§18** **addresses** **whether** **grounding**/**discovery** **posture** **permits** **substantive** **drafting** **;** **§19** **addresses** **originality**/**source-boundary** **verification** **for** **release** **paths** **when** **required** **.** **Passing** **§18** **sufficiency** **does** **not** **waive** **§19** **;** **§19** **does** **not** **prove** **§18** **grounding** **.**

### 19.1 Framing

**Where** **external** **distribution** **exists**, **internal** **and** **external** **channels** **SHALL** **use** **different** **policy** **thresholds** **(§19.4)** **—** **external-facing** **paths** **SHALL** **not** **implicitly** **inherit** **internal-only** **leniency** **unless** **policy** **explicitly** **documents** **an** **equivalent** **risk** **posture**.

**Publish**, **send**, **and** **formal** **export** **paths** **SHALL** **evaluate** **§19** **verification** **against** **policy** **thresholds** **for** **the** **target** **channel** **before** **release** **when** **§19.2** **applies**. **Failure** **SHALL** **yield** **a** **bounded** **outcome** **among** **§19.5** **(including** **blocked**, **review** **required**, **internal-only** **where** **policy** **allows**)** **—** **not** **silent** **pass-through**.

The runtime **SHALL** **prefer** **transformed**, **purpose-built** composition over **verbatim** or **near-verbatim** **reproduction** of **sources** or the **knowledge base** beyond **policy**-allowed bounds. **SHALL** **flag** **high-overlap** outputs for **review** and **SHALL** **block** or **downgrade** **publish**/**send**/**export** when **reproduction** risk is **too high** for the **target** channel—**not** as **legal advice**, but as **governed** product behavior.

### 19.2 Normative rule

For **composed artifacts** **derived** from **knowledge-base** or **other** **source** materials, the runtime **SHALL** apply an **originality** and **source-boundary** verification **gate** before **publish**, **send**, or **formal export** actions when **policy** or **artifact class** requires it. The system **SHALL** **prefer** **transformed**, **purpose-built** composition over **source** reproduction and **SHALL NOT** treat **source** **retrieval** as **permission** to reproduce **substantial** **protected expression** without **explicit** **authorizing** **workflow** (e.g. **short** **quoted** excerpts with **attribution** per **policy**).

Where output exhibits **high** **verbatim** overlap, **structurally** **excessive** similarity to a **single** source, or **knowledge-base** **extraction**-style behavior (dumping **internal** notes or **proprietary** material as **publishable** body text), the runtime **SHALL** **block** or **downgrade** the artifact to **review-required** status rather than treating it as **publish-ready**.

**The** **non-waiver** **and** **no-absolute-guarantee** **language** **in** **§19.9** **does** **not** **weaken** **the** **enforcement** **obligations** **in** **§19.2**–**§19.5** **;** **those** **sections** **remain** **binding** **for** **release-time** **gating** **and** **channel** **control**.

**Policy** **silence** **:** **if** **policy** **does** **not** **clearly** **specify** **whether** **§19.2** **applies** **to** **a** **given** **composed** **artifact** **or** **release** **path**, **the** **runtime** **SHALL** **fail** **closed** **per** **§5.9** **—** **not** **silent** **pass-through** **—** **until** **policy** **resolves** **applicability**, **verification** **runs**, **or** **the** **artifact** **remains** **on** **an** **internal-only** **path** **per** **§19.5**.

### 19.3 Gate checks (conceptual)

| Check | Question |
|-------|----------|
| **Verbatim reproduction risk** | Does output **copy** **source** text **too closely**? |
| **High-overlap paraphrase risk** | Is **structure**/**sequence** **too close** even when wording differs? |
| **Knowledge-base extraction risk** | Is the model **dumping** **internal** KB/doc content instead of **composing** a **new** artifact? |
| **Citation / quote boundary** | If **exact** language is used, is it **short**, **intentional**, **attributed** (if appropriate), and **within** **policy**? |
| **Publishability risk** | Is posture **acceptable** for **external** distribution **even if** **internal** draft use might be allowed? |

### 19.4 Internal vs external thresholds

**Policy** **SHALL** support **different** **thresholds** by **channel** **and** **SHALL** **define** **stricter** **originality**/**source-boundary** **rules** **for** **external-facing** **publish**, **send**, **and** **formal** **export** **than** **for** **internal-only** **drafts** **(numerically** **or** **by** **required** **review** **state**)** **—** **external-facing** **artifacts** **SHALL** **not** **use** **the** **same** **leniency** **as** **internal** **collaboration** **drafts** **unless** **policy** **explicitly** **documents** **an** **equivalent** **risk** **posture**.

**Policy** **SHALL** **either** **(a)** **define** **numeric** **or** **procedural** **thresholds** **that** **map** **§19.3** **signals** **to** **§19.5** **states** **for** **each** **channel** **class** **(internal** **vs** **external)**, **or** **(b)** **reference** **a** **governed** **specification** **or** **operations** **artifact** **that** **defines** **those** **thresholds** **and** **evaluation** **methods** **—** **and** **products** **SHALL** **bind** **release-time** **evaluation** **to** **that** **definition** **(§19.10)**.

**Default** **named** **artifact** **for** **option** **(b)** **:** **[ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD](../operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md)** **(registry** **AIOS-OPS-020)** **—** **until** **policy** **explicitly** **registers** **a** **different** **governed** **successor** **artifact**.

| Mode | Posture |
|------|---------|
| **Internal draft / analysis** | **More** source-near **excerpting** **MAY** be **acceptable** for **review** and **collaboration**. |
| **External publish / send / export** | **Stricter** **originality** and **source-boundary** **gate** **SHALL** **apply**. **SHALL** **meet** **policy** **thresholds** **for** **the** **external** **channel** **before** **release**. |

Illustrative **distribution** states (product **MAY** map names): `internal_review_ok`, `external_publish_review_required`, `blocked_high_overlap`, `internal_only_pending_release`.

### 19.5 Verification states

**Policy** **SHALL** support **verification** states for **shell** and **workflow**, including at least:

| State | Meaning |
|-------|--------|
| `originality_clear` | Within **policy** **thresholds** for the **target** channel. |
| `quote_limited` | **Short**, **bounded** **quotation**; **attribution** as required. |
| `overlap_review_required` | **Elevated** overlap; **human** or **policy** review before **publish**/**send**. |
| `high_reproduction_risk_blocked` | **Publish**/**send**/**export** **blocked** or **forced** to **scaffold**/**outline** until resolved. |
| `internal_only` | **External** **publish**/**send**/**formal** **export** **not** **permitted** **until** **resolved** **per** **policy**; **internal** **draft**/**collaboration** **MAY** **continue** **where** **policy** **allows**. |

### 19.6 High-risk next steps (not only “error”)

When risk is **high**, the runtime **SHALL** offer **controlled** **next steps** (illustrative): **summarize** instead of **quote**; **rewrite** from **findings** not **source phrasing**; **reduce** **direct** **extraction**; **convert** to **outline**/scaffold; **request** **explicit** **user** **approval** for **quoted** material; **limit** **export**/**publish** until **reviewed**.

### 19.7 Knowledge-base use rule

**Knowledge-base** access **SHALL** support **discovery**, **grounding**, and **evidence-backed** composition, but **SHALL NOT** be used as a basis for **wholesale** **reproduction**, **extraction-style** output, or **publication** of **protected** **source** **expression** **absent** an **explicitly** **authorized** **quoting** or **licensing** **workflow**.

### 19.8 Connection to other controls

**§19** **SHALL** be applied with **§18** (grounding), **§20** (reference-guided composition), **§17** (measurements), **§9.4** (professional), **§16** (language), **§5** (contract), and **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§10.11** (**premium** **publish**/**export**).

### 19.9 What this addendum does not claim

**No** **waiver** **of** **§19.2**/**§19.4**/**§19.5**. **The** **runtime** **SHALL**/**MUST** **NOT** **rules** **above** **remain** **binding** **product** **obligations** **where** **applicable**; **this** **subsection** **limits** **only** **what** **may** **be** **promised** **to** **users** **about** **third-party** **legal** **outcomes**.

**SHALL** **not** **market** **or** **represent** **the** **system** **as** **ensuring** **absolute** **copyright** **compliance**, **guaranteed** **uniqueness**, **or** **guaranteed** **non-infringement** **in** **all** **jurisdictions** **and** **facts** **—** **those** **are** **legal** **determinations** **outside** **this** **addendum** **and** **outside** **typical** **product** **warranties**. **Permitted** **claims:** **originality** **verification**, **source-boundary** **control**, **non-reproduction** **gate**, **high-overlap** **review** **—** **not** **“copyright** **protection”** **as** **an** **absolute** **guarantee**.

### 19.10 Implementation handoff (normative)

**This** **addendum** **does** **not** **embed** **full** **scoring** **algorithms**, **numeric** **constants**, **or** **JSON** **Schema** **in** **the** **body**. **It** **defines** **required** **control** **states**, **channel** **posture**, **enforcement** **outcomes**, **and** **fail-closed** **composition** **rules** **(§5.9**, **§19.2**–**§19.5)**.

**Implementation-specific** **validation** **logic**, **overlap**/**similarity** **scoring**, **threshold** **tables**, **serialized** **contract** **schemas**, **and** **control-plane** **transport** **bindings** **SHALL** **live** **in** **governed** **specification** **or** **operations** **artifacts** **registered** **by** **policy**, **such** **that** **§19** **verification** **is** **auditable** **and** **not** **solely** **implementation-defined** **without** **a** **traceable** **home**. **The** **default** **registered** **home** **is** **[ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD](../operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md)** **(AIOS-OPS-020)** **unless** **policy** **names** **a** **replacement**. **Products** **SHALL** **document** **which** **artifact** **supplies** **release-time** **evaluation** **for** **each** **conformance** **claim** **tied** **to** **this** **addendum**.

**Division** **of** **labor** **:** **this** **addendum** **states** **obligations** **and** **states** **(§19.2**–**§19.5**)** **;** **AIOS-OPS-020** **supplies** **normative** **metric** **names**, **default** **threshold** **bands**, **severity** **×** **channel** **→** **state** **mapping**, **`OriginalityEvaluationRecordV1`**, **and** **DCP** **outcome** **codes** **.** **Algorithm** **IDs** **and** **concrete** **scorers** **remain** **deferred** **to** **policy** **or** **AIOS-OPS-020** **v0.4.0** **.**

**Conformance** **claims** **to** **§19** **SHALL** **name** **the** **governed** **artifact** **identifier** **and** **version** **used** **(e.g.** **`AIOS-OPS-020`** **`v0.3.2`** **)** **for** **metrics**, **thresholds**, **record** **shape**, **and** **transport** **bindings** **.**

**Minimum** **surface** **for** **claims** **against** **AIOS-OPS-020** **(unless** **policy** **registers** **a** **replacement** **with** **equivalent** **coverage**)**:** **products** **SHALL** **implement** **(a)** **normative** **metric** **names** **and** **inputs** **per** **§6.1**, **(b)** **severity** **discipline** **under** **§6**, **(c)** **§7** **severity** **×** **channel** **→** **enforcement** **state** **mapping**, **(d)** **§9** **evaluation** **record** **contract** **and** **Appendix** **A** **JSON** **Schema** **for** **`OriginalityEvaluationRecordV1`**, **(e)** **§10** **DCP**/**transport** **outcome** **codes** **for** **release-time** **results**, **(f)** **`policy_pack_id`** **(and** **`metric_snapshot`** **when** **used)** **on** **each** **evaluation** **record**, **and** **(g)** **§13** **DCP** **codes** **for** **§5.9** **composition** **fail-closed** **signaling** **when** **the** **product** **emits** **control-plane** **transport** **for** **those** **gates** **.**

## 20. Reference-guided composition

**Reference documents** and **comparable materials** (**examples**, **prior filings**, **house style** samples) **SHALL** be governable as **first-class** **composition inputs**: they **guide** **spirit**, **structure**, **cadence**, and **document anatomy**—**not** as a license to **copy** **protected expression**. This section is **style-bound** and **form-bound** **guidance**; it **SHALL** remain **subject** to **§18** (**knowledge** **basis**—references are a **special** kind of **source** oriented to **form**), **§19** (**non-reproduction**), **§9.4** (**professional** drafts), **§17**, and **§16**.

### 20.1 Guiding, not copying

The **normative** posture **SHALL NOT** be “**copy** this **reference**.” The **normative** posture **SHALL** be “**use** this **reference** to **guide**” **structure**, **tone**, **section order**, **level of detail**, **stylistic** **posture**, **formal** **conventions**, and **expected** **document** **anatomy**—so that **role**/**intent**/**outcome** (**§5**) produce the **right kind** of artifact (e.g. **patent**-shaped vs **memo**-shaped), not merely **correct** **isolated** **facts**.

### 20.2 Core rule

For **composed artifacts**, the runtime **MAY** use **one** or **more** **reference documents** as **guidance** for **structure**, **tone**, **sectioning**, and **stylistic** **posture**. **Reference-guided** composition **SHALL** **inform** the **spirit** and **organizational** **pattern** of the **output** **without** **authorizing** **wholesale** **reproduction** of **protected** **expression**.

The runtime **SHALL** support **reference-guided** composition where **users** provide **example** documents, **templates**, or **comparable** materials to indicate **desired** **spirit**, **structure**, or **stylistic** **posture**. The system **SHALL** **distinguish** **reference** materials used for **guidance** from **authoritative** **templates** **required** for **conformity** (**§20.3**). **Reference** use **SHALL** remain **subject** to **originality**, **non-reproduction**, **professional-review**, and **knowledge-basis** **controls**.

Where a **reference** is **supplied**, the runtime **SHOULD** determine whether it is used **primarily** for **structure**, **tone**, **style**, **formatting**, or **authoritative** **conformity** **before** **substantive** **drafting** **proceeds** (when **policy** or **workflow** **requires** **disposition**).

### 20.3 Template, reference, and authority (do not conflate)

| Kind | Meaning |
|------|--------|
| **Template** | A **sanctioned** **form** **intended** for **direct** **reuse** (e.g. **approved** **letterhead** block, **fill-in** **fields**)—**still** **subject** to **§19** and **policy** for **what** may be **copied** **verbatim**. |
| **Reference** | An **example** used to **guide** the **new** artifact’s **shape** and **spirit**—**default** **assumption**: **not** **permission** to **clone** **proprietary** **boilerplate** or **long** **protected** **runs** of **text**. |
| **Authority** | A **governing** or **required** **form** (**court** rules, **regulator** **schema**, **mandatory** **section** **order**) that **constrains** **output** **structure**—**may** **require** **closer** **format** **conformity** **subject** to **professional** **review** and **§19**. |

Illustrations: a **user-uploaded** **patent** **filing** **MAY** be a **reference**; an **approved** **company** **letter** **form** **MAY** be a **template**; a **court-mandated** **filing** **structure** **MAY** be an **authority**. **Product** **SHALL NOT** treat these as **interchangeable** **labels**.

### 20.4 First-class inputs (illustrative fields)

**Policy** and **product** **SHALL** support **explicit** **inputs**, including at minimum the following **conceptual** **fields** (names **MAY** **map**):

| Field | Role |
|-------|------|
| `reference_documents` | **Ordered** or **tagged** **list** of **document** **handles** (uploads, **KB** **links**, **citations**) **designated** for **composition** **guidance**. |
| `reference_mode` | **Primary** **use** of **references** for **this** **draft** (illustrative **values** follow **this** **table**). |
| `reference_role` | **R1** / **R2** / **R3** (**§20.5**) or **product**-equivalent **encoding**. |
| `reference_adherence` | **Single** **dial** **1**–**10**: **layout**/**reference** **conformity**—**how** **closely** **output** **follows** **reference** **structure**/**spirit** (**§20.11**–**§20.15**). **SHALL NOT** be conflated with **model** **temperature** or **decoding**/**sampling**. |
| `structure_adherence` | **Optional** **1**–**10** when **split** **controls** **are** **used** instead of **or** **alongside** **`reference_adherence`**—**section** **order**, **heading** **hierarchy**, **layout** **rhythm**, **document** **anatomy**. |
| `style_adherence` | **Optional** **1**–**10**—**voice**, **cadence**, **formality**, **rhetorical** **posture**. |
| `innovation_mode` | **Whether** **to** **preserve**, **refine**, or **reimagine** **within** the **allowed** **adherence** **range**—illustrative: `preserve` \| `improve` \| `reimagine` (**§20.12**). |

Illustrative **`reference_mode`** values (product **MAY** **extend**): `structure_only`, `style_only`, `tone_only`, `format_and_structure`, `example_of_spirit`, `authoritative_template`, `comparative_multi_reference`.

**Semantics** for **adherence** **fields**: **§20.11**–**§20.15**.

### 20.5 Reference roles (R1–R3)

| Role | Name | Governs |
|------|------|--------|
| **R1** | **Stylistic reference** | **Voice**, **tone**, **rhythm**, **level** of **polish**. |
| **R2** | **Structural reference** | **Section** **order**, **headings**, **document** **anatomy**, **composition** **pattern**. |
| **R3** | **Authoritative template / reference** | **Sanctioned** or **required** **structure** **subject** to **professional** **review** and **§19**/**§9.4**—**conformity** **MAY** be **stricter** than **R1**/**R2**. |

### 20.6 What reference documents may guide

**Non-exhaustive**: **document** **class** **fit**; **section** **order**; **heading** **style**; **tone**/**formality**; **depth**; **argument** or **claim** **style**; **summary** **style**; **citation** **style**; **boilerplate** **expectations** (where **policy** **allows**); **visual**/**structural** **rhythm** (within **ADD-002** **packaging** **constraints**).

### 20.7 What reference documents do not automatically authorize

**SHALL NOT** **automatically** **authorize**: **direct** **copying**; **sentence-by-sentence** **mimicry**; **reuse** of **protected** **text** **blocks**; **cloning** **proprietary** **boilerplate** **without** **review**; **inheriting** **factual** **assumptions** **true** only in the **reference** **context** (**SHALL** **defer** to **§18** **grounding** and **§17** **measurements**).

### 20.8 Practical pre-draft questions

Before **substantive** **drafting**, the runtime **SHOULD** resolve (or **surface** for **user** **confirmation**) where **references** **apply**:

- **Style**, **structure**, **tone**, or **required** **conformity**?  
- **Template**, **example**, or **authority**?  
- **Similar** in **spirit** or **close** in **format**?  
- **User-owned**, **licensed**, **internal**, or **third-party** **sample**?  
- **Professional** **review** (**§9.4**)?  
- **Elevated** **copying**/**overlap** **risk** (**§19**)?  
- **Reference** **adherence** **level** (**structure**/**style**/**combined**) and **innovation** **posture** (**§20.11**–**§20.15**)?  

### 20.9 Patents, legal, and high-stakes drafts

For **patents**, **legal** **documents**, **policies**, **specs**, **formal** **letters**, and **comparable** **classes**, **reference-guided** composition **SHALL** be **allowed** **with** **stricter** **controls**, including where **policy** **requires**: **draft** **labeling**; **explicit** **whether** the **reference** is **example** **only**, **preferred** **structure**, or **required** **structure**; **licensed** **professional** **review** **disclosure** (**§9.4**); **§19** **overlap** **controls** **against** the **reference**; **disclaimer**/**export** **preservation** per **§9.4**/**policy**.

### 20.10 Connection to other controls

**§20** **SHALL** be applied with **§5** (**contract**), **§18** (**knowledge** **basis** / **discovery**), **§19** (**originality**), **§9.4** (**professional**), **§17** (**measurements**), **§16** (**language**), and **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§10**/**§10.11** as applicable. **Reference** **guidance** **SHALL NOT** **bypass** **§19**; **high**/**overlap** **risk** **SHALL** **trigger** **review**/**blocked** **paths** per **§19**.

### 20.11 Naming: not “temperature”

**Layout** **adherence**, **reference** **conformity**, **structure**/**document** **shape** **fidelity**, and **reference** **adherence** **SHALL** denote **composition** **controls**—**how** **closely** **output** **follows** **reference** **structure**, **layout**, **and** **spirit**. **Product** and **documentation** **SHALL NOT** **label** these **controls** **“temperature”** or **conflate** them with **model** **randomness**, **decoding**, or **sampling** **behavior**.

### 20.12 Normative adherence and innovation controls

**Reference-guided** composition **MAY** include **explicit** **adherence** **controls** **governing** **how** **closely** **output** **follows** the **structure**, **layout**, and **organizational** **pattern** of a **reference** **document**. **Higher** **adherence** **values** **SHALL** **increase** **conformity** to **document** **shape** and **sequencing**, but **SHALL NOT** **authorize** **direct** **reproduction** of **protected** **expression** or **knowledge-base** **extraction** (**§19**). **Lower** **adherence** **values** **MAY** **permit** **broader** **reorganization**, **simplification**, or **improvement** of the **reference** **form**.

The runtime **MAY** **separately** **expose** an **innovation** **control** **indicating** whether the **system** **should** **preserve**, **refine**, or **reimagine** the **reference** **structure** **within** the **allowed** **adherence** **range**. Illustrative **`innovation_mode`** **values**: `preserve` (**minimal** **structural** **change** **beyond** **what** **adherence** **requires**), `improve` (**clarify**, **tighten**, **modernize** **while** **respecting** **adherence**), `reimagine` (**broader** **reorganization** **allowed** **when** **adherence** **is** **low** **enough**).

**Product** **MAY** ship **one** **combined** **`reference_adherence`** **(1–10)** **first**; **SHOULD** **support** **split** **`structure_adherence`** **and** **`style_adherence`** **(each** **1–10**)** when** **users** **need** **different** **posture** **for** **anatomy** **vs** **voice** (e.g. **match** **structure**, **vary** **tone**).

### 20.13 Reference adherence scale (1–10)

| Level | Label | Meaning |
|-------|--------|--------|
| **1** | **Loose inspiration** | **Reference** **only** **as** **general** **inspiration**; **broad** **spirit** **only**; **structure** **MAY** **change** **significantly**; **innovate** **freely**—**suitable** **for** **improve-this** **or** **modernize-this** **tasks**. |
| **2–3** | **Light reference** | **Some** **section** **patterns** **MAY** **carry** **over**; **tone** **and** **high-level** **rhythm** **MAY** **be** **similar**; **layout** **MAY** **change** **substantially**. |
| **4–5** | **Moderate guidance** | **Core** **section** **order** **MAY** **be** **preserved**; **recognizable** **shape** **retained**; **MAY** **simplify**, **improve**, or **reorganize**—**informative** **default** for **many** **business** **documents**. |
| **6–7** | **Strong adherence** | **Preserve** **most** **section** **order** **and** **document** **anatomy**; **only** **moderate** **innovation**—**like-this-but-for-my-case** **posture**. |
| **8–9** | **Near-form fidelity** | **Closely** **follow** **headings**, **sequence**, **and** **layout** **logic**; **only** **necessary** **adjustments** **for** **new** **content**/**context**; **strong** **control** **for** **formal** **patterns**. |
| **10** | **Exact layout conformity** | **Preserve** **document** **layout**/**structure** **as** **closely** **as** **allowed** **when** **reference** **functions** **like** **a** **required** **form** **or** **strict** **model**—**still** **not** **permission** **to** **copy** **protected** **language** (**§20.14**). |

**Simple** **product** **ladder** (**informative**): **1** = **loose** **inspiration**; **5** = **guided** **similarity**; **10** = **strict** **structural** **conformity**.

### 20.14 Maximum adherence and the originality gate

**Maximum** **layout**/**reference** **adherence** **authorizes** **close** **conformity** **to** **structure**, **ordering**, **section** **pattern**, **and** **formatting** **logic**, but **SHALL NOT** **authorize** **wholesale** **reproduction** of **protected** **text** or **knowledge-base** **extraction** (**§19**). **Even** **at** **level** **10**, **conformity** **is** **to** **shape**, **not** **to** **verbatim** **content**.

**High** **reference** **adherence** **(including** **level** **10** **)** **SHALL** **not** **bypass** **§19** **verification** **or** **channel** **thresholds** **in** **[ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD](../operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md)** **when** **§19.2** **applies** **—** **structure** **fidelity** **does** **not** **imply** **originality_clear** **or** **release** **clearance** **.**

### 20.15 Illustrative defaults by artifact class (informative)

**Policy** **MAY** **suggest** **starting** **adherence** **ranges**; **users** **SHALL** **override** **as** **needed**:

| Context | Informative default range |
|---------|---------------------------|
| **Patents**, **legal**, **highly** **formal** **docs** | **Often** **7**–**10** **when** **reference** **shape** **matters** |
| **Blogs**, **articles**, **marketing** | **Often** **2**–**6** |
| **Internal** **plans**, **reports** | **Often** **4**–**7** |

## 21. Non-goals

This addendum does not define:

- **Navigation primitives** — **[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**
- **Output depth**, **VC** classes, **packaging** taxonomy detail — **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** (output depth remains orthogonal to **composition contract** — **§5** **here**)
- **Machine-translation** engine selection, **MT** APIs, or **linguistic** QA tooling — product/operations
- **BOOK** phased **B0–B9** detail — **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** §10
- Provider **API** schemas (Google Calendar, SMTP, etc.)
- **Visual** templates or brand kits
- **Metrology** hardware, **survey** procedures, or **engineering** calculation libraries — product/operations
- **Retrieval** backend implementation, **index** topology, or **RAG** pipeline details — **product**/**operations** (governance of **when** discovery runs is **§18** **here**)
- **Legal** determination of **infringement**, **fair use**, or **licensing**—**counsel** and **jurisdiction**-specific law; **§19** is **operational** **risk** **control** only
- **UI** layout for **reference** **pickers**, **diff**/**overlap** **visualization**, or **template** **libraries**—**product**/**design** (normative **fields** are **§20** **here**)

---

*End of AMD-2026-008-ADD-003, version 0.14.2 (draft).*



---

## Cross-reference bundle: `AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001`

**[Bundled cross-reference — use this file’s version]** **`AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001`** — **version** **`1.0.0`**

---

---
document_id: AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001
version: 1.0.0
status: draft
category: reference
title: Composition control plane — architecture memo (bounded domains and addendum seams)
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008
  - doc_id: AMD-2026-008-ADD-001
  - doc_id: AMD-2026-008-ADD-002
  - doc_id: AMD-2026-008-ADD-003
  - doc_id: AIOS-COMPOSITION-CONTROL-RD-NOTES-001
  - doc_id: AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001
note: Informative partitioning memo; not ratified law.
amendment_history:
  - version: 1.0.0
    date: 2026-04-10
    summary: Initial architect backfill — domain boundaries, dependency map, OUT scope, ADD-003 refinement hooks.
---

# Composition control plane — architecture memo (001)

## Purpose

This memo **backfills** the **architect** **layer** that **should** **precede** **or** **accompany** **heavy** **addendum** **drafting**: **where** **each** **concern** **lives**, **what** **depends** **on** **what**, and **what** **SHALL** **not** **bleed** **across** **seams**. It **informs** **revision** **of** **[ADD-001](../amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**, **[ADD-002](../amendments/AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)**, **[ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** **without** **replacing** **them**.

**Inputs:** **[AIOS-COMPOSITION-CONTROL-RD-NOTES-001](AIOS-COMPOSITION-CONTROL-RD-NOTES-001.md)**. **Outputs** **for** **product:** **[AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001](AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001.md)**.

---

## Bounded domains

| Domain | Owns | Does not own |
|--------|------|----------------|
| **Shell navigation** | **START_HERE**, **CONTINUE**, **CHOOSE**, **SINGLE_INPUT**, **MULTI_INPUT**; **alert**/**continue**/**choose** primitives | **Composition** **class** **labels**; **EMAIL**/**DOCUMENT** **body** **schema** **detail** |
| **Output depth** | **RESPONSE** → **BOOK** **ladder**; **promotion** **rules** | **Intent** **primitive** **routing** (**AIOS-SPEC-009**); **Workspace** **MCP** **scopes** (**AIOS-SPEC-007**) |
| **Shell voice** | **VC0**–**VC5** **obligations** | **Acoustic**/**engine** **TTS** **selection** |
| **Packaging** | **TXT**/**MD**/**PDF**/**DOCX**/**JSON**/**HTML** **classes** | **Renderer** **implementation**; **font**/**template** **assets** |
| **BOOK** **workflow** | **B0**–**B9** **phases**, **gates**, **premium** **vs** **base** (**§10**/**§10.11**) | **Payment** **provider** **APIs** (**MPOA** **tier** **facts**) |
| **Composition** **classes** | **Family** + **class** **identifiers**; **action** **semantics** (**draft**/send/**publish**) | **Provider** **APIs** (**Gmail**/**Calendar** **schemas**) |
| **Composition** **contract** | **role**/**intent**/**outcome** **for** **composed** **artifacts** | **User** **editable** **field** **UI** **layout** |
| **Language** | **L0**–**L3**, **authoritative** **language**, **translation** **mode** | **MT** **engine** **choice** |
| **Measurement** | **method**/**unit**/**basis**/**precision** **for** **quantified** **claims** | **Survey** **hardware**; **calculation** **libraries** |
| **Knowledge** **basis** | **sufficiency**; **discovery-before-create**; **creation** **mode** | **Index** **topology**; **RAG** **pipeline** |
| **Originality**/**source** **boundary** | **Overlap**/**extraction** **risk**; **publish**/**send** **gate** | **Legal** **determination** **of** **infringement** |
| **Reference-guided** **composition** | **Template** **vs** **reference** **vs** **authority**; **R1**–**R3**; **adherence** **1**–**10**; **innovation** **mode** | **Copyright** **registration**; **licensing** **negotiation** |

---

## Dependency map (read order)

```text
ADD-001 (navigation)     ──►  ADD-002 (depth / VC / packaging / BOOK)
                                      │
                                      ▼
ADD-003 (composition plane, contracts, KB, originality, reference adherence)
        │
        ├──► AIOS-SPEC-009 (lanes, intent model) — parent AMD-2026-008 §3.1
        ├──► MPOA (commercial / liability)
        └──► AIOS-SPEC-007 (Workspace) where workspace intents touch export/send
```

---

## Addendum seam rules (normative for authors, not for runtime)

1. **ADD-002** **SHALL** **not** **define** **composition** **class** **taxonomies**; **ADD-003** **owns** **those**.
2. **ADD-003** **SHALL** **not** **redefine** **VC** **classes** **or** **output** **depth** **ladder**; **cross-ref** **ADD-002**.
3. **Gates** **stack**: **knowledge** **basis** (**§18**) **before** **substantive** **drafting**; **reference** **disposition** (**§20**) **when** **references** **apply**; **originality** (**§19**) **before** **external** **publish**/**send** **when** **policy** **requires** **—** **order** **is** **in** **ADD-003** **§18.11**.

---

## OUT of addenda (belongs elsewhere)

| Topic | Proper home |
|-------|-------------|
| **Retrieval** **backend**, **chunking**, **RAG** | **Product**/**operations**; **AMD-2026-009** **retrieval** **neutrality** **where** **relevant** |
| **API** **schemas** (**SMTP**, **Calendar**) | **Integrations**/**specs**; **not** **ADD-003** |
| **Visual** **brand** **kits** | **Product**/**design** |

---

## ADD-003 refinement hooks (use when revising)

- **Tighten** **cross-references** **so** **each** **§** **has** **one** **obvious** **“home”** **axis** **from** **§6** **twelve-axis** **table**.
- **Consider** **moving** **long** **informative** **JSON** **examples** **to** **an** **annex** **file** **if** **the** **main** **file** **remains** **hard** **to** **review**.
- **Align** **reference** **adherence** **language** **with** **§19** **everywhere** **“maximum”** **structure** **conformity** **is** **mentioned**.

---

*End of AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001, version 1.0.0 (draft).*


---

## Cross-reference bundle: `AIOS-COMPOSITION-CONTROL-RD-NOTES-001`

**[Bundled cross-reference — use this file’s version]** **`AIOS-COMPOSITION-CONTROL-RD-NOTES-001`** — **version** **`1.0.0`**

---

---
document_id: AIOS-COMPOSITION-CONTROL-RD-NOTES-001
version: 1.0.0
status: draft
category: reference
title: Composition control plane — R&D and knowledge capture (AMD-2026-008 addendum track)
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008
  - doc_id: AMD-2026-008-ADD-001
  - doc_id: AMD-2026-008-ADD-002
  - doc_id: AMD-2026-008-ADD-003
  - doc_id: AIOS-AMD-PLAN-001
  - doc_id: AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001
  - doc_id: AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001
note: Informative knowledge capture before or alongside doctrine refinement; not ratified law.
amendment_history:
  - version: 1.0.0
    date: 2026-04-10
    summary: Initial capture — process defect diagnosis; clustered principles; open questions; points to architect and surface memos.
---

# Composition control plane — R&D and knowledge capture (001)

## Purpose

This document **captures** founder/operator **insights**, **constraints**, and **open questions** that informed **AMD-2026-008-ADD-001**–**ADD-003**. It is **informative** **knowledge**, **not** **normative** **doctrine**. Use it to **ground** revisions to the addenda and to **avoid** repeating the process gap: **jumping** from **raw** **R&D** **directly** to **draft** **amendments** **without** **architect** **partitioning**, **UI**/**shell** **grounding**, or **knowledge-basis** **normalization** (see **[AIOS-AMD-PLAN-001](AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** for the **optional** **full** **planning** **stack**).

**Related:** **[AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001](AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.md)** (bounded domains and addendum seams), **[AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001](AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001.md)** (surface grammar and states).

---

## Process defect (what was skipped)

| Layer | Intended role | Effect when skipped |
|-------|----------------|----------------------|
| **Knowledge capture** (this note) | Separate **principles** from **implementation** and **open** **questions** | Doctrine mixed with undigested R&D |
| **Architect synthesis** | **Partition** **control-plane** **domains**; **split**/**merge** **recommendations** | **Bundling** **pressure** and **ADD-003** **sprawl** |
| **UI/shell synthesis** | **Visible** **primitives**, **states**, **gates** **grounded** **in** **shell** **patterns** | **Abstract** **rules** **or** **orphan** **UI** **phrasing** |
| **Knowledge-basis sufficiency** | **What** **exists** **in** **specs**/**KB** **vs** **assumption** | Reviewers **and** **runtime** **inherit** **hidden** **assumptions** |

**Not** a failure of **ideas** — a **compression** of **stages** that **[AMD-2026-005](../amendments/AMD-2026-005.md)** **peer** **review** **alone** **cannot** **fully** **substitute** **for**.

---

## Principles (clustered)

- **Composition** is **not** **freeform** **length**; it is **class** + **contract** + **action** **semantics**.
- **Navigation** (**START** **HERE**, **continue**, **choose**, **input** **classes**) is **shell** **grammar**, **not** **model** **style**.
- **Output** **depth** and **voice** **controls** (**VC0**–**VC5**) **SHALL** be **shell** **obligations**, **not** **optional** **skills**.
- **Knowledge** **basis** and **discovery** **before** **creation** **SHALL** **govern** **when** **drafting** **outruns** **grounding**.
- **Originality** and **source-boundary** **gate** **SHALL** **reduce** **reproduction** **risk** **without** **claiming** **absolute** **copyright** **outcomes**.
- **Reference** **documents** **SHALL** **guide** **shape** **and** **spirit** **(reference** **adherence**, **not** **model** **temperature**)** **without** **authorizing** **wholesale** **copying**.
- **Professional** **drafts** **SHALL** **carry** **disclosure** **and** **review** **posture** **per** **policy** (**§9.4** **line**).

---

## Constraints and risks

- **Risk:** **Treating** **retrieval** **as** **permission** **to** **reproduce** **KB** **or** **source** **text**.
- **Risk:** **Confusing** **reference** **guidance** **with** **verbatim** **copying** **or** **with** **authoritative** **court**/**regulator** **forms** **without** **explicit** **role**.
- **Risk:** **Measurement** **claims** **without** **method**/**unit**/**basis** **discipline**.
- **Risk:** **Publishing**/**send**/**export** **without** **stacking** **gates** (**originality**, **professional**, **premium** **BOOK** paths).
- **Constraint:** **Parent** **[AMD-2026-008](../amendments/AMD-2026-008.md)** **is** **ratified**; **addenda** **extend** **composition**/**voice**/**surface** **doctrine** **without** **re‑opening** **§3.1** **runtime** **package** **unless** **a** **future** **amendment** **says** **so**.

---

## Control requirements (candidate themes)

| Theme | Where it landed (addendum) |
|-------|---------------------------|
| **Navigation** **classes** | **[ADD-001](../amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)** |
| **Depth**/**VC**/**packaging**/**BOOK** | **[ADD-002](../amendments/AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** |
| **Composition** **classes**, **contract**, **language**, **measurement**, **KB**, **originality**, **reference** **adherence** | **[ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** |

---

## Open questions (for next doctrine pass)

1. **Split** **vs** **trim:** **Should** **any** **ADD-003** **sections** **move** **to** **a** **separate** **addendum** **or** **SPEC** **annex** **to** **reduce** **reader** **load**?
2. **Product** **binding:** **Which** **fields** **are** **MUST** **implement** **in** **shell** **vs** **MAY** **map** **for** **v1**?
3. **KB** **pipeline:** **What** **is** **normative** **here** **vs** **in** `operations`/retrieval **implementation** **docs**?
4. **Overlap** **with** **AIOS-SPEC-009** **§16**/**§17** — **confirm** **no** **dual** **source** **of** **truth** **for** **lanes** **vs** **composition** **plane**.

---

## Maintenance

- **Revise** **this** **note** **when** **operator** **knowledge** **materially** **changes** **or** **after** **architect**/**surface** **memos** **freeze** **a** **new** **partitioning**.

---

*End of AIOS-COMPOSITION-CONTROL-RD-NOTES-001, version 1.0.0 (draft).*


---

## Cross-reference bundle: `AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001`

**[Bundled cross-reference — use this file’s version]** **`AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001`** — **version** **`1.0.0`**

---

---
document_id: AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001
version: 1.0.0
status: draft
category: reference
title: Shell and composition — surface grammar and user-state memo (AMD-2026-008 addendum track)
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008-ADD-001
  - doc_id: AMD-2026-008-ADD-002
  - doc_id: AMD-2026-008-ADD-003
  - doc_id: AIOS-SPEC-006
  - doc_id: AIOS-COMPOSITION-CONTROL-RD-NOTES-001
  - doc_id: AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001
note: Informative UI/shell grounding; product implementation is ai-os-voice-interface.
amendment_history:
  - version: 1.0.0
    date: 2026-04-10
    summary: Initial surface memo — primitives, VC, BOOK gates, review states, paid gates; maps to addenda.
---

# Shell and composition — surface grammar and user-state memo (001)

## Purpose

This memo **backfills** the **UI/shell** **synthesis** **layer**: **what** **users** **and** **operators** **should** **see** **and** **traverse** **so** **that** **[ADD-001](../amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**/**[ADD-002](../amendments/AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)**/**[ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** **doctrine** **does** **not** **float** **without** **surface** **consequence**. It is **informative** **only**; **normative** **UI** **law** **remains** **[AIOS-SPEC-006](../specifications/UIComponentRegistryStandard.md)** **where** **it** **applies**.

**Inputs:** **[AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001](AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.md)**.

---

## Navigation primitives (ADD-001) — surface mapping

| Primitive | User-visible meaning | Typical transition |
|-----------|----------------------|---------------------|
| **START_HERE** | **Entry** **point**; **one** **recommended** **next** **step** | **Idle** **→** **focused** **task** |
| **CONTINUE** | **Resume** **linear** **flow** **without** **branching** | **Step** **n** **→** **n+1** |
| **CHOOSE** | **Explicit** **choice** **among** **options** | **Branch** **selection** |
| **SINGLE_INPUT** | **One** **slot** (e.g. **text**, **confirm**) | **Collect** **→** **validate** |
| **MULTI_INPUT** | **Several** **slots** **before** **proceed** | **Form** **→** **submit** |

**Design rule:** **Navigation** **class** **SHALL** **be** **visible** **or** **derivable** **from** **shell** **chrome** (footer, **prompt** **context**, **or** **voice** **system** **turn**) — **not** **only** **inferred** **from** **model** **prose**.

---

## Output depth and voice (ADD-002) — surface mapping

| Control | User-visible meaning |
|---------|----------------------|
| **Depth** **(RESPONSE** **→** **BOOK**)** | **How** **much** **artifact** **is** **being** **produced**; **BOOK** **implies** **long-form** **structure** **and** **review** **checkpoints** |
| **VC0**–**VC5** | **Density**, **delivery**, **interruption**, **transformation**, **routing**, **segment** **traversal** **—** **shell** **controls** **over** **narration** |
| **Packaging** | **Export** **format** **(TXT**/**MD**/**PDF**/**DOCX**/**JSON**/**HTML**)** **as** **explicit** **action** **or** **preview** |

**Promotion** **paths** **(draft** **→** **review** **→** **export**/**send**)** **SHALL** **remain** **explicit** **actions**, **not** **silent** **model** **side** **effects**.

---

## BOOK workflow (ADD-002 §10–§10.11) — gates as surfaces

| Gate | Surface idea |
|------|----------------|
| **TOC** **/** **chapter** **approval** | **Review** **canvas** **with** **approve**/**revise** **per** **section** |
| **Final** **assembly** | **Explicit** **“assemble”** **or** **“freeze** **structure”** **before** **export** |
| **Premium** **(§10.11)** | **Gated** **actions** **(images**, **layout**, **publish-ready** **package**)** **with** **entitlement** **disclosure** |

---

## Composition plane (ADD-003) — states and gates

| Concept | Surface idea |
|---------|----------------|
| **Composition** **contract** | **Role**/**intent**/**outcome** **captured** **before** **or** **during** **draft** (**wizard** **or** **compact** **confirm**) |
| **Knowledge** **basis** | **“Grounding** **required”** **/** **“Discovery** **suggested”** **banners**; **block** **or** **scaffold** **when** **insufficient** |
| **Measurement** **confirmation** | **Prompt** **for** **method**/**unit**/**basis** **when** **claims** **are** **material** |
| **Professional** **disclosure** (**§9.4**)** | **Mandatory** **label** **and** **export** **preservation** |
| **Originality**/**overlap** (**§19**) | **Status** **badges** (e.g. **review** **required**, **blocked**) **before** **send**/**publish** |
| **Reference** **adherence** (**§20**)** | **Sliders**/**presets** **(1**–**10** **or** **structure**/**style** **split**)** **labeled** **as** **layout**/**conformity**, **not** **temperature** |
| **Reference** **role** | **Picker** **for** **example** **vs** **template** **vs** **authority** |

---

## Implementation note

**Product** **repo:** **ai-os-voice-interface**. **Refresh** **product** **context** **before** **alignment** **reviews:** `py -3 scripts/generate_product_context_bundle.py` **(see** **[DEVELOPER.md](../DEVELOPER.md)****)**.

---

*End of AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001, version 1.0.0 (draft).*


---

## Cross-reference bundle: `AMD-2026-008`

**[Bundled cross-reference — use this file’s version]** **`AMD-2026-008`** — **version** **`1.0.0`**

---

---
document_id: AMD-2026-008
version: 1.0.0
status: ratified
category: amendment
title: Sovereign Voice and Local Runtime Lanes (Incorporation by Reference)
author: Gateway Global AIOS
created: 2026-04-04
last_updated: 2026-04-10
ratification_target: "2026-04-08"
supersedes: null
addenda:
  - path: amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md
    title: Base Shell Navigation Primitives and Start-Here Control
  - path: amendments/AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md
    title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
  - path: amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
    title: Composition Control Plane for Messages, Invites, and Documents
cross_references:
  - doc_id: AMD-2026-008-RATIFICATION-MOTION
    title: Ratification motion — AMD-2026-008
    relationship: ratification_motion
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
  - doc_id: AIOS-SPEC-007
    title: Google Workspace Integration Governance
  - doc_id: OLLAMA_RUNTIME_STANDARD
    title: Ollama Local Model Runtime Standard
  - doc_id: WHISPER_RUNTIME_STANDARD
    title: Whisper / faster-whisper Local STT Runtime Standard
  - doc_id: LOCAL_TTS_RUNTIME_STANDARD
    title: Local Text-to-Speech (TTS) Runtime Standard
  - doc_id: MPOA
    title: Master Platform Operating Agreement
amendment_history:
  - version: 1.0.0
    date: 2026-04-08
    summary: "Ratified per AMD-2026-008-RATIFICATION-MOTION v1.0.2; substantive basis draft v1.2.0; §3.1 incorporation package frozen (AIOS-SPEC-009 0.5.7; AIOS-OPS-001–003 0.1.0); Round 3 triangulation complete (AMD-2026-005 thresholds); closure 2026-04-08."
  - version: 1.2.0
    date: 2026-04-04
    summary: "Final tightening (pre-ratification draft): objective re-ratification trigger (§3.3.3); AIOS-OPS-001–003 registry aliases; disclosure mechanism (§4.3); §4.4 triggers; Round 2 review (Set 1b)."
  - version: 1.1.0
    date: 2026-04-04
    summary: "Major revision: incorporation by reference (§3), binding clauses (§4), WORKSPACE.md informative (§3.2), shell readiness §4.4, MPOA cross-ref §5."
  - version: 0.1.0
    date: 2026-04-04
    summary: "Initial draft (package manifest — superseded in structure by 1.1.0)."
---

# AMD-2026-008 — Sovereign Voice and Local Runtime Lanes

## 1. Purpose

This amendment **ratifies**, as a **single governed package**, the **sovereign runtime stack** for **speech-input**, **interpretation**, and **speech-output**, and binds the platform to **incorporated** normative documents listed in Section 3. It **does not** replace substantive law in those documents; it **adopts** them for ratification and **adds** the obligations in Sections 4–6.

**Ratification process:** This amendment **SHALL** become effective only upon **Council ratification** and registration in accordance with the **Governance Constitution** (legislative process for amendments and binding documents).

**Scope**

- **Speech-input** (local STT), **interpretation** (local LLM / Ollama), and **speech-output** (local TTS) are **distinct lanes** (**AIOS-SPEC-009**, Section 17).
- This amendment addresses **procedural completeness** and **binding language** for council ratification; operational detail remains in the **incorporated standards** unless Section 4 states otherwise.

---

## 2. Definitions

| Term | Meaning |
|------|--------|
| **Sovereign voice mode** | Any product or environment **declared** as local-first, sovereign, or air-gapped for **voice** or **audio** processing, per **AIOS-SPEC-009** Section 17. |
| **Incorporated document** | A document listed in Section 3.1 as part of the **ratification package**, as amended from time to time under its own revision process. |
| **Workspace Domain Pack (informative registry)** | The **WORKSPACE.md** file in the AI OS voice interface repository, which **aligns** capability ids with **AIOS-SPEC-007** and **AIOS-SPEC-009**; it is **informative** unless a future amendment elevates it to normative status. **Normative** capability requirements for Workspace integration remain **AIOS-SPEC-007**; **normative** intent and lanes remain **AIOS-SPEC-009**. |

---

## 3. Incorporation by reference (ratification package)

### 3.1 Documents adopted as substantive normative law

Upon **ratification** of **AMD-2026-008**, the following **governed documents** are **incorporated by reference** and constitute the **substantive normative package** ratified together with this amendment:

| Registry ID (canonical) | Document ID | Title | Role |
|-------------------------|---------------|--------|------|
| — | **AIOS-SPEC-009** | *Intent Primitive and Execution Model* | Section 16 local interpretation lane (Ollama); Section 17 sovereign voice and local runtime lanes; **POL-LANE-VOICE-001**–**003**; **POL-MODEL-001**–**004** where applicable. |
| **AIOS-OPS-001** | **OLLAMA_RUNTIME_STANDARD** | *Ollama Local Model Runtime Standard* | Interpretation runtime: readiness, fallback, disclosure, capabilities (`local.llm.*`). |
| **AIOS-OPS-002** | **WHISPER_RUNTIME_STANDARD** | *Whisper / faster-whisper Local STT Runtime Standard* | Speech-input runtime: readiness, fallback, disclosure, capability `local.stt.transcribe`. |
| **AIOS-OPS-003** | **LOCAL_TTS_RUNTIME_STANDARD** | *Local Text-to-Speech (TTS) Runtime Standard* | Speech-output runtime: readiness, fallback, disclosure, capability `local.tts.speak`. |

**Registry discipline:** **AIOS-OPS-001** through **AIOS-OPS-003** are the **canonical registry aliases** for the three operations standards in the governance graph; **OLLAMA_RUNTIME_STANDARD**, **WHISPER_RUNTIME_STANDARD**, and **LOCAL_TTS_RUNTIME_STANDARD** remain the **stable document_id** values in each file’s front matter and **SHALL** resolve to the same governed artifact as **AIOS-OPS-001**–**003** respectively.

**Effect**

- The **current** revision of each document **as of the ratification date** is incorporated, subject to Section 3.3.
- Implementations **SHALL** treat violations of incorporated **SHALL** / **MUST NOT** language in those documents as **governance violations** in scope for this amendment.

### 3.2 Informative alignment artifact (not incorporated as standalone law)

| Artifact | Role |
|----------|------|
| **WORKSPACE.md** (Workspace Domain Pack v1, repository root) | **Informative** capability registry and operator notes; **MUST** remain **aligned** with **AIOS-SPEC-007** and **AIOS-SPEC-009** as implemented. **Normative** force for Workspace tools and intents remains **AIOS-SPEC-007**; **normative** force for lanes and voice policy remains **AIOS-SPEC-009** and Section 3.1 above. |

### 3.3 Revisions to incorporated documents and re-ratification of this amendment

**3.3.1** Amendments to **AIOS-SPEC-009** or to **OLLAMA_RUNTIME_STANDARD**, **WHISPER_RUNTIME_STANDARD**, or **LOCAL_TTS_RUNTIME_STANDARD** **SHALL** follow their respective governance processes.

**3.3.2** Re-ratification of **AMD-2026-008** **SHALL NOT** be required solely for **editorial** or **clarifying** updates to incorporated standards **that do not** change the normative force of any clause that used **SHALL**, **MUST**, or **MUST NOT** in the revision that was incorporated at **AMD-2026-008** ratification.

**3.3.3 (Objective trigger)** Re-ratification of **AMD-2026-008** **SHALL** be required, and the **Council** **SHALL** issue a **new amendment** or **revision** to **AMD-2026-008**, if any **incorporated document** under Section 3.1 is amended such that it **alters**, **removes**, or **makes optional** any clause that contained **SHALL**, **MUST**, or **MUST NOT** in the revision incorporated at **AMD-2026-008** ratification.

**3.3.4** If a **conflict** arises between Sections 4–6 of this amendment and a later revision of an incorporated document, **this amendment** **SHALL** be **reconciled** by **Council** amendment or supersession in accordance with the **Governance Constitution**.

---

## 4. Normative obligations (binding clauses)

The following obligations apply **in addition to** incorporated documents listed in Section 3.1.

**4.1 Lanes**

The platform **SHALL** treat **speech-input**, **interpretation**, and **speech-output** as **separate** governed runtime lanes where **AIOS-SPEC-009** Section 17 applies, and **SHALL NOT** conflate STT, local LLM inference, or TTS into a single undifferentiated “voice API.”

**4.2 Silent remote substitution**

The platform **MUST NOT** **silently** substitute **remote** STT, **remote** TTS, or **remote** interpretation for tasks designated **sovereign** or **local-first** for that lane, except where **explicit** policy and **user or operator** visibility exist, per **AIOS-SPEC-009** Sections 16.4 and 17.4, and **POL-LANE-VOICE-001**–**003** / **POL-MODEL-003**.

**4.3 Readiness and disclosure (mechanism)**

The platform **SHALL** expose **readiness** state for each applicable local runtime **before** offering execution or inference on that lane for **sovereign** modes, per the incorporated runtime standards.

**Disclosure mechanism (minimum):**

- **Readiness** and **fallback posture** **SHALL** be visible on the **shell** or **session summary** (or equivalent **primary** chrome), consistent with **AIOS-SPEC-006** transparency expectations, when a lane is **in scope** for the active session.
- **Readiness** **SHALL** be **disclosed** on **operator** or **audit** surfaces when invoked, such that **unavailable** or **degraded** states are **not** treated as **available** without disclosure.
- **Remote** fallback, when policy-allowed, **SHALL** remain **traceable** (operator trace or equivalent) per Section 4.5.

**4.4 Shell and session summary (pre-production requirement)**

Before **production** deployment, **multi-tenant** exposure, or **non-founder** environments (whichever occurs first) for **sovereign voice** features, the **shell** or **session summary** (or equivalent primary chrome) **SHALL** disclose **side-by-side** readiness for **local STT**, **local interpretation (Ollama)**, and **local TTS** when those lanes are **in scope**, using **consistent** readiness language and **fallback posture** across lanes, aligned with **OLLAMA_RUNTIME_STANDARD** Section 8 and the analogous disclosure sections in **WHISPER_RUNTIME_STANDARD** and **LOCAL_TTS_RUNTIME_STANDARD**.

**4.5 Auditability of fallback**

Where **remote** fallback is **allowed** by policy, such use **SHALL** be **auditable** (operator trace or equivalent), per **POL-MODEL-003** and **POL-LANE-VOICE-003**.

---

## 5. Economics, liability, and data classification (cross-reference)

**5.1** Remote fallback and processing of **voice audio**, **transcripts**, or **inference payloads** in **non-local** regimes **SHALL** remain subject to **data classification**, **tenant policy**, and **commercial** terms in the **Master Platform Operating Agreement** (MPOA) and related **legal** instruments where applicable. This amendment **does not** waive or rewrite **MPOA** economics or liability allocations.

**5.2** **SHALL NOT**: This amendment **SHALL NOT** be read to permit **silent** cross-border or **unapproved** data processing; **incorporated** runtime standards under Section 3.1 and the **MPOA** **SHALL** be read **together** where both apply.

---

## 6. Deliverables summary (informative)

| Deliverable | Governed ID / artifact |
|-------------|-------------------------|
| Specification text for Section 17 and lane policy | **AIOS-SPEC-009** (repository: `specifications/IntentPrimitiveAndExecutionModel.md`) |
| Ollama operational standard | **AIOS-OPS-001** / **OLLAMA_RUNTIME_STANDARD** |
| Whisper / STT operational standard | **AIOS-OPS-002** / **WHISPER_RUNTIME_STANDARD** |
| Local TTS operational standard | **AIOS-OPS-003** / **LOCAL_TTS_RUNTIME_STANDARD** |
| Informative capability registry alignment | **WORKSPACE.md** (see Section 3.2) |

---

## 7. Implementation sequencing (informative)

1. **Ratify** **AMD-2026-008** and incorporated Section 3.1 documents per **Governance Constitution** and Council process.
2. **Implement** shell/session readiness disclosure per Section 4.4 **before** production, multi-tenant, or non-founder exposure of sovereign voice features.
3. **Maintain** **WORKSPACE.md** alignment with **AIOS-SPEC-007** / **AIOS-SPEC-009** as code evolves.

---

## 8. Revision history

| Version | Date | Summary |
|---------|------|---------|
| 1.0.0 | 2026-04-08 | **Ratified** per **AMD-2026-008-RATIFICATION-MOTION** **v1.0.2**; substantive basis **draft v1.2.0**; **§3.1** incorporation package frozen at ratification (see front matter **amendment_history**). |
| 1.2.0 | 2026-04-04 | **Final tightening:** objective re-ratification trigger (Section 3.3.3); **AIOS-OPS-001**–**003** registry aliases; disclosure **mechanism** (Section 4.3); Section 4.4 triggers (production / multi-tenant / non-founder); Constitution ratification sentence (Section 1); MPOA spelled out on first use (Section 5.1); Section numbering in prose for style consistency; Round 2 review (Set 1b). |
| 1.1.0 | 2026-04-04 | **Major revision:** incorporation by reference (Section 3), binding clauses (Section 4), **WORKSPACE.md** informative (Section 3.2), shell readiness Section 4.4, MPOA cross-ref Section 5, formal document IDs; triage after triangulated peer review (Set 1). |
| 0.1.0 | 2026-04-04 | Initial draft (package manifest — superseded in structure by 1.1.0). |

---

**End of AMD-2026-008**


---

## Cross-reference bundle: `AMD-2026-008-ADD-001`

**[Bundled cross-reference — use this file’s version]** **`AMD-2026-008-ADD-001`** — **version** **`0.1.0`**

---

---
document_id: AMD-2026-008-ADD-001
parent_amendment: AMD-2026-008
parent_version: 1.0.0
version: 0.1.0
status: draft
category: amendment_addendum
title: Base Shell Navigation Primitives and Start-Here Control
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-09
cross_references:
  - doc_id: AMD-2026-008
    title: Sovereign Voice and Local Runtime Lanes (Incorporation by Reference)
  - doc_id: AMD-2026-008-ADD-002
    title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
addendum_history:
  - version: 0.1.0
    date: 2026-04-09
    summary: Initial draft — navigation classes (START_HERE, CONTINUE, CHOOSE, SINGLE_INPUT, MULTI_INPUT); alert/continue/choose/single/multi primitives; cross-ref ADD-002 for output depth and shell voice controls.
---

# AMD-2026-008-ADD-001 — Base Shell Navigation Primitives and Start-Here Control

## 0. Status and intent

| Field | Value |
|-------|--------|
| **Status** | **`draft` `0.1.0`** — addendum to **[AMD-2026-008](AMD-2026-008.md)** **1.0.0** |
| **Does not replace** | **AMD-2026-008** remains the parent framework for **sovereign voice** and **local runtime lanes**. This addendum defines the **navigation** axis of the shell control plane. **Output depth**, **shell voice output controls**, and **packaging** are governed by **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)**. |

---

## 1. Purpose

This addendum defines **base shell navigation primitives**—including **start-here** and **continuation** behavior—so that session flow, choice, and input capture are **shell-governed**, not improvised by model habit or ad hoc agent skills.

## 2. Governing principle

The shell **SHALL** expose **deterministic navigation classes** for how the user moves through a session. **Navigation** governs **where the user is in the flow**; it **SHALL NOT** be conflated with **how much** is said (**ADD-002** output depth), **how** speech is delivered or interrupted (**ADD-002** shell voice controls), or **export format** (**ADD-002** packaging).

## 3. Navigation classes

The following **navigation classes** are **normative labels** for shell-level routing. Implementations **MAY** surface them under product-specific names; behavior **SHALL** remain mappable to these classes.

| Class | Meaning |
|-------|--------|
| **START_HERE** | Initial orientation: where to begin, what the session is for, or recovery to a known entry point. |
| **CONTINUE** | Proceed along the current thread without forcing a new branch or capture shape. |
| **CHOOSE** | Discrete selection among presented options (list, tiles, voice enumeration, or equivalent). |
| **SINGLE_INPUT** | One primary free-form input (utterance, prompt, or single field). |
| **MULTI_INPUT** | Structured capture of **multiple** fields, slots, or sequential answers in one governed interaction. |

## 4. Core primitives (mapping)

These **primitives** **SHALL** be realizable as **shell affordances** (voice, touch, or equivalent), not only as model behaviors:

| Primitive | Role |
|-----------|------|
| **Alert** | Interruptive or high-priority notice; **SHALL** be distinguishable from routine continuation and **SHALL NOT** silently replace structured choice or input capture. |
| **Continue** | Maps to **CONTINUE** — advance or resume without redefining capture shape. |
| **Choose** | Maps to **CHOOSE** — pick among explicit options. |
| **Single input** | Maps to **SINGLE_INPUT** — one primary response channel for the active step. |
| **Multi input** | Maps to **MULTI_INPUT** — multiple fields or steps under one governed pattern. |

## 5. Shell obligations (navigation)

The shell **SHALL**:

1. Make the **active navigation class** **observable** to the user when ambiguity would cause mis-routing (e.g. choose vs free-form).
2. **NOT** treat **navigation** as interchangeable with **verbosity** or **export**; those are **ADD-002**.
3. Preserve **auditability** of **branching** and **selection** consistent with **AIOS-SPEC-009** session and intent boundaries where applicable.

## 6. Non-goals

This addendum does not define:

- output depth, narration density, or **shell voice output controls** (**ADD-002**)
- output packaging or export formats (**ADD-002**)
- visual styling tokens or chrome layout
- workspace tool routing or **AIOS-SPEC-007** integration detail

---

*End of AMD-2026-008-ADD-001, version 0.1.0 (draft).*


---

## Cross-reference bundle: `AMD-2026-008-ADD-002`

**[Bundled cross-reference — use this file’s version]** **`AMD-2026-008-ADD-002`** — **version** **`0.13.0`**

---

---
document_id: AMD-2026-008-ADD-002
parent_amendment: AMD-2026-008
parent_version: 1.0.0
version: 0.13.0
status: draft
category: amendment_addendum
title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
author: Gateway Global AIOS
created: 2026-04-09
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008
    title: Sovereign Voice and Local Runtime Lanes (Incorporation by Reference)
  - doc_id: AMD-2026-008-ADD-001
    title: Base Shell Navigation Primitives and Start-Here Control
  - doc_id: MPOA
    title: Master Platform Operating Agreement
    note: Commercial entitlements and tiers for premium BOOK capabilities (Section 10.11).
  - doc_id: AMD-2026-008-ADD-003
    title: Composition Control Plane for Messages, Invites, and Documents
    note: Composition classes, document subclasses, action semantics, composition contract (§5), language/localization (§16), measurement contract (§17), knowledge basis/discovery (§18), originality/source-boundary (§19), reference-guided composition (§20 incl. adherence §20.11–§20.15), professional disclosure (§9.4); orthogonal to depth/packaging.
addendum_history:
  - version: 0.13.0
    date: 2026-04-10
    summary: ADD-003 §20.11–§20.15 reference adherence (1–10; optional structure/style split; innovation_mode); axis-12 scope note.
  - version: 0.12.0
    date: 2026-04-10
    summary: Twelve-axis table — ADD-003 §20 reference-guided composition (template vs reference vs authority; R1–R3).
  - version: 0.11.0
    date: 2026-04-10
    summary: Eleven-axis table — ADD-003 §19 originality / source-boundary / non-reproduction verification.
  - version: 0.10.0
    date: 2026-04-10
    summary: Ten-axis table — ADD-003 §18 knowledge basis / discovery gating.
  - version: 0.9.0
    date: 2026-04-10
    summary: Nine-axis table — ADD-003 §17 measurement contract / quantified claims.
  - version: 0.8.0
    date: 2026-04-10
    summary: Eight-axis table — ADD-003 §16 language/localization/authoritative version.
  - version: 0.7.0
    date: 2026-04-10
    summary: Seven-axis table — ADD-003 composition contract (role/intent/outcome) §5; composition class §§7–10; document subclass §9.2.
  - version: 0.6.0
    date: 2026-04-10
    summary: ADD-003 filename/title — composition control plane (messages, invites, documents, publications); six-axis table (subclass in ADD-003 §7.2).
  - version: 0.5.0
    date: 2026-04-10
    summary: Cross-reference ADD-003 — five-axis control plane; artifact output classes (A0–A5) defined in ADD-003, not in ADD-002.
  - version: 0.4.0
    date: 2026-04-10
    summary: BOOK base vs premium product gates — Authoring / Enhancement / Publishing feature classes; paid entitlement for images, layout, publish-ready packaging, distribution; SHALL NOT auto-image or auto-publish; shell gated controls; simple vs publish-ready PDF split (§7.3, §10.11).
  - version: 0.3.0
    date: 2026-04-09
    summary: BOOK hard approval gates — TOC/chapter/final assembly; phased workflow B0–B9; review state machine; shell approve/revise/export controls; BOOK as human-guided co-authored artifact; SHALL NOT opaque single-pass BOOK generation.
  - version: 0.2.0
    date: 2026-04-09
    summary: Shell voice control classes VC0–VC5; four-axis control-plane model; voice-shell obligations; promotion rules (user/shell/workflow/policy); book threshold includes navigable voice segmentation; cross-ref ADD-001.
  - version: 0.1.0
    date: 2026-04-09
    summary: Initial draft — output depth ladder (V0–V4), promotion rules, packaging classes (TXT/MD/PDF/DOCX/JSON/HTML), book threshold, non-goals.
---

# AMD-2026-008-ADD-002 — Verbose Grounding, Shell Voice Output Control, and Output Packaging

## 0. Status and intent

| Field | Value |
|-------|--------|
| **Status** | **`draft` `0.13.0`** — addendum to **[AMD-2026-008](AMD-2026-008.md)** **1.0.0** |
| **Does not replace** | **AMD-2026-008** remains the parent framework for **sovereign voice** and **local runtime lanes**. This addendum governs **output depth**, **shell-level voice output controls**, and **export/render packaging**. **Base navigation primitives** are **[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**. **Composition classes** (messages, invites, documents, publications) are **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)**. |

---

## 1. Purpose

This addendum defines:

1. the governed **output depth** ladder for AI OS surfaces,
2. **shell voice control** classes that govern **narration density**, **delivery**, **interruption**, **transformation**, **routing**, and **segment traversal**—as **shell affordances**, not optional agent skills or default model style, and
3. allowed **output packaging** classes for rendered or exported content, and
4. **BOOK**-class **human-guided** progression through **explicit review checkpoints** (Section 10), and
5. **product/commercial gates** for **value-added** **BOOK** capabilities—**enhancement** and **publishing**—distinct from the **base authoring** workflow (Section 10.11).

**Composition artifact classes** (e.g. **EMAIL**, **CALENDAR_INVITE**, **DOCUMENT** subclasses, **POST**, **BLOG**, **BOOK**) are **not** defined in this addendum; they are **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)**.

## 2. Governing principle

The system **SHALL** produce the **minimum output depth** necessary to satisfy the **active intent** and **actor context**. **Shell voice controls** **SHALL** govern **expansion**, **reduction**, **traversal**, **interruption**, and **output transformation** so that voice-first delivery is not left to unconstrained model discretion.

**Normative line:** Output depth, narration length, explanation expansion, and traversal of long-form content **SHALL** be controlled through **shell-level voice controls** and **SHALL NOT** be left solely to model discretion or skill-level implementation.

Richer explanation, longer exposition, and artifact-grade outputs require **explicit** authorization via **user request**, **shell control**, **policy**, **workflow requirement**, or **export intent**—consistent with Section 9.

## 3. Control-plane model (twelve axes)

| Axis | Governed by | Scope |
|------|-------------|--------|
| **1. Navigation class** | **[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)** | START_HERE, CONTINUE, CHOOSE, SINGLE_INPUT, MULTI_INPUT |
| **2. Output depth** | This addendum (Section 4; **BOOK** also Section 10) | RESPONSE, SUMMARY, EXPLANATION, BRIEF, BOOK |
| **3. Shell voice controls** | This addendum (Section 5) | VC0–VC5 |
| **4. Output packaging** | This addendum (Section 7) | TXT, MD, PDF, DOCX, JSON, HTML |
| **5. Composition class** | **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** §§7–10 | EMAIL, CALENDAR_INVITE, DOCUMENT, POST, BLOG, ARTICLE, … |
| **6. Document subclass** | **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** §9.2 | MEMO, LETTER, PROPOSAL, SPEC, RESEARCH_REPORT, BOOK, … |
| **7. Composition contract** | **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** §5 | role, intent, outcome (composed artifacts) |
| **8. Language / localization** | **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** §16 | L0–L3, authoritative_language, translation_mode |
| **9. Measurement / quantified claims** | **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** §17 | method, unit, basis, precision |
| **10. Knowledge basis / discovery** | **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** §18 | sufficiency state, discovery-before-creation, creation mode |
| **11. Originality / source-boundary** | **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** §19 | non-reproduction verification, quote/quoting posture |
| **12. Reference-guided composition** | **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** §20 | reference vs template vs authority; **adherence** 1–10 (**§20.13**); optional structure/style split; **not** **temperature** |

## 4. Output depth ladder

### 4.1 V0 — RESPONSE

Smallest valid answer.

Allowed:

- short alert
- short answer
- one action
- one-line result

Use when:

- immediate status is enough
- action is primary
- explanation is unnecessary

### 4.2 V1 — SUMMARY

Condensed statement of the key point.

Allowed:

- short paragraph
- 2–5 bullets or equivalent structure
- one next action

Use when:

- user needs orientation
- result must be compressed
- follow-up decision is likely

### 4.3 V2 — EXPLANATION

Clear explanation of why, how, or what changed.

Allowed:

- multiple paragraphs
- short sections
- examples
- caveats

Use when:

- reasoning must be understandable
- user needs operational clarity
- the system must justify a result

### 4.4 V3 — BRIEF

Structured decision or work document.

Allowed:

- title
- executive summary
- sections
- findings
- recommendations
- tables/lists where appropriate

Use when:

- user must review and act
- the output is work-product grade
- a packet or memo is needed

### 4.5 V4 — BOOK

Long-form reference or governed artifact. A **BOOK** is **not** a normal single-pass response; it is a **human-guided, co-authored governed artifact**. **Section 10** (approval gates, workflow, and shell controls) **SHALL** apply.

Allowed:

- title page or header
- executive overview
- table of contents
- chapters/sections
- appendices
- references
- export-ready structure

Use when:

- the artifact itself is the intended output
- doctrinal or educational depth is required
- persistent reference value justifies long form

## 5. Shell voice control classes

These are **shell affordances** that control **narration density** and **delivery behavior**. They **SHALL NOT** be defined solely as **agent skills** or **ad hoc conversational habits**; the shell **SHALL** expose governed mappings (e.g. user utterance “shorter” **SHALL** map to **VC1**, not an unconstrained model length change).

### 5.1 VC0 — Stop / Pause / Continue

Controls **live speech flow**.

Examples (illustrative):

- Stop, Pause, Resume, Continue

### 5.2 VC1 — Shorten

Reduce verbosity.

Examples (illustrative):

- Shorter, Just the answer, Give me the summary, Less detail

### 5.3 VC2 — Expand

Increase verbosity.

Examples (illustrative):

- Explain, Tell me more, Go deeper, Walk me through it

### 5.4 VC3 — Transform

Change **presentation** or **depth class** without necessarily changing the **underlying result** (subject to policy and truthfulness constraints).

Examples (illustrative):

- Turn this into a summary, Make this a brief, Convert this to a document, Show as book, Read bullet points

### 5.5 VC4 — Route

Move across **shell surfaces** or **modalities**.

Examples (illustrative):

- Show on canvas, Read aloud, Stop reading and show text, Export this, Save as PDF

### 5.6 VC5 — Segment navigation

Move **within** a long output.

Examples (illustrative):

- Next section, Previous section, Skip ahead, Go to table of contents, Read chapter 2, Jump to recommendations

## 6. Voice-shell obligations

The shell **SHALL** expose governed controls for:

1. **stopping** and **resuming** narration (**VC0**),
2. **reducing** or **increasing** detail (**VC1**, **VC2**) consistent with Section 4,
3. **transforming** presentation or depth class (**VC3**) within policy,
4. **switching** between voice and visual surfaces (**VC4**),
5. **navigating** long outputs by segment (**VC5**),
6. **export** or **render** requests that bind to **packaging** classes (Sections 7–8),
7. **BOOK** workflow **approval** and **progression** controls when **BOOK** depth is active (Section 10).

**Practical mapping (informative):** User utterances such as “shorter,” “explain that,” “put this on screen,” “make this a PDF,” “read the next part,” or “give me the summary” **SHALL** resolve through **shell-level** control-plane routing (**VC** classes and/or packaging), not discretionary model behavior alone.

## 7. Output packaging classes

### 7.1 TXT

Plain text output.

Use when:

- portability is primary
- no rich formatting is needed
- simple logging or copy/paste is desired

### 7.2 MD

Markdown output.

Use when:

- human-readable structure is needed
- repo-native or documentation-native workflows apply
- headings, lists, code blocks, or tables are needed

### 7.3 PDF

Fixed-layout read/share/print artifact.

**Product note:** **Policy** **MAY** distinguish **simple** or **personal review** PDF (e.g. manuscript snapshot) from **print-ready**, **image-enhanced**, or **publish-ready** PDF—**premium**-tier outputs are governed under **Section 10.11**, not by changing the **PDF** packaging class label alone.

Use when:

- presentation integrity matters
- printing matters
- signatures/review packet behavior is expected
- user should not casually mutate the layout

### 7.4 DOCX

Editable document output.

Use when:

- downstream editing is expected
- business/legal/admin users need office-native editing
- tracked revision workflows are likely

### 7.5 JSON

Structured machine-readable output.

Use when:

- another system consumes the result
- schema validation matters
- control-plane/runtime exchange is needed

### 7.6 HTML

Structured renderable output.

Use when:

- web rendering is primary
- the output is meant to be embedded or displayed in a browser context

## 8. Packaging rules

- TXT and MD are preferred for light-weight outputs.
- PDF is preferred for fixed review packets, print artifacts, and formal distributions.
- DOCX is preferred when user-side editing is expected.
- JSON is preferred for system interchange, not primary human review.
- HTML is preferred for governed web rendering, not archival doctrine by default.

## 9. Promotion rules

The runtime **SHALL NOT** promote output depth beyond **V0 RESPONSE** unless one or more of the following are true:

1. the **user** requests more detail,
2. **policy** requires explanation,
3. the **workflow** requires structured review,
4. **export packaging** requires a richer form,
5. the **current view class** explicitly permits richer output,
6. or a **shell voice control** (**VC2**, **VC3**, or equivalent governed path) **explicitly** authorizes deeper presentation.

The model **SHALL NOT** self-promote from **response**-class output to **book**-class output without **explicit** authorization from **user request**, **shell control**, **workflow requirement**, or **policy**. Promotion into **BOOK** **SHALL** enter the **BOOK workflow** (Section 10); **SHALL NOT** bypass **TOC**, **chapter**, or **final** approval gates.

## 10. BOOK approval and review gates

### 10.1 Classification and bottom line

A **BOOK**-class artifact **SHALL** be treated as a **human-guided composed artifact**, not a default long model answer. The system **MAY** **assist**, **scaffold**, **propose**, and **assemble**; the system **SHALL NOT** **unilaterally complete** and **finalize** a **BOOK** without **human review** at defined checkpoints.

**BOOK**-class output **SHALL** be **phased**, **review-gated**, and **human-guided**; **SHALL NOT** be **auto-finalized** in a single opaque pass.

### 10.2 Lower depth classes vs BOOK

| Depth | Generation posture (normative intent) |
|-------|----------------------------------------|
| **RESPONSE**, **SUMMARY**, **EXPLANATION**, **BRIEF** | **MAY** be produced more **directly** subject to Sections 2, 5–9 and policy. |
| **BOOK** | **SHALL** follow **Section 10** — **mandatory** **TOC approval**, **per-chapter** review gates, **assembly** review, and **final** approval before **export-ready** completion. |

### 10.3 Normative doctrine

**BOOK**-class output **SHALL** be treated as a **human-guided composed artifact**. The system **MAY** propose, draft, revise, and assemble; the system **SHALL NOT** **autonomously finalize** a **BOOK** without **human approval** of the **table of contents**, **each chapter’s** progression through review, and the **final assembled manuscript**. The runtime **SHALL** require **explicit human approval** of the **TOC** before **full** chapter drafting proceeds (beyond a **small sample** where **policy** permits). **Each chapter** **SHALL** pass a **review checkpoint** before it is treated as **approved for assembly**.

**BOOK** generation **SHALL NOT** operate as an **opaque single-pass** model response. The **BOOK** workflow **SHALL** expose **explicit review states** and **approval controls** in the **shell** (Section 10.8, 10.10).

### 10.4 Mandatory approval — table of contents

Before **full** drafting of the manuscript **SHALL** proceed, a **human** **SHALL** **approve** (including **edit**, **reorder**, **remove**, or **add** chapters, and **narrow** scope) at minimum:

- title
- purpose
- audience
- **table of contents**
- chapter order
- scope boundaries

**No** chapter drafting beyond a **small sample** **SHALL** proceed until this **TOC approval gate** is **resolved**, except as **policy** explicitly permits for a given deployment.

### 10.5 Mandatory approval — chapter progression

**Each chapter** **SHALL** move through a governed sequence that includes **human review** before the chapter is **locked** or **marked ready** for assembly. The system **MAY** generate objectives, outlines, drafts, and revisions; the system **SHALL NOT** treat the **full book** as **done** without **per-chapter** gate resolution.

**Next chapter** **SHALL NOT** be treated as **final sequence progress** until the **current** chapter’s gate is **resolved** (approve, revise, rewrite, defer, split, or merge — as exposed by the shell).

### 10.6 Mandatory approval — assembly and final

After **chapters** are **approved**, the system **MAY** assemble the manuscript, normalize tone and terminology, generate references, appendix, and front matter, and prepare **export** packages. A **final human review** **SHALL** occur before the artifact is treated as **complete** and **export-ready**.

### 10.7 BOOK workflow phases (B0–B9)

The **BOOK** workflow **SHALL** be **visible** and **phased**. The runtime **SHALL** implement **at least** the following phases (labels **MAY** differ by product):

| Phase | Name | Requirement |
|-------|------|-------------|
| **B0** | Book request recognized | User or workflow enters **BOOK** intent; scope capture begins. |
| **B1** | Scope contract | Gather topic, audience, purpose, desired depth, target **output package** (Section 7). |
| **B2** | TOC proposal | System proposes title, subtitle if needed, **TOC**, chapter summaries. |
| **B3** | **TOC approval gate** | Human **SHALL** approve, edit, reorder, remove, add, or narrow scope. **No full book generation** beyond this gate **without approval**. |
| **B4** | Chapter planning | Per chapter: objective, key points, examples, subsection plan. |
| **B5** | Chapter draft | System drafts chapter content. |
| **B6** | **Chapter approval gate** | Human reviews — approve, revise, rewrite, defer, split, merge. |
| **B7** | Assembly | Compile **approved** chapters; front matter, appendix, references as authorized. |
| **B8** | **Final approval gate** | Human reviews coherence, order, terminology, front matter, appendix, **export** choice. |
| **B9** | Export | Prepare MD, PDF, DOCX, TXT, or other **authorized** formats (Section 7–8). **Premium** export and publishing paths **SHALL** follow **Section 10.11**. |

### 10.8 Review state machine

The **BOOK** workflow **SHALL** expose **explicit review states** so progression is **not** opaque. States **SHALL** include at least the following **meanings** (exact identifiers **MAY** be product-specific):

| State | Meaning |
|-------|--------|
| `scope_pending` | Scope contract not complete. |
| `toc_pending_approval` | TOC proposal awaits human decision. |
| `chapter_plan_pending` | Chapter plan not approved for drafting. |
| `chapter_draft_pending_review` | Draft awaits human review. |
| `chapter_approved` | Chapter cleared for assembly sequence. |
| `assembly_pending_review` | Manuscript assembled; not yet final-approved. |
| `final_pending_approval` | Final gate before **export-ready**. |
| `export_ready` | Human-approved; export **MAY** proceed per policy. |

### 10.9 Structural threshold and voice segmentation

A **BOOK**-class output **SHALL** include:

- title
- structured section hierarchy
- table of contents
- bounded chapter organization
- **navigable voice segmentation** consistent with **VC5** (long-form voice delivery **SHALL** be traversable; **BOOK** without segment navigation is **not** sufficient)

A long answer without those elements **SHALL NOT** be classified as a **BOOK**.

### 10.10 Shell controls for BOOK workflow

The shell **SHALL** expose governed controls for **BOOK** workflows (voice, touch, or equivalent), **not** only hidden prompts. Illustrative mappings include:

- Approve TOC / Edit TOC
- Draft chapter *n* / Revise this chapter / Approve chapter
- Go to next chapter
- Assemble manuscript / Review final draft
- Export as PDF / Export as DOCX / Export as MD

These **SHALL** bind to the **BOOK** review state machine and **SHALL NOT** be replaced by unconstrained natural-language shortcuts that **skip** gates.

### 10.11 Base and premium BOOK workflows (product gates)

**Value-added** capabilities for **BOOK**-class or comparable **premium artifact** workflows—**image** generation or insertion, **layout** enhancement, **publishing**/**distribution**, and **advanced** export packages—**SHALL** be **product-gated** capabilities, **not** merely optional UX. They **SHALL** sit in a **monetized or entitlement-controlled** layer where **commercial** terms apply (**MPOA** and product policy), because they increase **cost**, **complexity**, **commercial value**, and often **platform liability**.

#### 10.11.1 Base vs premium split

| Tier | Scope (normative intent) |
|------|-------------------------|
| **Base BOOK workflow** | **Authoring** in the **standard governed** flow: scope, **TOC**, chapter planning, chapter drafting, chapter review, assembly, **basic** exports (**TXT**, **MD**, **DOCX**, **simple** **PDF** for personal or internal review — Section 7.3). |
| **Premium BOOK workflow** | **Enhancement** and **publishing**: generated or inserted **images**, chapter **illustrations**, **cover** generation, **visual** layouts, **advanced** styling, **publishing** pipeline, **publish-ready** packaging, **distribution** or **public** channels, storefront or **branded** outputs. |

The **core drafting/review flow** **MAY** exist in the **standard** governed workflow; **enhancement** and **publishing** **SHALL** be **entitlement-gated**.

#### 10.11.2 Feature classes

| Class | Examples | Gate |
|-------|----------|------|
| **Authoring** | **TOC** approval, chapter review, manuscript assembly | **Standard** (governed workflow; not optional UX alone) |
| **Enhancement** | Add/generated **images**, **covers**, richer **layout**, **visual** styling, **image-enhanced** or **designed** PDF | **Premium** (or equivalent **commercial entitlement**) |
| **Publishing** | **Publish**, **distribute**, **public** share links, **marketplace**/store output, **branded** packaging | **Premium** (or equivalent **commercial entitlement**) |

**Enhancement** and **Publishing** **SHALL** be **gated**; **Authoring** **SHALL** remain **available** without requiring **Enhancement** or **Publishing** entitlements.

#### 10.11.3 Normative doctrine

**Image** insertion, **illustration** generation, **cover** generation, and **publishing**/**distribution** actions for **BOOK**-class artifacts **SHALL** be treated as **gated product capabilities** and **MAY** require **paid membership** or **equivalent commercial entitlement**. The **base authoring** workflow **MAY** remain **available** without those **enhancement** or **publishing** capabilities.

The system **SHALL NOT** **automatically** add **images** to, or **publish**, a **BOOK**-class artifact unless the **actor** is **entitled** for those capabilities **and** **explicitly** invokes the related **shell** controls (or equivalent governed **workflow** steps).

#### 10.11.4 Entitlement buckets (illustrative)

Implementations **SHALL** map shell actions to **entitlements**. Illustrative **Standard** vs **Premium** buckets:

| **Standard** | **Premium** |
|--------------|-------------|
| Draft, review, **approve TOC**, **approve chapters**, assemble manuscript | Add or **generate** images; **cover** art |
| Export **TXT**, **MD**, **DOCX**, **simple** **PDF** (personal/review) | **Advanced** **PDF** (print-ready, designed, image-enhanced); **cover** package |
| — | **Publish**, **distribute**, **public-ready** artifacts, **distribution** workflows |

Exact **SKU** or **tier** names are **product** decisions; the **doctrinal** requirement is **gating** **Enhancement** and **Publishing** separately from **base** **Authoring**.

#### 10.11.5 PDF: review vs publish-ready

**Simple** or **review** **PDF** (**Standard**) **SHALL** be distinguished from **publish-ready**, **print-ready**, or **image-enhanced** **PDF** (**Premium**), which **SHALL** follow **Section 10.11**. **Exporting** a **PDF** for **personal** or **internal review** is **not** the same as **publishing** or producing a **polished commercial** artifact.

#### 10.11.6 Shell controls (gated)

**Premium** actions **SHALL** appear as **shell** affordances (voice, touch, or equivalent), **SHALL** be **gated**, and **SHALL NOT** execute without **entitlement** and **explicit** invocation. The shell **MAY** show them **locked** with **upgrade** or **entitlement** language, or **hide** them when the actor is **not** entitled—**product** choice, provided **gating** is **consistent** with this section.

Illustrative **Premium** shell actions include:

- Add images / Generate illustrations
- Generate cover
- Publish book / Create public version
- Export **print-ready** or **publish-ready** PDF / **distribution** to public channels

## 11. Non-goals

This addendum does not define:

- **base shell navigation primitives** (**START_HERE**, **CONTINUE**, **CHOOSE**, etc.) — see **[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**
- **composition artifact classes** (messages, invites, documents, publications) — see **[ADD-003](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)**
- visual styling tokens
- export transport mechanisms
- storage rules
- version-control policy

---

*End of AMD-2026-008-ADD-002, version 0.13.0 (draft).*


---

## Cross-reference bundle: `AMD-2026-008-ADD-003-ANNEX-A`

**[Bundled cross-reference — use this file’s version]** **`AMD-2026-008-ADD-003-ANNEX-A`** — **version** **`1.0.0`**

---

---
document_id: AMD-2026-008-ADD-003-ANNEX-A
parent_amendment: AMD-2026-008
parent_addendum: AMD-2026-008-ADD-003
version: 1.0.0
status: draft
category: amendment_addendum_annex
title: ADD-003 Annex A — Informative composition and knowledge-basis examples
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008-ADD-003
    title: Composition Control Plane for Messages, Invites, and Documents
  - doc_id: AMD-2026-008-ADD-002
    title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
note: Informative JSON only; not normative. Depth/packaging labels refer to ADD-002 definitions.
---

# AMD-2026-008-ADD-003 Annex A — Informative examples

**Binding** **SHALL**/**MUST** **language** **remains** **in** **[AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)**. **Field** **names** **below** **are** **illustrative** **serialization** **hints** **for** **products**.

**Depth** and **packaging** **strings** **in** **examples** **refer** **to** **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§4** **and** **§7** **(not** **redefined** **here**)**.

---

## 1. Composition contract JSON (informative)

Moved from **ADD-003** **§5.7**.

```json
{
  "artifact_class": "ARTICLE",
  "role": "Founder",
  "intent": "Educate and persuade",
  "outcome": "Reader understands the AI OS position and joins early access",
  "audience": "operators and technical founders",
  "depth": "EXPLANATION",
  "packaging": "MD"
}
```

```json
{
  "artifact_class": "EMAIL",
  "role": "Executive Assistant",
  "intent": "Coordinate meeting scheduling",
  "outcome": "Recipient accepts one of the proposed meeting times",
  "audience": "external partner",
  "depth": "BRIEF",
  "action_mode": "DRAFT_ONLY"
}
```

---

## 2. Knowledge-basis / discovery JSON (informative)

Moved from **ADD-003** **§18.9**.

```json
{
  "artifact_class": "RESEARCH_REPORT",
  "knowledge_basis_required": true,
  "knowledge_sources": [
    "uploaded_files",
    "governing_docs",
    "current_web_sources"
  ],
  "knowledge_state": "partial",
  "discovery_required": true,
  "creation_mode": "scaffold_only"
}
```

---

*End of Annex A, version 1.0.0 (draft).*


---

## Cross-reference bundle: `ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD`

**[Bundled cross-reference — use this file’s version]** **`ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD`** — **version** **`0.3.2`** — **registry_id** **`AIOS-OPS-020`**

---

---

document_id: ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD

registry_id: AIOS-OPS-020

version: 0.3.2

status: draft

category: operations

title: Originality and Source-Boundary Verification (Implementation Home)

author: Gateway Global AIOS

created: 2026-04-08

last_updated: 2026-04-10

reviewers: []

cross_references:

  - doc_id: AMD-2026-008-ADD-003

    title: Composition Control Plane for Messages, Invites, and Documents

    note: Normative doctrine — §19 originality/source-boundary gate; §19.4 option (b); §19.10 implementation handoff.

amendment_history:

  - version: 0.3.2

    date: 2026-04-10

    summary: "§13 — ADD-003 §5.9 fail-closed rows → DCP transport codes (aios.dcp.composition + originality §10 cross-ref)."

  - version: 0.3.1

    date: 2026-04-10

    summary: "§11 — explicit pointer to ADD-003 §19.10 minimum conformance surface mapped to this document’s §§6–10 and Appendix A."

  - version: 0.3.0

    date: 2026-04-10

    summary: "Numeric severity bands (default policy pack), metric names 0.0–1.0, mapping table severity×channel→state; JSON Schema (draft 2020-12) for evaluation record (Appendix A); metric_snapshot optional on record."

  - version: 0.2.0

    date: 2026-04-08

    summary: "Channel classes, signal taxonomy, enforcement states, procedural mapping posture, release-time triggers, minimal evaluation record fields, DCP code names. Numeric scoring algorithms and full JSON Schema file still deferred to v0.3+."

  - version: 0.1.0

    date: 2026-04-08

    summary: "Placeholder registered home for release-time evaluation methods, overlap/similarity scoring, threshold tables, and DCP/transport bindings per ADD-003 §19.4/§19.10. Substance to be filled as product policy matures."

---



# Originality and Source-Boundary Verification (Implementation Home)



## 1. Purpose



**[AMD-2026-008-ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** **§19** defines **required** **verification** **states**, **channel** **posture**, **enforcement** **outcomes**, and **fail-closed** **rules**. **§19.4** allows **policy** to **either** define thresholds **in** **policy** **or** **reference** **this** **artifact** **for** **evaluation** **methods** **(option** **b)**. **§19.10** requires **implementation** **logic**, **scoring**, **schemas**, **and** **transport** **bindings** **to** **have** **a** **traceable** **home**.



This **operations** **standard** **(registry** **AIOS-OPS-020)** **is** **the** **default** **named** **home** **until** **superseded** **by** **a** **policy-registered** **successor**.



## 2. Scope



### In scope (v0.3.0)



- **§§3–5** **—** **channel** **classes**, **signal** **taxonomy**, **canonical** **enforcement** **states**

- **§6** **—** **normative** **metric** **names**, **severity** **bands**, **default** **threshold** **policy** **pack** **(numeric)**

- **§7** **—** **mapping** **severity** **×** **channel** **→** **enforcement** **state**

- **§8** **—** **release-time** **evaluation** **triggers**

- **§9** **—** **evaluation** **record** **field** **contract** **+** **Appendix** **A** **JSON** **Schema**

- **§10** **—** **DCP** **/** **transport** **codes**

- **§13** **—** **ADD-003** **§5.9** **fail-closed** **→** **DCP** **composition** **codes** **(binding** **table**)**



### Deferred to v0.4.0+



- **Concrete** **implementations** **of** **metric** **computers** **(which** **n-grams**, **which** **structural** **distance** **function)** **—** **products** **SHALL** **document** **algorithm** **IDs** **per** **`policy_pack_id`**

- **Full** **DCP** **protobuf**/**OpenAPI** **artifacts** **(if** **distinct** **from** **JSON** **payloads)**



## 3. Channel classes (normative)



| Code | Meaning |

|------|---------|

| `INTERNAL` | **Draft** **or** **collaboration** **surface** **only** **;** **no** **external** **delivery** **on** **this** **path** **(until** **promoted)**. |

| `EXTERNAL` | **Publish**, **send**, **or** **formal** **export** **to** **an** **external** **recipient**, **feed**, **or** **shared** **surface** **per** **ADD-003** **§19.2**. |



**Policy** **MAY** **subdivide** **but** **SHALL** **map** **subdivisions** **to** **these** **two** **base** **classes** **for** **originality** **evaluation**.



**SHALL** **not** **treat** **EXTERNAL** **with** **the** **same** **leniency** **as** **INTERNAL** **unless** **policy** **explicitly** **documents** **equivalent** **risk** **(per** **ADD-003** **§19.4)**.



## 4. Signal classes (from ADD-003 §19.3)



| Code | Primary metric(s) (§6) |

|------|-------------------------|

| `SIG_VERBATIM` | `verbatim_ngram_overlap` |

| `SIG_STRUCTURE` | `structural_similarity_score` |

| `SIG_KB_EXTRACT` | `kb_extraction_score` |

| `SIG_QUOTE` | **Policy** **—** **bounded** **quote** **detection** **;** **may** **reuse** **`verbatim_ngram_overlap`** **on** **non-quoted** **spans** |

| `SIG_PUBLISH_EXT` | **Derived** **from** **channel** **+** **other** **metrics** **(no** **separate** **0–1** **score** **required)** |



## 5. Enforcement states (canonical)



**Aligned** **to** **ADD-003** **§19.5**.



| Canonical `originality_verification_state` | Aliases (informative) |

|-------------------------------------------|------------------------|

| `originality_clear` | `clear` |

| `quote_limited` | `quote_ok` |

| `overlap_review_required` | `review_required` |

| `high_reproduction_risk_blocked` | `blocked` |

| `internal_only` | `internal_only_pending_release` |



## 6. Metrics, severity, and default threshold bands



### 6.1 Normative metrics (real numbers in [0.0, 1.0])



| Metric key | Meaning |

|------------|---------|

| `verbatim_ngram_overlap` | **Maximum** **or** **aggregate** **overlap** **of** **n-gram** **runs** **between** **output** **and** **single** **source** **(product** **defines** **n**, **window)** **—** **scaled** **to** **0–1**. |

| `structural_similarity_score` | **Structural** **similarity** **(outline**/**heading**/**sequence)** **vs** **dominant** **source**, **0–1**. |

| `kb_extraction_score` | **Extraction-style** **dump** **risk** **from** **KB**/**notes**, **0–1**. |



**Implementations** **SHALL** **persist** **the** **metric** **values** **used** **for** **the** **decision** **in** **`metric_snapshot`** **(§9** **/** **Appendix** **A)** **when** **claiming** **conformance** **to** **this** **standard**.



### 6.2 Severity per signal



For **each** **of** **`SIG_VERBATIM`**, **`SIG_STRUCTURE`**, **`SIG_KB_EXTRACT`**, **map** **the** **primary** **metric** **to** **severity**:



| Severity | Meaning |

|----------|---------|

| `NONE` | **Below** **ELEVATED** **floor** **for** **that** **metric** **and** **channel** **column**. |

| `ELEVATED` | **Between** **ELEVATED** **floor** **and** **HIGH** **floor**. |

| `HIGH` | **At** **or** **above** **HIGH** **floor**. |



### 6.3 Default policy pack `AIOS-OPS-020-DEFAULT-v1` (normative defaults)



**Policy** **MAY** **override** **these** **cutoffs** **;** **override** **SHALL** **register** **a** **new** **`policy_pack_id`**. **All** **thresholds** **are** **inclusive** **on** **the** **upper** **bound** **for** **ELEVATED** **and** **exclusive** **above** **HIGH** **where** **noted**.



**`verbatim_ngram_overlap`** **(SIG_VERBATIM)**



| Channel | ELEVATED floor (≥) | HIGH floor (≥) |

|---------|-------------------|----------------|

| `INTERNAL` | 0.08 | 0.28 |

| `EXTERNAL` | 0.04 | 0.18 |



**`structural_similarity_score`** **(SIG_STRUCTURE)**



| Channel | ELEVATED floor (≥) | HIGH floor (≥) |

|---------|-------------------|----------------|

| `INTERNAL` | 0.12 | 0.38 |

| `EXTERNAL` | 0.08 | 0.28 |



**`kb_extraction_score`** **(SIG_KB_EXTRACT)**



| Channel | ELEVATED floor (≥) | HIGH floor (≥) |

|---------|-------------------|----------------|

| `INTERNAL` | 0.10 | 0.35 |

| `EXTERNAL` | 0.06 | 0.25 |



**Interpretation:** **LOWER** **floors** **on** **`EXTERNAL`** **enforce** **stricter** **gates** **for** **the** **same** **raw** **metric** **values** **(per** **ADD-003** **§19.4)**.



## 7. Mapping: severity × channel → enforcement state



**Apply** **after** **computing** **severity** **for** **each** **applicable** **signal** **(§6.2)**. **Use** **the** **worst** **(highest** **risk)** **severity** **across** **signals** **for** **the** **current** **evaluation**.



| Worst severity | `INTERNAL` | `EXTERNAL` |

|----------------|------------|------------|

| `NONE` | `originality_clear` **or** `quote_limited` **if** **only** **bounded** **quotation** **detected** | `originality_clear` **or** `quote_limited` |

| `ELEVATED` | `overlap_review_required` **unless** **policy** **allows** **clear** **for** **draft-only** **;** **default** **`overlap_review_required`** | `overlap_review_required` **(minimum)** |

| `HIGH` | **`internal_only`** **or** **`high_reproduction_risk_blocked`** **per** **product** **policy** **;** **default** **`internal_only`** **if** **artifact** **must** **not** **leave** **internal** **collaboration** | **`high_reproduction_risk_blocked`** **or** **`internal_only`** **;** **default** **`high_reproduction_risk_blocked`** **when** **external** **release** **is** **the** **trigger** |



**Promotion** **from** **`INTERNAL`** **to** **`EXTERNAL`** **SHALL** **re-run** **§8** **evaluation** **with** **`channel_class`** **=`EXTERNAL`** **;** **SHALL** **not** **reuse** **`INTERNAL`** **severity** **classification** **alone** **to** **authorize** **external** **release**.



## 8. Release-time evaluation triggers



**Originality**/**source-boundary** **evaluation** **SHALL** **run** **before** **completing** **any** **of** **the** **following** **when** **ADD-003** **§19.2** **applies** **to** **the** **artifact** **class**:



1. **Publish**

2. **Send**

3. **Formal** **export**

4. **Shared** **external** **surface** **(policy-defined)**



**Evaluation** **SHALL** **not** **be** **skipped** **on** **silent** **defaults** **;** **missing** **evaluation** **when** **required** **SHALL** **fail** **closed** **per** **ADD-003** **§5.9**.



## 9. Evaluation record (field contract)



**Control-plane** **and** **audit** **logs** **SHALL** **conform** **to** **Appendix** **A** **JSON** **Schema** **`OriginalityEvaluationRecordV1`** **for** **the** **payload** **shape** **(JSON** **encoding)**.



| Field | Required | Description |

|-------|:--------:|-------------|

| `originality_verification_state` | **Yes** | Canonical **value** **from** **§5** |

| `channel_class` | **Yes** | `INTERNAL` **\|** `EXTERNAL` |

| `evaluation_trigger` | **Yes** | **`publish`** **\|** **`send`** **\|** **`formal_export`** **\|** **`shared_surface`** |

| `signal_flags` | **No** | **Array** **of** **§4** **codes** |

| `policy_pack_id` | **No** | **Default** **`AIOS-OPS-020-DEFAULT-v1`** **when** **omitted** **for** **threshold** **lookup** |

| `evaluated_at` | **Yes** | **UTC** **ISO** **8601** |

| `artifact_id` | **No** | **Stable** **artifact** **id** |

| `metric_snapshot` | **No** | **Object** **with** **§6.1** **keys** **and** **numeric** **values** **used** **for** **the** **decision** |

| `dcp_outcome_code` | **No** | **§10** **outcome** **code** **redundant** **with** **state** **but** **required** **for** **DCP** **transport** **when** **using** **DCP** **envelope** |



## 10. DCP / transport binding names



**Namespace:** **`aios.dcp.originality`**



**Outcome** **codes** **(map** **to** **§5)**



| Code | Canonical state |

|------|-----------------|

| `ORIG_CLEAR` | `originality_clear` |

| `ORIG_QUOTE_LIMITED` | `quote_limited` |

| `ORIG_REVIEW_REQUIRED` | `overlap_review_required` |

| `ORIG_BLOCKED` | `high_reproduction_risk_blocked` |

| `ORIG_INTERNAL_ONLY` | `internal_only` |



**Fail-closed** **rejection** **reasons**



| Code | When |

|------|------|

| `ORIG_REJECT_MISSING_EVAL` | **Required** **gate** **not** **run** **or** **no** **state** **recorded** |

| `ORIG_REJECT_CHANNEL_MISMATCH` | **EXTERNAL** **release** **with** **INTERNAL-only** **clearance** |

| `ORIG_REJECT_POLICY_STALE` | **Policy** **pack** **missing** **or** **invalid** |



## 11. Normative anchor



**Doctrine** **remains** **in** **ADD-003** **§19** **and** **§5.9**. **This** **artifact** **binds** **metrics**, **thresholds**, **evaluation** **records**, **DCP** **codes** **(§§10**, **§13)**, **and** **ADD-003** **§5.9**/**§19** **transport** **mappings**. **Products** **claiming** **§19** **conformance** **via** **this** **standard** **SHALL** **meet** **the** **minimum** **surface** **enumerated** **in** **ADD-003** **§19.10** **(mapped** **to** **§§6**–**10** **and** **Appendix** **A** **here**)** **;** **products** **emitting** **DCP** **for** **§5.9** **composition** **fail-closed** **rows** **SHALL** **use** **§13** **codes** **unless** **policy** **extends** **the** **namespace** **.**



## 12. Revision path



**v0.4.0** **—** **algorithm** **IDs** **and** **optional** **separate** **machine-readable** **schema** **URL** **for** **DCP** **protobuf** **definitions**.



## 13. ADD-003 §5.9 fail-closed → DCP transport codes (composition plane)



**Normative** **binding** **for** **[ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** **§5.9** **fail-closed** **table** **:** **implementations** **SHALL** **emit** **the** **codes** **below** **on** **control-plane** **/** **DCP** **envelopes** **when** **signaling** **those** **failure** **modes** **(unless** **policy** **registers** **a** **compatible** **extension** **namespace** **)** **.** **Originality-only** **failures** **reuse** **§10** **where** **noted** **.**



**Namespace** **`aios.dcp.composition`** **(non-originality** **gates** **)** **:**



| ADD-003 §5.9 condition (summary) | DCP code | Typical enforcement surface |

|--------------------------------|----------|------------------------------|

| **Mandatory** **composition** **contract** **fields** **missing** **or** **invalid** **where** **§5** **requires** **them** | `COMP_CONTRACT_INCOMPLETE` | **No** **substantive** **draft** **except** **explicit** **§5.4** **scaffold**/**outline** **path** **;** **no** **silent** **promotion** **to** **send-ready** **.** |

| **Professional-use** **disclosure** **metadata** **or** **§9.4** **surface** **missing** **where** **§9.4** **applies** | `COMP_PROF_DISCLOSURE_MISSING` | **Block** **send**/**publish**/**export** **as** **professional-use** **draft** **until** **remediated** **or** **policy** **exception** **;** **§9.4.3(5)** **export** **rules** **.** |

| **Knowledge** **basis** **insufficiency** **where** **§18** **requires** **grounding** **or** **discovery** | `COMP_KNOWLEDGE_INSUFFICIENT` | **Scaffold-only**, **blocked**, **or** **discovery-required** **per** **§18.5**/**§18.6** **;** **no** **silent** **external** **release** **.** |



**Namespace** **`aios.dcp.originality`** **(§10)** **—** **originality**/**source-boundary** **row** **of** **§5.9** **:**



| ADD-003 §5.9 condition (summary) | DCP code | Typical enforcement surface |

|--------------------------------|----------|------------------------------|

| **Originality**/**source-boundary** **verification** **outcome** **missing**, **unknown**, **or** **not** **permitted** **for** **the** **target** **channel** **where** **§19.2** **requires** **a** **gate** | `ORIG_REJECT_MISSING_EVAL` **(**§10**)** | **No** **publish**/**send**/**formal** **export** **until** **§19** **evaluation** **record** **and** **§19.5** **permit** **;** **may** **pair** **with** **`ORIG_*`** **outcome** **codes** **once** **eval** **exists** **.** |



**Note** **:** **`COMP_*`** **codes** **describe** **composition-plane** **and** **gating** **failures** **outside** **the** **numeric** **metric** **pipeline** **;** **they** **SHALL** **not** **replace** **`OriginalityEvaluationRecordV1`** **when** **§19** **evaluation** **runs** **.**



---



## Appendix A — JSON Schema (OriginalityEvaluationRecordV1)



**Draft** **2020-12**. **URI** **`https://aios.governance/schemas/originality-evaluation-record-v1.json`** **(informative** **—** **register** **in** **product** **catalog** **when** **stable)**.



```json

{

  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "$id": "https://aios.governance/schemas/originality-evaluation-record-v1.json",

  "title": "OriginalityEvaluationRecordV1",

  "type": "object",

  "additionalProperties": false,

  "required": [

    "originality_verification_state",

    "channel_class",

    "evaluation_trigger",

    "evaluated_at"

  ],

  "properties": {

    "originality_verification_state": {

      "type": "string",

      "enum": [

        "originality_clear",

        "quote_limited",

        "overlap_review_required",

        "high_reproduction_risk_blocked",

        "internal_only"

      ]

    },

    "channel_class": {

      "type": "string",

      "enum": ["INTERNAL", "EXTERNAL"]

    },

    "evaluation_trigger": {

      "type": "string",

      "enum": ["publish", "send", "formal_export", "shared_surface"]

    },

    "signal_flags": {

      "type": "array",

      "items": {

        "type": "string",

        "enum": [

          "SIG_VERBATIM",

          "SIG_STRUCTURE",

          "SIG_KB_EXTRACT",

          "SIG_QUOTE",

          "SIG_PUBLISH_EXT"

        ]

      }

    },

    "policy_pack_id": {

      "type": "string",

      "description": "Omit to use AIOS-OPS-020-DEFAULT-v1 thresholds."

    },

    "evaluated_at": {

      "type": "string",

      "format": "date-time"

    },

    "artifact_id": { "type": "string" },

    "metric_snapshot": {

      "type": "object",

      "additionalProperties": false,

      "properties": {

        "verbatim_ngram_overlap": { "type": "number", "minimum": 0, "maximum": 1 },

        "structural_similarity_score": { "type": "number", "minimum": 0, "maximum": 1 },

        "kb_extraction_score": { "type": "number", "minimum": 0, "maximum": 1 }

      }

    },

    "dcp_outcome_code": {

      "type": "string",

      "enum": [

        "ORIG_CLEAR",

        "ORIG_QUOTE_LIMITED",

        "ORIG_REVIEW_REQUIRED",

        "ORIG_BLOCKED",

        "ORIG_INTERNAL_ONLY"

      ]

    }

  }

}

```



