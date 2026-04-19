---
document_id: AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001
version: 0.4.0
status: draft
category: reference
title: AI OS Shell UI Layout and Component Standard
author: Gateway Global AIOS
created: 2026-04-16
last_updated: 2026-04-19
cross_references:
  - doc_id: AIOS-SPEC-006
    title: UI Component Registry Standard
  - doc_id: AMD-2026-007
    title: Intent Primitive, Shell Affordances, Session Disclosure, Workspace Domain Pack
  - doc_id: AMD-2026-008-ADD-004
    title: Pre-Human Browser Review and Visual Proof Gate
  - doc_id: AMD-2026-012
    title: Shell Authority and Voice-First Entry
  - doc_id: AMD-2026-016
    title: Governed Non-Human Principals and Deterministic Routed Authority
  - doc_id: ADR-001-core-shell-vs-interface-boundaries
    title: Core Shell vs Interface Boundaries (proposed)
  - doc_id: AIOS-VOICE-FIRST-UI-ARTIFACT-KIT-STANDARD-001
    title: Voice-first UI artifact kit standard
---

# AI OS Shell UI Layout and Component Standard

`AIOS-SHELL-UI-LAYOUT-AND-COMPONENT-STANDARD-001` — Draft v0.4.0

---

## 1. Purpose

This document establishes the canonical UI layout and component standards for the AI OS voice shell runtime interface (`ai-os-voice-interface`). It provides governed authority for the design token system, layout structure, overlay positioning rules, and component styling contract. It exists to prevent UI drift across sessions and agents by codifying the system as a formal standard rather than an implicit convention.

---

## 2. Scope

This standard applies to all React components under `src/` in the `ai-os-voice-interface` repository, including but not limited to: shell chrome components (`ShellIdentityBar`, `ShellSystemControls`, `CommandRail`), onboarding screens, overlay panels, and any new components added to the shell.

It does not govern the governing documentation repo (`aios-governing-docs`) or CLI tooling.

This standard now also governs the disclosure/player bar model used for shell audio visibility, the first-run onboarding stability rule tied to narrated intro slides, and the deterministic menu placement contract for protected shell chrome.

---

## 3. Design Token System

### 3.1 CSS Custom Property Vocabulary

The shell uses a `--panel-*` CSS custom property family defined in `src/index.css` and dynamically stamped by `useShellTheme() → themeToCssVars()` onto the root container element. All components MUST inherit from these tokens. No component may hardcode theme values.

| Token | Role | Default value (dark theme) |
|-------|------|---------------------------|
| `--panel-bg` | Panel/card primary background | `rgba(255,255,255,0.07)` |
| `--panel-surface` | Secondary surface (nested cards) | `rgba(255,255,255,0.05)` |
| `--panel-bg-hover` | Interactive hover background | `rgba(255,255,255,0.12)` |
| `--panel-border` | Standard border | `rgba(255,255,255,0.15)` |
| `--panel-input-bg` | Form input background | `rgba(255,255,255,0.08)` |
| `--panel-input-border` | Form input border | `rgba(255,255,255,0.18)` |
| `--panel-text` | Primary body text | `rgba(255,255,255,0.92)` |
| `--panel-text-muted` | Secondary / muted text | `rgba(255,255,255,0.45)` |
| `--panel-heading` | Heading text | `rgba(255,255,255,1.0)` |
| `--panel-accent-bg` | Accent/active background | `rgba(16,185,129,0.15)` |
| `--panel-accent-border` | Accent/active border | `rgba(52,211,153,0.4)` |
| `--panel-accent-text` | Accent/active text | `rgba(167,243,208,1.0)` |

### 3.2 Prohibited Styling Patterns

The following Tailwind CSS utility patterns are **prohibited** in all shell components. They hardcode dark-theme assumptions and fail when the theme changes:

- `bg-white/[0.xx]` — any opacity-white background utility
- `border-white/10`, `border-white/15`, `border-white/20` — hardcoded white border
- `bg-slate-950`, `bg-slate-900`, `bg-zinc-950` — hardcoded dark backgrounds
- `text-zinc-400`, `text-zinc-500`, `text-zinc-600` — hardcoded muted text colors

### 3.3 Required Implementation Pattern

```tsx
// CORRECT — CSS custom properties via style attribute
<div style={{
  background: 'var(--panel-bg)',
  border: '1px solid var(--panel-border)',
}}>
  <h2 style={{ color: 'var(--panel-heading)' }}>Title</h2>
  <p style={{ color: 'var(--panel-text)' }}>Body</p>
  <span style={{ color: 'var(--panel-text-muted)' }}>Secondary</span>
</div>
```

---

## 4. Layout Structure

### 4.1 Layout Tokens

The shell layout is driven by two CSS custom properties that MUST be used for all spacing calculations:

| Token | Value | Purpose |
|-------|-------|---------|
| `--shell-header-height` | `2.75rem` | Fixed header bar height |
| `--shell-footer-height` | `6rem` | Fixed footer (CommandRail) height |

### 4.2 Content Zone Padding

The main content area MUST account for both fixed chrome bars:

```css
padding-top: calc(var(--shell-header-height) + 2.5rem);
padding-bottom: calc(var(--shell-footer-height) + 1.25rem);
```

Overlay scroll containers (DISC Profile, Voice Settings, etc.) MUST add `padding-bottom: var(--shell-footer-height)` to their scrollable inner div to prevent content being hidden behind the footer.

### 4.3 Z-Index Layer Map

All shell layers use named CSS custom properties. Raw z-index integers are prohibited:

| Token | Value | Layer |
|-------|-------|-------|
| `--z-shell-base` | `0` | Base layer |
| `--z-shell-main` | `10` | Main content |
| `--z-shell-chrome` | `40` | Chrome overlays |
| `--z-shell-workspace-canvas` | `60` | Workspace canvas |
| `--z-shell-modal-backdrop` | `65` | Modal backdrops |
| `--z-shell-header` | `70` | Fixed header |
| `--z-shell-footer` | `70` | Fixed footer |
| `--z-shell-system-controls` | `75` | System controls panel |

### 4.4 Disclosure / player bar

`ShellIdentityBar` is the shell disclosure surface and the operator-facing audio authority. It MUST:

- avoid centered disclosure bubbles or other redundant mid-header status plates when the same state can be conveyed through the bounded player cluster or menu surfaces,
- keep model disclosure compact and subordinate to shell chrome rather than turning it into a second menu trigger,
- surface play or stop, mic enabled, speaker enabled, cue-menu access, and the governed header system-menu trigger in the same bounded player cluster, and
- reserve the right-side `LayoutGrid` trigger as the sole primary entry point into the header system shell menu.

`HeaderCueDrawer` is a bounded cue-state surface. It MUST:

- remain attached to `ShellIdentityBar`,
- expose only current cue, queued cues, playback state, and closely related shell-audio status,
- SHALL NOT duplicate voice-route switching or deeper settings actions that belong to `VoiceControlPanel` or the governed header menu, and
- keep queued speech inspectable without turning the drawer into a second navigation surface.

`ShellSystemControls` is the top-right system handoff surface for deeper shell controls. When the governed voice runtime is present, it MUST:

- expose a current voice-runtime summary card while the system-controls panel is open,
- show the active voice route and live shell-owned status rather than a detached settings-only entry point,
- avoid competing with the header system shell menu for primary navigation ownership,
- limit itself to account, summary, and bounded handoff duties unless later law explicitly expands that scope,
- route deeper changes into `VoiceControlPanel.tsx` or other shell-root overlays through prop callbacks, and
- remain subordinate to the shell cue controller in `App.tsx` for playback, queue, and mute authority.

### 4.5 Onboarding stability

First-run onboarding surfaces MAY be narrated, but narration MUST NOT cause the onboarding center-stage surface to disappear. Generic shell `speaking` state is not sufficient authority to blank the first-run orientation surface while intro narration is active.

### 4.6 Multi-step card navigation

Any multi-step card or slide sequence rendered in the shell MUST expose basic navigation visibly rather than relying only on narration, stateful memory, or agent guidance.

Minimum requirements:

- top-right progress label in the form `X of Y`
- back button
- close button

These controls are required for multi-step overlays, cards, and guided-shell sequences unless a later ratified accessibility or safety exception explicitly narrows the rule.

### 4.7 Deterministic shell menu contract

The shell SHALL use one governed menu model for protected shell chrome.

Protected shell chrome means the header and footer surfaces that establish shell identity, disclosure, routing, user control, and exit posture. Those surfaces SHALL remain shell-owned composition zones even when agents, tools, or downstream apps propose content.

#### Header

The header SHALL be the primary system-shell menu surface.

Header menus SHALL:

- render as header-attached overlays anchored to the bottom edge of `ShellIdentityBar`,
- use governed menu records rather than ad hoc JSX placement,
- declare template family, level count, content source type, and permission class,
- remain shell-owned even when the content is proposed by a non-human principal through governed data,
- use the right-side header `LayoutGrid` control as the only primary menu trigger, and
- route shell destinations into voice-first Level 1 / Level 2 intent surfaces rather than dropping directly into feature-dense destination pages.

#### Footer

The footer SHALL remain a secondary user/PTT surface.

Footer menus SHALL:

- remain subordinate to the command rail and PTT or chat primary action,
- be limited to user-related or session-related controls,
- SHALL NOT become a general dumping ground for system-shell navigation or arbitrary agent actions.

#### Protected-shell mutation boundary

Agents and other non-human principals MAY request menu content, menu state, template selection, or style-guide-linked content settings only through governed records and documented shell-owned render paths.

Agents and other non-human principals SHALL NOT directly mutate:

- header structure,
- footer structure,
- shell-chrome placement,
- control ownership for protected shell chrome.

#### Ad hoc placement prohibition

System-shell menus SHALL NOT be mounted in arbitrary canvas locations, floating one-off drawers, or unrelated overlays when the menu belongs to protected shell chrome.

Where a view needs a view-local menu, that menu SHALL be registered as view-owned under `AIOS-SPEC-006` and SHALL NOT masquerade as header or footer chrome.

---

## 5. Overlay Positioning Law

### 5.1 Stacking Context Trap

`position: fixed` inside a CSS-transformed ancestor is positioned relative to that ancestor, NOT the viewport. Framer Motion's `motion.div` with active animations applies CSS `transform`, creating a new stacking context. Any `fixed inset-0` child rendered within such an ancestor will be clipped to the ancestor's bounds, not the full viewport.

**All full-viewport overlays MUST be rendered from the application root level** (`App.tsx` or `main.tsx`), never from within `ShellSystemControls`, `ShellIdentityBar`, `CommandRail`, or any animated (`motion.*`) component.

Components that need to trigger overlays MUST use prop callbacks, not local state mounting:

```tsx
// CORRECT: component fires a callback
<ShellSystemControls onOpenVoiceSettings={() => setMode('voice_control')} />

// WRONG: component mounts its own full-viewport overlay
function ShellSystemControls() {
  const [show, setShow] = useState(false);
  return <>{show && <FullScreenOverlay />}</>;
}
```

### 5.2 Overlay Positioning Pattern

All centered OS overlays use the full-backdrop + centered-card pattern:

```tsx
// Backdrop
<div className="fixed inset-0 z-[var(--z-shell-modal-backdrop)] bg-black/55 backdrop-blur-[2px]"
     onClick={onClose} />
// Centered card
<div className="fixed inset-0 z-[var(--z-shell-system-controls)] flex items-center justify-center pointer-events-none">
  <div className="pointer-events-auto w-full max-w-2xl mx-4" onClick={e => e.stopPropagation()}>
    {/* content */}
  </div>
</div>
```

Dropdown positioning from header corners is prohibited for general navigation or system panels. The bounded exceptions are:

- a governed cue drawer attached to `ShellIdentityBar` that exists only to expose current and queued shell audio plus cue-state disclosure,
- a governed header-attached menu overlay that satisfies §4.7 and remains shell-owned.

### 5.3 Top-aligned menu overlays

When shell-menu-driven destination surfaces remain overlay-based, they SHALL preserve header clearance and visible shell ownership.

Minimum requirements:

- the overlay launch path SHALL originate from the governed header menu or another explicitly governed shell route,
- overlays launched from those menu routes SHALL align to the top rather than centering by default,
- top-aligned overlays SHALL preserve `padding-top` that clears `--shell-header-height`, and
- destination surfaces such as Voice Control, Voice Box, Appearance, and System Configuration SHALL expose a Level 1 intent menu plus a focused Level 2 pane instead of a flat long-form control dump.

---

## 6. Conformance

Agents and developers making changes to shell UI components SHALL:

1. Read this document before writing or modifying any component
2. Use only `--panel-*` tokens for theming — never hardcode colors
3. Render full-viewport overlays exclusively from `App.tsx` root level
4. Use layout tokens (`--shell-header-height`, `--shell-footer-height`) for all spacing
5. Route protected shell menus through governed menu records rather than ad hoc menu placement
6. Keep the header as the primary system-shell menu zone and the footer as a secondary user/PTT zone
7. Keep cue drawers cue-only and prevent them from becoming secondary settings menus
8. Use top-aligned overlay posture for shell-menu-driven destination surfaces that remain overlay-based
9. Reference `AIOS-SPEC-006` for component registration requirements

Violations of §3.2 (prohibited styling patterns), §4.7 (deterministic shell menu contract), or §5.1 (stacking context trap) constitute UI governance failures and MUST be remediated before any related build is approved per AMD-2026-008-ADD-004.

---

*Document status: draft. Enters peer review → ratification pipeline per AMD-2026-005.*
