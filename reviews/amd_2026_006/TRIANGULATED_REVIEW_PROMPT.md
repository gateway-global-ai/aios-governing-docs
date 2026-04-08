# Triangulated peer review prompt — AMD-2026-006 + AIOS-SPEC-007

**Review type:** Round 1 — **coordinated package**: amendment **[AMD-2026-006](../../amendments/AMD-2026-006.md)** (**v0.1.0**) + **[AIOS-SPEC-007](../../specifications/GoogleWorkspaceIntegrationGovernance.md)** (**v0.1.1**).  
**Rubric:** [`templates/grading_rubric.md`](../../templates/grading_rubric.md) — 11 dimensions, scores **1–5** per dimension.  
**Thresholds ([AMD-2026-005](../../amendments/AMD-2026-005.md)):** Composite **≥ 3.5** and **no dimension below 3**.

**Purpose:** Validate **integration governance** — intent-only entry, control plane, MCP adapter boundary, retrieval policy, and cross-spec consistency — not general editing.

---

## Documents under review

| Doc | Path |
|-----|------|
| **AMD-2026-006** | [`amendments/AMD-2026-006.md`](../../amendments/AMD-2026-006.md) |
| **AIOS-SPEC-007** | [`specifications/GoogleWorkspaceIntegrationGovernance.md`](../../specifications/GoogleWorkspaceIntegrationGovernance.md) |

**Informative context (not separately scored unless contradiction):**  
[`amendments/AMD-2026-005.md`](../../amendments/AMD-2026-005.md); [`specifications/IntentPrimitiveAndExecutionModel.md`](../../specifications/IntentPrimitiveAndExecutionModel.md) (**AIOS-SPEC-009**); [`amendments/AMD-2026-009.md`](../../amendments/AMD-2026-009.md); [`specifications/ExecutionScopeAndContextBounding.md`](../../specifications/ExecutionScopeAndContextBounding.md) (**AIOS-SPEC-010**).

---

## A. Amendment shell (AMD-2026-006)

1. **Rationale (§1)**  
   Does the **risk framing** (unbounded MCP surface) **justify** the **three** proposed changes? **Missing** hazards?

2. **Proposed changes (§2)**  
   - **Change 1:** Is “**ratify AIOS-SPEC-007**” **clear** as the operative effect?  
   - **Change 2 / 3:** References to **SPEC-003** and **SPEC-006** — are they **specific enough** for implementers and **policy index** traceability, or do you **require** explicit section IDs in the amendment text?

3. **Cross-document impact (§3)**  
   Is the **table** **complete**? Are **Runtime** / **Deployment** rows **actionable**?

4. **Ratification requirements (§4)**  
   Consistent with **[AMD-2026-005](../../amendments/AMD-2026-005.md)** process?

---

## B. Normative spec (AIOS-SPEC-007)

5. **§2 Routing model**  
   - **SHALL** / **MUST NOT** rules: **sufficient** to **block** direct MCP tool calls from bypassing **intent** resolution?  
   - **One intent → one scope class** (where domain pack defines mapping): **clear** and **consistent** with **AIOS-SPEC-009**?

6. **§3 Web search and external retrieval**  
   - Alignment with **AMD-2026-009** and **policy-registered** backends: **gaps** or **loopholes**?  
   - **PSE credentials** on MCP server only — **enforceable** against **client-bundle** leaks?

7. **§4 Relationship to other documents**  
   Is the **roles** table **accurate**? **Missing** dependencies (e.g. **POL-WORKSPACE-*** from longer SPEC drafts elsewhere)?

---

## C. Cross-document integrity

8. Does **AMD-2026-006** **contradict** **AIOS-SPEC-007** anywhere?  
9. Does **AIOS-SPEC-007** **§2–3** **conflict** with **AIOS-SPEC-010** or **AMD-2026-009** on **bounding** or **search scope**?

---

## D. Required output per reviewer

1. **Executive summary** (≤ 250 words).  
2. **Scorecard:** all **11** rubric dimensions with **1–5** scores and **one sentence** rationale each — applied to the **combined** **AMD-2026-006** + **AIOS-SPEC-007** package.  
3. **Composite score** (mean of 11 dimensions, one decimal).  
4. **Disposition:** one of `approved` | `approved_with_changes` | `major_revision_required` (per [`templates/grading_rubric.md`](../../templates/grading_rubric.md)).  
5. **Blocking issues** (if any): **normative** gaps, **unenforceable** clauses, or **cross-spec contradictions** — cite **section** IDs.

---

## Filing

Save as **`round_1/review_<NNN>_<provider>.md`** per [`reviews/README.md`](../README.md) naming conventions.
