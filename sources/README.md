# AIOS Source Material Archive

This directory contains external source material that has been analyzed against the AIOS governance framework, along with the impact reports produced by that analysis.

---

## How It Works

When you encounter an article, research report, or external reference that could inform the AIOS governance documents, you run it through the source analysis pipeline:

```bash
cd scripts/
python analyze_source.py path/to/article.md --name descriptive_name
```

The pipeline:
1. Preserves the original source verbatim in `sources/{name}/source.md`
2. Sends it to all 3 models (DeepSeek, OpenAI, Gemini) with full governing context
3. Each model produces an independent impact report
4. Reports are saved as `impact_report_{model}.md`

---

## Folder Structure

```
sources/{source_name}/
├── source.md                      # Original material (never modified)
├── impact_report_deepseek.md      # Analysis from DeepSeek
├── impact_report_openai.md        # Analysis from OpenAI
├── impact_report_gemini.md        # Analysis from Gemini
└── impact_report_consolidated.md  # Merged recommendations (if generated)
```

---

## Analyzed Sources

### token_trap
- **Type:** Research / Market Data
- **Source:** "The Token Trap" — analysis of AI vendor economics vs. enterprise production gap
- **Key Insight:** Market validation of the AIOS governance thesis; identified financial circuit breakers and memory pointer patterns as potential new primitives
- **Affected Documents:** Technical Manifesto, MPOA, NodeContract spec, PolicyRecord spec

### clean_room
- **Type:** Design Standard / Technical Reference
- **Source:** Clean Room Extraction & Quarantine System — supply chain security pipeline
- **Key Insight:** Implements supply-chain integrity as a governed pipeline; recommended adding as a constitutional mandate in the Technical Manifesto
- **Affected Documents:** Technical Manifesto, Marketplace Terms, AIP, CLI Guide

### google_cli_article
- **Type:** External Article / Industry Analysis
- **Source:** Analysis of Google's CLI design principles for AI agent consumption
- **Key Insight:** CLI should be agent-native with `--json` output, structured help, environment detection, and deterministic exit codes
- **Affected Documents:** CLI Developer Guide, AIP, agents.md, Technical Manifesto
