#!/usr/bin/env python3
"""
Validate CANI persisted artifacts and telemetry/intake envelopes.

Outcome family:
  - pass
  - fail
  - blocked
  - advisory_warning
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from cani_validator import (
    BASE_DIR,
    PERSISTED_OBSERVATION_ARTIFACT,
    PERSISTED_RECOMMENDATION_ARTIFACT,
    TELEMETRY_INTAKE_ENVELOPE,
    validate_cani_target,
)


def _err(message: str) -> None:
    print(message, file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate CANI artifacts and intake envelopes")
    parser.add_argument("--path", required=True, help="Path to a CANI observation dir, recommendation dir, or intake-envelope file")
    parser.add_argument(
        "--artifact-class",
        choices=(
            PERSISTED_OBSERVATION_ARTIFACT,
            PERSISTED_RECOMMENDATION_ARTIFACT,
            TELEMETRY_INTAKE_ENVELOPE,
        ),
        help="Explicit CANI artifact class. If omitted, the validator auto-detects it from the target path.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON result.")
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if not target.exists():
        _err(f"Not found: {target}")
        return 1

    result = validate_cani_target(target, artifact_class=args.artifact_class, base_dir=BASE_DIR)
    if args.json:
        print(json.dumps(result.to_dict(), indent=2))
    else:
        for finding in result.findings:
            _err(f"{finding.outcome.upper()}: [{finding.code}] {finding.message}")
        _err(f"Result: {result.outcome}")

    return 0 if result.outcome in {"pass", "advisory_warning"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
