## Discovery scope  
The discovery scope for `AMD-2026-016` is governed by the `DISCOVERY_SCOPE.yaml` artifact, which declares the following:  
- **Target document**: `AMD-2026-016.md`  
- **Required taxonomy classes**: `target_authority`, `cross_document_authority`, `taxonomy_and_process_authority`  
- **Optional taxonomy classes**: `implementation_authority`, `review_evidence`  
- **Prohibited source classes**: `raw_chat_transcripts`, `unpublished_private_notes`, `undeclared_external_web_sources`, `discussion_without_repo_conversion`  
- **Allow runtime evidence**: `false`  
- **Require review evidence**: `true`  

---

## Resolved taxonomy classes  
The required taxonomy classes are resolved as follows:  
- **`target_authority`**: The amendment itself, `AMD-2026-016.md`, is the primary source of authority.  
- **`cross_document_authority`**: Directly constraining documents include `AMD-2026-007.md` (shell-state routing), `AMD-2026-012.md` (shell authority), `AIOS-SPEC-002.md` (PolicyRecord schema), and `AIOS-SPEC-009.md` (intent lifecycle).  
- **`taxonomy_and_process_authority`**: The `AIOS-TAXONOMY-FIRST-DISCOVERY-CONTRACT-001.md` and `AIOS-REPO-TAXONOMY-001.md` provide the framework for governance and implementation.  

---

## Direct authority anchors  
The following artifacts directly constrain `AMD-2026-016`:  
1. **`AMD-2026-007.md`** (shell-state routing and separation of powers)  
2. **`AMD-2026-012.md`** (shell authority and session boundaries)  
3. **`AIOS-SPEC-002.md`** (PolicyRecord schema and evaluation context)  
4. **`AIOS-SPEC-009.md`** (intent lifecycle, execution envelopes, and actor definitions)  

These documents define the governance boundaries, role binding, and audit requirements that `AMD-2026-016` must align with.  

---

## Supporting authority anchors  
The following artifacts provide implementation/process guidance:  
1. **`AIOS-TAXONOMY-FIRST-DISCOVERY-CONTRACT-001.md`** (taxonomic structure for governance)  
2. **`AIOS-REPO-TAXONOMY-001.md`** (repository classification for governance artifacts)  
3. **`AIOS-SPEC-002.md`** (schema for policy evaluation and audit linkage)  
4. **`AIOS-SPEC-009.md`** (intent execution and principal attribution rules)  

These anchors clarify how non-human principals integrate with existing systems and define the technical framework for implementation.  

---

## Review evidence required for this lane  
The following review evidence is required for this lane:  
1. **`REV-AMD-2026-016-001.md`** (peer review from DeepSeek, OpenAI, Gemini, and Claude)  
2. **`AIOS-AMD-PLAN-001.md`** (amendment pre-ratification planning lifecycle)  
3. **`AIOS-SYSTEMS-AND-PLANNING-MANUAL-001.md`** (planner/knowledge-base restoration guidance)  

These reviews provide critical feedback on enforceability, implementation gaps, and cross-document consistency.  

---

## Excluded or deferred source classes  
The following source classes are excluded or deferred:  
- **`raw_chat_transcripts`**: Not a formal governance artifact.  
- **`unpublished_private_notes`**: Not part of the ratified knowledge base.  
- **`undeclared_external_web_sources`**: Cannot be validated without formal declaration.  
- **`discussion_without_repo_conversion`**: Does not meet the threshold for authoritative governance.  

---

## Recommended discovered packet  
The downstream research and drafting lanes should consume the following discovered packet:  
1. **`AMD-2026-016.md`** (target document)  
2. **`AMD-2026-007.md`**, **`AMD-2026-012.md`**, **`AIOS-SPEC-002.md`**, **`AIOS-SPEC-009.md`** (direct authority anchors)  
3. **`AIOS-TAXONOMY-FIRST-DISCOVERY-CONTRACT-001.md`**, **`AIOS-REPO-TAXONOMY-001.md`** (supporting implementation anchors)  
4. **`REV-AMD-2026-016-001.md`** (review evidence)  

This packet provides a complete foundation for aligning the amendment with existing governance structures, resolving implementation gaps, and ensuring enforceability.
