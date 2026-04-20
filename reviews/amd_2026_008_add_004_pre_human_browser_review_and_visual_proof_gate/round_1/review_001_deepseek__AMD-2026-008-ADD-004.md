---
review_id: REV-AMD-2026-008-ADD-004-001
document_reviewed: amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md
document_version: 0.2.0
reviewer: DeepSeek
review_date: 2026-04-08
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: AMD-2026-008-ADD-004 — Pre-Human Browser Review and Visual Proof Gate

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | Uses correct cross-references but lacks binding to AIOS-SPEC-006 (transparency) and AIOS-SPEC-009 (intent/execution model) for UI state verification. |
| 2 | Business Model Alignment | 2 | No connection to MPOA liability tiers or commercial SLAs for review delays; silent on cost of evidence capture. |
| 3 | Legal Enforceability | 2 | Missing specific SLAs, thresholds, and concrete failure definitions; "policy MAY" language creates optionality. |
| 4 | Architectural Fidelity | 4 | Correctly separates browser review from planning/execution planes; aligns with DCP separation of powers. |
| 5 | Completeness | 3 | Covers core concepts but lacks JSON schemas, concrete review target examples, and integration with CI/CD pipelines. |
| 6 | Conflict Freedom | 4 | No direct conflicts with referenced documents; respects ADD-001/002/003 boundaries. |
| 7 | Practical Operability | 2 | Vague on implementation: no concrete file paths, registry IDs, or tooling requirements; "policy SHALL define" deferrals. |
| 8 | Style & Clarity | 4 | Follows Style Guide; well-structured with clear tables; some definitions need tightening. |
| 9 | Developer Synchrony | 2 | No machine-readable schemas, no DCP transport definitions, no integration with existing governance CI. |
| 10 | Platform Economics Synchrony | 2 | Silent on resource costs for visual proof capture; no tie to tenant billing or resource quotas. |
| 11 | Friction Factor | 3 | Adds necessary gate but risks over-bureaucracy without clear proportionality rules. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- **Clear architectural separation:** Correctly positions browser review as a pre-approval phase distinct from planning and execution (Section 5.1).
- **Well-defined scope:** Section 3.1 provides concrete examples of UI-affecting changes that trigger the gate.
- **Good cross-referencing:** Properly references AMD-2026-008 family and related planning lifecycle (AIOS-AMD-PLAN-001).
- **Evidence integrity focus:** Section 8.5 correctly emphasizes that captures must be current and map to review targets.

### Critical Gaps

1. **Missing implementation bindings:** No concrete schemas, registry IDs, or DCP transport definitions (Section 6.1 defers everything to "policy SHALL define").
2. **No integration with existing governance stack:** Doesn't reference AIOS-SPEC-006 (transparency) or AIOS-SPEC-009 (intent/execution) for UI state verification.
3. **Vague enforcement:** Section 4.1 allows policy to "shape" minimum proof without clear guardrails; Section 7.2 test-captured proof constraints are complex and unverifiable.
4. **Economic blind spot:** No consideration of resource costs for visual proof capture or impact on development velocity.

---

## Article-by-Article Review

### Section 0.1 Definitions

**Feedback:** Definitions are generally clear but missing critical terms: "policy-equivalent governed surface" needs definition; "artifact_version" needs binding to git commit or DCP artifact ID. "Stale" vs "Current" definitions are good but need concrete time bounds or version-matching rules.

**Scores:** Architectural Fidelity: 4, Practical Operability: 2

**Recommendation:** Add definitions for "policy-equivalent governed surface" (e.g., "any renderable output surface governed by AIOS-SPEC-006") and "artifact_version" (e.g., "git commit hash or DCP artifact ID that uniquely identifies the build being reviewed"). Add a time-bound rule: "Evidence older than 24 hours from review date SHALL be considered stale unless explicitly frozen by policy."

### Section 4.1 Policy proportionality

**Feedback:** This section creates a dangerous loophole. "Policy MAY define risk classes that shape the minimum visual proof... without waiving §2" is contradictory—if policy can reduce minimums, it effectively waives §2. The "without waiving" clause is unenforceable.

**Scores:** Legal Enforceability: 1, Conflict Freedom: 2

**Recommendation:** Replace with: "Policy MAY define risk classes that determine which §7.1 proofs are required, but SHALL NOT reduce below the minimum set: (1) surface proof and (2) control proof for any UI-affecting change. Any reduction SHALL be recorded in the exception_state field per §11."

### Section 6.1 Required review target

**Feedback:** The table of fields is conceptually sound but completely unbound to implementation. "Normative field names in §6.1 are doctrine" but then immediately defers everything to "policy SHALL define." This creates a governance document that cannot be implemented without another document.

**Scores:** Developer Synchrony: 1, Practical Operability: 1

**Recommendation:** Add a normative JSON Schema in an appendix or reference a concrete implementation home (e.g., "SHALL conform to AIOS-OPS-021 BrowserReviewTargetV1 schema"). At minimum, provide a concrete example YAML with all required fields.

### Section 7.2 Acceptable forms / test-captured UI proof

**Feedback:** The triple-condition test-captured proof is overly complex and unverifiable. Condition (b) "test or harness is policy-approved or registered for the surface" creates circular dependency—policy needs to exist before tests can be approved, but policy needs tests to be approved. Condition (c) is redundant with §8.5.

**Scores:** Architectural Fidelity: 2, Practical Operability: 2

**Recommendation:** Simplify to: "Test-captured UI proof SHALL be acceptable only when: (1) the test is part of a governed test suite registered in the platform test registry (AIOS-OPS-0XX), and (2) the test produces human-auditable visual artifacts (screenshots, videos) that are preserved with the test results."

### Section 9.4 Remediation and exit from blocked states

**Feedback:** Provides reasonable paths but lacks concrete SLAs. "Policy MAY define SLAs" means there may be no SLAs, allowing indefinite blockage. The four paths are clear but need integration with existing governance workflows (e.g., how does "Resubmit" trigger a new review cycle?).

**Scores:** Practical Operability: 3, Business Model Alignment: 2

**Recommendation:** Add: "Policy SHALL define maximum remediation time (e.g., 72 hours) after which blocked states SHALL escalate to governance council review. Resubmission SHALL create a new review_slug with parent relationship to the original."

### Section 11 Audit posture

**Feedback:** Good field list but missing critical fields: `evidence_hashes` (for screenshot integrity), `reviewer_id`, and `next_review_date` (for periodic reviews). No binding to existing audit systems (AIOS-SPEC-003).

**Scores:** Architectural Fidelity: 3, Developer Synchrony: 2

**Recommendation:** Add fields: `evidence_hashes` (SHA-256 of visual proofs), `reviewer_id` (DCP actor ID), `parent_review_slug` (for resubmissions). Add: "Audit records SHALL be stored in the governed audit system per AIOS-SPEC-003 §8."

### Section 16 Informative external reference

**Feedback:** Correctly uses quarantine per AMD-2026-011 but doesn't specify what aspects of the reference are being studied. The quarantine record should reference specific patterns (e.g., "CI checks for UI changes") rather than the entire repo.

**Scores:** Cross-Document Consistency: 4, Completeness: 3

**Recommendation:** Add: "Study focus: CI-driven UI validation patterns and screenshot comparison workflows. Promotion beyond quarantine SHALL require analysis of license compatibility and dependency review per AIOS-SPEC-013 §3."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | 4.1 | Policy proportionality creates unenforceable loophole | Replace with guarded reduction rule requiring surface+control proof minimum | Critical | 3, 6 |
| 2 | 6.1 | No implementation binding; all deferred to policy | Add normative JSON Schema reference or concrete example YAML | Critical | 7, 9 |
| 3 | 7.2 | Overly complex test-captured proof conditions | Simplify to require governed test suite registration | High | 4, 7 |
| 4 | 0.1 | Missing concrete definitions for key terms | Add definitions for "policy-equivalent surface" and "artifact_version" with time bounds | High | 7, 8 |
| 5 | 9.4 | No SLAs for remediation; indefinite blockage possible | Require policy to define maximum remediation time with escalation path | Medium | 2, 7 |
| 6 | 11 | Missing critical audit fields and system integration | Add evidence_hashes, reviewer_id; bind to AIOS-SPEC-003 audit system | Medium | 4, 9 |
| 7 | Entire doc | No economic consideration of proof capture costs | Add section on resource quotas and tie to tenant billing | Low | 2, 10 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** Composite score of 2.8 with critical dimensions (Legal Enforceability, Practical Operability, Developer Synchrony) at 2 or below. The document establishes sound principles but lacks concrete implementation bindings, creating unenforceable "policy SHALL define" deferrals.

**Top 3 Actions Required:**
1. **Fix the policy proportionality loophole** in Section 4.1 with concrete minimum proof requirements.
2. **Add implementation bindings** - either normative JSON schemas or references to concrete operations standards.
3. **Simplify test-captured proof rules** in Section 7.2 to be verifiable and implementable.