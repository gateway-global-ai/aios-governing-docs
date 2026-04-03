# Source material: AMD-2026-005 Workspace Model & Governed Interface Surfaces

**Status:** Working source for formal amendment `amendments/AMD-2026-005.md`  
**Date:** 2026-04-02  
**Derivation:** Consolidates the voice-interface implementation (workspace hub, intent routing, load-state truth) with the draft in `ai-os-voice-interface/user uploads/ammendment_chatgpt_aios_pr_submission.md`.

## Executive summary

The Amendment Program and related governed surfaces must operate under a **workspace model**: **hub → selection → workflow**, with **no implicit execution**, **explicit intents** (`hub`, `resume`, `review`, `create`), **transparent load states** (`ok` | `empty` | `error`), and **binding** intent/view/run schemas for implementations.

## Implementation references (authoritative evidence)

| Area | Location |
|------|----------|
| Canvas views & intents | `ai-os-voice-interface/src/governance/canvasTypes.ts`, `intentParse.ts` |
| Hub payload & load truth | `ai-os-voice-interface/src/governance/loadGovernancePayload.ts` |
| Run status buckets | `ai-os-voice-interface/src/governance/amendmentStatus.ts` |
| API list runs / templates | `ai-os-voice-interface/src/api/governance.ts` |
| Policy denial / canvas | `ai-os-voice-interface/src/governance/GovernanceCanvasContext.tsx` |

## Normative goals (carried into amendment)

1. **Workspace hub** as first-class canvas (`amendment_hub`) — no auto-create on entry.  
2. **Intent routing** — structured `INTENT_JSON` with required parameters per intent class.  
3. **Shell vs view** — governance canvas provider owns navigation; surfaces own content; footer/mode contract described in amendment annex.  
4. **Execution constraints** — no implicit workflow creation; user or explicit intent triggers execution.  
5. **Transparency** — hub and API lists must not conflate failure with empty registry.  
6. **Ratification path** — author pre-validation → triangulated peer review → score thresholds → ratification; **no** post–peer-review human audit step (see amendment supersession clause).
