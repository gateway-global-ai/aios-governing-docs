#!/usr/bin/env python3
"""Normalize one governed operator_note input into a validated CANI intake envelope."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from cani_operator_note_normalizer import OperatorNoteNormalizationError
from cani_operator_note_normalizer import load_operator_note_spec
from cani_operator_note_normalizer import normalize_operator_note_to_intake_envelope


def _err(message: str) -> None:
    print(message, file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize one governed operator_note into a CANI intake envelope")
    parser.add_argument("--input", required=True, help="YAML or JSON operator_note normalization input")
    parser.add_argument("--output", required=True, help="Repo-local YAML path for the normalized intake envelope")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON result.")
    args = parser.parse_args()

    try:
        spec = load_operator_note_spec(Path(args.input))
        result = normalize_operator_note_to_intake_envelope(spec, output_path=args.output)
    except OperatorNoteNormalizationError as exc:
        _err(str(exc))
        return 1

    if args.json:
        print(
            json.dumps(
                {
                    "output_path": result.output_path,
                    "validator_result": result.validator_result.to_dict(),
                    "persisted_handoff_performed": result.persisted_handoff_performed,
                },
                indent=2,
            )
        )
    else:
        _err(f"Wrote intake envelope: {result.output_path}")
        _err(f"Validator result: {result.validator_result.outcome}")
        _err(f"Persisted handoff performed: {result.persisted_handoff_performed}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
