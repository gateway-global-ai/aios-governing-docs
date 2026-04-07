---
artifact: kernel_shadow_findings
status: pilot_run_1
binding: false
advisory: true
normative_basis: AMD-2026-010 §4.4
---

# Kernel shadow findings — AIOS-SPEC-009 @ 0.5.4

**⚠ Advisory / non-binding (pilot)** — Per **[AMD-2026-010 §4.4](../../../amendments/AMD-2026-010.md)**, these findings **do not** gate ratification or merge. **[AMD-2026-005](../../../amendments/AMD-2026-005.md)** triangulated peer review remains the **sole binding** review path for documents that have a committee package unless a future amendment authorizes a blocking kernel gate.

| Field | Value |
|-------|--------|
| **Target** | [`specifications/IntentPrimitiveAndExecutionModel.md`](../../../specifications/IntentPrimitiveAndExecutionModel.md) (**v0.5.3**) |
| **Reviewer(s)** | AIOS Kernel Shadow Pilot (Coordinator) |
| **Date** | 2026-04-06 (findings); overlap **2026-04-10** / **2026-04-15** |
| **Parallel triangulation** | **Round 2** — [`../round_2/REVIEW_SYNTHESIS.md`](../round_2/REVIEW_SYNTHESIS.md); **AMD-2026-005** **PASS** (`review_001`–`review_003` DeepSeek/OpenAI/Gemini); [`../round_2/RATIFICATION_GATE_REPORT.md`](../round_2/RATIFICATION_GATE_REPORT.md) — **READY_FOR_RATIFICATION** (peer-review stage). |

## Executive summary

The specification **§2.1** boundary (domain intent vs shell routing plane, **POL-SHELL-004**) is **clear and internally consistent** with **AMD-2026-007** intent. **Temporal grounding** (**§6.3.1–6.3.2**, **§15.1**) and **primary vs operator** (**§12**) are strong for kernel-relevant disclosure. Residual risk clusters in **(a)** schema shape (**`ExecutionPlan.temporalScope`** required globally vs optional **`Intent.temporalScope`**), **(b)** **§16.4** interaction between “voice / live” layers and **§17** sovereign lanes, and **(c)** **§19** implementation pointers that assume a **voice-repo** layout not present in **aios-governing-docs**. **Triangulated Round 1** (**2026-04-10**) nonetheless issued **`major_revision_required`** (economics/§15.4, **§6.3** definitional precision, **§8**/**§12** clarity, Style Guide front matter) — **kernel** findings are **orthogonal** on several items (**see overlap** below). Kernel notes remain **advisory** and **non-blocking**.

---

## Findings by category

Severity is **informative** only (pilot).

### 1. Shell / routing invariants

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-001 | Low | §2.1, §6.1 | **Menu** is listed as an intent source alongside voice/chat; implementers must still classify **shell chrome** commands per **AMD-2026-007 §11.9** vs **domain** intent. The spec defers shell semantics correctly; **product QA** should verify menu handlers do not register domain “fulfillment” for shell-only paths. | AMD-2026-007 §11.9; §2.1 |
| K-002 | Observation | §19 | Implementation bullets list **UI rendering, proposal flows, and shell chrome** — consistent with deferral to **SPEC-006**; **cross-repo** readers may need an explicit “see **AIOS-SPEC-006** for command rail” one-liner to reduce **mis-wiring** risk. **Also:** pointers to **`../../src/intent/spec009Types.ts`** resolve in **ai-os-voice-interface** but are **non-resolvable** in **aios-governing-docs** — label §19 as **voice-app informative** or mirror types here to avoid **normative vs repo-hint** confusion. | AIOS-SPEC-006 |

### 2. State vs skill boundary

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-010 | Low | §15.2–15.3 | Execution plans **map to registry skills** under policy; **§2.1** forbids modeling **shell-only** commands as **domain fulfillment**. The split is **normative**; **edge case:** a **Workspace** “skill” that manipulates chrome should be classified in **domain packs** as **shell-adjacent** or excluded — **SPEC-009** does not name that edge; **domain pack** discipline carries the burden. | §2.1, §15.2 |
| K-011 | Medium | §15.3 | **`ExecutionPlan`** requires **`temporalScope: TemporalScope`** unconditionally, while **`Intent.temporalScope`** is optional (**§5**). For **non–time-indexed** domains, implementations need a **product convention** (e.g. neutral preset, explicit “N/A”) to avoid type-level confusion between “optional on intent” and “required on plan.” | §5, §15.1–15.3 |

### 3. Authority / disclosure (primary vs operator)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-020 | Low | §12 | **Operator trace** must not be default primary; aligns with **AMD-2026-007** transparency posture. **Kernel note:** **§15.8** adds **retrieval / review mode** metadata — ensure **operator** surfaces expose **scope class + review mode** when debugging **web** steps without leaking them into **primary** mail/calendar UX. | §12, §15.8 |

### 4. Routing ambiguity (`app.*` / `governance.*` / `workspace.*`)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-030 | Medium | §16.4 | **“Voice / live customer-facing layers MAY use Gemini … for features not governed by §17”** creates a **classification burden**: implementers must decide what is “not governed by §17” while **§17** governs **sovereign** STT/TTS. Risk of **inconsistent** disclosure if **live** features share **session** with **Workspace interpretation** (**§16**). **Recommendation (non-blocking):** add a **single** clarifying sentence that **§16.1–16.3** default **Workspace text interpretation** rules **apply** unless the **task** is explicitly **outside** **mail/calendar interpretation** (product-defined enum). | §16.4, §17 |

### 5. Voice / UI parity (shell affordances)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-040 | Low | §13 vs §17 | **§13** defines **voice-first AI** broadly; **§17** narrows **sovereign** lanes (**POL-LANE-VOICE-001**–**003**). **Parity:** products **without** sovereign claims still owe **POL-INTENT** / **§10–12** UI truthfulness; **no conflict** — but **onboarding** docs should not cite **§13** alone when **§17** applies. | §13, §17 |
| K-041 | Low | §10, §18 (SPEC-006) | **Primary surface** grounding controls for time-indexed Workspace (**§10**) **SHOULD** align with **command rail / shell** affordances per **SPEC-006** — **kernel** check passes to **cross-spec** review; **SPEC-009** states the **intent** side adequately. | AIOS-SPEC-006, §10 |

### 6. Session truth / composed disclosure

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-050 | Medium | §6.3.1 (2), §6.7 | **Session context** may satisfy **temporal grounding** if a **valid** `TemporalScope` is already in **active intent state**. **Composed session summary** (**§6.7**) must **reflect** **defaulted** windows (**§6.3.1(3)**) so **session truth** does not **omit** that the system **narrowed** time — **kernel** risk is **stale** or **silent** carry-forward of scope. Recommend **conformance tests** (**§21**) explicitly cover **turn N default** → **turn N+1** disclosure. | §6.3.1, §6.7, POL-INTENT-004/005 |

---

## Overlap with triangulated committee

### A. AIOS-SPEC-009 Round 1 (same document) — [`../round_1/REVIEW_SYNTHESIS.md`](../round_1/REVIEW_SYNTHESIS.md)

| Kernel ID | Addressed in Round 1 committee? | Notes |
|-------------|--------------------------------|-------|
| **K-001** | **Partial** | OpenAI flags **§2** shell vs domain clarity; kernel focused **menu vs shell chrome** — same **§2.x** neighborhood, different angle. |
| **K-002** | **Partial** | Gemini flags **front matter** / **Style Guide**; kernel flagged **§19** `src/` paths — both **doc-hygiene**, not identical. |
| **K-010** | **No** | Committee did not surface **shell-adjacent Workspace skill** edge explicitly. |
| **K-011** | **No** | **Unique kernel** — committee did not discuss **`ExecutionPlan` vs `Intent` `temporalScope`** shape. |
| **K-020** | **Partial** | OpenAI **§12 transparency** depth; kernel **§15.8** operator fields for **web** — overlapping **disclosure** theme. |
| **K-030** | **No** | **Unique kernel** — committee **praised** **§16–§17** (Gemini); no **§16.4** vs **§17** classification carve-out. |
| **K-040** | **No** | Not a committee theme in Round 1 scorecard narrative. |
| **K-041** | **No** | Not surfaced. |
| **K-050** | **Partial** | Gemini **§6.3** “weasel words” / policy thresholds — **same** temporal-grounding **problem cluster** as kernel **session-truth** carry-forward; kernel **more** **UX/session-composition** specific. |

**Unique kernel yield (vs Round 1):** **K-011**, **K-030**, **K-010**, **K-040**, **K-041**, and **part** of **K-002** (repo-relative **§19** paths vs Style **cross_references**).

**Committee unique (vs kernel):** **§15.4** Funded Data Account / **cost disclosure**; **MPOA** **liability** for approved plans; **“verified playbook”** vs liability; **front matter** Style Guide compliance — **not** in original kernel tables.

### B. Prior related reviews (other documents)

| Kernel finding ID | Addressed elsewhere? | Committee / synthesis ref |
|-------------------|--------------------|---------------------------|
| K-001, K-010 (shell vs domain / routing plane) | **Partial** (doctrine level) | **[AMD-2026-007 Round 2 synthesis](../../amd_2026_007/round_2/REVIEW_SYNTHESIS.md)** — **§11.9** vs **SPEC-009** non-duplication, **POL-SHELL-004**. |
| Runtime / §16–17 | **Partial** | [`ollama_runtime_standard/round_2/`](../../ollama_runtime_standard/round_2/), [`whisper_runtime_standard/round_2/`](../../whisper_runtime_standard/round_2/), [`local_tts_runtime_standard/round_2/`](../../local_tts_runtime_standard/round_2/). |

### C. v0.5.3 revision + Round 1 Pass B (2026-04-14) — overlap refresh

**Specification** now encodes **policy-defined thresholds** (**§6.3.1**), **composed session truth** (**§6.7**), **§8.1–8.2** multi-modal/session rules, **§12** disclosure structure, **§15.4** economic disclosure, **§15.5.1** MPOA liability, **promoted playbook** terminology, and **Style Guide**-style **`cross_references`**.

| Kernel ID | Resolved or reduced by v0.5.3 text? | Notes |
|-----------|-------------------------------------|-------|
| **K-011** | **Partial** | **`ExecutionPlan.temporalScope`** semantics unchanged; **§6.3.1** thresholds reduce **ambiguity** for time-indexed use; **non–time-indexed** convention still **product**-defined. |
| **K-030** | **Unchanged** | **§16.4** carve-out not **reopened** in this revision round. |
| **K-050** | **Yes** | **§6.7** now **requires** **TemporalScope** in **composed session summary** when **defaulted**. |
| **K-002** | **Partial** | **Front matter** **citations** improve **governance-repo** clarity; **§19** **`src/`** paths remain **voice-repo** informative. |
| **K-001** | **Partial** | **§2.1** **example** clarifies **shell vs domain**. |

**Committee (Pass B) vs kernel:** **Economic** / **MPOA** items from **Round 1 Pass A** are **reflected** in **§15.4–15.5.1**. **Kernel-unique** items (**K-030**, **K-011** edge, **§19** paths) remain **valid** **advisory** **follow-ups**.

---

## Sign-off

| Role | Name | Date |
|------|------|------|
| Kernel reviewer | AIOS Kernel Shadow Pilot (Coordinator) | 2026-04-06 |
| Overlap update (Round 1 vs kernel) | AIOS Kernel Shadow Pilot (Coordinator) | 2026-04-10 |

---

*Advisory / non-binding — AMD-2026-010 §4.4.*
