---
review_id: REV-AMD-2026-008-ADD-002-001
document_reviewed: AMD-2026-008-ADD-002
document_version: 0.13.0
reviewer: OpenAI
review_date: 2026-04-08
review_round: 1
review_type: editorial
disposition: approved_with_changes
composite_score: 4.0
---

# Peer Review: AMD-2026-008-ADD-002 — Verbose Grounding, Shell Voice Output Control, and Output Packaging

## Grading Scorecard

| # | Dimension | Score (1-5) | Key Finding |
|---|-----------|:-----------:|-------------|
| 1 | Cross-Document Consistency | 4 | The addendum is largely well-aligned with AMD-2026-008, ADD-001, and ADD-003, but it still uses the legacy V0–V4 labels in Section 4 while the control-plane table and surrounding prose now foreground RESPONSE/SUMMARY/EXPLANATION/BRIEF/BOOK, creating avoidable terminology drift. |
| 2 | Business Model Alignment | 4 | Section 10.11 cleanly separates base authoring from premium enhancement/publishing, but the commercial boundary would be stronger if “comparable premium artifact workflows” were narrowed or cross-referenced more precisely to product policy. |
| 3 | Legal Enforceability | 3 | The document is generally enforceable, but several provisions rely on open-text phrases such as “small sample,” “personal or internal review,” and “equivalent commercial entitlement” without a defined policy hook or objective boundary. |
| 4 | Architectural Fidelity | 4 | The document preserves shell supremacy over verbosity, routing, and traversal and stays orthogonal to ADD-003 composition controls, but Section 9’s “current view class” trigger is underdefined relative to the otherwise disciplined control-plane model. |
| 5 | Completeness | 4 | The document covers its promised scope well, including BOOK workflow and packaging, but it lacks a compact seam clause clarifying how packaging/export requests interact with ADD-003 action semantics for send/publish/export. |
| 6 | Conflict Freedom | 4 | No direct contradictions were found, and the seams with ADD-001 and ADD-003 are mostly respected, though some overlap remains around VC3 “Convert this to a document” versus ADD-003’s ownership of composition class taxonomy. |
| 7 | Practical Operability | 4 | Most controls are implementable, especially Sections 5, 6, and 10, but some gating criteria and state transitions would benefit from more explicit fail-closed language outside the BOOK workflow. |
| 8 | Style & Clarity | 4 | The document is readable and authoritative, but terminology is not fully normalized and a few phrases are broader or more conversational than the style guide prefers. |
| 9 | Developer Synchrony | 4 | The shell-control framing is implementable and coherent with the product snapshot’s control-plane posture, but the document does not yet specify enough observable state or transport expectations for VC mappings and packaging invocation outcomes. |
| 10 | Platform Economics Synchrony | 4 | The premium gating model is commercially coherent and appropriately tied to MPOA, but the entitlement doctrine would benefit from a clearer statement that pricing/tier names are non-normative while gating logic is normative. |
| 11 | Friction Factor | 5 | The document introduces meaningful governance without excessive operational drag, and the phased BOOK workflow is proportionate to the risk of long-form artifact generation. |
| | **Composite Score** | **4.0** | |

---

## Overall Assessment

### Strengths

- **Section 2** states the core doctrine clearly: output depth and narration control belong to the shell, not unconstrained model behavior.
- **Section 3** is strong cross-document architecture: the twelve-axis table now cleanly positions this addendum relative to ADD-001 and ADD-003.
- **Sections 5–6** are the strongest editorial portions of the draft; the VC taxonomy is intuitive, bounded, and operationally useful.
- **Section 10** is substantively strong and internally coherent; the B0–B9 workflow, review state machine, and shell controls create a credible governed BOOK process.
- **Section 10.11** appropriately separates base authoring from premium enhancement/publishing and keeps commercial entitlements subordinate to MPOA and product policy.

### Critical Gaps

- **Section 4** still uses the legacy “V0–V4” labels in headings while the rest of the document and ADD-003 now use the canonical depth names directly; this should be normalized.
- **Section 5.4** risks encroaching on ADD-003 by using examples such as “Convert this to a document” without clarifying that VC3 changes presentation/depth posture but does not itself define composition class.
- **Section 9** includes “the current view class explicitly permits richer output,” but “view class” is not defined in this addendum, AMD-2026-008, or the cited addenda, making the promotion rule less enforceable.
- **Section 10.4** and **Section 10.11.5** use subjective phrases like “small sample” and “personal or internal review” without a policy-defined threshold or explicit delegation clause.
- The document would benefit from one explicit seam clause stating that packaging/export here does not authorize send/publish execution semantics, which remain governed by AMD-2026-008-ADD-003 (Section 12).

---

## Article-by-Article Review

### 0. Status and intent

**Feedback:** This section is concise and effective. The “Does not replace” table is especially strong because it establishes the seam with AMD-2026-008-ADD-001 and AMD-2026-008-ADD-003 early. Editorially, this is one of the cleanest sections in the draft.

**Scores:** Cross-Document Consistency: 5, Style & Clarity: 5, Conflict Freedom: 5

**Recommendation:** No substantive change required. Optionally add “Execution/action semantics remain governed by AMD-2026-008-ADD-003” to the “Does not replace” row for even tighter seam control.

---

### 1. Purpose

**Feedback:** The purpose statement is comprehensive and tracks the actual body well. The list format is useful, but item 3 (“allowed output packaging classes”) and item 5 (“product/commercial gates”) would read more cleanly if grouped as packaging/export and premium BOOK capabilities. The final sentence correctly defers composition classes to ADD-003.

**Scores:** Completeness: 5, Cross-Document Consistency: 4, Style & Clarity: 4

**Recommendation:** Tighten the list for readability. Proposed revision to the opening sentence:
> This addendum defines the governed output-depth ladder, shell-level voice output controls, output packaging classes, and the BOOK-specific review and entitlement gates that apply to long-form governed artifacts.

---

### 2. Governing principle

**Feedback:** This is a strong doctrinal section and one of the best in the document. It clearly centers shell governance and minimum necessary depth. The final sentence in this section is also a good bridge into Section 9. No conflict with AMD-2026-008 or ADD-001 was found.

**Scores:** Architectural Fidelity: 5, Conflict Freedom: 5, Style & Clarity: 5

**Recommendation:** No substantive revision required.

---

### 3. Control-plane model (twelve axes)

**Feedback:** The table is strong and materially improves cross-document coherence. It aligns well with ADD-003 Section 6. The only editorial issue is that Axis 2 uses the canonical names RESPONSE/SUMMARY/EXPLANATION/BRIEF/BOOK, while Section 4 headings still use V0–V4. That mismatch should be removed.

**Scores:** Cross-Document Consistency: 4, Architectural Fidelity: 5, Developer Synchrony: 4

**Recommendation:** Normalize Section 4 headings to match this table. Replace:
> “### 4.1 V0 — RESPONSE”
with:
> “### 4.1 RESPONSE”
and apply the same pattern through Section 4.5. If legacy aliases must remain, place them once in a note such as:
> Legacy aliases V0–V4 MAY be used in implementation history, but the normative labels are RESPONSE, SUMMARY, EXPLANATION, BRIEF, and BOOK.

---

### 4. Output depth ladder

**Feedback:** Substantively sound, but editorially inconsistent with the rest of the document set. The section appears to be in transition from the older V0–V4 ladder to the newer canonical depth names. Because ADD-003 already cites ADD-002 Section 4 as owning “RESPONSE … BOOK,” retaining V0–V4 in the headings creates unnecessary cross-document friction. The content of each depth level is otherwise clear and useful.

**Scores:** Cross-Document Consistency: 3, Style & Clarity: 4, Practical Operability: 4

**Recommendation:** Make the canonical labels primary and demote V0–V4 to historical aliases or remove them entirely. Proposed replacement structure:
> ### 4.1 RESPONSE  
> Smallest valid answer.  
>  
> **Legacy alias (non-normative):** V0
and similarly for the remaining levels.

---

### 5. Shell voice control classes

**Feedback:** This section is strong and operationally useful. The classes are intuitive and map well to shell affordances. The main issue is in **Section 5.4 VC3 — Transform**, where examples such as “Convert this to a document” and “Show as book” risk blurring the seam with ADD-003’s ownership of composition class and composition contract. The section should clarify that VC3 can request a transformed presentation or governed workflow entry, but classification and gating remain elsewhere.

**Scores:** Cross-Document Consistency: 3, Architectural Fidelity: 4, Practical Operability: 4

**Recommendation:** Add a seam sentence to Section 5.4. Proposed text:
> **VC3** MAY request transformation of presentation, depth, or governed workflow entry, but **VC3** **SHALL NOT** by itself redefine composition class, waive composition-contract requirements, or bypass **AMD-2026-008-ADD-003** where artifact classification or action semantics apply.

Also revise the examples to reduce ambiguity:
> Turn this into a summary, Make this a brief, Enter BOOK workflow, Read bullet points

---

### 6. Voice-shell obligations

**Feedback:** This section is clear and implementable. The informative mapping sentence is especially helpful. However, “export or render requests that bind to packaging classes” would be stronger if paired with a non-conflation clause stating that packaging does not itself authorize send/publish actions.

**Scores:** Practical Operability: 4, Conflict Freedom: 4, Developer Synchrony: 4

**Recommendation:** Add a final bullet or sentence:
> Packaging or render selection under this addendum **SHALL NOT** by itself authorize **send**, **publish**, or other execution actions governed by **AMD-2026-008-ADD-003**.

---

### 7. Output packaging classes

**Feedback:** This section is straightforward and mostly clean. The PDF subsection is particularly useful because it distinguishes packaging class from premium quality tier. That said, “simple or personal review PDF” and “publish-ready PDF” should be tied more explicitly to policy or entitlement state to avoid interpretive drift.

**Scores:** Legal Enforceability: 3, Platform Economics Synchrony: 4, Style & Clarity: 4

**Recommendation:** In Section 7.3, replace:
> simple or personal review PDF
with:
> simple review PDF as defined by product policy
and replace:
> publish-ready PDF
with:
> publish-ready or print-ready PDF where product policy and entitlement permit.

---

### 8. Packaging rules

**Feedback:** This section is useful but reads more like guidance than enforceable doctrine. That may be acceptable if intended, but the section should say whether these are defaults, preferences, or mandatory routing rules. As written, “preferred” is softer than the rest of the document.

**Scores:** Legal Enforceability: 3, Practical Operability: 3, Style & Clarity: 4

**Recommendation:** Add a framing sentence:
> The following are default packaging preferences unless policy, workflow, or artifact class requires otherwise.
If stronger doctrine is intended, replace “preferred” with “default” throughout.

---

### 9. Promotion rules

**Feedback:** This section is central and mostly strong, but item 5 introduces “the current view class explicitly permits richer output,” which is not defined in the document or cross-referenced to a governing source. That weakens enforceability and creates implementation ambiguity. The rest of the section is coherent, especially the anti-self-promotion rule into BOOK.

**Scores:** Legal Enforceability: 3, Architectural Fidelity: 4, Practical Operability: 3

**Recommendation:** Either define “view class” in this addendum or replace it with a governed term. Proposed replacement for item 5:
> the active shell surface or workflow state, as defined by product policy, explicitly permits richer output
Better still:
> the active shell control state explicitly permits richer output
if that term exists or will be defined consistently across the addendum set.

---

### 10. BOOK approval and review gates

**Feedback:** This is the strongest substantive section in the document. The phased workflow, state machine, and shell-control requirements are coherent and proportionate. The main editorial/legal issue is the phrase “small sample” in Sections 10.3 and 10.4, which is too open-ended for a governance document unless policy is explicitly delegated to define it.

**Scores:** Completeness: 5, Practical Operability: 5, Legal Enforceability: 4

**Recommendation:** Replace “small sample” with policy-bound language. Proposed text in Sections 10.3 and 10.4:
> beyond a limited pre-approval sample expressly permitted by policy
or
> beyond a policy-defined sample threshold
This preserves flexibility while making the delegation explicit.

---

### 10.11 Base and premium BOOK workflows (product gates)

**Feedback:** This section is commercially coherent and well-structured. It appropriately distinguishes authoring from enhancement and publishing. The main issue is that terms such as “comparable premium artifact workflows,” “equivalent commercial entitlement,” and “public-ready artifacts” are slightly broader than the rest of the document’s otherwise disciplined vocabulary. They should either be narrowed or explicitly delegated to product policy.

**Scores:** Business Model Alignment: 4, Legal Enforceability: 3, Platform Economics Synchrony: 4

**Recommendation:** Tighten the doctrine with explicit policy delegation. Proposed addition to Section 10.11 opening paragraph:
> Product policy **SHALL** define the specific capability bundles, entitlement checks, and artifact classes to which this premium-gating doctrine applies.
Also revise Section 10.11.3:
> MAY require paid membership or equivalent commercial entitlement
to:
> MAY require a paid tier or other commercial entitlement defined by product policy and governed commercial terms.

---

### 11. Non-goals

**Feedback:** This section is concise and useful. It correctly defers navigation primitives and composition classes. One additional non-goal would improve seam clarity: this addendum does not define send/publish execution semantics.

**Scores:** Conflict Freedom: 5, Cross-Document Consistency: 5, Style & Clarity: 5

**Recommendation:** Add one bullet:
> send, publish, approve, or other action semantics for composed artifacts — see **AMD-2026-008-ADD-003**

---

## Summary of Recommendations

| # | Section | Issue | Recommendation | Priority | Dimensions Affected |
|---|---------|-------|----------------|----------|---------------------|
| 1 | Section 4 | Legacy V0–V4 headings conflict with the canonical RESPONSE/SUMMARY/EXPLANATION/BRIEF/BOOK terminology used elsewhere. | Make RESPONSE/SUMMARY/EXPLANATION/BRIEF/BOOK the normative headings and demote V0–V4 to non-normative legacy aliases or remove them. | High | 1, 8 |
| 2 | Section 5.4 | VC3 examples blur the seam with ADD-003’s ownership of composition class and composition contract. | Add a clause stating VC3 does not redefine composition class or bypass ADD-003, and revise examples accordingly. | Critical | 1, 4, 6 |
| 3 | Section 6 / Section 11 | Packaging/export could be misread as authorizing send/publish execution semantics. | Add explicit language that packaging selection does not authorize send/publish; defer those actions to ADD-003. | High | 1, 4, 6, 7 |
| 4 | Section 8 | Packaging rules use soft “preferred” language without clarifying whether they are defaults or mandates. | Frame Section 8 as default packaging preferences unless policy/workflow/artifact class requires otherwise. | Medium | 3, 7, 8 |
| 5 | Section 9 | “Current view class” is undefined and weakens enforceability. | Replace with a defined term such as “active shell control state” or explicitly delegate definition to product policy. | Critical | 3, 4, 7, 8 |
| 6 | Sections 10.3–10.4 | “Small sample” is too vague for a binding governance document. | Replace with “policy-defined sample threshold” or equivalent delegated language. | High | 3, 7, 8 |
| 7 | Section 10.11 | Commercial gating terms are slightly open-text and should be tied more tightly to policy. | Add a sentence requiring product policy to define capability bundles, entitlement checks, and covered artifact classes. | Medium | 2, 3, 10 |
| 8 | Section 11 | Non-goals omit action semantics, leaving one seam implicit rather than explicit. | Add a non-goal bullet deferring send/publish/approve semantics to ADD-003. | Medium | 1, 6, 8 |

---

## Final Verdict

**Disposition:** approved_with_changes

**Rationale:** The document is substantively strong, architecturally coherent, and largely aligned with the surrounding AMD-2026-008 addendum set, but several editorial and seam-control issues should be corrected before ratification, especially the Section 4 terminology drift, the Section 5.4 overlap with ADD-003, and the undefined “view class” trigger in Section 9.

**Top 3 Actions Required:**
1. Normalize Section 4 to the canonical depth labels and remove or demote the legacy V0–V4 terminology.
2. Harden the seam between VC3 transformation and ADD-003 composition-class ownership.
3. Replace undefined or vague triggers such as “current view class” and “small sample” with policy-bound or explicitly defined language.