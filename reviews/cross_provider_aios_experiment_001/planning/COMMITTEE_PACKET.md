# Committee packet — `AIOS-CROSS-PROVIDER-AI-OS-EXPERIMENT-PROTOCOL-001` (draft)

**Date:** 2026-04-17  
**Review body:** Internal AIOS research committee  
**Purpose:** Advisory planning-completeness review before raw provider experiment runs are treated as evidence.

---

## 1. Packet summary

| Item | Link / value |
|------|--------------|
| Target document | `reference/implementation/AIOS-CROSS-PROVIDER-AI-OS-EXPERIMENT-PROTOCOL-001.md` |
| Knowledge packet | `reviews/cross_provider_aios_experiment_001/planning/RESULT_RECORD_SCHEMA.yaml` plus `SCENARIO_MATRIX.yaml` |
| Current state | The repo has a five-provider peer-review engine and a growing research set, but it does not yet have a governed harness for direct same-scenario cross-provider conversation testing. |
| Intent | Test whether an `80-app AI OS` pitch triggers shared planning failures across multiple providers under the same user profile. |
| Desired outcome | Produce a repeatable experiment lane with raw transcripts, structured result records, and a later five-provider review of the resulting report set. |
| Architect plan | Use a dedicated experiment harness that reuses provider callers from `scripts/context_assembler.py` without changing `scripts/peer_review.py` semantics. |
| UI plan | None; this is a research/evidence lane rather than a product UI lane. |
| Supporting evidence | `AIOS-PEER-REVIEW-MODEL-ROUTING-001`, `AIOS-REVIEW-PACKET-TAXONOMY-001`, `AIOS-RESEARCH-PACK-REPORT-SET-ANALYSIS-001`, the Case Study 001 family |

---

## 2. Decision questions

1. Are the declared inputs appropriate for a provider-comparative experiment lane?
2. Are `current state`, `intent`, and `desired outcome` stated explicitly and grounded in declared inputs?
3. Does the scenario matrix preserve equal-ground comparison rather than hidden prompt drift?
4. Are authority boundaries visible between raw experiment output, coordinator interpretation, and later peer review?
5. What remains unresolved before a first run can be considered governed evidence?

---

## 3. Committee outcome

| Field | Value |
|-------|-------|
| Outcome | Approve with changes |
| Recorded by | Cursor agent |
| Date | 2026-04-17 |
| Notes | The lane structure is sound. Before public use, the experiment report set should preserve a strict evidence boundary and avoid treating provider self-assessment as the final adjudicator without later synthesis. |

---

## 4. Next step

Implement the dedicated harness, preserve one raw transcript plus one structured result record per provider/scenario pair, then open `round_1/` under this review root and assemble a first report set before invoking the expanded five-provider peer-review flow over the report itself.
