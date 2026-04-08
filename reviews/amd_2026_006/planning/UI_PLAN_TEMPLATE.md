# UI plan — AMD-2026-006 / Workspace surfaces (draft)

**Date:** YYYY-MM-DD  
**Builds on:** [`ARCHITECT_PLAN.md`](ARCHITECT_PLAN.md) (same packet)  
**Verifier:** _name / role_

---

## 1. Executive summary

_How users see Workspace: hubs, onboarding, errors, disclosure — Shell authority per **AMD-2026-007** / **AIOS-SPEC-006** registration intent._

---

## 2. Surfaces inventory

| Canvas / view id | User-facing purpose | Primary entry intent | Component / file |
|------------------|---------------------|----------------------|------------------|
| | | | |

---

## 3. Disclosure & readiness

_Alignment with **SPEC-009** disclosure; **no** contradictory “connected” vs “sign-in required” per **AMD-2026-012** family where applicable._

---

## 4. Shell vs Workspace boundary

_What **Shell** owns vs **Workspace** canvas; voice/chat routing to `workspace.*` intents._

---

## 5. Gaps / open UX risks

| Risk | Mitigation in spec or code |
|------|----------------------------|
| | |

---

## 6. Verification checklist

- [ ] Surface IDs match **`canvasTypes.ts`** / **`ALL_CANVAS_VIEWS`** (or document **new** IDs for spec merge).
- [ ] No **dashboard-first** regression vs shell authority amendments.
