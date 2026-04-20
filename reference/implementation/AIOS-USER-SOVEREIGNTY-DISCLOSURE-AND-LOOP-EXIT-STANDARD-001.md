---
document_id: AIOS-USER-SOVEREIGNTY-DISCLOSURE-AND-LOOP-EXIT-STANDARD-001
version: 0.1.0
status: draft
category: reference_implementation
title: User sovereignty disclosure and loop-exit standard
author: Gateway Global AIOS
created: 2026-04-17
last_updated: 2026-04-17
cross_references:
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack v1, and Primary vs Operator UI
  - doc_id: AIOS-SPEC-009
    title: Intent Primitive and Execution Model
  - doc_id: AIOS-KB-RESEARCH-INTENT-SIGNAL-GOVERNANCE-001
    title: Research Studies - Intent Control Layer and Signal Governance
  - doc_id: AIOS-KB-RESEARCH-CHATGPT-OPERATING-MODEL-001
    title: Research Studies - ChatGPT Operating Model and Danger Analysis
  - doc_id: AIOS-DISCOVER-AGENT-PROCESS-001
    title: Discover-agent process for taxonomy-driven knowledge assembly
  - doc_id: AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001
    title: Pre-architecture discovery agent for five-pass system research
  - doc_id: AMD-2026-008-ADD-004
    title: Pre-Human Browser Review and Visual Proof Gate
  - doc_id: AIOS-BROWSER-REVIEW-GATE-RD-NOTES-001
    title: Browser review gate - R&D and knowledge capture
  - doc_id: AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001
    title: AI OS Shell UI Layout and Component Standard
  - doc_id: AIOS-VOICE-TTS-ARCHITECTURE-STANDARD-001
    title: AI OS Voice TTS Architecture Standard
note: Draft implementation standard for restoring user sovereignty through inspectable signal use, granular disclosure controls, explicit loop-exit surfaces, discovery-first sequencing, and rendered UI verification for voice-first AI systems.
---

# User sovereignty disclosure and loop-exit standard

## Purpose

Define the minimum implementation standard for restoring user sovereignty in AI-first systems.

This standard exists to prevent a recurring failure pattern:

- the platform benefits from hidden logging, hidden inference, hidden guardrails, or hidden behavioral adaptation
- the user cannot inspect or contest those hidden states
- planning collapses into dashboard-first or menu-first surface work before intent, discovery, and rendered proof are stable
- voice-first systems are trusted through summaries rather than through browser-visible output after each session

The system should therefore be designed so power returns to the user rather than remaining concentrated in opaque platform layers.

## Scope

This standard applies to AI-first systems that:

- capture user intent through voice, chat, or agent-driven interaction
- infer behavioral or emotional signals
- log conversation state, telemetry, or adaptation settings
- generate or revise UI components through coding agents or runtime composition
- claim voice-first operation or voice-first entry

This standard is implementation authority for reviewable design and runtime requirements. It does not by itself ratify a product release or replace existing amendment law.

## Core principle

If a hidden system behavior benefits the platform while increasing opacity, dependence, or user disadvantage, that behavior should be disclosed, inspectable, and user-governable.

## 1. User-visible disclosure requirements

### 1.1 Disclosure bar minimum

Any AI-first shell with persistent session behavior SHOULD expose a disclosure surface equivalent to an agent disclosure bar.

At minimum, that surface MUST allow the user to inspect:

- current acting identity or agent surface
- active model or route when material
- whether memory or session carry-forward is active
- whether logging is active
- whether behavioral adaptation is active
- whether special guardrails or policy modes are active
- whether voice analysis, transcript storage, or UI-generation instrumentation is active

### 1.2 Hidden conflict disclosure

The system SHOULD disclose when a meaningful conflict of interest exists between:

- what improves platform engagement, retention, data capture, or workflow continuity
- and what improves user clarity, autonomy, or outcome closure

Examples that SHOULD be disclosed include:

- hidden logging that persists beyond user expectation
- hidden signal inference that changes behavior without user visibility
- hidden memory or preference carry-forward
- hidden pressure toward continued interaction when no evidential outcome has been reached
- hidden routing from primary assistant behavior into monetization, retention, or additional capture surfaces

## 2. Precision control requirements

### 2.1 Logging controls

Users MUST be able to:

- view what categories of data are being logged
- wipe stored user-facing session data clean
- turn logging off entirely when policy permits
- adjust logging with precision rather than only through a single coarse toggle

Precision controls SHOULD distinguish at least:

- transcript logging
- voice transcript retention
- telemetry / analytics
- preference memory
- behavioral or style adaptation state
- UI-generation or artifact-inspection traces

### 2.2 Behavioral and communication settings

The system SHOULD expose user-facing controls for:

- communication style
- verbosity or compression preference
- behavioral adaptation posture
- visible guardrail posture when configurable
- memory preference
- inference-sensitive features that affect tone, pacing, or pushback behavior

The user should not be forced to accept an invisible behavioral-management layer as a condition of using the system.

## 3. Inspectable signal use

### 3.1 Signal transparency

If the system infers signals about the user, those signal families SHOULD be inspectable.

Inspectable means the user can see at least:

- which signal family is in use
- what it is allowed to affect
- whether it is currently enabled
- how to disable, limit, or clear it when policy permits

Signal families that SHOULD be surfaced when present include:

- confusion or overload inference
- distress or pain-pattern inference
- behavioral-style adaptation
- trust or skepticism adaptation
- complexity or compression preference
- urgency or escalation handling

### 3.2 Guardrail transparency

The system SHOULD disclose guardrails that materially alter behavior, including:

- refusal or safety posture
- approval boundaries
- logging or monitoring posture
- routing or review gates
- browser-proof or artifact-check requirements

Users should be able to tell whether a limit comes from:

- the model layer
- the product layer
- policy logic
- execution tooling
- or review-gate enforcement

## 4. Loop-exit requirements

### 4.1 Loop-exit doctrine

An AI-first system MUST include a user-comprehensible path to exit the progress loop.

Loop exit requires more than a satisfying conversation. It requires a visible route from:

- declared intent
- to next real step
- to rendered or real-world evidence
- to closure or explicit stop

### 4.2 Victory-lap boundary

Conversation quality, emotional comfort, or polished summaries do not count as completion by themselves.

Loop closure SHOULD require:

- a declared outcome
- an evidential check against that outcome
- a visible state transition showing whether the loop is closed, blocked, or still unresolved

### 4.3 Exit options

The system SHOULD offer explicit loop-exit options such as:

- stop and clear state
- export current state and evidence
- hand off to human review
- reset intent and begin again
- freeze the current packet for external inspection

## 5. Discovery-first planning rule

### 5.1 Discovery before UI

For AI-first and especially voice-first systems, planning MUST NOT begin with dashboards, dropdown menus, or broad UI composition as the primary architecture move.

The sequence SHOULD be:

1. discovery
2. architecture cartography
3. capability extraction
4. schema / route / storage mapping
5. governance breach audit
6. intent and loop-closure design
7. only then shell and UI composition

Starting with menus and dashboards instead of intent is treated by this standard as a high-risk planning error.

### 5.2 Multi-agent discovery lane

When current-system structure matters, the planning lane SHOULD run multi-agent discovery using specialized passes such as:

- cartography
- capability extraction
- schema review
- route review
- storage / state review
- governance breach audit
- rendered-surface inspection
- artifact integrity checks

This aligns with `AIOS-DISCOVER-AGENT-PROCESS-001` and `AIOS-PRE-ARCHITECTURE-DISCOVERY-AGENT-001`.

## 6. Voice-first rendered-truth rule

### 6.1 No blind trust in summaries

For voice-first AI systems, reviewers MUST NOT rely only on coding-agent summaries, planner summaries, or generated status reports to determine whether the system works.

Rendered truth is required.

### 6.2 Browser viewer requirement

If the system uses Voice AI and generates or revises UI components on the fly, the workflow SHOULD include a governed browser viewer such as Playwright or equivalent browser inspection tooling after each meaningful session.

The purpose is to verify:

- the actual rendered output
- the visible shell state
- the disclosure surfaces
- the interaction behavior
- the component integrity
- the absence of summary-report substitution

### 6.3 Artifact checks

Voice-first lanes that generate or revise UI SHOULD also produce reviewable artifact checks covering:

- rendered surface proof
- current route or shell region
- disclosure-bar state
- active logging / memory / guardrail toggles
- component presence or absence
- packet linkage to the review slug or session artifact bundle

This requirement reinforces `AMD-2026-008-ADD-004` and the browser-review knowledge capture.

## 7. UI sequencing rule for voice-first systems

### 7.1 Anti-dashboard-first rule

Voice-first systems SHOULD NOT be architected as dashboard-first systems with voice added later.

The governing posture is:

- intent first
- shell authority first
- disclosure first
- rendered proof first
- UI support surfaces after the control plane is clear

### 7.2 Menu and dropdown caution

Menus and dropdowns MAY exist as fallback or secondary shell affordances.

They SHOULD NOT act as the primary substitute for:

- intent declaration
- state disclosure
- loop closure
- or execution accountability

If a design is relying on menus because the intent model is not ready, the correct action is usually to fix the intent model and disclosure model first rather than expanding UI chrome.

## 8. Review and conformance

A lane conforms to this standard only if a reviewer can inspect:

- what user data categories are being logged
- what the user can view, clear, or disable
- what behavioral and guardrail settings are exposed
- how loop exit is implemented
- whether discovery preceded UI planning
- whether voice-first output was browser-inspected after meaningful sessions
- whether rendered UI proof exists instead of summary-only approval

## Final principle

Power should remain with the user through inspectable disclosure, precise control, and evidence-based loop exit, not with hidden platform layers that silently manage the many for the benefit of the few.
