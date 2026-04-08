# Revision log — AMD-2026-013 — Round 1 → Round 2

| Field | Value |
|-------|--------|
| **From** | v0.2.2 (Round 1 **PASS**, `approved_with_changes`) |
| **To** | v0.2.3 (frozen for Round 2) |
| **Date** | 2026-04-08 |

## Items addressed (narrow follow-on)

| Round 1 theme | Change |
|---------------|--------|
| Role accountability | New **§6.1** — architecture role vs builder tied to governed process and published maintainer policy (`CODEOWNERS` / `MAINTAINERS` / README). |
| Examples / clarity | **§2.2** examples (`reviews/demos/`, `reviews/amendments/…`); memo examples table row for classified demo root; **§1.1** shortened sentence. |
| AIOS-SPEC-009 alignment | **§1.4** row — paths consistent with intent domains where SPEC-009 applies; no new domains by paths alone. YAML `cross_references` **AIOS-SPEC-009**. |
| Optional validation | Memo **§F** — non-normative CI / integrity-check hook + dual-read reminder. |
| Style | Reduced prose density in **§1.1**; no bounded-thesis changes. |

## Explicitly out of scope

- New JSON schema mandate, new automation law, Phase 2 migration execution, product repo **must**-level rules.

## Companion memo

**AIOS-REPO-TAXONOMY-001** **v0.2.3** — §F conformance; examples row; frozen with amendment.

---

# Revision — v0.2.3 → v0.2.4 (Round 2 §6.1 accountability)

| Field | Value |
|-------|--------|
| **From** | v0.2.3 (Round 2 **PASS**, Gemini `approved_with_changes` on §6.1) |
| **To** | v0.2.4 |
| **Date** | 2026-04-08 |

## Items addressed (surgical)

| Round 2 concern | Change |
|-----------------|--------|
| **Architecture role** framed as “process” / non-normative planning as authority | **§6.1** — **Accountable actors** = **repository maintainer(s)** who **approve merge** of changes that declare or change taxonomy; **AIOS-AMD-PLAN-001** = **non-normative planning input only**; **higher-tier** route per **[Governance Constitution](../../core/governance_constitution.md)** (**AIOS-CORE-002**) where applicable. |
| **Builder** — “for example” left list non-binding | **§6.1** — **authoritative list** at repo root when published; **README** **precedence** if multiple; else **platform** **merge** model. |
| Memo alignment | **§C** opening sentence mirrors §6.1; memo **v0.2.4**. |

## Explicitly out of scope

- Creating **CODEOWNERS** / **MAINTAINERS** files in-repo (optional publish per §6.1); new constitutional offices; migration or path-class changes.

## Companion memo

**AIOS-REPO-TAXONOMY-001** **v0.2.4** — §C mirror only.
