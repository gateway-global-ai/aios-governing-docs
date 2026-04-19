---
document_id: AIOS-SCHEMA-ROUTE-STORAGE-INVENTORY-001
version: 0.1.1
status: draft
category: reference
title: Schema, route, and storage inventory for the restored planner and review system
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001
    title: Pre-architecture discovery agent for five-pass system research
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy
  - doc_id: AIOS-SYSTEMS-AND-PLANNING-MANUAL-001
    title: Systems and planning manual for planner/knowledge-base restoration
note: Consolidated inventory of the main structured surfaces and route/state paths in the current governance system.
---

# AIOS-SCHEMA-ROUTE-STORAGE-INVENTORY-001

## Purpose

Collect the current schema-bearing, route-bearing, and storage-bearing surfaces that the repaired planner system must understand and expose.

## Schema inventory

| Surface | Primary artifact | Notes |
|---------|------------------|-------|
| intake identity/status/events | `reviews/<slug>/intake/*.yaml` | lane lifecycle state and append-only intake memory |
| discovery scope | `reviews/<slug>/planning/DISCOVERY_SCOPE.yaml` | declared taxonomy classes, discovery profile, and source rules for discovery |
| discovered packet | `reviews/<slug>/planning/DISCOVERED_KNOWLEDGE_PACKET.yaml` | discovery-built packet for downstream research/drafting |
| pre-architecture discovery suite | `reviews/<slug>/planning/pre_architecture/*.md` | five-pass current-system discovery outputs used before architect planning when required |
| review packet identity/status/events | `reviews/<slug>/round_<N>/*.yaml` | peer-review packet taxonomy |
| knowledge packet | `reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml` | declared source set for one planning lane |
| built KB manifest | `reference/knowledge_base/agents/corpus/build_manifest.json` | proves bundle composition |
| execution transaction | `reference/schemas/execution_transaction.schema.json` | isolated execution demo packet |
| CANI envelopes and persisted artifacts | CANI validator/writer contracts | observation, recommendation, and normalized intake surfaces |

## Route inventory

| Route family | Entry | Destination / effect |
|--------------|-------|----------------------|
| intake lifecycle | `scripts/amendment_intake_agent.py` | evidence -> architect -> UI -> committee -> author revision -> peer review -> ratification handoff |
| discovery lane | `reviews/<slug>/planning/DISCOVERY_SCOPE.yaml` + `scripts/run_ollama_revision_loop.py` | `DISCOVERY_REPORT.md`, `DISCOVERED_KNOWLEDGE_PACKET.yaml`, and when required the five-pass pre-architecture suite |
| pre-architecture discovery lane | `reference/knowledge_base/cursor_research_pack.md` + discovery scope | five-pass discovery outputs before architect planning |
| architect lane | `scripts/intake_phases.py` + `scripts/ollama_planning_agent.py` | `reviews/<slug>/planning/ARCHITECT_PLAN.md` |
| UI lane | `scripts/intake_phases.py` + `scripts/ollama_planning_agent.py` | `reviews/<slug>/planning/UI_PLAN.md` |
| peer review | `scripts/peer_review.py` | `reviews/<slug>/round_<N>/` review docs and packet YAMLs |
| packet validation | `scripts/validate_review_packet.py` | packet accept/block signal |
| intake validation | `scripts/validate_intake_state.py` | intake accept/block signal |
| author-like drafting | `scripts/ollama_authoring_agent.py` | bounded drafting output from declared manifests |
| CANI normalization | `scripts/normalize_cani_*` | normalized intake envelope output |
| CANI validation | `scripts/validate_cani_artifacts.py` | pass / fail / blocked / advisory outcome |
| CANI persistence | `scripts/write_cani_artifacts.py` | repo-local persisted CANI artifacts |

## Storage and state inventory

| Storage surface | Ownership model | State type |
|-----------------|-----------------|------------|
| `reviews/<slug>/planning/` | planning lane | templates, plans, committee packet, provenance status, knowledge packet |
| `reviews/<slug>/planning/DISCOVERY_*` | discovery lane | scope, assignment, report, future discovered packet |
| `reviews/<slug>/planning/pre_architecture/` | pre-architecture discovery lane | five-pass discovery outputs used before architect planning |
| `reviews/<slug>/intake/` | intake scaffold | identity, mutable status, append-only events, non-authoritative handoff note |
| `reviews/<slug>/round_<N>/` | peer review | review docs, packet yaml, synthesis, gate report |
| `reviews/<slug>/kernel/` | kernel shadow lane | advisory review only |
| `reviews/<slug>/ratification/` | ratification support | handoff artifacts, non-ratifying support docs |
| `reference/knowledge_base/agents/corpus/` | generated bundle state | current built knowledge bundle and build manifest |
| `reference/knowledge_base/review_surface/` | review interface data | TOC, approval states, role attachments |
| `templates/governance_system/` | neutral source-of-truth templates | structure only, no lane-specific doctrine |

## Storage rule

Mutable state belongs in status artifacts. Append-only history belongs in events artifacts. Human-readable orientation belongs in markdown handoff notes. No lane should hide workflow truth only in prose.
