#!/usr/bin/env python3
"""
Emit one self-contained Markdown file for manual peer review (e.g. ChatGPT upload).

Includes: instructions, light rubric, primary amendment, and smart-context cross-references
(same bundle as peer_review.py --smart-context).

Usage:
  py -3 scripts/assemble_manual_review_packet.py
  py -3 scripts/assemble_manual_review_packet.py amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from context_assembler import BASE_DIR, read_file, read_relevant_context  # noqa: E402

DEFAULT_DOC = (
    "amendments/AMD-2026-008-ADD-003-composition-control-plane-messages-invites-documents.md"
)
RUBRIC_LIGHT = BASE_DIR / "templates" / "grading_rubric_light.md"
OUT_DIR = (
    BASE_DIR
    / "reviews"
    / "amd_2026_008_add_003_composition_control_plane_messages_invites_documents"
    / "round_1"
)


def _parse_front_matter(content: str) -> dict:
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                pass
    return {}


def build_packet(doc_path: str) -> tuple[str, str]:
    rel = doc_path.replace("\\", "/")
    primary = read_file(BASE_DIR / rel)
    meta = _parse_front_matter(primary)
    version = meta.get("version", "unknown")
    doc_id = meta.get("document_id", rel)
    rubric = read_file(RUBRIC_LIGHT)

    ctx = read_relevant_context(rel)
    ctx_lines = []
    for cid in sorted(ctx.keys()):
        ctx_lines.append(f"\n\n---\n\n## Cross-reference bundle: `{cid}`\n\n")
        ctx_lines.append(ctx[cid])

    instructions = f"""# Manual peer review packet — **{doc_id}** **`draft` `{version}`**

## How to use this file

1. **Upload this entire file** to ChatGPT (or another reviewer) as a single attachment.
2. Ask the model to follow **Round 1**, **light rubric**, **editorial + governance** focus (same role as automated OpenAI in `peer_review.py`).
3. **Output** must be **paste-back ready** for the repo: **YAML front matter** (see template below) + **scorecard table** + **short narrative**.

## Reviewer focus (editorial / cross-document coherence)

- Check cross-references and seams (**ADD-001**, **ADD-002**, **MPOA**, **OPS-020** where bundled).
- Terminology and **SHALL**/**MUST** discipline; ambiguity; density where it blocks understanding.
- You still **score every dimension** in the light rubric below.

## Output template (copy and fill)

```yaml
---
review_id: REV-AMD-2026-008-ADD-003-MANUAL-002
document_reviewed: AMD-2026-008-ADD-003
document_version: {version}
reviewer: OpenAI
review_source: manual_chatgpt
review_date: YYYY-MM-DD
review_round: 1
review_type: editorial
disposition: approved_with_changes | major_revision_required | approved
composite_score: 0.0
---
```

Then: **`## Grading Scorecard (light rubric)`** table (5 dimensions + composite mean), **`## Overall assessment`**, **`## Top actions`** (if any).

**Gate context (informational):** [AMD-2026-005](https://github.com/gateway-global-ai/aios-governing-docs/blob/main/amendments/AMD-2026-005.md) expects composite **≥ 3.5** and **no dimension below 3** for triangulated review.

---

## Grading rubric (light)

{rubric}

---

## Primary document — **{doc_id}** **`{version}`**

{primary}
{"".join(ctx_lines)}
"""
    return instructions, version


def main() -> None:
    ap = argparse.ArgumentParser(description="Assemble manual peer review Markdown packet.")
    ap.add_argument("document", nargs="?", default=DEFAULT_DOC, help="Path under governing_docs/")
    ap.add_argument(
        "-o",
        "--output",
        help="Output .md path (default: reviews/.../MANUAL_PEER_REVIEW_PACKET_<version>.md)",
    )
    args = ap.parse_args()

    packet, version = build_packet(args.document)
    out = Path(args.output) if args.output else OUT_DIR / f"MANUAL_PEER_REVIEW_PACKET_v{version}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(packet, encoding="utf-8")
    print(f"Wrote {out} ({len(packet):,} chars)")


if __name__ == "__main__":
    main()
