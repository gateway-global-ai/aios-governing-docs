# Reviews tree — classification, migration map, and policy

**Status:** governance infrastructure (non-normative).  
**Purpose:** Make `reviews/` scalable and classifiable; preserve traceability; avoid blind renames.

**Normative framing (draft):** Intent-bearing repository taxonomy and architecture/builder authority are stated in **[AMD-2026-013](../amendments/AMD-2026-013.md)**; operational detail is in **[AIOS-REPO-TAXONOMY-001](../reference/implementation/AIOS-REPO-TAXONOMY-001.md)**. This document remains the operational migration map until superseded.

---

## A. Audit — current top-level folders under `reviews/`

Alphabetical (as of hygiene pass):

| Folder | Preliminary class |
|--------|-------------------|
| `aios_dev_conformance_process` | reference_or_process_doc |
| `amd_2026_006` | amendment |
| `amd_2026_007` | amendment |
| `amd_2026_008` | amendment |
| `amd_2026_009` | amendment |
| `amd_2026_009_add_001` | amendment (composite slug — addendum) |
| `amd_2026_010` | amendment |
| `amd_2026_012` | amendment |
| `AMD-2026-005` | amendment (legacy naming — uppercase) |
| `AMD-2026-011-AIOS-SPEC-013` | **composite_package** (`AMD-2026-011` + `AIOS-SPEC-013` — explicit in `round_1/README.md`) |
| `demo_exec_packet_no_git` | demo_sample *(moved to `demos/` in first slice)* |
| `demo_exec_packet_samples` | demo_sample *(moved to `demos/` in first slice)* |
| `demo_exec_packet_wt_full` | demo_sample *(moved to `demos/` in first slice)* |
| `demo_exec_packet_wt_skip` | demo_sample *(moved to `demos/` in first slice)* |
| `demo_exec_ui_review` | demo_sample *(moved to `demos/` in first slice)* |
| `executionscopeandcontextbounding` | legacy_unclear (topic slug; no canonical doc ID in folder name) |
| `googleworkspaceintegrationgovernance` | legacy_unclear |
| `governance_constitution` | specification (topic-named; maps to `core/governance_constitution.md` — verify) |
| `intent_primitive_execution_model` | legacy_unclear |
| `kernel_shadow` | reference_or_process_doc (pilot coordination) |
| `local_tts_runtime_standard` | specification (topic-named; maps to `specifications/` or `commercial/` — verify) |
| `master_platform_operating_agreement` | specification |
| `ollama_runtime_standard` | specification |
| `technical_manifesto` | specification |
| `whisper_runtime_standard` | specification |

### Naming patterns observed

- **Lowercase `amd_YYYY_NNN`:** dominant for current amendment tracks.
- **Uppercase `AMD-YYYY-NNN`:** legacy (`AMD-2026-005`, composite package folder).
- **Topic slugs (no AMD/SPEC ID):** `technical_manifesto`, `googleworkspaceintegrationgovernance`, etc. — **ambiguous without explicit mapping** to `document_id` in front matter.
- **Hyphens vs underscores:** mixed; target policy uses **lowercase + underscores only** for *new* paths.
- **Composite:** `AMD-2026-011-AIOS-SPEC-013` is explicitly a **two-document package** (not a single-amendment slug).

---

## B. Target classified layout (durable)

| Class | Target path | Notes |
|-------|-------------|--------|
| Amendment | `reviews/amendments/<slug>/` | `<slug>` e.g. `amd_2026_012` (lowercase) |
| Specification | `reviews/specifications/<slug>/` | `<slug>` derived from document ID or stable file slug |
| Composite package | `reviews/packages/<composite_slug>/` | e.g. `amd_2026_011_aios_spec_013` (define convention before move) |
| Reference / process | `reviews/reference_docs/<slug>/` | e.g. `aios_dev_conformance_process` |
| Demo / sample | `reviews/demos/<slug>/` | **Never** at `reviews/` root |
| Legacy / unclear | `reviews/archive/legacy_flat_reviews/<slug>/` | Only after explicit reclassification |

**Rules:** lowercase; underscores only; no spaces; no raw display titles; canonical IDs where known; composite packages must use an explicit naming convention.

---

## C. Migration map (every current top-level folder)

| Current path | Proposed class | Proposed new path | Confidence | Rationale | When | Stub? |
|----------------|----------------|-------------------|------------|-----------|------|-------|
| `aios_dev_conformance_process` | reference_or_process_doc | `reviews/reference_docs/aios_dev_conformance_process/…` | medium | Clear process-doc review; many links in repo | **Defer** | optional redirect after move |
| `amd_2026_006` … `amd_2026_012`, `amd_2026_009_add_001` | amendment | `reviews/amendments/<same_slug>/` | high | Straightforward | **Defer** — high link surface | yes |
| `AMD-2026-005` | amendment | `reviews/amendments/amd_2026_005/` (normalize case) | medium | Uppercase legacy; **defer** until link audit | **Defer** | yes |
| `AMD-2026-011-AIOS-SPEC-013` | composite_package | `reviews/packages/amd_2026_011_aios_spec_013/` (example) | medium | **Composite** — must not collapse to single ID; **defer** until convention locked | **Defer** | yes |
| `demo_exec_*` (5 folders) | demo_sample | `reviews/demos/<same_slug>/` | **high** | Non-authoritative samples | **First slice** | migration doc only |
| `executionscopeandcontextbounding` | legacy_unclear | `archive/legacy_flat_reviews/…` or re-map to spec | **low** | No ID in folder name | **Defer** | — |
| `googleworkspaceintegrationgovernance` | legacy_unclear | same | **low** | — | **Defer** | — |
| `governance_constitution` | specification | `reviews/specifications/…` or map to `core/` doc ID | medium | Topic slug | **Defer** | — |
| `intent_primitive_execution_model` | legacy_unclear | archive or spec | **low** | — | **Defer** | — |
| `kernel_shadow` | reference_or_process_doc | `reviews/reference_docs/kernel_shadow/` | medium | Pilot coordination | **Defer** | — |
| `local_tts_runtime_standard` | specification | `reviews/specifications/…` | medium | Verify `document_id` | **Defer** | — |
| `master_platform_operating_agreement` | specification | `reviews/specifications/…` | medium | — | **Defer** | — |
| `ollama_runtime_standard` | specification | `reviews/specifications/…` | medium | — | **Defer** | — |
| `technical_manifesto` | specification | `reviews/specifications/technical_manifesto/` | high | Common doc | **Defer** (many links) | — |
| `whisper_runtime_standard` | specification | `reviews/specifications/…` | medium | — | **Defer** | — |

**Traceability:** Git history preserves old paths; this table is the human-readable mapping; **CHANGELOG** records the first slice.

---

## D. Operational policy (summary)

1. **`reviews/` is a classified workspace tree**, not a general scratch area.
2. **No new unclassified root-level folders** — pick a class (or use `demos/` for samples).
3. **Every review workspace** must map to a **known class** (amendment, specification, package, reference, demo, or archived legacy).
4. **Demo/sample execution packets** live under **`reviews/demos/<slug>/`** only.
5. **Ambiguous legacy** topic folders are **reclassified or archived** only after explicit review (not bulk-renamed).
6. **New work** should use the classified layout **even before** legacy migration completes (e.g. new demos under `reviews/demos/`).

Full policy: [`README.md` § Reviews tree — operational policy](README.md#reviews-tree--operational-policy) (this file is the canonical detail).

---

## E. First slice (implemented)

1. Add **`reviews/CLASSIFICATION_AND_MIGRATION.md`** (this document) and **`reviews/demos/README.md`**.
2. **Move only** `demo_exec_*` folders into **`reviews/demos/`** (same leaf names).
3. Update **READMEs**, **CHANGELOG**, **runner** (`--review-slug demos/...`), and **pipeline** cross-links.
4. **Do not** move amendment, specification, composite, or legacy folders in this slice.

### Runner usage after first slice

- Use **`--review-slug demos/<demo_slug>`** (e.g. `demos/demo_exec_ui_review`).

---

## F. Self-check (before edits)

| Question | Answer |
|----------|--------|
| Ambiguous moves in first slice? | **No** — only `demo_exec_*` samples. |
| Break active paths? | **Mitigated** — update in-repo links; external bookmarks may need this doc. |
| More than minimum slice? | **No** — amendments/specs left untouched. |

---

*End of classification and migration note.*
