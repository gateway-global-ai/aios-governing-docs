---
document_id: AMD-2026-008-ADD-003
parent_amendment: AMD-2026-008
parent_version: 1.0.0
version: 1.0.0
status: ratified
category: amendment_addendum
title: Composition Control Plane for Messages, Invites, and Documents
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
ratification_date: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008-ADD-003-RATIFICATION-MOTION
    title: Ratification motion — AMD-2026-008-ADD-003
    relationship: ratification_motion
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
  - version: 1.0.0
    date: 2026-04-10
    summary: Ratified per AMD-2026-008-ADD-003-RATIFICATION-MOTION v1.0.0; substantive basis draft v0.14.7; Round 2 triangulation + AMD-2026-005 gate PASS (reviews 004/005/006).
  - version: 0.14.7
    date: 2026-04-10
    summary: Round 2 editorial — §20.2/§20.8/§18.11 SHALL for reference disposition; §0/§1 stable doc titles; §5.9 default Class 3 posture; §9.4.0/§9.4.6/§10/§14 gates; OPS-020 and MPOA cited by registry id + title; reduce path-only cross-refs.
  - version: 0.14.6
    date: 2026-04-10
    summary: Phase E — §2.1 DCP transport seam (namespace aios.dcp.composition; minimum envelope AIOS-OPS-020 §14 / Appendix B CompositionPlaneDcpV1); addresses Round 1 developer-synchrony gap without embedding full schemas in the addendum.
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
| **Status** | **`ratified` `1.0.0`** — addendum to **[AMD-2026-008](AMD-2026-008.md)** **1.0.0** (**[ratification motion](AMD-2026-008-ADD-003-ratification-motion.md)**) |
| **Does not replace** | *Base Shell Navigation Primitives and Start-Here Control* (**[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**) (navigation), *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (**[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)**) (output depth, shell voice controls, **packaging classes**, **BOOK** workflow, **premium** gates). This addendum defines **what** is being composed, **composition contracts** (**role**/**intent**/**outcome**), and **which actions** may execute—**not** interchangeable freeform text. |
| **Informative grounding** (**not** **law** **here**) | *Composition control plane — R&D and knowledge capture (AMD-2026-008 addendum track)* (**AIOS-COMPOSITION-CONTROL-RD-NOTES-001**); *Composition control plane — architecture memo (bounded domains and addendum seams)* (**AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001**); *Shell and composition — surface grammar and user-state memo (AMD-2026-008 addendum track)* (**AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001**) — informative only; no additional **SHALL**/**MUST** obligations. |

---

## 1. Purpose

This addendum defines the **composition control plane** for governed **artifact creation** on AI OS surfaces: **messages**, **calendar invites**, **documents** (including **subclasses**), and **publication**/**distribution** artifacts. It specifies **responsive** vs **procedural** vs **composed** output classes and the **composition contract** (**role**, **intent**, **outcome**) for **non-trivial** composition (**Section 5**).

It **SHALL** also govern **professional-use draft disclosure** for **licensed-professional** document classes (**§9.4**); **language**, **localization**, and **authoritative** multilingual version rules (**§16**); **measurement contracts** for **quantified** claims (**§17**); **knowledge basis** and **discovery** **gating** before **substantive** creation (**§18**); **originality**, **source-boundary**, and **non-reproduction** verification for **source-derived** composed artifacts (**§19**); and **reference-guided** composition—**example**, **template**, or **authority** materials used to shape **spirit**, **structure**, and **form** without authorizing **wholesale** **reproduction** (**§20**; **reference** **adherence**/**conformity** **controls** **§20.11**–**§20.15**, **not** **model** **temperature**).

It **SHALL** be read with *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (**[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)**) for **depth**, **voice controls**, **packaging**, and **BOOK**-specific gates (Sections 4, 5, 7, and 10 of that addendum). The documents listed in Section 0 as informative grounding remain non-normative context only.

## 2. Governing principle

**Artifact generation** **SHALL** follow **composition** **class**, **structure**, and **action** **semantics**—**not** **generic** **length**-scaled **text**. The runtime **SHALL** **keep** **message**, **invite**, **document**, and **publication** **artifacts** **distinct**.

**Composition** **class** **SHALL** **not** **be** **inferred** **from** **packaging** **alone**. **Output** **depth** (**[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§4**) **remains** **orthogonal** **to** **composition** **class** **(this** **addendum** **owns** **class** **labels**).**

For **action-bearing** **artifacts**, **composition** **SHALL** **stay** **separate** **from** **execution** (**draft**/**review**/**approve** **vs** **send**/**publish**).**

### 2.1 Addendum seams (normative for authors)

The seam rules in this Section 2.1 are binding on document authors and controlling for interpretation where this addendum overlaps with ADD-001, ADD-002, or **AIOS-OPS-020**.

- **Output depth** (**RESPONSE** … **BOOK**), **shell** **voice** **controls** (**VC0**–**VC5**), and **packaging** **classes** **SHALL** **be** **used** **as** **defined** **in** **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§4**, **§5**, **§7**; **this** **addendum** **SHALL** **not** **redefine** **those** **labels** **or** **ladder** **semantics**.
- **Navigation** **primitives** **SHALL** **follow** **[ADD-001](AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**; **this** **addendum** **SHALL** **not** **redefine** **them**.
- **Composition** **classes**, **composition** **contracts**, **and** **action** **semantics** **for** **artifacts** **SHALL** **be** **owned** **here** (**or** **policy** **downstream**); **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **SHALL** **not** **define** **composition** **class** **taxonomies** (**see** *Composition control plane — architecture memo (bounded domains and addendum seams)* (**AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001**) bounded domains table).
- **DCP** **transport** **for** **§5.9** **fail-closed** **composition** **conditions** **SHALL** **emit** **codes** **in** **namespace** **`aios.dcp.composition`** **(**and** **originality**/**release** **codes** **per** **AIOS-OPS-020** (*Originality and Source-Boundary Verification (Implementation Home)*) **§10**/**§13** **where** **applicable**)** **;** **the** **minimum** **DCP** **envelope** **SHALL** **conform** **to** **AIOS-OPS-020** **§14**, **with** **machine** **shape** **in** **Appendix** **B** **(**`CompositionPlaneDcpV1`** **)** **.**

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

**Unless** **policy** **expressly** **defines** **a** **narrower** **or** **stricter** **rule**, **missing** **mandatory** **composition-contract** **fields** **for** **a** **Class** **3** **artifact** **SHALL** **force** **scaffold-only** **posture** **and** **SHALL** **block** **send**, **publish**, **and** **formal** **export** **.**

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

**Exact** **error** **codes**, **serialized** **schemas**, **and** **DCP** **transport** **SHALL** **bind** **in** **implementation** **artifacts** **as** **policy** **defines** **(§19.10** **;** **default** **home** **AIOS-OPS-020)** **.** **Default** **DCP** **code** **names** **for** **the** **fail-closed** **rows** **above** **—** **AIOS-OPS-020** **§13** **(**`aios.dcp.composition`** **and** **§10** **originality** **cross-reference**)** **unless** **policy** **registers** **extensions** **.**

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

When **signals** **conflict** or **remain** **ambiguous** after **policy-defined** **classification** **steps**, the runtime **SHALL** **apply** **§9.4** **draft** **posture** **and** **disclosure** **rather** **than** **assuming** **non-professional** use — **unless** **policy** **records** **a** **narrower** **rule** **with** **audit** **visibility**.

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

**Commercial**, **liability**, and **tenant** terms **SHALL** remain subject to **MPOA** (*Gateway Global AIOS Master Platform Operating Agreement*) and **product** agreements; **§9.4** states **minimum** **governance** and **disclosure** expectations for the **composition plane**.

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

**Governance** **clearance** **to** **publish** **or** **distribute** **under** **this** **addendum** **does** **not** **by** **itself** **grant** **commercial** **entitlement** **to** **enhancement**, **publishing**, **or** **distribution** **capabilities**; **those** **remain** **separately** **governed** **by** *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (**ADD-002** Section 10.11) **and** **applicable** **MPOA** **terms**.

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

- **Governance** **review** **gates:** **Policy** **may** **require** **review** **or** **approval** **before** **send**, **issue**, **publish**, **or** **formal** **export**.
- **Workflow** **gates:** **RESEARCH_REPORT**, **BOOK**, **and** **public** **REPORT** **artifacts** **SHALL** **follow** **any** **mandatory** **review** **workflow** **defined** **in** **this** **addendum** **and** **in** *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (**ADD-002** Sections 10 and 10.11).
- **Commercial** **gates:** **Image** **insertion**, **designed** **PDF**, **publishing** **pipeline**, **and** **public** **distribution** **may** **require** **separate** **entitlement** **or** **paid** **access** **under** **ADD-002** Section 10.11 **and** **applicable** **MPOA** **terms** **(see** **§10** **)** **.**
- **EMAIL** **and** **CALENDAR_INVITE:** **Policy** **MAY** **require** **approval** **before** **send**/**issue**; **controls** **SHALL** **be** **enforceable** **via** **shell** **and** **audit** **surfaces** **.**

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

The obligations in **§17** define **procedural** requirements for **quantified** claims and **measurements**. They **do** **not** **warrant** or **guarantee** the **factual** **accuracy** of any **number**, **measurement**, or **derived** **value** produced by the system. **Commercial** terms, **remedies**, and **liability** for **reliance** on **generated** content **SHALL** be governed **exclusively** by **MPOA** (*Gateway Global AIOS Master Platform Operating Agreement*) and applicable **product** agreements — **not** by **§17** alone.

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
4. **Reference disposition** — **§20** when **reference_documents** or **reference_role** applies (**SHALL** resolve **structure**/**tone**/**style**/**authority** posture **before** **substantive** drafting).  
5. **Creation mode** — **§18.6** (and **§17**, **§16**, **§9.4** as applicable).

**B — Before external publish, send, or formal export (when applicable)**

6. **Originality / source-boundary** — **§19** when **policy** or **artifact** **class** **requires** **verification** **before** **publish**/**send**/**export**; **§19** **SHALL** **not** **substitute** **for** **§18** **grounding** **where** **§18** **applies** **(ground** **first**)**.

**Parallel** **obligations** **(same** **artifact** **may** **trigger** **several**)**:** **professional** **disclosure** (**§9.4**); **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **BOOK**/**TOC**/**chapter**/**premium** **gates** **where** **BOOK**/**export** **path** **applies**.

**Thresholds**, **metric** **mapping**, **evaluation** **record** **shape**, **and** **DCP** **outcome** **codes** **for** **§19** **default** **to** **AIOS-OPS-020** (*Originality and Source-Boundary Verification (Implementation Home)*) **§6**–**§9** **unless** **policy** **registers** **a** **replacement** **artifact** **.**

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

**Default** **named** **artifact** **for** **option** **(b)** **:** **AIOS-OPS-020** (*Originality and Source-Boundary Verification (Implementation Home)*) **—** **until** **policy** **explicitly** **registers** **a** **different** **governed** **successor** **artifact**.

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

**Implementation-specific** **validation** **logic**, **overlap**/**similarity** **scoring**, **threshold** **tables**, **serialized** **contract** **schemas**, **and** **control-plane** **transport** **bindings** **SHALL** **live** **in** **governed** **specification** **or** **operations** **artifacts** **registered** **by** **policy**, **such** **that** **§19** **verification** **is** **auditable** **and** **not** **solely** **implementation-defined** **without** **a** **traceable** **home**. **The** **default** **registered** **home** **is** **AIOS-OPS-020** (*Originality and Source-Boundary Verification (Implementation Home)*) **unless** **policy** **names** **a** **replacement**. **Products** **SHALL** **document** **which** **artifact** **supplies** **release-time** **evaluation** **for** **each** **conformance** **claim** **tied** **to** **this** **addendum**.

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

Where a **reference** is **supplied**, the runtime **SHALL** determine whether it is used **primarily** for **structure**, **tone**, **style**, **formatting**, or **authoritative** **conformity** **before** **substantive** **drafting** **proceeds** (when **policy** or **workflow** **requires** **disposition**).

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

Before **substantive** **drafting**, the runtime **SHALL** resolve (or **surface** for **user** **confirmation**) where **references** **apply**:

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

**High** **reference** **adherence** **(including** **level** **10** **)** **SHALL** **not** **bypass** **§19** **verification** **or** **channel** **thresholds** **in** **AIOS-OPS-020** (*Originality and Source-Boundary Verification (Implementation Home)*) **when** **§19.2** **applies** **—** **structure** **fidelity** **does** **not** **imply** **originality_clear** **or** **release** **clearance** **.**

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

*End of AMD-2026-008-ADD-003, version 1.0.0 (ratified).*
