# Pull request — governance repository (draft template)

**Installed copy:** [`.github/pull_request_template.md`](../../.github/pull_request_template.md) (2026-04-07). Edit either location and keep them aligned if both are retained.

## Governing documents

- **Primary `document_id`(s) affected:** <!-- e.g. AIOS-OPS-004 -->
- **Lifecycle state of change:** <!-- draft | under_review | ratified -->
- **Change type (pick one):**
  - [ ] **Doctrinal** (normative law, amendments, specs)
  - [ ] **Enforcement** (rules, CI, registry, agent registry)
  - [ ] **Implementation support** (templates, checklists, non-normative docs)

## Registry

- [ ] **`py -3 scripts/registry_generator.py`** run after front-matter changes to governed markdown (if applicable)

## Agent / automation

- [ ] **Agent-originated PR** (bot / automation account)
- If yes: **`agent_id:`** line in PR body matching **`reference/agent_registry.yaml`**
- [ ] **Preflight / CI:** `aios_preflight_complete` or required check satisfied (**AIOS-OPS-005** **I-5** when applicable)

## Review

- **Peer review path** (if required for this change): <!-- e.g. reviews/... -->

---

*Template only — not a governed law document.*
