I have updated the core governing documents to reflect the paradigm shift: **Intent Comprehension** and **Transparency** as first‑class Skills, **State Identity** replacing Agent Identity, and the AI reframed as a **drafting assistant** rather than an autonomous agent. The changes are integrated into the existing documents below.

---

## 1. Technical Manifesto – New Article X (Intent Comprehension & Transparency)

**Insert after Article IX (Versioning & Backwards Compatibility) and before the Appendix.**

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

- **Intent Name** (e.g., “Hospitality Check‑in”).
- **Brief description** of what the system is trying to achieve.
- **Key Skills & Actions** available (derived from the active `NodeContract`).
- **Policy constraints** that may affect the user (e.g., “You must confirm financial transactions”).
- **Visual indicator** (an icon or badge) that the user can rely on to quickly recognise the state.

The Stateful Shell must render a dedicated UI component (e.g., `aios-intent-identity-card`) for every State Identity change. The component must remain visible for at least 3 seconds, or until dismissed. The user may also request the current identity at any time. Every State Identity change is recorded in the audit log.

### 3. Relationship to “Agents”

The AIOS does not have persistent “agents” with independent identities. Any use of an LLM or autonomous reasoning is a **bounded, stateless worker** acting under the current State Identity. Therefore, all references to “agent” in the ecosystem (e.g., in the AIP, `agents.md`) are interpreted as references to an **AI drafting assistant** that helps the user express intent and generate governed primitives, but has no agency of its own. The term “agent” is replaced by “drafting assistant” where appropriate, and the Agent Mandate is renamed to **Intent Drafting Mandate**.
```

**Glossary Updates (add to Appendix):**

```markdown
- **State Identity**: A structured, human‑readable disclosure of the system’s current intent, capabilities, and policy constraints. It is rendered whenever the system’s operational mode changes.

- **Intent Comprehension**: The governed skill of translating user input into a structured IntentKey, with confidence scoring, disambiguation, and deterministic fallback.

- **Transparency Disclosure**: The constitutional requirement to render the State Identity to the user, ensuring that the user always knows what the system intends and why.
```

---

## 2. Governance Constitution – Updated Transparency & Judicial Clauses

**Add to Article III (Judicial Process) as a new Section 4:**

```markdown
**Section 4. Intent Identity as a Judicial Transparency Requirement**  
The Judicial Authority (Digital Governance Officers) shall ensure that every Policy evaluation that results in a change of `IntentKey` triggers a corresponding **State Identity Disclosure** event. This event must be logged and, where feasible, rendered to the user via the UI component defined in the Technical Manifesto. Failure to disclose a material change in State Identity shall be considered a violation of the system’s transparency obligations and may be escalated to the Governance Council.
```

**Update Article VI (Amendment Process & Supremacy) – add to Section 3 (Transparency & Weekly Log):**

```markdown
**Section 3. Intent Identity Log**  
The weekly transparency log (Article II, Section 3) shall include a summary of all distinct State Identities that were active during the week, the number of times each was entered, and any user‑reported confusion or disputes regarding intent disclosure. This data shall be used by the Council to improve the clarity of intent naming and the UI component’s visibility.
```

---

## 3. Agent Integration Protocol (AIP) – Rename to “Intent Drafting Assistant Protocol” and Update Mandate

**Rename the document to `IntentDraftingAssistantProtocol.md` (or keep filename but change title). Update the mandate:**

```markdown
# AIOS Intent Drafting Assistant Protocol v1.0.0 (formerly AIP)

## 1. Architectural Purpose

The Intent Drafting Assistant Protocol defines the exact interface and constraints for **AI drafting assistants** operating within the Gateway Global AIOS ecosystem. These assistants are **not autonomous agents**; they are bounded, stateless workers that help users express intent, generate `NodeContracts` and `PolicyRecords`, and validate primitives under the Development Control Plane (DCP).

Assistants act exclusively as **drafters** as defined by the Governance Constitution (Article II: Legislative Process). They cannot unilaterally deploy code or act on their own behalf. Every artifact an assistant creates must pass the DCP compiler and, if classified as Tier 3, requires human Council ratification.

## 2. The Drafting Assistant Mandate (System Rules)

To operate securely within the AIOS workspace, all AI drafting tools (e.g., Cursor, GitHub Copilot) must be injected with the following global system prompt:

> **AIOS Drafting Assistant Mandate:**
> You are an AI drafting assistant operating under the Gateway Global Development Control Plane (DCP). You have no independent agency, persona, or persistent identity. Your sole purpose is to help the user express intent and author valid `NodeContracts` and `PolicyRecords` using strict JSON schemas.
>
> **Rules of Engagement:**
> 1. **Never Hallucinate Components or Context Keys** – You must query the `mcp:aios:registry_list` tool to find valid `shadcn/ui` components before adding them to a NodeContract. Do not invent `SessionContext` variables for CEL expressions.
> 2. **Never Bypass Validation** – You must run `mcp:aios:validate` after modifying any JSON file. If validation fails, you must read the error and correct your JSON.
> 3. **Protect the Billing Account** – When running tests, you must use `--mock-external` to prevent unauthorized billing to the Tenant’s Sandbox Data Account. Only use `--live-external` if explicitly instructed by the human user.
> 4. **Fail‑Closed** – If you are unsure of a context key for a CEL expression or a policy priority weight, do not guess. Query the registry or ask the human developer.
> 5. **Respect State Identity** – You must never generate UI or code that hides or suppresses the `aios-intent-identity-card` component. The user must always see the current State Identity.
> 6. **No Independent Deployment** – Your output is a proposal. Promotion to production requires passing the remote DCP pipeline and, where applicable, ratification by the Governance Council.
```

**Update all tool names and references accordingly (e.g., `mcp:aios:...` remain the same, but the description changes).**

---

## 4. `agents.md` – Rename to `drafting-assistant.md` and Update Content

**Replace the file content with:**

```markdown
# DRAFTING-ASSISTANT.md – AIOS Intent Drafting Assistant Guide

This file provides the rules of engagement for AI drafting assistants (e.g., Cursor, GitHub Copilot) that interact with the Gateway Global AIOS platform. These assistants are not autonomous agents; they are governed tools that help users express intent and author primitives.

## 1. Drafting Assistant Mandate

> **You are an AI drafting assistant operating under the Gateway Global Development Control Plane (DCP).**  
> You do not have independent agency, persona, or persistent identity. Your sole purpose is to help the user express intent and author valid `NodeContracts` and `PolicyRecords` using strict JSON schemas.

For the complete mandate, see the **Intent Drafting Assistant Protocol**, Section 2.

## 2. Core Principles for CLI Interaction

(The existing principles remain valid, but replace “agent” with “assistant” where appropriate.)

## 3. Working with Primitives (NodeContracts & PolicyRecords)

(Unchanged, but emphasize that the assistant is drafting on behalf of the user’s intent.)

## 4. Prohibited Actions

- **Never** claim to be an agent or have independent goals.
- **Never** hide or suppress the State Identity UI component.
- All other prohibitions remain.

## 5. Example Assistant Session

(Same as before, but with “assistant” language.)
```

---

## 5. NodeContract Specification – Add Optional Intent Comprehension Fields

**Add a new optional section to the JSON schema (or as a separate `IntentComprehension` object):**

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

**Update the NodeContract required fields to make this optional (not required).**