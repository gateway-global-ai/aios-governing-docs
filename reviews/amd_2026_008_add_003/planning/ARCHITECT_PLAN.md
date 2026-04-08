# Architect plan — AMD-2026-008-ADD-003 (merged)

**Date:** 2026-04-08  
**Method:** Local Ollama — phased phases + Ollama merge pass into single body.

---

# Architect plan — AMD-2026-008-ADD-003 (Composition control plane) + AIOS-OPS-020

**Date:** YYYY-MM-DD  
**Evidence used:** knowledge bundle (`government_and_reports_bundle.md`); `product_context_bundle.md` if present in bundle  
**Verifier:** _name / role_

**Primary doctrine:** [`amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md`](../../../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md) **`draft` `0.14.5`** (or current)  
**Default ops artifact:** [`operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md`](../../../operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION STANDARD.md) **AIOS-OPS-020** **`v0.3.2"`

## 1. Executive summary

The composition control plane is responsible for managing the release-time originality handoff to OPS-020. This includes fail-closed → §13 DCP codes and ensuring that the composition contract fields (§5) are complete.

## 2. Current system grounding (file-cited)

| Topic | Repo path(s) | Notes |
|-------|--------------|--------|
| Composition / voice surfaces | `ai-os-voice-interface` — _cite from bundle_ | |
| Control-plane / DCP emission | `_cite from bundle or unknown_` | |
| Governance — ADD-003 | `aios-governing-docs/amendments/AMD-2026-008-ADD-003-*.md` | |
| Governance — OPS-020 | `aios-governing-docs/operations/ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD.md` | **§13** **COMP_***/**ORIG_*** |

## 3. Schemas / records (normative targets)

_Tables or JSON fragments:_

*   Composition contract fields (§5)
*   `OriginalityEvaluationRecordV1` (OPS Appendix A)
*   DCP envelope fields for §5.9 / §13 codes

### Composition Contract Fields
| Field Name | Data Type | Description |
|------------|-----------|-------------|
| composition_contract_incomplete | _boolean_ | Whether the field is complete |
| professional_disclosure_missing | _boolean_ | Whether the field is missing disclosure information |

### OriginalityEvaluationRecordV1
| Field Name | Data Type | Description |
|------------|-----------|-------------|
| originality_evaluation_status | _string_ | The status of the originality evaluation |
| evaluation_date | _date_ | The date of the originality evaluation |

### DCP Envelope Fields
| Field Name | Data Type | Description |
|------------|-----------|-------------|
| dcp_envelope_content | _string_ | The content of the DCP envelope |
| dcp_envelope_header | _string_ | The header of the DCP envelope |

## 4. Gate flow (§18 → §19 → release)

_Table or numbered flow:_

*   Knowledge basis / discovery
*   Substantive draft
*   Originality eval
*   Publish/send/export

### Table:
| Step # | Step Name | Notes |
|--------|-----------|-------|
| 1      | Discovery | Identify knowledge gaps and required data |
| 2      | Draft | Create substantive draft based on discovery findings |
| 3      | Evaluation | Conduct originality evaluation using `OriginalityEvaluationRecordV1` |
| 4      | Publish | Publish the final version of the composition control plane |

## 5. DCP / transport (§5.9 ↔ OPS-020 §13)

| ADD-003 §5.9 row | Code | Namespace | Notes |
|------------------|------|-----------|----------|
| Composition contract | `COMP_CONTRACT_INCOMPLETE` | `aios.dcp.composition` | This row is missing a specific description for the composition contract field. |
| Professional disclosure | `COMP_PROF_DISCLOSURE_MISSING` | `aios.dcp.composition` | The professional disclosure field is required in all cases, except when specified by policy. |
| Knowledge insufficiency | `COMP_KNOWLEDGE_INSUFFICIENT` | `aios.dcp.composition` | This row should include additional guidance for handling knowledge insufficiencies. |

## 6. Gaps vs governing text

| AMD/OPS Section | Proposed Resolution |
|-----------------|--------------------|
| §5.9 | Ensure composition contract fields are complete before release |
| §13 | Include additional guidance for handling knowledge insufficiencies |

## 7. Verification checklist
[] 
[] 
[]
