---
document_id: AIOS-SYSTEMS-AND-PLANNING-MANUAL-001
version: 0.1.1
status: draft
category: reference
title: Systems and planning manual for planner/knowledge-base restoration
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-PLANNER-DRIFT-PROVENANCE-LEDGER-001
    title: Planner drift provenance ledger and containment classification
  - doc_id: AIOS-AMD-PLAN-001
    title: Amendment pre-ratification planning lifecycle
  - doc_id: AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001
    title: Pre-architecture discovery agent for five-pass system research
  - doc_id: AIOS-AMENDMENT-INTAKE-SCAFFOLD-001
    title: Amendment intake scaffold standard
  - doc_id: AIOS-REVIEW-PACKET-TAXONOMY-001
    title: Review packet artifact taxonomy
  - doc_id: AMD-2026-013
    title: Intent-bearing repository taxonomy
note: Manual for the restored planner, knowledge packet, template, and review-surface model.
---

# AIOS-SYSTEMS-AND-PLANNING-MANUAL-001

## Purpose

This manual consolidates the operating model that was previously scattered across draft planning lanes, implementation notes, and local operator habits.

It exists so the planner, review, and ratification support surfaces can be understood as one governed system with visible inputs, roles, templates, states, and approval seams.

## Core diagnosis

The planner drift problem was not only a bad template path. It exposed a deeper issue:

- knowledge packet authority was implicit instead of declared
- taxonomy was not first-class in packet assembly
- discovery was not formalized as its own role before research and drafting
- roles existed, but their authority status was not surfaced clearly
- templates carried semantic content from a prior lane
- human review existed procedurally, but not as a first-class review surface

## Restored system model

### 1. Knowledge foundation

All planner and review work begins from declared repo artifacts, not hidden discussion or copied prior-lane planning output.

Knowledge assembly must follow:

1. taxonomy
2. discovery
3. explicit packet compilation
4. downstream research or drafting

The baseline packet layers are:

1. constitutional and philosophy root
2. Jason-authored philosophy and design artifacts where materially relevant
3. target amendment or target document
4. implementation/reference support
5. product evidence only when the lane actually depends on runtime state

If a lane depends on current runtime behavior before architecture planning can begin, the knowledge foundation should also include pre-architecture discovery outputs produced by the governed five-pass discovery suite.

### 2. Role model

Every lane is executed by a role with visible authority boundaries.

Core system roles:

- intake coordinator
- architect planner
- UI planner
- committee reviewer
- author / reviser
- peer-review coordinator
- kernel shadow reviewer
- ratification coordinator
- systems-manual reviewer

Each role must show:

- what packet it used
- whether the role is governing, advisory, operational, or local-only
- what human checkpoint remains required

### 3. Template model

Reusable templates now live under `templates/governance_system/`.

Those templates are:

- structural only
- lane-neutral
- reusable across amendments
- subordinate to the declared knowledge packet

Every planning template must also carry explicit planning metadata for:

- current state
- intent
- desired outcome

Those metadata fields are required because architect, UI, committee, and peer-review lanes cannot be trusted to infer the same purpose or success condition from prose alone.

### 4. Packet model

Each planning lane owns `reviews/<slug>/planning/KNOWLEDGE_PACKET.yaml`.

That packet is now the default manifest for evidence refresh and architect-lane execution. A shared manifest may still exist for manual review-surface assembly, but it is not the implicit packet for unrelated amendment lanes.

### 4A. Discovery model

Planning and amendment-revision lanes should move toward a taxonomy-first discovery model.

That means a lane should own:

- `DISCOVERY_SCOPE.yaml`
- `DISCOVERY_ASSIGNMENT.md`
- `DISCOVERY_REPORT.md`
- `DISCOVERED_KNOWLEDGE_PACKET.yaml`

The discovery role identifies eligible source classes before research or drafting begins.

When the lane needs current-system mapping before architecture planning, discovery should also run the governed pre-architecture five-pass suite:

- architecture cartography
- implicit capability extraction
- governance breach audit
- registry migration planning
- control-plane coverage audit

That suite is the discovery agent's pre-architecture mode, not a substitute for architect planning.

### 5. Transparency model

The system is not considered repaired unless a human reviewer can see:

- the declared packet
- the current lifecycle state
- the template source being used
- the provenance status of existing lane artifacts
- the next required human decision

## Dependency chain

The restored dependency order is:

`knowledge foundation -> taxonomy -> discovery -> pre-architecture discovery where required -> systems manual -> role model -> template model -> packet model -> review surface -> planner execution -> downstream review and ratification support`

## Human review gate

Human review is a hard operating seam, not a hidden assumption.

The following steps remain human-gated:

- architect verification
- UI verification
- committee outcome recording
- peer-review interpretation and next-step acceptance
- ratification motion approval / execution
- approval of the assembled knowledge-base review surface

## Lane repair rule

If a lane was created from the contaminated template/manifest path, it must stay one of:

- historical only
- relabeled as quarantined
- regenerated from the corrected packet and neutral templates

until its provenance is repaired.

## Manual appendices

This manual is implemented together with:

- `reference/implementation/AIOS-AGENT-AND-TOOLCHAIN-ROSTER-001.md`
- `reference/implementation/AIOS-SCHEMA-ROUTE-STORAGE-INVENTORY-001.md`
- `reference/implementation/AIOS-KNOWLEDGE-BASE-REVIEW-INTERFACE-MODEL-001.md`
- `reference/implementation/AIOS-PLANNER-DRIFT-PROVENANCE-LEDGER-001.md`

## Approval use

This manual is intended to be reviewed through the knowledge-base review surface before the planner repair is treated as fully trusted operating law.
