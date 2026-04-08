---
document_id: AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001
version: 1.0.0
status: draft
category: reference
title: Composition control plane — architecture memo (bounded domains and addendum seams)
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008
  - doc_id: AMD-2026-008-ADD-001
  - doc_id: AMD-2026-008-ADD-002
  - doc_id: AMD-2026-008-ADD-003
  - doc_id: AIOS-COMPOSITION-CONTROL-RD-NOTES-001
  - doc_id: AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001
note: Informative partitioning memo; not ratified law.
amendment_history:
  - version: 1.0.0
    date: 2026-04-10
    summary: Initial architect backfill — domain boundaries, dependency map, OUT scope, ADD-003 refinement hooks.
---

# Composition control plane — architecture memo (001)

## Purpose

This memo **backfills** the **architect** **layer** that **should** **precede** **or** **accompany** **heavy** **addendum** **drafting**: **where** **each** **concern** **lives**, **what** **depends** **on** **what**, and **what** **SHALL** **not** **bleed** **across** **seams**. It **informs** **revision** **of** **[ADD-001](../amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)**, **[ADD-002](../amendments/AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)**, **[ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** **without** **replacing** **them**.

**Inputs:** **[AIOS-COMPOSITION-CONTROL-RD-NOTES-001](AIOS-COMPOSITION-CONTROL-RD-NOTES-001.md)**. **Outputs** **for** **product:** **[AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001](AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001.md)**.

---

## Bounded domains

| Domain | Owns | Does not own |
|--------|------|----------------|
| **Shell navigation** | **START_HERE**, **CONTINUE**, **CHOOSE**, **SINGLE_INPUT**, **MULTI_INPUT**; **alert**/**continue**/**choose** primitives | **Composition** **class** **labels**; **EMAIL**/**DOCUMENT** **body** **schema** **detail** |
| **Output depth** | **RESPONSE** → **BOOK** **ladder**; **promotion** **rules** | **Intent** **primitive** **routing** (**AIOS-SPEC-009**); **Workspace** **MCP** **scopes** (**AIOS-SPEC-007**) |
| **Shell voice** | **VC0**–**VC5** **obligations** | **Acoustic**/**engine** **TTS** **selection** |
| **Packaging** | **TXT**/**MD**/**PDF**/**DOCX**/**JSON**/**HTML** **classes** | **Renderer** **implementation**; **font**/**template** **assets** |
| **BOOK** **workflow** | **B0**–**B9** **phases**, **gates**, **premium** **vs** **base** (**§10**/**§10.11**) | **Payment** **provider** **APIs** (**MPOA** **tier** **facts**) |
| **Composition** **classes** | **Family** + **class** **identifiers**; **action** **semantics** (**draft**/send/**publish**) | **Provider** **APIs** (**Gmail**/**Calendar** **schemas**) |
| **Composition** **contract** | **role**/**intent**/**outcome** **for** **composed** **artifacts** | **User** **editable** **field** **UI** **layout** |
| **Language** | **L0**–**L3**, **authoritative** **language**, **translation** **mode** | **MT** **engine** **choice** |
| **Measurement** | **method**/**unit**/**basis**/**precision** **for** **quantified** **claims** | **Survey** **hardware**; **calculation** **libraries** |
| **Knowledge** **basis** | **sufficiency**; **discovery-before-create**; **creation** **mode** | **Index** **topology**; **RAG** **pipeline** |
| **Originality**/**source** **boundary** | **Overlap**/**extraction** **risk**; **publish**/**send** **gate** | **Legal** **determination** **of** **infringement** |
| **Reference-guided** **composition** | **Template** **vs** **reference** **vs** **authority**; **R1**–**R3**; **adherence** **1**–**10**; **innovation** **mode** | **Copyright** **registration**; **licensing** **negotiation** |

---

## Dependency map (read order)

```text
ADD-001 (navigation)     ──►  ADD-002 (depth / VC / packaging / BOOK)
                                      │
                                      ▼
ADD-003 (composition plane, contracts, KB, originality, reference adherence)
        │
        ├──► AIOS-SPEC-009 (lanes, intent model) — parent AMD-2026-008 §3.1
        ├──► MPOA (commercial / liability)
        └──► AIOS-SPEC-007 (Workspace) where workspace intents touch export/send
```

---

## Addendum seam rules (normative for authors, not for runtime)

1. **ADD-002** **SHALL** **not** **define** **composition** **class** **taxonomies**; **ADD-003** **owns** **those**.
2. **ADD-003** **SHALL** **not** **redefine** **VC** **classes** **or** **output** **depth** **ladder**; **cross-ref** **ADD-002**.
3. **Gates** **stack**: **knowledge** **basis** (**§18**) **before** **substantive** **drafting**; **reference** **disposition** (**§20**) **when** **references** **apply**; **originality** (**§19**) **before** **external** **publish**/**send** **when** **policy** **requires** **—** **order** **is** **in** **ADD-003** **§18.11**.

---

## OUT of addenda (belongs elsewhere)

| Topic | Proper home |
|-------|-------------|
| **Retrieval** **backend**, **chunking**, **RAG** | **Product**/**operations**; **AMD-2026-009** **retrieval** **neutrality** **where** **relevant** |
| **API** **schemas** (**SMTP**, **Calendar**) | **Integrations**/**specs**; **not** **ADD-003** |
| **Visual** **brand** **kits** | **Product**/**design** |

---

## ADD-003 refinement hooks (use when revising)

- **Tighten** **cross-references** **so** **each** **§** **has** **one** **obvious** **“home”** **axis** **from** **§6** **twelve-axis** **table**.
- **Consider** **moving** **long** **informative** **JSON** **examples** **to** **an** **annex** **file** **if** **the** **main** **file** **remains** **hard** **to** **review**.
- **Align** **reference** **adherence** **language** **with** **§19** **everywhere** **“maximum”** **structure** **conformity** **is** **mentioned**.

---

*End of AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001, version 1.0.0 (draft).*
