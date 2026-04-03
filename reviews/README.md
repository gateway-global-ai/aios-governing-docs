# AIOS Peer Review Archive

This directory contains all peer reviews of AIOS governing documents, organized by document and review round.

---

## Review Process: The 5-Stage Document Lifecycle

Every governing document follows a mandatory 5-stage pipeline:

```
Stage 1: DRAFT          DeepSeek authors the document
    |
Stage 2: ROUND 1        OpenAI + Gemini independently review
    |
Stage 3: REVISION       DeepSeek revises, producing a revision log
    |
Stage 4: ROUND 2        All 3 models review the revised document
    |
Stage 5: RATIFICATION   2+ approvals = ratified; 2+ major_revision = back to Stage 3
```

### Stage Gates

- **Draft -> Round 1:** Document exists and passes basic structural validation
- **Round 1 -> Revision:** At least 2 reviews received with 11-dimension scores
- **Revision -> Round 2:** Revised document + revision log exist; revision log addresses every recommendation
- **Round 2 -> Ratification:** At least 2 of 3 reviewers issue `approved` or `approved_with_changes`
- **Ratification -> Back to Stage 3:** 2+ reviewers issue `major_revision_required`

---

## Folder Structure

```
reviews/
├── {document_slug}/
│   ├── round_1/
│   │   ├── review_001_{model}.md
│   │   └── review_002_{model}.md
│   ├── round_2/
│   │   ├── review_003_{model}.md
│   │   ├── review_004_{model}.md
│   │   └── review_005_{model}.md
│   └── revision_log.md
```

---

## Grading System

All reviews use the 11-dimension rubric defined in `templates/grading_rubric.md`:

1. Cross-Document Consistency
2. Business Model Alignment
3. Legal Enforceability
4. Architectural Fidelity
5. Completeness
6. Conflict Freedom
7. Practical Operability
8. Style & Clarity
9. Developer Synchrony
10. Platform Economics Synchrony
11. Friction Factor

Each dimension is scored 1-5. Disposition is determined by scores:
- **Approved:** No dimension below 4, composite >= 4.0
- **Approved with changes:** No dimension below 3, composite >= 3.5
- **Major revision required:** Any dimension at 1, or 2+ at 2, or composite below 3.0

---

## Running Reviews

```bash
cd scripts/

# Round 1 review (OpenAI + Gemini)
python peer_review.py core/technical_manifesto.md --round 1

# Revision (DeepSeek)
python revise_document.py core/technical_manifesto.md

# Round 2 review (all 3 models)
python peer_review.py core/technical_manifesto.md --round 2

# Or run the full lifecycle
python lifecycle.py core/technical_manifesto.md
```

---

## Review History

### Technical Manifesto
- Round 1: `review_001_deepseek.md` (pre-automation, migrated from root)

### Governance Constitution
- Round 1: `review_001_deepseek.md`, `review_002_deepseek.md` (pre-automation, migrated from root)

### Master Platform Operating Agreement
- Round 1: `review_001_deepseek.md` (pre-automation, migrated from root)
