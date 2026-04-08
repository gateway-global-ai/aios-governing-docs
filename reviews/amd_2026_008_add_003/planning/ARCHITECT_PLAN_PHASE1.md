Here is the reformatted text:

# Architect plan — AMD-2026-008-ADD-003 (Composition control plane) + AIOS-OPS-020

**Date:** YYYY-MM-DD  
**Evidence used:** knowledge bundle (`government_and_reports_bundle.md`); `product_context_bundle.md` if present in bundle  
**Verifier:** _name / role_

**Primary doctrine:** [`amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md`](../../../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md) **`draft` `0.14.5`** (or current)  
**Default ops artifact:** [`operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md`](../../../operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION STANDARD.md) **AIOS-OPS-020** **`v0.3.2"`

## 1. Executive summary

_3–6 sentences: what the composition control plane owns vs ADD-001 / ADD-002; release-time originality handoff to OPS-020; §5.9 fail-closed → §13 DCP codes._

## 2. Current system grounding (file-cited)

| Topic | Repo path(s) | Notes |
|-------|--------------|--------|
| Composition / voice surfaces | `ai-os-voice-interface` — _cite from bundle_ | |
| Control-plane / DCP emission | _cite from bundle or_ **unknown** | |
| Governance — ADD-003 | `aios-governing-docs/amendments/AMD-2026-008-ADD-003-*.md` | |
| Governance — OPS-020 | `aios-governing-docs/operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md` | **§13** **COMP_***/**ORIG_*** |

## 3. Schemas / records (normative targets)

_Tables or JSON fragments: composition contract fields (§5); `OriginalityEvaluationRecordV1` (OPS Appendix A); DCP envelope fields for §5.9 / §13 codes._

## 4. Gate flow (§18 → §19 → release)

_Table or numbered flow: knowledge basis / discovery → substantive draft → originality eval → publish/send/export; where OPS-020 §6–§10 applies._
