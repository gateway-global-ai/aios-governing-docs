# External peer review — ADD-004 audit package (2026-04-08)

This folder holds **handoff material** for an **external reviewer** who was not in the authoring session. It documents **what changed**, **why**, how that maps to **`CHANGELOG.md`**, and a **complete file manifest** for the AMD-2026-008-ADD-004 workstream.

## How to use this package

1. Read **`AUDIT_AND_CHANGE_HISTORY.md`** first — it is the narrative audit (requirements → logic → edits).
2. Use **`FILE_MANIFEST.md`** to locate every path and its role (doctrine, packet, tooling, registry).
3. Compare against **`CHANGELOG_EXCERPT_ADD004.md`** (verbatim excerpt from repo root **`CHANGELOG.md`** for ADD-004–related bullets under **`[Unreleased]`**).
4. In a checkout of **`aios-governing-docs`**, run **`git status`** and **`git diff`** from the repository root to see **uncommitted** edits relative to your baseline; this package was prepared while ADD-004 paths were still **partially untracked** (new tree) or **modified** (tracked files).

## Canonical subject matter

- **Amendment:** `amendments/AMD-2026-008-ADD-004-pre-human-browser-review-and-visual-proof-gate.md` — pre-human **browser-visible** proof gate for UI-affecting work.
- **Process anchors:** **[AMD-2026-005](../../../amendments/AMD-2026-005.md)** peer-review thresholds; **[AIOS-AMD-PLAN-001](../../../reference/implementation/AIOS-AMD-PRE-RATIFICATION-PLANNING-LIFECYCLE.md)** planning lifecycle.

## Bottom-line posture (intended)

**ADD-004 is artifact-healthy and revision-ready; AMD-2026-005 review gate failed at assessed `draft` `0.2.0` — revise toward `0.3.0` and Round 2, not ratify. The committee packet is closed as procedural supersession by Round 1 findings, not as a fix for packet integrity.**

---

*Package assembled for external peer review — 2026-04-08.*
