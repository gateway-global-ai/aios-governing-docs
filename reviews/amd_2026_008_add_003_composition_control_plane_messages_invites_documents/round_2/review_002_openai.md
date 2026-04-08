---
review_id: REV-AMD-2026-008-ADD-003-002
document_reviewed: amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.14.6
reviewer: OpenAI
review_date: 2026-04-08
review_round: 2
review_type: editorial
disposition: major_revision_required
composite_score: 3.5
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The document is substantially aligned to AMD-2026-008, ADD-001, ADD-002, AIOS-OPS-020, and the architecture memo, but it still uses inconsistent citation style and contains stale version references that weaken governance coherence. |
| 2 | Business Model Alignment | 3 | The document generally respects ADD-002 and MPOA boundaries, but governance gates and commercial/entitlement gates remain insufficiently separated in Sections 10 and 14. |
| 3 | Legal Enforceability | 4 | The fail-closed posture, professional-use disclosure, and §19 non-waiver language are materially stronger than Round 1, though a few “policy” dependencies and “SHOULD” formulations still soften determinism. |
| 4 | Architectural Fidelity | 4 | The document now cleanly preserves the seams among navigation, depth/VC, composition class, grounding, originality, and DCP transport, including the new §2.1 DCP seam. |
| 5 | Completeness | 4 | The addendum comprehensively covers the intended composition-plane scope, including contract, disclosure, language, measurement, knowledge basis, originality, and reference-guided composition. |
| 6 | Conflict Freedom | 3 | No direct contradiction is evident, but stale internal versioning and mixed citation forms create editorial tension with the style guide and with the document’s own metadata integrity. |
| 7 | Practical Operability | 3 | The control model is implementable in principle, but several provisions still defer too much to policy and leave default runtime behavior under-specified outside originality. |
| 8 | Style & Clarity | 2 | The draft remains materially harder to read than necessary because of excessive bolding, path-style references, and unresolved front-matter/body/footer version mismatches. |
| 9 | Developer Synchrony | 4 | The revision directly addresses the Round 1 DCP namespace/envelope gap and now aligns well with AIOS-OPS-020 §§10, 13, 14, and Appendix B. |
| 10 | Platform Economics Synchrony | 3 | The document properly defers liability and premium BOOK economics to MPOA and ADD-002, but it still does not crisply distinguish governance clearance from paid entitlement. |
| 11 | Friction Factor | 3 | The doctrinal partitioning is sound, but the drafting density and visual noise still impose unnecessary review and implementation friction. |
| | **Composite Score** | **3.5** | |

---

## Overall Assessment

### Strengths

- **Section 2.1** materially improves the document by adding the missing DCP transport seam and explicitly binding §5.9 fail-closed composition conditions to the `aios.dcp.composition` namespace and AIOS-OPS-020 §14 / Appendix B.
- **Section 5.9** is now much stronger than in Round 1; the fail-closed table is operationally meaningful and coheres with **Originality and Source-Boundary Verification (Implementation Home)** (§13 and §14).
- **Sections 18 and 19** now show a clearer handoff between grounding/discovery and release-time originality verification, including joinability through shared artifact identifiers in **§18.11**.
- **Section 9.4** remains one of the strongest parts of the document; the professional-use disclosure regime is specific, durable, and well bounded against MPOA liability allocation.
- **Section 19.9** now properly avoids the Round 1 contradiction by clarifying that disclaimer language limits marketing claims, not runtime enforcement obligations.

### Critical Gaps

- The document still has a **serious editorial integrity defect**: front matter says **0.14.6**, Section 0 says **0.14.5**, and the footer says **0.14.2**.
- Cross-references still frequently use **repository path / markdown-link style** rather than the style guide’s required stable document-title-plus-section citation format, especially in **§0, §1, §2.1, §5.7, §9.4.6, §18.11, §19.4, §19.10, §20.14, and §21**.
- Governance gates, workflow gates, and commercial entitlement gates remain insufficiently separated, especially in **§10** and **§14**, leaving ambiguity about whether a publish-capable artifact is governance-cleared, commercially entitled, or both.
- Several key provisions still rely on **“policy”** without enough default runtime posture, especially in **§5.9, §9.3, §16.5–§16.6, and §18.5–§18.6**.
- **§20.2** and **§20.8** still use **SHOULD** for pre-draft reference disposition steps that appear intended to be mandatory, and Gemini’s Round 1 concern remains valid.

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:** This section still contains one of the document’s clearest Round 2 defects. The front matter version is **0.14.6**, but the status table says **0.14.5**, and the footer says **0.14.2**. That is not a cosmetic issue in a governed document set; it undermines citation reliability and revision traceability. In addition, the “Informative grounding” row still uses repository-path markdown links rather than stable title references, contrary to the style guide.

**Scores:** Cross-Document Consistency: 2, Style & Clarity: 2, Conflict Freedom: 3

**Recommendation:** Correct all version references to **0.14.6** and normalize the grounding row to stable citations. Proposed replacement:

> **Status** | **`draft` `0.14.6`** — addendum to *Sovereign Voice and Local Runtime Lanes* **1.0.0**  
> **Informative grounding (not law here)** | *Composition control plane — R&D and knowledge capture (AMD-2026-008 addendum track)*, *Composition control plane — architecture memo (bounded domains and addendum seams)*, and *Shell and composition — surface grammar and user-state memo (AMD-2026-008 addendum track)* are informative only and do not create additional normative obligations.

---

### 1. Purpose

**Feedback:** The split introduced in prior revisions improved readability, and the section now states scope more clearly. However, it still mixes stable concepts with file-link citation style and remains visually over-emphasized. The final sentence is better than earlier drafts, but it still reads like drafting metadata rather than polished doctrine.

**Scores:** Completeness: 4, Style & Clarity: 3, Cross-Document Consistency: 3

**Recommendation:** Replace markdown-link references with stable title references and reduce emphasis. Proposed final sentence:

> This addendum shall be read together with *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 4, Section 5, Section 7, and Section 10). The documents listed in Section 0 as informative grounding remain non-normative context only.

---

### 2. Governing principle and 2.1 Addendum seams

**Feedback:** This is the strongest Round 2 improvement. I agree with DeepSeek’s Round 1 concern that the DCP seam was missing, and the new fourth bullet in **§2.1** substantially resolves that gap. The section now better reflects the architecture memo’s seam rules and cleanly separates ownership among ADD-001, ADD-002, this addendum, and AIOS-OPS-020. The remaining issue is editorial: the section still uses file-style references and excessive bolding, and “normative for authors” could still be read too narrowly given that implementers will also rely on these seam rules for interpretation.

**Scores:** Architectural Fidelity: 5, Developer Synchrony: 5, Style & Clarity: 3

**Recommendation:** Keep the new DCP seam, but clarify interpretive scope. Proposed insertion under the heading:

> The seam rules in this Section 2.1 are binding on document authors and controlling for interpretation where this addendum overlaps with ADD-001, ADD-002, or AIOS-OPS-020.

---

### 5. Composition contract requirements, especially 5.9

**Feedback:** This section is materially improved from Round 1. The fail-closed table is now coherent, and the explicit pointer to AIOS-OPS-020 §13 for default DCP code names addresses a major prior synchrony gap. However, the section still leaves too much to policy in one important respect: it says policy shall define when missing or invalid fields block send/publish/export or force scaffold/review, but it does not state a default runtime posture for all Class 3 artifacts when policy is silent. The fail-closed table helps, but the opening sentence of **§5.9** still reads as if policy is the primary determinant.

**Scores:** Legal Enforceability: 4, Practical Operability: 3, Developer Synchrony: 4

**Recommendation:** Add a default rule at the start of **§5.9**. Proposed text:

> Unless policy expressly defines a narrower or stricter rule, missing mandatory composition-contract fields for a Class 3 artifact shall force scaffold-only posture and shall block send, publish, and formal export.

---

### 9.4 Professional-use draft disclosure

**Feedback:** This remains a high-quality section. The trigger hierarchy in **§9.4.0** is useful, and the export-preservation rule in **§9.4.3(5)** is strong. I continue to agree with the Round 1 assessment that this section is one of the most legally and operationally mature parts of the draft. The remaining issue is editorial and enforceability-related: **§9.4.0** still uses “reasonable classification,” which is softer than the rest of the framework and weaker than the style guide prefers.

**Scores:** Legal Enforceability: 4, Style & Clarity: 3, Cross-Document Consistency: 3

**Recommendation:** Replace “reasonable classification” in **§9.4.0** with more deterministic language. Proposed replacement:

> When signals conflict or remain ambiguous after policy-defined classification steps, the runtime shall apply §9.4 draft posture and disclosure rather than assuming non-professional use, unless policy records a narrower rule with audit visibility.

Also normalize **§9.4.6** to cite *Gateway Global AIOS Master Platform Operating Agreement* by title rather than file path.

---

### 10. Publication and distribution classes

**Feedback:** This section is still too thin relative to the importance of publish/distribute semantics elsewhere in the document. It correctly points to ADD-002 §10.11 for premium enhancement and distribution, but it still does not clearly distinguish governance eligibility from commercial entitlement. That ambiguity was flagged in Round 1 and remains unresolved.

**Scores:** Business Model Alignment: 3, Platform Economics Synchrony: 3, Practical Operability: 3

**Recommendation:** Add an explicit distinction. Proposed sentence after the table:

> Governance clearance to publish or distribute under this addendum does not itself grant commercial entitlement to enhancement, publishing, or distribution capabilities; those remain separately governed by *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 10.11) and applicable MPOA terms.

---

### 14. Review, approval, and paid gates

**Feedback:** This remains one of the weakest sections. It gestures at policy approval, ADD-002 review gates, and premium gates, but it still does not clearly separate governance review gates, workflow gates, and commercial gates. This was a major Round 1 editorial coherence issue and is still only partially addressed.

**Scores:** Business Model Alignment: 2, Platform Economics Synchrony: 2, Style & Clarity: 3

**Recommendation:** Rewrite **§14** into three explicit bullets:

> - **Governance review gates:** Policy may require review or approval before send, issue, publish, or formal export.  
> - **Workflow gates:** RESEARCH_REPORT, BOOK, and public REPORT artifacts shall follow any mandatory review workflow defined in this addendum and in *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 10 and Section 10.11).  
> - **Commercial gates:** Image insertion, designed PDF, publishing pipeline, and public distribution may require separate entitlement or paid access under ADD-002 Section 10.11 and applicable MPOA terms.

---

### 16. Language, localization, and authoritative version control

**Feedback:** This section is strong in structure and seam discipline, especially **§16.7**, which now properly avoids re-owning depth/VC. However, the authoritative-language rule still leaves too much to policy and workflow for high-stakes multilingual artifacts. The current wording says the runtime shall identify the authoritative version “when required” by policy, workflow, or professional-use context. For legal, policy, compliance, contract, and comparable professional-use multilingual artifacts, that should be a default requirement, not merely a conditional one.

**Scores:** Legal Enforceability: 3, Practical Operability: 3, Cross-Document Consistency: 4

**Recommendation:** Strengthen **§16.5**. Proposed replacement:

> Where multiple language versions of the same legal, policy, compliance, contract, or other professional-use artifact exist, the runtime shall require an explicit `authoritative_language` designation before send, publish, or formal export unless policy expressly records that no authoritative-language distinction applies.

---

### 18. Knowledge basis and discovery gating, especially 18.11

**Feedback:** This section is improved and now much clearer in its seam with §19. The joinability language in **§18.11** is a meaningful improvement and aligns with AIOS-OPS-020 §15. However, the section still lacks a minimum auditable record for §18 itself analogous to the explicit record shape available for §19. The text says grounding and originality should be joinable in audit, but the grounding side remains under-specified. Also, **§18.11(A)(4)** still uses **SHOULD** for reference disposition before substantive drafting, which weakens determinism.

**Scores:** Completeness: 4, Practical Operability: 3, Developer Synchrony: 4

**Recommendation:** Add a minimum §18 audit record requirement and tighten the reference-disposition step. Proposed additions:

> When Section 18 applies, the runtime shall record at minimum the artifact identifier, `knowledge_state`, `creation_mode`, and the basis for that determination in an auditable control-plane record.

And revise **§18.11(A)(4)** from **SHOULD** to **SHALL** if reference disposition is intended to be mandatory when references are in scope.

---

### 19. Originality, source-boundary, and non-reproduction verification

**Feedback:** This section is substantially stronger than in Round 1. I agree with DeepSeek that the earlier contradiction between enforcement and disclaimer language has been resolved. The non-waiver language in **§19.2** and **§19.9** is now clear and coherent. The remaining editorial issue is that **§19.10** still contains stale version examples: it references **AIOS-OPS-020 v0.4.0** and gives **v0.3.2** as the conformance example, while the bundled operations standard is **0.4.1**. That is not fatal doctrinally, but it is poor cross-document hygiene.

**Scores:** Legal Enforceability: 5, Conflict Freedom: 4, Cross-Document Consistency: 3

**Recommendation:** Update **§19.10** to reference the bundled version consistently. Proposed replacement:

> Algorithm identifiers and concrete scorers remain deferred to policy or AIOS-OPS-020 **v0.4.1**.  
> Conformance claims to §19 shall name the governed artifact identifier and version used, for example `AIOS-OPS-020 v0.4.1`.

---

### 20. Reference-guided composition

**Feedback:** This section remains substantively strong but still carries the main unresolved legal/editorial issue from Gemini’s Round 1 review. **§20.2** and **§20.8** still use **SHOULD** for pre-draft reference analysis and disposition steps that appear intended to be mandatory in a governed composition system. I agree with Gemini that this weakens enforceability. The section is also still longer and more repetitive than necessary.

**Scores:** Legal Enforceability: 3, Style & Clarity: 3, Practical Operability: 3

**Recommendation:** Replace **SHOULD** with **SHALL** in **§20.2** and **§20.8**. Proposed changes:

- **§20.2**  
  **Old:** “Where a reference is supplied, the runtime SHOULD determine…”  
  **New:** “Where a reference is supplied, the runtime SHALL determine…”

- **§20.8**  
  **Old:** “Before substantive drafting, the runtime SHOULD resolve…”  
  **New:** “Before substantive drafting, the runtime SHALL resolve…”

---

### 21. Non-goals

**Feedback:** The section is useful, but it still uses file-style references rather than stable title-and-section citations. This is a recurring editorial problem across the document. The non-goal on legal determination of infringement is sound and coheres with **§19.9**.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 3

**Recommendation:** Normalize the bullets to stable references. Example:

> - Navigation primitives — *Base Shell Navigation Primitives and Start-Here Control*  
> - Output depth, VC classes, packaging taxonomy detail, and BOOK workflow phases — *Verbose Grounding, Shell Voice Output Control, and Output Packaging* (Section 4, Section 5, Section 7, and Section 10)

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §0 / footer / global | Version references are internally inconsistent (0.14.6 vs 0.14.5 vs 0.14.2) | Correct all body and footer version references to 0.14.6 and verify no stale internal version examples remain. | Critical | 1, 6, 8 |
| 2 | Global | Cross-references still use path/link style instead of stable title-and-section citations | Replace repository-path references with canonical document-title and section citations throughout. | High | 1, 8 |
| 3 | §14 | Governance gates, workflow gates, and commercial gates remain conflated | Rewrite §14 into separate governance, workflow, and commercial gate clauses. | Critical | 2, 7, 10 |
| 4 | §20.2 / §20.8 / §18.11(A)(4) | “SHOULD” weakens mandatory pre-draft reference disposition | Replace “SHOULD” with “SHALL” where reference disposition is intended to be binding. | High | 3, 7, 8 |
| 5 | §16.5 | Authoritative-language rule is too policy-dependent for high-stakes multilingual artifacts | Require explicit `authoritative_language` for legal, policy, compliance, contract, and other professional-use multilingual artifacts before release unless policy expressly records otherwise. | High | 3, 7 |
| 6 | §5.9 | Default runtime posture for missing Class 3 contract fields is still too policy-dependent | Add a default rule that missing mandatory Class 3 contract fields force scaffold-only posture and block send/publish/formal export unless policy is stricter. | High | 3, 7 |
| 7 | §18 | Knowledge-basis gating lacks a minimum auditable record analogous to §19 | Require an auditable control-plane record with artifact identifier, `knowledge_state`, `creation_mode`, and basis for determination. | Medium | 5, 7, 9 |
| 8 | §19.10 | Stale AIOS-OPS-020 version examples reduce cross-document hygiene | Update examples to the bundled AIOS-OPS-020 version (0.4.1) or label them explicitly as illustrative historical examples. | Medium | 1, 8 |
| 9 | Global | Excessive bolding still materially reduces readability | Remove non-essential bold formatting and reserve emphasis for defined terms and critical rules only. | Medium | 8, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The revision meaningfully improves architectural fidelity and developer synchrony, especially through the new DCP seam and stronger §19 posture, but the document still fails the disposition threshold because Style & Clarity remains at 2 and several high-impact editorial and cross-document coherence defects remain unresolved.

**Top 3 Actions Required:**
1. Fix document integrity defects immediately: align all version references and normalize citations to stable document-title-plus-section form.
2. Rewrite Section 14 to clearly separate governance review gates, workflow gates, and commercial entitlement gates.
3. Replace remaining critical “SHOULD” formulations in Sections 18 and 20 with “SHALL” where the process is intended to be mandatory.