---
document_id: AIOS-ADR-001
version: 1.1.0
status: proposed
category: reference
title: 'ADR-001: Core shell/kernel/control-plane vs AI OS interface boundaries'
author: Gateway Global AIOS
created: 2026-04-07
last_updated: 2026-04-07
cross_references:
  - doc_id: AIOS-MASTER-IMPL-001
  - doc_id: AMD-2026-012
  - doc_id: AIOS-SPEC-009
amendment_history:
  - version: 1.1.0
    date: 2026-04-07
    summary: Correction — status proposed pending council review; prior accepted status rescinded.
  - version: 1.0.0
    date: 2026-04-07
    summary: Initial ADR text (prematurely marked accepted — superseded by v1.1.0).
---

# ADR-001: Core shell / kernel / control-plane vs AI OS interface boundaries

## Status

**Proposed** — **pending council review**. When **accepted**, this ADR **closes MBL-001** for the **governing / architectural record** (module ownership and import rules). **Code enforcement** (packages, ESLint boundaries, CI) remains **downstream** in `ai-os-voice-interface` and any future **core** repository — tracked under **MBL-002+**. **Not** amendment ratification — **council** (or delegated body) **acceptance** of this ADR is the gate.

---

## Context

Ratified law (**AMD-2026-012**, **AIOS-SPEC-009**, **AIOS-SPEC-002**) requires **session authority**, **§7 outcome family**, **PolicyRecord-aligned readiness**, and **integration control plane** semantics to be **runtime truth** consumable by **any** interface — not defined ad hoc in a single React app.

**Current evidence:** Shell and control-plane logic is **embedded** in `ai-os-voice-interface` under paths such as `src/shell/`, `src/workspace/integrationControlPlane.ts`, `src/intent/`, and `src/compliance/`. That creates **center-of-gravity** risk: every repo tries to own shell law because the code is **near** the UI.

---

## Decision

### Core shell / kernel / control-plane (law → contracts → policy gates)

**Owns:**

- Session surface mode, interim elevation, bootstrap precedence (**shell authority** semantics).
- **Session entry classification** model (**new** / **returning**) — type contract; **storage** is an adapter.
- **Shell primary outcome** taxonomy (**AMD-2026-012 §7**) and deterministic mapping hooks to SessionContext / PolicyRecord fields.
- **Disclosure predicates** (SPEC-009 §12.2-style): when primary disclosure is *required* from readiness inputs — **not** the React component strings.
- **Workspace integration control plane** entry: intent → scope → policy → `callWorkspaceMcpAdapter` (no MCP bypass).

**Does not own:** JSX, CSS, layout, voice orb animation, marketing copy, tenant branding.

### AI OS interface layer (`ai-os-voice-interface`)

**Owns:**

- Rendering **ShellIdentityBar**, **CommandRail**, idle panels, Workspace surfaces **after** routing.
- Binding **core** outputs (predicates, outcome, session classification) to **props** and **local presentation state**.
- Browser-specific adapters (e.g. `localStorage` for entry classification) **implementing** core ports.

**Does not own:** Defining §7 outcomes, ICP routing rules, or PolicyRecord semantics **without** importing from **core** contracts.

### Tool plane (`google-workspace-mcp` and peers)

**Owns:** MCP tools, OAuth transport, server-side scope behavior aligned with **SPEC-007**.

**Does not own:** Shell entry, fallback authority, or primary outcome selection.

---

## Import / ownership rules (normative for implementation)

1. **Core modules** (whether extracted to `packages/*` or a future repo) **must not** import from **React** or **UI** layers.
2. **Interface** **may** import **core**; **must not** duplicate outcome taxonomy or ICP routing **in components**.
3. **New shell semantics** default to **core** first; **interface** only adds **pilot** code if labeled and tracked toward **MBL-002–MBL-004**.

---

## Consequences

- **MBL-006** (e.g. `resolvedIntentRequiresLocalModel` wiring) is **valid** only when **execution policy** is produced by **core** (or shared policy layer), **not** inferred in `App.tsx`.
- **BL-004**-style work remains **child** and **must not** return as **mainline** until **MBL-004** is **done** in core.
- Extraction of a **standalone core package** is **allowed but not required** by this ADR; the **boundary rules** apply **even when code still lives in the interface repo** (e.g. `src/core/` or equivalent namespace with enforced imports).

---

## Compliance evidence (next implementation steps)

| Step | Evidence |
|------|----------|
| Namespace or `packages/aios-shell-core` (optional) | Repo layout PR + CI import rule |
| Move predicate **pure functions** next to core | Unit tests in core-only path |
| Interface imports only from `@aios/shell-core` (or `src/core/`) for law | Lint rule |

---

*End of ADR-001 v1.1.0.*
