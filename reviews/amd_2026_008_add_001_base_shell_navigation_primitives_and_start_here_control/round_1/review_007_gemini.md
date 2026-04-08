review_id: REV-AMD-2026-008-ADD-001-001
document_reviewed: amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md
document_version: 0.1.0
reviewer: Gemini
review_date: 2024-05-15
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 3.4
---

# Peer Review: Base Shell Navigation Primitives and Start-Here Control

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The document fits logically within the control-plane model of ADD-002 and correctly references its parent. |
| 2 | Completeness | 2 | It defines the navigation classes but critically omits state transitions, error/failure modes, and initial state definitions. |
| 3 | Practical Operability | 2 | The shell obligations in Section 5 are stated with subjective, unenforceable triggers, making them unauditable as written. |
| 4 | Conflict Freedom | 5 | No conflicts with the provided context documents were identified; it properly isolates its concerns from other addenda. |
| 5 | Style & Clarity | 4 | The document adheres well to the Style Guide but some definitions lack the legal precision required for governance. |
| | **Composite Score** | **3.4** | |

---

## Overall Assessment

This document establishes a sound and necessary principle: making user navigation a governed, deterministic function of the shell. Its structure is logical, and its separation of concerns from its sibling addendum (`ADD-002`) is clean and correct. The definition of the five navigation classes provides a solid foundation for this aspect of the shell control plane.

However, the document suffers from significant gaps in enforceability and completeness that prevent it from being ratifiable in its current form. The obligations placed upon the shell in Section 5 use vague, subjective language ("when ambiguity would cause mis-routing") that would be indefensible in arbitration. Furthermore, for a document that defines the primitives of a state machine, it completely omits rules for transitions between states and handling of invalid or failed navigation events. These omissions render the governance incomplete and the system's behavior under stress undefined.

### Strengths

- **Clear Separation of Concerns:** The document does an excellent job of defining its scope (navigation) and explicitly deferring related but distinct concerns (output depth, voice controls, packaging) to `ADD-002`, which aligns with the control-plane model presented in that document.
- **Strong Governing Principle:** Section 2 establishes a clear and appropriate normative line: navigation is a shell-governed function, not an emergent property of model behavior. This is a critical principle for a governed execution environment.
- **Logical Structure:** The use of tables to define navigation classes (Section 3) and map them to primitives (Section 4) is clear and follows the Style Guide.

### Critical Gaps

- **Unenforceable Obligations:** Section 5.1 contains a subjective trigger ("when ambiguity would cause mis-routing") that is not a measurable or auditable standard. A governing document must provide objective criteria for compliance.
- **Missing State Logic:** The document defines navigation *states* (classes) but fails to define the governed rules for *transitions* between them. It also omits any definition of failure modes (e.g., what happens on an invalid user choice) or error handling.
- **Insufficient Precision in Definitions:** Terms like "Initial orientation" for `START_HERE` are descriptive but lack the precision needed for a binding specification.

---

## Article-by-Article Review

### Section 2. Governing principle

**Feedback:** This section is strong. The distinction between navigation, output depth, and speech delivery is crucial and well-stated. It correctly establishes the normative line for this document.

**Scores:** Style & Clarity: 5, Practical Operability: 5

**Recommendation:** No changes needed.

### Section 3. Navigation classes

**Feedback:** The classes are logical, but their definitions could be tightened for legal precision. For example, `START_HERE`'s definition as "Initial orientation..." is a description of purpose, not a definition of a state. A more precise definition would focus on the system's posture.

**Scores:** Completeness: 3, Style & Clarity: 3

**Recommendation:** Refine the definitions to be more precise about the system's state or expected behavior.

*Proposed Text Change (for `START_HERE` definition):*
> **Initial state** of a user session or a recovery point following an unhandled error or explicit reset. The shell's primary function in this state is to establish context and present initial, valid pathways for user action.

### Section 4. Core primitives (mapping)

**Feedback:** The mapping is clear and correct. The note that an `Alert` must be distinguishable from other primitives is an important compliance point, especially for disclosures or warnings.

**Scores:** Cross-Document Consistency: 5, Style & Clarity: 5

**Recommendation:** No changes needed.

### Section 5. Shell obligations (navigation)

**Feedback:** This section contains the document's most critical flaws. The obligations are the legally binding portion, and they are currently unenforceable. The term "observable" is not defined, and "when ambiguity would cause mis-routing" is a classic weasel-word phrase that creates a compliance loophole. The auditability requirement is stated but not supported by any specific mechanism or standard.

**Scores:** Legal Enforceability: 1 (not in rubric, but my focus), Practical Operability: 2

**Recommendation:** Rewrite Section 5.1 to remove subjective language and replace it with a clear, deterministic rule. Define what "observable" and "auditable" mean in this context.

*Proposed Text Change (for Section 5.1):*
> 1. The shell **SHALL** expose the **active navigation class** and any associated constraints (e.g., the valid options for a **CHOOSE** class) through a designated field in the session state object, available to operator and audit surfaces.
> 2. For user-facing surfaces, the shell **SHALL** present affordances consistent with the active navigation class. For example, a **CHOOSE** class **SHALL** be accompanied by a rendered list of options, and a **SINGLE_INPUT** class **SHALL** be accompanied by an active input field or an open microphone state.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 5.1 | The obligation to make the navigation class "observable" is triggered by a subjective condition ("when ambiguity would cause..."). | Rewrite the obligation to be deterministic, requiring the shell to always expose the active navigation class to audit surfaces and render consistent UI affordances. | Critical | 3, 2 |
| 2 | N/A | The document defines navigation states but not the rules for transitions between them or how to handle invalid transitions/errors. | Add a new section defining the state transition logic, including how the shell handles user input that is inconsistent with the active navigation class (e.g., a free-form answer when in a `CHOOSE` state). | High | 2, 3 |
| 3 | 3 | The definitions for the navigation classes are descriptive rather than technically precise. | Refine the definitions to describe the system's required behavior or posture for each class, rather than just its purpose. | Medium | 5 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document requires a major revision because two key dimensions, Completeness and Practical Operability, scored a 2. The obligations on the shell are currently unenforceable, and the document is critically incomplete by omitting state transition and error handling logic, undermining its core purpose of creating a deterministic, governed navigation system.

**Top 3 Actions Required:**
1. **Rewrite Section 5:** Replace the subjective and unenforceable shell obligations with deterministic, auditable rules for how the navigation state is exposed and rendered.
2. **Add a State Transition Section:** Define the allowed transitions between navigation classes and specify the required behavior for handling invalid user actions or errors.
3. **Refine Definitions:** Tighten the definitions in Section 3 to be legally and technically precise, focusing on system state and behavior.