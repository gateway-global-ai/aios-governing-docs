#!/usr/bin/env python3
"""
MVP runner for AIOS-EXEC-DEMO-001 (non-normative operational tooling).

Creates reviews/<slug>/execution/ in the governance repo, initializes the execution packet,
optionally creates a git worktree on the product repo, runs install/build/test, and writes
validation + human-review stubs. Does not modify ratification mechanics.

Usage (governance repo root):
  py -3 scripts/run_isolated_execution_demo.py --review-slug amd_2026_006 \\
      --product-repo C:/Apps/ai-os-voice-interface --source-branch main

  py -3 scripts/run_isolated_execution_demo.py --review-slug amd_2026_006 --no-git

See: reference/implementation/AIOS-ISOLATED-EXECUTION-DEMONSTRATION-PIPELINE.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore

RUNNER_NAME = "run_isolated_execution_demo.py"
RUNNER_VERSION = "0.3.0"
SCRIPT_DIR = Path(__file__).resolve().parent
GOVERNANCE_ROOT = SCRIPT_DIR.parent
DEFAULT_MANIFEST = GOVERNANCE_ROOT / "reference/knowledge_base/agents/agent_kb_manifest.yaml"
SCHEMA_PATH = GOVERNANCE_ROOT / "reference/schemas/execution_transaction.schema.json"
TEMPLATE_DIR = GOVERNANCE_ROOT / "templates/execution_packet"


def _utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%SZ")


def _iso_utc_now() -> str:
    """ISO 8601 UTC for transaction timestamps (schema date-time)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _artifact_rel_paths() -> dict[str, str]:
    """Paths relative to reviews/<slug>/execution/ (transaction index)."""
    return {
        "execution_contract": "EXECUTION_CONTRACT.md",
        "validation_results": "VALIDATION_RESULTS.md",
        "worklog": "WORKLOG.md",
        "changed_files": "CHANGED_FILES.md",
        "human_review_packet": "HUMAN_REVIEW_PACKET.md",
        "visual_evidence_dir": "VISUAL_EVIDENCE",
    }


def _default_human_review_status() -> dict[str, Any]:
    return {
        "state": "pending",
        "reviewed_at": None,
        "reviewer": None,
        "notes": None,
    }


def _compute_operator_disclosures(
    *,
    no_git: bool,
    worktree_path: str | None,
    failure_stage: str | None,
    verification_status: str,
    skip_validation: bool,
    validation_ran_any: bool,
) -> dict[str, Any]:
    """
    Honest posture: packet_only is not a bound execution proof.
    validation_skipped / skip_validation are non-proof states, not soft success.
    """
    if no_git:
        return {
            "execution_lane_posture": "packet_only",
            "validation_proof_available": False,
            "validation_non_proof_reason": "no_git_product_repo_path_not_applicable",
            "visual_capture_automated": False,
        }
    if not worktree_path:
        reason = "git_fetch_failed"
        if failure_stage == "worktree_creation":
            reason = "worktree_add_failed"
        elif failure_stage != "git_fetch":
            reason = "failed_pre_worktree"
        return {
            "execution_lane_posture": "failed_pre_worktree",
            "validation_proof_available": False,
            "validation_non_proof_reason": reason,
            "visual_capture_automated": False,
        }
    proof = verification_status == "repo_truth_ok"
    reason: str | None = None
    if proof:
        return {
            "execution_lane_posture": "worktree_bound",
            "validation_proof_available": True,
            "validation_non_proof_reason": None,
            "visual_capture_automated": False,
        }
    if skip_validation:
        reason = "skip_validation"
    elif failure_stage == "validation_skipped":
        reason = "validation_skipped_non_proof"
    elif verification_status == "failed" and validation_ran_any:
        reason = "npm_command_failed"
    elif verification_status == "branch_ready":
        reason = "skip_validation"
    else:
        reason = "no_validation_proof"
    return {
        "execution_lane_posture": "worktree_bound",
        "validation_proof_available": False,
        "validation_non_proof_reason": reason,
        "visual_capture_automated": False,
    }


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _read_manifest_label() -> str:
    if yaml is None or not DEFAULT_MANIFEST.is_file():
        return "unknown"
    try:
        raw = yaml.safe_load(DEFAULT_MANIFEST.read_text(encoding="utf-8"))
        return str(raw.get("label") or "unknown")
    except Exception:
        return "unknown"


def _resolve_argv(argv: list[str]) -> list[str]:
    """Resolve bare executable names via PATH (Windows: npm is npm.cmd; CreateProcess needs a real path)."""
    if not argv or not argv[0]:
        return argv
    head = argv[0]
    try:
        if Path(head).exists():
            return argv
    except OSError:
        pass
    if "/" in head or "\\" in head:
        return argv
    resolved = shutil.which(head)
    if resolved:
        return [resolved] + list(argv[1:])
    return argv


def _run_subprocess(
    cwd: Path,
    argv: list[str],
    timeout: float = 900.0,
) -> tuple[int, str, str]:
    """Return (exit_code, stdout, stderr) as strings."""
    argv = _resolve_argv(argv)
    p = subprocess.run(
        argv,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        timeout=timeout,
        shell=False,
    )
    return p.returncode, p.stdout or "", p.stderr or ""


def _git(args: list[str], cwd: Path, timeout: float = 120.0) -> tuple[int, str, str]:
    return _run_subprocess(cwd, ["git", *args], timeout=timeout)


def _load_validation_commands(exec_dir: Path, config_path: Path | None) -> dict[str, list[str]]:
    """Return dict with optional keys install, build, test — each value is argv list."""
    defaults: dict[str, list[str]] = {}
    path = config_path
    if path is None:
        candidate = exec_dir / "VALIDATION_COMMANDS.json"
        if candidate.is_file():
            path = candidate
    if path is None or not path.is_file():
        return defaults
    data = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, list[str]] = {}
    for key in ("install", "build", "test"):
        if key not in data:
            continue
        val = data[key]
        if not isinstance(val, list) or not val or not all(isinstance(x, str) for x in val):
            raise ValueError(f"{path}: {key} must be a non-empty list of strings")
        out[key] = val
    return out


def _npm_defaults(product_repo: Path) -> dict[str, list[str]]:
    if not (product_repo / "package.json").is_file():
        return {}
    lock = product_repo / "package-lock.json"
    install_cmd = ["npm", "ci"] if lock.is_file() else ["npm", "install"]
    return {
        "install": install_cmd,
        "build": ["npm", "run", "build"],
        "test": ["npm", "test"],
    }


def _sanitize_branch_segment(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._/-]+", "-", s).strip("-") or "slug"


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _write_aux_artifacts(
    exec_dir: Path,
    slug: str,
    gov: Path,
    worktree_path: str | None,
    base_sha: str,
    tx: dict[str, Any],
    args: argparse.Namespace,
) -> None:
    """CHANGED_FILES, VISUAL_EVIDENCE stubs, HUMAN_REVIEW_PACKET (shared success + early failure)."""
    _write_text(
        exec_dir / "CHANGED_FILES.md",
        "# CHANGED_FILES\n\n"
        "No product source files were modified by this MVP runner (packet generation only). "
        "Record implementation diffs here after you edit the worktree.\n",
    )
    vis = exec_dir / "VISUAL_EVIDENCE"
    vis.mkdir(exist_ok=True)
    od = tx.get("operator_disclosures") or {}
    manual_visual = od.get("visual_capture_automated") is False
    _write_text(
        vis / "CAPTURE_CHECKLIST.md",
        "# Visual evidence — manual capture (MVP)\n\n"
        + (
            "**Automation:** Screenshots are **not** produced by the runner (`visual_capture_automated` is false in "
            "`EXECUTION_TRANSACTION.json`). What is missing until you add files here is **visible proof**, not a secret "
            "success.\n\n"
            if manual_visual
            else ""
        )
        + "Complete this checklist after `npm run dev` or your preferred preview.\n\n"
        "- [ ] Route / surface: …\n"
        "- [ ] Screenshot saved as `screenshots/01-<surface>.png`\n"
        "- [ ] Notes on expected vs observed behavior\n\n"
        "Add files under this folder; the **`artifacts`** object in the transaction points here.\n",
    )
    (vis / "screenshots").mkdir(exist_ok=True)

    arts = tx.get("artifacts") or _artifact_rel_paths()
    nav_rows = "\n".join(
        f"| `{k}` | `{v}` |" for k, v in sorted(arts.items())
    )
    od_lines = (
        "- **execution_lane_posture:** `"
        + str(od.get("execution_lane_posture", ""))
        + "`\n"
        "- **validation_proof_available:** "
        + str(od.get("validation_proof_available"))
        + "\n"
        "- **validation_non_proof_reason:** "
        + str(od.get("validation_non_proof_reason"))
        + "\n"
        "- **visual_capture_automated:** "
        + str(od.get("visual_capture_automated"))
        + "\n"
    )
    binding_block = ""
    if od.get("execution_lane_posture") == "packet_only":
        binding_block = (
            "> **Binding:** This run used `--no-git`. **`product_repo_path` is `not_applicable`.** "
            "This packet is **governance + planning evidence only** — **not** equivalent to a bound product clone or "
            "worktree execution proof. Do not treat it like a full execution lane result.\n\n"
        )
    elif od.get("validation_proof_available") is False and od.get("validation_non_proof_reason") in (
        "validation_skipped_non_proof",
        "skip_validation",
    ):
        binding_block = (
            "> **Validation proof:** **`validation_skipped`** or **`--skip-validation`** means **no install/build/test "
            "proof** was produced. That is an honest **non-success** for build health — not a soft pass.\n\n"
        )

    hrp = (
        "# Human review packet — "
        + slug
        + "\n\n"
        "**Status:** draft — MVP runner output\n\n"
        "## Navigation (canonical)\n\n"
        "Start from **`EXECUTION_TRANSACTION.json`**. The **`artifacts`** object is the index of paths "
        "(relative to this folder):\n\n"
        "| Key | Relative path |\n"
        "|-----|----------------|\n"
        + nav_rows
        + "\n\n"
        "## Binding and proof (from `operator_disclosures`)\n\n"
        + binding_block
        + od_lines
        + "\n"
        "## Summary\n\n"
        "- **Isolation:** "
        + (f"worktree `{worktree_path}`" if worktree_path else "none (`--no-git` or failed early)")
        + "\n"
        "- **Base commit:** `" + (base_sha or "n/a") + "`\n"
        "- **verification_status:** `" + str(tx.get("verification_status", "")) + "`\n"
        "- **promotion_status:** `" + str(tx.get("promotion_status", "")) + "`\n"
        "- **failure_stage:** `"
        + ("null" if tx.get("failure_stage") is None else str(tx.get("failure_stage")))
        + "`\n\n"
        "## Decision requested\n\n"
        "Can you approve **next action** given **what is actually proven** above (binding + validation proof + "
        "manual visual gap)?\n\n"
        "- [ ] I understand what is **not** proven (packet-only, skipped validation, or failed npm).\n"
        "- [ ] Validation / logs are acceptable for the claimed scope, or I reject.\n"
        "- [ ] Visual evidence is sufficient for UI-affecting scope, or N/A.\n"
        "- [ ] **Decision:** proceed with implementation / request changes / reject.\n\n"
        "## Overrides disclosed\n\n"
        + ("- `--no-git` or `--skip-validation` was used.\n" if (args.no_git or args.skip_validation) else "- None.\n")
        + "\n"
    )
    _write_text(exec_dir / "HUMAN_REVIEW_PACKET.md", hrp)


def _governance_path_for_json(gov: Path) -> str:
    """Prefer '.' when cwd is the governance root (portable in committed JSON)."""
    try:
        if Path.cwd().resolve() == gov.resolve():
            return "."
    except OSError:
        pass
    return gov.as_posix()


def _build_transaction(
    *,
    slug: str,
    args: argparse.Namespace,
    gov: Path,
    manifest_label: str,
    arch_hash: str,
    ui_hash: str | None,
    working_branch: str,
    product_repo_path: str,
    source_repo_url: str | None,
    worktree_path: str | None,
    isolation_mode: str,
    base_sha: str,
    head_sha: str,
    verification_status: str,
    promotion_status: str,
    overrides: bool,
    notes: str,
    created_at: str,
    updated_at: str,
    validation_started_at: str | None,
    validation_completed_at: str | None,
    failure_stage: str | None,
    operator_disclosures: dict[str, Any],
    human_review_status: dict[str, Any] | None = None,
) -> dict[str, Any]:
    # Local path is first-class; source_repo remains URL-or-identity (defaults to path).
    source_identity = (source_repo_url or "").strip() or product_repo_path
    return {
        "schema_version": "1.2.0",
        "review_slug": slug,
        "source_repo": source_identity,
        "product_repo_path": product_repo_path,
        "source_branch": args.source_branch,
        "working_branch": working_branch,
        "base_commit_sha": base_sha,
        "head_commit_sha": head_sha or None,
        "governing_manifest_label": manifest_label,
        "evidence_bundle_hash": None,
        "architect_plan_hash": arch_hash,
        "ui_plan_hash": ui_hash,
        "execution_scope": f"mvp_runner_{slug}",
        "allowed_surfaces": [],
        "required_visual_proofs": [],
        "created_at": created_at,
        "updated_at": updated_at,
        "validation_started_at": validation_started_at,
        "validation_completed_at": validation_completed_at,
        "artifacts": _artifact_rel_paths(),
        "failure_stage": failure_stage,
        "operator_disclosures": operator_disclosures,
        "human_review_status": human_review_status or _default_human_review_status(),
        "verification_status": verification_status,
        "promotion_status": promotion_status,
        "overrides_disclosed": overrides,
        "notes": notes,
        "governance_repo_path": _governance_path_for_json(gov),
        "worktree_path": worktree_path,
        "isolation_mode": isolation_mode,
        "runner_name": RUNNER_NAME,
        "runner_version": RUNNER_VERSION,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="MVP isolated execution demonstration packet + optional git worktree validation"
    )
    parser.add_argument("--review-slug", required=True, help="reviews/<slug>/")
    parser.add_argument(
        "--governance-root",
        type=Path,
        default=GOVERNANCE_ROOT,
        help="Path to aios-governing-docs root",
    )
    parser.add_argument(
        "--product-repo",
        type=Path,
        help="Path to implementation repo (e.g. ai-os-voice-interface). Required unless --no-git.",
    )
    parser.add_argument(
        "--source-branch",
        default="main",
        help="Branch to base worktree on (default: main)",
    )
    parser.add_argument(
        "--worktree-parent",
        type=Path,
        help="Directory where a new worktree folder will be created. Default: parent of --product-repo",
    )
    parser.add_argument(
        "--working-branch",
        help="New branch name for worktree. Default: execution/<slug>/runner-<utc>",
    )
    parser.add_argument(
        "--validation-config",
        type=Path,
        help="Path to VALIDATION_COMMANDS.json (else execution dir after copy, else npm defaults)",
    )
    parser.add_argument(
        "--no-git",
        action="store_true",
        help="Only create execution packet and stubs; skip worktree and validation commands",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Create worktree but do not run install/build/test",
    )
    parser.add_argument(
        "--source-repo-url",
        metavar="URL",
        help="Optional remote URL or repo identity for source_repo field (defaults to --product-repo path).",
    )
    args = parser.parse_args()

    gov = args.governance_root.resolve()
    slug = args.review_slug.strip()
    planning = gov / "reviews" / slug / "planning"
    arch = planning / "ARCHITECT_PLAN.md"
    ui = planning / "UI_PLAN.md"
    exec_dir = gov / "reviews" / slug / "execution"

    if not arch.is_file():
        print(f"ERROR: Missing required planning artifact: {arch}", file=sys.stderr)
        sys.exit(2)

    exec_dir.mkdir(parents=True, exist_ok=True)
    run_started_at = _iso_utc_now()

    # Copy template contract + example validation commands if not present
    contract_dst = exec_dir / "EXECUTION_CONTRACT.md"
    if not contract_dst.is_file():
        tpl = TEMPLATE_DIR / "EXECUTION_CONTRACT_TEMPLATE.md"
        if tpl.is_file():
            body = tpl.read_text(encoding="utf-8").replace("<review_slug>", slug)
            contract_dst.write_text(body, encoding="utf-8")
    ex_val = TEMPLATE_DIR / "VALIDATION_COMMANDS.example.json"
    if ex_val.is_file() and not (exec_dir / "VALIDATION_COMMANDS.example.json").is_file():
        _write_text(exec_dir / "VALIDATION_COMMANDS.example.json", ex_val.read_text(encoding="utf-8"))

    arch_hash = _sha256_file(arch)
    ui_hash = _sha256_file(ui) if ui.is_file() else None
    manifest_label = _read_manifest_label()
    stamp = _utc_stamp()
    working_branch = args.working_branch or f"execution/{_sanitize_branch_segment(slug)}/runner-{stamp}"

    isolation_mode = "none"
    worktree_path: str | None = None
    product_resolved: Path | None = None
    base_sha = ""
    head_sha = ""

    worklog_lines = [
        f"# WORKLOG — {slug}",
        "",
        f"- **{stamp}** — MVP runner {RUNNER_VERSION} started",
        f"- Planning: `{arch.relative_to(gov)}` (sha256 `{arch_hash[:16]}…`)",
    ]
    if ui.is_file():
        worklog_lines.append(f"- UI plan: `{ui.relative_to(gov)}` (sha256 `{ui_hash[:16]}…`)")  # type: ignore
    else:
        worklog_lines.append("- `UI_PLAN.md` absent (allowed for narrow scope)")

    validation_md_parts: list[str] = [
        "# VALIDATION_RESULTS",
        "",
        f"**Generated:** {stamp} (UTC) by `{RUNNER_NAME}` {RUNNER_VERSION}",
        "",
    ]

    verification_status = "pending"
    promotion_status = "blocked"
    failure_stage: str | None = None
    validation_started_at: str | None = None
    validation_completed_at: str | None = None
    validation_ran_any = False
    product_path_str = "not_applicable"

    if args.no_git:
        worklog_lines.append(f"- **{stamp}** — `--no-git`: skipped worktree and validation commands")
        validation_md_parts.append("## Status")
        validation_md_parts.append("")
        validation_md_parts.append("**Skipped:** `--no-git` — no product repo commands executed.")
        validation_md_parts.append("")
        validation_md_parts.append("## Non-proof state")
        validation_md_parts.append("")
        validation_md_parts.append(
            "**No product clone was bound.** `product_repo_path` is `not_applicable`. "
            "See `operator_disclosures.execution_lane_posture` = `packet_only` — **not** equivalent to a bound "
            "execution run."
        )
        validation_md_parts.append("")
        verification_status = "inputs_valid"
        promotion_status = "blocked"
        work_branch_final = "not_applicable"
        failure_stage = None
    else:
        work_branch_final = working_branch
        if not args.product_repo:
            print("ERROR: --product-repo is required unless --no-git", file=sys.stderr)
            sys.exit(2)
        product_resolved = args.product_repo.resolve()
        if not product_resolved.is_dir():
            print(f"ERROR: product repo not found: {product_resolved}", file=sys.stderr)
            sys.exit(2)
        product_path_str = product_resolved.as_posix()

        parent = args.worktree_parent.resolve() if args.worktree_parent else product_resolved.parent
        wt_name = f"aios-exec-{slug}-{stamp}"
        wt_path = parent / wt_name
        if wt_path.exists():
            print(f"ERROR: worktree path already exists: {wt_path}", file=sys.stderr)
            sys.exit(3)

        worklog_lines.append(f"- **{stamp}** — creating worktree at `{wt_path}` branch `{working_branch}`")

        rc, out, err = _git(["fetch", "origin", args.source_branch], product_resolved, timeout=300)
        if rc != 0:
            worklog_lines.append(f"- **FAIL** git fetch: {err.strip()}")
            validation_md_parts.append("## git fetch")
            validation_md_parts.append("")
            validation_md_parts.append(f"**exit {rc}**")
            validation_md_parts.append("")
            validation_md_parts.append("```")
            validation_md_parts.append((out + err).strip())
            validation_md_parts.append("```")
            fail_time = _iso_utc_now()
            od_fail = _compute_operator_disclosures(
                no_git=False,
                worktree_path=None,
                failure_stage="git_fetch",
                verification_status="failed",
                skip_validation=False,
                validation_ran_any=False,
            )
            tx = _build_transaction(
                slug=slug,
                args=args,
                gov=gov,
                manifest_label=manifest_label,
                arch_hash=arch_hash,
                ui_hash=ui_hash,
                working_branch=work_branch_final,
                product_repo_path=product_path_str,
                source_repo_url=args.source_repo_url,
                worktree_path=None,
                isolation_mode="none",
                base_sha="0000000",
                head_sha="",
                verification_status="failed",
                promotion_status="blocked",
                overrides=True,
                notes="git fetch failed — worktree not created",
                created_at=run_started_at,
                updated_at=fail_time,
                validation_started_at=None,
                validation_completed_at=None,
                failure_stage="git_fetch",
                operator_disclosures=od_fail,
            )
            _write_text(exec_dir / "EXECUTION_TRANSACTION.json", json.dumps(tx, indent=2) + "\n")
            _write_text(exec_dir / "WORKLOG.md", "\n".join(worklog_lines) + "\n")
            _write_text(exec_dir / "VALIDATION_RESULTS.md", "\n".join(validation_md_parts) + "\n")
            _write_aux_artifacts(exec_dir, slug, gov, None, "", tx, args)
            print("ERROR: git fetch failed", file=sys.stderr)
            sys.exit(4)

        rc, out, err = _git(
            [
                "worktree",
                "add",
                str(wt_path),
                "-b",
                working_branch,
                f"origin/{args.source_branch}",
            ],
            product_resolved,
            timeout=120,
        )
        if rc != 0:
            worklog_lines.append(f"- **FAIL** git worktree add: {err.strip()}")
            validation_md_parts.append("## git worktree add")
            validation_md_parts.append("")
            validation_md_parts.append(f"**exit {rc}**")
            validation_md_parts.append("")
            validation_md_parts.append("```")
            validation_md_parts.append((out + err).strip())
            validation_md_parts.append("```")
            fail_time = _iso_utc_now()
            od_fail = _compute_operator_disclosures(
                no_git=False,
                worktree_path=None,
                failure_stage="worktree_creation",
                verification_status="failed",
                skip_validation=False,
                validation_ran_any=False,
            )
            tx = _build_transaction(
                slug=slug,
                args=args,
                gov=gov,
                manifest_label=manifest_label,
                arch_hash=arch_hash,
                ui_hash=ui_hash,
                working_branch=work_branch_final,
                product_repo_path=product_path_str,
                source_repo_url=args.source_repo_url,
                worktree_path=None,
                isolation_mode="none",
                base_sha="0000000",
                head_sha="",
                verification_status="failed",
                promotion_status="blocked",
                overrides=True,
                notes="git worktree add failed",
                created_at=run_started_at,
                updated_at=fail_time,
                validation_started_at=None,
                validation_completed_at=None,
                failure_stage="worktree_creation",
                operator_disclosures=od_fail,
            )
            _write_text(exec_dir / "EXECUTION_TRANSACTION.json", json.dumps(tx, indent=2) + "\n")
            _write_text(exec_dir / "WORKLOG.md", "\n".join(worklog_lines) + "\n")
            _write_text(exec_dir / "VALIDATION_RESULTS.md", "\n".join(validation_md_parts) + "\n")
            _write_aux_artifacts(exec_dir, slug, gov, None, "", tx, args)
            print("ERROR: git worktree add failed", file=sys.stderr)
            sys.exit(5)

        isolation_mode = "worktree"
        worktree_path = wt_path.resolve().as_posix()
        rc, rev_out, _rev_err = _git(["rev-parse", "HEAD"], Path(wt_path), timeout=30)
        if rc != 0:
            base_sha = "0000000"
        else:
            base_sha = rev_out.strip()
        head_sha = base_sha
        worklog_lines.append(f"- **{stamp}** — base_commit_sha `{base_sha}`")

        if args.skip_validation:
            worklog_lines.append(f"- **{stamp}** — `--skip-validation`: install/build/test not run")
            validation_md_parts.append("## Status")
            validation_md_parts.append("")
            validation_md_parts.append("**Skipped:** `--skip-validation`")
            validation_md_parts.append("")
            validation_md_parts.append("## Non-proof state")
            validation_md_parts.append("")
            validation_md_parts.append(
                "**No npm install/build/test was run.** This is intentional for lane isolation checks — "
                "`validation_proof_available` is **false** in `operator_disclosures`."
            )
            validation_md_parts.append("")
            verification_status = "branch_ready"
            promotion_status = "blocked"
        else:
            cmds = _load_validation_commands(exec_dir, args.validation_config)
            if not cmds:
                cmds = _npm_defaults(wt_path)
            if not cmds:
                validation_md_parts.append("## Status")
                validation_md_parts.append("")
                validation_md_parts.append(
                    "**No commands run:** no `VALIDATION_COMMANDS.json` and no `package.json` defaults."
                )
                validation_md_parts.append("")
                validation_md_parts.append("## Non-proof state")
                validation_md_parts.append("")
                validation_md_parts.append(
                    "**`failure_stage` is `validation_skipped`.** This is **not** a soft success — no build/test "
                    "evidence was produced. See `operator_disclosures`."
                )
                validation_md_parts.append("")
                verification_status = "failed"
                promotion_status = "blocked"
                failure_stage = "validation_skipped"
            else:
                validation_started_at = _iso_utc_now()
                all_ok = True
                first_failure: str | None = None
                for step in ("install", "build", "test"):
                    if step not in cmds:
                        validation_md_parts.append(f"## {step}")
                        validation_md_parts.append("")
                        validation_md_parts.append("*Omitted (not in config / defaults).*")
                        validation_md_parts.append("")
                        continue
                    argv = cmds[step]
                    validation_md_parts.append(f"## {step}")
                    validation_md_parts.append("")
                    validation_md_parts.append(f"**cwd:** `{wt_path}`")
                    validation_md_parts.append("")
                    validation_md_parts.append(f"**command:** `{' '.join(argv)}`")
                    validation_md_parts.append("")
                    rc, o, e = _run_subprocess(Path(wt_path), argv, timeout=900.0)
                    validation_ran_any = True
                    validation_md_parts.append(f"**exit {rc}**")
                    validation_md_parts.append("")
                    validation_md_parts.append("```")
                    validation_md_parts.append((o + e).strip() or "(no output)")
                    validation_md_parts.append("```")
                    validation_md_parts.append("")
                    if rc != 0:
                        all_ok = False
                        if first_failure is None:
                            first_failure = step
                validation_completed_at = _iso_utc_now()
                verification_status = "repo_truth_ok" if all_ok else "failed"
                promotion_status = "ready_for_human_review" if all_ok else "blocked"
                if not all_ok and first_failure:
                    failure_stage = first_failure
                worklog_lines.append(
                    f"- **{stamp}** — validation finished (`verification_status={verification_status}`)"
                )

    if args.no_git:
        tx_base = "0000000"
    else:
        tx_base = base_sha if base_sha and re.match(r"^[0-9a-f]{7,40}$", base_sha) else "0000000"

    od_final = _compute_operator_disclosures(
        no_git=args.no_git,
        worktree_path=worktree_path,
        failure_stage=failure_stage,
        verification_status=verification_status,
        skip_validation=args.skip_validation,
        validation_ran_any=validation_ran_any,
    )
    notes_final = (
        "MVP runner — visual capture manual; see VISUAL_EVIDENCE/CAPTURE_CHECKLIST.md. "
        "operator_disclosures states binding and validation proof honestly."
    )
    transaction = _build_transaction(
        slug=slug,
        args=args,
        gov=gov,
        manifest_label=manifest_label,
        arch_hash=arch_hash,
        ui_hash=ui_hash,
        working_branch=work_branch_final,
        product_repo_path=product_path_str,
        source_repo_url=args.source_repo_url,
        worktree_path=worktree_path,
        isolation_mode=isolation_mode,
        base_sha=tx_base,
        head_sha=head_sha if not args.no_git else "",
        verification_status=verification_status,
        promotion_status=promotion_status,
        overrides=bool(args.no_git or args.skip_validation),
        notes=notes_final,
        created_at=run_started_at,
        updated_at=_iso_utc_now(),
        validation_started_at=validation_started_at,
        validation_completed_at=validation_completed_at,
        failure_stage=failure_stage,
        operator_disclosures=od_final,
    )

    _write_text(exec_dir / "EXECUTION_TRANSACTION.json", json.dumps(transaction, indent=2) + "\n")

    _write_text(exec_dir / "WORKLOG.md", "\n".join(worklog_lines) + "\n")
    _write_text(exec_dir / "VALIDATION_RESULTS.md", "\n".join(validation_md_parts) + "\n")
    _write_aux_artifacts(
        exec_dir,
        slug,
        gov,
        worktree_path,
        base_sha if not args.no_git else "",
        transaction,
        args,
    )

    print(f"Wrote execution packet: {exec_dir.relative_to(gov)}")
    if worktree_path:
        print(f"Worktree: {worktree_path}")
    print("Next: fill VISUAL_EVIDENCE/, review EXECUTION_CONTRACT.md, and complete human checklist.")


if __name__ == "__main__":
    main()
