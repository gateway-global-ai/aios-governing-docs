review_id: REV-AIOS-VOICE-FIRST-UI-ARTIFACT-KIT-STANDARD-001-001
document_reviewed: AIOS-VOICE-FIRST-UI-ARTIFACT-KIT-STANDARD-001
document_version: 0.1.0
reviewer: Gemini
review_date: 2024-05-24
review_round: 1
review_type: legal
disposition: major_revision_required
composite_score: 3.1
---

# Peer Review: Voice-first UI artifact kit standard

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 3 | The document's principles align well, but its use of "SHOULD" creates a soft conflict with the "SHALL" mandates of other governing documents. |
| 2 | Business Model Alignment | 4 | By standardizing core UI artifacts, this document strongly supports the ecosystem model, enabling vendors to build consistent, compliant experiences. |
| 3 | Legal Enforceability | 2 | The pervasive use of "SHOULD" instead of "SHALL" for key requirements renders the standard largely unenforceable and advisory rather than binding. |
| 4 | Architectural Fidelity | 5 | Placing the canonical UI kit within the governance repository is an exemplary embodiment of UI sovereignty and policy supremacy. |
| 5 | Completeness | 2 | The document is missing critical components for implementation, including a schema for the manifest and definitions for artifact properties. |
| 6 | Conflict Freedom | 3 | While there are no direct contradictions, the weak, non-binding language creates significant tension with related mandatory standards. |
| 7 | Practical Operability | 2 | The lack of a manifest schema and property definitions makes it impossible for a developer to implement or validate against this standard. |
| 8 | Style & Clarity | 4 | The document's purpose and principles are clearly stated and adhere to the Style Guide, but the implementation details are too vague. |
| 9 | Developer Synchrony | 2 | A developer receives a list of concepts but no concrete schemas or definitions, making it impossible to build against this standard. |
| 10 | Platform Economics Synchrony | 4 | The document has no direct economic implications but does not conflict with the established platform economics model. |
| 11 | Friction Factor | 3 | While the principle is low-friction, the lack of clarity and specifications would create significant friction and ambiguity during implementation. |
| | **Composite Score** | **3.1** | |

---

## Overall Assessment

### Strengths

-   **Architectural Principle:** The core rule to locate the canonical UI artifact kit within the `aios-governing-docs` repository ("Governing rule" section) is a powerful and correct enforcement of the "UI Sovereignty" principle from the Technical Manifesto. It prevents implementation drift from silently overriding governance.
-   **Strategic Alignment:** The document strongly aligns with the voice-first principles established in `AMD-2026-012` (Shell Authority) and `AMD-2026-007` (Intent Primitive), correctly positioning UI as a subordinate support surface for intent.
-   **Consistency in Specifics:** The "Multi-step card navigation rule" is excellent, as it directly mirrors and reinforces the same requirement in `AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001`, showing good cross-document awareness.

### Critical Gaps

-   **Legal Unenforceability:** The most significant flaw is the repeated use of "SHOULD" for requirements that must be binding. This transforms a standard into a set of recommendations, undermining its legal and technical authority. For example, the "Rendered-proof rule" *should* require proof, but `AMD-2026-008-ADD-004` *shall* require it, creating a compliance gap.
-   **Missing Normative Schemas:** The document mandates a "machine-readable manifest" but fails to provide a schema for it. It also requires artifacts to declare properties like `surface_zone` and `artifact_kind` without defining the allowed values. This makes conformance impossible to measure or enforce.
-   **Ambiguous Relationship with Component Registry:** The "Relationship to the registry" section states that `AIOS-SPEC-006` is the authority but does not define the mandatory, enforceable mechanism by which an `artifact_id` from this kit maps to a `component_id` in the registry. The weak language in `AIOS-SPEC-006` ("SHOULD preserve stable mapping") is not corrected or clarified here, leaving a critical integration point undefined.

---

## Article-by-Article Review

### Purpose & Governing rule

**Feedback:** The purpose is clear and the governing rule is strong, using "SHALL" correctly. This section sets a strong foundation that the rest of the document unfortunately fails to build upon.

**Scores:** Architectural Fidelity: 5, Legal Enforceability: 5

**Recommendation:** No changes needed.

### In-repo library model

**Feedback:** The reference to the library path is good, but the requirement for what the root directory contains is not binding.
**Scores:** Legal Enforceability: 2

**Recommendation:** Change "That root SHOULD contain" to "That root **SHALL** contain". Furthermore, add a requirement for a `schema.json` file for the manifest itself.

### Artifact family

**Feedback:** This section lists artifact names without any definition. While this is a `reference_implementation` document, a one-sentence description for each family is necessary to prevent ambiguity. For example, what is the distinction between `4_2 Title and Description` and `4_3 Title Description and Paragraph`?
**Scores:** Completeness: 2, Practical Operability: 2

**Recommendation:** Add a table defining each artifact's purpose.

### Artifact identity rule

**Feedback:** This rule is not a rule; it is a suggestion. It lists properties without defining their types, constraints, or allowed values.
**Scores:** Legal Enforceability: 1, Developer Synchrony: 1

**Recommendation:**
1.  Change "Each governed artifact SHOULD declare at minimum" to "Each governed artifact **SHALL** declare at minimum".
2.  Provide a table defining the type and purpose of each property. For properties that are enums (e.g., `surface_zone`, `artifact_kind`), list the permissible values.

### Rendered-proof rule

**Feedback:** This is a critical compliance gap. The browser review gate (`AMD-2026-008-ADD-004`) is not optional. This document's language must reflect the mandatory nature of that gate.
**Scores:** Legal Enforceability: 1, Cross-Document Consistency: 2

**Recommendation:**
1.  Change both instances of "SHOULD" to "**SHALL**".
2.  Reword to be more definitive: "Artifacts that drive user-visible disclosures, navigation, multi-step cards, agent controls, or session-critical state transitions **SHALL** require browser-visible proof and artifact checks under `AMD-2026-008-ADD-004`."

### Relationship to the registry

**Feedback:** This is the most significant technical and legal gap. The link between this kit and the canonical component registry (`AIOS-SPEC-006`) is left to interpretation. An enforceable system requires a deterministic, non-negotiable process for how these two documents interact.
**Scores:** Completeness: 2, Legal Enforceability: 2

**Recommendation:** Add a new section, "Registration and Mapping Mandate," that specifies the following:
"When an artifact from this kit is used, it **SHALL** be registered in the UI Component Registry (`AIOS-SPEC-006`). The `component_id` in the registry **SHALL** follow the format `kit-vf1-{artifact_id}`. The registry entry's `source` field **SHALL** be set to `governed-kit:voice-first-v1`, and it **SHALL** include a `kit_metadata` object containing the `artifact_id` and `version` from the kit's manifest to ensure auditable traceability."

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---|---|---|---|---|
| 1 | Multiple | The document uses "SHOULD" for binding requirements, making it unenforceable. | Replace all normative instances of "SHOULD" with "**SHALL**", specifically in "In-repo library model", "Artifact identity rule", and "Rendered-proof rule". | Critical | 3, 6, 7 |
| 2 | In-repo library model / Artifact identity rule | The standard references a "machine-readable manifest" and artifact properties but provides no schema or definitions. | Add a new appendix containing a normative JSON schema for the manifest and a table defining the type and allowed enum values for all artifact properties. | Critical | 5, 7, 9 |
| 3 | Relationship to the registry | The link between a kit `artifact_id` and a registry `component_id` is ambiguous and not mandatory. | Add a new section defining the mandatory mapping process and `component_id` format for registering kit artifacts in the `AIOS-SPEC-006` registry. | High | 1, 5, 7, 9 |
| 4 | Rendered-proof rule | The language weakens the requirements of the mandatory browser review gate. | Reword the section to use "SHALL" and explicitly state that compliance with `AMD-2026-008-ADD-004` is non-negotiable for the listed artifact types. | High | 1, 3, 6 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is founded on a sound and important architectural principle, but its legal and technical enforceability is critically flawed. The pervasive use of non-binding language and the absence of essential schemas render it inoperable as a governing standard.

**Top 3 Actions Required:**
1.  Conduct a global search-and-replace of "SHOULD" with "**SHALL**" for all normative statements to make the document legally and technically binding.
2.  Create and include a normative JSON schema for the kit manifest and define all properties and their allowed values, making compliance machine-verifiable.
3.  Add a new section that explicitly and mandatorily defines the process for mapping and registering kit artifacts within the master UI Component Registry (`AIOS-SPEC-006`).