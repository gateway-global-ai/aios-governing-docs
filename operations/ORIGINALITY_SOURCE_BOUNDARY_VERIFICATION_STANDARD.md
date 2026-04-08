---

document_id: ORIGINALITY_SOURCE_BOUNDARY_VERIFICATION_STANDARD

registry_id: AIOS-OPS-020

version: 0.4.1

status: draft

category: operations

title: Originality and Source-Boundary Verification (Implementation Home)

author: Gateway Global AIOS

created: 2026-04-08

last_updated: 2026-04-11

reviewers: []

cross_references:

  - doc_id: AMD-2026-008-ADD-003

    title: Composition Control Plane for Messages, Invites, and Documents

    note: Normative doctrine — §19 originality/source-boundary gate; §19.4 option (b); §19.10 implementation handoff.

amendment_history:

  - version: 0.4.1

    date: 2026-04-11

    summary: "§15 — implementation binding matrix, §18↔§19 handoff (artifact_id + optional knowledge_basis_state on Appendix A); Appendix B JSON Schema CompositionPlaneDcpV1; pipeline steps for emit order."

  - version: 0.4.0

    date: 2026-04-10

    summary: "§14 — minimum DCP envelope fields for §13/§10 rejection codes (validation + informative JSON); defers metric-computer algorithms and protobuf/OpenAPI to v0.5.0+."

  - version: 0.3.2

    date: 2026-04-10

    summary: "§13 — ADD-003 §5.9 fail-closed rows → DCP transport codes (aios.dcp.composition + originality §10 cross-ref)."

  - version: 0.3.1

    date: 2026-04-10

    summary: "§11 — explicit pointer to ADD-003 §19.10 minimum conformance surface mapped to this document’s §§6–10 and Appendix A."

  - version: 0.3.0

    date: 2026-04-10

    summary: "Numeric severity bands (default policy pack), metric names 0.0–1.0, mapping table severity×channel→state; JSON Schema (draft 2020-12) for evaluation record (Appendix A); metric_snapshot optional on record."

  - version: 0.2.0

    date: 2026-04-08

    summary: "Channel classes, signal taxonomy, enforcement states, procedural mapping posture, release-time triggers, minimal evaluation record fields, DCP code names. Numeric scoring algorithms and full JSON Schema file still deferred to v0.3+."

  - version: 0.1.0

    date: 2026-04-08

    summary: "Placeholder registered home for release-time evaluation methods, overlap/similarity scoring, threshold tables, and DCP/transport bindings per ADD-003 §19.4/§19.10. Substance to be filled as product policy matures."

---



# Originality and Source-Boundary Verification (Implementation Home)



## 1. Purpose



**[AMD-2026-008-ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** **§19** defines **required** **verification** **states**, **channel** **posture**, **enforcement** **outcomes**, and **fail-closed** **rules**. **§19.4** allows **policy** to **either** define thresholds **in** **policy** **or** **reference** **this** **artifact** **for** **evaluation** **methods** **(option** **b)**. **§19.10** requires **implementation** **logic**, **scoring**, **schemas**, **and** **transport** **bindings** **to** **have** **a** **traceable** **home**.



This **operations** **standard** **(registry** **AIOS-OPS-020)** **is** **the** **default** **named** **home** **until** **superseded** **by** **a** **policy-registered** **successor**.



## 2. Scope



### In scope (v0.3.0)



- **§§3–5** **—** **channel** **classes**, **signal** **taxonomy**, **canonical** **enforcement** **states**

- **§6** **—** **normative** **metric** **names**, **severity** **bands**, **default** **threshold** **policy** **pack** **(numeric)**

- **§7** **—** **mapping** **severity** **×** **channel** **→** **enforcement** **state**

- **§8** **—** **release-time** **evaluation** **triggers**

- **§9** **—** **evaluation** **record** **field** **contract** **+** **Appendix** **A** **JSON** **Schema**

- **§10** **—** **DCP** **/** **transport** **codes**

- **§13** **—** **ADD-003** **§5.9** **fail-closed** **→** **DCP** **composition** **codes** **(binding** **table**)**



- **§14** **—** **composition-plane** **DCP** **envelope** **minimum** **(field** **contract** **+** **validation** **posture** **for** **§13**/**§10** **codes**)**



- **§15** **—** **implementation** **binding** **matrix** **,** **§18** **↔** **§19** **handoff** **,** **Appendix** **B** **(**`CompositionPlaneDcpV1`**)**



### Deferred to v0.5.0+



- **Concrete** **implementations** **of** **metric** **computers** **(which** **n-grams**, **which** **structural** **distance** **function)** **—** **products** **SHALL** **document** **algorithm** **IDs** **per** **`policy_pack_id`**

- **Full** **DCP** **protobuf**/**OpenAPI** **artifacts** **(if** **distinct** **from** **JSON** **payloads)**



## 3. Channel classes (normative)



| Code | Meaning |

|------|---------|

| `INTERNAL` | **Draft** **or** **collaboration** **surface** **only** **;** **no** **external** **delivery** **on** **this** **path** **(until** **promoted)**. |

| `EXTERNAL` | **Publish**, **send**, **or** **formal** **export** **to** **an** **external** **recipient**, **feed**, **or** **shared** **surface** **per** **ADD-003** **§19.2**. |



**Policy** **MAY** **subdivide** **but** **SHALL** **map** **subdivisions** **to** **these** **two** **base** **classes** **for** **originality** **evaluation**.



**SHALL** **not** **treat** **EXTERNAL** **with** **the** **same** **leniency** **as** **INTERNAL** **unless** **policy** **explicitly** **documents** **equivalent** **risk** **(per** **ADD-003** **§19.4)**.



## 4. Signal classes (from ADD-003 §19.3)



| Code | Primary metric(s) (§6) |

|------|-------------------------|

| `SIG_VERBATIM` | `verbatim_ngram_overlap` |

| `SIG_STRUCTURE` | `structural_similarity_score` |

| `SIG_KB_EXTRACT` | `kb_extraction_score` |

| `SIG_QUOTE` | **Policy** **—** **bounded** **quote** **detection** **;** **may** **reuse** **`verbatim_ngram_overlap`** **on** **non-quoted** **spans** |

| `SIG_PUBLISH_EXT` | **Derived** **from** **channel** **+** **other** **metrics** **(no** **separate** **0–1** **score** **required)** |



## 5. Enforcement states (canonical)



**Aligned** **to** **ADD-003** **§19.5**.



| Canonical `originality_verification_state` | Aliases (informative) |

|-------------------------------------------|------------------------|

| `originality_clear` | `clear` |

| `quote_limited` | `quote_ok` |

| `overlap_review_required` | `review_required` |

| `high_reproduction_risk_blocked` | `blocked` |

| `internal_only` | `internal_only_pending_release` |



## 6. Metrics, severity, and default threshold bands



### 6.1 Normative metrics (real numbers in [0.0, 1.0])



| Metric key | Meaning |

|------------|---------|

| `verbatim_ngram_overlap` | **Maximum** **or** **aggregate** **overlap** **of** **n-gram** **runs** **between** **output** **and** **single** **source** **(product** **defines** **n**, **window)** **—** **scaled** **to** **0–1**. |

| `structural_similarity_score` | **Structural** **similarity** **(outline**/**heading**/**sequence)** **vs** **dominant** **source**, **0–1**. |

| `kb_extraction_score` | **Extraction-style** **dump** **risk** **from** **KB**/**notes**, **0–1**. |



**Implementations** **SHALL** **persist** **the** **metric** **values** **used** **for** **the** **decision** **in** **`metric_snapshot`** **(§9** **/** **Appendix** **A)** **when** **claiming** **conformance** **to** **this** **standard**.



### 6.2 Severity per signal



For **each** **of** **`SIG_VERBATIM`**, **`SIG_STRUCTURE`**, **`SIG_KB_EXTRACT`**, **map** **the** **primary** **metric** **to** **severity**:



| Severity | Meaning |

|----------|---------|

| `NONE` | **Below** **ELEVATED** **floor** **for** **that** **metric** **and** **channel** **column**. |

| `ELEVATED` | **Between** **ELEVATED** **floor** **and** **HIGH** **floor**. |

| `HIGH` | **At** **or** **above** **HIGH** **floor**. |



### 6.3 Default policy pack `AIOS-OPS-020-DEFAULT-v1` (normative defaults)



**Policy** **MAY** **override** **these** **cutoffs** **;** **override** **SHALL** **register** **a** **new** **`policy_pack_id`**. **All** **thresholds** **are** **inclusive** **on** **the** **upper** **bound** **for** **ELEVATED** **and** **exclusive** **above** **HIGH** **where** **noted**.



**`verbatim_ngram_overlap`** **(SIG_VERBATIM)**



| Channel | ELEVATED floor (≥) | HIGH floor (≥) |

|---------|-------------------|----------------|

| `INTERNAL` | 0.08 | 0.28 |

| `EXTERNAL` | 0.04 | 0.18 |



**`structural_similarity_score`** **(SIG_STRUCTURE)**



| Channel | ELEVATED floor (≥) | HIGH floor (≥) |

|---------|-------------------|----------------|

| `INTERNAL` | 0.12 | 0.38 |

| `EXTERNAL` | 0.08 | 0.28 |



**`kb_extraction_score`** **(SIG_KB_EXTRACT)**



| Channel | ELEVATED floor (≥) | HIGH floor (≥) |

|---------|-------------------|----------------|

| `INTERNAL` | 0.10 | 0.35 |

| `EXTERNAL` | 0.06 | 0.25 |



**Interpretation:** **LOWER** **floors** **on** **`EXTERNAL`** **enforce** **stricter** **gates** **for** **the** **same** **raw** **metric** **values** **(per** **ADD-003** **§19.4)**.



## 7. Mapping: severity × channel → enforcement state



**Apply** **after** **computing** **severity** **for** **each** **applicable** **signal** **(§6.2)**. **Use** **the** **worst** **(highest** **risk)** **severity** **across** **signals** **for** **the** **current** **evaluation**.



| Worst severity | `INTERNAL` | `EXTERNAL` |

|----------------|------------|------------|

| `NONE` | `originality_clear` **or** `quote_limited` **if** **only** **bounded** **quotation** **detected** | `originality_clear` **or** `quote_limited` |

| `ELEVATED` | `overlap_review_required` **unless** **policy** **allows** **clear** **for** **draft-only** **;** **default** **`overlap_review_required`** | `overlap_review_required` **(minimum)** |

| `HIGH` | **`internal_only`** **or** **`high_reproduction_risk_blocked`** **per** **product** **policy** **;** **default** **`internal_only`** **if** **artifact** **must** **not** **leave** **internal** **collaboration** | **`high_reproduction_risk_blocked`** **or** **`internal_only`** **;** **default** **`high_reproduction_risk_blocked`** **when** **external** **release** **is** **the** **trigger** |



**Promotion** **from** **`INTERNAL`** **to** **`EXTERNAL`** **SHALL** **re-run** **§8** **evaluation** **with** **`channel_class`** **=`EXTERNAL`** **;** **SHALL** **not** **reuse** **`INTERNAL`** **severity** **classification** **alone** **to** **authorize** **external** **release**.



## 8. Release-time evaluation triggers



**Originality**/**source-boundary** **evaluation** **SHALL** **run** **before** **completing** **any** **of** **the** **following** **when** **ADD-003** **§19.2** **applies** **to** **the** **artifact** **class**:



1. **Publish**

2. **Send**

3. **Formal** **export**

4. **Shared** **external** **surface** **(policy-defined)**



**Evaluation** **SHALL** **not** **be** **skipped** **on** **silent** **defaults** **;** **missing** **evaluation** **when** **required** **SHALL** **fail** **closed** **per** **ADD-003** **§5.9**.



## 9. Evaluation record (field contract)



**Control-plane** **and** **audit** **logs** **SHALL** **conform** **to** **Appendix** **A** **JSON** **Schema** **`OriginalityEvaluationRecordV1`** **for** **the** **payload** **shape** **(JSON** **encoding)**.



| Field | Required | Description |

|-------|:--------:|-------------|

| `originality_verification_state` | **Yes** | Canonical **value** **from** **§5** |

| `channel_class` | **Yes** | `INTERNAL` **\|** `EXTERNAL` |

| `evaluation_trigger` | **Yes** | **`publish`** **\|** **`send`** **\|** **`formal_export`** **\|** **`shared_surface`** |

| `signal_flags` | **No** | **Array** **of** **§4** **codes** |

| `policy_pack_id` | **No** | **Default** **`AIOS-OPS-020-DEFAULT-v1`** **when** **omitted** **for** **threshold** **lookup** |

| `evaluated_at` | **Yes** | **UTC** **ISO** **8601** |

| `artifact_id` | **No** | **Stable** **artifact** **id** |

| `metric_snapshot` | **No** | **Object** **with** **§6.1** **keys** **and** **numeric** **values** **used** **for** **the** **decision** |

| `dcp_outcome_code` | **No** | **§10** **outcome** **code** **redundant** **with** **state** **but** **required** **for** **DCP** **transport** **when** **using** **DCP** **envelope** |



## 10. DCP / transport binding names



**Namespace:** **`aios.dcp.originality`**



**Outcome** **codes** **(map** **to** **§5)**



| Code | Canonical state |

|------|-----------------|

| `ORIG_CLEAR` | `originality_clear` |

| `ORIG_QUOTE_LIMITED` | `quote_limited` |

| `ORIG_REVIEW_REQUIRED` | `overlap_review_required` |

| `ORIG_BLOCKED` | `high_reproduction_risk_blocked` |

| `ORIG_INTERNAL_ONLY` | `internal_only` |



**Fail-closed** **rejection** **reasons**



| Code | When |

|------|------|

| `ORIG_REJECT_MISSING_EVAL` | **Required** **gate** **not** **run** **or** **no** **state** **recorded** |

| `ORIG_REJECT_CHANNEL_MISMATCH` | **EXTERNAL** **release** **with** **INTERNAL-only** **clearance** |

| `ORIG_REJECT_POLICY_STALE` | **Policy** **pack** **missing** **or** **invalid** |



## 11. Normative anchor



**Doctrine** **remains** **in** **ADD-003** **§19** **and** **§5.9**. **This** **artifact** **binds** **metrics**, **thresholds**, **evaluation** **records**, **DCP** **codes** **in** **§§10** **and** **§13** **,** **§14**/**§15** **implementation** **paths** **,** **and** **ADD-003** **§5.9**/**§19** **transport** **mappings**. **Products** **claiming** **§19** **conformance** **via** **this** **standard** **SHALL** **meet** **the** **minimum** **surface** **enumerated** **in** **ADD-003** **§19.10** **(mapped** **to** **§§6**–**10** **,** **§15** **,** **and** **Appendices** **A**–**B** **here**)** **;** **products** **emitting** **DCP** **for** **§5.9** **composition** **fail-closed** **rows** **SHALL** **use** **§13** **codes** **unless** **policy** **extends** **the** **namespace** **.**



## 12. Revision path



**v0.5.0** **—** **algorithm** **IDs** **and** **optional** **separate** **machine-readable** **schema** **URL** **for** **DCP** **protobuf** **definitions** **(see** **§2** **"Deferred** **to** **v0.5.0+")** **.**



## 13. ADD-003 §5.9 fail-closed → DCP transport codes (composition plane)



**Normative** **binding** **for** **[ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** **§5.9** **fail-closed** **table** **:** **implementations** **SHALL** **emit** **the** **codes** **below** **on** **control-plane** **/** **DCP** **envelopes** **when** **signaling** **those** **failure** **modes** **(unless** **policy** **registers** **a** **compatible** **extension** **namespace** **)** **.** **Originality-only** **failures** **reuse** **§10** **where** **noted** **.**



**Namespace** **`aios.dcp.composition`** **(non-originality** **gates** **)** **:**



| ADD-003 §5.9 condition (summary) | DCP code | Typical enforcement surface |

|--------------------------------|----------|------------------------------|

| **Mandatory** **composition** **contract** **fields** **missing** **or** **invalid** **where** **§5** **requires** **them** | `COMP_CONTRACT_INCOMPLETE` | **No** **substantive** **draft** **except** **explicit** **§5.4** **scaffold**/**outline** **path** **;** **no** **silent** **promotion** **to** **send-ready** **.** |

| **Professional-use** **disclosure** **metadata** **or** **§9.4** **surface** **missing** **where** **§9.4** **applies** | `COMP_PROF_DISCLOSURE_MISSING` | **Block** **send**/**publish**/**export** **as** **professional-use** **draft** **until** **remediated** **or** **policy** **exception** **;** **§9.4.3(5)** **export** **rules** **.** |

| **Knowledge** **basis** **insufficiency** **where** **§18** **requires** **grounding** **or** **discovery** | `COMP_KNOWLEDGE_INSUFFICIENT` | **Scaffold-only**, **blocked**, **or** **discovery-required** **per** **§18.5**/**§18.6** **;** **no** **silent** **external** **release** **.** |



**Namespace** **`aios.dcp.originality`** **(§10)** **—** **originality**/**source-boundary** **row** **of** **§5.9** **:**



| ADD-003 §5.9 condition (summary) | DCP code | Typical enforcement surface |

|--------------------------------|----------|------------------------------|

| **Originality**/**source-boundary** **verification** **outcome** **missing**, **unknown**, **or** **not** **permitted** **for** **the** **target** **channel** **where** **§19.2** **requires** **a** **gate** | `ORIG_REJECT_MISSING_EVAL` **(**§10**)** | **No** **publish**/**send**/**formal** **export** **until** **§19** **evaluation** **record** **and** **§19.5** **permit** **;** **may** **pair** **with** **`ORIG_*`** **outcome** **codes** **once** **eval** **exists** **.** |



**Note** **:** **`COMP_*`** **codes** **describe** **composition-plane** **and** **gating** **failures** **outside** **the** **numeric** **metric** **pipeline** **;** **they** **SHALL** **not** **replace** **`OriginalityEvaluationRecordV1`** **when** **§19** **evaluation** **runs** **.**



## 14. Composition-plane DCP envelope (minimum transport) — v0.4.0



**Purpose** **:** **When** **emitting** **§13** **(**composition** **)** **or** **§10** **(**originality** **)** **rejection** **/** **fail-closed** **codes** **on** **the** **control** **plane** **,** **implementations** **SHALL** **emit** **a** **machine-readable** **envelope** **with** **at** **least** **the** **fields** **below** **(**JSON** **or** **equivalent** **)** **.** **This** **does** **not** **replace** **Appendix** **A** **for** **full** **evaluation** **records** **.**



| Field | Required | Notes |

|-------|----------|--------|

| **`dcp_namespace`** | **Yes** | **`aios.dcp.composition`** **,** **`aios.dcp.originality`** **,** **or** **policy-registered** **extension** **.** |

| **`dcp_code`** | **Yes** | **Registered** **code** **from** **§13** **or** **§10** **(**e.g.** **`COMP_CONTRACT_INCOMPLETE`** **,** **`ORIG_REJECT_MISSING_EVAL`** **)** **.** |

| **`artifact_id`** | **No** | **Stable** **artifact** **id** **when** **the** **failure** **is** **tied** **to** **a** **specific** **artifact** **.** |

| **`trace_id`** | **No** | **Correlation** **id** **for** **logs** **/** **support** **.** |

| **`related_evaluation_record_id`** | **No** | **Opaque** **id** **or** **URI** **to** **an** **Appendix** **A** **record** **when** **§19** **evaluation** **exists** **(**see** **Appendix** **B** **)** **.** |



**Validation** **posture** **:** **empty** **or** **missing** **`dcp_code`** **SHALL** **not** **be** **treated** **as** **success** **;** **unknown** **codes** **SHALL** **fail** **closed** **or** **map** **to** **policy-defined** **handling** **.**



**Informative** **JSON** **example** **:**



```json

{ "dcp_namespace": "aios.dcp.composition", "dcp_code": "COMP_CONTRACT_INCOMPLETE", "artifact_id": "art_123", "related_evaluation_record_id": "oer_v1:eval_789" }

```



---



## 15. Implementation binding matrix and §18 ↔ §19 handoff (v0.4.1)



### 15.1 Traceability — ADD-003 doctrine → this artifact



| ADD-003 locus | AIOS-OPS-020 binding | Implementers SHALL emit / record |
|---------------|----------------------|----------------------------------|
| **§5.9** fail-closed (**composition** rows) | **§13** + **§14** | **§14** envelope with **`dcp_namespace`** + **`dcp_code`** from **§13** |
| **§5.9** fail-closed (**originality** row) | **§10** + **§13** + **§14** | **`ORIG_REJECT_MISSING_EVAL`** **or** **paired** **`ORIG_*`** **with** **Appendix** **A** **when** **eval** **exists** |
| **§18.11** **B** (release **gate**) | **§8** **triggers** **,** **§9** **record** **,** **Appendix** **A** | **`OriginalityEvaluationRecordV1`** **when** **§19.2** **applies** |
| **§18.11** **joinability** **posture** | **§9** **`artifact_id`** **+** **optional** **`knowledge_basis_state`** **(**Appendix** **A** **)** | **Same** **`artifact_id`** **as** **§18** **metadata** **for** **the** **artifact** **SHALL** **appear** **on** **the** **evaluation** **record** **when** **both** **§18** **and** **§19** **apply** |



### 15.2 Processing pipeline (normative intent)



1. **Composition** **§5.9** **fail-closed** **—** **emit** **§14** **envelope** **(**`aios.dcp.composition`** **+** **§13** **code** **)** **before** **silent** **promotion** **to** **substantive** **/** **send-ready** **.**  
2. **§19** **required** **for** **release** **—** **produce** **Appendix** **A** **record** **or** **emit** **`ORIG_REJECT_MISSING_EVAL`** **(**§14** **+** **§10** **)** **until** **eval** **exists** **.**  
3. **§18** **+** **§19** **on** **same** **artifact** **—** **`artifact_id`** **SHALL** **align** **;** **`knowledge_basis_state`** **SHOULD** **be** **set** **when** **§18.5** **classification** **is** **known** **(**Appendix** **A** **optional** **field** **)** **.**



### 15.3 End-to-end informative examples



**A** **—** **Composition** **fail-closed** **only** **(**no** **§19** **eval** **yet** **)** **:**



```json

{ "dcp_namespace": "aios.dcp.composition", "dcp_code": "COMP_CONTRACT_INCOMPLETE", "artifact_id": "art_123", "trace_id": "tr_abc" }

```



**B** **—** **§19** **eval** **record** **(**Appendix** **A** **excerpt** **with** **§18** **join** **)** **:**



```json

{

  "artifact_id": "art_123",

  "knowledge_basis_state": "sufficient",

  "originality_verification_state": "originality_clear",

  "channel_class": "EXTERNAL",

  "evaluation_trigger": "publish",

  "evaluated_at": "2026-04-10T12:00:00Z"

}

```



---



## Appendix A — JSON Schema (OriginalityEvaluationRecordV1)



**Draft** **2020-12**. **URI** **`https://aios.governance/schemas/originality-evaluation-record-v1.json`** **(informative** **—** **register** **in** **product** **catalog** **when** **stable)**.



```json

{

  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "$id": "https://aios.governance/schemas/originality-evaluation-record-v1.json",

  "title": "OriginalityEvaluationRecordV1",

  "type": "object",

  "additionalProperties": false,

  "required": [

    "originality_verification_state",

    "channel_class",

    "evaluation_trigger",

    "evaluated_at"

  ],

  "properties": {

    "originality_verification_state": {

      "type": "string",

      "enum": [

        "originality_clear",

        "quote_limited",

        "overlap_review_required",

        "high_reproduction_risk_blocked",

        "internal_only"

      ]

    },

    "channel_class": {

      "type": "string",

      "enum": ["INTERNAL", "EXTERNAL"]

    },

    "evaluation_trigger": {

      "type": "string",

      "enum": ["publish", "send", "formal_export", "shared_surface"]

    },

    "signal_flags": {

      "type": "array",

      "items": {

        "type": "string",

        "enum": [

          "SIG_VERBATIM",

          "SIG_STRUCTURE",

          "SIG_KB_EXTRACT",

          "SIG_QUOTE",

          "SIG_PUBLISH_EXT"

        ]

      }

    },

    "policy_pack_id": {

      "type": "string",

      "description": "Omit to use AIOS-OPS-020-DEFAULT-v1 thresholds."

    },

    "evaluated_at": {

      "type": "string",

      "format": "date-time"

    },

    "artifact_id": { "type": "string" },

    "knowledge_basis_state": {

      "type": "string",

      "description": "Optional join to ADD-003 §18.5 when §18 applied to the same artifact as §19.",

      "enum": ["sufficient", "partial", "insufficient", "stale", "conflicted", "unverified"]

    },

    "metric_snapshot": {

      "type": "object",

      "additionalProperties": false,

      "properties": {

        "verbatim_ngram_overlap": { "type": "number", "minimum": 0, "maximum": 1 },

        "structural_similarity_score": { "type": "number", "minimum": 0, "maximum": 1 },

        "kb_extraction_score": { "type": "number", "minimum": 0, "maximum": 1 }

      }

    },

    "dcp_outcome_code": {

      "type": "string",

      "enum": [

        "ORIG_CLEAR",

        "ORIG_QUOTE_LIMITED",

        "ORIG_REVIEW_REQUIRED",

        "ORIG_BLOCKED",

        "ORIG_INTERNAL_ONLY"

      ]

    }

  }

}

```



## Appendix B — JSON Schema (CompositionPlaneDcpV1)



**Draft** **2020-12**. **URI** **`https://aios.governance/schemas/composition-plane-dcp-v1.json`** **(informative** **—** **register** **in** **product** **catalog** **when** **stable** **)** **.** **Normative** **field** **contract** **remains** **§14** **;** **this** **appendix** **supplies** **a** **machine-readable** **schema** **for** **validators** **and** **CI** **.**



```json

{

  "$schema": "https://json-schema.org/draft/2020-12/schema",

  "$id": "https://aios.governance/schemas/composition-plane-dcp-v1.json",

  "title": "CompositionPlaneDcpV1",

  "type": "object",

  "additionalProperties": false,

  "required": ["dcp_namespace", "dcp_code"],

  "properties": {

    "dcp_namespace": {

      "type": "string",

      "enum": ["aios.dcp.composition", "aios.dcp.originality"]

    },

    "dcp_code": { "type": "string" },

    "artifact_id": { "type": "string" },

    "trace_id": { "type": "string" },

    "related_evaluation_record_id": {

      "type": "string",

      "description": "Opaque id or URI to an OriginalityEvaluationRecordV1 (Appendix A) when §19 eval exists."

    }

  }

}

```


