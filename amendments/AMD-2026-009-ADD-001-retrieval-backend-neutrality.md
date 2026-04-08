---
document_id: AMD-2026-009-ADD-001
parent_amendment: AMD-2026-009
parent_version: 0.1.6
version: 1.0.3
status: draft
category: amendment_addendum
title: Retrieval backend neutrality (beyond Google PSE / Custom Search)
author: Gateway Global AIOS
created: 2026-04-03
last_updated: 2026-04-08
ratification_target: null
peer_review: round_1_complete
peer_review_date: 2026-04-08
reviewers:
  - DeepSeek R3
  - OpenAI
  - Gemini 2.5 Pro
peer_review_rounds:
  round_1: reviews/amd_2026_009_add_001/round_1/
cross_references:
  - doc_id: AMD-2026-009
  - doc_id: AIOS-SPEC-007
  - doc_id: AIOS-SPEC-010
  - path: reviews/amd_2026_009_add_001/round_1/REVIEW_BRIEF.md
    note: Triangulated peer review prompt (search/knowledge strategy)
  - path: reviews/amd_2026_009_add_001/round_1/REVIEW_SYNTHESIS.md
    note: Round 1 synthesis — approved_with_changes; gate report
addendum_history:
  - version: 1.0.3
    date: 2026-04-08
    summary: Narrow post–Round 1 author revision — §2 minimum registration fields + diligence ownership; §2.3 backend eligibility; §2.1 default-deny scraping / unofficial endpoints; informative table retained.
  - version: 1.0.2
    date: 2026-04-08
    summary: Triangulated peer review Round 1 complete — reviews/amd_2026_009_add_001/round_1/ (light rubric); RATIFICATION_GATE_REPORT PASS AMD-2026-005 numerics; disposition approved_with_changes (author revision before ratification).
  - version: 1.0.1
    date: 2026-04-03
    summary: §2.1 privacy/independent providers (DuckDuckGo et al.); triangulated peer review brief under reviews/amd_2026_009_add_001/.
  - version: 1.0.0
    date: 2026-04-03
    summary: Initial draft — policy-registered retrieval backends; PSE optional; exemplar providers.
---

# AMD-2026-009-ADD-001 — Retrieval backend neutrality

## 0. Status and intent

| Field | Value |
|-------|--------|
| **Status** | `draft` — **addendum** to **[AMD-2026-009](AMD-2026-009.md)** for Council / architecture review |
| **Does not replace** | **AMD-2026-009** remains the parent framework for **governed external knowledge acquisition**. This addendum **narrows** one implementation assumption: **Google Programmable Search Engine (PSE) / Custom Search JSON API** is **one** permitted **retrieval backend**, not a **mandatory** exclusive. |

## 1. Problem statement (operational)

Many deployments use **PSE** with **`GOOGLE_PSE_*`** credentials on the MCP host. Operators report that **PSE / Custom Search Engine** configuration is increasingly **manual** (e.g. site lists and engine definition via **Google Cloud / Programmable Search** consoles) and **not** always **programmatically** maintainable at the cadence required for **policy-as-code** or **frequent scope changes**.

**Governance need:** The **same** normative guarantees (**search scope classes**, **SPEC-010** envelope, **review modes**, **audit §9**) **SHALL** hold regardless of whether results come from **PSE**, a **provider-native web/grounding API**, or another **policy-approved** bounded retrieval implementation.

## 2. Normative effect (upon ratification of this addendum)

When **AMD-2026-009-ADD-001** is ratified alongside or after **AMD-2026-009**:

1. **Retrieval backend** **SHALL** be **explicitly registered** in policy (extend **POL-WEB-SCOPE-001** or add **POL-WEB-RETRIEVAL-BACKEND-001**). Each registration **SHALL** include at minimum:
   1. **`backend_id`** — stable identifier referenced by **SPEC-010** keys (§3) and **audit** metadata.
   2. **`allowed_scope_classes`** — subset of **AMD-2026-009 §4** classes this backend may serve.
   3. **`hosting`** — **server-side** only; **MUST NOT** ship raw provider secrets to browser bundles.
   4. **`audit_reference_format`** — how the active backend appears in logs (**alias** — **not** raw secrets).
   5. **`result_evidence_contract`** — that the backend returns a **citable** structured list (at minimum **title**, **snippet**, **URL** per item, or a **policy-referenced** schema id for the same).
   6. **`operator_attestation`** — **Operator** (tenant / deployer) **SHALL** be named as the party responsible for **commercial** and **ToS** diligence for that backend; **Council** (or body **Council** delegates for this purpose) **SHALL** record **first production approval** (identifier + date) when the stack adopts a **new** backend class not previously approved for that environment.
2. **Google PSE / Custom Search JSON API** **MAY** remain a **valid** backend where operators choose it; it is **not** required to be the **only** backend.
3. **Alternative backends** **MAY** be used only where **all** of the following hold:
   1. The integration uses the provider’s **officially published**, **commercially supported** API (or **documented** stable contract with a **licensed** intermediary such as an aggregator **named** in policy) that returns **citable result lists** suitable for **result_set_review**.
   2. **Operator** has completed **commercial / ToS** diligence appropriate to the deployment and **SHALL** retain evidence suitable for audit (not necessarily in-repo).
   3. **Council** (or delegate) **approval record** exists per **§2** item **1.6** before **production** use of a **new** backend **class** for that governed environment.
4. **Illustrative providers** ( **informative only** — not exhaustive, not endorsement):
   - **Google** — **Gemini**-family APIs with **grounding** / **Search** tools where the product binds **scope** and **discloses** retrieval (register the **concrete** API surface in policy).
   - **OpenAI** — APIs that expose **web search** or **grounded** retrieval as **bounded** tool outputs (e.g. Responses API patterns), registered per tenant policy.
   - **DeepSeek** or **other providers** — only under **§2.3**; **MUST NOT** rely on ad hoc prompt-only “pretend to browse.”
5. **Logical resource keys** in **AIOS-SPEC-010** **`review_files`** **SHALL** support a **backend-agnostic** pattern in addition to **`web:pse:…`** (see §3).
6. **MUST NOT:** This addendum **does not** authorize **unbounded** browsing, **silent** provider switching, or **weakening** **AMD-2026-009 §4** / **§11** non-goals.

### 2.1 High-risk retrieval surfaces (normative)

1. **HTML scraping**, **headless rendering of arbitrary sites**, and **unofficial** / **reverse-engineered** HTTP endpoints **SHALL NOT** be registered or used as **governed** retrieval backends **by default**.
2. Any **exception** to **§2.1** item **1** **SHALL** be **Council-recorded** (or delegate with written charter), with **operator**-signed risk acceptance and **explicit** legal/compliance review **before** production routing — not informal “best effort.”
3. **MUST NOT** treat **§2** item **4** (illustrative providers) as **automatically** compliant; **each** backend **SHALL** satisfy **§2**, **§2.1**, **§2.2**, and **parent** **AMD-2026-009** non-goals.

### 2.2 Privacy-first and independent index providers (informative)

Operators may prefer **non-Google** search surfaces for **privacy**, **jurisdiction**, or **vendor diversity**. The table below is **illustrative**, not normative; **each** row **still** requires **§2** registration, **§2.1** compliance, and **no** weakening of the parent amendment.

| Class | Examples (informative) | Governance notes |
|-------|------------------------|------------------|
| **Independent / privacy-oriented** | **DuckDuckGo** (official offerings are **narrow** — e.g. Instant Answer / limited APIs; **not** a full public SERP product comparable to PSE for all use cases), **Brave Search API**, other **paid** search APIs | Prefer **vendor-documented** HTTP APIs with **stable** result shapes. **§2.1** default-deny applies to **scraping** / **unofficial** endpoints. |
| **Major index APIs** | **Bing Web Search**, **Google** programmatic surfaces **other than** PSE where licensed | Register **backend_id** per tenant; respect **quota**, **attribution**, and **region** terms. |
| **Aggregator / SERP proxies** | Third parties that return structured SERP from multiple engines | **Contract** is with the **aggregator**; still **SHALL** record **which** logical engine family was requested in **audit** metadata where knowable. |
| **LLM-native “search” tools** | **Gemini**, **OpenAI**, **DeepSeek** tool or grounding features | Must return **citable** segments for **result_set_review**, not prose-only “trust me.” |

**DuckDuckGo specifically:** There is **no** drop-in replacement for **PSE** with identical governance knobs for every tenant. If **DuckDuckGo** (or similar) is chosen, **Council** **SHALL** record **which** integration path is used (official limited API vs **commercial** search API product vs aggregator). **Scraping**-based paths **SHALL NOT** be claimed as **AMD-2026-009**-compliant except under **§2.1** paragraph **2** (Council-recorded exception).

**Triangulated peer input:** See **[round_1/REVIEW_BRIEF.md](../reviews/amd_2026_009_add_001/round_1/REVIEW_BRIEF.md)** and **[round_1/REVIEW_SYNTHESIS.md](../reviews/amd_2026_009_add_001/round_1/REVIEW_SYNTHESIS.md)** (Round 1 complete **2026-04-08**).

## 3. SPEC-010 logical keys (addition to AMD-2026-009 §1.2)

Implementations **SHALL** accept at least the following **generic** pattern (alongside existing **`web:pse:…`** examples):

| Example key (illustrative) | Binds |
|----------------------------|--------|
| `web:retrieval:{backend_id}:{query_fingerprint}` | One **governed** bounded retrieval call for a **policy-registered** backend **`backend_id`** and normalized query fingerprint. |

**`backend_id`** **SHALL** map to the policy register row (**§2** item **1**). **Fingerprinting** remains as in parent amendment.

## 4. Deltas to sibling artifacts (checklist)

| Artifact | Delta |
|----------|--------|
| **AMD-2026-009** | Incorporate §1.3 summary + link; optional wording tweaks in §1 Purpose flow and §3 **Web retrieval** definition (see parent amendment when merged). |
| **AIOS-SPEC-007** | §3: retrieval **SHALL** be policy-scoped for **any** registered backend, not **PSE-only**; env vars **SHALL** use **server-side** secrets for the **active** backend. |
| **WORKSPACE.md** | Informative: troubleshooting may list **non-PSE** env vars per MCP release; **PSE** remains one path. |
| **Product / MCP** | Register backends in **POL-WEB-*** ; map **`workspace.web.search`** (or successor) to **configured** backend per tenant. |

## 5. Non-goals

- **Does not** require any specific cloud vendor.
- **Does not** bless **prompt-only** web access without **bounded** API evidence and **audit**.
- **Does not** change **page_review** limits or **broad_public** triggers except through **shared** parent amendment text.

## 6. Ratification checklist (addendum)

- [ ] Council approves **AMD-2026-009-ADD-001** as amending **AMD-2026-009** implementation assumptions.
- [ ] **POL-WEB-RETRIEVAL-BACKEND-001** (or merged policy row) drafted.
- [ ] **SPEC-010** / product **review_files** validators accept **`web:retrieval:…`** where applicable.
- [ ] **WORKSPACE.md** / operator docs updated for **multi-backend** configuration.
- [ ] **Triangulated peer review** (see `reviews/amd_2026_009_add_001/round_1/`) completed or consciously waived with rationale.

---

*End of AMD-2026-009-ADD-001, version 1.0.3.*
