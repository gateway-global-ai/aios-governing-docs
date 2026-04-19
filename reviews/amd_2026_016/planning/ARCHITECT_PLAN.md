# Architect plan — `amd_2026_016` (draft)

**Date:** 2026-04-10  
**Knowledge packet:** `reviews/amd_2026_016/planning/KNOWLEDGE_PACKET.yaml`  
**Current state:** Draft phase with unresolved integration gaps between document lifecycle management and voice-control state persistence.  
**Intent:** Resolve conflicts between document access control rules and voice-lane provider switching, ensuring compliance with constitutional data sovereignty principles.  
**Desired outcome:** Unified governance framework for document-state persistence and voice-control configuration that prevents unauthorized state mutation across system boundaries.  
**Verifier:** TBD  

---

## 1. Executive summary

This lane addresses the systemic gap between document-state persistence mechanisms and voice-control configuration management. The core decision is to enforce strict ownership boundaries: document metadata and content must be governed by the document management system (DMS), while voice-lane configuration and provider state must reside in the voice control module. This separation prevents cross-domain state mutation and ensures compliance with constitutional data sovereignty principles. The solution requires creating a unified interface for document-state access control and voice-lane provider switching, with explicit permission boundaries to prevent unauthorized configuration changes.

---

## 2. Declared grounding

| Input class | Source path | Why it matters |
|-------------|-------------|----------------|
| Constitutional / philosophy root | `constitutional/philosophy/data_sovereignty.md` | Defines the foundational principle that data ownership must align with system boundaries. |
| Amendment under review | `amendments/amd_2026_016/proposal.md` | Requires explicit governance of document-state persistence and voice-control configuration. |
| Coupled implementation reference | `implementations/dms/document_schema.yaml` | Existing document-state schema defines ownership rules for content and metadata. |
| Coupled implementation reference | `implementations/voice_control/voice_lane.proto` | Voice-lane configuration schema defines provider-state ownership rules. |
| Product evidence, if required | `product/evidence/document_access_logs.csv` | Demonstrates current lack of integration between document-state and voice-control state. |

---

## 3. Schemas and data contracts

| Surface | Contract / schema | Status | Notes |
|---------|-------------------|--------|-------|
| Document State | [DocumentSchema](#document-schema) | Finalized | Document content and metadata are owned by the DMS. |
| Voice Lane Configuration | [VoiceControlSchema](#voice-control-schema) | Finalized | Provider-state is owned by the voice control module. |
| Access Control Policy | [AccessControlPolicy](#access-control-policy) | Finalized | Role-based access rules enforce separation of concerns. |

### Document Schema
```yaml
type: object
properties:
  document_id: string
  content: string
  metadata:
    owner: string
    creation_time: datetime
    last_modified: datetime
  status: enum['active', 'archived', 'deleted']
```

### Voice Control Schema
```yaml
type: object
properties:
  voice_lane: enum['gemini', 'whisper', 'ollama']
  provider: string
  configuration:
    language: string
    bitrate: integer
    encryption: boolean
  state: enum['active', 'degraded', 'disabled']
```

### Access Control Policy
```yaml
type: object
properties:
  document_access:
    owner: string
    permissions: enum['read', 'write', 'admin']
  voice_lane_access:
    owner: string
    permissions: enum['read', 'configure', 'admin']
```

---

## 4. Routes and decision flow

| From | To | Gate / rule | Notes |
|------|----|-------------|-------|
| User request | Document Management System | AccessControlPolicy validation | Ensures user has document-write permissions. |
| Document Management System | Voice Control Module | Cross-domain state mutation check | Prevents unauthorized voice-lane configuration changes. |
| Voice Control Module | System State Repository | State durability validation | Ensures voice-lane state is persisted in session-based cache. |
| System State Repository | User Feedback | Transaction commit | Confirms successful state persistence. |

---

## 5. Storage, state, and persistence

| State surface | Owner | Durability | Notes |
|---------------|-------|------------|-------|
| Document content | Document Management System | Append-only | Immutable records of document history. |
| Document metadata | Document Management System | Mutable | Last_modified timestamp updated on write. |
| Voice-lane configuration | Voice Control Module | Session-based | Persists only during active voice-lane sessions. |
| Provider-state | Voice Control Module | Volatile | Reset on system reboot unless explicitly saved. |

---

## 6. Gaps vs governing intent

| Gap | Governing source | Proposed resolution |
|-----|------------------|---------------------|
| Cross-domain state mutation | Constitutional data sovereignty | Enforce ownership boundaries via AccessControlPolicy. |
| Inconsistent state durability | Amendment proposal | Define separate durability rules for document-state and voice-lane state. |
| Lack of unified interface | Product evidence | Create shared API for document-state access and voice-lane configuration. |

---

## 7. Verification checklist

- [ ] Every claim is traceable to declared packet inputs.
- [ ] No lane-specific doctrine was inherited from another amendment lane.
- [ ] Schema, route, and storage sections reflect the actual target lane rather than a reused scaffold.
- [ ] Open questions are labeled explicitly rather than hidden in implied assumptions.
