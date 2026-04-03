# AIOS Peer Review Grading Rubric

This rubric defines the 11 dimensions used to evaluate every AIOS governing document. It is injected into every peer review prompt to ensure all reviewers (human and AI) grade on the same scale.

---

## Scale Definition (All Dimensions)

| Score | Label | Meaning |
|:-----:|-------|---------|
| **5** | Exemplary | Sets the standard. No issues found. Could be cited as a reference for other documents. |
| **4** | Strong | Meets all requirements with only minor stylistic or editorial suggestions. No substantive gaps. |
| **3** | Acceptable | Functionally sound but has identifiable gaps, ambiguities, or inconsistencies that should be addressed before ratification. |
| **2** | Major Issues | Significant problems that undermine the document's purpose. Requires substantial revision in this dimension. |
| **1** | Critical Failure | Fundamentally broken in this dimension. Contains contradictions, missing critical sections, or actively conflicts with other governing documents. |

---

## Dimension Definitions

### 1. Cross-Document Consistency

Does this document use terminology, defined terms, and structural patterns consistent with the governing set? Does it reference other documents by correct title, Article, and Section? Does it use the canonical glossary from the Technical Manifesto Appendix without inventing new terms or redefining existing ones?

**Score 5:** Every term matches the glossary. Every cross-reference cites the correct Article/Section. Structural patterns (heading hierarchy, table formats) mirror the existing set.
**Score 3:** Most terms are correct but 2-3 inconsistencies exist. Some cross-references are vague ("see the Constitution" instead of citing Article/Section).
**Score 1:** Invents new terms that conflict with the glossary. References documents by wrong names or nonexistent sections. Structural patterns diverge significantly from the set.

### 2. Business Model Alignment

Does this document support the overall platform strategy: marketplace (not product factory), vendor ecosystem, enterprise adoption, and Kit-based distribution? Does it avoid language that contradicts the partnership-first positioning?

**Score 5:** Reinforces the marketplace model. Language encourages vendor participation and enterprise adoption. No contradictions with commercial strategy.
**Score 3:** Generally aligned but contains language that could be interpreted as platform-centric rather than ecosystem-centric. Minor tensions with the partnership model.
**Score 1:** Actively undermines the marketplace model. Contains language that would deter vendors or enterprises. Contradicts the "governed execution environment" positioning.

### 3. Legal Enforceability

Are the rules specific enough to survive legal scrutiny? Are liability boundaries explicit? Are defined terms used precisely? Would this hold up in the Delaware arbitration venue defined in the MPOA? Are there weasel words ("reasonable efforts," "generally," "may") where binding language is needed?

**Score 5:** Every rule is specific and enforceable. Liability boundaries are explicit. Defined terms are used precisely. No weasel words in binding contexts.
**Score 3:** Most rules are enforceable but 2-3 provisions use vague language. Some liability boundaries are implicit rather than explicit.
**Score 1:** Multiple provisions are unenforceable due to vague language. Liability boundaries are missing or contradictory. Key terms are used inconsistently.

### 4. Architectural Fidelity

Does this document accurately reflect the Technical Manifesto's architecture: separation of powers (Lawmaking/Executive/Judicial), stateless compute, UI sovereignty, policy supremacy, deterministic execution, MCP integration? Does it introduce any concepts that violate the Execution Laws?

**Score 5:** Perfect alignment with the Technical Manifesto. Every architectural reference is accurate. No concepts violate the Execution Laws.
**Score 3:** Generally aligned but introduces 1-2 concepts that are ambiguous relative to the Manifesto. Does not explicitly violate the Execution Laws but could be misinterpreted.
**Score 1:** Contradicts the Technical Manifesto. Introduces concepts that violate separation of powers or policy supremacy. Misrepresents the architecture.

### 5. Completeness

Does this document cover everything its entry in the 12-document plan (`introduction.md`) promises? Are there sections that the plan describes but the document omits? Are edge cases addressed? Are failure modes defined?

**Score 5:** Covers every item described in the plan. Edge cases are addressed. Failure modes are defined with specific recovery procedures.
**Score 3:** Covers the core requirements but omits 2-3 items from the plan. Some edge cases are unaddressed. Failure modes are mentioned but not fully specified.
**Score 1:** Missing entire sections promised by the plan. Major edge cases are unaddressed. No failure mode definitions.

### 6. Conflict Freedom

Does this document contradict any other governing document? Does it respect the Supremacy Clause (Constitution for governance, MPOA for liability/economics, Manifesto for architecture)? If it touches multiple domains, are the boundaries clear?

**Score 5:** No contradictions with any other document. Supremacy Clause is respected. Domain boundaries are explicit.
**Score 3:** No direct contradictions but 1-2 provisions create tension with other documents. Supremacy Clause is implicitly respected but not explicitly acknowledged.
**Score 1:** Direct contradictions with other governing documents. Violates the Supremacy Clause. Domain boundaries are blurred.

### 7. Practical Operability

Could a real developer, enterprise customer, or AI agent actually follow these rules? Are SLAs specific (numbers, not "timely")? Are processes step-by-step? Are thresholds defined? Would this document work on day one of platform launch?

**Score 5:** Every rule is actionable. SLAs have specific numbers. Processes are step-by-step with clear inputs and outputs. Ready for day-one use.
**Score 3:** Most rules are actionable but 2-3 provisions are too abstract to implement without interpretation. Some SLAs lack specific numbers.
**Score 1:** Rules are aspirational rather than operational. SLAs are vague. Processes are described at a high level without actionable steps.

### 8. Style & Clarity

Does the writing follow the Style Guide? Is it precise and unambiguous? Free of marketing language in specification contexts? Correct heading hierarchy? Proper use of bold, backticks, and blockquotes? Third person, present tense for rules?

**Score 5:** Perfect adherence to the Style Guide. Precise, unambiguous, well-structured. No marketing language. Correct formatting throughout.
**Score 3:** Generally follows the Style Guide but has 3-5 formatting inconsistencies. Minor ambiguities. Occasional lapses in voice or tense.
**Score 1:** Does not follow the Style Guide. Marketing language in specifications. Inconsistent formatting. Ambiguous or unclear language throughout.

### 9. Developer Synchrony

How well does this document serve developers and AI agents? Can they read it and know exactly what to build, what CLI commands to run, what schemas to follow? Is it consistent with the CLI Guide, AIP, agents.md, and the NodeContract/PolicyRecord specs?

**Score 5:** A developer or agent could implement from this document alone. Schemas are complete. CLI commands are referenced. Consistent with all developer-facing docs.
**Score 3:** Provides useful guidance but requires consulting 2-3 other documents to implement. Some schemas or commands are missing.
**Score 1:** A developer would not know where to start. Missing schemas, examples, or CLI references. Inconsistent with developer-facing docs.

### 10. Platform Economics Synchrony

Does this document correctly represent the economic mechanics: thin slice (max 2.5% GTV), 2x multiplier on external intelligence, Shadow Mode ($0 tolls but 2x on live external calls), Funded Data Accounts, BYOK? Does it avoid creating perverse incentives or hidden costs?

**Score 5:** Economic mechanics are accurately represented. No perverse incentives. Pricing and billing are transparent and consistent with the MPOA.
**Score 3:** Economic mechanics are generally correct but 1-2 details are imprecise or could create confusion about costs.
**Score 1:** Economic mechanics are wrong or contradictory. Creates perverse incentives. Pricing is opaque or inconsistent with the MPOA.

### 11. Friction Factor

How much unnecessary friction does this document introduce? Are there approval gates, processes, or requirements that slow adoption without proportional safety or governance benefit?

**Score 5:** Minimal friction. Lean processes that balance governance with developer velocity. Approval gates are proportional to risk.
**Score 3:** Some friction that could be reduced without compromising governance. 1-2 processes are heavier than necessary.
**Score 1:** Excessive bureaucracy. Multiple approval gates with no clear risk justification. Would deter ecosystem participation.

---

## Composite Score Calculation

The composite score is the arithmetic mean of all 11 dimension scores, rounded to one decimal place.

## Disposition Rules

The disposition is determined by the dimension scores, not the composite alone:

| Disposition | Criteria |
|-------------|----------|
| **Approved** | No dimension below 4. Composite >= 4.0. |
| **Approved with Changes** | No dimension below 3. Composite >= 3.5. |
| **Major Revision Required** | Any dimension at 1, OR two or more dimensions at 2, OR composite below 3.0. |

---

**This rubric is governed by the AIOS Governance Constitution (v1.0).**
