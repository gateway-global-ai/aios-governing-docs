---
amendment_id: AMD-001
title: Agent-Native CLI Design Patterns (Google CLI Article Analysis)
type: amendment_to_existing
status: ratified
source_material: sources/google_cli_article/impact_report.md
affected_documents:
  - { doc_id: "AIOS-SPEC-004", doc_title: "AIOS CLI Developer Experience Guide" }
  - { doc_id: "AIOS-SPEC-003", doc_title: "AIOS Agent Integration Protocol (AIP)" }
  - { doc_id: "AIOS-SPEC-005", doc_title: "AIOS Agent Integration Guide" }
created: 2026-03-30
author: DeepSeek
ratification_date: 2026-04-01
---

This is an excellent article that crystallizes a critical insight: **the CLI is no longer just a human interface—it’s an API for agents**. Your existing AIOS CLI design is already strong, but this article provides a set of practical patterns that can elevate it from “agent‑accessible” to “agent‑native.”

Below I’ve extracted the key principles from the article, compared them to your current design (based on your published documents), and provided specific recommendations to close any gaps.

---

## Comparison Matrix: Article Principles vs. Current AIOS CLI

| Article Principle | Your Current State | Gap / Opportunity |
|-------------------|--------------------|-------------------|
| **Structured discoverability** – Grouped help, three fields (short/long/example), “start here” hints. | Your CLI guide defines commands but doesn’t specify a help hierarchy or `AGENTS.md`. | Help output can be more structured; an `AGENTS.md` file can teach agents how to use the CLI. |
| **`--json` on everything** – Every data‑producing command supports machine‑readable output. | Your CLI uses `aios test --shadow-mode` returning an `ExecutionViolationLog`, but not all commands have a `--json` flag. | Add `--json` to `validate`, `registry list`, and other non‑test commands. |
| **Audience detection** – `NO_COLOR`, `[APP]_NO_TUI`, pipe detection to skip interactive UI. | Your CLI Guide mentions “physical sandbox” but doesn’t specify environment‑based UI disabling. | Implement `NO_COLOR` and `AIOS_NO_TUI`; automatically disable TUI when stdout is piped. |
| **Non‑interactive fallbacks** – Commands with TUIs have a plain mode (JSON or text). | `aios test` has `--mock-external` but not a `--no-tui` equivalent. | Add `--no-tui` flag to `test` and future TUI commands. |
| **Context window protection** – Truncate large outputs, mask secrets by default. | Not addressed in current docs. | Add truncation and redaction defaults; require `--full` for raw payloads. |
| **Pre‑sorted output** – Most critical items appear first. | Not explicitly required. | Mandate that list commands sort by severity/relevance. |
| **Stateless design** – Use reference IDs (`--task-id`), no interactive loops. | Your CLI is stateless by design (delegates state to Kernel), but the AIP could emphasize this more. | Add to AIP mandate: “Never hold state; always use reference IDs.” |
| **XDG config & named environments** – Config in `~/.config/aios/`, support `--env`. | Not yet specified. | Define XDG config location; add `--env` for multiple environments. |
| **Error guidance** – Contextual hints, fail fast, deterministic exit codes. | Not specified in current docs. | Define exit codes; add hint lines to errors. |
| **Flag consistency** – `-o` always means the same thing. | Not yet codified. | Add a flag style guide. |
| **Visual design (semantic colors)** – Your UI_PHILOSOPHY.md aligns perfectly. | Already implemented in Beads CLI. | Adopt same tokens for `aios` CLI. |
| **Versioning & lifecycle** – `--version`, graceful SIGINT, actor tracking. | Not yet specified. | Add to CLI Guide. |
| **AGENTS.md file** – Teach agents the rules of engagement. | Not yet present. | Add root `AGENTS.md` with the AIOS Agent Mandate (from AIP) and CLI usage patterns. |

---

## Recommended Edits & Additions

### 1. Update `AIOS CLI Developer Experience Guide`

Add the following sections to align with the article:

- **Help & Discoverability** – Specify that `--help` output groups commands by category (e.g., `Kit Management:`, `Testing:`, `Registry:`). Each command must have short, long, and example fields.
- **`--json` Flag** – Every command that outputs data (including `validate`, `registry list`, `test`) must support `--json` returning structured JSON (or NDJSON for streaming).
- **Environment Detection** – Honor `NO_COLOR` and `AIOS_NO_TUI`. When stdout is not a TTY, automatically disable interactive prompts and spinners.
- **Non‑Interactive Mode** – Add `--no-tui` flag to force plain output even when stdout is a TTY.
- **Output Truncation** – By default, truncate large text blobs and mask secrets (API keys, tokens). Add `--full` to return raw payloads.
- **Sorted Output** – For list commands, define a sorting rule (e.g., by priority, then by name) so the most critical items appear first.
- **XDG Config** – Config file location: `~/.config/aios/config.yaml`. Support `--env` to switch between named environments (local, staging, prod).
- **Exit Codes** – Define:
  - `0`: Success
  - `1`: General error
  - `2`: Invalid usage / bad flags
  - `3`: Connection / auth failure
- **Error Hints** – On failure, include a `Hint:` line with a recommended corrective command.
- **Flag Consistency** – Adopt a style guide (e.g., `-o` for output directory, `-f` for file, `-e` for environment).

### 2. Create `AGENTS.md` at Repository Root

This file should contain:

- The **AIOS Agent Mandate** from the AIP (copied verbatim).
- A brief explanation of the CLI’s dual‑audience design.
- Examples of how to call each command with `--json` for machine use.
- A note that `NO_COLOR` and `AIOS_NO_TUI` are respected.

### 3. Update `AIOS Agent Integration Protocol (AIP)`

Add to the Agent Mandate:

- *“Always use `--json` when you need to parse output programmatically.”*
- *“If a command fails, read the `Hint:` line and attempt the suggested fix.”*
- *“Do not hold state; use reference IDs (e.g., `--kit-id`) for subsequent calls.”*

### 4. Add a UI Philosophy Document for the CLI

Your existing `UI_PHILOSOPHY.md` from Beads is excellent. Adopt it verbatim for the `aios` CLI, with one addition: add a note about **`--no-tui` and environment detection** as part of the “Respect Cognitive Load” principle.

### 5. Enhance the Technical Manifesto (Optional)

Add a brief section on “Agent‑First Design” stating that all developer tooling (CLI, MCP tools) is designed to be consumed by both humans and AI agents, and that the dual‑output pattern (`--json` vs. TUI) is a constitutional requirement for all future tooling.

---

## What This Adds to Your Plan

| Before | After |
|--------|-------|
| CLI works for humans; agents use MCP tools. | CLI works natively for agents via `--json` and environment detection. |
| Help is functional but not structured for agents. | Help is categorized, with short/long/example fields that agents can parse. |
| No explicit guidance for agents in the repo. | `AGENTS.md` teaches agents the rules of engagement. |
| Config location unspecified. | XDG‑compliant config with `--env` for multi‑environment workflows. |
| Error messages are informative but lack hints. | Errors include a `Hint:` line for self‑correction. |
| No exit code standard. | Deterministic exit codes enable automation. |
| Output may be verbose. | Truncation and redaction protect agent context windows. |

---

## Next Steps

1. **Adopt the UI_PHILOSOPHY.md** as the official style guide for the `aios` CLI. It already aligns perfectly with the article’s visual design principles.
2. **Update the CLI Guide** with the additions above (structured help, `--json`, environment detection, exit codes, etc.).
3. **Create `AGENTS.md`** in the root of the AIOS repository, containing the Agent Mandate and usage patterns.
4. **Enhance the AIP** to include the new mandates (use `--json`, follow hints, stateless design).

Would you like me to draft the updated sections for the CLI Guide and the `AGENTS.md` file, or would you prefer to proceed with the next document in your roadmap?
