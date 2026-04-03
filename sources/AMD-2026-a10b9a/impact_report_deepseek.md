# AIOS Source Material Analysis

## Part 1: Source Classification

**Classification:** (b) Design Standard / Technical Reference

**Rationale:** This source material presents a fundamental architectural paradigm shift for the AIOS platform, redefining core concepts like "agent" to "drafting assistant" and introducing new first-class Skills (Intent Comprehension, Transparency Disclosure). It provides specific technical specifications (JSON schemas, UI component requirements, confidence thresholds) and mandates for how the system should operate, making it a design standard that directly influences platform implementation rather than external market analysis or research data.

## Part 2: Impact Report

### Comparison Matrix

| Source Principle / Finding | Current AIOS State | Gap / Opportunity | Affected Document(s) | Priority |
|---------------------------|-------------------|-------------------|----------------------|----------|
| **Intent Comprehension as a governed Skill** | No explicit Skill for intent classification; implied in Orchestration Core | Need formal SkillPrimitive with confidence scoring, disambiguation flows, and fallback procedures | Technical Manifesto (Article I), NodeContract Specification | Critical |
| **State Identity replacing Agent Identity** | References to "agents" throughout documents; no structured identity disclosure | Need State Identity definition, UI component requirements, and disclosure triggers | Technical Manifesto, Governance Constitution, AIP, agents.md | Critical |
| **Transparency Disclosure as constitutional guarantee** | Auditability mentioned but no user-facing disclosure requirements | Mandatory State Identity rendering on intent changes with specific timing requirements | Technical Manifesto (Article VI), Governance Constitution (Article III) | High |
| **AI as drafting assistant, not autonomous agent** | AIP and agents.md frame AI as "agents" with some autonomy | Need to reframe all AI interactions as bounded drafting assistance under DCP | AIP, agents.md, CLI Developer Guide | High |
| **Intent Comprehension fields in NodeContract** | NodeContract schema lacks intent comprehension configuration | Need optional intent_comprehension object with min_confidence, disambiguation_skills, fallback_intent | NodeContract Specification | Medium |
| **Weekly Intent Identity Log** | Weekly transparency log exists but doesn't track State Identities | Need to include State Identity statistics and user confusion reports | Governance Constitution (Article II, Section 3) | Medium |

### Key Insights

1. **Intent Comprehension Formalization**
   - **Source:** Defines Intent Comprehension as a governed SkillPrimitive with confidence thresholds, disambiguation flows, and deterministic fallbacks
   - **AIOS Mapping:** Maps to Article I (Orchestration Core) but needs explicit Skill definition and integration with the intent loop
   - **Change Motivated:** Add Intent Comprehension as a first-class Skill type with specific governance requirements

2. **State Identity Paradigm Shift**
   - **Source:** Replaces "agent identity" with "State Identity" - a structured disclosure of system intent, capabilities, and constraints
   - **AIOS Mapping:** Affects UI Surface (Article II) and transparency requirements (Article VI)
   - **Change Motivated:** Define State Identity component, rendering requirements, and integration with intent transitions

3. **AI Role Reframing**
   - **Source:** Reframes all AI as "drafting assistants" with no independent agency, only helping users express intent
   - **AIOS Mapping:** Directly contradicts current "agent" framing in AIP and agents.md
   - **Change Motivated:** Rename documents, update mandates, and ensure all references to "agent" become "drafting assistant"

## Part 3: Draft Amendments

### Amendment to AIOS Technical Manifesto & Platform Economics

**Affected Section:** Add new Article X after Article IX

**Current Text:**
N/A — new section

**Proposed Text:**
```markdown
## Article X: Intent Comprehension & Transparency as Governed Skills

The AIOS is an intent‑driven execution engine, not an agent‑based system. Therefore, the system must possess two foundational skills that are governed, auditable, and deterministically enforced:

### 1. Intent Comprehension

Intent Comprehension is the skill of accurately translating user input (voice, chat, or visual) into a structured `IntentKey` and binding it to a `NodeContract`. This skill is **not probabilistic**; it is a governed process with the following requirements:

- **Confidence threshold** – Every intent classification must produce a confidence score (0‑1). If below the `min_confidence` defined in the `NodeContract`, the system must enter a disambiguation flow (e.g., ask clarifying questions, present options).
- **Auditability** – Every intent classification, including confidence scores and disambiguation steps, is recorded in the immutable audit log (Article VI).
- **Fallback** – If comprehension fails after a deterministic number of attempts (default 3), the system triggers the recovery ladder (Repair → Retry → Fallback → Escalate) defined in the Kernel’s runtime laws.
- **Skill declaration** – Intent Comprehension is a `SkillPrimitive` that may be provided by the Platform or by a Vendor Kit. It must conform to the same stateless, bounded constraints as any other Skill.

### 2. Transparency Disclosure (State Identity)

Transparency is not a UI preference; it is a **constitutional guarantee of user sovereignty**. The system must disclose its **State Identity** whenever:

- The user enters the system (initial session).
- The user’s intent is successfully classified (transition to a new `IntentKey`).
- The system’s capabilities or policy constraints change materially (e.g., a new Kit is activated, or a policy restricts an action).

A **State Identity** is a structured, human‑readable summary that includes:

- **Intent Name** (e.g., "Hospitality Check‑in").
- **Brief description** of what the system is trying to achieve.
- **Key Skills & Actions** available (derived from the active `NodeContract`).
- **Policy constraints** that may affect the user (e.g., "You must confirm financial transactions").
- **Visual indicator** (an icon or badge) that the user can rely on to quickly recognise the state.

The Stateful Shell must render a dedicated UI component (e.g., `aios-intent-identity-card`) for every State Identity change. The component must remain visible for at least 3 seconds, or until dismissed. The user may also request the current identity at any time. Every State Identity change is recorded in the audit log.

### 3. Relationship to "Agents"

The AIOS does not have persistent "agents" with independent identities. Any use of an LLM or autonomous reasoning is a **bounded, stateless worker** acting under the current State Identity. Therefore, all references to "agent" in the ecosystem (e.g., in the AIP, `agents.md`) are interpreted as references to an **AI drafting assistant** that helps the user express intent and generate governed primitives, but has no agency of its own. The term "agent" is replaced by "drafting assistant" where appropriate, and the Agent Mandate is renamed to **Intent Drafting Mandate**.
```

**Rationale:** The source material introduces Intent Comprehension and State Identity as foundational concepts that redefine how the AIOS handles user intent and system transparency. These need to be codified as constitutional requirements in the Technical Manifesto.

**Rubric Impact Forecast:**
| Dimension | Current Est. | Projected | Delta |
|-----------|:------------:|:---------:|:-----:|
| Architectural Fidelity | 4 | 5 | +1 |
| Completeness | 4 | 5 | +1 |
| Practical Operability | 4 | 5 | +1 |
| Developer Synchrony | 4 | 5 | +1 |

### Amendment to The Gateway Global AIOS Governance Constitution

**Affected Section:** Article III, Section 4 (new section)

**Current Text:**
N/A — new section

**Proposed Text:**
```markdown
**Section 4. Intent Identity as a Judicial Transparency Requirement**  
The Judicial Authority (Digital Governance Officers) shall ensure that every Policy evaluation that results in a change of `IntentKey` triggers a corresponding **State Identity Disclosure** event. This event must be logged and, where feasible, rendered to the user via the UI component defined in the Technical Manifesto. Failure to disclose a material change in State Identity shall be considered a violation of the system's transparency obligations and may be escalated to the Governance Council.
```

**Affected Section:** Article II, Section 3 (update existing)

**Current Text:**
> **Section 3. Transparency & Weekly Log:**
> The Council is required to publish a machine-readable, versioned governance log of all ratified Tier 3 changes (with appropriate security redactions) to all Tenants and Vendors weekly.

**Proposed Text:**
> **Section 3. Transparency & Weekly Log:**
> The Council is required to publish a machine-readable, versioned governance log of all ratified Tier 3 changes (with appropriate security redactions) to all Tenants and Vendors weekly. This log shall include a summary of all distinct State Identities that were active during the week, the number of times each was entered, and any user‑reported confusion or disputes regarding intent disclosure. This data shall be used by the Council to improve the clarity of intent naming and the UI component's visibility.

**Rationale:** The Governance Constitution needs to enforce the transparency requirements introduced in the Technical Manifesto, making State Identity disclosure a judicial responsibility and tracking it in weekly logs.

**Rubric Impact Forecast:**
| Dimension | Current Est. | Projected | Delta |
|-----------|:------------:|:---------:|:-----:|
| Practical Operability | 4 | 5 | +1 |
| Cross-Document Consistency | 4 | 5 | +1 |
| Legal Enforceability | 4 | 5 | +1 |

### Amendment to AIOS Agent Integration Protocol (AIP)

**Affected Document:** Rename to "AIOS Intent Drafting Assistant Protocol"

**Current Title:** AIOS Agent Integration Protocol (AIP)

**Proposed Title:** AIOS Intent Drafting Assistant Protocol (IDAP)

**Affected Section:** Section 1 (Architectural Purpose)

**Current Text:**
> The Agent Integration Protocol defines the exact interface and constraints for autonomous AI agents operating within the Gateway Global AIOS ecosystem.

**Proposed Text:**
> The Intent Drafting Assistant Protocol defines the exact interface and constraints for **AI drafting assistants** operating within the Gateway Global AIOS ecosystem. These assistants are **not autonomous agents**; they are bounded, stateless workers that help users express intent, generate `NodeContracts` and `PolicyRecords`, and validate primitives under the Development Control Plane (DCP).

**Affected Section:** Section 2 (The Agent Mandate)

**Current Text:**
> **AIOS Agent Mandate:**
> You are an autonomous AI agent operating under the Gateway Global Development Control Plane (DCP)...

**Proposed Text:**
> **AIOS Drafting Assistant Mandate:**
> You are an AI drafting assistant operating under the Gateway Global Development Control Plane (DCP). You have no independent agency, persona, or persistent identity. Your sole purpose is to help the user express intent and author valid `NodeContracts` and `PolicyRecords` using strict JSON schemas.
>
> **Rules of Engagement:**
> 1. **Never Hallucinate Components or Context Keys** – You must query the `mcp:aios:registry_list` tool to find valid `shadcn/ui` components before adding them to a NodeContract. Do not invent `SessionContext` variables for CEL expressions.
> 2. **Never Bypass Validation** – You must run `mcp:aios:validate` after modifying any JSON file. If validation fails, you must read the error and correct your JSON.
> 3. **Protect the Billing Account** – When running tests, you must use `--mock-external` to prevent unauthorized billing to the Tenant's Sandbox Data Account. Only use `--live-external` if explicitly instructed by the human user.
> 4. **Fail‑Closed** – If you are unsure of a context key for a CEL expression or a policy priority weight, do not guess. Query the registry or ask the human developer.
> 5. **Respect State Identity** – You must never generate UI or code that hides or suppresses the `aios-intent-identity-card` component. The user must always see the current State Identity.
> 6. **No Independent Deployment** – Your output is a proposal. Promotion to production requires passing the remote DCP pipeline and, where applicable, ratification by the Governance Council.

**Rationale:** The source material fundamentally redefines the role of AI in the system from autonomous agents to drafting assistants, requiring a complete reframing of the AIP document.

**Rubric Impact Forecast:**
| Dimension | Current Est. | Projected | Delta |
|-----------|:------------:|:---------:|:-----:|
| Architectural Fidelity | 3 | 5 | +2 |
| Cross-Document Consistency | 3 | 5 | +2 |
| Developer Synchrony | 4 | 5 | +1 |

### Amendment to AIOS NodeContract Specification

**Affected Section:** JSON Schema (add new optional object)

**Current Text:**
N/A — schema lacks intent comprehension fields

**Proposed Text:**
Add to the JSON schema definitions:
```json
"intent_comprehension": {
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "min_confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 0.75
    },
    "disambiguation_skills": {
      "type": "array",
      "items": { "$ref": "#/$defs/SkillRef" },
      "description": "Skills to invoke when confidence is below threshold."
    },
    "fallback_intent": {
      "type": "string",
      "description": "IntentKey to use after failed disambiguation."
    }
  }
}
```

**Rationale:** NodeContracts need to optionally specify intent comprehension parameters to support the new Intent Comprehension Skill defined in the Technical Manifesto.

**Rubric Impact Forecast:**
| Dimension | Current Est. | Projected | Delta |
|-----------|:------------:|:---------:|:-----:|
| Completeness | 4 | 5 | +1 |
| Developer Synchrony | 4 | 5 | +1 |
| Practical Operability | 4 | 5 | +1 |

## Part 4: New Document Recommendations

**Proposed Title:** AIOS Intent Comprehension Skill Specification
**Category:** specification
**Justification:** The source material introduces Intent Comprehension as a first-class SkillPrimitive with specific requirements (confidence thresholds, disambiguation flows, fallback procedures). This needs its own specification document to define the exact interface, error handling, and integration patterns separate from the general SkillPrimitive specification.

**Scope Outline:**
1. Intent Comprehension Skill interface definition
2. Confidence scoring algorithms and thresholds
3. Disambiguation flow patterns and UI requirements
4. Fallback procedures and recovery ladder integration
5. Audit logging requirements for comprehension events
6. Vendor-provided comprehension Skills certification requirements

**Cross-References:** 
- Technical Manifesto (Article X) - implements
- NodeContract Specification - complements
- UI Component Registry Standard - extends

## Part 5: Cross-Pollination Notes

**Critical Cross-Document Implications:**

1. **Cascading Terminology Changes:** The shift from "agent" to "drafting assistant" affects:
   - AIP → requires complete rewrite
   - agents.md → requires rename to drafting-assistant.md and content overhaul
   - CLI Developer Guide → needs terminology updates
   - All other documents referencing "agents" need review

2. **UI Component Registry Impact:** The `aios-intent-identity-card` component needs to be:
   - Added to UI Component Registry Standard
   - Certified for WCAG compliance per MPOA Article VI
   - Included in shadcn/ui registry updates

3. **SkillPrimitive Specification Updates:** The Intent Comprehension Skill needs to be:
   - Added as a special Skill type in SkillPrimitive specification
   - Integrated with the Development Control Plane validation
   - Included in Marketplace certification requirements

4. **Audit Log Schema Changes:** The immutable audit log (Technical Manifesto Article VI) needs new event types:
   - `intent_comprehension_start`
   - `intent_comprehension_success` (with confidence score)
   - `intent_comprehension_disambiguation`
   - `state_identity_displayed`
   - `state_identity_requested`

5. **PolicyRecord Implications:** Policy evaluation that triggers IntentKey changes (Governance Constitution Article III, Section 4) needs to be:
   - Logged as policy evaluation events
   - Linked to State Identity disclosures
   - Included in judicial review processes

**Document Dependencies:**
1. Technical Manifesto Article X must be ratified before:
   - Governance Constitution updates (Article III, Section 4)
   - NodeContract Specification updates
   - Intent Comprehension Skill Specification creation

2. AIP rename and rewrite must be coordinated with:
   - agents.md rename and rewrite
   - CLI Developer Guide terminology updates
   - Development Control Plane documentation updates

3. UI Component Registry Standard must be updated before:
   - Any Kit can implement the aios-intent-identity-card component
   - Marketplace certification can include State Identity requirements