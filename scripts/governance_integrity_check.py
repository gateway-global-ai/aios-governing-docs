#!/usr/bin/env python3
"""
CI governance integrity checks (AIOS-OPS-005 / AIOS-OPS-006).

Validates only what existing repo tooling supports truthfully:
  G-1  duplicate document_id across scanned registry documents
  G-3  broken cross_references (via conflict_detector)
  G-7  DOCUMENT_REGISTRY.* matches scripts/registry_generator.py output
  YAML reference/agent_registry.yaml parses

Does not run ci_governance_dry_run (requires missing automated_review_pipeline.py).

Usage (repo root):
  py -3 scripts/governance_integrity_check.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
BASE = SCRIPTS.parent

sys.path.insert(0, str(SCRIPTS))

from conflict_detector import _validate_cross_references  # noqa: E402
from registry_generator import _normalize_cross_refs, scan_documents  # noqa: E402


def check_g1_duplicate_ids(docs: list[dict]) -> bool:
    rows: list[tuple[str, str]] = []
    for d in docs:
        did = d.get("document_id")
        if did and did not in ("—", "", "unregistered"):
            rows.append((did, d.get("_path", "")))
    counts = Counter(r[0] for r in rows)
    dups = [k for k, v in counts.items() if v > 1]
    if not dups:
        return True
    print("G-1 duplicate document_id:", file=sys.stderr)
    for dup in sorted(dups):
        paths = [p for i, p in rows if i == dup]
        print(f"  {dup}: {paths}", file=sys.stderr)
    return False


def check_g3_cross_references(docs: list[dict]) -> bool:
    norm = []
    for d in docs:
        nd = dict(d)
        nd["cross_references"] = _normalize_cross_refs(d.get("cross_references", []))
        norm.append(nd)
    findings = _validate_cross_references(norm)
    if not findings:
        return True
    print("G-3 broken cross_reference:", file=sys.stderr)
    for f in findings:
        print(f"  {f.get('message', f)}", file=sys.stderr)
    return False


def check_g7_registry_drift() -> bool:
    r = subprocess.run(
        [sys.executable, str(SCRIPTS / "registry_generator.py")],
        cwd=str(BASE),
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
        return False
    # Compare working tree to HEAD so CI and local runs detect uncommitted/stale registry
    # (not merely unstaged vs index).
    r2 = subprocess.run(
        ["git", "diff", "--exit-code", "HEAD", "--", "DOCUMENT_REGISTRY.md", "DOCUMENT_REGISTRY.json"],
        cwd=str(BASE),
        capture_output=True,
        text=True,
    )
    if r2.returncode != 0:
        print(
            "G-7 registry drift: committed DOCUMENT_REGISTRY.* does not match "
            "scripts/registry_generator.py. Run: py -3 scripts/registry_generator.py",
            file=sys.stderr,
        )
        if r2.stdout:
            print(r2.stdout, file=sys.stderr)
        if r2.stderr:
            print(r2.stderr, file=sys.stderr)
        return False
    return True


def check_agent_registry_yaml() -> bool:
    path = BASE / "reference" / "agent_registry.yaml"
    if not path.is_file():
        print("reference/agent_registry.yaml missing.", file=sys.stderr)
        return False
    try:
        import yaml  # type: ignore

        yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"reference/agent_registry.yaml parse error: {e}", file=sys.stderr)
        return False
    return True


def check_preflight_schema_json() -> bool:
    path = BASE / "reference" / "schemas" / "cursor_preflight.schema.json"
    if not path.is_file():
        return True
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"cursor_preflight.schema.json invalid JSON: {e}", file=sys.stderr)
        return False
    return True


def main() -> int:
    docs = scan_documents()
    ok = True
    ok = check_g1_duplicate_ids(docs) and ok
    ok = check_g3_cross_references(docs) and ok
    ok = check_g7_registry_drift() and ok
    ok = check_agent_registry_yaml() and ok
    ok = check_preflight_schema_json() and ok
    if ok:
        print("governance_integrity_check: OK")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
