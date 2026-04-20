# Round 2 — review synthesis — AMD-2026-008-ADD-004

**Structured status:** See **[`PACKET_STATUS.yaml`](PACKET_STATUS.yaml)** and **[`PACKET_EVENTS.yaml`](PACKET_EVENTS.yaml)**. **Human-readable (same meaning):** **Artifact health** — **`healthy`**. **Review gate** — **FAIL** — see **[`RATIFICATION_GATE_REPORT.md`](RATIFICATION_GATE_REPORT.md)**. **Next** — **`revise`** while **`draft` `0.3.0`** remains the last reviewed version. **Committee** — **`closed_superseded_by_review`** — narrative [`../planning/COMMITTEE_PACKET.md`](../planning/COMMITTEE_PACKET.md).

**Document:** [`AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md`](../../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md) — **`draft` `0.3.0`**  
**Date:** 2026-04-09  
**Prior reviewed draft:** **`0.2.0`** — [`../round_1/REVIEW_SYNTHESIS.md`](../round_1/REVIEW_SYNTHESIS.md)  
**Reviews:** [`review_001_deepseek__AMD-2026-008-ADD-004.md`](review_001_deepseek__AMD-2026-008-ADD-004.md), [`review_002_openai__AMD-2026-008-ADD-004.md`](review_002_openai__AMD-2026-008-ADD-004.md), [`review_003_gemini__AMD-2026-008-ADD-004.md`](review_003_gemini__AMD-2026-008-ADD-004.md)  
**Manifest:** [`peer_review_manifest_20260409T170114Z.json`](peer_review_manifest_20260409T170114Z.json)

---

## Triangulation status

**Complete (three lanes):** **deepseek**, **openai**, **gemini** on **`--rubric light`** + **`--smart-context`**.

---

## Score snapshot

| Reviewer | Composite | Disposition |
|----------|-----------|-------------|
| DeepSeek | **2.8** | `major_revision_required` |
| OpenAI | **3.7** | `approved_with_changes` |
| Gemini | **4.4** | `approved_with_changes` |

**AMD-2026-005 thresholds:** composite **≥ 3.5** and **no dimension < 3** — **not satisfied** (DeepSeek composite **2.8**; DeepSeek scorecard also includes multiple dimensions at **2**). See **[`RATIFICATION_GATE_REPORT.md`](RATIFICATION_GATE_REPORT.md)**.

---

## What Round 2 improved

- **Round 1 response was real, not cosmetic.** OpenAI and Gemini both acknowledge meaningful improvement in **§2.1**, **§3.4**, **§11.1**, and **§12.4**.
- **Implementation seam and precedence posture are now substantially stronger.** The main Round 1 concerns about orphaned audit fields and ratified-vs-draft addendum ambiguity were materially reduced.
- **The gate is now viewed as operational doctrine, not just a concept note.** Two lanes judge the draft broadly workable with bounded follow-up tightening rather than wholesale rework.

---

## Convergent themes (remaining gaps)

1. **Policy proportionality still needs a non-waivable floor.** DeepSeek and Gemini both still see **§4.1** as the main loophole because policy can shape minimum proof without an explicit hard floor in the addendum itself.
2. **Policy authority remains underdefined.** OpenAI and Gemini both call out the repeated use of **policy** without clearly defining what governed authority can create, amend, or grant exceptions under that policy.
3. **The implementation home is improved but not fully closed.** All three lanes still want a stronger default conformance path for the review-target / audit contract, especially in **§6.1**, **§11.1**, and **§14**.
4. **Approval / exception taxonomy still needs tighter audit language.** OpenAI particularly notes that **§9–§11** should distinguish full, partial, blocked, and exception-based approval more explicitly.
5. **Editorial cleanup remains warranted, not foundational.** OpenAI flags over-bolded prose and shorthand cross-references as readability and citation-discipline issues rather than a doctrine-structure failure.

---

## Recommended next step

- **Revision required before any ratification path.** The packet should stay at **`review_gate_status: fail`** with **`next_action: revise`** on the assessed **`draft` `0.3.0`**.
- **Target the next author pass narrowly:** close the **§4.1** floor, define valid **policy** authority, and harden the default review-target / audit-home language before any later review cycle is opened.

---

*Synthesis — Round 2 — **`0.3.0`** — 2026-04-09.*
