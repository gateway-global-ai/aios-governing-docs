---
amendment_id: AMD-{NNN}
title: {Amendment Title}
type: amendment_to_existing | new_document_recommendation
status: draft | under_review | ratified | rejected
source_material: {path to source in sources/ or null}
affected_documents:
  - { doc_id: "{AIOS-XXX-NNN}", doc_title: "{Title}" }
created: {YYYY-MM-DD}
author: {name/model}
ratification_date: null
---

# Amendment: {Title}

## 1. Rationale

{Why this amendment is needed. Cite the source material that motivated it, if applicable.}

---

## 2. Source Material

**Source:** {Title or description of the external article, research, or analysis that motivated this amendment.}
**Path:** `{sources/{name}/source.md}` or N/A
**Impact Report:** `{sources/{name}/impact_report_consolidated.md}` or N/A

---

## 3. Proposed Changes

{For `amendment_to_existing` type:}

### Change 1: {Brief Description}

**Affected Document:** {Document Title} ({Document ID})
**Affected Section:** {Article/Section reference}

**Old Text:**
> {Exact text being replaced, quoted verbatim.}

**New Text:**
> {Proposed replacement text.}

**Rubric Impact Forecast:**
| Dimension | Current Estimated Score | Projected Score | Delta |
|-----------|:----------------------:|:---------------:|:-----:|
| {Affected dimension} | {N} | {N} | {+/-N} |

---

### Change 2: {Brief Description}

{Repeat the above structure for each change...}

---

{For `new_document_recommendation` type:}

## 3. New Document Proposal

**Proposed Title:** {Title}
**Category:** {core | specification | commercial | article}
**Target Audience:** {Who will read this document}
**Scope Outline:**
1. {Section 1 topic}
2. {Section 2 topic}
3. {Section 3 topic}

**Justification:** {Why this document is needed and how it fills a gap in the current governance set.}

**Cross-References:** {Which existing documents would reference or be referenced by this new document.}

---

## 4. Cross-Document Impact

{List any cascading changes required in other documents if this amendment is ratified.}

| Document | Required Change | Priority |
|----------|----------------|----------|
| {Document Title} | {Brief description of cascading change} | {High/Medium/Low} |

---

## 5. Ratification Requirements

Use this checklist against the **ratified** workspace and lifecycle rules in **[AMD-2026-005](../amendments/AMD-2026-005.md)** and the emission/ratification language in **AIOS-SPEC-003** §§7–10.

- [ ] **Author pre-validation** completed (self-check against amendment scope before submission)
- [ ] **Triangulated peer review** completed (Round 1 or as required by document tier; record scores)
- [ ] **Thresholds met:** composite **≥ 3.5** and **no dimension below 3** (see `grading_rubric.md`)
- [ ] Round 2 peer review completed **only if** required by the **Governance Constitution** or document class for that tier—not as a mandatory “human audit after peer review”
- [ ] No unresolved conflicts with existing ratified documents
- [ ] **No post–peer-review human audit** required **solely** to satisfy workflow once the above thresholds are met; **ratification** follows the constitutional / Council path for the tier involved
- [ ] If this amendment touches Amendment Program UI or governed surfaces, confirm alignment with **AIOS-SPEC-006** §§8–12 where applicable

**Clarification:** “Human ratification” means **tier-appropriate approval** (e.g. Council, dual-signature for Tier 3)—not an extra governance audit step after peer review scores already satisfy thresholds.

---

**This amendment is governed by the AIOS Governance Constitution (v1.0).**
