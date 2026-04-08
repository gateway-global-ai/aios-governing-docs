---
document_id: AMD-2026-008-ADD-003-ANNEX-A
parent_amendment: AMD-2026-008
parent_addendum: AMD-2026-008-ADD-003
version: 1.0.0
status: draft
category: amendment_addendum_annex
title: ADD-003 Annex A — Informative composition and knowledge-basis examples
author: Gateway Global AIOS
created: 2026-04-10
last_updated: 2026-04-10
cross_references:
  - doc_id: AMD-2026-008-ADD-003
    title: Composition Control Plane for Messages, Invites, and Documents
  - doc_id: AMD-2026-008-ADD-002
    title: Verbose Grounding, Shell Voice Output Control, and Output Packaging
note: Informative JSON only; not normative. Depth/packaging labels refer to ADD-002 definitions.
---

# AMD-2026-008-ADD-003 Annex A — Informative examples

**Binding** **SHALL**/**MUST** **language** **remains** **in** **[AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md](AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md)**. **Field** **names** **below** **are** **illustrative** **serialization** **hints** **for** **products**.

**Depth** and **packaging** **strings** **in** **examples** **refer** **to** **[ADD-002](AMD-2026-008-ADD-002-verbose-grounding-shell-voice-output-and-output-packaging.md)** **§4** **and** **§7** **(not** **redefined** **here**)**.

---

## 1. Composition contract JSON (informative)

Moved from **ADD-003** **§5.7**.

```json
{
  "artifact_class": "ARTICLE",
  "role": "Founder",
  "intent": "Educate and persuade",
  "outcome": "Reader understands the AI OS position and joins early access",
  "audience": "operators and technical founders",
  "depth": "EXPLANATION",
  "packaging": "MD"
}
```

```json
{
  "artifact_class": "EMAIL",
  "role": "Executive Assistant",
  "intent": "Coordinate meeting scheduling",
  "outcome": "Recipient accepts one of the proposed meeting times",
  "audience": "external partner",
  "depth": "BRIEF",
  "action_mode": "DRAFT_ONLY"
}
```

---

## 2. Knowledge-basis / discovery JSON (informative)

Moved from **ADD-003** **§18.9**.

```json
{
  "artifact_class": "RESEARCH_REPORT",
  "knowledge_basis_required": true,
  "knowledge_sources": [
    "uploaded_files",
    "governing_docs",
    "current_web_sources"
  ],
  "knowledge_state": "partial",
  "discovery_required": true,
  "creation_mode": "scaffold_only"
}
```

---

*End of Annex A, version 1.0.0 (draft).*
