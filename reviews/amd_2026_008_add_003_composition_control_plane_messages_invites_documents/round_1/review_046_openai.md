---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003
document_version: 0.14.5
reviewer: OpenAI
review_date: 2026-04-08
review_round: 1
review_type: editorial
disposition: approved_with_changes
composite_score: 3.8
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The addendum is largely well-aligned with AMD-2026-008, ADD-001, ADD-002, and AIOS-OPS-020, but several citations use file paths or section shorthand instead of the style guide’s preferred full title plus section format. |
| 2 | Business Model Alignment | 4 | The document consistently preserves MPOA and ADD-002 §10.11 supremacy for premium publishing, send/publish liability, and entitlement gating. |
| 3 | Legal Enforceability | 3 | Most obligations are framed with enforceable SHALL language, but several provisions still defer too much to unspecified policy, especially around subclass structures, approval levels, and applicability thresholds. |
| 4 | Architectural Fidelity | 4 | The document strongly preserves the seam between navigation, depth/voice, composition, grounding, and originality, with only minor ambiguity around where implementation-state joins occur between §18 and §19. |
| 5 | Completeness | 4 | The document covers the promised control-plane scope comprehensively, but some edge-case handling remains underdefined for hybrid artifacts, policy silence, and external export classes. |
| 6 | Conflict Freedom | 4 | No direct contradiction with the bundled governing set appears, though a few formulations create mild tension with the style guide’s cross-reference discipline and with ADD-002’s ownership language. |
| 7 | Practical Operability | 3 | The doctrine is operationally rich, but implementers still lack a few concrete decision rules for hybrid class selection, policy precedence, and when “formal export” differs from ordinary export. |
| 8 | Style & Clarity | 3 | The document is materially clearer than a typical sprawling draft, but bold-heavy formatting, dense sentence construction, and occasional duplicated concepts reduce readability and increase review friction. |
| 9 | Developer Synchrony | 4 | The addendum maps well to control-plane implementation concepts, explicit fields, states, and AIOS-OPS-020 handoff surfaces, making product translation plausible. |
| 10 | Platform Economics Synchrony | 4 | Economic and liability boundaries are generally kept in MPOA/ADD-002 rather than redefined here, which is the correct governance posture. |
| 11 | Friction Factor | 3 | The document is usable by expert reviewers, but its density, repeated seam language, and mixed normative/informative prose create avoidable cognitive load. |
| | **Composite Score** | **3.8** | |

---

## Overall Assessment

### Strengths

- **Section 2 and §2.1** do an excellent job preserving addendum seams and preventing ADD-003 from re-owning navigation, depth, voice, or packaging already governed by *AMD-2026-008-ADD-001 — Base Shell Navigation Primitives and Start-Here Control* and *AMD-2026-008-ADD-002 — Verbose Grounding, Shell Voice Output Control, and Output Packaging*.
- **Sections 5, 18, 19, and 20** form a coherent control stack: composition contract, knowledge sufficiency, originality/source-boundary verification, and reference-guided composition are clearly separated and cross-linked.
- **§9.4** is one of the strongest parts of the document: the trigger logic in **§9.4.0**, the doctrine in **§9.4.2**, and the export-preservation rule in **§9.4.3(5)** are materially enforceable and commercially coherent.
- **§19.10** and **§5.9** appropriately keep doctrine in the addendum while assigning metrics, schemas, and DCP bindings to *Originality and Source-Boundary Verification (Implementation Home)* (AIOS-OPS-020).
- **Section 6** usefully situates this addendum in the twelve-axis model already reflected in ADD-002 and the architecture memo.

### Critical Gaps

- **Cross-reference style is inconsistent** throughout the document: many references use markdown paths or shorthand like “ADD-002 §10.11” instead of the style guide’s preferred full title plus section citation.
- **The footer contains a version mismatch**: the body is version **0.14.5**, but the closing line says “version 0.14.2 (draft),” which is a material editorial defect for a governed document.
- **Several key enforcement points remain too policy-dependent** without minimum fallback rules, especially in **§9.3**, **§15**, and parts of **§18–§20**.
- **The distinction between “export” and “formal export” is not consistently defined**, even though that distinction drives gating in **§5.9**, **§18.11**, and **§19.2**.
- **The document remains harder to read than necessary** because many sentences stack multiple bolded concepts and parenthetical clauses, especially in **§1**, **§2**, **§16.7**, **§18**, and **§19.10**.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:**  
This section is structurally sound and correctly frames the document as an addendum to *AMD-2026-008 — Sovereign Voice and Local Runtime Lanes*. The seam statement is strong. However, the “Informative grounding” row uses repository-style relative paths that do not match the style guide’s preferred citation form. In a governed document, path references are useful for repo navigation but should not substitute for formal document-title citations.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 4, Conflict Freedom: 4

**Recommendation:**  
Retain the table, but revise the informative grounding row to cite full document titles first and paths secondarily if needed. Proposed replacement language:

> **Informative grounding (not law here)** | *Composition control plane — R&D and knowledge capture (AMD-2026-008 addendum track)*, *Composition control plane — architecture memo (bounded domains and addendum seams)*, and *Shell and composition — surface grammar and user-state memo (AMD-2026-008 addendum track)* are informative only and do not add independent normative obligations.

---

### 1. Purpose

**Feedback:**  
The section is substantively complete and accurately describes the addendum’s scope. It also correctly distinguishes this addendum from ADD-002. The main issue is readability: the second paragraph is overloaded with nested parentheticals, repeated bolding, and multiple concepts in one sentence. This is editorially dense enough to obscure otherwise good doctrine.

**Scores:** Completeness: 4, Style & Clarity: 3, Cross-Document Consistency: 4

**Recommendation:**  
Split the second paragraph into shorter sentences and reduce formatting emphasis. Proposed replacement language:

> This addendum also governs professional-use draft disclosure for licensed-professional document classes (§9.4), language and authoritative-version controls (§16), measurement contracts for quantified claims (§17), knowledge-basis and discovery gating (§18), originality and source-boundary verification (§19), and reference-guided composition (§20).  
> Reference-guided composition includes example, template, and authority materials used to shape structure, spirit, and form without authorizing wholesale reproduction. Reference adherence controls in §20.11–§20.15 govern conformity to reference shape; they do not denote model temperature or sampling behavior.

---

### 2. Governing principle and 2.1 Addendum seams

**Feedback:**  
This is one of the strongest sections in the document. It clearly preserves the separation between composition class, packaging, and execution. The seam rules are coherent with the architecture memo and with ADD-001/ADD-002. The only editorial issue is that the prose is more typographically emphatic than necessary, which makes the section feel heavier than its actual content.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 5, Style & Clarity: 4

**Recommendation:**  
No substantive change required. Editorially, reduce bolding to defined terms and critical prohibitions only. For example, convert:

> **Composition class SHALL not be inferred from packaging alone.**

to:

> Composition class **SHALL NOT** be inferred from packaging alone.

---

### 3. Composition class versus packaging and execution

**Feedback:**  
This section is clear and useful. It operationalizes the seam with ADD-002 and gives a concrete example that improves interpretability. No major doctrinal issue appears here.

**Scores:** Practical Operability: 4, Style & Clarity: 4, Architectural Fidelity: 4

**Recommendation:**  
Add one sentence clarifying “formal artifact” versus ordinary export, because later sections rely on that distinction. Proposed addition at the end:

> For this addendum, “formal artifact” means an export or rendered output intended for review, distribution, filing, recordkeeping, or external reliance, as distinguished from transient preview or working-session display.

---

### 4. Responsive, procedural, and composed outputs

**Feedback:**  
The three-class model is coherent and useful. It gives the rest of the document a gating backbone. The main gap is that hybrid cases are acknowledged elsewhere but not resolved here. For example, a structured email campaign draft, a public report, or a document-like invite packet may straddle categories.

**Scores:** Completeness: 4, Practical Operability: 3, Developer Synchrony: 4

**Recommendation:**  
Add a hybrid-resolution rule. Proposed text after §4.3:

> Where an artifact plausibly fits more than one class, the runtime **SHALL** apply the stricter class for gating, review, and disclosure unless policy defines a more specific precedence rule with audit visibility.

---

### 5. Composition contract requirements

**Feedback:**  
This section is strong and central. The triad is clear, the scaffold-only boundary is well stated, and the special cases are sensible. The compact validation table in **§5.9** is especially useful. The main issue is that the section still leaves too much to policy in places where a minimum default could be stated. Also, the phrase “desired outcome” in §5.9 differs slightly from “outcome” elsewhere; that is minor but should be normalized.

**Scores:** Completeness: 4, Legal Enforceability: 4, Practical Operability: 4, Cross-Document Consistency: 4

**Recommendation:**  
1. Normalize terminology to “outcome” throughout.  
2. Add a default fallback rule in §5.9. Proposed addition:

> Unless policy defines a narrower rule, missing mandatory composition-contract fields for a Class 3 artifact **SHALL** default to scaffold-only posture rather than substantive draft posture.

---

### 6. Control-plane axes (twelve axes summary)

**Feedback:**  
This table is useful and aligns well with ADD-002’s twelve-axis model. It materially improves cross-document coherence. No substantive issue.

**Scores:** Cross-Document Consistency: 5, Architectural Fidelity: 5, Developer Synchrony: 4

**Recommendation:**  
No substantive revision required. Consider changing “This addendum §§7–10” to “This addendum (Sections 7–10)” for style consistency.

---

### 7. Composition families

**Feedback:**  
The section is concise and functional. It correctly distinguishes families without overdefining them. No major issue.

**Scores:** Completeness: 4, Style & Clarity: 4

**Recommendation:**  
No substantive change required.

---

### 8. Message and invite classes

**Feedback:**  
The EMAIL and CALENDAR_INVITE sections are operationally useful and align with the product snapshot’s distinction between draft and send semantics. The action tables are clear. One gap is that “Publish to calendar” in §8.2 may be ambiguous because “publish” elsewhere is used for public/distribution classes.

**Scores:** Practical Operability: 4, Developer Synchrony: 4, Style & Clarity: 3

**Recommendation:**  
Replace “Publish to calendar” with a less overloaded term. Proposed replacement in §8.2 action table:

> **Create / place on calendar** | Create the event on the governed calendar surface per product semantics.

---

### 9. Document composition and 9.4 Professional-use draft disclosure

**Feedback:**  
This is a strong section overall. The subclass list is useful, and §9.4 is among the best-governed parts of the document. The trigger determinism in §9.4.0 is especially valuable. The main gap is §9.3, which says policy shall define minimum structure, review level, one-pass eligibility, and default packaging, but gives no minimum fallback if policy has not yet done so. That creates an enforceability gap for draft-stage governance.

**Scores:** Legal Enforceability: 4, Completeness: 4, Business Model Alignment: 4, Style & Clarity: 4

**Recommendation:**  
Add a default fallback in §9.3. Proposed text:

> Until policy defines subclass-specific structure and review posture, **RESEARCH_REPORT**, **POLICY**, **CONTRACT_SUMMARY**, and **BOOK** **SHALL** default to review-required posture and **SHALL NOT** be treated as one-pass send-ready or publish-ready artifacts.

Also revise §9.4.6 to cite the full title on first use:

> Commercial, liability, and Tenant terms remain subject to the *Master Platform Operating Agreement (MPOA)* and applicable product agreements.

---

### 10. Publication and distribution classes

**Feedback:**  
The section is concise and coherent with ADD-002 §10.11. It correctly avoids redefining premium gates. No major issue.

**Scores:** Business Model Alignment: 5, Cross-Document Consistency: 4, Conflict Freedom: 4

**Recommendation:**  
No substantive change required.

---

### 11. Publication-oriented labels (continuity from v0.1.0)

**Feedback:**  
This continuity section is helpful for migration and backward compatibility. It is appropriately limited. No major issue.

**Scores:** Developer Synchrony: 4, Completeness: 4

**Recommendation:**  
No substantive change required.

---

### 12. Action semantics and 12.1 Action-bearing outputs

**Feedback:**  
This section is clear and important. It reinforces that action-bearing artifacts are executions, not just files. It aligns well with the product snapshot’s intent/action separation. One minor issue is that “publish_book” may be read as bypassing ADD-002’s BOOK workflow unless the cross-reference is made more explicit.

**Scores:** Architectural Fidelity: 4, Practical Operability: 4, Cross-Document Consistency: 4

**Recommendation:**  
Add a clarifying sentence after §12.1:

> Any `publish_book` action remains subordinate to the BOOK workflow, approval gates, and entitlement controls defined in *AMD-2026-008-ADD-002 — Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 10 and Section 10.11).

---

### 13. Shell controls and 14. Review, approval, and paid gates

**Feedback:**  
These sections are coherent and appropriately illustrative. They preserve shell visibility and do not overstep into UI design law. No major doctrinal issue appears.

**Scores:** Architectural Fidelity: 4, Developer Synchrony: 4, Style & Clarity: 4

**Recommendation:**  
No substantive change required.

---

### 15. Packaging defaults (informative)

**Feedback:**  
This section is directionally correct but underpowered. It says policy shall associate default packaging with class, but does not define what happens if policy has not done so. Because packaging affects export behavior and later gating, the absence of a fallback rule weakens operability.

**Scores:** Practical Operability: 3, Legal Enforceability: 3, Completeness: 3

**Recommendation:**  
Add a default fallback rule. Proposed replacement:

> Policy **SHALL** associate default packaging with class (for example, EMAIL → provider-native or HTML; MEMO → DOCX or PDF; POST → HTML or MD). Until policy defines a class-specific default, the runtime **SHALL NOT** assume that every class supports every format as a primary path and **SHALL** prefer non-destructive draft or preview posture over irreversible export posture.

---

### 16. Language, localization, and authoritative version control

**Feedback:**  
This section is substantively strong and well integrated with §9.4 and ADD-002. The seam in §16.7 is especially important and mostly well drafted. The main issue is readability: §16.7 is overlong and repeats the same seam point twice. The closing fragment “§2.1 addendum seams.” reads like an editing remnant rather than finished prose.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 3, Conflict Freedom: 4

**Recommendation:**  
Clean §16.7 and remove the orphaned fragment. Proposed replacement for the final line:

> This subsection implements the addendum seam stated in Section 2.1 and does not transfer ownership of depth or VC semantics from ADD-002 to this addendum.

---

### 17. Measurement contract and quantified claims

**Feedback:**  
This section is clear, useful, and commercially disciplined. §17.7 correctly preserves MPOA supremacy for liability and remedies. No major issue.

**Scores:** Business Model Alignment: 5, Legal Enforceability: 4, Style & Clarity: 4

**Recommendation:**  
No substantive change required.

---

### 18. Knowledge basis and discovery gating

**Feedback:**  
This section is conceptually strong and well separated from §19. The seam language is good, and the states/modes are implementable. The main issue is density. Also, the final implementation-join sentence in §18.11 is useful but slightly ambiguous: “record knowledge-basis metadata” does not specify minimum fields or whether the join is mandatory whenever §18 applied.

**Scores:** Architectural Fidelity: 4, Practical Operability: 3, Style & Clarity: 3, Developer Synchrony: 4

**Recommendation:**  
Clarify the minimum join requirement in §18.11. Proposed replacement for the final sentence:

> When §19.2 applies, an `OriginalityEvaluationRecordV1` per AIOS-OPS-020 §9 **SHALL** refer to the same artifact identifier used for the applicable §18 knowledge-basis state record. At minimum, the joinable record set **SHALL** preserve artifact identifier, knowledge state, creation mode, and evaluation timestamp so grounding and originality decisions are auditable together.

---

### 19. Originality, source-boundary, and non-reproduction verification

**Feedback:**  
This is a strong section and much improved by the AIOS-OPS-020 handoff. The distinction between doctrine and implementation home is clear. The fail-closed rule for policy silence in §19.2 is especially important. The main remaining issue is that “formal export” is still not crisply defined, even though it is a gating trigger here and in §5.9 and §18.11. Also, §19.10 cites AIOS-OPS-020 version examples inconsistently with the bundled context, which currently includes AIOS-OPS-020 v0.4.0.

**Scores:** Legal Enforceability: 4, Cross-Document Consistency: 4, Practical Operability: 3, Developer Synchrony: 5

**Recommendation:**  
1. Define “formal export” once, preferably in Section 3 or §19.2.  
2. Update the version example in §19.10 to match the bundled artifact or make it explicitly illustrative. Proposed text:

> Conformance claims to §19 **SHALL** name the governed artifact identifier and version used (for example, `AIOS-OPS-020 v0.4.0`, if that is the active registered version for the deployment) for metrics, thresholds, record shape, and transport bindings.

---

### 20. Reference-guided composition

**Feedback:**  
This section is comprehensive and coherent with §18 and §19. The distinction among template, reference, and authority is particularly strong. The main issue is editorial length and some duplication between §20.1, §20.2, §20.7, and §20.14. The doctrine is sound, but the section could be tightened without loss.

**Scores:** Completeness: 5, Style & Clarity: 3, Conflict Freedom: 4, Architectural Fidelity: 4

**Recommendation:**  
Condense repeated anti-copying language so the section reads more cleanly. For example, merge the first sentence of §20.1 with the first paragraph of §20.2 and reserve §20.14 for the specific “maximum adherence does not bypass §19” rule.

---

### 21. Non-goals

**Feedback:**  
This section is appropriate and consistent with the architecture memo. It helps preserve seams and prevents scope creep. No major issue.

**Scores:** Conflict Freedom: 5, Cross-Document Consistency: 4, Style & Clarity: 4

**Recommendation:**  
No substantive change required.

---

### Footer / End matter

**Feedback:**  
The footer contains a material version-control defect: it says “version 0.14.2 (draft)” while the document front matter and body state version 0.14.5. In a governed document, that is not a cosmetic issue; it creates ambiguity about the reviewed artifact.

**Scores:** Style & Clarity: 2, Cross-Document Consistency: 2, Legal Enforceability: 3

**Recommendation:**  
Replace the footer with:

> *End of AMD-2026-008-ADD-003, version 0.14.5 (draft).*

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Footer / End matter | Version mismatch says 0.14.2 instead of 0.14.5 | Correct the closing footer to match the reviewed version exactly. | Critical | 1, 3, 8 |
| 2 | Sections 0, 1, 9.4.6, 19.10 and throughout | Cross-reference style is inconsistent and often uses file paths or shorthand | Normalize citations to full document title plus section on first reference, with repo paths only as secondary aids if needed. | High | 1, 6, 8 |
| 3 | Section 3 and §19.2 | “Formal export” is a gating trigger but not clearly defined | Add a single definition distinguishing formal export from transient preview or working-session display. | High | 3, 5, 7 |
| 4 | Section 4 | Hybrid artifacts are not explicitly resolved | Add a stricter-class default rule when an artifact plausibly fits multiple classes. | High | 5, 7, 9 |
| 5 | §9.3 | Subclass review/structure defaults are left entirely to policy | Add a fallback rule that high-stakes subclasses default to review-required posture until policy specifies otherwise. | High | 3, 5, 7 |
| 6 | §15 | Packaging defaults lack a fallback when policy is absent | Add a default non-destructive draft/preview posture when no class-specific packaging default exists. | High | 3, 5, 7 |
| 7 | §16.7 | Seam language is correct but overlong and contains an orphan fragment | Rewrite §16.7 more cleanly and remove “§2.1 addendum seams.” as a dangling line. | Medium | 8, 11 |
| 8 | §18.11 | Join between knowledge-basis records and originality records is useful but underspecified | State minimum joinable fields: artifact identifier, knowledge state, creation mode, and evaluation timestamp. | Medium | 4, 7, 9 |
| 9 | §8.2 | “Publish to calendar” uses overloaded terminology | Replace with “Create / place on calendar” or equivalent provider-neutral wording. | Medium | 7, 8 |
| 10 | Sections 1, 16, 18, 19, 20 | Dense formatting and repeated bolding increase friction | Reduce bolding to defined terms and critical mandates; split long sentences where possible. | Medium | 8, 11 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:**  
The document is substantively strong, architecturally coherent, and largely consistent with the bundled governance set, but it still contains several editorial and operability defects that should be corrected before ratification, including a material footer version mismatch, inconsistent citation style, and a few underdefined fallback rules.

**Top 3 Actions Required:**
1. Fix the footer version mismatch and normalize cross-reference formatting throughout the document.
2. Define “formal export” and add fallback rules where policy is currently the only source of operational detail.
3. Tighten readability by simplifying dense seam language, especially in §§1, 16.7, 18.11, and 19.10.