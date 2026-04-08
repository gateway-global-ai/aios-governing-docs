---
review_id: REV-AMD-2026-008-ADD-003-001
document_reviewed: AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
document_version: 0.14.5
reviewer: DeepSeek
review_date: 2026-04-10
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 3.2
---

# Peer Review: AMD-2026-008-ADD-003 — Composition Control Plane for Messages, Invites, and Documents

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | Strong alignment with ADD-001/ADD-002 seams, but §16.7 language control vs depth/VC boundary needs clearer separation of concerns. |
| 2 | Business Model Alignment | 3 | Professional-use disclosure (§9.4) and premium BOOK gates reference MPOA but lack specific liability boundary language for measurement accuracy claims. |
| 3 | Legal Enforceability | 3 | §19 originality gate has strong enforcement posture but §17.7 measurement accuracy disclaimer creates potential conflict with MPOA liability allocations. |
| 4 | Architectural Fidelity | 2 | Composition contract (§5) lacks concrete JSON schema or DCP binding; §5.9 fail-closed table references OPS-020 but doesn't define composition-plane validation mechanics. |
| 5 | Completeness | 4 | Covers all twelve axes comprehensively, but §18 knowledge basis implementation lacks concrete state machine for discovery-before-creation workflows. |
| 6 | Conflict Freedom | 4 | No direct contradictions with other documents, but §20 reference adherence at level 10 creates tension with §19 originality thresholds. |
| 7 | Practical Operability | 3 | Many conceptual fields lack implementation mapping; §19.10 implementation handoff defers too much to OPS-020 without defining composition-plane integration points. |
| 8 | Style & Clarity | 3 | Document is overly dense; §5 composition contract could use clearer examples; §18.11 sequence diagram would help operational understanding. |
| 9 | Developer Synchrony | 3 | References product implementation snapshot but doesn't define how composition classes map to existing intent registry or workspace control plane. |
| 10 | Platform Economics Synchrony | 4 | Clear premium BOOK gates and professional-use disclosure align with MPOA commercial tiers, but measurement liability gap remains. |
| 11 | Friction Factor | 3 | Twelve-axis control plane creates cognitive load; §5.9 fail-closed semantics need clearer escalation paths for developers. |
| | **Composite Score** | **3.2** | |

---

## Overall Assessment

### Strengths

1. **Comprehensive twelve-axis model** (§6) provides complete coverage of composition control plane dimensions with clear ownership boundaries between ADD-001, ADD-002, and ADD-003.
2. **Strong originality enforcement posture** (§19.2-§19.5) establishes mandatory verification states and channel-based thresholds with clear fail-closed semantics.
3. **Clear professional-use disclosure framework** (§9.4) defines three levels of assistance and mandatory disclosure text with export preservation requirements.
4. **Well-defined addendum seams** (§2.1) prevents overlap with navigation, depth, and voice control domains owned by other addenda.

### Critical Gaps

1. **Missing composition contract validation mechanics** (§5.9) references OPS-020 for originality but doesn't define how composition contract fields are validated or how validation failures propagate through DCP.
2. **Measurement accuracy liability conflict** (§17.7) disclaimer creates tension with MPOA commercial terms without clear reconciliation mechanism.
3. **Implementation handoff deferral** (§19.10) pushes too much implementation detail to OPS-020 without defining composition-plane integration points or state transition requirements.
4. **Overly dense structure** makes the document difficult to implement; needs clearer operational sequences and state machines.

---

## Article-by-Article Review

### §5 Composition Contract Requirements

**Feedback:** The triad (role, intent, outcome) is conceptually sound but lacks concrete validation mechanics. §5.9 fail-closed table references OPS-020 for originality but doesn't define how composition contract validation failures (missing role/intent/outcome) should be signaled in DCP. The scaffold-only boundary (§5.4) needs clearer state transitions: what triggers scaffold vs full draft? How does the system know when contract is "satisfied"?

**Scores:** Architectural Fidelity: 2, Practical Operability: 3, Developer Synchrony: 2

**Recommendation:** Add explicit validation state machine and DCP codes for composition contract failures. Proposed addition to §5.9:

```
**Composition contract validation states:**
- `contract_pending` - Contract fields not yet collected/validated
- `contract_partial` - Some fields present but insufficient for Class 3
- `contract_satisfied` - All required fields present and valid
- `contract_invalid` - Fields present but contradictory or impossible

**DCP codes for composition contract failures (namespace `aios.dcp.composition`):**
- `COMP_CONTRACT_MISSING_ROLE` - Required role field missing
- `COMP_CONTRACT_MISSING_INTENT` - Required intent field missing  
- `COMP_CONTRACT_MISSING_OUTCOME` - Required outcome field missing
- `COMP_CONTRACT_INCONSISTENT` - Fields contradictory (e.g., role=founder but intent=legal_advice)
```

### §17 Measurement Contract and Quantified Claims

**Feedback:** §17.7 creates a liability gap: "They do not warrant or guarantee the factual accuracy of any number... Commercial terms, remedies, and liability for reliance on generated content SHALL be governed exclusively by MPOA." This creates tension because §17 imposes procedural requirements but disclaims accuracy, while MPOA may allocate liability differently. Need clearer boundary between procedural compliance (governance) and factual accuracy (commercial).

**Scores:** Legal Enforceability: 2, Business Model Alignment: 2, Conflict Freedom: 3

**Recommendation:** Clarify that §17 procedural requirements are governance obligations, while accuracy warranties and liability are MPOA matters. Add explicit cross-reference to MPOA Article for measurement liability. Proposed revision to §17.7:

```
**17.7 Accuracy, Reliance, and MPOA Integration**
The obligations in §17 define **procedural governance requirements** for quantified claims and measurements. Compliance with §17 **does not constitute** a warranty of factual accuracy. **Commercial terms**, **remedies for inaccuracy**, and **liability allocation** for reliance on generated measurements **SHALL** be governed exclusively by **[MPOA](../core/master_platform_operating_agreement.md)** Article [X] (Measurement and Data Accuracy) and applicable product agreements. Implementations **SHALL** record §17 compliance (method, unit, basis confirmation) separately from accuracy warranties to enable audit trail alignment with MPOA terms.
```

### §19 Originality and Source-Boundary Verification

**Feedback:** Strong enforcement posture but §19.10 implementation handoff defers too much to OPS-020. The composition plane needs to define: (1) when originality verification is triggered (which artifact classes, which release paths), (2) how verification state integrates with composition workflow state machine, (3) what happens during verification (blocking vs non-blocking), (4) how verification results are stored with artifact metadata.

**Scores:** Architectural Fidelity: 3, Practical Operability: 2, Developer Synchrony: 3

**Recommendation:** Define composition-plane integration points before deferring to OPS-020. Add to §19.2:

```
**19.2.1 Verification Trigger Conditions**
Originality verification SHALL be triggered when ALL of the following are true:
1. Artifact is Class 3 (§4.3) OR policy requires verification for the artifact class
2. Release path is publish, send, or formal export (§19.2)
3. Artifact has source-derived content (knowledge-base, uploaded files, reference documents)
4. Channel is EXTERNAL per OPS-020 §3 (or policy defines equivalent external-facing path)

**19.2.2 Workflow Integration**
Verification SHALL be non-blocking for draft composition but SHALL block release actions (publish/send/export) until verification completes with permitted state (§19.5). The composition workflow SHALL maintain `originality_verification_state` as part of artifact metadata, synchronized with OPS-020 evaluation records via artifact_id.
```

### §20 Reference-Guided Composition

**Feedback:** §20.14 correctly states that maximum adherence doesn't bypass §19 originality thresholds, but creates implementation tension: how can system achieve "exact layout conformity" (level 10) while avoiding "verbatim content" reproduction? Need clearer guidance on what constitutes "structure" vs "content" for adherence controls.

**Scores:** Architectural Fidelity: 3, Conflict Freedom: 3, Practical Operability: 3

**Recommendation:** Define structural elements separately from content elements for adherence controls. Add to §20.14:

```
**20.14.1 Structural vs Content Elements**
For adherence controls, structural elements SHALL include: section order, heading hierarchy, document anatomy, formatting logic, boilerplate placement. Content elements SHALL include: specific phrasing, sentence construction, proprietary text blocks, factual assertions. Level 10 adherence authorizes close conformity to structural elements only; content elements remain subject to §19 originality verification regardless of adherence level.

**20.14.2 Implementation Guidance**
Implementations SHALL separate reference analysis into:
1. Structural template extraction (headings, sections, formatting patterns)
2. Content analysis for originality verification (§19)
3. Adherence application to structural template only
This separation ensures high structural fidelity without content reproduction risk.
```

### §18 Knowledge Basis and Discovery Gating

**Feedback:** §18 defines conceptual states but lacks concrete state machine for discovery-before-creation workflows. §18.11 sequence is helpful but needs explicit transition conditions and error handling. How does system move from `insufficient` to `partial` to `sufficient`? What triggers discovery vs scaffold?

**Scores:** Architectural Fidelity: 3, Practical Operability: 3, Completeness: 3

**Recommendation:** Add explicit state machine with transition conditions. Proposed addition to §18:

```
**18.12 Knowledge Workflow State Machine**
States: `pending_assessment` → `assessing` → `sufficient` | `partial` | `insufficient` | `stale` | `conflicted` | `unverified`

Transitions:
- `pending_assessment` → `assessing`: When artifact composition begins and knowledge basis check required
- `assessing` → `sufficient`: All required knowledge sources available and current
- `assessing` → `partial`: Some sources missing but policy allows partial drafting
- `assessing` → `insufficient`: Critical sources missing; scaffold-only required
- `partial` → `sufficient`: Missing sources provided via discovery
- Any state → `stale`: Source freshness check fails (policy-defined TTL)
- `sufficient` → `conflicted`: Inconsistent sources detected

**18.13 Discovery Trigger Conditions**
Discovery SHALL be triggered when:
1. Knowledge state is `partial`, `insufficient`, or `stale`
2. AND artifact class requires discovery per §18.10 tier
3. AND workflow allows discovery (not time-critical response)
Discovery MAY be automated (search KB, check current state) or manual (user query) per policy.
```

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | §5.9 | Missing composition contract validation mechanics | Add validation state machine and DCP codes for contract failures | Critical | 4, 7, 9 |
| 2 | §17.7 | Measurement accuracy liability conflict with MPOA | Clarify procedural vs accuracy boundaries; add MPOA cross-reference | High | 2, 3, 6 |
| 3 | §19.10 | Implementation handoff defers too much to OPS-020 | Define composition-plane integration points before deferral | High | 4, 7, 9 |
| 4 | §20.14 | Tension between adherence level 10 and originality | Separate structural vs content elements for adherence controls | Medium | 4, 6, 7 |
| 5 | §18 | Missing knowledge workflow state machine | Add explicit states, transitions, and discovery triggers | Medium | 4, 5, 7 |
| 6 | Document structure | Overly dense; hard to implement | Add operational sequence diagrams and state machines | Low | 8, 11 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** While the document establishes a comprehensive twelve-axis composition control plane, critical architectural gaps in validation mechanics (§5), liability boundaries (§17), and implementation integration (§19) prevent practical operability. The composite score of 3.2 reflects these substantive issues that must be addressed before ratification.

**Top 3 Actions Required:**
1. Define concrete validation mechanics and DCP codes for composition contract failures (§5.9)
2. Resolve measurement accuracy liability conflict with MPOA integration (§17.7)
3. Specify composition-plane integration points for originality verification before deferring to OPS-020 (§19.10)