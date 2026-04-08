---
review_id: REV-AMD-2026-008-ADD-003-003
document_reviewed: amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.14.7
reviewer: OpenAI
review_date: 2026-04-08
review_round: 2
review_type: editorial
disposition: approved_with_changes
composite_score: 4.0
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Round 1 citation and seam issues were materially improved, but the document still relies too heavily on markdown file-link style references instead of stable title-plus-section citations in the body. |
| 2 | Business Model Alignment | 4 | The revision now clearly separates governance clearance from entitlement gating in §10 and §14, though a few action sections still do not restate that separation where execution occurs. |
| 3 | Legal Enforceability | 4 | The document now uses stronger deterministic defaults in §5.9, §18.11, and §20, but several clauses still defer to policy without always stating a minimum audit or precedence rule. |
| 4 | Architectural Fidelity | 5 | The addendum now cleanly preserves seams among composition, grounding, originality, DCP transport, and ADD-002 depth/VC controls without collapsing domains. |
| 5 | Completeness | 4 | The document comprehensively covers the intended control-plane scope, with only minor remaining gaps around minimum audit treatment for non-originality gates. |
| 6 | Conflict Freedom | 4 | The major Round 1 tensions were resolved, and no direct contradiction remains, though a few alias and citation choices still create interpretive friction across the set. |
| 7 | Practical Operability | 4 | The document is now substantially more implementable, especially with §5.9 and §18.11 strengthened, but some sections still leave implementers to infer minimum audit behavior outside AIOS-OPS-020. |
| 8 | Style & Clarity | 3 | The draft is clearer than v0.14.5, but excessive bolding, dense sentence construction, and mixed citation style still materially reduce readability in a binding governance text. |
| 9 | Developer Synchrony | 4 | The DCP seam and AIOS-OPS-020 handoff are now explicit and coherent, though product implementation evidence for this addendum remains mostly prospective rather than demonstrated. |
| 10 | Platform Economics Synchrony | 4 | The document now better distinguishes governance gates from premium and MPOA-governed commercial gates, with only minor residual ambiguity at the action layer. |
| 11 | Friction Factor | 4 | The doctrinal structure is now well partitioned and safer to implement, but the drafting style still adds avoidable review and implementation friction. |
| | **Composite Score** | **4.0** | |

---

## Overall Assessment

### Strengths

- **Round 1 issues were substantially addressed.** The most important fixes landed: §2.1 now explicitly assigns DCP transport seam ownership; §5.9 now provides a default Class 3 fail-closed posture; §18.11 now uses mandatory SHALL language for reference disposition and artifact joinability; and §10/§14 now better separate governance gates from commercial entitlement gates.
- **Section 2.1** is materially stronger than the prior draft. It now gives a clear interpretive seam among *Base Shell Navigation Primitives and Start-Here Control*, *Verbose Grounding, Shell Voice Output Control, and Output Packaging*, and **AIOS-OPS-020**.
- **Section 5.9** is now one of the strongest operational sections in the document. It gives a deterministic default posture for missing Class 3 contract fields and ties fail-closed behavior to AIOS-OPS-020 without overloading this addendum with implementation detail.
- **Sections 18–20** now read as a coherent gate stack: grounding first, originality at release time, and reference-guided composition as a controlled input rather than a copying license.
- **Sections 9.4, 10, and 14** now show much better boundary discipline with the Master Platform Operating Agreement (MPOA) and ADD-002 premium gating.

### Critical Gaps

- **Style-guide conformance remains the main weakness.** The document still uses markdown file-link style references throughout the body instead of stable document-title-plus-section citations, despite Round 1 feedback on this exact point. This remains visible in **§0, §1, §2, §2.1, §5.6, §6, §10, §16.7, §18.8, §18.11, §19.8, §20.10, and §21**.
- **The document remains visually over-emphasized.** Excessive bolding still makes binding rules harder to parse than necessary, especially in **§2, §5.2, §5.9, §16.7, §18, §19, and §20**.
- **Minimum audit treatment is still uneven outside originality.** While §18.11 improves joinability with AIOS-OPS-020, the document still does not state a comparably crisp minimum control-plane record for composition-contract failure, professional-use gating, and reference disposition.
- **Section 11** still leaves the A3 alias slightly under-specified by saying “document or publication per context” without requiring policy resolution before release-path actions.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:**  
This section is improved from Round 1 because it now uses stable document titles in prose and better distinguishes informative grounding from law. However, it still presents those titles through markdown file links rather than the style guide’s preferred stable citation form. In a governed corpus, path-shaped references are less durable than title-plus-section references.

**Scores:** Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:**  
Replace file-link style references in the table with plain stable citations. Proposed replacement in the “Does not replace” row:

> **Does not replace:** *Base Shell Navigation Primitives and Start-Here Control* (AMD-2026-008-ADD-001) governs navigation. *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (AMD-2026-008-ADD-002) governs output depth, shell voice controls, packaging classes, BOOK workflow, and premium gates.

---

### 1. Purpose

**Feedback:**  
This section is materially improved. The purpose statement is now cleaner, and the relationship to ADD-002 is more readable than in Round 1. The remaining issue is editorial: the section still mixes stable prose with markdown-linked references, and the sentence density remains high.

**Scores:** Completeness: 5, Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:**  
Keep the structure, but normalize citations and reduce formatting noise. Proposed replacement for the final sentence:

> This addendum shall be read together with *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (AMD-2026-008-ADD-002, Section 4, Section 5, Section 7, and Section 10). The documents listed in Section 0 remain informative only and do not create additional normative obligations.

---

### 2. Governing principle / 2.1 Addendum seams

**Feedback:**  
This is one of the strongest revised sections. It directly addresses the Round 1 seam problem and now clearly states that DCP transport for §5.9 fail-closed conditions emits `aios.dcp.composition` codes and uses AIOS-OPS-020 §14 / Appendix B. This is a successful revision and materially improves cross-document coherence and developer synchrony.

The only remaining issue is citation style and readability. The substance is now sound.

**Scores:** Architectural Fidelity: 5, Cross-Document Consistency: 5, Developer Synchrony: 5, Style & Clarity: 3

**Recommendation:**  
Retain substance. Editorially simplify the fourth bullet by replacing file-link style references with stable citations:

> DCP transport for Section 5.9 fail-closed composition conditions shall emit codes in namespace `aios.dcp.composition`; originality and release codes shall follow *Originality and Source-Boundary Verification (Implementation Home)* (AIOS-OPS-020, Section 10 and Section 13). The minimum DCP envelope shall conform to AIOS-OPS-020 Section 14 and Appendix B (`CompositionPlaneDcpV1`).

---

### 3. Composition class versus packaging and execution

**Feedback:**  
This section remains clear and useful. It continues to do good editorial work by separating artifact class, packaging, and execution. No substantive issue remains here.

**Scores:** Practical Operability: 4, Architectural Fidelity: 4, Style & Clarity: 4

**Recommendation:**  
Optional minor addition for consistency with later sections:

> Execution-bearing actions in this Section 3 remain subject to governance review, policy approval, and any applicable entitlement controls described in Section 14.

---

### 4. Responsive, procedural, and composed outputs

**Feedback:**  
This section is still structurally sound. It gives the rest of the document a stable gating foundation. The only lingering issue is that “non-trivial” remains operative but undefined. The context makes the meaning inferable, but a defined threshold would improve enforceability and consistency.

**Scores:** Completeness: 4, Legal Enforceability: 4, Practical Operability: 4

**Recommendation:**  
Add a definition sentence at the end of §4.3:

> For purposes of this addendum, “non-trivial” means persistent, externally distributable, approval-bearing, or materially consequential artifacts, including all Class 3 artifacts unless policy expressly defines a narrower subset.

---

### 5. Composition contract requirements / 5.9 Normative fields and validation posture

**Feedback:**  
This section shows one of the clearest successful Round 2 revisions. The new opening sentence in §5.9 directly addresses the Round 1 concern by creating a default Class 3 fail-closed posture. The fail-closed table is also much stronger and now coheres with AIOS-OPS-020.

The remaining gap is audit symmetry. Originality has a named evaluation record in AIOS-OPS-020, but composition-contract failure and professional-use gating still lack a minimum required control-plane record in this addendum.

**Scores:** Practical Operability: 5, Legal Enforceability: 4, Developer Synchrony: 4, Completeness: 4

**Recommendation:**  
Add a minimum audit sentence after the §5.9 table:

> For each fail-closed outcome in this Section 5.9, the runtime shall record at minimum the artifact identifier, gate category, blocking condition, and resulting posture in an auditable control-plane record.

---

### 6. Control-plane axes (twelve axes summary)

**Feedback:**  
This remains a strong summary map and is now well aligned with the surrounding addenda. It improves coherence across the package. No substantive issue remains.

**Scores:** Cross-Document Consistency: 5, Architectural Fidelity: 4, Style & Clarity: 4

**Recommendation:**  
Optional editorial addition:

> This table is a summary map and does not supersede the operative text in the cited sections.

---

### 7. Composition families / 8. Message and invite classes

**Feedback:**  
These sections are clear and operationally useful. They preserve the distinction between draft and execution-bearing actions, which is important. However, the action tables in §8 still do not explicitly restate that send/issue actions remain subject to policy, audit, and entitlement constraints. That is inferable from §14, but a direct reminder here would improve local clarity.

**Scores:** Practical Operability: 4, Business Model Alignment: 4, Platform Economics Synchrony: 4

**Recommendation:**  
Add to the end of §8.1 and §8.2:

> All execution-bearing actions in this Section 8 remain subject to policy approval requirements, audit recording, and any applicable entitlement or provider constraints.

---

### 9. Document composition / 9.4 Professional-use draft disclosure

**Feedback:**  
This remains one of the strongest sections in the document. The trigger determinism in §9.4.0 is materially better than earlier drafts, and §9.4.6 now properly cites MPOA by title rather than only by path. This section is legally and editorially strong.

The only remaining improvement would be to make the minimum audit expectation explicit when policy defines a different precedence rule under §9.4.0.

**Scores:** Legal Enforceability: 5, Cross-Document Consistency: 4, Conflict Freedom: 5

**Recommendation:**  
Add to §9.4.0 after the first paragraph:

> Any policy-defined alternative precedence rule shall be recorded with audit visibility sufficient to show why professional-use treatment did or did not apply to the artifact.

---

### 10. Publication and distribution classes

**Feedback:**  
This section successfully addresses a major Round 1 issue. It now clearly states that governance clearance does not itself grant commercial entitlement, and it ties premium enhancement, publishing, and distribution back to ADD-002 Section 10.11 and MPOA terms. This is a strong revision.

**Scores:** Business Model Alignment: 5, Platform Economics Synchrony: 5, Conflict Freedom: 4

**Recommendation:**  
No substantive change required.

---

### 11. Publication-oriented labels (continuity from v0.1.0)

**Feedback:**  
This section is acceptable, but the A3 row still leaves too much ambiguity by saying “document or publication per context.” For a continuity alias table, that should be resolved by policy before release-path actions, not left open-ended.

**Scores:** Cross-Document Consistency: 3, Practical Operability: 3, Style & Clarity: 3

**Recommendation:**  
Revise the A3 row to:

> **A3 RESEARCH_REPORT** | **RESEARCH_REPORT**; policy shall classify it as a document-class or publication-class artifact before send, publish, or formal export |

---

### 12. Action semantics / 13. Shell controls / 14. Review, approval, and paid gates

**Feedback:**  
These sections now work much better together than in Round 1. Section 14 in particular successfully separates governance review gates, workflow gates, and commercial gates. That was a key requested fix, and it has been addressed well.

Section 12 could still benefit from one sentence clarifying that action semantics do not themselves determine billing or entitlement status.

**Scores:** Business Model Alignment: 4, Platform Economics Synchrony: 4, Practical Operability: 4

**Recommendation:**  
Add to §12:

> Action semantics in this Section 12 govern workflow posture and do not by themselves determine packaging, billing, or entitlement status.

---

### 15. Packaging defaults

**Feedback:**  
This section remains acceptable and appropriately informative. No substantive issue.

**Scores:** Style & Clarity: 4, Practical Operability: 4

**Recommendation:**  
No change required.

---

### 16. Language, localization, and authoritative version control

**Feedback:**  
This section is substantively strong and well partitioned. The seam with ADD-002 remains clear. However, the Round 1 recommendation to make authoritative-language designation more deterministic for high-stakes multilingual artifacts was only partially addressed. Section 16.5 still says “when required by policy, workflow, or professional-use context,” which is directionally correct but softer than ideal for legal, policy, compliance, and contract artifacts.

**Scores:** Legal Enforceability: 4, Practical Operability: 4, Cross-Document Consistency: 4

**Recommendation:**  
Strengthen §16.5 with a default rule:

> For legal, policy, compliance, contract, and other professional-use multilingual artifacts, the runtime shall require an explicit `authoritative_language` designation before send, publish, or formal export unless policy expressly records that no authoritative-language distinction applies.

---

### 17. Measurement contract and quantified claims

**Feedback:**  
This section remains strong. It is well bounded and properly defers liability and reliance questions to MPOA. No major issue remains.

**Scores:** Legal Enforceability: 4, Conflict Freedom: 5, Practical Operability: 4

**Recommendation:**  
Optional refinement in §17.3:

> Policy shall define artifact classes or claim types presumed to be materially measurement-dependent for purposes of this Section 17.

---

### 18. Knowledge basis and discovery gating / 18.11 Recommended sequence

**Feedback:**  
This section is materially improved from Round 1. The seam with §19 is now clear, and §18.11 now uses SHALL for reference disposition and explicitly requires joinability between §18 and §19 records. This is a successful revision.

The remaining issue is that §18 still lacks a named minimum record shape of its own. The text now says the states must be implementable as explicit state transitions, which is good, but a minimum record requirement would improve operability.

**Scores:** Completeness: 4, Practical Operability: 4, Developer Synchrony: 4

**Recommendation:**  
Add to §18.11:

> When Section 18 applies, the runtime shall record at minimum the artifact identifier, knowledge_state, creation_mode, and basis for determination in an auditable control-plane record, whether or not Section 19 later applies.

---

### 19. Originality, source-boundary, and non-reproduction verification / 19.10 Implementation handoff

**Feedback:**  
This section is now substantially stronger and resolves the major Round 1 contradiction concern. The non-waiver language in §19.9 is now clearly subordinate to the binding runtime obligations in §19.2–§19.5. The handoff to AIOS-OPS-020 is also much clearer.

One remaining editorial issue: §19.10 still uses `AIOS-OPS-020 v0.3.2` as the example conformance version even though the bundled artifact is now 0.4.1. That is not fatal, but it is an avoidable coherence defect in a governed set.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 5, Cross-Document Consistency: 4, Style & Clarity: 3

**Recommendation:**  
Update the example sentence in §19.10 to:

> Conformance claims to Section 19 shall name the governed artifact identifier and version used, for example `AIOS-OPS-020 v0.4.1`, for metrics, thresholds, record shape, and transport bindings.

---

### 20. Reference-guided composition

**Feedback:**  
This section successfully addresses Gemini’s Round 1 concern by converting key SHOULD language in §20.2 and §20.8 to SHALL. That is an important and successful revision. The section is now doctrinally strong.

The remaining weakness is editorial density. The section still repeats anti-copying concepts across §20.1, §20.2, §20.7, §20.10, and §20.14. Also, §20.12 still uses SHOULD for split `structure_adherence` and `style_adherence`, which is acceptable because it is clearly framed as a product maturity recommendation rather than a core legal obligation.

**Scores:** Legal Enforceability: 5, Completeness: 5, Style & Clarity: 3

**Recommendation:**  
No doctrinal change required. Editorially compress repeated anti-copying language by keeping the primary rule in §20.2 and shortening later restatements.

---

### 21. Non-goals

**Feedback:**  
This section is useful, but it still uses file-link style references rather than stable title citations. The substance is fine.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 3

**Recommendation:**  
Replace link-style bullets with stable citations, for example:

> - Navigation primitives — *Base Shell Navigation Primitives and Start-Here Control* (AMD-2026-008-ADD-001)  
> - Output depth, VC classes, and packaging taxonomy detail — *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (AMD-2026-008-ADD-002)  
> - BOOK phased B0–B9 detail — AMD-2026-008-ADD-002, Section 10

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Global | Body citations still rely on markdown file-link style rather than stable document-title-plus-section citations | Replace file-link references throughout the body with stable citations using document title, document ID where helpful, and section references where applicable. | High | 1, 8, 11 |
| 2 | Global | Excessive bolding still reduces readability and increases interpretive friction | Remove non-essential bold formatting and reserve emphasis for defined terms, section labels, and truly critical rules. | High | 8, 11 |
| 3 | §5.9 | Non-originality fail-closed gates still lack a minimum explicit audit record requirement | Add a sentence requiring an auditable control-plane record with artifact identifier, gate category, blocking condition, and resulting posture for each fail-closed outcome. | High | 3, 5, 7, 9 |
| 4 | §11 | A3 RESEARCH_REPORT alias remains under-specified | Require policy to classify A3 as document-class or publication-class before send, publish, or formal export. | Medium | 1, 5, 7 |
| 5 | §16.5 | Authoritative-language designation remains slightly too policy-dependent for high-stakes multilingual artifacts | Add a default rule requiring explicit `authoritative_language` for legal, policy, compliance, contract, and other professional-use multilingual artifacts before release unless policy expressly records otherwise. | High | 3, 7, 1 |
| 6 | §18.11 | Knowledge-basis gating still lacks a named minimum record requirement of its own | Add a minimum auditable control-plane record for artifact identifier, knowledge_state, creation_mode, and basis for determination whenever §18 applies. | High | 5, 7, 9 |
| 7 | §19.10 | Example conformance version is stale relative to bundled AIOS-OPS-020 v0.4.1 | Update the example version reference to the bundled artifact version or label the example as illustrative only. | Medium | 1, 8 |
| 8 | §8 / §12 | Action sections do not locally restate policy/audit/entitlement constraints | Add short clarifying sentences that execution-bearing actions remain subject to policy approval, audit recording, and applicable entitlement constraints, and that action semantics do not themselves determine billing or entitlement. | Medium | 2, 7, 10 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The revision successfully resolves the major Round 1 editorial and coherence defects, especially around DCP seam ownership, default fail-closed posture, §20 SHALL language, and governance-versus-commercial gate separation. The remaining issues are now mostly editorial normalization and a few operability refinements rather than substantive structural defects.

**Top 3 Actions Required:**
1. Normalize body citations to stable document-title-plus-section references and remove remaining path-style link dependence.
2. Add explicit minimum audit-record requirements for §5.9 fail-closed outcomes and §18 knowledge-basis gating.
3. Reduce excessive bolding and tighten a few residual ambiguity points, especially §11 A3 classification and §16.5 authoritative-language defaulting.