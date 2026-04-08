# Triangulated peer review prompt — AMD-2026-012

**Review type:** Round 1 — amendment only (**Shell Authority and Voice-First Entry**).  
**Rubric:** [`templates/grading_rubric.md`](../../templates/grading_rubric.md) — 11 dimensions, scores **1–5** per dimension.  
**Thresholds (AMD-2026-005 alignment):** Composite **≥ 3.5** and **no dimension below 3** (see `templates/grading_rubric.md` disposition rules).

**Purpose:** Apply **pressure on enforceability and product feel**, not general prose polish. The draft is **coherent**; reviewers should probe **loopholes**, **testability**, and **abuse cases**.

---

## Document under review

| Doc | Path |
|-----|------|
| **AMD-2026-012** (v0.1.1) | [`amendments/AMD-2026-012.md`](../../amendments/AMD-2026-012.md) |

**Companion context (informative, not co-reviewed unless coordinator expands scope):**  
- [`amendments/AMD-2026-007.md`](../../amendments/AMD-2026-007.md) — shell affordances, primary vs operator.  
- [`specifications/IntentPrimitiveAndExecutionModel.md`](../../specifications/IntentPrimitiveAndExecutionModel.md) (**AIOS-SPEC-009**) — shell vs domain, disclosure (**§12**).

---

## A. Core law (§§4–7)

Answer with concrete **section / table references**.

1. **Single entry and session authority (§§4.1–4.2)**  
   Is the Shell clearly **authority**, not **chrome**? Any ambiguity that would let a skill, tool, or launcher **replace** the default entry path?

2. **Identity and fallback (§§4.3–4.4)**  
   Is **fallback law** tight enough to **prevent persona drift** and **dashboard drift**?  
   Flag **any** path where a **subordinate** lane could **own** fallback without Shell decision.

3. **Finite outcome family (§7)**  
   - Is the family **enforceable** and **testable** for **Shell-exposed** primary outcomes?  
   - Does the **informative boundary** (Shell-exposed primary outcomes **vs** internal subcodes/diagnostics) **resolve** the “too small for real implementations” objection?  
   - **If not**, what **one** normative or informative addition would fix it?

---

## B. Journey and user state (§§5–6)

4. **New vs returning**  
   Is placement **before** tool posture (§5.3, §6) **correct** and **sufficient** for “journey first” framing?

---

## C. Voice-first, tools, discovery, prohibitions (§§8–12)

5. **Voice-first (§8)**  
   Are **SHALL** / **SHOULD** rules **auditable** without prescribing pixel-level UI?

6. **Subordinate skills/tools (§9)**  
   Is **subordination** crisp enough to **block** integration-first or tool-catalog-first **home** states?

7. **Transparency (§10)**  
   Are **readiness** and **disclosure** obligations **concrete** enough for **QA** (same user-visible truth across surfaces)?

8. **Discovery-first (§11)** — **abuse case**  
   Could a team use **discovery-first** to **reintroduce** launcher grids, dashboard-first onboarding, or verbose instructional UI?  
   What **additional clause** (if any) would **close** that loophole?

9. **Prohibited patterns (§12)**  
   Is the **P1–P9** table **complete** for the regressions you care about? **Missing** rows?

---

## D. Governance separation and control plane (§§13–16)

10. **§13 separation**  
    Is the bar **high enough** to stop **governance/admin** from **contaminating** end-user runtime via **defaults**, **fallback**, or **bootstrap**?  
    Name **one** residual risk.

11. **§14 control-plane implications**  
    Concrete enough to **drive** behavior?  
    **Stress-test** with these **non-conformant examples** (illustrative):

    - Shell says **connected**; panel says **sign-in required** for the **same** path.  
    - **Edited** UI identity **differs** from **runtime** identity **without** governed apply.  
    - **Tool lane** picks **fallback** or **next surface** **without** Shell decision.

    Should **any** of these be **elevated** to a **normative example** in the amendment, or stay **review-only**?

12. **Conformance (§15) and migration (§16)**  
    Are **non-conformance** clauses **actionable**? Is **archive/separation** **credible** as a conformance move?

---

## E. Cross-document alignment (informative)

13. Does **AMD-2026-012** **align** with **AMD-2026-007** and **AIOS-SPEC-009** **without** **contradiction**? **Any** duplicate definitions that could **drift**?

---

## F. Required output per reviewer

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
documents: ["AMD-2026-012"]
package: "amd_2026_012"
round: 1
disposition: approved | approved_with_changes | major_revision_required
composite_score: 0.0
---
```

---

## G. Integrity and registry (for coordinators)

- **`py -3 scripts/governance_integrity_check.py`** should pass on the branch under review.  
- **`DOCUMENT_REGISTRY.*`** generated from **`scripts/registry_generator.py`** after any governed front-matter edits.

---

## H. Alignment path (informative)

1. Freeze **AMD-2026-012** text except **targeted** revisions from review.  
2. **Round 1** triangulation → **revision** for **enforceability**.  
3. **Ratification** when ready.  
4. Use **ratified** shell law to drive **control-plane** and **UI** cleanup in product repos.
