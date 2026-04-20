---
review_id: REV-AIOS-SHELL-AUTH-001
document_reviewed: reviews/aios_shell_governing_document_and_artifact_plan_001/phase_packets_2026-04-10/PHASE_1_SHELL_AUTHORITY_SURFACES.md
document_version: 1.0
reviewer: DeepSeek
review_date: 2026-04-09
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.9
---

# Peer Review: Phase 1 shell authority surfaces

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | References multiple governing documents but lacks explicit mapping to canonical terms and fails to cite specific Articles/Sections. |
| 2 | Business Model Alignment | 4 | Supports marketplace model by keeping Workspace subordinate and defining clear authority boundaries for shell control. |
| 3 | Legal Enforceability | 2 | Uses descriptive language rather than binding rules; lacks specific SLAs, liability boundaries, or defined terms for enforcement. |
| 4 | Architectural Fidelity | 3 | Generally aligns with Technical Manifesto but misses explicit connection to separation of powers and policy supremacy. |
| 5 | Completeness | 3 | Covers core authority surfaces but lacks JSON schemas, CLI commands, and specific implementation requirements. |
| 6 | Conflict Freedom | 4 | No direct contradictions with governing documents; respects Workspace subordination principle. |
| 7 | Practical Operability | 2 | Describes current state but lacks actionable rules, step-by-step processes, or specific thresholds for implementation. |
| 8 | Style & Clarity | 3 | Generally clear but uses first-person perspective in places and lacks proper heading hierarchy for a specification. |
| 9 | Developer Synchrony | 2 | Missing schemas, CLI references, and specific implementation guidance; developers wouldn't know what to build. |
| 10 | Platform Economics Synchrony | 4 | Correctly separates shell authority from economic mechanics; no contradictions with MPOA. |
| 11 | Friction Factor | 3 | Defines reasonable authority gates but lacks clarity on approval processes for future identity-bound authority. |
| | **Composite Score** | **3.0** | |

---

## Overall Assessment

### Strengths

1. **Clear separation of concerns**: The document correctly distinguishes shell surface authority from ordinary shell modes and subordinate Workspace views, preventing authority bypass paths.
2. **Evidence-based approach**: References actual implementation evidence from `ai-os-voice-interface`, grounding the discussion in real code.
3. **Transition planning**: Identifies the interim device-local authority model as temporary and defines a clear replacement seam for identity-bound authority.
4. **Workspace subordination**: Explicitly keeps Workspace as a subordinate controlled surface, preventing domain planes from becoming alternate authority systems.

### Critical Gaps

1. **Missing normative structure**: This reads as an analysis document, not a governing specification. It lacks Articles, Sections, and binding language.
2. **No schemas or interfaces**: Critical missing components include JSON schemas for authority envelopes, CLI commands for shell mode transitions, and API specifications.
3. **Incomplete disclosure requirements**: While disclosure obligations are mentioned, they lack specific format requirements, timing, and audit logging specifications.
4. **Vague acceptance criteria**: The "Acceptance criteria" section uses subjective language ("explicitly," "kept separate") rather than verifiable conditions.

---

## Article-by-Article Review

### Purpose Section

**Feedback:** The purpose is clear but framed as an internal planning document rather than a governing specification. It should be rewritten as a normative preamble establishing the document's authority and scope.

**Scores:** Architectural Fidelity: 3, Style & Clarity: 3

**Recommendation:** Rewrite as a formal Preamble: "This specification defines the shell authority model governing access to privileged shell surfaces within the Gateway Global AI Operating System (AIOS). It establishes the separation between shell surface authority, ordinary shell modes, and subordinate domain execution planes."

### Current Baseline Section

**Feedback:** This section effectively documents the current implementation state but should be moved to an Appendix. The normative specification should define requirements, not describe existing code.

**Scores:** Developer Synchrony: 2, Practical Operability: 2

**Recommendation:** Move implementation evidence to Appendix A. Replace with normative requirements: "The shell SHALL implement surface modes `primary`, `developer`, and `operator`. The shell SHALL route `app.shell.*` intents through the shell authority layer. The shell SHALL keep Workspace entry subordinate to shell control."

### Current Authority Sources Section

**Feedback:** The table is useful but presented as descriptive analysis. It should be reformatted as a normative specification of allowed authority sources with clear validation rules.

**Scores:** Architectural Fidelity: 3, Practical Operability: 2

**Recommendation:** Convert to a normative table with validation rules:

| Authority Source | Type | Validation Rule | Governance Status |
|---|---|---|---|
| URL launch flag (`?aios_operator=1`) | Session initialization | SHALL be validated at session start; SHALL NOT persist across sessions | Interim only |
| Browser unlock key | Device-local elevation | SHALL require explicit user action; SHALL be cryptographically signed | Interim only |
| Build-time opt-in | Development convenience | SHALL only be enabled in development builds; SHALL be disabled in production | Development only |

### Authority Matrix Section

**Feedback:** This is a good start but lacks the binding language of a specification. It should define "SHALL" requirements for each actor posture.

**Scores:** Cross-Document Consistency: 3, Legal Enforceability: 2

**Recommendation:** Rewrite as binding requirements:

**Section 3.1: Actor Postures and Permitted Surfaces**
- **Primary User**: SHALL be granted access to the `primary` shell surface. SHALL NOT request elevation to `developer` or `operator` surfaces.
- **Interim Developer-Eligible Session**: MAY request elevation to `developer` surface IF interim eligibility exists. SHALL NOT access `operator` surface without separate eligibility.
- **Interim Operator-Eligible Session**: MAY request elevation to `operator` surface IF interim eligibility exists. Operator eligibility SHALL imply developer eligibility.

### Transition and Denial Rules Section

**Feedback:** The table format is appropriate but needs binding language and specific error codes/messages for denial cases.

**Scores:** Practical Operability: 3, Developer Synchrony: 2

**Recommendation:** Add specific requirements:

**Section 4.2: Denial Response Format**
When a shell surface transition is denied, the system SHALL return a structured denial response:
```json
{
  "denied": true,
  "requested_surface": "operator",
  "current_surface": "primary",
  "reason": "insufficient_authority",
  "error_code": "SHELL_AUTH_001",
  "user_message": "Operator surface requires administrative approval..."
}
```

### Shell-state versus shell-mode distinction

**Feedback:** This critical distinction is well-articulated but buried in descriptive text. It should be elevated to a core principle with explicit validation rules.

**Scores:** Architectural Fidelity: 4, Conflict Freedom: 4

**Recommendation:** Create a new Section 2: "Core Principles" with:
- **Principle 1: Separation of Authority Planes**: Shell surface authority SHALL be distinct from ordinary shell mode changes and subordinate domain views.
- **Principle 2: Single Authority Gate**: Only `set_surface_mode` actions SHALL require authority validation; other shell state changes SHALL bypass authority checks.
- **Principle 3: Subordinate Domain Execution**: Domain planes (e.g., Workspace) SHALL remain subordinate to shell authority and SHALL NOT implement independent authority systems.

### Disclosure Obligations Section

**Feedback:** Mentions disclosure but lacks specific format, timing, and audit requirements. Should reference AIOS-SPEC-009 §12.2 explicitly.

**Scores:** Cross-Document Consistency: 2, Legal Enforceability: 2

**Recommendation:** Add specific disclosure requirements aligned with AIOS-SPEC-009:
- **Section 5.1: Surface Mode Disclosure**: The current shell surface mode SHALL be displayed in the `ShellIdentityBar` component.
- **Section 5.2: Elevation Attempt Logging**: Denied elevation attempts SHALL be logged with timestamp, requested surface, and denial reason.
- **Section 5.3: Interim Authority Warning**: When using interim device-local authority, the UI SHALL display: "Using device-local authority - not identity-bound."

### Workspace Subordinate Boundary Section

**Feedback:** Correctly identifies the critical boundary but needs explicit routing validation rules.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 5

**Recommendation:** Add validation rule: "The shell router SHALL validate that `workspace.*` intents originate from an already-authorized shell surface. Workspace SHALL NOT be accessible without first passing through shell authority validation."

### Immediate Remediation Direction Section

**Feedback:** Good planning content but should be moved to a "Future Considerations" appendix. The specification should focus on current requirements.

**Scores:** Style & Clarity: 3, Completeness: 3

**Recommendation:** Move to Appendix B: "Future Authority Model". The main specification should define current requirements only.

### Required Phase Outputs Section

**Feedback:** Lists deliverables but doesn't structure them as part of the specification itself. These should become the actual sections of the document.

**Scores:** Practical Operability: 2, Completeness: 2

**Recommendation:** Restructure the document to include these as actual sections:
- Section 6: Shell Authority Matrix (normative table)
- Section 7: Transition and Denial Rules (with JSON schemas)
- Section 8: Disclosure Requirements (specific UI components and messages)
- Section 9: Subordinate Boundary Enforcement (validation rules)

### Acceptance Criteria Section

**Feedback:** Uses subjective language ("explicitly," "kept separate") rather than verifiable conditions. Should reference specific sections that must exist.

**Scores:** Legal Enforceability: 2, Practical Operability: 2

**Recommendation:** Rewrite as verifiable conditions:
1. The specification SHALL define actor classes `primary_user`, `developer_eligible`, and `operator_eligible` in Section 3.
2. The specification SHALL define transition rules for all surface mode combinations in Section 4.
3. The specification SHALL require Workspace routing through shell authority in Section 9.
4. The specification SHALL define disclosure requirements in Section 5.
5. The specification SHALL identify interim authority sources as "development_only" in Appendix A.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Entire document | Descriptive rather than normative | Restructure as formal specification with Articles/Sections and binding "SHALL" language | Critical | 3, 5, 7, 8, 9 |
| 2 | Missing schemas | No JSON schemas for authority envelopes | Add schemas for `ShellAuthorityRequest`, `ShellAuthorityResponse`, `SurfaceTransitionDenial` | High | 5, 7, 9 |
| 3 | Disclosure requirements | Vague obligations without specific formats | Define exact UI components, messages, and audit logging requirements | High | 3, 5, 7 |
| 4 | Implementation guidance | Developers can't implement from this document | Add CLI commands, API endpoints, and validation pseudocode | High | 7, 9 |
| 5 | Cross-references | Missing explicit citations to governing docs | Add citations to AMD-2026-012 §4, AIOS-SPEC-009 §12.2, etc. | Medium | 1, 6 |
| 6 | Acceptance criteria | Subjective language | Rewrite as verifiable conditions referencing specific sections | Medium | 3, 5 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document contains valuable analysis and correctly identifies critical architectural boundaries, but it fails as a governing specification due to descriptive rather than normative language, missing schemas and implementation guidance, and vague acceptance criteria. Multiple dimensions score at or below 3, with Legal Enforceability and Developer Synchrony at critical 2 scores.

**Top 3 Actions Required:**
1. **Restructure as a formal specification** with binding "SHALL" language, proper Articles/Sections, and normative requirements rather than descriptive analysis.
2. **Add JSON schemas and implementation guidance** including CLI commands, API endpoints, and validation rules that developers can actually implement.
3. **Define specific disclosure requirements** with exact UI components, messages, and audit logging formats aligned with AIOS-SPEC-009 §12.2.