# AIOS Governance Changelog

All notable changes to the governing document set are recorded here.

## Tagging Convention

- Ratified versions: `v{version}-{doc-slug}` (e.g., `v1.0.0-technical-manifesto`)
- System milestones: `system-v{version}` (e.g., `system-v1.0`)

---

## [Unreleased] — Governance + Google Workspace pack (2026-04-02)

### Added

- Draft [`specifications/GoogleWorkspaceIntegrationGovernance.md`](specifications/GoogleWorkspaceIntegrationGovernance.md) (**AIOS-SPEC-007**): two-layer taxonomy (Layer 1 scope classes, Layer 2 intents; **one intent → one scope class**), control plane, routing envelope, POL-WORKSPACE-001–006, phased deployment, MCP adapter failure handling.
- Draft amendment [`amendments/AMD-2026-006.md`](amendments/AMD-2026-006.md): Google Workspace governed integration plane.
- **Ratified** amendment [`amendments/AMD-2026-005.md`](amendments/AMD-2026-005.md) (v1.0.0): workspace model, governed interface surfaces, authoritative schema, deterministic intent-failure policy, phased migration, supersession of post–peer-review human audit in non-constitutional guides.
- Source package [`sources/AMD-2026-005/`](sources/AMD-2026-005/) (impact study, gap analysis, disposition).
- Peer reviews Round 1 [`reviews/AMD-2026-005/round_1/`](reviews/AMD-2026-005/round_1/); Round 2 reviews + [`ratification_processor_output.md`](reviews/AMD-2026-005/round_2/ratification_processor_output.md) (**READY_FOR_RATIFICATION**).
- [`prompts/ratification_processor.md`](prompts/ratification_processor.md): reusable ratification processor prompt.
- Amendment workflow templates [`amendment_workflow/templates/AMD-2026-005.md`](amendment_workflow/templates/AMD-2026-005.md) and [`AMD-2026-005-meta.json`](amendment_workflow/templates/AMD-2026-005-meta.json).

### Changed

- [`specifications/AgentIntegrationProtocol.md`](specifications/AgentIntegrationProtocol.md) **v1.2.0**: **§11** Google Workspace governed intents (SPEC-007); prior **v1.1.0** Amendment Program + **§§7–10** (AMD-2026-005).
- [`specifications/UIComponentRegistryStandard.md`](specifications/UIComponentRegistryStandard.md) **v1.2.0**: **§13** Workspace canvas surfaces; appendices **§14**; prior **v1.1.0** **§§8–12** (AMD-2026-005).
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
