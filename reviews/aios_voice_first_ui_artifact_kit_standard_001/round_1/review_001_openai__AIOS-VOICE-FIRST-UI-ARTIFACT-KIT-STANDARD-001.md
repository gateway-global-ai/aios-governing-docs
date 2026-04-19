---
review_id: REV-AIOS-VOICE-FIRST-UI-ARTIFACT-KIT-STANDARD-001-001
document_reviewed: AIOS-VOICE-FIRST-UI-ARTIFACT-KIT-STANDARD-001
document_version: 0.1.0
reviewer: OpenAI
review_date: 2026-04-17
review_round: 1
review_type: editorial
disposition: major_revision_required
composite_score: 2.8
---

# Peer Review: Voice-first UI artifact kit standard

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 2 | The document aligns conceptually with AMD-2026-007 and AMD-2026-012 but uses non-canonical cross-references and undefined terms without section-level citations or glossary discipline. |
| 2 | Business Model Alignment | 3 | The document does not conflict with the platform model, but it is largely silent on Vendor and downstream consumption implications beyond a general anti-drift posture. |
| 3 | Legal Enforceability | 2 | Several core rules rely on vague or advisory language such as “should recognize,” “should default,” and “foundational,” which weakens enforceability for a purported governing standard. |
| 4 | Architectural Fidelity | 4 | The document is broadly faithful to shell authority, voice-first entry, and anti-dashboard principles established in AMD-2026-007 and AMD-2026-012. |
| 5 | Completeness | 2 | The document states a kit model and artifact family but omits schema, approval flow, conformance criteria, failure handling, and the machine-readable contract needed to make the kit operational. |
| 6 | Conflict Freedom | 3 | No direct contradiction appears, but the document creates boundary ambiguity with AIOS-SPEC-006 and AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001 regarding where normative artifact requirements actually live. |
| 7 | Practical Operability | 2 | A developer or reviewer cannot reliably implement or test this standard because required fields, proof obligations, and registry integration are not specified with enough precision. |
| 8 | Style & Clarity | 4 | The prose is readable and mostly consistent in tone, but the structure is too lightweight for a governing standard and lacks the standard relationship and conformance sections expected by the style guide. |
| 9 | Developer Synchrony | 2 | The document names a repo path and artifact fields, but it does not provide a manifest schema, file contract, examples, or integration instructions sufficient for implementation. |
| 10 | Platform Economics Synchrony | 3 | The document does not introduce economic conflict, but it also does not explain whether in-repo kit governance affects Vendor submission, approval cost, or downstream packaging economics. |
| 11 | Friction Factor | 4 | The proposed governance is relatively lightweight and proportionate, though some ambiguity may create hidden friction during implementation and review. |
| | **Composite Score** | **2.8** | |

---

## Overall Assessment

### Strengths

- The document clearly reinforces the anti-drift principle that foundational voice-first artifacts should remain governed at the law-controlled source rather than silently migrating into product repos, especially in **Governing rule** and **In-repo library model**.
- The document is substantively coherent with **AMD-2026-012 §§4, 7, 8, 9** and **AMD-2026-007 §§4.1, 11.4, 11.9** in treating the Shell as authority and menus/dropdowns as subordinate fallbacks.
- The **Multi-step card navigation rule** usefully mirrors the more detailed requirement already present in **AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001 §4.6**, which is a good cross-document instinct.
- The **Rendered-proof rule** appropriately points toward **AMD-2026-008-ADD-004** and recognizes that session-critical UI artifacts require browser-visible proof.

### Critical Gaps

- The document does not cite controlling documents by section, even where it is plainly implementing them; this is a major cross-document coherence defect given the style guide requirement for specific Article/Section citations.
- The document lacks a **Relationship to Governing Documents** section and a **Conformance** section, both of which are expected structural elements for governing documents and are especially necessary here because the boundary with **AIOS-SPEC-006** is otherwise unclear.
- The artifact identity model is incomplete: **Artifact identity rule** says artifacts “SHOULD declare at minimum” certain fields, but a governing kit standard needs a mandatory schema, field types, and validation rules.
- The document creates ambiguity between this standard, **AIOS-SPEC-006**, and **AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001** as to whether the kit is a registry family, a layout standard, a reference implementation, or all three.
- The document does not explain approval, versioning, deprecation, exception handling, or how browser-proof obligations are recorded per **AMD-2026-008-ADD-004 §§6, 7, 11**.

---

## Article-by-Article Review

### Frontmatter

**Feedback:**  
The frontmatter is serviceable but under-specified for a document intended to function as governed implementation authority. The `category` is `reference_implementation`, yet the body repeatedly uses mandatory language such as “SHALL,” which makes the document operate more like a specification or implementation standard. That mismatch should be resolved. The `cross_references` list names relevant documents, but it does not identify the controlling sections that this document implements or extends. This weakens traceability and makes later conflict analysis harder.

**Scores:** Cross-Document Consistency: 2, Legal Enforceability: 2, Style & Clarity: 3

**Recommendation:**  
Revise the frontmatter and opening note to clarify document class and authority. If the document is intended to impose binding implementation requirements, either change `category` to `specification` or add explicit language such as:

> This document is a governed implementation standard. Where it uses **SHALL**, **SHALL NOT**, or **MUST**, those requirements are binding for the in-repo voice-first UI artifact kit and any downstream implementation claiming conformance.

Also expand `cross_references` in the body with section-level citations, for example:
- **AMD-2026-012 §4.1, §4.2, §8**
- **AMD-2026-007 §4.1, §11.4, §11.9.3**
- **AMD-2026-008-ADD-004 §§4, 6, 7, 11**
- **AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001 §§4.4–4.6, §5**

---

### Purpose

**Feedback:**  
The purpose statement is clear and readable, and it identifies a real governance problem: silent mutation of effective law through downstream UI libraries. However, it does not explicitly state whether this document governs artifact identity only, artifact rendering rules, artifact proof obligations, or all three. That omission causes downstream ambiguity in scope.

**Scores:** Style & Clarity: 4, Completeness: 3, Conflict Freedom: 3

**Recommendation:**  
Add a scope sentence to the end of **Purpose**:

> This standard governs artifact identity, minimum metadata, placement-class expectations, proof obligations, and the relationship between the governed in-repo kit and downstream product implementations; it does not replace the UI registry, shell layout standard, or browser-review gate.

---

### Governing rule

**Feedback:**  
This section captures the core policy intent well, but it is too terse to be enforceable. “Silent authority” is understandable editorially, but it is not a defined governance term. The section also does not specify what downstream repos may change locally versus what must remain derived from the governed source.

**Scores:** Legal Enforceability: 2, Architectural Fidelity: 4, Cross-Document Consistency: 2

**Recommendation:**  
Replace the second sentence with more precise language:

> Product repositories **MAY** consume, mirror, or adapt implementations of governed kit artifacts, but they **SHALL NOT** redefine canonical `artifact_id`, required metadata, minimum controls, or proof obligations without a ratified change to this standard or a controlling referenced standard.

Also define “canonical” in this section or a definitions section.

---

### In-repo library model

**Feedback:**  
Naming the root path is useful, but the section uses “SHOULD contain” for elements that appear essential to the standard’s operation. If the manifest and governing references are required for conformance, they should be mandatory. The section also lacks a file-level contract, such as required filenames or manifest structure.

**Scores:** Practical Operability: 2, Developer Synchrony: 2, Legal Enforceability: 2

**Recommendation:**  
Convert the minimum library contents into mandatory requirements and add a file contract. Proposed replacement text:

> The governed library root for the first release **SHALL** be `sdk/voice_first_ui_artifact_kit/`.  
> That root **SHALL** contain at minimum:
> - `voice_first_ui_artifact_kit_manifest.yaml`
> - one or more machine-readable artifact definition files
> - a mapping of `artifact_id` to controlling standards
> - required placement and proof metadata for each governed artifact
> - version metadata for the kit release
>
> A downstream implementation claiming conformance **SHALL** be able to trace each consumed artifact to a governed source record in this root.

---

### Artifact family

**Feedback:**  
The section is understandable but editorially inconsistent. It mixes shell-level family names (`Header`, `Canvas`, `Footer`) with numbered canvas artifact labels (`1_1 Background`, `4_2 Title and Description`) without explaining the taxonomy. It is unclear whether these are artifact classes, concrete artifact IDs, design exemplars, or placeholder names. This is a major clarity and operability issue.

**Scores:** Style & Clarity: 3, Completeness: 2, Developer Synchrony: 2

**Recommendation:**  
Split this into two subsections: **Artifact classes** and **Initial governed artifacts**. Add explicit naming rules. For example:

> The kit taxonomy **SHALL** distinguish:
> - **artifact_class** — broad family such as `shell_header`, `shell_canvas`, `shell_footer`, `overlay_card`
> - **artifact_id** — stable governed identifier for a concrete reusable artifact such as `overlay_card_title_description`
>
> The initial governed artifact set for v0.1.0 is:
> - `shell_header`
> - `shell_canvas`
> - `shell_footer`
> - `background`
> - `container`
> - `overlay_card`
> - `title`
> - `title_description`
> - `title_description_paragraph`
> - `image`
> - `video`
> - `agent_controls`

If the numbered labels are intentional, define the numbering scheme.

---

### Artifact identity rule

**Feedback:**  
This is the document’s most important section, but it is currently too weak. It says each artifact “SHOULD declare at minimum” a list of fields, but a standard of this kind needs a mandatory schema, field types, allowed values, and at least one example artifact record. Without that, neither registry integration nor conformance testing is possible.

**Scores:** Legal Enforceability: 2, Practical Operability: 1, Developer Synchrony: 1

**Recommendation:**  
Replace the bullet list with a normative schema block. Example:

```yaml
artifact_id: string            # stable kebab-case identifier
artifact_label: string         # human-readable label
artifact_class: string         # shell_header | shell_canvas | shell_footer | overlay_card | media | control_group
surface_zone: string           # header | canvas | footer | overlay
artifact_kind: string          # structural | content | control | media
interactive: boolean
voice_first_role: string       # disclosure | navigation | orientation | action | support
required_controls: []          # list of governed control identifiers
required_visual_proofs: []     # list of proof identifiers mapped to review target obligations
related_governing_docs: []     # list of doc_id + section references
version: string
deprecated: boolean
```

Then add:

> Each governed artifact record **SHALL** include all fields above. Field extensions **MAY** be added if they do not alter the required minimum contract.

---

### Voice-first design rule

**Feedback:**  
This section is directionally correct and consistent with the broader framework, but it should cite the controlling sections it is implementing. As written, it restates principles already established in **AMD-2026-007** and **AMD-2026-012** without clarifying whether this document is merely inheriting them or adding kit-specific constraints.

**Scores:** Cross-Document Consistency: 2, Architectural Fidelity: 4, Conflict Freedom: 3

**Recommendation:**  
Add explicit citations and narrow the section to kit-specific implications. Proposed text:

> Consistent with **AMD-2026-012 §§4, 8, 9** and **AMD-2026-007 §4.1, §11.4, §11.9.3**, the kit **SHALL** support a voice-first shell architecture in which intent leads, the Shell remains the governing authority, and menus or dropdowns remain subordinate fallback surfaces.  
> The kit **SHALL NOT** define artifact patterns that presume dashboard-first entry, launcher-first control flow, or menu-first session architecture for standard end-user sessions.

---

### Multi-step card navigation rule

**Feedback:**  
This section is one of the strongest in the document because it is concrete and testable. However, it duplicates **AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001 §4.6** almost verbatim without saying whether this is incorporation by reference or a restatement for kit applicability. That duplication risks drift later.

**Scores:** Cross-Document Consistency: 3, Legal Enforceability: 4, Conflict Freedom: 3

**Recommendation:**  
Replace the body with a direct incorporation statement:

> For any multi-step card or slide sequence in the governed kit, the navigation minimums in **AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001 §4.6** are incorporated by reference and **SHALL** apply.  
> Each such artifact definition **SHALL** declare the presence of:
> 1. a progress label in the form `X of Y`;
> 2. a back control;
> 3. a close control.

This reduces duplication while preserving kit-level applicability.

---

### Overlay-card minimum

**Feedback:**  
The section is useful but under-specified. Terms like “clear title hierarchy” and “deterministic footer” are not defined. It also does not say whether these are required metadata properties, visual requirements, or runtime behavior requirements.

**Scores:** Legal Enforceability: 2, Practical Operability: 2, Style & Clarity: 3

**Recommendation:**  
Convert the section into explicit artifact requirements. For example:

> Any governed `overlay_card` artifact **SHALL** declare:
> - a primary title region;
> - a close control region;
> - a back control region when `multi_step: true`;
> - a step indicator when `multi_step: true`;
> - an action region or footer region when user or agent controls are present.
>
> For this section, “deterministic” means the action region location and control ownership are fixed by the artifact definition and do not vary ad hoc by downstream implementation.

---

### Rendered-proof rule

**Feedback:**  
This section is conceptually aligned with **AMD-2026-008-ADD-004**, but it is too tentative. “SHOULD declare whether rendered proof is required” and “SHOULD default to browser-visible proof” are not enough for a standard governing session-critical artifacts. It also does not map artifact-level proof declarations to the review-target machinery required by the browser-review addendum.

**Scores:** Cross-Document Consistency: 2, Legal Enforceability: 2, Practical Operability: 2

**Recommendation:**  
Tighten the rule and connect it to the existing review-target framework. Proposed replacement text:

> Each governed artifact record **SHALL** declare whether browser-visible proof is required for approval or promotion.  
> For artifacts that govern user-visible disclosures, voice-first navigation, multi-step session cards, agent controls, or session-critical state transitions, `browser_proof_required` **SHALL** default to `true` unless an explicit policy exception is recorded under **AMD-2026-008-ADD-004 §10**.  
> Where browser proof is required, the artifact record **SHALL** map its `required_visual_proofs` to the applicable review target fields defined in **AMD-2026-008-ADD-004 §6** and audit posture in **§11**.

---

### Relationship to the registry

**Feedback:**  
This section correctly says the standard does not replace **AIOS-SPEC-006**, but it does not define the exact boundary. “The registry should recognize” is especially weak and leaves open whether recognition is mandatory, optional, or future-state. This is the document’s main cross-document coherence problem.

**Scores:** Cross-Document Consistency: 2, Conflict Freedom: 2, Legal Enforceability: 2

**Recommendation:**  
Replace the bullets with a boundary table. Proposed text:

| Concern | Governing authority |
|---------|---------------------|
| Component registration and approval workflow | **AIOS-SPEC-006 §§3–6** |
| Shell layout, overlay positioning, disclosure/player bar, onboarding stability | **AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001 §§4–5** |
| Shell authority, voice-first entry, subordinate tools | **AMD-2026-012 §§4, 8, 9** |
| Intent-driven primary surface and shell/domain boundary | **AMD-2026-007 §11** |
| Browser-visible proof gate | **AMD-2026-008-ADD-004 §§4–11** |
| Governed in-repo voice-first artifact definitions | **This standard** |

Then add:

> **AIOS-SPEC-006** **SHALL** remain the registry authority. A product or registry implementation claiming conformance to this standard **SHALL** preserve stable mapping between each governed `artifact_id` and any corresponding registry `component_id` where such mapping exists.

---

### Final principle

**Feedback:**  
The closing principle is coherent but non-operative. For a governance document, the final section should either summarize conformance or state a binding rule. As written, it reads more like a manifesto sentence than a standard clause.

**Scores:** Style & Clarity: 4, Legal Enforceability: 2

**Recommendation:**  
Replace with a conformance-oriented closing:

> A product implementation **SHALL NOT** claim conformance to the governed voice-first UI artifact kit unless its foundational shell-authority, disclosure, and navigation artifacts are traceable to governed artifact definitions in this standard or a ratified successor.

---

### Missing section: Relationship to Governing Documents

**Feedback:**  
The style guide expects a relationship section, and this document especially needs one because it sits at the intersection of registry, shell layout, shell authority, and browser review. Its absence materially harms coherence.

**Scores:** Cross-Document Consistency: 1, Completeness: 1, Conflict Freedom: 2

**Recommendation:**  
Insert a new section after **Purpose**:

> ## Relationship to governing documents
>
> | Document | Relationship |
> |----------|--------------|
> | **AIOS-SPEC-006** | Defines registry authority, component approval workflow, and mapping discipline for governed artifacts. |
> | **AMD-2026-007** | Constrains intent-driven primary surfaces, shell fallbacks, and shell-vs-domain boundaries that the kit must respect. |
> | **AMD-2026-012** | Constrains Shell authority, voice-first entry, and subordinate tool behavior that the kit must support. |
> | **AMD-2026-008-ADD-004** | Governs browser-visible proof obligations for artifacts requiring visual review. |
> | **AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001** | Governs shell layout, overlay positioning, disclosure/player bar, and multi-step card navigation requirements implemented by kit artifacts. |
> | **AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001** | Informs disclosure, inspectability, and loop-exit expectations for user-facing artifacts where applicable. |

---

### Missing section: Conformance

**Feedback:**  
The document has no conformance section, no failure conditions, and no testable claim boundary. That is a major omission for operability and enforceability.

**Scores:** Practical Operability: 1, Completeness: 1, Developer Synchrony: 2

**Recommendation:**  
Add a final **Conformance** section such as:

> ## Conformance
>
> An implementation is non-conformant with this standard if any of the following hold:
> 1. the canonical artifact definitions do not reside in the governed in-repo library;
> 2. a downstream product repo redefines canonical `artifact_id` or required metadata without ratified authority;
> 3. a governed multi-step artifact omits required navigation controls;
> 4. an artifact requiring browser-visible proof lacks mapped `required_visual_proofs`;
> 5. the implementation cannot trace a consumed artifact to a governed source record and version.
>
> A conformant implementation **SHALL** maintain machine-readable artifact records and versioned traceability from governed source to downstream use.

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | New section after Purpose | Missing relationship map to controlling documents and sections creates major coherence risk. | Add a formal **Relationship to governing documents** table with section-level authority boundaries. | Critical | 1, 5, 6, 8 |
| 2 | Artifact identity rule | No mandatory schema, field typing, or example record exists for the core artifact contract. | Replace the advisory field list with a normative machine-readable schema and example artifact record. | Critical | 3, 5, 7, 9 |
| 3 | Relationship to the registry | Boundary with AIOS-SPEC-006 is vague and uses non-binding language. | Add a boundary table and require stable mapping between `artifact_id` and registry `component_id` where applicable. | Critical | 1, 3, 6, 9 |
| 4 | New final section | No conformance criteria or failure conditions are defined. | Add a **Conformance** section with explicit non-conformance triggers and traceability requirements. | Critical | 3, 5, 7, 9 |
| 5 | In-repo library model | Required files and manifest location are not mandatory or precise enough. | Make the library root contents mandatory and name the manifest and source-trace requirements. | High | 3, 7, 9 |
| 6 | Rendered-proof rule | Proof obligations are too advisory and not tied to AMD-2026-008-ADD-004 review-target mechanics. | Require `browser_proof_required` and mapping to review-target and audit fields. | High | 1, 3, 7, 9 |
| 7 | Artifact family | Taxonomy mixes classes and concrete artifacts without naming rules. | Separate artifact classes from concrete artifact IDs and define the naming scheme. | High | 5, 7, 8, 9 |
| 8 | Multi-step card navigation rule | Current text duplicates another standard and may drift later. | Incorporate AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001 §4.6 by reference instead of restating it. | Medium | 1, 6, 8 |
| 9 | Governing rule / Final principle | Key terms like “silent authority” and “foundational” are rhetorically clear but not enforceable. | Replace with precise conformance language about canonical IDs, metadata, and downstream redefinition limits. | Medium | 3, 8 |
| 10 | Frontmatter | `reference_implementation` category conflicts with the document’s binding normative posture. | Clarify authority in the note or reclassify the document to match its use of SHALL-level requirements. | Medium | 1, 3, 8 |

---

## Final Verdict

**Disposition:** major_revision_required

**Rationale:** The document is directionally strong and coherent with the shell-authority amendments, but it is not yet precise enough to function as a governed standard. Multiple dimensions score at 2, and the absence of a mandatory schema, conformance section, and clear authority boundaries materially undermines enforceability and cross-document coherence.

**Top 3 Actions Required:**
1. Add a mandatory machine-readable artifact schema, including field definitions, allowed values, and an example record.
2. Add explicit boundary and relationship sections tying this standard to AIOS-SPEC-006, AMD-2026-007, AMD-2026-012, AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001, and AMD-2026-008-ADD-004 by section.
3. Add a conformance section with explicit non-conformance triggers, traceability requirements, and browser-proof mapping rules.