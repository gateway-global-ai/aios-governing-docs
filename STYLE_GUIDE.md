# AIOS Governing Documents: Writing Style Guide

This guide defines the writing conventions for all AIOS governing documents. It is injected into every AI-driven creation and review prompt to ensure consistency across the document set.

---

## 1. Voice & Tone

- **Authoritative and precise.** These are governance documents, not marketing materials. Every statement should be specific enough to be enforceable or implementable.
- **Third person.** Never use "we," "you," or "I" in specification or governance documents. Use "the Platform," "the Tenant," "the Policy Engine," etc.
- **Present tense for rules.** "The Policy Engine evaluates..." not "The Policy Engine will evaluate..."
- **Future tense only for roadmap items.** Use "will" only when referring to planned but unimplemented features, and mark these clearly as "(in development)" or "(planned)."
- **Active voice for rules and mandates.** "The DCP rejects malformed artifacts" not "Malformed artifacts are rejected by the DCP."
- **Passive voice is acceptable** only for liability statements where the actor is intentionally ambiguous (e.g., "Liability is strictly capped at...").

---

## 2. Document Structure

### Heading Hierarchy

- `# Title` -- Document title (one per document)
- `## Article / Section` -- Major divisions (e.g., "Article I: The Sovereign Architecture")
- `### Subsection` -- Subdivisions within an article
- `#### Detail` -- Rare; use only for deeply nested specifications

### Standard Sections

Every governing document should include:

1. **Title** (H1)
2. **Preamble or Architectural Purpose** -- Why this document exists, what problem it solves
3. **Relationship to Governing Documents** -- Table mapping principles to enforcement mechanisms
4. **Body** -- The substantive content, organized by Articles or numbered sections
5. **Appendix** (if applicable) -- Glossary references, examples, related documents
6. **Governance Footer** -- "This specification is governed by the AIOS Governance Constitution (v1.0)."

### Article Numbering

- Core documents (Manifesto, Constitution, MPOA) use Roman numeral Articles: "Article I," "Article II"
- Specifications use Arabic numbered sections: "1. Architectural Purpose," "2. Relationship to Governing Documents"
- Subsections use nested numbering within Articles: "Section 1," "Section 2" or "### a.," "### b."

---

## 3. Terminology

### Canonical Terms

All terms are governed by the Appendix glossary in the Technical Manifesto. The following terms are always capitalized and used consistently:

| Term | Usage | Never Use |
|------|-------|-----------|
| NodeContract | Always one word, PascalCase | Node Contract, node contract, NC |
| PolicyRecord | Always one word, PascalCase | Policy Record, policy record, PR |
| SkillPrimitive | Always one word, PascalCase | Skill Primitive, skill |
| Kit | Always capitalized | kit, package, bundle |
| Stateful Shell | Two words, both capitalized | shell, the shell, stateful shell |
| Compute Kernel | Two words, both capitalized | kernel, the kernel |
| Policy Engine | Two words, both capitalized | policy engine, PE |
| Development Control Plane (DCP) | Spell out on first use, then DCP | dev control plane |
| Governance Council | Two words, both capitalized | the council, governance council |
| Tenant | Always capitalized when referring to an enterprise customer | tenant, customer, user |
| Vendor | Always capitalized when referring to a third-party Kit developer | vendor, developer |
| IntentKey | Always one word, PascalCase | Intent Key, intent key |
| RenderDirective | Always one word, PascalCase | Render Directive |
| Funded Data Account | Three words, all capitalized | funded data account, FDA |
| Shadow Mode | Two words, both capitalized | shadow mode, test mode |
| Tier 3 | Always "Tier 3" (capitalized, with space) | tier 3, T3 |
| MCP | Model Context Protocol; spell out on first use | mcp |
| MPOA | Master Platform Operating Agreement; spell out on first use | mpoa |

### Acronyms

- Spell out on first use with the acronym in parentheses: "Master Platform Operating Agreement (MPOA)"
- After first use, the acronym alone is acceptable
- Never introduce an acronym that is used fewer than 3 times in the document

### New Terms

- Any new term must be defined in the document where it is introduced
- If the term will be used across multiple documents, it must be added to the Technical Manifesto's Appendix glossary
- Bold the term on its first defining use: **"Funded Data Account"**

---

## 4. Cross-Referencing

### Citing Other Governing Documents

Always cite by full document title and specific Article/Section:

**Correct:**
- "as defined in the Governance Constitution (Article II, Section 2)"
- "per the Master Platform Operating Agreement (Article III)"
- "the Technical Manifesto (Article I) establishes..."

**Incorrect:**
- "as defined in the Constitution"
- "per the MPOA"
- "see the other document"

### Internal Cross-References

When referencing a section within the same document:
- "See Section 3 above" or "as defined in Article I"

### Reference Format in Tables

Use the `relationship` field when documenting cross-references in front matter:
- `constrained_by` -- This document's rules are bounded by the referenced document
- `incorporated_by` -- This document is incorporated by reference into the referenced document
- `implements` -- This document implements principles from the referenced document
- `amends` -- This document modifies the referenced document
- `extends` -- This document adds capabilities defined in the referenced document

---

## 5. Formatting Rules

### Text Formatting

- **Bold** for defined terms on first use, section labels ("**Strengths:**"), and emphasis on critical rules
- *Italics* for document titles when referenced inline, Latin phrases, and technical terms being introduced conceptually
- `Backticks` for code identifiers: `node_id`, `aios validate`, `mcp:aios:registry_list`, `SessionContext`
- Blockquotes (`>`) for mandates, agent instructions, and verbatim rules that must be followed exactly

### Tables

Use tables for:
- Comparison matrices (principle vs. enforcement mechanism)
- Term definitions
- Feature/capability listings
- Review scorecards

Always include a header row. Align columns for readability.

### Code Blocks

- Use fenced code blocks (```) with language identifier for JSON schemas, CLI examples, and configuration
- JSON schemas use `json` language tag
- CLI examples use `bash` language tag
- Architecture diagrams use plain ``` (no language tag) for ASCII art

### Lists

- Use bullet points (`*` or `-`) for unordered lists
- Use numbered lists (`1.`, `2.`) for sequential steps, ordered processes, or ranked items
- Nested lists should not exceed 2 levels of depth

---

## 6. Prohibited Patterns

- **No marketing language in specifications.** "Revolutionary," "game-changing," "unprecedented" have no place in governance documents. State facts and rules.
- **No undefined acronyms.** Every acronym must be spelled out on first use.
- **No vague quantifiers.** Replace "reasonable efforts" with specific SLAs. Replace "timely" with "within 72 business hours." Replace "generally" with specific conditions.
- **No passive voice in rules.** "The Kernel rejects..." not "It is rejected by..."
- **No first/second person** in governance or specification documents. Articles and research may use first person sparingly.
- **No duplicate glossary entries.** If a term is defined in the Technical Manifesto Appendix, reference it; do not redefine it.
- **No unattributed claims.** Market data, statistics, and competitive claims must cite sources.

---

## 7. Document Categories & Conventions

| Category | Naming Convention | Structure | Voice |
|----------|-------------------|-----------|-------|
| Core (Manifesto, Constitution, MPOA) | `{descriptive_name}.md` | Articles with Roman numerals, Sections | Formal, legally precise |
| Specification | `{PascalCaseName}.md` | Numbered sections, JSON schemas, examples | Technical, implementor-facing |
| Commercial | `{PascalCaseName}.md` | Numbered sections, checklists | Legal, vendor/enterprise-facing |
| Amendment | `amendment_{description}.md` | Rationale, affected docs, redline changes | Precise, change-focused |
| Article | `{snake_case_name}.md` | Free-form sections, data tables | Analytical, research-oriented |
| Reference | `{UPPER_CASE_NAME}.md` | Free-form | Instructional |

---

## 8. Review & Amendment Language

When writing peer reviews:
- Use the 11-dimension grading rubric defined in `templates/grading_rubric.md`
- Score every dimension with a specific 1-5 integer, never ranges or approximations
- Provide a "Key Finding" for each score that explains the rating in one sentence
- Recommendations must be specific: cite the exact Article/Section to change and propose specific language

When writing amendments:
- Always include "Old Text" and "New Text" for each change
- Cite the source material that motivated the amendment
- State the affected grading dimensions and the expected score impact

---

**This Style Guide is governed by the AIOS Governance Constitution (v1.0).**
Changes to this guide must follow the Constitution's legislative process.
