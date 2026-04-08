---
artifact: kernel_shadow_findings
status: pilot_run_amd_2026_012
binding: false
advisory: true
normative_basis: AMD-2026-010 §4.4
---

# Kernel shadow findings — AMD-2026-012 @ v0.1.2

**⚠ Advisory / non-binding (pilot)** — Per **[AMD-2026-010 §4.4](../../../amendments/AMD-2026-010.md)**, these findings **do not** gate ratification or merge. **[AMD-2026-005](../../../amendments/AMD-2026-005.md)** triangulated peer review remains the **sole binding** review path unless a future amendment authorizes a blocking kernel gate.

| Field | Value |
|-------|--------|
| **Target** | [`amendments/AMD-2026-012.md`](../../../amendments/AMD-2026-012.md) **v0.1.2** |
| **Reviewer(s)** | AIOS Kernel Shadow Pilot (Coordinator) |
| **Date** | 2026-04-09 |
| **Parallel triangulation** | Round 1 Pass B — [`../round_1/REVIEW_SYNTHESIS.md`](../round_1/REVIEW_SYNTHESIS.md) (`review_003_openai`, `review_004_gemini`); prior Pass A (`review_001`/`review_002`, v0.1.1) historical. |

## Executive summary

**AMD-2026-012** is **core kernel doctrine**: it **centers** Shell authority, **§7** as the **auditable** primary-outcome family, **§4.4** fallback **solely** through §7, and **§14** control-plane/UI alignment. From a **shell / state / routing** lens the amendment **strengthens** invariants that **AMD-2026-007** and **AIOS-SPEC-009** depend on. Residual **kernel** attention points: **(1)** **explicit** cross-link to **intent routing** taxonomy (`app.*` / `workspace.*`) in **AIOS-SPEC-009** so runtime teams do not invent shell outcomes **off** §7; **(2)** **§5.2** “governed session state” — **product** must bind **recent/pinned** intent to **actual** control-plane fields; **(3)** **§9.4** progressive Kit exposure — **watch** for **catalog** UX that **looks** like entry authority **without** a §7 **discovery_mode** outcome. None of these **invalidates** the triangulated **PASS**; they are **implementation and conformance** hooks.

---

## Findings by category

Severity is **informative** only (pilot).

### 1. Shell / routing invariants

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-001 | Low | §4, §7 | Single entry + **finite** §7 family gives a **clear** audit surface for “what primary state is the user in?” **Kernel-positive.** Ensure **runtime** routing tables **never** emit a **primary** UX state **label** outside §7 mapping (already stated in §7 informative boundary + normative paragraph). | AMD-2026-007 §11; AIOS-SPEC-009 §12 |
| K-002 | Medium | §4.4, §14 | Fallback **solely** via §7 + control-plane **fallback outcome selection** (**§14**) is **coherent**. **Risk:** an adapter or skill **returns** a **non-§7** “status” to **chrome** that **reads** as primary — **mitigate** by **mapping layer** at Shell boundary (product conformance). | §4.4, §14 |

### 2. State vs skill boundary

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-010 | Low | §9, §9.4 | Subordination **and** **§9.4** Kit/discovery language **reinforce** shell vs domain **without** making this a marketplace spec. **Kernel:** Kits **must not** register **shell** identity or **fallback** — aligns with **§9.1**. | §9.1, AMD-2026-007 |

### 3. Authority / disclosure (primary vs operator)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-020 | Low | §10, §13 | **Contradictory readiness** and **admin separation** match **kernel** session-truth expectations. **Triangulation** already stressed **§8.4** thresholds — **orthogonal** to **primary vs operator** but **feeds** disclosure consistency. | §10.2–10.3, AMD-2026-007 §4 |

### 4. Routing ambiguity (`app.*` / `governance.*` / `workspace.*`)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-030 | Low | §2, §17 | Amendment **does not** enumerate **intent prefixes** — **by design**. **Kernel** readers should treat **routing** detail as **owned** by **AIOS-SPEC-009** / **AMD-2026-007**; **AMD-2026-012** sets **Shell** authority **over** outcomes, **not** string-level routing. **Optional editorial:** one **informative** sentence in §17 pointing to **SPEC-009** §2.1 shell vs domain. | AIOS-SPEC-009 §2.1 |

### 5. Voice / UI parity (shell affordances)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-040 | Observation | §8, §8.4 | Voice-first **norms** + **§8.4** measurable thresholds **defer** to subordinate policy — **correct** split. **Kernel** does not require numeric limits **in** the amendment. | §8.4, AMD-2026-007 §4.1 |

### 6. Session truth / composed disclosure

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-050 | Medium | §5.2, §7 | **Returning user** restoration from **governed** state + **PolicyRecord** is **kernel-appropriate**. **Conformance risk:** if **control-plane** does not yet expose **pinned/recent** intent **deterministically**, implementations **must not** fake **continuity** from **local** UI-only memory — **aligns** with **§4.3** identity authority. | §5.2, §4.3, AIOS-SPEC-009 |

---

## Overlap with triangulated committee

| Kernel finding ID | Addressed in Round 1 Pass B? (Y/N/partial) | Committee review ref |
|-------------------|------------------------------------------|------------------------|
| K-001 | **Partial** | §7 finiteness / enforceability (Gemini/OpenAI) |
| K-002 | **Partial** | **§14** concreteness (Gemini); **control-plane** mapping |
| K-010 | **Partial** | **§9.4** economics / Kit (Gemini) |
| K-020 | **Y** | **§10** contradictory readiness (review packet) |
| K-030 | **N** | Committee did not stress **SPEC-009 §2.1** cross-pointer **as kernel** |
| K-040 | **Y** | **§8.4** subordinate thresholds (Gemini) |
| K-050 | **Partial** | **§5.2** governed state (Gemini); **kernel** stresses **control-plane** truth vs UI |

**Unique kernel yield:** **K-030** (explicit **routing** doc ownership vs amendment scope); **K-002** (adapter/chrome **mapping** to §7 at boundary); **K-050** (control-plane **field** readiness for **§5.2**).

---

## Sign-off

| Role | Name | Date |
|------|------|------|
| Kernel reviewer (pilot) | Coordinator — kernel shadow | 2026-04-09 |

---

*Advisory only — AMD-2026-010 §4.4.*
