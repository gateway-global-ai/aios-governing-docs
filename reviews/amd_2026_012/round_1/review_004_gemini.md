---
review_id: REV-AMD-2026-012-004
document_reviewed: AMD-2026-012
document_version: 0.1.2
reviewer: Gemini
review_date: 2026-04-09
review_round: 1
review_type: legal
disposition: approved_with_changes
composite_score: 3.6
---

# Peer Review: AMD-2026-012 — Shell Authority and Voice-First Entry

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The document aligns well with core concepts from AMD-2026-007 and AIOS-SPEC-009 but needs to explicitly tie its state definitions to ratified objects. |
| 2 | Business Model Alignment | 4 | Section 9.4 correctly subordinates Kit discovery to the Shell, preserving the marketplace model, but is silent on the economic implications of this gatekeeping role. |
| 3 | Legal Enforceability | 3 | The use of subjective, undefined terms ("brief", "minimal") is a significant flaw, although partially mitigated by the promise of future definition in Section 8.4. |
| 4 | Architectural Fidelity | 4 | The concept of a single, governed entry point strongly reinforces the Technical Manifesto's principles of UI sovereignty and policy supremacy. |
| 5 | Completeness | 3 | The document defines Shell authority over the user experience but is missing authority over audit and economic disclosure, which are critical session concerns. |
| 6 | Conflict Freedom | 4 | It successfully subordinates Workspace surfaces (AMD-2026-005) and other skills, avoiding direct conflict by establishing a clear hierarchy. |
| 7 | Practical Operability | 3 | The rules are clear, but the dependency on a yet-to-be-written policy for UX thresholds (§8.4) makes day-one implementation a matter of interpretation. |
| 8 | Style & Clarity | 5 | The document adheres perfectly to the AIOS Style Guide, using precise, authoritative language and correct formatting. |
| 9 | Developer Synchrony | 3 | It provides strong conceptual guidance but lacks concrete schemas or control-plane contracts for the "finite family" of outcomes, leaving implementation details ambiguous. |
| 10 | Platform Economics Synchrony | 3 | The amendment correctly avoids defining economic mechanics but fails to acknowledge that Shell-led discovery (§9.4) is a powerful economic lever that needs governance. |
| 11 | Friction Factor | 4 | The rigid voice-first model is a deliberate, high-friction choice that aligns with the product vision; the rules themselves add minimal *unnecessary* friction. |
| | **Composite Score** | **3.6** | |

---

## Overall Assessment

### Strengths

This amendment provides a powerful and necessary framework for establishing the Shell as the locus of control for the user session. Its greatest strengths are:

*   **§4 Normative shell authority:** The definition of the Shell as the "single governed point of entry" and session authority is legally robust and critical for preventing architectural drift and fragmentation.
*   **§7 Shell-owned governed outcomes:** Establishing a "finite family" of outcomes is an exemplary governance pattern. It replaces ambiguity with a discrete, auditable set of states, which is highly enforceable.
*   **§12 Prohibited patterns:** This section creates a clear list of "negative covenants" that are unambiguous and directly enforceable against internal development and third-party Kits.

### Critical Gaps

The document's primary weakness lies in its reliance on subjective language for core operational mandates, which undermines its enforceability.

*   **Undefined Qualitative Terms:** Section 8 mandates behaviors that are "brief," "concise," and "minimal." Section 8.4 punts the definition of these terms to a future document. From a legal perspective, this is a "promise to agree" and makes the standard unenforceable until that subordinate document is ratified. This is the single most critical gap.
*   **Incomplete Session Authority:** The Shell's authority in Section 4.2 omits critical session concerns, namely the authority over initiating audit trails and presenting economic disclosures (e.g., per AIOS-SPEC-009 §15.4). A true session authority must govern these aspects.
*   **Ambiguous State Source:** Section 5.2 states the Shell should restore context for returning users from "governed session state," but this term is not precisely defined. It needs to be explicitly tied to ratified objects like the `SessionContext` from the control plane or a `PolicyRecord`.

---

## Article-by-Article Review

### §4. Normative shell authority

**Feedback:** This section is strong. The use of "solely" in §4.4 provides a clear, enforceable boundary against fallback drift. The concept of an "auditable" fallback is also excellent. However, the definition of the Shell's authority should be expanded to be fully complete.

**Scores:** Legal Enforceability: 4, Completeness: 3

**Recommendation:** In the table in Section 4.2, add rows for `Audit trail initiation` and `Economic disclosure` with the Shell authority marked as `Yes — presentation and timing`. This clarifies the Shell's role without making it responsible for the underlying economic calculations.

### §5. User entry classification

**Feedback:** The distinction between "new" and "returning" is a clear operational rule. The key strength is §5.3, which prevents tool state from overriding this primary classification. However, §5.2's reference to "governed session state" is legally imprecise.

**Scores:** Legal Enforceability: 3, Practical Operability: 4

**Recommendation:** Modify the text in Section 5.2 to be more specific:
**Old Text:** "...restoration of context from governed session state..."
**New Text:** "...restoration of context from governed session state, as defined by control-plane session records and continuity fields in the active PolicyRecord (per AIOS-SPEC-009)..."

### §7. Shell-owned governed outcomes (finite family)

**Feedback:** This is a model of good governance writing. The finite list is clear, and the informative boundary correctly separates primary UX outcomes from internal diagnostics. It provides a solid, enforceable foundation for the Shell's decision-making process.

**Scores:** Legal Enforceability: 5, Practical Operability: 5

**Recommendation:** No changes needed. This section is exemplary.

### §8. Voice-first interaction standard

**Feedback:** This is the document's weakest section from an enforceability standpoint. The terms "briefly," "one," "concisely," "minimize," and "lightweight" are all subjective. Section 8.4 acknowledges this but its solution—deferring to a future document—is insufficient. An unratified document has no legal weight, and until it exists, this entire section is legally void for vagueness.

**Scores:** Legal Enforceability: 2, Practical Operability: 2

**Recommendation:** Add a clause to Section 8.4 to establish binding, conservative defaults until the subordinate policy is ratified.
**Proposed addition to §8.4:** "Until such a subordinate document is ratified, implementations claiming conformance **SHALL** operate under the following interim thresholds: 'brief' and 'concise' acknowledgments **SHALL NOT** exceed 15 words or 5 seconds of speech; 'minimal' clarification **SHALL NOT** exceed two distinct choices; 'persistent explanatory text' **SHALL NOT** exceed 40 words on initial entry."

### §9. Skills and tools are subordinate

**Feedback:** This section establishes a clear and necessary hierarchy. §9.4 is particularly important, as it addresses how the marketplace model interacts with the Shell's authority. It correctly states that while the Shell may expose Kits, it must not invert the authority hierarchy. However, it completely ignores the economic implications.

**Scores:** Legal Enforceability: 5, Platform Economics Synchrony: 3

**Recommendation:** Add a sentence to the end of the informative note in Section 9.4.
**Proposed addition:** "The economic rules governing Kit discovery, listing, and promotion via the Shell **SHALL** be defined in the *Marketplace Terms*." This doesn't solve the problem but correctly assigns it to the appropriate commercial document.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §8.4 | Qualitative UX terms ("brief", "minimal") are legally unenforceable without defined thresholds. | Add an interim clause that defines conservative, numeric thresholds for these terms, which remain binding until a formal subordinate policy is ratified. | Critical | 3, 7, 9 |
| 2 | §4.2 | The list of Shell authorities is incomplete, omitting its role in audit and economic disclosures. | Add `Audit trail initiation` and `Economic disclosure` to the table of Shell authorities to make its session-governing role complete. | High | 5 |
| 3 | §5.2 | The term "governed session state" is vague and not tied to a specific, ratified source of truth. | Revise the text to explicitly link "governed session state" to control-plane records and the active `PolicyRecord` defined in AIOS-SPEC-009. | High | 1, 3 |
| 4 | §9.4 | The document acknowledges Shell-led Kit discovery but is silent on the economic governance of this function. | Add an informative note clarifying that the economic rules for Kit discovery are governed by the *Marketplace Terms* document. | Medium | 2, 10 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document provides a critical and well-structured definition of Shell authority that is essential for platform integrity. However, its reliance on subjective, undefined terms in Section 8 creates a major enforceability gap that must be closed before ratification.

**Top 3 Actions Required:**
1.  **Amend Section 8.4:** Implement the recommendation to add binding, interim numerical thresholds for all qualitative UX terms.
2.  **Amend Section 4.2:** Expand the definition of Shell authority to include its role in presenting audit and economic information.
3.  **Amend Section 5.2:** Make the source of "governed session state" legally precise by referencing specific objects like `PolicyRecord`.