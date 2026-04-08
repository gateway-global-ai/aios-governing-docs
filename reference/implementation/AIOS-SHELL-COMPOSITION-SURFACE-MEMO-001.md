---
document_id: AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001
version: 1.0.0
status: draft
category: reference
title: Shell and composition — surface grammar and user-state memo (AMD-2026-008 addendum track)
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008-ADD-001
  - doc_id: AMD-2026-008-ADD-002
  - doc_id: AMD-2026-008-ADD-003
  - doc_id: AIOS-SPEC-006
  - doc_id: AIOS-COMPOSITION-CONTROL-RD-NOTES-001
  - doc_id: AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001
note: Informative UI/shell grounding; product implementation is ai-os-voice-interface.
amendment_history:
  - version: 1.0.0
    date: 2026-04-10
    summary: Initial surface memo — primitives, VC, BOOK gates, review states, paid gates; maps to addenda.
---

# Shell and composition — surface grammar and user-state memo (001)

## Purpose

This memo **backfills** the **UI/shell** **synthesis** **layer**: **what** **users** **and** **operators** **should** **see** **and** **traverse** **so** **that** **[ADD-001](../amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**/**[ADD-002](../amendments/AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)**/**[ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** **doctrine** **does** **not** **float** **without** **surface** **consequence**. It is **informative** **only**; **normative** **UI** **law** **remains** **[AIOS-SPEC-006](../specifications/UIComponentRegistryStandard.md)** **where** **it** **applies**.

**Inputs:** **[AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001](AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.md)**.

---

## Navigation primitives (ADD-001) — surface mapping

| Primitive | User-visible meaning | Typical transition |
|-----------|----------------------|---------------------|
| **START_HERE** | **Entry** **point**; **one** **recommended** **next** **step** | **Idle** **→** **focused** **task** |
| **CONTINUE** | **Resume** **linear** **flow** **without** **branching** | **Step** **n** **→** **n+1** |
| **CHOOSE** | **Explicit** **choice** **among** **options** | **Branch** **selection** |
| **SINGLE_INPUT** | **One** **slot** (e.g. **text**, **confirm**) | **Collect** **→** **validate** |
| **MULTI_INPUT** | **Several** **slots** **before** **proceed** | **Form** **→** **submit** |

**Design rule:** **Navigation** **class** **SHALL** **be** **visible** **or** **derivable** **from** **shell** **chrome** (footer, **prompt** **context**, **or** **voice** **system** **turn**) — **not** **only** **inferred** **from** **model** **prose**.

---

## Output depth and voice (ADD-002) — surface mapping

| Control | User-visible meaning |
|---------|----------------------|
| **Depth** **(RESPONSE** **→** **BOOK**)** | **How** **much** **artifact** **is** **being** **produced**; **BOOK** **implies** **long-form** **structure** **and** **review** **checkpoints** |
| **VC0**–**VC5** | **Density**, **delivery**, **interruption**, **transformation**, **routing**, **segment** **traversal** **—** **shell** **controls** **over** **narration** |
| **Packaging** | **Export** **format** **(TXT**/**MD**/**PDF**/**DOCX**/**JSON**/**HTML**)** **as** **explicit** **action** **or** **preview** |

**Promotion** **paths** **(draft** **→** **review** **→** **export**/**send**)** **SHALL** **remain** **explicit** **actions**, **not** **silent** **model** **side** **effects**.

---

## BOOK workflow (ADD-002 §10–§10.11) — gates as surfaces

| Gate | Surface idea |
|------|----------------|
| **TOC** **/** **chapter** **approval** | **Review** **canvas** **with** **approve**/**revise** **per** **section** |
| **Final** **assembly** | **Explicit** **“assemble”** **or** **“freeze** **structure”** **before** **export** |
| **Premium** **(§10.11)** | **Gated** **actions** **(images**, **layout**, **publish-ready** **package**)** **with** **entitlement** **disclosure** |

---

## Composition plane (ADD-003) — states and gates

| Concept | Surface idea |
|---------|----------------|
| **Composition** **contract** | **Role**/**intent**/**outcome** **captured** **before** **or** **during** **draft** (**wizard** **or** **compact** **confirm**) |
| **Knowledge** **basis** | **“Grounding** **required”** **/** **“Discovery** **suggested”** **banners**; **block** **or** **scaffold** **when** **insufficient** |
| **Measurement** **confirmation** | **Prompt** **for** **method**/**unit**/**basis** **when** **claims** **are** **material** |
| **Professional** **disclosure** (**§9.4**)** | **Mandatory** **label** **and** **export** **preservation** |
| **Originality**/**overlap** (**§19**) | **Status** **badges** (e.g. **review** **required**, **blocked**) **before** **send**/**publish** |
| **Reference** **adherence** (**§20**)** | **Sliders**/**presets** **(1**–**10** **or** **structure**/**style** **split**)** **labeled** **as** **layout**/**conformity**, **not** **temperature** |
| **Reference** **role** | **Picker** **for** **example** **vs** **template** **vs** **authority** |

---

## Implementation note

**Product** **repo:** **ai-os-voice-interface**. **Refresh** **product** **context** **before** **alignment** **reviews:** `py -3 scripts/generate_product_context_bundle.py` **(see** **[DEVELOPER.md](../DEVELOPER.md)****)**.

---

*End of AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001, version 1.0.0 (draft).*
