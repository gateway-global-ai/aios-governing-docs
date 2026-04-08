# UI plan — AMD-2026-006 / Workspace surfaces (draft)

**Date:** 2026-04-08  
**Builds on:** [`ARCHITECT_PLAN.md`](ARCHITECT_PLAN.md) (Phase B **verified** 2026-04-08)  
**Verifier:** _pending human review_

---

## 1. Executive summary

Users experience **Google Workspace** through a **single overlay stack** in **`ai-os-voice-interface`**: **`App.tsx`** mounts **`WorkspaceOnboardingSurface`** or **`WorkspaceHubSurface`** depending on **`WorkspaceCanvasState.view`** (`src/shellCanvas/canvasTypes.ts` — `CanvasView` / `ALL_CANVAS_VIEWS`). **`WorkspaceHubSurface`** (`src/overlays/WorkspaceHubSurface.tsx`) implements **six** interaction modes (`hub`, `calendar`, `mail`, `drive`, `contacts`, `search`) behind one component; **MCP** calls are **not** made from the component — data flows through **`loadWorkspacePayload.ts`** → **`runWorkspaceControlPlane`** (`src/workspace/integrationControlPlane.ts`). **Primary-strip disclosure** for Workspace aligns with **AIOS-SPEC-009** presentation rules via **`buildPrimarySecondaryDisclosureLine`** (`src/compliance/spec009PrimaryDisclosure.ts`) and **`workspacePrimaryLine`** (`src/shell/shellSurfaceLabels.ts`); **resolved workspace intent** for policy/disclosure is derived in **`deriveWorkspaceIntentForDisclosure`** (`src/shellCanvas/deriveWorkspaceIntentForDisclosure.ts`). **Shell authority** (**AMD-2026-007** / **AIOS-SPEC-006**): shell navigation from agent output is centralized in **`shellIntentRouter.ts`** (`app.open.workspace`, `app.shell.*`); **Layer 2** `workspace.*` execution remains on the **Workspace** canvas + ICP path described in **`ARCHITECT_PLAN.md`**.

---

## 2. Surfaces inventory

| Canvas / view id | User-facing purpose | Primary entry intent(s) | Component / file |
|------------------|----------------------|-------------------------|------------------|
| `workspace_onboarding` | Connect Google (GIS OAuth) or continue without | Typically reached before hub when not connected; hub flow uses `workspace.hub` | `WorkspaceOnboardingSurface` — `src/overlays/WorkspaceOnboardingSurface.tsx`; mount in `App.tsx` when `workspaceCanvas.view === 'workspace_onboarding'` |
| `workspace_hub` | Launcher: tiles to Calendar, Mail, Drive, Contacts, Web search; sign-in bar | `workspace.hub`; **also** fallback routing for Phase 1 intents **without** a dedicated hub (e.g. `workspace.calendar.events.list`, `workspace.docs.*`) per `workspaceIntentToCanvasView` — `src/workspace/workspaceIntentRouter.ts` | `WorkspaceHubSurface` `mode="hub"` — `src/overlays/WorkspaceHubSurface.tsx` |
| `workspace_calendar_hub` | Calendar list / read-only calendar UX | `workspace.calendar.list`, `workspace.calendar.get` | `WorkspaceHubSurface` `mode="calendar"`; payload `WorkspaceCalendarHubPayload` — `src/shellCanvas/loadWorkspacePayload.ts` |
| `workspace_mail_hub` | Mail search, open message, thread actions | `workspace.mail.search`, `workspace.mail.read`, thread intents, `workspace.mail.draft_reply`, etc. | `WorkspaceHubSurface` `mode="mail"` |
| `workspace_drive_hub` | Drive list / search / read | `workspace.drive.list`, `workspace.drive.search`, `workspace.drive.read` | `WorkspaceHubSurface` `mode="drive"` |
| `workspace_contacts_hub` | Contacts (People) read | `workspace.contacts.list`, `workspace.contacts.search` | `WorkspaceHubSurface` `mode="contacts"`; `ContactsReadPanel` — `src/components/workspace/ContactsReadPanel.tsx` |
| `workspace_search_hub` | Programmable / web search surface | `workspace.web.search` | `WorkspaceHubSurface` `mode="search"` |

**Cross-reference:** `shellSurfaceLabels.ts` maps `workspace_calendar_hub` / `workspace_mail_hub` (and related) to user-visible short labels for the shell strip.

---

## 3. Disclosure & readiness

- **Primary + secondary lines:** **`buildPrimarySecondaryDisclosureLine`** (`src/compliance/spec009PrimaryDisclosure.ts`) composes **Workspace connection** copy (`workspacePrimaryLine` / `workspaceState`) with optional **voice** and **local model** capability lines — consistent with **SPEC-009** §12.2 *presentation* (predicates in `src/core/compliance/spec009DisclosurePredicates.ts` per file header in `spec009PrimaryDisclosure.ts`).
- **Resolved intent for Workspace:** **`deriveWorkspaceIntentForDisclosure`** maps canvas + payload to a **single** representative `workspace.*` id for dedicated hubs; for **`workspace_hub`** and **`workspace_onboarding`** it returns **`null`** (no resolved id), so disclosure stays at **connection / shell** level unless a dedicated hub is active. **Documented gap** in **`deriveWorkspaceIntentForDisclosure.ts`** (comment): **`workspace.mail.thread.summarize`** is not fully represented from payload alone — affects **local-model** disclosure edge cases until lifted.
- **Sign-in vs connected:** **`GoogleWorkspaceSignInBar`** (`src/components/workspace/GoogleWorkspaceSignInBar.tsx`) implements GIS OAuth; hub **`connected`** prop gates tiles vs sign-in prompt (`App.tsx` + `shouldShowWorkspaceHub` / `workspaceState` — `src/shell/workspaceState.ts`). **No contradictory “connected” copy** should appear when **`workspaceState`** indicates auth required — align committee/spec review with **AMD-2026-012** family where **session truth** matters.

---

## 4. Shell vs Workspace boundary

| Concern | Owner | Code |
|--------|--------|------|
| **Agent / app intents** that open Workspace or switch shell modes | **Shell** | **`shellIntentRouter.ts`** — `app.open.workspace` (target `workspace.hub` or empty → `open_workspace`), `app.shell.*` surface / voice / developer / operator |
| **Layer 2 `workspace.*` shape, canvas view, scope class** | **Workspace** | **`workspaceIntentRouter.ts`** — `workspaceIntentToCanvasView`, `routeWorkspaceIntent`; **`scopeClasses.ts`** |
| **Async data + ICP** | **Workspace** | **`loadWorkspacePayload.ts`**, **`integrationControlPlane.ts`** |
| **Voice/chat routing** to open canvas | **App** | **`App.tsx`** + **`WorkspaceCanvasContext`** (`src/shellCanvas/WorkspaceCanvasContext.tsx`) |

**Voice/chat:** User-facing routing of natural language to **`workspace.*`** remains whatever the app’s intent pipeline resolves; this UI plan does not invent new routes — it documents **where** surfaces render once **`WorkspaceCanvasState`** is set.

---

## 5. Gaps / open UX risks

| Risk | Mitigation in spec or code |
|------|----------------------------|
| **Fallback to `workspace_hub`** for `workspace.calendar.events.list` and **`workspace.docs.*`** (see **`ARCHITECT_PLAN.md` §4**) | **Product decision:** Treat as **MVP aggregation** — user lands on **hub** with tiles; **ICP** may still run the intent. **Spec/UI follow-up:** If **AIOS-SPEC-006** surface registry requires **one canvas per Phase 1 intent**, add **`workspace_docs_hub`** (or extend calendar routing) + `workspaceIntentToCanvasView` branches + `CanvasView` union — **committee + author revision**, not this draft alone. |
| **`deriveWorkspaceIntentForDisclosure`** **`null`** on **`workspace_hub`** | Disclosure cannot name a single **resolved** `workspace.*` on the launcher; acceptable if **primary line** carries **Workspace connection** state; **revisit** if peer review demands intent-specific copy on hub. |
| **Thread summarize** not reflected in disclosure derivation | See comment in **`deriveWorkspaceIntentForDisclosure.ts`** — future: thread intent through payload or active-intent state. |
| **Single component** (`WorkspaceHubSurface`) for all hubs | Reduces duplication; **risk** of mode-specific regressions — mitigate with existing tests (`*.test.ts` near workspace/shell) and visual checks before Round 2. |

---

## 6. Verification checklist

- [ ] Surface IDs match **`src/shellCanvas/canvasTypes.ts`** — `CanvasView` / `ALL_CANVAS_VIEWS`.
- [ ] No **dashboard-first** regression vs **AMD-2026-007** / shell authority: **Shell** strip + **`shellIntentRouter`** remain the **app shell** authority; Workspace is **overlay** + **ICP**, not a separate “home app.”
- [ ] **`App.tsx`** branch per `workspaceCanvas.view` matches the table in **§2** (including **`WorkspaceHubSurface`** `mode` prop).
- [ ] Disclosure files (**`spec009PrimaryDisclosure.ts`**, **`deriveWorkspaceIntentForDisclosure.ts`**, **`shellSurfaceLabels.ts`**) reviewed if **SPEC-009** / **AMD-2026-012** alignment is questioned in committee.

---

*Draft — pending human verification against `ai-os-voice-interface` before Phase D (committee packet).*
