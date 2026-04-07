---
artifact: kernel_shadow_findings
status: template
binding: false
advisory: true
normative_basis: AMD-2026-010 §4.4
---

# Kernel shadow findings — {DOCUMENT_ID} @ {VERSION}

**⚠ Advisory / non-binding (pilot)** — Per **[AMD-2026-010 §4.4](../amendments/AMD-2026-010.md)**, these findings **do not** gate ratification or merge. **[AMD-2026-005](../amendments/AMD-2026-005.md)** triangulated peer review remains the **sole binding** review path unless a future amendment authorizes a blocking kernel gate.

| Field | Value |
|-------|--------|
| **Target** | `{path/to/document.md}` |
| **Reviewer(s)** | |
| **Date** | |
| **Parallel triangulation** | Link to `reviews/{slug}/round_N/` (e.g. `REVIEW_SYNTHESIS.md`) |

## Executive summary

*(2–6 sentences: overall kernel-risk posture of the document; no disposition such as “approve” — advisory only.)*

---

## Findings by category

Use **severity** labels as **informative** only: **Critical** (invariant violation risk) / **High** / **Medium** / **Low** / **Observation**.

### 1. Shell / routing invariants

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-001 | | | | e.g. AMD-2026-007 §11.9, POL-SHELL-004 |

### 2. State vs skill boundary

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-010 | | | | e.g. AIOS-SPEC-009 §2.1 |

### 3. Authority / disclosure (primary vs operator)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-020 | | | | e.g. AMD-2026-007 §4.5 |

### 4. Routing ambiguity (`app.*` / `governance.*` / `workspace.*`)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-030 | | | | |

### 5. Voice / UI parity (shell affordances)

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-040 | | | | e.g. AMD-2026-007 §4.1 |

### 6. Session truth / composed disclosure

| ID | Severity | Location (§) | Finding | Norm / spec pointer |
|----|----------|--------------|---------|---------------------|
| K-050 | | | | |

---

## Overlap with triangulated committee

| Kernel finding ID | Addressed in triangulation? (Y/N/partial) | Committee review ref (file + §) |
|-------------------|-------------------------------------------|-----------------------------------|
| K-001 | | |

**Unique kernel yield:** *(IDs not clearly covered in committee reviews — list.)*

---

## Sign-off

| Role | Name | Date |
|------|------|------|
| Kernel reviewer | | |

---

*Template — save as `reviews/{slug}/kernel/KERNEL_SHADOW_FINDINGS.md`.*
