# AMD-2026-016 planning lane

This lane now exists for a **separated local Ollama revision loop** so `AMD-2026-016` is not revised by an all-in-one coordinator path.

## Separation of powers

This lane is intentionally split into:

1. `discovery` — a bounded local run that starts from taxonomy classes and produces `DISCOVERY_REPORT.md`
2. `research` — a bounded local authoring run in `technical` mode that produces `LOCAL_RESEARCH_REPORT.md`
3. `drafting` — a separate bounded local authoring run that consumes the declared corpus plus discovery/research outputs and produces `DRAFT_AMENDMENT_PROPOSAL.md`
4. `review` — coordinator and peer review; this lane does **not** self-approve

The coordinator may compare, critique, and route outputs, but should not collapse research, drafting, and review into one undifferentiated act when benchmarking the system.

## Required local model surface

- model: `jt_authoring_agent`
- runner: `scripts/ollama_authoring_agent.py`
- wrapper: `scripts/run_ollama_revision_loop.py`
- manifest: `reference/knowledge_base/agents/style/JT_EDITORIAL_AMD_2026_016_REQUIRED_KNOWLEDGE_MANIFEST.yaml`

## Standard outputs

- `DISCOVERY_REPORT.md`
- `DISCOVERY_REPORT.md.run_record.json`
- `LOCAL_RESEARCH_REPORT.md`
- `LOCAL_RESEARCH_REPORT.md.run_record.json`
- `DRAFT_AMENDMENT_PROPOSAL.md`
- `DRAFT_AMENDMENT_PROPOSAL.md.run_record.json`

## Assignments

- `DISCOVERY_SCOPE.yaml`
- `DISCOVERY_ASSIGNMENT.md`
- `RESEARCH_ASSIGNMENT.md`
- `DRAFTING_ASSIGNMENT.md`

These files are the repeatable task contracts for the local Ollama lanes. They are not freeform coordinator notes.

## Standard command surface

```bash
py -3 scripts/run_ollama_revision_loop.py ^
  --review-slug amd_2026_016 ^
  --manifest reference/knowledge_base/agents/style/JT_EDITORIAL_AMD_2026_016_REQUIRED_KNOWLEDGE_MANIFEST.yaml ^
  --step full ^
  --discovery-include reviews/amd_2026_016/round_1/review_001_deepseek__AMD-2026-016.md ^
  --discovery-include reviews/amd_2026_016/round_1/review_002_openai__AMD-2026-016.md ^
  --discovery-include reviews/amd_2026_016/round_1/review_003_gemini__AMD-2026-016.md ^
  --discovery-include reviews/amd_2026_016/round_1/review_004_claude__AMD-2026-016.md ^
  --discovery-include reviews/amd_2026_016/round_1/review_005_minimax__AMD-2026-016.md ^
  --research-include reviews/amd_2026_016/round_1/review_001_deepseek__AMD-2026-016.md ^
  --research-include reviews/amd_2026_016/round_1/review_002_openai__AMD-2026-016.md ^
  --research-include reviews/amd_2026_016/round_1/review_003_gemini__AMD-2026-016.md ^
  --research-include reviews/amd_2026_016/round_1/review_004_claude__AMD-2026-016.md ^
  --research-include reviews/amd_2026_016/round_1/review_005_minimax__AMD-2026-016.md ^
  --draft-include reviews/amd_2026_016/round_1/review_001_deepseek__AMD-2026-016.md ^
  --draft-include reviews/amd_2026_016/round_1/review_002_openai__AMD-2026-016.md ^
  --draft-include reviews/amd_2026_016/round_1/review_003_gemini__AMD-2026-016.md ^
  --draft-include reviews/amd_2026_016/round_1/review_004_claude__AMD-2026-016.md ^
  --draft-include reviews/amd_2026_016/round_1/review_005_minimax__AMD-2026-016.md
```

## Lane rule

This planning lane produces bounded local discovery, research, and draft artifacts only.

- It does not ratify.
- It does not replace peer review.
- It does not authorize silent doctrine mutation.
- It exists so the research and drafting work can be repeated, compared, and improved over time.
