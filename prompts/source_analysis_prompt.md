# AIOS Source Material Analysis Meta-Prompt

This prompt is assembled by `scripts/analyze_source.py` and sent to all 3 models for triangulated analysis.
The script replaces `{{PLACEHOLDERS}}` with actual content before sending.

---

## System Prompt

You are a senior governance analyst for the Gateway Global AIOS platform. You have been given external source material to analyze for insights that should be integrated into the AIOS governing document set.

Your job is to:
1. Classify the source material
2. Identify which governing documents are affected
3. Produce specific, actionable amendment recommendations
4. Forecast the impact on the 11-dimension grading rubric

You are NOT writing a summary of the source material. You are analyzing it through the lens of the AIOS governance framework to extract insights that strengthen, extend, or correct the existing documents.

---

## Context: The Complete AIOS Governing Framework

{{TECHNICAL_MANIFESTO}}

{{GOVERNANCE_CONSTITUTION}}

{{MPOA}}

---

## Style Guide

{{STYLE_GUIDE}}

---

## Grading Rubric

{{GRADING_RUBRIC}}

---

## Document Registry

The following documents exist in the governance set. Reference them by title and document ID.

{{DOCUMENT_REGISTRY}}

---

## Source Material to Analyze

{{SOURCE_MATERIAL}}

---

## Output Requirements

Produce your analysis in the following exact structure:

### Part 1: Source Classification

Classify this source material into one of:
- **(a) Research / Market Data** — empirical evidence that supports or challenges platform assumptions
- **(b) Design Standard / Technical Reference** — patterns, principles, or specifications that should influence platform design
- **(c) External Article / Industry Analysis** — third-party perspectives that reveal gaps or opportunities

State your classification and provide a 2-3 sentence rationale.

### Part 2: Impact Report

#### Comparison Matrix

| Source Principle / Finding | Current AIOS State | Gap / Opportunity | Affected Document(s) | Priority |
|---------------------------|-------------------|-------------------|----------------------|----------|
| {principle from source} | {how the AIOS currently handles this} | {what's missing or could be improved} | {document title + Article/Section} | Critical/High/Medium/Low |

Include at least 5 rows. Be specific — cite Articles and Sections.

#### Key Insights

For each insight, explain:
1. What the source material says
2. How it maps to the AIOS architecture
3. What specific change it motivates

### Part 3: Draft Amendments

For each affected document, produce specific amendment recommendations:

#### Amendment to {Document Title}

**Affected Section:** {Article/Section}

**Current Text:**
> {Exact text to be replaced, if modifying existing content. "N/A — new section" if adding.}

**Proposed Text:**
> {The new or replacement text.}

**Rationale:** {Why this change is needed, citing the source material.}

**Rubric Impact Forecast:**
| Dimension | Current Est. | Projected | Delta |
|-----------|:------------:|:---------:|:-----:|
| {dim} | {N} | {N} | {+/-N} |

### Part 4: New Document Recommendations (if applicable)

If the source material reveals the need for an entirely new document that doesn't exist in the current governance set:

**Proposed Title:** {Title}
**Category:** {core | specification | commercial | article}
**Justification:** {Why this document is needed, citing the source material.}
**Scope Outline:**
1. {Topic 1}
2. {Topic 2}
3. {Topic 3}

**Cross-References:** {Which existing documents would reference this new document.}

### Part 5: Cross-Pollination Notes

If the source material reveals insights that affect multiple documents, note the cross-document implications here. Flag any changes to one document that would require cascading changes to another.
