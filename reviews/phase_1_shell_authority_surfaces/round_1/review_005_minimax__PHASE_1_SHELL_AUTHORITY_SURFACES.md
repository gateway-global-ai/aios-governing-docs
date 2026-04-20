---
review_id: REV-PHASE1-SHELL-AUTHORITY-001
document_reviewed: reviews/aios_shell_governing_document_and_artifact_plan_001/phase_packets_2026-04-10/PHASE_1_SHELL_AUTHORITY_SURFACES.md
document_version: current draft
reviewer: MiniMax
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.5
---

# Peer Review: Phase 1 shell authority surfaces

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | Document uses shorthand references (AMD-2026-012) instead of full titles and specific Article/Section citations required by Style Guide |
| 2 | Business Model Alignment | 3 | No direct contradiction to marketplace model, but document is silent on economic implications of privileged shell access |
| 3 | Legal Enforceability | 2 | Lacks specific SLAs, timelines, or measurable thresholds; "identity-bound" and "administrative posture" are undefined terms used as if they were defined |
| 4 | Architectural Fidelity | 3 | Generally aligned with shell/planes separation but conflates "shell authority" with "shell surface mode" — these are different concepts per Technical Manifesto |
| 5 | Completeness | 3 | Authority matrix and denial tables present, but "shell disclosure map" promised in Required Phase Outputs is not actually provided as a formal artifact |
| 6 | Conflict Freedom | 3 | No direct contradiction found, but document acknowledges interim device-local authority is temporary without clear replacement timeline |
| 7 | Practical Operability | 2 | Provides conceptual tables but no step-by-step processes, CLI commands, or schema definitions a developer could implement from |
| 8 | Style & Clarity | 3 | Uses effective tables but violates Style Guide: uses "This phase" instead of Article/Section structure; lacks standard governance document preamble with defined terms |
| 9 | Developer Synchrony | 1 | No schemas, no CLI commands, no code examples; developers cannot implement from this document alone |
| 10 | Platform Economics Synchrony | N/A | Not applicable — document addresses authority governance, not economic mechanics |
| 11 | Friction Factor | 4 | Appropriately scoped as Phase 1 floor; minimal unnecessary process requirements |
| | **Composite Score** | **2.5** | |

---

## Overall Assessment

### Strengths

1. **Authority Matrix Structure** (Table: Authority matrix) — The explicit mapping of actor posture to allowed surfaces provides needed clarity. This is the core deliverable that Phase 1 should produce.

2. **Transition and Denial Rules Table** — Well-structured enum of shell surface transitions with current outcomes. This directly addresses the "explicit, identity-safe, reviewable" requirement from the Purpose section.

3. **Clear Interim Identification** — The document explicitly acknowledges interim device-local authority is temporary and defines the replacement seam. This prevents the common governance failure of treating interim solutions as permanent.

4. **Workspace Subordination** — The three-part safeguard (app.shell.* plane, workspace.* intent space, separate Workspace policy gate) correctly prevents domain planes from becoming alternate authority systems.

### Critical Gaps

1. **Missing Shell Disclosure Map** — The Required Phase Outputs section promises "a shell disclosure map defining what each surface must reveal to the user" but no such map is provided in the document body. This is a completeness failure.

2. **Undefined Terms Used as Defined** — Terms like "identity-bound administrator posture," "administrative elevation rule," and "reviewable administrative elevation rule" appear without definition. Per Style Guide: "Any new term must be defined in the document where it is introduced."

3. **No Implementation Schemas** — Developer Synchrony dimension scores 1 because no JSON schemas, TypeScript interfaces, or CLI commands are provided. The document references implementation evidence but doesn't define the contract itself.

4. **Cross-Reference format violates Style Guide** — References like "AMD-2026-012.md" and "specifications/IntentPrimitiveAndExecutionModel.md" lack full titles and specific Article/Section citations. Style Guide requires: "as defined in the Governance Constitution (Article II, Section 2)"

---

## Article-by-Article Review

### Purpose Section

**Feedback:** The stated gap ("whether that authority is explicit, identity-safe, reviewable, and bounded strongly enough") is correctly framed. However, the Purpose section should define its governance category — is this a Specification, an Amendment, or a Reference document? The naming convention ambiguity makes review difficult.

**Scores:** Completeness: 3, Style & Clarity: 2

**Recommendation:** Add a governance category declaration (e.g., "Document type: Reference — Shell Authority Baseline") in the preamble or convert to standard specification format with numbered sections.

---

### Authority Matrix Section

**Feedback:** This is the strongest section. The table correctly shows:
- Actor postures mapped to allowed surfaces
- Elevation rights explicit
- Notes about interim vs identity-bound distinction

However, the "future identity-bound admin role" row uses "to be defined" which is contradictory — if this is Phase 1, the future role belongs in a later phase, not in this phase's artifact.

**Scores:** Cross-Document Consistency: 3, Completeness: 4, Architectural Fidelity: 4, Practical Operability: 3

**Recommendation:** Remove the future identity-bound admin row or mark it explicitly as placeholder for Phase 2. Propose language:
> | future identity-bound admin role | [reserved for Phase 2+] | [reserved for Phase 2+] | target replacement seam | Requires separate amendment |

---

### Transition and Denial Rules Section

**Feedback:** The table correctly identifies that `set_surface_mode` is the only authority-gated navigation action. This aligns with shellNavigationApply.ts implementation evidence cited elsewhere.

However, "operatorEligible" and "developerEligible" are used as if they're defined concepts — they're not defined in this document or the glossary.

**Scores:** Legal Enforceability: 2, Practical Operability: 2

**Recommendation:** Either define the eligibility check functions or provide their interfaces as an appendix. At minimum, add to Required Phase Outputs: "eligibility interface definitions for operatorEligible and developerEligible"

---

### Shell-state vs shell-mode distinction

**Feedback:** This section correctly prevents category confusion — a common governance failure path. The separation of surface authority from ordinary modes is architecturally sound.

**Scores:** Architectural Fidelity: 4, Conflict Freedom: 4

**Recommendation:** This distinction should be formalized in a brief glossary section rather than buried in body text.

---

### Disclosure obligations Section

**Feedback:** The required disclosures are appropriate:
- Current shell surface mode
- Denied elevation attempts and reasons
- Interim vs identity-bound authority distinction
- Operator/developer surface entry
- Workspace subordination

**However:** The document promises a "shell disclosure map" in Required Phase Outputs but does not provide one. This is a completeness gap.

**Scores:** Completeness: 2 (promises map, doesn't deliver)

**Recommendation:** Replace the narrative disclosure section with an actual table format:
> | Surface Mode | Must Disclose | Disclosure Trigger | Failure Consequence |
> |--------------|-------------|------------------|-------------------|
> | operator | "elevated operator surface" | enter operator mode | N/A - always visible |
> | developer | "developer surface" | enter developer mode | N/A - always visible |
> | ... | | | |

---

### Workspace Subordinate Boundary Section

**Feedback:** Three-part safeguard is correct. This aligns with Technical Manifesto Article IV which states "Kits execute in a sandboxed environment with explicitly defined permissions."

**Scores:** Architectural Fidelity: 4, Conflict Freedom: 4

**Recommendation:** Add a cross-reference to Technical Manifesto Article IV to strengthen the architectural grounding.

---

### Immediate Remediation Direction Section

**Feedback:** Correctly identifies the minimum replacement path components (identity-bound admin, reviewable elevation rule, bounded launch/downgrade, audit record). This is Phase-appropriate — it defines the seam without over-specifying the solution.

**Scores:** Practical Operability: 2, Completeness: 3

**Recommendation:** Add specific placeholder text for where each component should be defined in future phases, to prevent gap creation.

---

### Required Phase Outputs Section

**Feedback:** This section lists outputs but critically fails to deliver the "shell disclosure map" it promises. This is the second-most-damaging gap in the document.

Outputs provided:
- ✓ Authority matrix - provided
- ✓ Transition and denial table - provided  
- ✗ Shell disclosure map - NOT provided (only narrative, no formal map)
- ✓ Subordinate-boundary note - provided
- ✓ Remediation note - provided

**Scores:** Completeness: 2

**Recommendation:** Either deliver the shell disclosure map or change the output description to "shell disclosure requirements (narrative)"

---

### Surface Requirements Section

**Feedback:** This section correctly translates governance intent into specific surface requirements. However, it repeats content already in previous sections without adding new value.

**Recommendation:** Consolidate surface requirements into the Authority Matrix section rather than duplicating.

---

### Acceptance Criteria Section

**Feedback:** The seven criteria correctly define completion conditions. However, Criterion 3 ("shell authority is kept separate from Workspace or other domain-execution authority") contradicts Criterion 6's concern about "privileged shell surface authority" — these are two different things being conflated.

**Scores:** Clarity: 3, Completeness: 4

**Recommendation:** Clarify that shell authority ≠ domain execution authority. Shell authority determines who can enter privileged surfaces; domain execution (workspace.*) determines what operations are permitted after entering.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Cross-References | Shorthand doc IDs violate Style Guide | Change "AMD-2026-012" to "Shell Authority and Voice-First Entry Amendment (AMD-2026-012)" and cite specific Article/Section | High | 1, 8 |
| 2 | Required Phase Outputs | Shell disclosure map promised but not delivered | Provide actual disclosure map table or revise description | Critical | 5 |
| 3 | Undefined Terms | operatorEligible, developerEligible, identity-bound admin not defined | Add glossary subsection defining all eligibility and role terms | High | 3, 7 |
| 4 | Developer Synchrony | No schemas, CLI commands, or implementation interfaces | Add appendix with minimal TypeScript interfaces for shellSurfaceMode, operatorEligible, and developerEligible | High | 9 |
| 5 | Authority Matrix | Row for "future identity-bound admin role" is placeholder | Remove placeholder row or mark explicitly as "reserved for Phase 2" | Medium | 5 |
| 6 | Document Type | Unclear governance category | Declare document type (Reference/Specification/Amendment) in preamble | Low | 8 |
| 7 | Criterion 6/3 | Conflation of shell authority vs domain execution | Clarify distinction between privileged surface access vs execution permissions | Medium | 4 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** Composite score 2.5 falls below the 3.0 threshold for "Approved with Changes." Two critical failures: (1) Shell disclosure map promised in Required Phase Outputs but not delivered, (2) Undefined terms used throughout without definition. Additionally, Developer Synchrony scores 1 — no implementable artifacts provided. At least two dimensions score 2 or below, triggering the "Major Revision Required" disposition rule.

**Top 3 Actions Required:**
1. **Deliver the Shell Disclosure Map** in table format or revise the Required Phase Outputs description
2. **Define all eligibility and role terms** in a glossary subsection (operatorEligible, developerEligible, identity-bound administrator)
3. **Add minimal TypeScript interfaces** as an appendix for developer implementability (surface mode enum, eligibility functions)

---

**Reviewer signature:** DeepSeek R1  
**Review round:** 1  
**Structural/Technical/Editorial:** technical