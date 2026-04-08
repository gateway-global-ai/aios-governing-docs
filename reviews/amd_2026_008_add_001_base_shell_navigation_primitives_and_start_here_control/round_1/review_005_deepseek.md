---
review_id: REV-AMD-2026-008-ADD-001-001
document_reviewed: AMD-2026-008-ADD-001
document_version: 0.1.0
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.6
---

# Peer Review: AMD-2026-008-ADD-001 — Base Shell Navigation Primitives and Start-Here Control

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Navigation classes are introduced but lack explicit mapping to AIOS-SPEC-009 intent lifecycle and session boundaries. |
| 2 | Business Model Alignment | 2 | No connection to MPOA commercial tiers or product gating for premium navigation features. |
| 3 | Legal Enforceability | 2 | "SHALL" statements are present but lack specific violation consequences or audit requirements. |
| 4 | Architectural Fidelity | 4 | Navigation classes align with separation of powers and shell control plane principles. |
| 5 | Completeness | 2 | Missing concrete examples, state transitions, error handling, and integration with session context. |
| 6 | Conflict Freedom | 4 | No direct contradictions with AMD-2026-008 or ADD-002, but potential overlap with AIOS-SPEC-009 session management. |
| 7 | Practical Operability | 2 | Navigation classes are abstract; no implementation guidance, JSON schemas, or testable criteria. |
| 8 | Style & Clarity | 3 | Follows style guide but lacks precision in defining "observable" and "governed pattern." |
| 9 | Developer Synchrony | 2 | No mapping to existing code in ai-os-voice-interface snapshot; navigation primitives appear disconnected from current shell implementation. |
| 10 | Platform Economics Synchrony | 1 | Completely silent on cost, resource allocation, or commercial implications of navigation features. |
| 11 | Friction Factor | 3 | Navigation classes could reduce model discretion but may add complexity if not properly integrated. |
| | **Composite Score** | **2.6** | |

---

## Overall Assessment

### Strengths

- **Clear separation of concerns**: Section 2 correctly distinguishes navigation from output depth and voice controls (ADD-002).
- **Architectural alignment**: Navigation classes (Section 3) support shell governance over model discretion, consistent with AMD-2026-008's sovereign runtime principles.
- **Minimalist structure**: The document avoids over-specification in areas properly delegated to other addenda.

### Critical Gaps

1. **Missing integration with AIOS-SPEC-009**: No reference to how navigation classes interact with intent lifecycle, session boundaries, or disclosure requirements.
2. **No implementation artifacts**: Lacks JSON schemas, state diagrams, or concrete examples that would make navigation classes implementable.
3. **Incomplete shell obligations**: Section 5's "observable" requirement is vague; no audit trail or violation handling specified.
4. **Economic blind spot**: No consideration of resource costs or commercial gating for advanced navigation features.

---

## Article-by-Article Review

### Section 3: Navigation classes

**Feedback:** The five navigation classes (START_HERE, CONTINUE, CHOOSE, SINGLE_INPUT, MULTI_INPUT) are conceptually sound but lack precise definitions. For example, what distinguishes "CONTINUE" from normal conversation flow? How does "MULTI_INPUT" differ from sequential SINGLE_INPUT operations? The table provides minimal descriptions that leave room for interpretation.

**Scores:** Architectural Fidelity: 4, Practical Operability: 2, Completeness: 2

**Recommendation:** Add a "State Transition" subsection showing how navigation classes relate to session states. Provide concrete examples:

```
**Example: CHOOSE → SINGLE_INPUT**
1. Shell presents options: "Do you want to (a) search calendar, (b) read email, or (c) create document?"
2. User selects (a) → navigation class becomes SINGLE_INPUT
3. Shell prompts: "What time range for calendar search?"
```

### Section 4: Core primitives (mapping)

**Feedback:** The mapping table is redundant with Section 3 and adds little value. "Alert" is introduced here but not in the navigation classes table, creating inconsistency. The statement that primitives "SHALL be realizable as shell affordances" is good but needs concrete manifestation requirements.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 3

**Recommendation:** Merge Section 4 into Section 3 or remove it. If "Alert" is a distinct primitive, add it to the navigation classes table with clear differentiation from CONTINUE. Specify minimum shell affordances:

```
**Shell affordance requirements:**
- CHOOSE: Must present discrete options via voice enumeration, visual list, or equivalent
- SINGLE_INPUT: Must provide clear input completion signal (e.g., "Go ahead" prompt)
- MULTI_INPUT: Must display captured fields and remaining required fields
```

### Section 5: Shell obligations (navigation)

**Feedback:** The three obligations are too vague. "Observable" needs definition: does this mean UI indicators, voice announcements, or both? "Auditability" references AIOS-SPEC-009 but doesn't specify what data must be logged. Missing: error handling for invalid navigation state transitions.

**Scores:** Legal Enforceability: 2, Practical Operability: 2, Developer Synchrony: 2

**Recommendation:** Replace with specific requirements:

```
**5.1 Observability requirement**
The active navigation class SHALL be indicated to the user through at least one of:
- Voice announcement when class changes (e.g., "Now choosing from options")
- Persistent visual indicator in shell chrome
- Explicit confirmation before proceeding (e.g., "Ready for your input")

**5.2 Audit trail**
For each navigation class change, the shell SHALL log:
- Previous and new navigation class
- Timestamp
- Trigger (user utterance, system event, timeout)
- Session ID (per AIOS-SPEC-009 §8.3)

**5.3 Error handling**
If the shell receives input incompatible with the active navigation class (e.g., free-form text during CHOOSE), it SHALL:
- Reject the input with clear error message
- Maintain the current navigation class
- Log the violation per Section 5.2
```

### Section 6: Non-goals

**Feedback:** Correctly delegates to ADD-002 but misses opportunity to reference AIOS-SPEC-009 for intent/session boundaries and AMD-2026-012 for shell authority principles.

**Scores:** Cross-Document Consistency: 3, Completeness: 3

**Recommendation:** Expand non-goals list:
```
- Intent lifecycle management (AIOS-SPEC-009 §4-6)
- Shell authority elevation (AMD-2026-012 §4)
- Workspace tool routing (AIOS-SPEC-007 §2)
- Local runtime lane selection (AMD-2026-008 §4)
```

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 3 | Navigation classes lack precision and examples | Add state transition diagram and concrete examples | Critical | 5,7,8 |
| 2 | Section 4 | Redundant and inconsistent with Section 3 | Merge into Section 3 or remove; clarify "Alert" primitive | High | 3,8 |
| 3 | Section 5 | Vague obligations unenforceable | Replace with specific observability, audit, and error handling requirements | Critical | 3,5,7,9 |
| 4 | Entire doc | Missing AIOS-SPEC-009 integration | Add cross-reference and alignment with intent lifecycle | High | 1,6,9 |
| 5 | Entire doc | No economic considerations | Add section on resource implications and commercial gating | Medium | 2,10 |
| 6 | Entire doc | No implementation artifacts | Add JSON schema for navigation state and test cases | High | 7,9 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has foundational architectural value but lacks the specificity, integration, and enforceability required for a governed addendum. Critical gaps in completeness (score 2), practical operability (score 2), and platform economics synchrony (score 1) mandate substantial revision before ratification.

**Top 3 Actions Required:**
1. **Integrate with AIOS-SPEC-009**: Define how navigation classes interact with intent lifecycle, session boundaries, and disclosure requirements.
2. **Specify enforceable shell obligations**: Replace vague "observable" and "auditability" with concrete requirements including UI indicators, audit logs, and error handling.
3. **Add implementation artifacts**: Provide JSON schemas, state diagrams, and testable criteria to make navigation classes implementable.