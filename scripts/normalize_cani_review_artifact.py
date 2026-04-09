#!/usr/bin/env python3
"""Normalize one governed review_artifact input into a validated CANI intake envelope."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from cani_review_artifact_normalizer import ReviewArtifactNormalizationError
from cani_review_artifact_normalizer import load_review_artifact_spec
from cani_review_artifact_normalizer import normalize_review_artifact_to_intake_envelope


def _err(message: str) -> None:
    print(message, file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize one governed review_artifact into a CANI intake envelope")
    parser.add_argument("--input", required=True, help="YAML or JSON review_artifact normalization input")
    parser.add_argument("--output", required=True, help="Repo-local YAML path for the normalized intake envelope")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON result.")
    args = parser.parse_args()

    try:
        spec = load_review_artifact_spec(Path(args.input))
        result = normalize_review_artifact_to_intake_envelope(spec, output_path=args.output)
    except ReviewArtifactNormalizationError as exc:
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
