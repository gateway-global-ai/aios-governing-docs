"""
Execute approved actions from action_plan.json and append to execution_log.jsonl.

Only whitelisted execution_kind values run subprocesses; manual steps are logged.

Usage:
    py execute_action_plan.py AMD-2026-a10b9a
    py execute_action_plan.py AMD-2026-a10b9a --dry-run
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from context_assembler import BASE_DIR

SCRIPTS_DIR = Path(__file__).resolve().parent

ALLOWED_KINDS = frozenset({"manual", "registry_regenerate", "schema_extract"})


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _append_log(source_dir: Path, entry: dict):
    log_path = source_dir / "execution_log.jsonl"
    line = json.dumps(entry, ensure_ascii=False) + "\n"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(line)


def _save_plan(source_dir: Path, plan: dict):
    (source_dir / "action_plan.json").write_text(
        json.dumps(plan, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def _run_script(args: list[str], dry_run: bool) -> tuple[int, str]:
    if dry_run:
        return 0, f"[dry-run] would run: {' '.join(args)}"
    proc = subprocess.run(
        args,
        cwd=str(SCRIPTS_DIR),
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    msg = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, msg[:8000]


def execute(source_name: str, dry_run: bool = False) -> dict:
    source_dir = BASE_DIR / "sources" / source_name
    plan_path = source_dir / "action_plan.json"
    if not plan_path.exists():
        raise FileNotFoundError(f"No action_plan.json in {source_dir}")

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    actions = plan.get("actions", [])
    summary = {"source_name": source_name, "processed": 0, "completed": 0, "failed": 0, "skipped": 0}

    py = sys.executable

    for act in actions:
        if act.get("status") != "approved":
            summary["skipped"] += 1
            continue

        aid = act.get("id", "?")
        kind = act.get("execution_kind", "manual")
        if kind not in ALLOWED_KINDS:
            act["status"] = "failed"
            act["execution_error"] = f"Unknown execution_kind: {kind}"
            summary["failed"] += 1
            _append_log(
                source_dir,
                {
                    "ts": _now_iso(),
                    "action_id": aid,
                    "event": "failed",
                    "message": act["execution_error"],
                },
            )
            continue

        _append_log(
            source_dir,
            {"ts": _now_iso(), "action_id": aid, "event": "started", "execution_kind": kind},
        )

        if kind == "manual":
            act["status"] = "completed"
            act["executed_at"] = _now_iso()
            act["execution_note"] = "Logged manual step — perform document edits outside this script."
            _append_log(
                source_dir,
                {
                    "ts": _now_iso(),
                    "action_id": aid,
                    "event": "completed",
                    "message": "manual — see action description",
                },
            )
            summary["completed"] += 1
            summary["processed"] += 1
            continue

        if kind == "registry_regenerate":
            code, out = _run_script([py, str(SCRIPTS_DIR / "registry_generator.py")], dry_run)
        elif kind == "schema_extract":
            code, out = _run_script([py, str(SCRIPTS_DIR / "schema_extractor.py")], dry_run)
        else:
            code, out = 1, ""

        if code == 0:
            act["status"] = "completed"
            act["executed_at"] = _now_iso()
            act["execution_note"] = out[:2000] if out else "ok"
            _append_log(
                source_dir,
                {
                    "ts": _now_iso(),
                    "action_id": aid,
                    "event": "completed",
                    "execution_kind": kind,
                    "detail": out[:4000],
                },
            )
            summary["completed"] += 1
        else:
            act["status"] = "failed"
            act["execution_error"] = out or f"exit {code}"
            _append_log(
                source_dir,
                {
                    "ts": _now_iso(),
                    "action_id": aid,
                    "event": "failed",
                    "detail": out[:4000],
                },
            )
            summary["failed"] += 1
        summary["processed"] += 1

    _save_plan(source_dir, plan)
    _append_log(source_dir, {"ts": _now_iso(), "event": "batch_summary", **summary})
    return summary


def main():
    parser = argparse.ArgumentParser(description="Execute approved actions from action_plan.json")
    parser.add_argument("source_name")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        s = execute(args.source_name, dry_run=args.dry_run)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(s, indent=2))


if __name__ == "__main__":
    main()
