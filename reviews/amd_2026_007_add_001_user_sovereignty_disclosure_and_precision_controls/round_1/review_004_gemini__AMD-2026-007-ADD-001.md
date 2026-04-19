review_id: REV-AMD-2026-007-ADD-001-001
document_reviewed: AMD-2026-007-ADD-001
document_version: 0.1.0
reviewer: Gemini
review_date: 2024-05-15
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 3.1
---

# Peer Review: User Sovereignty Disclosure and Precision Controls

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The addendum is thematically consistent with its parent (AMD-2026-007) but fails to reference the specific policy or UI components that would implement its rules. |
| 2 | Business Model Alignment | 4 | Aligns well with the enterprise-focused, governed platform model by providing transparency and control, which builds trust. |
| 3 | Legal Enforceability | 2 | Extensive use of "SHOULD" and undefined qualifiers like "materially" and "meaningful" renders most clauses unenforceable recommendations rather than binding law. |
| 4 | Architectural Fidelity | 4 | The principles align with a governed shell architecture, but the document does not specify how user-preference state is managed, leaving a minor gap. |
| 5 | Completeness | 2 | Defines principles but omits critical operational details, such as data schemas for settings, failure modes, or how these rules interact with mandatory audit policies. |
| 6 | Conflict Freedom | 2 | The ability to "disable logging" creates a major potential conflict with system-wide auditability requirements (e.g., in AIOS-SPEC-009), which is inadequately resolved by a vague "where policy permits" clause. |
| 7 | Practical Operability | 3 | The intent is clear, but the requirements are too high-level for a developer to implement without significant further specification and interpretation. |
| 8 | Style & Clarity | 4 | The document follows the basic structure and formatting of the Style Guide, but its overuse of "SHOULD" for core requirements obscures its binding authority. |
| 9 | Developer Synchrony | 2 | A developer would not be able to build from this document; it lacks the necessary schemas, event models, or clear policy hooks to be actionable. |
| 10 | Platform Economics Synchrony | 4 | The document does not create any direct economic conflicts, but it doesn't address the potential impact of disabling telemetry on usage-based metering or platform analytics. |
| 11 | Friction Factor | 4 | The controls it mandates add necessary implementation friction for the platform but are justified by the significant benefit to user trust and sovereignty. |
| | **Composite Score** | **3.1** | |

---

## Overall Assessment

### Strengths

- **Clear Principles:** The document establishes a strong, user-centric governing principle in Section 2 that correctly frames the need for transparency and control over platform-managed state.
- **Good Categorization:** Section 3 ("Required disclosure classes") and Section 4 ("Precision controls") provide a well-structured and comprehensive list of the state categories that must be made transparent and governable. This provides a solid foundation for a more detailed specification.

### Critical Gaps

- **Lack of Enforceable Language:** The document's primary failure is its reliance on "SHOULD" for requirements that are central to its purpose (e.g., Sections 2, 5, 6, 7). As written, it is a set of strong recommendations, not binding shell law. This makes it legally weak and would likely fail scrutiny in arbitration.
- **Undefined Qualifiers:** The use of ambiguous terms like "materially," "user-comprehensible," and "meaningful" without reference to a `PolicyRecord` or other quantitative threshold creates unenforceable loopholes. For a rule to be binding, its conditions must be testable.
- **Conflict with Auditability:** Section 4 allows users to "disable logging." This directly threatens the auditable, deterministic execution model mandated by `AIOS-SPEC-009`. The escape clause "where policy permits" is insufficient to resolve this fundamental conflict without more explicit rules defining what logging is non-negotiable for system integrity.

---

## Article-by-Article Review

### Section 2: Governing principle

**Feedback:** The principle is well-stated but uses "SHOULD," which immediately undermines the document's authority. A governing principle in a binding addendum must be a mandate. The qualifier "materially" is undefined.

**Scores:** Legal Enforceability: 2, Style & Clarity: 3

**Recommendation:** Change from a recommendation to a mandate and add a requirement to define the threshold for "materially."

**Proposed Text:**
> If a shell or surrounding runtime captures, infers, stores, or applies user-relevant state that materially affects behavior, the user **SHALL** be able to inspect and govern that state. The definition of "materially" **SHALL** be operationalized through thresholds defined in the active `PolicyRecord`.

### Section 3: Required disclosure classes

**Feedback:** This is a good list, but the opening sentence uses "SHALL disclose... whether the following classes are active when they materially exist." This again hinges on the undefined term "materially." The term "user-comprehensible surface" is also vague and should be tied to a defined component in the UI specification (`AIOS-SPEC-006`).

**Scores:** Legal Enforceability: 3, Practical Operability: 3

**Recommendation:** Tie the disclosure surface to a canonical UI component and require the `PolicyRecord` to define what constitutes a material existence for each class.

**Proposed Text:**
> The shell **SHALL** disclose, via a **documented component in the UI Component Registry Standard (AIOS-SPEC-006)**, whether the following classes are active. A class is considered active if its operation exceeds the minimum threshold defined for it in the active `PolicyRecord`.

### Section 4: Precision controls

**Feedback:** The core mandates in the first paragraph use "SHALL," which is excellent. However, the second paragraph detailing the minimum required distinctions reverts to "SHOULD," weakening the requirement. The potential conflict with mandatory audit logging is severe.

**Scores:** Conflict Freedom: 2, Legal Enforceability: 3

**Recommendation:** Upgrade the list of distinctions to a `SHALL` requirement. Add an explicit clause subordinating user choice to non-negotiable system audit requirements.

**Proposed Text:**
> At minimum, precision controls **SHALL** distinguish:
> ...
>
> **4.1 Overriding Policy:** User-configurable logging controls **SHALL NOT** override non-discretionary audit logging required for platform security, billing integrity, or governance enforcement as defined by `POL-AUDIT-001` (or equivalent). The shell **SHALL** disclose the existence of such non-discretionary logging.

### Section 5 & 6: Behavioral and guardrail settings / Inspectable signal use

**Feedback:** Both sections suffer from using "SHOULD" for their primary requirements. They describe laudable goals but fail to make them binding. This is a missed opportunity to formalize user sovereignty.

**Scores:** Legal Enforceability: 2

**Recommendation:** Convert all instances of "SHOULD" in these sections to "SHALL" to make the provisions for inspecting behavioral settings and inferred signals mandatory.

**Proposed Text (for Section 5):**
> Where a system exposes configurable behavior, the shell **SHALL** surface user-governable settings for...

**Proposed Text (for Section 6):**
> If the system infers user signals that affect pacing, tone, escalation, or safety posture, the shell **SHALL** disclose...

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 2, 5, 6, 7 | Weak Language | Replace all key instances of "SHOULD" with "SHALL" to make the document's principles binding and legally enforceable. | Critical | 3, 5, 7, 9 |
| 2 | 2, 3 | Undefined Qualifiers | Remove weasel words like "materially" and "meaningful," or require that they be defined by quantitative thresholds in a `PolicyRecord`. | Critical | 3, 7 |
| 3 | 4 | Conflict of Interest | Add a new subsection explicitly stating that user logging preferences cannot override mandatory system-level audit logging required for security and governance, and that this fact must be disclosed. | High | 6, 1 |
| 4 | 3 | Vague UI Reference | Change "user-comprehensible surface" to a specific, binding reference to a component defined in `AIOS-SPEC-006`. | Medium | 9, 7 |

---

## Final Verdict

**Disposition:** **major_revision_required**

**Rationale:** The document outlines excellent principles for user sovereignty but fails to make them legally enforceable due to pervasive use of "SHOULD" and undefined, ambiguous terms. Furthermore, it creates a potential conflict with core system auditability requirements without adequately resolving it.

**Top 3 Actions Required:**
1.  Strengthen the document by replacing all key instances of "SHOULD" with "SHALL," converting its principles into binding requirements.
2.  Explicitly subordinate user-configurable logging to non-discretionary system audit policies required by `AIOS-SPEC-009`, and mandate the disclosure of this limitation.
3.  Define all qualitative thresholds (e.g., "materially") by requiring them to be operationalized in a `PolicyRecord` to make the rules auditable and enforceable.