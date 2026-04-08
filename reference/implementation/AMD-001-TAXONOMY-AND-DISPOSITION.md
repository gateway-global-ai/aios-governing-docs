---
document_id: AIOS-AMD-001-DISPOSITION-001
version: 1.0.0
status: ratified
category: reference
title: AMD-001 — taxonomy, classification, and disposition
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
cross_references:
  - doc_id: AMD-001
  - doc_id: AMD-2026-013
  - doc_id: AIOS-SPEC-003
  - doc_id: AIOS-SPEC-004
  - doc_id: AIOS-SPEC-005
---

# AMD-001 — taxonomy, classification, and disposition

**Purpose:** Resolve **[AMD-001](../../amendments/ammendment_google.md)** as a **classification and integration** problem (not an unfinished-law problem). **[AMD-2026-013](../../amendments/AMD-2026-013.md)** ratifies that **declared taxonomy and accountability** matter; this document places **AMD-001** explicitly in the amendment **universe** so it is neither ignored nor confused with the **`AMD-2026-*`** program.

---

## 1. What class of instrument is AMD-001?

| Question | Answer |
|----------|--------|
| **Legacy ratified amendment?** | **Yes.** It predates the **`AMD-2026-*`** series and uses **`AMD-001`** numbering. |
| **Source-analysis-derived?** | **Yes.** Substantive content derives from **`sources/google_cli_article/impact_report.md`** (same lineage as the body text). |
| **Pre-2026 series?** | **Yes** in the sense of **numbering era**; calendar dates in front matter are still 2026. Treat **`AMD-001`** as a **separate series** from **`AMD-2026-*`**. |
| **Amendment vs spec-only?** | It **is** a **ratified amendment** (`type: amendment_to_existing`). It **directs** changes to **AIOS-SPEC-003, 004, 005**; it does **not** replace those specs. **Normative developer CLI law** remains in the **specs** once updated; AMD-001 remains the **ratified bridge** and **gap matrix** until a future instrument **supersedes** or **folds** it. |

---

## 2. How it lives in the repo taxonomy

| Rule | Record |
|------|--------|
| **Canonical file** | **`amendments/ammendment_google.md`** — path and filename **retained** for stability (including legacy spelling **ammendment**). |
| **Document ID** | **`AMD-001`** (`amendment_id` / `document_id` in front matter). **Do not** renumber into **`AMD-2026-*`** without a council-level decision and migration plan. |
| **Classification (YAML)** | **`legacy_ratified_bridge`** — see **[AMD-001](../../amendments/ammendment_google.md)** front matter. |
| **Linked specs** | **[AIOS-SPEC-003](../../specifications/AgentIntegrationProtocol.md)** (AIP), **[AIOS-SPEC-004](../../specifications/CLIDeveloperGuide.md)** (CLI Dev Guide), **[AIOS-SPEC-005](../../specifications/agents.md)** (Agent Integration Guide) — as listed in AMD-001 **`affected_documents`**. |

---

## 3. Current operational effect

| Layer | Effect |
|-------|--------|
| **Authority** | **Ratified** — council process completed; **`ratification_date: 2026-04-01`**. |
| **Standalone law?** | **Partially.** It is **not** a full substitute for the CLI specs; it is a **ratified directive + comparison matrix + recommended edits** toward **agent-native CLI** behavior. |
| **Specs embodiment** | **Incremental.** The **[AMD-001](../../amendments/ammendment_google.md)** matrix and “Recommended Edits” remain the **audit list** until **AIOS-SPEC-003/004/005** explicitly absorb each requirement (or consciously defer). **Absence** of a row in the specs does **not** silently repeal AMD-001; **tracking** is a **spec maintenance** obligation. |
| **Relationship to `AMD-2026-*`** | **Orthogonal series.** Closure of **006 / 009 / 008** does **not** depend on AMD-001 **substance**; **taxonomy clarity** (this document) should precede **heavy** 2026 closure work so the **constitution of amendments** stays legible. |

---

## 4. Ordering relative to cohesion-critical AMDs

1. **AMD-001 — taxonomy resolution** (this document + YAML on **[AMD-001](../../amendments/ammendment_google.md)**) — **classification fixed in-repo**.  
2. **AMD-2026-006 → AMD-2026-009 → AMD-2026-008** — **[cohesion closure order](AMD-AMENDMENT-REVIEW-TRACKER-001.md#foundation-cohesion--remaining-amd-closure-order)** unchanged.

---

## 5. Optional: Cursor prompt (spec embodiment / disposition pass)

Use when you want tooling to **diff** AMD-001 against current specs and propose **SPEC** edits or a **supersession note** (not to re-ratify AMD-001):

```text
You are working in aios-governing-docs. Read amendments/ammendment_google.md (AMD-001, legacy_ratified_bridge),
reference/implementation/AMD-001-TAXONOMY-AND-DISPOSITION.md, and the current text of specifications/AgentIntegrationProtocol.md,
specifications/CLIDeveloperGuide.md, and specifications/agents.md. For each row in AMD-001’s comparison matrix and “Recommended Edits” sections,
state: (a) already embodied in spec text, (b) partial, (c) missing. Propose minimal spec edits or explicit NON-GOALS with citations.
Do not change AMD-001 numbering or file path unless user requests a migration plan. Output a short table and optional PR-style edit list.
```

---

*End of AMD-001 taxonomy and disposition — v1.0.0.*
