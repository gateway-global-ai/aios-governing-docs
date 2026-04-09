#!/usr/bin/env python3
"""
Deterministic review_artifact -> intake-envelope normalization.

This module implements one narrow collector-side slice only:
  - accepts a governed repo-local review artifact input shape
  - normalizes it into a CANI intake envelope
  - validates the envelope with the existing CANI validator
  - stops at validator output with no writer handoff
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import yaml

from _cani_repo_local_intake_common import _build_common_repo_local_intake_envelope
from _cani_repo_local_intake_common import _RepoLocalIntakeSurfaceConfig
from cani_validator import BASE_DIR
from cani_validator import CaniValidationResult
from cani_validator import validate_intake_envelope_path

SPEC_REQUIRED_KEYS = frozenset({
    "review_artifact_ref",
    "ingestion_envelope_id",
    "recorded_at",
    "signal_family",
    "signal_type",
    "admitted_by",
    "evidence_basis",
    "stream_key",
    "sequence_id",
    "evidence_refs",
})

SPEC_OPTIONAL_KEYS = frozenset({
    "observed_by",
    "confidence",
    "interpretation_limit",
    "notes",
    "batch_id",
    "causal_parent_id",
    "related_observation_set_id",
    "related_recommendation_id",
})

COMMON_ENVELOPE_CONFIG = _RepoLocalIntakeSurfaceConfig(
    input_label="Review artifact input",
    artifact_ref_key="review_artifact_ref",
    source_surface="review_artifact",
    markdown_artifact_label="repo-local markdown review artifact",
    required_keys=SPEC_REQUIRED_KEYS,
    optional_keys=SPEC_OPTIONAL_KEYS,
)


class ReviewArtifactNormalizationError(RuntimeError):
    """Raised when review_artifact normalization must fail closed."""


@dataclass
class ReviewArtifactNormalizationResult:
    output_path: str
    envelope: dict[str, Any]
    validator_result: CaniValidationResult
    persisted_handoff_performed: bool = False


def load_review_artifact_spec(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        body = json.loads(text)
    else:
        body = yaml.safe_load(text)
    if not isinstance(body, dict):
        raise ReviewArtifactNormalizationError("Review artifact normalization input must be a mapping/object.")
    return body


def _resolve_repo_output_path(value: str | Path, *, base_dir: Path) -> Path:
    raw_path = Path(value)
    resolved = raw_path.resolve() if raw_path.is_absolute() else (base_dir / raw_path).resolve()
    try:
        resolved.relative_to(base_dir.resolve())
    except Exception as exc:
        raise ReviewArtifactNormalizationError(f"Output path escapes the repo authority boundary: {value}") from exc
    if resolved.suffix.lower() not in {".yaml", ".yml"}:
        raise ReviewArtifactNormalizationError("Output path must be a YAML file.")
    return resolved


def build_review_artifact_envelope(spec: Mapping[str, Any], *, base_dir: Path = BASE_DIR) -> dict[str, Any]:
    try:
        return _build_common_repo_local_intake_envelope(
            spec,
            config=COMMON_ENVELOPE_CONFIG,
            base_dir=base_dir,
        )
    except ValueError as exc:
        raise ReviewArtifactNormalizationError(str(exc)) from exc


def normalize_review_artifact_to_intake_envelope(
    spec: Mapping[str, Any],
    *,
    output_path: str | Path,
    base_dir: Path = BASE_DIR,
) -> ReviewArtifactNormalizationResult:
    envelope = build_review_artifact_envelope(spec, base_dir=base_dir)
    resolved_output = _resolve_repo_output_path(output_path, base_dir=base_dir)
    resolved_output.parent.mkdir(parents=True, exist_ok=True)
    resolved_output.write_text(yaml.safe_dump(envelope, sort_keys=False), encoding="utf-8")

    validator_result = validate_intake_envelope_path(resolved_output, base_dir=base_dir)
    if validator_result.outcome not in {"pass", "advisory_warning"}:
        if resolved_output.exists():
            resolved_output.unlink()
        details = ", ".join(f"{finding.outcome}:{finding.code}" for finding in validator_result.findings) or validator_result.outcome
        raise ReviewArtifactNormalizationError(f"Normalized review_artifact intake envelope failed validation: {details}")

    return ReviewArtifactNormalizationResult(
        output_path=resolved_output.relative_to(base_dir.resolve()).as_posix(),
        envelope=envelope,
        validator_result=validator_result,
        persisted_handoff_performed=False,
    )
