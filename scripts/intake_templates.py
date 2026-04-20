#!/usr/bin/env python3
"""
Bootstrap non-doctrine scaffold files for amendment intake.
"""

from __future__ import annotations

from pathlib import Path

from intake_paths import BASE_DIR, IntakePaths

NEUTRAL_TEMPLATE_ROOT = BASE_DIR / "templates" / "governance_system"
PLANNING_TEMPLATE_SOURCE = NEUTRAL_TEMPLATE_ROOT
KERNEL_TEMPLATE_BRIEF = BASE_DIR / "templates" / "kernel_shadow_review_brief.md"
KERNEL_TEMPLATE_FINDINGS = BASE_DIR / "templates" / "kernel_shadow_findings.md"


def _copy_if_missing(src: Path, dest: Path) -> bool:
    if dest.exists():
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return True


def _sync_from_source(src: Path, dest: Path) -> bool:
    src_text = src.read_text(encoding="utf-8")
    if dest.exists():
        dest_text = dest.read_text(encoding="utf-8")
        if dest_text == src_text:
            return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(src_text, encoding="utf-8")
    return True


def _planning_template_mapping(paths: IntakePaths) -> dict[Path, Path]:
    if PLANNING_TEMPLATE_SOURCE.resolve() != NEUTRAL_TEMPLATE_ROOT.resolve():
        raise RuntimeError(
            "Planner template source must resolve to the neutral shared template root: "
            f"{NEUTRAL_TEMPLATE_ROOT}"
        )
    mapping = {
        PLANNING_TEMPLATE_SOURCE / "ARCHITECT_PLAN_TEMPLATE.md": paths.planning_dir / "ARCHITECT_PLAN_TEMPLATE.md",
        PLANNING_TEMPLATE_SOURCE / "UI_PLAN_TEMPLATE.md": paths.planning_dir / "UI_PLAN_TEMPLATE.md",
        PLANNING_TEMPLATE_SOURCE / "COMMITTEE_PACKET_TEMPLATE.md": paths.planning_dir / "COMMITTEE_PACKET_TEMPLATE.md",
    }
    for src in mapping:
        if not src.is_file():
            raise FileNotFoundError(f"Required neutral planning template missing: {src}")
    return mapping


def ensure_planning_templates(paths: IntakePaths) -> list[str]:
    created: list[str] = []
    mapping = _planning_template_mapping(paths)
    for src, dest in mapping.items():
        if _sync_from_source(src, dest):
            created.append(dest.relative_to(paths.base_dir).as_posix())
    return created


def ensure_committee_packet(paths: IntakePaths) -> list[str]:
    created = ensure_planning_templates(paths)
    committee_packet = paths.planning_dir / "COMMITTEE_PACKET.md"
    template = paths.planning_dir / "COMMITTEE_PACKET_TEMPLATE.md"
    if not committee_packet.exists():
        committee_packet.write_text(template.read_text(encoding="utf-8"), encoding="utf-8")
        created.append(committee_packet.relative_to(paths.base_dir).as_posix())
    return created


def ensure_kernel_files(paths: IntakePaths) -> list[str]:
    created: list[str] = []
    brief = paths.kernel_dir / "KERNEL_SHADOW_BRIEF.md"
    findings = paths.kernel_dir / "KERNEL_SHADOW_FINDINGS.md"
    if _copy_if_missing(KERNEL_TEMPLATE_BRIEF, brief):
        created.append(brief.relative_to(paths.base_dir).as_posix())
    if _copy_if_missing(KERNEL_TEMPLATE_FINDINGS, findings):
        created.append(findings.relative_to(paths.base_dir).as_posix())
    return created


def ensure_ratification_handoff(paths: IntakePaths) -> list[str]:
    created: list[str] = []
    paths.ratification_dir.mkdir(parents=True, exist_ok=True)
    readme = paths.ratification_dir / "README.md"
    handoff = paths.ratification_dir / "RATIFICATION_HANDOFF.md"
    if not readme.exists():
        readme.write_text(
            "\n".join(
                [
                    f"# Ratification handoff — {paths.document_id}",
                    "",
                    "This folder is a non-doctrine handoff workspace for ratification preparation.",
                    "",
                    "- It does not ratify the amendment.",
                    "- It does not mutate amendment or motion files by itself.",
                    "- Council / constitutional approval remains manual.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        created.append(readme.relative_to(paths.base_dir).as_posix())
    if not handoff.exists():
        handoff.write_text(
            "\n".join(
                [
                    f"# Ratification handoff packet — {paths.document_id}",
                    "",
                    "## Purpose",
                    "",
                    "Prepare the evidence and references needed for a later motion or council handoff.",
                    "",
                    "## Required references",
                    "",
                    f"- Amendment: `{paths.document_path}`",
                    f"- Intake status: `{paths.intake_status.relative_to(paths.base_dir).as_posix()}`",
                    f"- Intake events: `{paths.intake_events.relative_to(paths.base_dir).as_posix()}`",
                    f"- Round 1 packet: `{paths.round_1_dir.relative_to(paths.base_dir).as_posix()}`",
                    f"- Round 2 packet: `{paths.round_2_dir.relative_to(paths.base_dir).as_posix()}`",
                    "",
                    "## Manual authority",
                    "",
                    "- Motion drafting is manual in Stage 2.",
                    "- Ratified status changes are manual in Stage 2.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        created.append(handoff.relative_to(paths.base_dir).as_posix())
    return created

