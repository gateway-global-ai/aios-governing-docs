# Review brief — AMD-2026-007 v0.2.0 (Round 1)

| Field | Value |
|-------|--------|
| **Document** | `amendments/AMD-2026-007.md` |
| **Version** | 0.2.0 |
| **Focus** | §11.9 *Shell state controls vs skills and voice parity*; **POL-SHELL-004**–**006**; alignment with §11 intent primitive and SPEC-009 domain model |
| **Rubric** | Full (11 dimensions) — `templates/grading_rubric.md` |
| **Round 1 models (engine default)** | OpenAI + Gemini — see `scripts/peer_review.py` `ROUND_1_MODELS` |
| **Gate (AMD-2026-005 §3)** | Composite **≥ 3.5**; **no dimension < 3** |

## Review questions (coordinator)

1. Is **shell-state control** vs **skill/tool** vs **workflow** defined crisply enough to implement and audit?
2. Is **voice parity** correctly **bounded** by **authority/policy** (operator-only paths)?
3. Are **engineering bootstrap** exceptions (**POL-SHELL-006**) narrow enough?
4. Does §11.9 stay **distinct** from **AIOS-SPEC-009** domain intent / execution chain?
5. Is the doctrine **architecture-defining** and **testable** (MUST/SHALL, policy IDs)?
6. Any **unintended overlap** with shell, intent, UI, or policy language elsewhere in the amendment?

## Automation (optional)

From repo root:

```bash
cd scripts
py -3 peer_review.py ../amendments/AMD-2026-007.md --round 1 --rubric full --smart-context
```

*(Requires model API configuration per `DEVELOPER.md`.)*

## Artifacts

| File | Role |
|------|------|
| `review_001_openai.md` | Round 1 — editorial / cross-document coherence |
| `review_002_gemini.md` | Round 1 — legal/compliance / binding language |
| `REVIEW_SYNTHESIS.md` | Triangulated summary + gate check vs **AMD-2026-005** |
| `RATIFICATION_GATE_REPORT.md` | Round 1 outcome vs **reviews/README.md** lifecycle |
