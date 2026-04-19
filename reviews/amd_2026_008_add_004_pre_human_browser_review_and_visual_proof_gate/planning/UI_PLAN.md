# UI plan — AMD-2026-008-ADD-004 (browser-visible proof)

**Date:** 2026-04-08  
**Depends on:** [`ARCHITECT_PLAN.md`](ARCHITECT_PLAN.md)  
**Primary doctrine:** [`AMD-2026-008-ADD-004`](../../../amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md)

---

## 1. Surfaces in scope

Any **browser-rendered** AI OS surface where **§3.1** applies:

- Shell, overlays, canvas views, navigation and input states
- Review / approve / send / publish controls
- Disclosures, warnings, banners, blocked paths

**Out of scope for mandatory browser proof:** pure doctrine, backend-only, refactors with no rendered change (**§3.2**).

---

## 2. User-visible states to evidence

Map captures to **§7** minimum set:

| Proof type | What reviewers expect to see |
|------------|------------------------------|
| **Surface** | Correct page/shell region; title/context |
| **State** | Draft vs final, blocked, warning visible |
| **Control** | Required actions visible; forbidden actions not offered (or correctly blocked) |
| **Behavior** | Transition, recovery, or fallback as specified |

---

## 3. Human review packet (recommended)

Per **§14**, the UI track should produce or reference:

- `CAPTURE_CHECKLIST.md` — checkbox list tied to `required_visual_proofs`
- `HUMAN_REVIEW_PACKET.md` — narrative + links to screenshots/recordings
- Stable pointer (`review_slug` → folder or URL)

---

## 4. Blocked approval UX (conceptual)

When proof is missing, approval status **SHALL** reflect **§9.2** (e.g. `blocked_pending_visual_proof`) — product implementation **SHALL NOT** show “approved” based on plan/diff alone.

**§9.4 remediation:** UX **SHALL** expose a **recorded** exit path — resubmit proof, narrow **`approval_scope`** (**§9.3**), **§10** exception, or **policy-defined** escalation — without implying **§10** substance from **delay** alone.

---

## 5. Gaps vs architect plan

| Gap | Resolution |
|-----|------------|
| Automated vs manual capture | **§7.2** constrains **test-captured** proof; product policy still needed |
| **§4.1** proportionality | Risk-class UI may shape minimum proof — surface in settings or packet |
| Multi-surface work items | **§9.3** partial approval + explicit scope |

---

## 6. Verification checklist (planning)

- [ ] Shell/composition surfaces from ADD-001–ADD-003 have a **clear** **visual proof** story in the packet.
- [ ] No approval UX implies completion without **§7** minimums.

---

*UI planning baseline — non-normative unless promoted by process.*
