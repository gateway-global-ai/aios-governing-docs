---
document_id: AIOS-COMMITTEE-BRIEF-AMD-2026-013
version: 1.0.1
status: draft
category: reference
title: Committee review brief — intent-bearing repository taxonomy (AMD-2026-013)
author: Gateway Global AIOS
created: 2026-04-08
last_updated: 2026-04-08
cross_references:
  - doc_id: AMD-2026-013
  - doc_id: AIOS-REPO-TAXONOMY-001
  - doc_id: AMD-2026-005
  - doc_id: AMD-2026-007
  - doc_id: AMD-2026-012
  - doc_id: AIOS-AMD-PLAN-001
amendment_history:
  - version: 1.0.1
    date: 2026-04-08
    summary: Reviewer lead frame — bounded control-plane lens; no substantive change to AMD-2026-013 / AIOS-REPO-TAXONOMY-001.
  - version: 1.0.0
    date: 2026-04-08
    summary: Initial committee packet — fit assessment, scoring risks, v0.2.0 delta, questions, readiness.
---

# Committee review brief — intent-bearing repository taxonomy (AMD-2026-013)

**Reviewer’s lens (read the packet through this frame):**

- this is a bounded control-plane proposal
- it does not mandate universal path encoding
- it does not alter ratification mechanics
- it allocates taxonomy authority to architecture/builder and preserves downstream separation of duties
- it proposes staged adoption, not immediate mass migration

---

**Purpose:** Single packet for **committee** (or designated reviewers) to **discipline** the **draft** amendment **AMD-2026-013** and its implementation memo **AIOS-REPO-TAXONOMY-001** before **binding** triangulated peer review under **[AMD-2026-005](../amendments/AMD-2026-005.md)**. This is **control-plane** governance (who may define repository semantics), **not** a folder-cleanup campaign.

**Governing draft (normative law, when ratified):**  
[`amendments/AMD-2026-013.md`](../amendments/AMD-2026-013.md) — **v0.2.1** (committee packet pointer)

**Operational memo (non-normative detail):**  
[`AIOS-REPO-TAXONOMY-001.md`](AIOS-REPO-TAXONOMY-001.md) — **v0.2.1**

**Operational migration map (non-normative):**  
[`reviews/CLASSIFICATION_AND_MIGRATION.md`](../reviews/CLASSIFICATION_AND_MIGRATION.md)

**Ratification law unchanged:** **[AMD-2026-005](../amendments/AMD-2026-005.md)** triangulation and Council paths are **not** modified by this package.

---

## 1. What changed in v0.2.0 (delta from v0.1.0)

| Area | v0.1.0 | v0.2.0 |
|------|--------|--------|
| Thesis | Broad principles | **Bounded:** taxonomy applies **where declared**; not all intent in paths |
| Applicability | Implicit | **Explicit:** binding only on **declared** taxonomies; legacy valid until staged migration |
| Planning / execution | Strong “SHALL” risk | **Qualified** **should** / **where specified**; metadata and transactions preserved |
| Non-goals | Short list | **Expanded:** no blanket path mandate, no mass reorg, no ratification shortcut, no cleanup-as-law |
| Operability | Partial | **Migration map**, **ambiguous paths**, **dual-read**, builder-maintained audit doc |
| Committee | Short note | **Routing** expanded; safe vs draft-until-approval |

**v0.2.1 (this packet):** Adds this committee brief and cross-references only; **no** change to normative substance of §2–4.

---

## 2. Committee-fit assessment (review dimensions)

### 2.1 Completeness

| Strengths | Likely objections | Substantive? |
|-----------|-------------------|--------------|
| Scope, non-goals, rollout, separation of duties, relationship table | “Who is builder?” (role vs person) | **Cosmetic** — clarify as **maintainer/builder role** |
| Applicability gate (declared taxonomy) | Product repo **should** feels soft | **Substantive (bounded)** — intentional; ratified product process may tighten later |
| Migration deferred phases | None material | — |

### 2.2 Conflict freedom

| Strengths | Likely objections | Substantive? |
|-----------|-------------------|--------------|
| AMD-2026-007 / metadata row; planning vs ratification §1.3 | Dual taxonomy if product ignores memo | **Plausible** — **not** a doc conflict; **mitigation:** product **should** align; no **must** until policy adopts |
| AIOS-AMD-PLAN-001 remains non-normative; AMD-2026-013 adds **should** for paths | Slight tension with “any planning path” | **Cosmetic** — **should** + **where declared** resolves |
| Shell (AMD-2026-012) unchanged | None | — |

### 2.3 Practical operability

| Strengths | Likely objections | Substantive? |
|-----------|-------------------|--------------|
| `reviews/demos/` first slice done; phases 2–5 deferred | Phase 2 link audit is heavy | **Operational cost**, not a drafting defect |
| `CLASSIFICATION_AND_MIGRATION.md` as live map | Maintenance burden | Acknowledged; **builder** owns map |

---

## 3. Cross-document conflict check (summary)

| Topic | Finding |
|-------|---------|
| Authority | **Architecture role** defines; **builder** maintains; **implementation / execution** consume — consistent across AMD-2026-013 §6 and AIOS-REPO-TAXONOMY-001 §A/C. |
| Path vs metadata / runtime | **Explicit** non-exclusivity in amendment §1.2, §2.2.3, table row “Metadata, schemas, transactions” — **no** claim that paths replace intent primitives or evidence records. |
| Builder vs downstream | **Clear** prohibition on silent new roots; **no** conflict with peer review **content** judgment. |
| Governing repo vs product | **Primary** binding narrative is **`aios-governing-docs`**; product **should** — **no** false universal mandate. |
| Migration | **Staged**; **no** blind bulk rename; **ambiguous** paths documented — aligns with `CLASSIFICATION_AND_MIGRATION.md`. |
| Ratification | **Explicit** AMD-2026-005 unchanged; taxonomy is **not** a gate substitute — **no** ratification-law conflict. |

**Invented conflicts:** none identified.

---

## 4. Scoring risk summary (delta-oriented)

| Risk | Severity | Notes |
|------|------------|--------|
| Misread as “mandatory path encoding of all intent” | Medium | **Mitigated** in v0.2.0; brief repeats bounded thesis |
| Product **should** seen as unenforceable | Low–medium | **Intentional** narrowness; committee may **accept** or **request** future product instrument |
| Operational load on builder for migration map | Low | **Process** cost; not a **completeness** gap in law |
| Terminology “architecture role” vs “architecture agent” in KB | Low | **Cosmetic** unless committee standardizes titles |

---

## 5. Questions for committee

1. Is the **authority allocation** (architecture defines declared taxonomy; builder maintains; downstream consumes) **acceptable** as control-plane law for this repository?
2. Is **product** alignment remaining **should** until separate product policy **deliberately** the right **boundary**?
3. Should **Phase 2** (`amd_*` → `reviews/amendments/`) require a **separate** migration decision **after** amendment ratification, or **only** after committee **principles** approval?
4. Are **non-goals** (§4) sufficient to **foreclose** “cleanup elevated to architecture” critiques?
5. Is the **recommended order** acceptable: **committee principles review** → **author stabilization** → **AMD-2026-005 peer review** → **ratification path** (no change to ratification mechanics)?

---

## 6. Preparatory work vs remains draft

| Safe before committee approval | Remains draft until ratification path completes |
|---------------------------------|-----------------------------------------------|
| This brief; memo; migration map; `reviews/demos/` pattern | Claims that AMD-2026-013 is **ratified** |
| Registry entries **draft** | Mandatory org-wide migration **deadlines** |
| Non-destructive cross-links | **Must**-level product tree law **without** product instrument |

---

## 7. Recommended next step

After committee feedback: **freeze** normative wording for a **peer review round** under **AMD-2026-005**, with **AIOS-REPO-TAXONOMY-001** as the **non-normative** companion (revisable for clarity post-committee).

---

*End of AIOS-COMMITTEE-BRIEF-AMD-2026-013 v1.0.1 draft.*
