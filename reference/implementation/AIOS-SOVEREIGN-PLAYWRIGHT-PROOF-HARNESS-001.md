---
document_id: AIOS-SOVEREIGN-PLAYWRIGHT-PROOF-HARNESS-001
version: 0.1.0
status: draft
category: reference_implementation
title: Sovereign Playwright proof harness
author: Gateway Global AIOS
created: 2026-04-17
last_updated: 2026-04-17
cross_references:
  - doc_id: AMD-2026-008-ADD-004
    title: Pre-Human Browser Review and Visual Proof Gate
  - doc_id: AMD-2026-008-ADD-005
    title: Voice-First Rendered Session Proof and Artifact Checks
  - doc_id: AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001
    title: AI OS Shell UI Layout and Component Standard
  - doc_id: AIOS-VOICE-FIRST-UI-ARTIFACT-KIT-STANDARD-001
    title: Voice-first UI artifact kit standard
  - doc_id: AIOS-SPEC-006
    title: UI Component Registry Standard
note: Draft implementation record for the governance-owned Playwright harness that produces browser-visible proof artifacts from this repo without making a downstream product repo the silent authority.
---

# Sovereign Playwright proof harness

## Purpose

This document defines the first governance-owned Playwright harness inside `aios-governing-docs`.

The harness exists because rendered proof is now part of governance law. If the governing system cannot produce browser-visible evidence on its own, then browser proof depends on a downstream runtime repo and sovereignty collapses into implementation convenience.

## Governing principle

The governing system SHALL own a browser-proof harness capable of:

- producing visual proof artifacts from a governance-controlled fixture by default,
- targeting a downstream runtime when a policy-approved base URL is supplied,
- storing golden visual baselines and run outputs under governed paths,
- exercising protected shell-chrome contracts for header, footer, and menu placement.

## First implementation scope

The first harness release includes:

- `playwright.config.ts`
- `tests/playwright/shell-authority.spec.ts`
- `tests/playwright/fixtures/index.html`

The default fixture is a sovereign shell-authority surface that proves:

- fixed protected header
- fixed protected footer
- header-attached system menu
- footer-secondary user menu

## Target model

### Default target

When no external target is declared, the harness SHALL run against the governance-owned fixture served from:

- `tests/playwright/fixtures/`

This preserves sovereign capability even if downstream product repos are unavailable.

### External target

When `AIOS_PLAYWRIGHT_BASE_URL` is supplied, the harness MAY target an external runtime such as a downstream AI OS implementation.

That external target SHALL be treated as a proof target, not as the authority that defines the test law.

## Artifact paths

The first harness release uses the following paths:

| Path | Purpose |
|------|---------|
| `artifacts/browser_review/golden/` | Golden master screenshots committed as governed visual baselines. |
| `artifacts/browser_review/results/` | Per-run Playwright output such as traces, failure screenshots, and videos. |
| `artifacts/browser_review/report/` | Human-readable Playwright HTML report output. |

Generated run output MAY be ignored in Git, but golden baselines are part of the governed evidence surface and SHOULD remain reviewable.

## Commands

| Command | Purpose |
|---------|---------|
| `npm run playwright:test` | Run the governance-owned Playwright suite. |
| `npm run playwright:update-snapshots` | Refresh governed golden baselines after an intentional law-aligned UI change. |
| `npm run playwright:report` | Open the last generated HTML report. |

## Relation to browser-proof doctrine

This harness does not replace `REVIEW_TARGET.yaml`, `SESSION_PROOF.yaml`, or any review packet.

Instead:

- `AMD-2026-008-ADD-004` remains the pre-human approval gate,
- `AMD-2026-008-ADD-005` remains the higher-frequency rendered-session-proof doctrine where applicable,
- the Playwright harness is one approved mechanism for generating the browser-visible proof those documents require.

## First conformance expectation

At minimum, the harness SHALL fail if:

- the protected header is no longer fixed,
- the protected footer is no longer fixed,
- the system menu no longer attaches to the header,
- the user menu no longer remains a secondary footer surface,
- the rendered proof drifts from the approved golden baseline without intentional snapshot renewal.

## Final principle

If AI OS governance is sovereign, then browser proof cannot remain a ghost dependency. The governing system itself must own the mechanism that produces visual proof of its shell law.
