---
review_id: REV-AMD-2026-008-ADD-001-001
document_reviewed: AMD-2026-008-ADD-001
document_version: 0.1.0
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: AMD-2026-008-ADD-001 — Base Shell Navigation Primitives and Start-Here Control

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Navigation classes correctly reference ADD-002 for output depth, but missing explicit linkage to AIOS-SPEC-009 session boundaries. |
| 2 | Business Model Alignment | 3 | No direct conflict with MPOA, but lacks commercial hooks for premium navigation features or tier differentiation. |
| 3 | Legal Enforceability | 2 | Primitives are descriptive but lack binding implementation requirements or verification mechanisms. |
| 4 | Architectural Fidelity | 2 | Navigation classes are abstract without mapping to DCP pipeline, session state, or deterministic execution paths. |
| 5 | Completeness | 2 | Missing critical sections: state transitions, error handling, session recovery, and concrete JSON schemas for navigation context. |
| 6 | Conflict Freedom | 5 | No contradictions found with AMD-2026-008, ADD-002, or other governing documents. |
| 7 | Practical Operability | 2 | Navigation classes are too abstract; developers cannot implement without additional specification of how shell maps user input to classes. |
| 8 | Style & Clarity | 4 | Follows Style Guide conventions, but some sections are overly terse and lack illustrative examples. |
| 9 | Developer Synchrony | 2 | No alignment with existing product implementation; no references to current shell capabilities or migration path. |
| 10 | Platform Economics Synchrony | 3 | Neutral impact on economics, but misses opportunity to define commercial navigation features. |
| 11 | Friction Factor | 3 | Navigation classes could reduce model improvisation, but abstract definitions may increase implementation friction. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- **Clear separation of concerns:** Correctly distinguishes navigation from output depth and voice controls (Section 2), aligning with ADD-002's control-plane model.
- **Consistent terminology:** Uses defined terms like "shell affordances" and references parent amendment correctly.
- **Minimalist structure:** Gets straight to the point without unnecessary elaboration.

### Critical Gaps

1. **Missing architectural integration:** No connection to AIOS-SPEC-009 session model or DCP pipeline for navigation state management.
2. **Incomplete state machine:** Navigation classes lack defined transitions, error states, and recovery mechanisms.
3. **No implementation schemas:** Absence of JSON schemas for navigation context makes the specification unimplementable.
4. **Weak shell obligations:** Section 5 is descriptive rather than prescriptive, lacking specific "SHALL" requirements for implementation.

---

## Article-by-Article Review

### Section 3: Navigation classes

**Feedback:** The five navigation classes (START_HERE, CONTINUE, CHOOSE, SINGLE_INPUT, MULTI_INPUT) are conceptually sound but lack architectural grounding. Each class should map to specific session state transitions in the DCP pipeline. The distinction between SINGLE_INPUT and MULTI_INPUT is clear, but CONTINUE vs START_HERE needs more precise boundary conditions.

**Scores:** Architectural Fidelity: 2, Practical Operability: 2

**Recommendation:** Add a table mapping each navigation class to:
1. Required session context (e.g., START_HERE requires no active thread)
2. Allowed transitions (e.g., CHOOSE → SINGLE_INPUT)
3. DCP pipeline stage where navigation class is resolved
4. Example user utterances that trigger each class

### Section 4: Core primitives (mapping)

**Feedback:** The mapping from primitives to navigation classes is helpful but incomplete. The "Alert" primitive is problematic—it's described as interruptive but lacks governance around priority escalation or policy overrides. The primitives should be defined as shell API endpoints with input/output contracts.

**Scores:** Architectural Fidelity: 2, Legal Enforceability: 2

**Recommendation:** Replace the current table with a formal specification:
1. Define each primitive as a shell API method with JSON schema for parameters
2. Specify error conditions (e.g., what happens if CHOOSE is called with empty options)
3. Add "Recover" primitive for session restoration after errors
4. Clarify that "Alert" must respect user's "do not disturb" settings and session priority

### Section 5: Shell obligations (navigation)

**Feedback:** This section is too weak for a governing document. "Observable" is not defined. "Auditability" references AIOS-SPEC-009 but doesn't specify what must be logged. The shell obligations should be specific requirements with verification criteria.

**Scores:** Legal Enforceability: 1, Practical Operability: 2

**Recommendation:** Rewrite as binding requirements:
1. "The shell SHALL expose the active navigation class through the session context API (see AIOS-SPEC-009 §8.3)."
2. "Navigation state transitions SHALL be logged to the audit trail with timestamp, previous class, new class, and triggering input."
3. "The shell SHALL prevent navigation class transitions that violate the state machine defined in Appendix A."
4. "Multi-tenant deployments SHALL isolate navigation state per tenant session."

### Missing: State transitions and error handling

**Feedback:** The document completely omits how navigation classes transition, what happens on errors, and how sessions recover from invalid states. This is a critical gap for deterministic execution.

**Scores:** Completeness: 1, Architectural Fidelity: 1

**Recommendation:** Add a new Section 6: "Navigation State Machine" with:
1. State diagram or table of allowed transitions
2. Error states (NAVIGATION_ERROR, RECOVERY_NEEDED)
3. Recovery primitives (RESET_TO_START_HERE, CONTINUE_FROM_LAST_VALID)
4. Timeout handling for stuck states

### Missing: Implementation schemas

**Feedback:** Without JSON schemas, developers cannot implement interoperable navigation systems. The navigation context should be a defined data structure passed through the DCP.

**Scores:** Developer Synchrony: 1, Practical Operability: 1

**Recommendation:** Add Appendix A: "Navigation Context Schema" with:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "NavigationContext",
  "type": "object",
  "properties": {
    "navigation_class": {
      "type": "string",
      "enum": ["START_HERE", "CONTINUE", "CHOOSE", "SINGLE_INPUT", "MULTI_INPUT"]
    },
    "session_id": {"type": "string"},
    "thread_id": {"type": "string"},
    "previous_class": {"type": "string"},
    "transition_reason": {"type": "string"},
    "input_expected": {"type": "boolean"},
    "options": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Required for CHOOSE class"
    }
  },
  "required": ["navigation_class", "session_id"]
}
```

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 3 | Navigation classes lack architectural mapping | Add table mapping classes to session context, transitions, and DCP pipeline stage | Critical | 4, 5, 7 |
| 2 | Section 4 | Primitives are abstract without API contracts | Define as shell API methods with JSON schemas and error handling | Critical | 3, 4, 7 |
| 3 | Section 5 | Shell obligations are weak and unenforceable | Rewrite as specific "SHALL" requirements with verification criteria | High | 3, 7, 9 |
| 4 | Missing | No state machine or error handling | Add Section 6 with state transitions, error states, and recovery primitives | Critical | 4, 5, 7 |
| 5 | Missing | No implementation schemas | Add Appendix A with NavigationContext JSON schema | High | 7, 9 |
| 6 | Missing | No alignment with product implementation | Add reference to current shell capabilities and migration path | Medium | 9, 10 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document has fundamental gaps in architectural integration, implementation specificity, and completeness. With scores of 2 in Architectural Fidelity, Completeness, Practical Operability, and Developer Synchrony, it cannot be approved in its current form.

**Top 3 Actions Required:**
1. Define the navigation state machine with allowed transitions and error handling (Section 6).
2. Provide JSON schemas for navigation context and shell API primitives (Appendix A).
3. Strengthen shell obligations to specific "SHALL" requirements with verification mechanisms (Section 5 rewrite).