---
document_id: AIOS-COMPOSITION-CONTROL-RD-NOTES-001
version: 1.0.0
status: draft
category: reference
title: Composition control plane — R&D and knowledge capture (AMD-2026-008 addendum track)
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008
  - doc_id: AMD-2026-008-ADD-001
  - doc_id: AMD-2026-008-ADD-002
  - doc_id: AMD-2026-008-ADD-003
  - doc_id: AIOS-AMD-PLAN-001
  - doc_id: AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001
  - doc_id: AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001
note: Informative knowledge capture before or alongside doctrine refinement; not ratified law.
amendment_history:
  - version: 1.0.0
    date: 2026-04-10
    summary: Initial capture — process defect diagnosis; clustered principles; open questions; points to architect and surface memos.
---

# Composition control plane — R&D and knowledge capture (001)

## Purpose

This document **captures** founder/operator **insights**, **constraints**, and **open questions** that informed **AMD-2026-008-ADD-001**–**ADD-003**. It is **informative** **knowledge**, **not** **normative** **doctrine**. Use it to **ground** revisions to the addenda and to **avoid** repeating the process gap: **jumping** from **raw** **R&D** **directly** to **draft** **amendments** **without** **architect** **partitioning**, **UI**/**shell** **grounding**, or **knowledge-basis** **normalization** (see **[AIOS-AMD-PLAN-001](AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** for the **optional** **full** **planning** **stack**).

**Related:** **[AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001](AIOS-COMPOSITION-CONTROL-ARCHITECTURE-MEMO-001.md)** (bounded domains and addendum seams), **[AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001](AIOS-SHELL-COMPOSITION-SURFACE-MEMO-001.md)** (surface grammar and states).

---

## Process defect (what was skipped)

| Layer | Intended role | Effect when skipped |
|-------|----------------|----------------------|
| **Knowledge capture** (this note) | Separate **principles** from **implementation** and **open** **questions** | Doctrine mixed with undigested R&D |
| **Architect synthesis** | **Partition** **control-plane** **domains**; **split**/**merge** **recommendations** | **Bundling** **pressure** and **ADD-003** **sprawl** |
| **UI/shell synthesis** | **Visible** **primitives**, **states**, **gates** **grounded** **in** **shell** **patterns** | **Abstract** **rules** **or** **orphan** **UI** **phrasing** |
| **Knowledge-basis sufficiency** | **What** **exists** **in** **specs**/**KB** **vs** **assumption** | Reviewers **and** **runtime** **inherit** **hidden** **assumptions** |

**Not** a failure of **ideas** — a **compression** of **stages** that **[AMD-2026-005](../amendments/AMD-2026-005.md)** **peer** **review** **alone** **cannot** **fully** **substitute** **for**.

---

## Principles (clustered)

- **Composition** is **not** **freeform** **length**; it is **class** + **contract** + **action** **semantics**.
- **Navigation** (**START** **HERE**, **continue**, **choose**, **input** **classes**) is **shell** **grammar**, **not** **model** **style**.
- **Output** **depth** and **voice** **controls** (**VC0**–**VC5**) **SHALL** be **shell** **obligations**, **not** **optional** **skills**.
- **Knowledge** **basis** and **discovery** **before** **creation** **SHALL** **govern** **when** **drafting** **outruns** **grounding**.
- **Originality** and **source-boundary** **gate** **SHALL** **reduce** **reproduction** **risk** **without** **claiming** **absolute** **copyright** **outcomes**.
- **Reference** **documents** **SHALL** **guide** **shape** **and** **spirit** **(reference** **adherence**, **not** **model** **temperature**)** **without** **authorizing** **wholesale** **copying**.
- **Professional** **drafts** **SHALL** **carry** **disclosure** **and** **review** **posture** **per** **policy** (**§9.4** **line**).

---

## Constraints and risks

- **Risk:** **Treating** **retrieval** **as** **permission** **to** **reproduce** **KB** **or** **source** **text**.
- **Risk:** **Confusing** **reference** **guidance** **with** **verbatim** **copying** **or** **with** **authoritative** **court**/**regulator** **forms** **without** **explicit** **role**.
- **Risk:** **Measurement** **claims** **without** **method**/**unit**/**basis** **discipline**.
- **Risk:** **Publishing**/**send**/**export** **without** **stacking** **gates** (**originality**, **professional**, **premium** **BOOK** paths).
- **Constraint:** **Parent** **[AMD-2026-008](../amendments/AMD-2026-008.md)** **is** **ratified**; **addenda** **extend** **composition**/**voice**/**surface** **doctrine** **without** **re‑opening** **§3.1** **runtime** **package** **unless** **a** **future** **amendment** **says** **so**.

---

## Control requirements (candidate themes)

| Theme | Where it landed (addendum) |
|-------|---------------------------|
| **Navigation** **classes** | **[ADD-001](../amendments/AMD-2026-008-ADD-001-base-shell-navigation-primitives-and-start-here-control.md)** |
| **Depth**/**VC**/**packaging**/**BOOK** | **[ADD-002](../amendments/AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** |
| **Composition** **classes**, **contract**, **language**, **measurement**, **KB**, **originality**, **reference** **adherence** | **[ADD-003](../amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)** |

---

## Open questions (for next doctrine pass)

1. **Split** **vs** **trim:** **Should** **any** **ADD-003** **sections** **move** **to** **a** **separate** **addendum** **or** **SPEC** **annex** **to** **reduce** **reader** **load**?
2. **Product** **binding:** **Which** **fields** **are** **MUST** **implement** **in** **shell** **vs** **MAY** **map** **for** **v1**?
3. **KB** **pipeline:** **What** **is** **normative** **here** **vs** **in** `operations`/retrieval **implementation** **docs**?
4. **Overlap** **with** **AIOS-SPEC-009** **§16**/**§17** — **confirm** **no** **dual** **source** **of** **truth** **for** **lanes** **vs** **composition** **plane**.

---

## Maintenance

- **Revise** **this** **note** **when** **operator** **knowledge** **materially** **changes** **or** **after** **architect**/**surface** **memos** **freeze** **a** **new** **partitioning**.

---

*End of AIOS-COMPOSITION-CONTROL-RD-NOTES-001, version 1.0.0 (draft).*
