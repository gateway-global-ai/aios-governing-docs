# Agent corpus (generated)

Run from repository root:

```bash
py -3 scripts/build_agent_kb.py
```

This writes **`government_and_reports_bundle.md`** and **`build_manifest.json`** (gitignored). The Ollama planning agents read that bundle plus planning templates — see [`../README.md`](../README.md).
