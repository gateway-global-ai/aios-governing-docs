# Triangulated peer review prompt — AMD-2026-011 + AIOS-SPEC-013

**Review type:** Round 1 — coordinated package (amendment + specification).  
**Rubric:** [`templates/grading_rubric.md`](../../../templates/grading_rubric.md) — 11 dimensions, scores **1–5** per dimension.  
**Thresholds (amendment ratification alignment):** Composite **≥ 3.5** and **no dimension below 3** (see **AMD-2026-011** §5 and `templates/grading_rubric.md` disposition rules).

---

## Documents under review

| Doc | Path |
|-----|------|
| **AMD-2026-011** (v0.1.2) | [`amendments/AMD-2026-011.md`](../../../amendments/AMD-2026-011.md) |
| **AIOS-SPEC-013** (v0.1.1) | [`specifications/ExternalRepositoryAcquisitionAnalysisAndPromotion.md`](../../../specifications/ExternalRepositoryAcquisitionAnalysisAndPromotion.md) |

---

## A. AMD-2026-011 — focus questions

Answer with concrete references (section numbers / table rows).

1. **Governed acquisition vs exploratory local clone**  
   Is the boundary between **governed channels** / **acquisition intent** and **exploratory** work clear? Does the **copy/import** sentence close the “side door” without contradicting local exploratory policy?

2. **Quarantine / analysis / promotion**  
   Are **quarantine-by-default**, **analysis** before reuse, and **promotion** principles stated clearly at amendment depth (not over-specified)?

3. **Minimal execution dependency**  
   Is this framed as a **governance principle** (trust surface of CI/automation), not only as a pip optimization? Is the link to **`scripts/requirements.governance-integrity.txt`** proportionate?

4. **Amendment vs specification**  
   Is the split from **AIOS-SPEC-013** clean (principles + repo CI exemplar in the amendment; SHALL contracts and classes in the spec)? Flag any **duplication** that could drift.

---

## B. AIOS-SPEC-013 — focus questions

1. **Acquisition intent contract** — Are required elements (subject, actor/tenant, purpose class, timestamp) sufficient and aligned with **AIOS-SPEC-003**?

2. **Quarantine-by-default** — Is the rule enforceable as a **promotion class** (§8)?

3. **Machine-readable repository record** — Are §§4–7 (bundle, versioning, doc URLs, deps/env/API, execution/risk class) complete enough for conformance without mandating storage?

4. **Authoritative documentation URLs** — Separate from source URL; stale URL handling in analysis — adequate?

5. **Dependency / environment / API extraction** — Names without secret values — sufficient?

6. **Promotion classes** — **quarantine**, **evaluation**, **sandbox**, **approved**, **vendored / reusable**: coherent? Any conflict with **AMD-2026-011** §2.4 item 5?

7. **No direct operational use before promotion** — Does §9 align with §8 (including sandbox exception via policy)?

8. **Audit / evidence** — Auditable events and **AIOS-SPEC-003** alignment — gaps?

9. **Narrowness** — Avoids vendor lock-in, blob-store design, and **MCP**/governance-doc conflation per §11?

---

## C. Package-level (both documents)

Assess **together**:

| Topic | What to judge |
|-------|----------------|
| **Cross-document consistency** | Terminology, cross-references (**§2.2**, **§2.5** in AMD vs SPEC pointers), promotion intermediate states (**AIOS-SPEC-013** §8). |
| **Architectural fidelity** | Planes: governance markdown vs runtime MCP vs design-time acquisition — consistent with **AMD-2026-011** §1.1 and **AIOS-SPEC-013** §11. |
| **Governance enforceability** | MUST/SHALL language, auditability, loopholes. |
| **Practical operability** | Can operators and implementers comply without an ops runbook (not required at this tier)? |
| **Conflict freedom** | vs **AIOS-CORE-002**, **AMD-2026-005**, **AIOS-SPEC-003**, **AMD-2026-009** (web retrieval — different acquisition plane). |
| **Scope discipline** | No creep into long-term ingestion storage design. |
| **Friction factor** | Gates proportional to risk. |

---

## D. Required output per reviewer

1. **Executive summary** (≤ 250 words).  
2. **Scorecard:** all **11** rubric dimensions with **1–5** scores and **one sentence** rationale each.  
3. **Composite score** (mean of 11 dimensions, one decimal).  
4. **Disposition:** one of `approved` | `approved_with_changes` | `major_revision_required` (per `templates/grading_rubric.md`).  
5. **Blocking issues** (if any) and **non-blocking** recommendations.  
6. **YAML front matter** (recommended):

```yaml
---
reviewer: "<id>"
review_date: "YYYY-MM-DD"
documents: ["AMD-2026-011", "AIOS-SPEC-013"]
package: "AMD-2026-011-AIOS-SPEC-013"
round: 1
disposition: approved | approved_with_changes | major_revision_required
composite_score: 0.0
---
```

---

## E. Integrity and registry (for coordinators)

- **`py -3 scripts/governance_integrity_check.py`** should pass on the branch under review.  
- **`DOCUMENT_REGISTRY.*`** generated from **`scripts/registry_generator.py`** after any governed front-matter edits.

---

*This file is a review instruction artifact, not governed law.*
