---
document_id: AIOS-AGENT-AND-TOOLCHAIN-ROSTER-001
version: 0.1.1
status: draft
category: reference
title: Agent, role, and toolchain roster for the restored planner system
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-SYSTEMS-AND-PLANNING-MANUAL-001
    title: Systems and planning manual for planner/knowledge-base restoration
  - doc_id: AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001
    title: Pre-architecture discovery agent for five-pass system research
  - doc_id: AIOS-SPEC-012
    title: Agent registry
  - doc_id: AIOS-GOVERNED-AUTHORING-KNOWLEDGE-INPUT-STANDARD-001
    title: Governed authoring knowledge inputs and bounded author-like drafting
note: Roster of system roles, operational agents, and principal scripts used by the current governance toolchain.
---

# AIOS-AGENT-AND-TOOLCHAIN-ROSTER-001

## Purpose

Provide one visible roster of who acts in the system, what authority they carry, and what scripts support them.

## Operational automation agents

| Agent / surface | Source | Role class | Authority status |
|-----------------|--------|------------|------------------|
| `aios-gov-agent-audit-001` | `reference/agent_registry.yaml` | governance audit | active, bounded, non-ratifying |
| `aios-gov-agent-drafting-001` | `reference/agent_registry.yaml` | governance drafting | active, bounded, non-ratifying |
| `aios-gov-agent-review-001` | `reference/agent_registry.yaml` | review | active, bounded, non-ratifying |
| local discover agent | taxonomy-first discovery lane | discovery | draft-producing only |
| pre-architecture discovery agent | five-pass system discovery suite | discovery | advisory discovery only |
| local architect planner | `scripts/ollama_planning_agent.py` | planning | draft-producing only |
| local UI planner | `scripts/ollama_planning_agent.py` | planning | draft-producing only |
| bounded JT authoring agent | `scripts/ollama_authoring_agent.py` | author-like drafting | advisory only |

## Governance and human roles

| Role | Primary responsibility | Authority status |
|------|------------------------|------------------|
| intake coordinator | initialize lanes, refresh evidence, record lifecycle movement | operational, non-ratifying |
| discover reviewer | review discovery scope and discovered packet before downstream use | human approval required |
| architect reviewer | review architecture-bearing planner output | human approval required |
| UI reviewer | review user-facing planning output | human approval required |
| committee reviewer | evaluate planning completeness before binding peer review | advisory committee gate |
| author / reviser | revise amendment or support text | governed drafting role |
| peer-review coordinator | run triangulated review and packet validation | operational, bound by AMD-2026-005 |
| kernel reviewer | advisory shadow review where applicable | advisory only |
| ratification coordinator | prepare or execute motion paths | manual constitutional/council seam |
| systems reviewer | review the assembled knowledge-base and packet model | human approval required |

## Principal scripts

| Script | Purpose |
|--------|---------|
| `scripts/amendment_intake_agent.py` | CLI entrypoint for the intake scaffold |
| `scripts/intake_phases.py` | lifecycle phase orchestration |
| `scripts/intake_paths.py` | deterministic path and lane-contract resolution |
| `scripts/intake_templates.py` | scaffolds planning, kernel, and ratification support files |
| `scripts/intake_state.py` | intake identity/status/events persistence |
| `scripts/intake_architect.py` | architect bundle/template validation helpers |
| `scripts/intake_ratification.py` | ratification handoff preparation |
| `scripts/build_agent_kb.py` | declared manifest to knowledge bundle build |
| `scripts/run_ollama_revision_loop.py` | separated local discovery/research/drafting wrapper |
| `scripts/ollama_planning_agent.py` | local architect/UI planning runner |
| `scripts/ollama_authoring_agent.py` | bounded author-like drafting runner |
| `scripts/peer_review.py` | triangulated peer review runner |
| `scripts/validate_review_packet.py` | packet taxonomy validator |
| `scripts/validate_intake_state.py` | intake taxonomy validator |
| `scripts/generate_product_context_bundle.py` | product snapshot builder |
| `scripts/registry_generator.py` | document registry regeneration |
| `scripts/preflight_local_agents.py` | local Ollama readiness checks |

## CANI script surfaces

| Script | Purpose |
|--------|---------|
| `scripts/cani_validator.py` | validate CANI envelopes and persisted artifacts |
| `scripts/cani_writer.py` | materialize repo-local CANI persisted artifacts |
| `scripts/cani_planning_artifact_normalizer.py` | normalize planning artifacts into CANI intake envelopes |
| `scripts/cani_review_artifact_normalizer.py` | normalize review artifacts into CANI intake envelopes |
| `scripts/cani_operator_note_normalizer.py` | normalize operator notes into CANI intake envelopes |

## Review and execution support scripts

| Script | Purpose |
|--------|---------|
| `scripts/review_packet_taxonomy.py` | exact-key and event discipline helpers for review packets |
| `scripts/assemble_manual_review_packet.py` | manual packet assembly support |
| `scripts/run_isolated_execution_demo.py` | produce isolated execution demonstration packets |
| `scripts/governance_integrity_check.py` | integrity checks over the governance repo |
| `scripts/automated_review_pipeline.py` | operator automation around review loops |

## Role hardening rule

No role listed here should act with hidden packet composition. A role is only reviewable when its declared packet or manifest can be shown beside the artifact it produced.
