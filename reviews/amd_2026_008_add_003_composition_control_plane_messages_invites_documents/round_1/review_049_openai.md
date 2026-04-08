---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.14.5
reviewer: OpenAI
review_date: 2026-04-08
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 3.2
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The document is largely aligned to ADD-001, ADD-002, AMD-2026-008, and AIOS-OPS-020, but several citations use file-style references or inconsistent path/title forms instead of stable document-title-plus-section references required by the style guide. |
| 2 | Business Model Alignment | 3 | The document generally respects MPOA and ADD-002 premium gating, but send/publish/export controls do not consistently distinguish governance gating from commercial entitlement gating. |
| 3 | Legal Enforceability | 3 | Many obligations are framed with enforceable SHALL language, but several provisions defer too much to “policy” without specifying minimum decision criteria, audit requirements, or precedence rules. |
| 4 | Architectural Fidelity | 4 | The document strongly preserves the seam between navigation, depth/VC, composition class, grounding, and originality, and it correctly avoids collapsing composition into generic text generation. |
| 5 | Completeness | 4 | The document covers the intended control-plane scope comprehensively, including contract, professional disclosure, language, measurement, grounding, originality, and reference adherence. |
| 6 | Conflict Freedom | 3 | No direct contradiction is evident, but there is tension between this addendum’s broad normative surface and the parent amendment’s sovereign voice/runtime scope, and some MPOA references are too general to prove clean boundary discipline. |
| 7 | Practical Operability | 3 | The control logic is conceptually strong, but implementers still lack enough concrete minimums for policy silence, required audit fields outside originality, and release-path decision handling across all gates. |
| 8 | Style & Clarity | 2 | The document is materially harder to read than necessary because of excessive bolding, dense sentence construction, inconsistent section-reference style, and a footer version mismatch. |
| 9 | Developer Synchrony | 3 | The document is architecturally coherent with the surrounding memos and AIOS-OPS-020, but the product snapshot does not yet evidence implementation of this composition plane, leaving synchrony mostly aspirational. |
| 10 | Platform Economics Synchrony | 3 | The document properly points to MPOA and ADD-002 for liability and premium BOOK economics, but it does not clearly separate which actions are merely governed versus billable, toll-bearing, or entitlement-gated. |
| 11 | Friction Factor | 4 | Despite density, the control model is logically partitioned and should reduce unsafe composition behavior once implemented, though the drafting style itself adds review friction. |
| | **Composite Score** | **3.2** | |

---

## Overall Assessment

### Strengths

- **Section 2 and Section 2.1** clearly establish doctrinal seams with **AMD-2026-008-ADD-001** and **AMD-2026-008-ADD-002**, which materially improves cross-document coherence.
- **Section 5** provides a strong conceptual core through the role/intent/outcome composition contract and correctly distinguishes scaffold-only output from substantive drafting.
- **Section 9.4** is one of the strongest parts of the document; it gives a meaningful governance posture for professional-use drafts and preserves alignment with MPOA liability boundaries.
- **Sections 18–20** are substantively well-structured and show good editorial discipline in separating grounding, originality, and reference-guided composition.
- **Section 19.10** appropriately hands off metrics, schemas, and DCP bindings to **ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD (AIOS-OPS-020)** rather than overloading this addendum.

### Critical Gaps

- The document does **not** follow the stated style-guide cross-reference convention consistently; many references are file/path style rather than stable title-and-section citations, especially in **Sections 0, 1, 2.1, 5.7, 9.4.6, 18.11, 19.4, 19.10, 20.14, and 21**.
- The document footer says **“version 0.14.2”** while the front matter says **0.14.5**, which is a material editorial integrity defect.
- Several provisions rely on “policy” as the operative decision-maker without enough minimum governance content, especially in **Sections 5.9, 9.3, 16.6, 18.5–18.6, and 19.4**, making enforcement and implementation less deterministic than the rest of the framework.
- The document’s prose is over-emphasized and visually noisy; the pervasive bolding materially reduces clarity and increases ambiguity risk in a binding governance text.
- The relationship between governance gates and commercial gates remains under-specified, especially where **send**, **publish**, **formal export**, and **premium enhancement/publishing** intersect across **Sections 10, 12, 14, 15, and 19**.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:**  
This section correctly positions the addendum relative to ADD-001 and ADD-002, and the inclusion of informative grounding documents is useful. However, the references are presented as markdown file links and repository paths rather than stable governance citations by document title and section. That weakens cross-document durability. The path references also appear inconsistent with the bundled metadata categories; for example, the informative memos are presented under `../reference/implementation/...`, while the bundled documents are reference-category governance artifacts, not necessarily implementation-path artifacts. That creates editorial uncertainty about canonical location versus cited identity.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 2, Developer Synchrony: 3

**Recommendation:**  
Replace file-path style references with stable document-title references. Proposed text change in the “Informative grounding” row:

> **Informative grounding (not law here):** *Composition control plane — R&D and knowledge capture (AMD-2026-008 addendum track)*, *Composition control plane — architecture memo (bounded domains and addendum seams)*, and *Shell and composition — surface grammar and user-state memo (AMD-2026-008 addendum track)* are informative only and do not create additional normative obligations.

If section-level citations are available, add them.

---

### 1. Purpose

**Feedback:**  
The section is substantively strong and accurately scopes the addendum. It also properly states that the addendum must be read with ADD-002. However, the prose is overloaded with emphasis and parenthetical density. The final sentence beginning “Informative only...” is especially hard to parse and reads more like a drafting note than polished doctrine. This section should be a clean statement of purpose, not a compressed index.

**Scores:** Completeness: 4, Style & Clarity: 2, Conflict Freedom: 3

**Recommendation:**  
Split the section into a short purpose paragraph and a short “Relationship to Other Documents” paragraph. Proposed replacement for the final sentence:

> This addendum shall be read together with *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 4, Section 5, Section 7, and Section 10) for output depth, shell voice controls, packaging, and BOOK workflow gates. The R&D notes, architecture memo, and shell surface memo listed in Section 0 are informative only and do not create additional runtime obligations.

---

### 2. Governing principle

**Feedback:**  
This is one of the strongest sections in the document. It clearly states that artifact generation follows composition class and action semantics rather than generic text length. The seam language in **Section 2.1** is also valuable. The main issue is editorial: the section is visually over-bolded and therefore harder to interpret than necessary. Also, “normative for authors” in Section 2.1 is useful, but the document should clarify whether those seam rules are binding only on future document authors or also on implementers interpreting overlaps.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:**  
Retain substance, simplify formatting, and clarify audience. Proposed insertion at the start of Section 2.1:

> The seam rules in this Section 2.1 are binding on document authors and controlling for interpretation where this addendum overlaps with ADD-001 or ADD-002.

---

### 3. Composition class versus packaging and execution

**Feedback:**  
This section is clear and useful. It correctly distinguishes composition class, packaging, and execution. The examples are practical and align with ADD-002. No major substantive issue appears here. Minor improvement: “primary path” for EMAIL and CALENDAR_INVITE should be tied more explicitly to action semantics in Section 12 to avoid duplicate interpretive work.

**Scores:** Practical Operability: 4, Architectural Fidelity: 4, Style & Clarity: 4

**Recommendation:**  
Add one sentence at the end:

> Action-bearing artifacts shall follow the action semantics in Section 12 even when a product also supports export or archival packaging.

---

### 4. Responsive, procedural, and composed outputs

**Feedback:**  
The three-class model is coherent and useful. It gives the later gating logic a stable foundation. The main issue is that “non-trivial” appears repeatedly but is not itself defined. Because many later obligations hinge on whether an artifact is “non-trivial,” the document should either define that term or avoid using it as a threshold trigger.

**Scores:** Completeness: 4, Legal Enforceability: 3, Practical Operability: 3

**Recommendation:**  
Add a definition sentence in Section 4.3 or Section 5. Proposed text:

> For purposes of this addendum, “non-trivial” means persistent, externally distributable, approval-bearing, or materially consequential artifacts, including all Class 3 artifacts unless policy expressly classifies a narrower subset.

---

### 5. Composition contract requirements

**Feedback:**  
This is the doctrinal center of the addendum and is generally well done. The role/intent/outcome triad is clear, and scaffold-only behavior is appropriately fail-safe. The main gap is in **Section 5.9**: it says policy shall define when missing or invalid fields block send/publish/export or force scaffold/review, but the document itself should specify a minimum default posture for each Class 3 action even absent policy detail. Otherwise, “policy” becomes a hidden dependency that can weaken determinism.

The DCP handoff to AIOS-OPS-020 is sensible, but only originality has a named implementation home. Composition-contract validation and knowledge-state signaling remain less concretely specified.

**Scores:** Completeness: 4, Legal Enforceability: 3, Practical Operability: 3, Cross-Document Consistency: 4

**Recommendation:**  
Strengthen Section 5.9 with a default rule. Proposed insertion after the first sentence of Section 5.9:

> Unless policy expressly defines a narrower or stricter rule, missing mandatory composition-contract fields for a Class 3 artifact shall default to scaffold_only for drafting and shall block send, publish, and formal export.

Also consider adding a minimal audit requirement:

> The runtime shall record the contract-resolution state for each Class 3 artifact before substantive drafting, send, publish, or formal export.

---

### 6. Control-plane axes (twelve axes summary)

**Feedback:**  
This section is useful and aligns well with ADD-002’s twelve-axis framing. It improves coherence across the addenda. No substantive defect appears. Minor editorial issue: the section should explicitly say it is a summary map and not a source of independent obligations beyond the cited sections.

**Scores:** Cross-Document Consistency: 5, Style & Clarity: 4, Architectural Fidelity: 4

**Recommendation:**  
Add a final sentence:

> This table is a control-map summary and does not supersede the operative text in the cited sections.

---

### 7. Composition families

**Feedback:**  
The family taxonomy is concise and coherent. It aligns with later sections. No major issue. Minor suggestion: “Invites” currently references future task reminders but says not defined here; that is acceptable, though it may be cleaner to omit future hints from normative taxonomy sections.

**Scores:** Completeness: 4, Style & Clarity: 4

**Recommendation:**  
Optional editorial trim: remove the parenthetical future reminder note from the table and leave future expansion to Section 8.3.

---

### 8. Message and invite classes

**Feedback:**  
This section is operationally useful and clearly separates draft, review, send, and schedule semantics. That is a strong fit with the broader governance model. The main gap is that **Schedule send** and **Publish to calendar** are introduced without any explicit tie to approval, audit, or policy gating. Because these are execution-bearing actions, the section should state that they remain subject to policy and audit controls.

**Scores:** Practical Operability: 4, Legal Enforceability: 3, Developer Synchrony: 3

**Recommendation:**  
Add to both 8.1 and 8.2:

> All execution-bearing actions in this Section 8 remain subject to policy approval requirements, audit recording, and any applicable entitlement or provider constraints.

---

### 9. Document composition

**Feedback:**  
The subclass taxonomy is strong and useful. Section 9.4 is especially well developed and likely to be reusable elsewhere. The trigger hierarchy in **Section 9.4.0** is a good improvement. The main issue is that “reasonable classification” appears in **Section 9.4.0**, which is softer than the style guide prefers. Also, **Section 9.4.6** cites MPOA by file path rather than stable title reference.

**Scores:** Legal Enforceability: 4, Cross-Document Consistency: 3, Style & Clarity: 3

**Recommendation:**  
Replace “reasonable classification” with more deterministic language. Proposed text in Section 9.4.0:

> When signals conflict or remain unresolved after policy-defined classification steps, the runtime shall apply Section 9.4 draft posture and disclosure rather than assuming non-professional use, unless policy records a narrower rule with audit visibility.

Also revise Section 9.4.6 to:

> Commercial terms, liability allocation, and Tenant obligations remain governed by the *Gateway Global AIOS Master Platform Operating Agreement* (Article III, Article VIII, and Article X where applicable) and product agreements.

---

### 10. Publication and distribution classes

**Feedback:**  
This section is concise and coherent, but it is too thin relative to the importance of publish/distribute actions elsewhere in the document. It points to ADD-002 Section 10.11 for premium enhancement and distribution, but it does not distinguish governance eligibility from commercial entitlement. That creates ambiguity: can an artifact be governance-cleared for publish but still commercially locked, or vice versa? The answer is probably yes, but the document should say so.

**Scores:** Business Model Alignment: 3, Platform Economics Synchrony: 3, Practical Operability: 3

**Recommendation:**  
Add a clarifying sentence:

> Governance clearance to publish or distribute under this addendum does not itself grant commercial entitlement; premium enhancement, publishing, and distribution capabilities remain separately gated under *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 10.11) and applicable MPOA terms.

---

### 11. Publication-oriented labels (continuity from v0.1.0)

**Feedback:**  
This continuity section is acceptable, but it risks preserving legacy labels without enough guardrails. In particular, **A3 RESEARCH_REPORT** maps to a class that may be either document or publication “per context,” which is under-specified for a normative alias table.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 3

**Recommendation:**  
Clarify that policy must resolve ambiguous mappings. Proposed revision to the A3 row:

> **A3 RESEARCH_REPORT** | **RESEARCH_REPORT**; policy shall classify it as **DOCUMENT.RESEARCH_REPORT** or **REPORT** under Section 10 before send, publish, or formal export |

---

### 12. Action semantics (cross-cutting)

**Feedback:**  
This section is important and generally clear. It correctly rejects a single undifferentiated “generate” action. However, the action list should explicitly state that action semantics are governance controls independent of packaging and independent of premium entitlement. That would reduce ambiguity with Sections 10 and 15.

**Scores:** Architectural Fidelity: 4, Practical Operability: 4, Platform Economics Synchrony: 3

**Recommendation:**  
Add:

> Action semantics in this Section 12 govern workflow posture and do not by themselves determine packaging, billing, or entitlement status.

---

### 13. Shell controls (illustrative)

**Feedback:**  
Useful as an illustrative section, but because it is illustrative, it should be more clearly labeled as non-exhaustive and non-binding. Otherwise readers may infer a minimum UI inventory. The shell surface memo already carries much of this burden.

**Scores:** Style & Clarity: 3, Developer Synchrony: 3

**Recommendation:**  
Retitle to:

> ### 13. Shell controls (illustrative, non-exhaustive)

And add:

> Products may vary control names and presentation so long as the underlying governed actions remain observable and auditable.

---

### 14. Review, approval, and paid gates

**Feedback:**  
This section is directionally correct but underdeveloped. It mixes policy approval, ADD-002 review gates, and premium gates in three bullets without clearly separating governance review from commercial gating. This is one of the places where business-model coherence needs tightening.

**Scores:** Business Model Alignment: 2, Platform Economics Synchrony: 2, Practical Operability: 3

**Recommendation:**  
Rewrite as a three-part distinction:

> - **Governance review gates:** Policy may require review or approval before send, issue, publish, or formal export.  
> - **Workflow gates:** RESEARCH_REPORT, BOOK, and public REPORT artifacts shall follow any mandatory review workflow defined in this addendum and in *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 10 and Section 10.11).  
> - **Commercial gates:** Image insertion, designed PDF, publishing pipeline, and public distribution may require separate entitlement or paid access under ADD-002 Section 10.11 and applicable MPOA terms.

---

### 15. Packaging defaults (informative)

**Feedback:**  
This section is acceptable as informative guidance. It correctly avoids overcommitting every class to every format. No major issue.

**Scores:** Style & Clarity: 4, Practical Operability: 4

**Recommendation:**  
No substantive change required.

---

### 16. Language, localization, and authoritative version control

**Feedback:**  
This section is strong and well partitioned. Section 16.7 is especially valuable because it preserves the seam with ADD-002. The main issue is that some obligations still defer to policy without enough minimums for when multilingual artifacts require authoritative-language designation. For legal, policy, compliance, and contract contexts, the document should state a default requirement rather than leaving it entirely to policy/workflow/professional-use context.

**Scores:** Cross-Document Consistency: 4, Legal Enforceability: 3, Practical Operability: 3

**Recommendation:**  
Strengthen Section 16.5 with a default rule:

> For legal, policy, compliance, contract, and other professional-use multilingual artifacts, the runtime shall require an explicit authoritative_language designation before send, publish, or formal export unless policy expressly records that no authoritative-language distinction applies.

---

### 17. Measurement contract and quantified claims

**Feedback:**  
This section is conceptually strong and appropriately bounded by MPOA in Section 17.7. It clearly distinguishes procedural governance from factual warranty. No major contradiction appears. Minor issue: “materially rely” and “materially significant” are sensible but could benefit from a policy-defined threshold reference.

**Scores:** Legal Enforceability: 4, Conflict Freedom: 4, Practical Operability: 4

**Recommendation:**  
Add one sentence in Section 17.3:

> Policy shall define artifact classes or claim types presumed to be materially measurement-dependent for purposes of this Section 17.

---

### 18. Knowledge basis and discovery gating

**Feedback:**  
This is another strong section. The seam with Section 19 is now much clearer than in earlier drafts implied by the revision log. The sequence in Section 18.11 is useful. The main remaining gap is implementation determinism: knowledge states are defined, but there is no minimum required audit record or state object analogous to AIOS-OPS-020’s originality record. The text says grounding and originality results should be joinable in audit, but the grounding side remains underspecified.

**Scores:** Completeness: 4, Practical Operability: 3, Developer Synchrony: 3

**Recommendation:**  
Add a minimum audit requirement in Section 18.11 or 18.5:

> When Section 18 applies, the runtime shall record at minimum the artifact identifier, knowledge_state, creation_mode, and the basis for that determination in an auditable control-plane record.

If a separate operations artifact is planned, name it explicitly as future implementation home.

---

### 19. Originality, source-boundary, and non-reproduction verification

**Feedback:**  
This section is substantively strong and now coheres well with AIOS-OPS-020. The distinction between doctrinal obligations here and implementation detail in AIOS-OPS-020 is appropriate. The fail-closed rule for policy silence in Section 19.2 is especially important and well framed. The main issue is editorial density and some versioning ambiguity: Section 19.10 references AIOS-OPS-020 examples including `v0.3.2`, while the bundled artifact is `0.4.0`. That example is not wrong, but it is potentially confusing in a live governance set.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 4, Style & Clarity: 3, Practical Operability: 4

**Recommendation:**  
Update the example in Section 19.10 to use the bundled version or make it explicitly illustrative:

> Conformance claims to Section 19 shall name the governed artifact identifier and the exact version in force for the implementation, for example `AIOS-OPS-020 v0.4.0`.

Also reduce bolding throughout this section.

---

### 20. Reference-guided composition

**Feedback:**  
This section is comprehensive and well integrated with Sections 18 and 19. The distinction among template, reference, and authority is especially helpful. The adherence scale is useful and should be implementable. The main issue is length and repetition; several ideas recur across Sections 20.1, 20.2, 20.7, 20.12, and 20.14. Editorial compression would improve clarity without losing substance.

**Scores:** Completeness: 5, Style & Clarity: 3, Practical Operability: 4

**Recommendation:**  
Condense repeated anti-copying language and keep one primary rule in Section 20.2, then use later sections only for specific controls. No doctrinal change required.

---

### 21. Non-goals

**Feedback:**  
This section is useful and generally clean. However, it again uses file-style references rather than stable title-and-section citations. Also, the non-goal bullet for legal determination of infringement should cite Section 19.9 for internal coherence.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 3

**Recommendation:**  
Revise bullets to use stable references, for example:

> - Navigation primitives — *Base Shell Navigation Primitives and Start-Here Control*  
> - Output depth, VC classes, packaging taxonomy detail, and BOOK workflow phases — *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 4, Section 5, Section 7, and Section 10)  
> - Legal determination of infringement, fair use, or licensing — counsel and jurisdiction-specific law; see Section 19.9

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Global / Footer | Footer version says 0.14.2 while front matter says 0.14.5 | Correct the footer to match the front matter version and verify no stale internal version references remain. | Critical | 1, 6, 8 |
| 2 | Global | Cross-references use file/path style rather than stable title-and-section citations | Replace repository-path references with canonical document-title and section citations throughout. | High | 1, 8 |
| 3 | Global | Excessive bolding materially reduces readability | Remove non-essential bold formatting and reserve emphasis for defined terms and critical rules only. | High | 8, 11 |
| 4 | 5.9 | Policy dependency is too open-ended for Class 3 gating | Add a default rule that missing mandatory contract fields force scaffold_only and block send/publish/formal export unless policy is stricter. | Critical | 3, 5, 7 |
| 5 | 9.4.0 | “Reasonable classification” is softer than the rest of the framework | Replace with policy-defined classification steps and deterministic fallback to professional-use draft posture. | High | 3, 8 |
| 6 | 10 / 14 | Governance gates and commercial gates are not clearly separated | Distinguish governance clearance, workflow review, and commercial entitlement in explicit separate clauses. | Critical | 2, 7, 10 |
| 7 | 16.5 | Authoritative-language requirement is too policy-dependent for high-stakes multilingual artifacts | Require explicit authoritative_language for legal, policy, compliance, contract, and professional-use multilingual artifacts before release. | High | 3, 7 |
| 8 | 18.5 / 18.11 | Knowledge-state gating lacks a minimum auditable record | Require an auditable control-plane record with artifact_id, knowledge_state, creation_mode, and basis for determination. | High | 5, 7, 9 |
| 9 | 19.10 | Example version reference may confuse readers because bundled AIOS-OPS-020 is 0.4.0 | Update the example to the bundled version or label it explicitly as illustrative only. | Medium | 1, 8 |
| 10 | 20 | Repetition makes the section longer and harder to apply | Consolidate repeated anti-copying language and keep later subsections focused on controls rather than restatement. | Medium | 8, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is substantively strong and architecturally coherent, but it has one dimension at 2 and multiple dimensions at 3, with notable editorial integrity, cross-reference, and operability issues that should be corrected before ratification. The core doctrine is promising; the draft now needs tightening, normalization, and clearer governance-versus-commercial boundary language.

**Top 3 Actions Required:**
1. Fix editorial integrity defects: correct the footer version, normalize citations, and remove excessive bolding.
2. Add deterministic default rules where “policy” currently carries too much of the enforcement burden, especially in Sections 5.9, 16.5, and 18.5/18.11.
3. Explicitly separate governance gates, workflow review gates, and commercial entitlement gates across Sections 10, 12, and 14.