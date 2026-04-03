# Action plan synthesis (from impact reports)

You merge triangulated impact analyses into one **actionable, ordered plan** for humans to approve before execution.

## Inputs

### Amendment / source id
{{SOURCE_NAME}}

### Original source material (summary context)
{{SOURCE_EXCERPT}}

### Impact report — DeepSeek
{{REPORT_DEEPSEEK}}

### Impact report — OpenAI
{{REPORT_OPENAI}}

### Impact report — Gemini
{{REPORT_GEMINI}}

### Document registry (IDs and paths)
{{DOCUMENT_REGISTRY_EXCERPT}}

---

## Task

1. Identify **consensus** recommendations across the three reports and **notable conflicts** (call them out in `merge_notes`).
2. Produce **8–20** concrete actions, ordered by dependency (foundational docs first).
3. Each action must map to governance work: document edits, registry refresh, schema extraction, or explicit manual steps.

## Output — JSON only

Return **a single JSON object** (no markdown fences) with this exact shape:

```json
{
  "version": 1,
  "source_name": "{{SOURCE_NAME}}",
  "merge_notes": ["string"],
  "actions": [
    {
      "id": "act-001",
      "title": "short imperative title",
      "description": "what to do and why",
      "document_id": "AIOS-CORE-001 or empty string if not doc-specific",
      "target_path": "relative/path/from/governing_docs root or empty",
      "priority": "critical|high|medium|low",
      "status": "proposed",
      "execution_kind": "manual|registry_regenerate|schema_extract",
      "dependencies": ["act-000"]
    }
  ]
}
```

Rules:
- `id` must be `act-` + zero-padded three-digit number.
- `status` must always be `"proposed"` for new synthesis.
- `execution_kind`:
  - `manual` — text edits to markdown / legal review (human or revise_document flow).
  - `registry_regenerate` — safe to run `registry_generator.py` after doc changes.
  - `schema_extract` — run `schema_extractor.py` when NodeContract/PolicyRecord JSON embedded in specs change.
- Use empty `dependencies` when none.
