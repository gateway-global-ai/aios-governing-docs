#!/usr/bin/env python3
"""
Run a separated local Ollama amendment revision loop.

This wrapper preserves lane separation:
  1. discovery pass -> DISCOVERY_REPORT.md
  2. research pass -> LOCAL_RESEARCH_REPORT.md
  3. drafting pass -> DRAFT_AMENDMENT_PROPOSAL.md

It delegates actual model execution to scripts/ollama_authoring_agent.py so that:
  - manifests stay explicit
  - run records are written by the bounded authoring runner
  - the coordinator can review research and draft artifacts separately
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent


def _resolve_repo_path(path: str | Path) -> Path:
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = (BASE_DIR / str(candidate).replace("\\", "/")).resolve()
    else:
        candidate = candidate.resolve()
    try:
        candidate.relative_to(BASE_DIR.resolve())
    except ValueError as exc:
        raise ValueError(f"Path is outside repo root: {path}") from exc
    return candidate


def _repo_rel(path: Path) -> str:
    return path.resolve().relative_to(BASE_DIR.resolve()).as_posix()


def _read_required_text(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Required file missing: {path}")
    return path.read_text(encoding="utf-8")


def _run_authoring(
    *,
    mode: str,
    manifest_path: Path,
    assignment_path: Path,
    output_path: Path,
    includes: list[str],
) -> None:
    prompt = _read_required_text(assignment_path).strip()
    cmd = [
        sys.executable,
        str((SCRIPT_DIR / "ollama_authoring_agent.py").resolve()),
        "--mode",
        mode,
        "--manifest",
        _repo_rel(manifest_path),
        "--prompt",
        prompt,
        "--output",
        _repo_rel(output_path),
    ]
    for include in includes:
        cmd.extend(["--include", include.replace("\\", "/")])
    subprocess.run(cmd, cwd=BASE_DIR, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Separated Ollama amendment discovery/research/drafting loop")
    parser.add_argument(
        "--review-slug",
        required=True,
        help="Review root slug under reviews/<slug>/planning/",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        required=True,
        help="Repo-relative manifest used by the bounded authoring runner",
    )
    parser.add_argument(
        "--step",
        choices=["discovery", "research", "draft", "full"],
        default="full",
        help="Which separated lane to run",
    )
    parser.add_argument(
        "--discovery-mode",
        choices=["technical", "editorial"],
        default="technical",
        help="Authoring mode for the discovery pass",
    )
    parser.add_argument(
        "--research-mode",
        choices=["technical", "editorial"],
        default="technical",
        help="Authoring mode for the research pass",
    )
    parser.add_argument(
        "--draft-mode",
        choices=["technical", "editorial"],
        default="technical",
        help="Authoring mode for the drafting pass",
    )
    parser.add_argument(
        "--discovery-assignment",
        type=Path,
        help="Repo-relative assignment file for the discovery pass",
    )
    parser.add_argument(
        "--research-assignment",
        type=Path,
        help="Repo-relative assignment file for the research pass",
    )
    parser.add_argument(
        "--draft-assignment",
        type=Path,
        help="Repo-relative assignment file for the drafting pass",
    )
    parser.add_argument(
        "--discovery-output",
        type=Path,
        help="Repo-relative output file for the discovery pass",
    )
    parser.add_argument(
        "--research-output",
        type=Path,
        help="Repo-relative output file for the research pass",
    )
    parser.add_argument(
        "--draft-output",
        type=Path,
        help="Repo-relative output file for the drafting pass",
    )
    parser.add_argument(
        "--discovery-include",
        action="append",
        default=[],
        help="Optional manifest-declared include for discovery pass",
    )
    parser.add_argument(
        "--research-include",
        action="append",
        default=[],
        help="Optional manifest-declared include for research pass",
    )
    parser.add_argument(
        "--draft-include",
        action="append",
        default=[],
        help="Optional manifest-declared include for drafting pass",
    )
    args = parser.parse_args()

    planning_dir = (BASE_DIR / "reviews" / args.review_slug / "planning").resolve()
    manifest_path = _resolve_repo_path(args.manifest)
    discovery_assignment = _resolve_repo_path(
        args.discovery_assignment or planning_dir / "DISCOVERY_ASSIGNMENT.md"
    )
    research_assignment = _resolve_repo_path(
        args.research_assignment or planning_dir / "RESEARCH_ASSIGNMENT.md"
    )
    draft_assignment = _resolve_repo_path(
        args.draft_assignment or planning_dir / "DRAFTING_ASSIGNMENT.md"
    )
    discovery_output = _resolve_repo_path(
        args.discovery_output or planning_dir / "DISCOVERY_REPORT.md"
    )
    research_output = _resolve_repo_path(
        args.research_output or planning_dir / "LOCAL_RESEARCH_REPORT.md"
    )
    draft_output = _resolve_repo_path(
        args.draft_output or planning_dir / "DRAFT_AMENDMENT_PROPOSAL.md"
    )

    if args.step in {"discovery", "full"}:
        print(f"[discovery] manifest={_repo_rel(manifest_path)}")
        print(f"[discovery] assignment={_repo_rel(discovery_assignment)}")
        print(f"[discovery] output={_repo_rel(discovery_output)}")
        _run_authoring(
            mode=args.discovery_mode,
            manifest_path=manifest_path,
            assignment_path=discovery_assignment,
            output_path=discovery_output,
            includes=args.discovery_include,
        )

    if args.step in {"research", "full"}:
        research_includes = [inc.replace("\\", "/") for inc in args.research_include]
        discovery_rel = _repo_rel(discovery_output)
        if discovery_output.is_file() and discovery_rel not in research_includes:
            research_includes.append(discovery_rel)
        print(f"[research] manifest={_repo_rel(manifest_path)}")
        print(f"[research] assignment={_repo_rel(research_assignment)}")
        print(f"[research] output={_repo_rel(research_output)}")
        _run_authoring(
            mode=args.research_mode,
            manifest_path=manifest_path,
            assignment_path=research_assignment,
            output_path=research_output,
            includes=research_includes,
        )

    if args.step in {"draft", "full"}:
        draft_includes = [inc.replace("\\", "/") for inc in args.draft_include]
        discovery_rel = _repo_rel(discovery_output)
        if discovery_output.is_file() and discovery_rel not in draft_includes:
            draft_includes.append(discovery_rel)
        research_rel = _repo_rel(research_output)
        if research_output.is_file() and research_rel not in draft_includes:
            draft_includes.append(research_rel)
        print(f"[draft] manifest={_repo_rel(manifest_path)}")
        print(f"[draft] assignment={_repo_rel(draft_assignment)}")
        print(f"[draft] output={_repo_rel(draft_output)}")
        _run_authoring(
            mode=args.draft_mode,
            manifest_path=manifest_path,
            assignment_path=draft_assignment,
            output_path=draft_output,
            includes=draft_includes,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
