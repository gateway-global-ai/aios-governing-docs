---
review_id: REV-AMD-2026-006-001
document_reviewed: AMD-2026-006
document_version: 0.1.0
reviewer: DeepSeek
review_date: 2026-04-07
review_round: 1
review_type: technical
disposition: major_revision_required
composite_score: 2.5
---

# Peer Review: Amendment: Google Workspace Governed Integration Plane

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | References AMD-2026-005 but fails to incorporate its workspace/workflow model and deterministic failure policy for governed intents. |
| 2 | Business Model Alignment | 3 | Supports marketplace by governing third-party integrations, but lacks explicit vendor/enterprise adoption language. |
| 3 | Legal Enforceability | 2 | Lacks specific liability boundaries, SLAs, and weasel words like "MUST comply" without defined consequences. |
| 4 | Architectural Fidelity | 2 | Fails to detail the separation of powers (Intent Layer vs Control Plane vs MCP) and omits stateless compute requirements. |
| 5 | Completeness | 1 | Missing entire sections: no normative scope taxonomy, routing schemas, audit requirements, or phased rollout details. |
| 6 | Conflict Freedom | 3 | No direct contradictions, but creates tension by referencing unratified SPEC-007 without clear precedence rules. |
| 7 | Practical Operability | 2 | No step-by-step processes, specific thresholds, or actionable guidance for developers to implement. |
| 8 | Style & Clarity | 4 | Follows Style Guide structure and voice, but uses vague references like "Phase 1 read plane" without definition. |
| 9 | Developer Synchrony | 2 | Lacks JSON schemas, CLI commands, and concrete examples needed for implementation. |
| 10 | Platform Economics Synchrony | 3 | Implicitly aligns with thin-slice model but omits explicit 2x multiplier rules for external intelligence calls. |
| 11 | Friction Factor | 4 | Proposes lean governance with intent routing, avoiding excessive bureaucracy. |
| | **Composite Score** | **2.5** | |

---

## Overall Assessment

### Strengths

1. **Clear Rationale:** Section 1 effectively states the problem of "unbounded execution risk" from direct MCP exposure.
2. **Structural Alignment:** Follows the amendment template with Rationale, Proposed Changes, Cross-Document Impact, and Ratification Requirements.
3. **Friction Awareness:** Demonstrates understanding of minimizing unnecessary gates (Score 4 in Friction Factor).

### Critical Gaps

1. **Missing Normative Content:** The amendment lacks the binding technical schemas, scope classes, and routing contracts required to govern the integration plane. It references AIOS-SPEC-007 but does not itself define the rules.
2. **Architectural Vagueness:** Fails to specify how the "Intent Layer → Workspace Intent Router → Integration Control Plane → MCP Adapter" chain enforces separation of powers and stateless compute.
3. **Incomplete Cross-Document Impact:** Does not address how this amendment changes the affected documents (AIOS-SPEC-003, AIOS-SPEC-006) with specific text modifications.

---

## Article-by-Article Review

### Section 1: Rationale

**Feedback:** The rationale correctly identifies the risk but is purely descriptive. It references "Layer 1 governance scope classes" and "Layer 2 operational intents" which are undefined terms in this document. It assumes the reader has internal knowledge of SPEC-007.

**Scores:** Architectural Fidelity: 2, Completeness: 2, Style & Clarity: 3

**Recommendation:** Incorporate a concise, normative definition of the layered model directly into the amendment. Add a footnote or inline definition for "Layer 1" and "Layer 2" as per the intended taxonomy in SPEC-007.

**Proposed Text Addition to Section 1:**
```
...with **Layer 1** governance scope classes (e.g., `workspace.google.read`, `workspace.google.write`) defining the permission plane and **Layer 2** operational intents (e.g., `workspace.mail.search`) mapping one-to-one to a scope class, as defined in the authoritative schema in Annex A of this amendment.
```

### Section 2: Proposed Changes

**Feedback:** This section is a list of effects without the actual normative changes. It states "Effect:" but does not provide the text to insert into the affected documents. It does not define the `workspace.*` intent schema for AIOS-SPEC-003 or the canvas surface registration for AIOS-SPEC-006.

**Scores:** Completeness: 1, Developer Synchrony: 1, Practical Operability: 1

**Recommendation:** Transform each "Change" into a proper amendment directive with "Old Text" / "New Text" redlines for the affected documents. For Change 2, provide the exact JSON schema for `workspace.*` intents to be added to AIOS-SPEC-003 §7.

**Proposed Structure for Change 2:**
```
**Change 2: Extend AIOS-SPEC-003 with Governed Workspace Intents**

**Affected Document:** AIOS-SPEC-003 §7 (Governed Intent Emission Contract)

**Old Text:** [Quote the current section header or a relevant placeholder]

**New Text:**
### 11. Google Workspace Governed Intents
[Insert the full normative text from SPEC-007 §2, including the intent registry table and emission rules.]
```

### Section 3: Cross-Document Impact

**Feedback:** The table is insufficient. "Canonical scope taxonomy and routing (already drafted)" is not an actionable change. "Runtime (voice UI)" and "Deployment" are not documents, making this impact analysis non-compliant with the amendment template.

**Scores:** Cross-Document Consistency: 2, Practical Operability: 2

**Recommendation:** Replace the table with a proper cross-document impact matrix that lists each document (AIOS-SPEC-003, -006, -007), the specific section to modify, the required change, and the priority. Remove references to runtime/deployment as they are not governed documents.

**Proposed New Table:**
| Document | Section | Required Change | Priority |
|----------|---------|-----------------|----------|
| AIOS-SPEC-007 | Entire Document | Status changed from `draft` to `ratified`; ensure alignment with AMD-2026-005 Annex A schema. | Critical |
| AIOS-SPEC-003 | §7 (Governed Intent Emission Contract) | Add new subsection "11. Google Workspace Governed Intents" with schema and rules from SPEC-007 §2. | Critical |
| AIOS-SPEC-006 | §13 (Google Workspace Governed Canvas Surfaces) | Add surface registration table and requirements as defined in SPEC-007. | High |

### Section 4: Ratification Requirements

**Feedback:** The checklist is generic and does not include amendment-specific gates. Item 3 references "SPEC-007 aligned with AMD-2026-005" but does not specify what alignment means (e.g., schema compliance, load state rules).

**Scores:** Legal Enforceability: 2, Practical Operability: 3

**Recommendation:** Add specific, verifiable ratification gates. Require that the authoritative schema (Annex A) is defined and that a compliance test suite exists.

**Proposed Additions to Checklist:**
```
- [ ] Annex A (Authoritative Schema for Workspace Intents & Routing) is complete and normatively referenced.
- [ ] A test suite validating intent → scope class mapping and routing exists in the integration control plane repository.
- [ ] POL-WORKSPACE-001 through POL-WORKSPACE-006 policy packs are drafted and attached as Annex B.
```

### Missing: Annex A (Authoritative Schema)

**Feedback:** The amendment critically lacks the normative technical schema that makes it binding. AMD-2026-005 sets the precedent by including an "Annex A — Canonical schema." This amendment must define the intent IDs, parameters, scope class mappings, and routing contracts.

**Scores:** Architectural Fidelity: 1, Completeness: 1, Developer Synchrony: 1

**Recommendation:** Add an "Annex A — Workspace Intent & Routing Schema" as a normative section. This should include the Layer 1 scope class enumeration, the Layer 2 intent registry table, and the JSON schema for the routing envelope.

**Proposed Annex A Skeleton:**
```
## Annex A — Workspace Intent & Routing Schema (Normative)

### A.1 Layer 1: Governance Scope Classes
| Scope Class | Description | Policy Pack |
|-------------|-------------|-------------|
| `workspace.google.read` | Read-only access to user data. | POL-WORKSPACE-001 |
| `workspace.google.write` | Create/update/delete access. | POL-WORKSPACE-002 |
| `workspace.google.admin` | Administrative settings. | POL-WORKSPACE-003 |

### A.2 Layer 2: Operational Intents
| Intent ID | Required Parameters | Resolves to Scope Class |
|-----------|---------------------|--------------------------|
| `workspace.hub` | none | `workspace.google.read` |
| `workspace.mail.search` | `query` | `workspace.google.read` |
| `workspace.calendar.create` | `title`, `startTime`, `endTime` | `workspace.google.write` |

### A.3 Routing Envelope Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["intent", "scope_class", "parameters"],
  "properties": {
    "intent": { "type": "string", "pattern": "^workspace\\..+$" },
    "scope_class": { "type": "string" },
    "parameters": { "type": "object" }
  }
}
```
```

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Entire Document | Lacks normative technical schema. | Add Annex A with scope classes, intent registry, and routing JSON schema. | Critical | 4,5,9 |
| 2 | Section 2: Proposed Changes | Effects are not actionable amendments. | Rewrite each change with "Old Text"/"New Text" redlines for the affected documents. | Critical | 5,7,9 |
| 3 | Section 3: Cross-Document Impact | Table references non-documents and is vague. | Replace with a document-specific impact matrix listing sections and exact changes. | High | 1,7 |
| 4 | Section 4: Ratification Requirements | Checklist is generic. | Add amendment-specific gates: Annex A completeness, test suite, policy packs. | High | 3,7 |
| 5 | Section 1: Rationale | Uses undefined terms "Layer 1"/"Layer 2". | Add inline definitions linking to the new Annex A. | Medium | 1,8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The amendment scores a 1 in Completeness due to missing critical normative content (schemas, detailed changes) and a 2 in Architectural Fidelity, failing to define the governed integration plane's architecture. The composite score of 2.5 and the presence of a dimension score of 1 trigger the "Major Revision Required" disposition per the rubric.

**Top 3 Actions Required:**
1.  **Define the Binding Schema:** Draft and include Annex A with the complete Workspace Intent & Routing Schema, making the technical governance rules explicit and implementable.
2.  **Specify Document Changes:** Rewrite Section 2 to provide concrete "Old Text"/"New Text" amendments for AIOS-SPEC-003 and AIOS-SPEC-006.
3.  **Clarify Impact and Ratification:** Revise Sections 3 and 4 to provide a precise cross-document impact matrix and amendment-specific ratification checklist.