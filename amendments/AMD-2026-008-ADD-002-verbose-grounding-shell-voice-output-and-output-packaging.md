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
