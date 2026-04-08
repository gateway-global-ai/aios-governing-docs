# Architect plan — AMD-2026-006 / AIOS-SPEC-007 (draft)

**Date:** YYYY-MM-DD  
**Evidence used:** `product_context_bundle.md` (date); `CURRENT_SYSTEM_RESEARCH_*.md` (date)  
**Verifier:** _name / role_

---

## 1. Executive summary

_3–6 sentences: governed routing stack, MCP boundary, what is in scope for this ratification._

---

## 2. Current system grounding (file-cited)

| Topic | Repo path(s) | Notes |
|-------|--------------|--------|
| Phase 1 intents | `src/workspace/intentRegistry.ts` | |
| Intent → scope class | `src/workspace/scopeClasses.ts` | |
| Intent → MCP tool | `src/workspace/mcpIntentToolMap.ts` | |
| ICP entry | `src/workspace/integrationControlPlane.ts` | `runWorkspaceControlPlane` |
| Canvas views | `src/shellCanvas/canvasTypes.ts`, `workspaceIntentRouter.ts` | |
| HTTP host | `server/prodHost.ts` | |

---

## 3. Schemas (normative targets for SPEC / annex)

_JSON Schema fragments or tables for: routing envelope, audit fields, optional config — align with **AIOS-SPEC-009** / **AIOS-SPEC-010** where referenced._

---

## 4. Routes (intent → surface → control plane)

_Table: `workspace.*` intent → canvas view → scope class → policy check → MCP tool name._

---

## 5. Storage / session / tokens

_Where OAuth tokens live (memory vs server), MCP session headers, env vars — **no secrets** in client bundles for production claims._

---

## 6. Gaps vs governing text

| Gap | AMD/SPEC § | Proposed resolution |
|-----|------------|---------------------|
| | | |

---

## 7. Verification checklist

- [ ] Every **SHALL** in **AIOS-SPEC-007** §2–3 maps to a **file** or **explicit deferral**.
- [ ] No **invented** path — all **src/** references verified in repo.
- [ ] **Diff** reviewed against **`main`** (or stated branch).
