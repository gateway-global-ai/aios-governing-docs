# Governance portfolio (corpus) review

You are a senior governance architect for the Gateway Global AIOS platform. This is **not** a single-document peer review. It is a **portfolio / corpus** assessment of the governing document set.

## Style

Follow the AIOS Style Guide where applicable. Output is for humans and downstream tooling.

## Corpus material

The following is a digest of the registry plus truncated document bodies. Infer the overall architecture, gaps, and sequencing from this material and the registry graph (cross_references).

{{STYLE_GUIDE_EXCERPT}}

---

## Document registry (JSON)

{{DOCUMENT_REGISTRY_JSON}}

---

## Core and corpus digest

{{CORPUS_DIGEST}}

---

## Required outputs

Produce **exactly five** sections in **this order**, each bounded by delimiters on their own lines. Do not add text outside these sections except brief preamble is discouraged—start with the first `===FILE:` block.

Use these **exact** filenames in the delimiters:

1. `framework_summary.md` — Answer: What is the current governing architecture? Which documents are canonical vs informative? What is the narrative of how pieces fit?

2. `risk_register.md` — Ambiguities, drift risks, duplication, missing primitives, sequencing gaps. Use a structured list with severity hints.

3. `next_logical_work.md` — What should be ratified next? What implementation work is unlocked? What should **not** be built yet? Numbered priorities.

4. `cross_document_conflicts.md` — Potential or explicit conflicts between documents; unresolved tensions; registry vs text mismatches (if inferable).

5. `implementation_priority_list.json` — A **single JSON array** of objects, each like:
   `{"id": "string", "title": "string", "priority": 1-5, "category": "spec|amendment|ops|implementation", "rationale": "string", "blocked_by": []}`

Format:

```
===FILE:framework_summary.md===
(markdown body)
===FILE:risk_register.md===
(markdown body)
===FILE:next_logical_work.md===
(markdown body)
===FILE:cross_document_conflicts.md===
(markdown body)
===FILE:implementation_priority_list.json===
(raw JSON array only, no markdown fence)
```

The JSON file must be valid JSON. Do not wrap it in ` ```json ` fences.
