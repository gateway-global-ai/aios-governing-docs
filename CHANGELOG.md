# AIOS Governance Changelog

All notable changes to the governing document set are recorded here.

## Tagging Convention

- Ratified versions: `v{version}-{doc-slug}` (e.g., `v1.0.0-technical-manifesto`)
- System milestones: `system-v{version}` (e.g., `system-v1.0`)

---

## [Unreleased] — Governance + Google Workspace pack (2026-04-02)

### Added

- **Enforcement activation (2026-04-07):** [`.github/workflows/governance-integrity.yml`](.github/workflows/governance-integrity.yml) (`scripts/governance_integrity_check.py`: G-1, G-3, G-7, YAML parse); [`operations/GitHubBranchProtectionActivationChecklist.md`](operations/GitHubBranchProtectionActivationChecklist.md) (**AIOS-OPS-008**); [`operations/CursorEnforcementContract.md`](operations/CursorEnforcementContract.md) (**AIOS-OPS-009**); [`reference/schemas/cursor_preflight.schema.json`](reference/schemas/cursor_preflight.schema.json); [`.github/pull_request_template.md`](.github/pull_request_template.md) (from `reference/templates/governance_pr_template.md`); controlled [`reference/agent_registry.yaml`](reference/agent_registry.yaml) rows **aios-gov-agent-audit-001**, **aios-gov-agent-drafting-001**, **aios-gov-agent-review-001**.
- **Ratified (2026-04-07)** — **Governance Enforcement Package v1:** [`amendments/AMD-2026-010.md`](amendments/AMD-2026-010.md) **v1.0.2** with repository record [`amendments/AMD-2026-010-ratification-motion.md`](amendments/AMD-2026-010-ratification-motion.md); **AIOS-OPS-004** / **AIOS-OPS-005** / **AIOS-SPEC-012** at **v1.1.0** (incorporated by reference per motion). Implementation plans (non-normative): [`operations/GitHubGovernanceGatesImplementationPlan.md`](operations/GitHubGovernanceGatesImplementationPlan.md) (**AIOS-OPS-006**), [`operations/CursorAgentExecutionRulesImplementationPlan.md`](operations/CursorAgentExecutionRulesImplementationPlan.md) (**AIOS-OPS-007**). Empty-safe [`reference/agent_registry.yaml`](reference/agent_registry.yaml); templates [`reference/templates/agent_registration_template.yaml`](reference/templates/agent_registration_template.yaml), [`reference/templates/governance_pr_template.md`](reference/templates/governance_pr_template.md).
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

### Changed

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
