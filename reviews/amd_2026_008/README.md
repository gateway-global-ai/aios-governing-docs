# Peer review — AMD-2026-008 (sovereign voice and local runtime lanes)

**Post-ratification historical record** (not an open revision queue): [`revision_log.md`](revision_log.md).

**Status:** **`ratified` `1.0.0`** **2026-04-08** (substantive basis **draft v1.2.0**) — **[`AMD-2026-008.md`](../../amendments/AMD-2026-008.md)**. **Motion:** **[`AMD-2026-008-ratification-motion.md`](../../amendments/AMD-2026-008-ratification-motion.md)** **v1.0.2** **`approved`** **2026-04-08** (packet **`council_ready`** **2026-04-09** — see motion **Date legend**). **Tracker:** [`AMD-AMENDMENT-REVIEW-TRACKER-001`](../../reference/implementation/AMD-AMENDMENT-REVIEW-TRACKER-001.md) **v1.2.6**.

## Triangulated peer review

| Round | Synthesis | Gate report | Reviews |
|-------|-----------|-------------|---------|
| **Round 2** (historical; pre–1.2.0 revision cycle) | — | — | [`round_2/`](round_2/) (six files) |
| **Round 3** (**v1.2.0**) | [`round_3/REVIEW_SYNTHESIS.md`](round_3/REVIEW_SYNTHESIS.md) | [`round_3/RATIFICATION_GATE_REPORT.md`](round_3/RATIFICATION_GATE_REPORT.md) | [`review_001_deepseek.md`](round_3/review_001_deepseek.md), [`review_002_openai.md`](round_3/review_002_openai.md), [`review_003_gemini.md`](round_3/review_003_gemini.md) |

**Round 3 (peer review):** Triangulation **satisfied** **[AMD-2026-005](../../amendments/AMD-2026-005.md)** ratification thresholds — see **`round_3/REVIEW_SYNTHESIS.md`**. **Amendment outcome:** **`ratified` `1.0.0`** **2026-04-08** (not merely a gate **PASS**).

**Implementation follow-on (not doctrine):** amendment **§4** / **§7** and **WORKSPACE.md** alignment in product repositories (e.g. **`ai-os-voice-interface`**).

## Incorporated package (amendment §3.1)

| Role | Document |
|------|----------|
| Lanes / policy | **AIOS-SPEC-009** — [`IntentPrimitiveAndExecutionModel.md`](../../specifications/IntentPrimitiveAndExecutionModel.md) |
| Ops | **OLLAMA_RUNTIME_STANDARD** / **AIOS-OPS-001** — [`OLLAMA_RUNTIME_STANDARD.md`](../../operations/OLLAMA_RUNTIME_STANDARD.md) |
| Ops | **WHISPER_RUNTIME_STANDARD** / **AIOS-OPS-002** — [`WHISPER_RUNTIME_STANDARD.md`](../../operations/WHISPER_RUNTIME_STANDARD.md) |
| Ops | **LOCAL_TTS_RUNTIME_STANDARD** / **AIOS-OPS-003** — [`LOCAL_TTS_RUNTIME_STANDARD.md`](../../operations/LOCAL_TTS_RUNTIME_STANDARD.md) |

**Note:** **AIOS-SPEC-008** (*Intent Discovery & Onboarding*) is a **different** document ID from **AMD-2026-008**; the amendment does not incorporate **AIOS-SPEC-008** under §3.1.

## AMD-2026-008 addenda — process backfill (composition / shell)

**Parent** **[AMD-2026-008](../../amendments/AMD-2026-008.md)** **is** **ratified**. **ADD-003** — **[Composition control plane](../../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** — is **`ratified` `1.0.0`** (**[motion](../../amendments/AMD-2026-008-ADD-003-ratification-motion.md)** **2026-04-10**); **pre-ratification** peer review lives under [`reviews/amd_2026_008_add_003_composition_control_plane_messages_invites_documents/`](../amd_2026_008_add_003_composition_control_plane_messages_invites_documents/). **ADD-001** and **ADD-002** **remain** **`draft`** **pending** **their** **own** **ratification** **cycles**. **Knowledge** **capture** **and** **partitioning** **memos** **(informative)** **backfill** **layers** **that** **ideally** **precede** **heavy** **addendum** **drafting**:

| Artifact | Role |
|----------|------|
| **[AIOS-COMPOSITION-CONTROL-RD-NOTES-001](../../reference/implementation/AIOS-COMPOSITION-CONTROL-RD-NOTES-001.md)** | R&D **principles**, **constraints**, **open** **questions** |
| **[AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001](../../reference/implementation/AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.md)** | **Bounded** **domains**, **dependency** **map**, **addendum** **seams** |
| **[AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001](../../reference/implementation/AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001.md)** | **Surface** **grammar**, **gates**, **user-visible** **states** |

## Cross-references

- **[AMD-2026-005](../../amendments/AMD-2026-005.md)** — triangulation thresholds.
- **[AIOS-AMD-PLAN-001](../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** — optional planning lifecycle.
