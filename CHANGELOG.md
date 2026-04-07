# AIOS Governance Changelog

All notable changes to the governing document set are recorded here.

## Tagging Convention

- Ratified versions: `v{version}-{doc-slug}` (e.g., `v1.0.0-technical-manifesto`)
- System milestones: `system-v{version}` (e.g., `system-v1.0`)

---

## [Unreleased] — Governance + Google Workspace pack (2026-04-02)

### Added

- **Kernel shadow pilot (process):** [`reviews/kernel_shadow/README.md`](reviews/kernel_shadow/README.md), [`reviews/kernel_shadow/pilot_runs/README.md`](reviews/kernel_shadow/pilot_runs/README.md); templates [`templates/kernel_shadow_review_brief.md`](templates/kernel_shadow_review_brief.md), [`templates/kernel_shadow_findings.md`](templates/kernel_shadow_findings.md), [`templates/kernel_shadow_pilot_metrics.md`](templates/kernel_shadow_pilot_metrics.md). [`reviews/README.md`](reviews/README.md) — kernel folder convention + advisory/non-binding reminder.
- **Ratified** amendment [`amendments/AMD-2026-010.md`](amendments/AMD-2026-010.md) (**v0.2.0**): **Kernel Engineer** role; **kernel review lane** (shadow pilot); **§4.4** legal status of pilot findings (advisory/non-binding for gates); motion [`amendments/AMD-2026-010-ratification-motion.md`](amendments/AMD-2026-010-ratification-motion.md) v1.0.0 (**2026-04-08**). Peer reviews [`reviews/amd_2026_010/`](reviews/amd_2026_010/). Policy index [`reference/AIOS_POLICY_INDEX.md`](reference/AIOS_POLICY_INDEX.md) v1.1.0 — AMD-2026-010 entry (no new `POL-*` ids).
- **Automation (optional):** [`scripts/governance_portfolio_review.py`](scripts/governance_portfolio_review.py) + [`prompts/governance_portfolio_review_prompt.md`](prompts/governance_portfolio_review_prompt.md) — corpus / portfolio review (outputs under `portfolio_reviews/`, gitignored). [`scripts/automated_review_pipeline.py`](scripts/automated_review_pipeline.py) — automated multi-round peer review + OpenAI revision loop (uses [`review_queue.json`](review_queue.json) with `--next`, or `--document PATH`; writes under `reviews/<slug>/automated_runs/`, gitignored). See [`DEVELOPER.md`](DEVELOPER.md).
- **Synced from** [`ai-os-voice-interface`](https://github.com/gateway-global-ai/ai-os-voice-interface) **`governing_docs/`** into this repository: amendments **AMD-2026-007** through **AMD-2026-009** (and related addenda/checklists), specifications **AIOS-SPEC-008** (Intent Discovery / Onboarding), **AIOS-SPEC-009** (Intent Primitive and Execution Model), **AIOS-SPEC-010** (Execution Scope and Context Bounding), **AIOS-SPEC-009-CONFORMANCE-TEST-V1**, peer-review trees under `reviews/` (AMD-2026-008/009, execution-scope, runtime standards), [`legal/`](legal/) (LEGAL-001/002), [`operations/`](operations/) (Ollama / Whisper / local TTS runtime standards), [`prompts/automated_openai_revision.md`](prompts/automated_openai_revision.md), [`review_queue.json`](review_queue.json), and [`scripts/ci_governance_dry_run.py`](scripts/ci_governance_dry_run.py) for CI parity with the voice repo.
- **Document ID alignment:** **AIOS-SPEC-009** is reserved for *Intent Primitive and Execution Model* (per **AMD-2026-008** / **AMD-2026-009**). The **Security & Sandboxing Model** is renumbered to **AIOS-SPEC-011**; [`specifications/ExecutionScopeAndContextBounding.md`](specifications/ExecutionScopeAndContextBounding.md) references to security logging / emergency provisions were updated accordingly.
- `scripts/registry_generator.py`: scan `legal/` and `operations/`; normalize `cross_references` that are plain strings (YAML list entries).
- [`sources/AMD-2026-007/`](sources/AMD-2026-007/) source notes for **AMD-2026-007** (supplements the voice-synced amendment at [`amendments/AMD-2026-007.md`](amendments/AMD-2026-007.md), **v0.1.0** draft).
- Draft [`specifications/GoogleWorkspaceIntegrationGovernance.md`](specifications/GoogleWorkspaceIntegrationGovernance.md) (**AIOS-SPEC-007**): two-layer taxonomy (Layer 1 scope classes, Layer 2 intents; **one intent → one scope class**), control plane, routing envelope, POL-WORKSPACE-001–006, phased deployment, MCP adapter failure handling.
- Draft amendment [`amendments/AMD-2026-006.md`](amendments/AMD-2026-006.md): Google Workspace governed integration plane.
- **Ratified** amendment [`amendments/AMD-2026-005.md`](amendments/AMD-2026-005.md) (v1.0.0): workspace model, governed interface surfaces, authoritative schema, deterministic intent-failure policy, phased migration, supersession of post–peer-review human audit in non-constitutional guides.
- Source package [`sources/AMD-2026-005/`](sources/AMD-2026-005/) (impact study, gap analysis, disposition).
- Peer reviews Round 1 [`reviews/AMD-2026-005/round_1/`](reviews/AMD-2026-005/round_1/); Round 2 reviews + [`ratification_processor_output.md`](reviews/AMD-2026-005/round_2/ratification_processor_output.md) (**READY_FOR_RATIFICATION**).
- [`prompts/ratification_processor.md`](prompts/ratification_processor.md): reusable ratification processor prompt.
- Amendment workflow templates [`amendment_workflow/templates/AMD-2026-005.md`](amendment_workflow/templates/AMD-2026-005.md) and [`AMD-2026-005-meta.json`](amendment_workflow/templates/AMD-2026-005-meta.json).
- [`.github/pull_request_template.md`](.github/pull_request_template.md): minimal PR body template (GitHub vs AIOS governance, checklist).

### Changed

- **[AIOS-SPEC-009](specifications/IntentPrimitiveAndExecutionModel.md)** **v0.5.5** — **ratified** (**2026-04-06**): **§12.2** **PolicyRecord** (**AIOS-SPEC-002**) **execution-readiness** threshold; **§12.3** **confidence** **UX** policy; Path B coordinator sign-off [`reviews/intent_primitive_execution_model/round_2/EDITORIAL_APPROVAL_v0.5.5.md`](reviews/intent_primitive_execution_model/round_2/EDITORIAL_APPROVAL_v0.5.5.md).
- **Post-ratification §6 alignment (AMD-2026-007):** [AIOS-SPEC-006](specifications/UIComponentRegistryStandard.md) **v1.3.1** — shell state vs skill/capability registry, command rail, **POL-SHELL-004**; [AIOS-SPEC-009](specifications/IntentPrimitiveAndExecutionModel.md) **v0.5.2** — **§2.1** shell vs domain intent boundary; [AIOS-SPEC-007](specifications/GoogleWorkspaceIntegrationGovernance.md) **v0.1.3** — **§6–§9** **§6.2** annex (UI transparency, primary vs operator, **POL-*** tables, Workspace presentation); **§10** tenant/runbook out-of-repo + **AIOS-SPEC-012** schema deferral; [AIOS-SPEC-008](specifications/IntentDiscoveryOnboardingFramework.md) **v0.1.1** — **§3.1**/**§3.8**/**§18** AMD-2026-007 §6.1; **[AIOS-SPEC-012](specifications/WorkspaceDomainPackV1.md)** **v0.1.0** — Domain Pack skeleton. [AMD-2026-007](amendments/AMD-2026-007.md) **§14** checklist updated.
- **[AMD-2026-007](amendments/AMD-2026-007.md) v0.2.1 — ratified (`ratification_target` **2026-04-07**):** Motion **[AMD-2026-007-RATIFICATION-MOTION](amendments/AMD-2026-007-ratification-motion.md)** v1.0.0 approved; Round 2 peer review [`reviews/amd_2026_007/round_2/`](reviews/amd_2026_007/round_2/). §14 in-repo: [`reference/AIOS_POLICY_INDEX.md`](reference/AIOS_POLICY_INDEX.md) registers **§5** policy IDs.
- **[AMD-2026-007](amendments/AMD-2026-007.md) v0.2.0:** §11.9 *Shell state controls vs skills and voice parity*; **POL-SHELL-004**–**006**; Round 1 triangulated peer review under [`reviews/amd_2026_007/round_1/`](reviews/amd_2026_007/round_1/) (**READY_FOR_ROUND_2** per **RATIFICATION_GATE_REPORT**, not final ratification).
- [`README.md`](README.md), [`DEVELOPER.md`](DEVELOPER.md), [`reviews/README.md`](reviews/README.md): document **solo-maintainer** GitHub policy—**required status checks** on, **GitHub required human approval** optional; **AIOS** review/ratification remains in-repo (**AMD-2026-005** path); org **rulesets** may override repo settings.
- [`README.md`](README.md), [`DEVELOPER.md`](DEVELOPER.md): cross-reference PR template.
- [`specifications/AgentIntegrationProtocol.md`](specifications/AgentIntegrationProtocol.md) **v1.3.0**: **[AMD-2026-007](amendments/AMD-2026-007.md) Section 11** (Intent primitive in **§§7, 9**); **v1.2.0** **§11** Google Workspace (SPEC-007); prior **v1.1.0** Amendment Program + **§§7–10** (AMD-2026-005).
- [`specifications/UIComponentRegistryStandard.md`](specifications/UIComponentRegistryStandard.md) **v1.3.0**: **[AMD-2026-007](amendments/AMD-2026-007.md) Sections 11.4–11.6** (intent-driven primary surface in **§8**; governing-documents table); **v1.2.0** **§13** Workspace canvas surfaces; prior **v1.1.0** **§§8–12** (AMD-2026-005).
- [`specifications/GoogleWorkspaceIntegrationGovernance.md`](specifications/GoogleWorkspaceIntegrationGovernance.md) **v0.2.0**: **[AMD-2026-007](amendments/AMD-2026-007.md) Section 11** (intent resolution before Layer 2 routing).
- [`DEVELOPER.md`](DEVELOPER.md): normative lifecycle paragraph links **AMD-2026-007** with SPEC cross-references.
- [`DEVELOPER.md`](DEVELOPER.md): binding lifecycle block with links to AMD-2026-005 and SPEC sections; clarifies “human ratification” vs post-PR audit.
- [`templates/amendment_template.md`](templates/amendment_template.md): ratification checklist aligned with ratified AMD-2026-005 and AIOS-SPEC-003/006.

---

## [system-v1.0] - 2026-04-02

### Added
- Initial governance system with 5-stage document lifecycle
- 11-dimension grading rubric (full) and 5-dimension rubric (light)
- Triangulated peer review engine (DeepSeek, OpenAI, Gemini)
- Source analysis pipeline with quarantine system
- Human ratification gate (requires explicit approval)
- Quick lifecycle mode (3-stage for specifications)
- Smart context injection (cross-reference-based)
- Cross-document conflict detector
- MCP governance server (FastMCP) for AI agent access
- REST API (FastAPI) with OpenAPI/Swagger documentation
- Shared governance service layer
- JSON schema extraction for NodeContract and PolicyRecord
- Document registry (markdown + JSON)
- Git integration with auto-commit and version tagging on ratification

### Core Documents (ratified)
- AIOS Technical Manifesto v1.0.0
- AIOS Governance Constitution v1.0.0
- AIOS Master Platform Operating Agreement v3.0.0

### Specifications (ratified)
- NodeContract Specification v1.0.0
- PolicyRecord Specification v1.0.0
- Agent Integration Protocol v1.0.0
- CLI Developer Guide v1.0.0
- Agent Integration Guide v1.0.0
