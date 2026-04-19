# Governance system templates

This folder is the neutral source-of-truth template home for planner, review, knowledge-packet, and ratification scaffolds.

## Rules

- Templates in this folder carry structure only.
- Templates in this folder must not carry lane-specific doctrine, amendment IDs, spec IDs, product repo paths, or vendor-specific semantics.
- A lane becomes authoritative only when a declared knowledge packet is attached and the resulting output is human-reviewed in context.
- Historical lane-local templates may remain in old review folders for provenance, but they are not the reusable source-of-truth.
- Planning templates must require explicit metadata for `current_state`, `intent`, and `desired_outcome` so agents and reviewers share the same governing frame.

## Core templates

- `DISCOVERY_SCOPE_TEMPLATE.yaml`
- `DISCOVERY_ASSIGNMENT_TEMPLATE.md`
- `DISCOVERED_KNOWLEDGE_PACKET_TEMPLATE.yaml`
- `CROSS_PROVIDER_EXPERIMENT_SCENARIO_MATRIX_TEMPLATE.yaml`
- `CROSS_PROVIDER_EXPERIMENT_RESULT_RECORD_TEMPLATE.yaml`
- `PRE_ARCHITECTURE_01_ARCHITECTURE_CARTOGRAPHY_ASSIGNMENT_TEMPLATE.md`
- `PRE_ARCHITECTURE_02_IMPLICIT_CAPABILITY_EXTRACTOR_ASSIGNMENT_TEMPLATE.md`
- `PRE_ARCHITECTURE_03_GOVERNANCE_BREACH_AUDIT_ASSIGNMENT_TEMPLATE.md`
- `PRE_ARCHITECTURE_04_REGISTRY_MIGRATION_PLANNER_ASSIGNMENT_TEMPLATE.md`
- `PRE_ARCHITECTURE_05_CONTROL_PLANE_COVERAGE_AUDIT_ASSIGNMENT_TEMPLATE.md`
- `ARCHITECT_PLAN_TEMPLATE.md`
- `UI_PLAN_TEMPLATE.md`
- `COMMITTEE_PACKET_TEMPLATE.md`
- `PEER_REVIEW_TEMPLATE.md`
- `REVIEW_SYNTHESIS_TEMPLATE.md`
- `RATIFICATION_GATE_REPORT_TEMPLATE.md`
- `RATIFICATION_MOTION_TEMPLATE.md`
- `AGENT_KB_MANIFEST.template.yaml`

## Intended use

- taxonomy-first discovery lanes should begin from the discovery templates in this folder
- discovery scopes may declare a pre-architecture five-pass profile when current-system mapping is required before architect planning
- discovery should produce an explicit discovered packet before research or drafting runs begin
- `scripts/intake_templates.py` should copy planner scaffolds from this folder.
- Lane-specific `KNOWLEDGE_PACKET.yaml` files should be declared separately under the relevant review lane.
- Review surfaces may expose these templates as structure artifacts, but template structure never overrides amendment-specific governing inputs.
