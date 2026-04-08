---
document_id: AIOS-REPO-TAXONOMY-001
version: 0.2.3
status: draft
category: reference
title: Intent-bearing repository taxonomy — implementation note and migration appendix
author: Gateway Global AIOS
created: 2026-04-08
last_updated: 2026-04-08
cross_references:
  - doc_id: AMD-2026-013
    title: Intent-Bearing Repository Taxonomy (Architecture and Builder Control)
  - doc_id: AIOS-AMD-PLAN-001
  - doc_id: AIOS-EXEC-DEMO-001
  - doc_id: AIOS-COMMITTEE-BRIEF-AMD-2026-013
    title: Committee review brief — intent-bearing repository taxonomy (AMD-2026-013)
amendment_history:
  - version: 0.2.3
    date: 2026-04-08
    summary: "§F conformance hook (non-normative); aligned with AMD-2026-013 v0.2.3 Round 2 freeze."
  - version: 0.2.2
    date: 2026-04-08
    summary: "Frozen in lockstep with AMD-2026-013 v0.2.2 for peer review Round 1 — no substantive edits until peer review completes unless amendment requires revision."
  - version: 0.2.1
    date: 2026-04-08
    summary: "Committee submission packet cross-reference; aligned with AMD-2026-013 v0.2.1."
  - version: 0.2.0
    date: 2026-04-08
    summary: "Aligned with AMD-2026-013 v0.2.0 — normative boundary, applicability, ambiguous-path handling, operational constraints."
  - version: 0.1.0
    date: 2026-04-08
    summary: "Initial draft — classified path model, builder duties, migration phases, reviews/ examples; non-normative until AMD-2026-013 ratifies principles."
---

# AIOS-REPO-TAXONOMY-001 — Intent-bearing repository taxonomy

**Status:** draft implementation memo — operational detail for [AMD-2026-013](../../amendments/AMD-2026-013.md) **v0.2.3**. **Frozen** with the amendment for **peer review Round 2** (same freeze window). Normative law resides in the amendment; this memo may be revised for clarity after peer review unless the amendment requires substantive change.

## A. Normative boundary and applicability

- **Law vs guidance:** [AMD-2026-013](../../amendments/AMD-2026-013.md) states authority, applicability to **declared** taxonomies, and non-exclusivity (paths do not replace intent primitives, metadata, or transactions). This memo proposes **target** paths, **slug** conventions, and **migration** phases; it is not a substitute for ratified amendment text.
- **Where this binds:** Classification rules in sections B and E apply to **new** work and **staged** migrations once the architecture has **declared** the corresponding class in this memo (or a successor registry). **Undeclared** or **legacy** subtrees remain valid until migrated per [AMD-2026-013](../../amendments/AMD-2026-013.md) §5 and the migration map below.
- **Non-exclusivity:** Intent may be carried in front matter, YAML review targets, and execution transactions; paths provide **durable** scaffolding for **placement** and **discovery** where the architecture adopts them.

---

## B. Classified path model (proposed)

### Governing repository (`aios-governing-docs`) — target layout

| Class | Target path prefix | Intent expressed |
|-------|-------------------|------------------|
| Amendment peer review | `reviews/amendments/<slug>/` | Binding AMD triangulation workspace (slug aligns with existing `reviews/amd_*` convention — migration pending) |
| Specification peer review | `reviews/specifications/<slug>/` | SPEC and core document review tracks |
| Composite package | `reviews/packages/<composite_slug>/` | Coordinated multi-document reviews (e.g. AMD + SPEC) |
| Reference / process | `reviews/reference_docs/<slug>/` | Process documents (e.g. AIOS-DEV-PROC-001), conformance packets, pilots |
| Demo / sample execution | `reviews/demos/<slug>/` | AIOS-EXEC-DEMO-001 packets; non-authoritative process validation |
| Legacy (ambiguous) | `reviews/archive/legacy_flat_reviews/<slug>/` | Topic slugs without canonical `document_id` until reclassified |

### Conventions (new work)

- Lowercase only; underscores only; no spaces in folder names.
- Slugs **should** embed canonical IDs where known (e.g. `amd_2026_012`), not raw display titles.
- Composite packages **shall** document an explicit `composite_slug` in the package README (see AMD-2026-011 + AIOS-SPEC-013 pattern).

### Product repositories

Product trees **should** mirror intent classes under `docs/` or agreed roots per AIOS-DEV-PROC-001 when ratified. This memo does not mandate product tree structure while the amendment remains draft.

---

## Builder responsibilities

| Responsibility | Owner |
|----------------|--------|
| Apply declared taxonomy to new folders | Builder |
| Execute migrations with migration map and CHANGELOG / git traceability | Builder |
| Refuse unclassified new roots under `reviews/` without architecture alignment | Builder and maintainer policy |
| Define or change classes and prefix rules | Architecture role; update this memo or AMD-2026-013 if normative change is required |
| Maintain `CLASSIFICATION_AND_MIGRATION.md` (or successor) for ambiguous and legacy paths | Builder |

---

## Migration phases

| Phase | Action | Status (as of this memo) |
|-------|--------|---------------------------|
| 1 | Policy plus `reviews/demos/` for demo execution packets | Done — see [`reviews/CLASSIFICATION_AND_MIGRATION.md`](../../reviews/CLASSIFICATION_AND_MIGRATION.md) |
| 2 | Amendment folders `amd_*` → `reviews/amendments/` (or normalize in place per decision) | Deferred — high link surface; requires migration map and peer-review path updates |
| 3 | Specification topic folders → `reviews/specifications/` | Deferred — verify `document_id` per folder |
| 4 | Composite `AMD-2026-011-AIOS-SPEC-013` → `reviews/packages/...` | Deferred — explicit composite slug and committee alignment |
| 5 | Legacy unclear → `archive/legacy_flat_reviews/` or reclassify | Deferred — committee input |

---

## Compatibility and legacy handling

- Git history preserves old paths; human migration tables in [`CLASSIFICATION_AND_MIGRATION.md`](../../reviews/CLASSIFICATION_AND_MIGRATION.md) preserve interpretability for **ambiguous** paths (historical slugs, mixed-class roots).
- No deletion of authoritative review artifacts without archive copy or documented supersession.
- The execution runner `--review-slug` accepts multi-segment paths (e.g. `demos/demo_exec_ui_review`) so classification prefixes do not require separate code forks.
- **Dual-read period:** During migration, automation **should** accept both old and new paths where documented in the migration map until the builder retires the old path.

---

## Safe first slice (completed)

- `reviews/demos/` created; `demo_exec_*` samples moved under `reviews/demos/<leaf>/`.
- [`reviews/README.md`](../../reviews/README.md) operational policy; runner and templates updated for `demos/` slug.
- No amendment or spec review folder moves in that slice.

---

## Examples — `reviews/` tree

| Example | Path | Class |
|---------|------|-------|
| Execution demo packet | `reviews/demos/demo_exec_ui_review/planning/REVIEW_TARGET.yaml` | Demo — intent-bearing review target declared in YAML |
| Amendment review (current) | `reviews/amd_2026_012/round_2/` | Amendment — target path `reviews/amendments/amd_2026_012/` pending Phase 2 |
| Process packet | `reviews/aios_dev_conformance_process/` | Reference / process — target under `reviews/reference_docs/...` pending Phase 2 and mapping |
| Classified demo root | `reviews/demos/demo_exec_ui_review/` | Same demo, showing `reviews/demos/<leaf>/` prefix after Phase 1 |

---

## C. Architecture agent impact — separation of duties

Normative summary: see [AMD-2026-013 §6](../../amendments/AMD-2026-013.md).

- The **architecture role** defines taxonomy rules and documents them here and in planning prompts as needed.
- The **builder** maintains the tree according to those rules and the migration map.
- **Implementation** and **execution** agents **consume** paths as declared; they do **not** create new intent classes at repository roots without architecture update.
- **Review lanes** (peer review, execution packet review) evaluate artifacts in stable locations; repository-wide refactors without architecture update do not change normative meaning.

---

## D. Committee routing note

| Question | Answer |
|----------|--------|
| Why committee? | Control-plane authority (who defines repository semantics) and alignment with intent and shell governance. |
| Safe before approval? | Draft AMD-2026-013, this memo, non-destructive `reviews/demos/` pattern, documentation links. |
| Wait for committee? | Claims that taxonomy is mandatory law; organization-wide migration deadlines; binding product-repo requirements beyond **should**. |

See [AMD-2026-013 §7](../../amendments/AMD-2026-013.md) for the full routing section.

**Committee submission packet:** [AIOS-COMMITTEE-BRIEF-AMD-2026-013](COMMITTEE-REVIEW-BRIEF-AMD-2026-013.md) — fit assessment, scoring risks, v0.2.0 delta, questions, recommended order vs peer review.

---

## E. Migration appendix

### E.1 Classified review tree categories

| Category | Description | Deferred? |
|----------|-------------|-----------|
| amendment | AMD peer review workspace | Move deferred — link audit required |
| specification | SPEC / core doc reviews | Deferred |
| composite_package | Multi-document coordinated review | Deferred — `AMD-2026-011-AIOS-SPEC-013` is an explicit composite |
| reference_or_process_doc | Conformance, pilots, process | Deferred |
| demo_sample | Execution lane samples | First slice done — `reviews/demos/` |
| legacy_unclear | Topic slug without ID | Archive or reclassify — deferred |

### E.2 Canonical slug conventions (new work)

- **Amendments:** `amd_<year>_<nnn>` lowercase underscores (`amd_2026_012`).
- **Demos:** `demos/demo_exec_<descriptor>` under `reviews/` (runner `--review-slug demos/demo_exec_...`).
- **Composite:** `amd_<id>_aios_spec_<id>` or an explicit documented slug in the package README — do not infer from folder name alone without README confirmation.

### E.3 What is deferred

- Amendment folders `amd_*` at `reviews/` root — migrate after AMD-2026-013 progress and link inventory.
- Uppercase `AMD-2026-005`, `AMD-2026-011-AIOS-SPEC-013` — normalize only with migration map.
- Topic slugs (`technical_manifesto`, etc.) — map to `document_id` or archive.

### E.4 What moved first

- `reviews/demos/` only — demo execution packets for AIOS-EXEC-DEMO-001.

### E.5 Legacy and ambiguous paths

- Preserved in place until reclassified; no blind bulk rename.
- Operational audit lives in [`CLASSIFICATION_AND_MIGRATION.md`](../../reviews/CLASSIFICATION_AND_MIGRATION.md); this appendix aligns with that audit and may be updated as migrations progress.

---

## F. Conformance and validation (operator guidance, non-normative)

This section is **not** new binding law; it records **optional** hooks aligned with [AMD-2026-013](../../amendments/AMD-2026-013.md) §2.1.3.

- **Optional automation:** CI or `scripts/governance_integrity_check.py` may flag new top-level folders under `reviews/` that do not match a declared class or a documented exception in [`CLASSIFICATION_AND_MIGRATION.md`](../../reviews/CLASSIFICATION_AND_MIGRATION.md). Remediation remains human—architecture/builder alignment—not silent auto-rename.
- **Dual-read:** During migration, keep old/new path pairs documented in the migration map until the builder retires the old path.

---

## Cross-references

| Document | Purpose |
|----------|---------|
| [AMD-2026-013](../../amendments/AMD-2026-013.md) | Draft amendment — normative principles |
| [AIOS-COMMITTEE-BRIEF-AMD-2026-013](COMMITTEE-REVIEW-BRIEF-AMD-2026-013.md) | Committee review packet — submission readiness |
| [`reviews/CLASSIFICATION_AND_MIGRATION.md`](../../reviews/CLASSIFICATION_AND_MIGRATION.md) | Operational migration map and policy |
| [AIOS-EXEC-DEMO-001](AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md) | Execution lane — `demos/` slug |

---

*End of AIOS-REPO-TAXONOMY-001 v0.2.3 draft.*
