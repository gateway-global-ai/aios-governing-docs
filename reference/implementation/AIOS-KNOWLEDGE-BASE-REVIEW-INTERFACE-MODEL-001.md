---
document_id: AIOS-KNOWLEDGE-BASE-REVIEW-INTERFACE-MODEL-001
version: 0.1.1
status: draft
category: reference
title: Intent-driven knowledge-base review interface model
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AIOS-SYSTEMS-AND-PLANNING-MANUAL-001
    title: Systems and planning manual for planner/knowledge-base restoration
  - doc_id: AIOS-AGENT-AND-TOOLCHAIN-ROSTER-001
    title: Agent, role, and toolchain roster
  - doc_id: AIOS-SCHEMA-ROUTE-STORAGE-INVENTORY-001
    title: Schema, route, and storage inventory
  - doc_id: AIOS-PLANNER-DRIFT-PROVENANCE-LEDGER-001
    title: Planner drift provenance ledger and containment classification
note: Review-surface model for human approval of the assembled knowledge base before restored planner trust is granted.
---

# AIOS-KNOWLEDGE-BASE-REVIEW-INTERFACE-MODEL-001

## Purpose

Define the human-facing review surface that exposes the restored knowledge base, role attachments, templates, provenance, and approval state in one place.

## Navigation model

The review surface should organize material by intent, not by raw folder browsing.

Primary review intents:

- `review.overview`
- `review.provenance`
- `review.roles`
- `review.scripts`
- `review.schemas`
- `review.routes`
- `review.storage`
- `review.templates`
- `review.packets`
- `review.ratification`

## Required visible elements

For every reviewable artifact, the surface must show:

- title
- source path
- authority status
- approval status
- related packet or manifest
- related role

## Approval states

Allowed review states:

- `pending_human_review`
- `approved`
- `approved_with_notes`
- `changes_requested`
- `historical_only`

## Aggregate status semantics

`reference/knowledge_base/review_surface/REVIEW_STATUS.yaml` carries both artifact-level review states and a surface-level aggregate posture.

- An artifact entry status applies only to that listed artifact.
- `overall_status` applies to the assembled review surface as a whole.
- One artifact may be `approved` while `overall_status` remains `pending_human_review` if other required review-surface artifacts are still awaiting approval.
- The aggregate surface state must not be read as silently overriding a more specific artifact entry, and an approved artifact entry must not be misread as approval of the entire review surface.

## Role attachment rule

Every critical role shown in the review surface must display its attached knowledge packet or manifest as a reviewable artifact. Hidden packet composition is treated as a repair failure.

## Decision transparency rule

The review surface must expose:

- which role acted
- what declared inputs were attached
- which inputs were required vs optional
- what lifecycle state the lane is in
- why a lane is blocked, quarantined, or ready

## Review gate rule

Approval of the assembled knowledge-base review surface is the explicit human gate before the repaired planner path can be considered trusted again.
