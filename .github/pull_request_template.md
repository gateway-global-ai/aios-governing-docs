# Pull request — governance repository

## Summary

<!-- What this PR does (short). -->

## Governing documents

- **Primary `document_id`(s) affected:**
- **Lifecycle state of change:** <!-- draft | under_review | ratified -->
- **Change type (pick one):**
  - [ ] **Doctrinal** (normative law, amendments, specs)
  - [ ] **Enforcement** (rules, CI, registry, agent registry)
  - [ ] **Implementation support** (templates, checklists, non-normative docs)

## Registry

- [ ] **`py -3 scripts/registry_generator.py`** run after front-matter changes to governed markdown (if applicable)

## GitHub vs AIOS governance

- **GitHub** = merge mechanics and **required status checks** (CI). A GitHub **Approve** is **not** AIOS triangulated peer review, thresholds, or ratification in-repo (**AMD-2026-005**).
- **Required status checks** still gate merge when enabled on `main`.
- If this PR changes **governed** documents or material governance text, reference **in-repo** artifacts when applicable (e.g. `reviews/…`, ratification output, amendment paths).

## Agent / automation

- [ ] **Agent-originated PR** (bot / automation account)
- If yes: **`agent_id:`** line in PR body matching **`reference/agent_registry.yaml`**
- [ ] **Preflight / CI:** `aios_preflight_complete` or required check satisfied (**AIOS-OPS-005** **I-5** when applicable)

## Review

- **Peer review path** (if required for this change): <!-- e.g. reviews/... -->

## Checklist

- [ ] **Status checks** expected to pass (e.g. Governance integrity / `pytest` when applicable).
- [ ] **Review / ratification artifacts** linked or noted if this PR changes governed docs or governance substance.
- [ ] **`CHANGELOG.md`** updated if the change is user-visible.

---

*PR body template — GitHub vs AIOS governance; see **README.md** and **DEVELOPER.md**. Not a governed law document.*
