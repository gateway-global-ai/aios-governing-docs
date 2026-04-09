#!/usr/bin/env python3
"""
Deterministic operator_note -> intake-envelope normalization.

This module implements one narrow collector-side slice only:
  - accepts a governed repo-local operator note input shape
  - normalizes it into a CANI intake envelope
  - validates the envelope with the existing CANI validator
  - stops at validator output with no writer handoff
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

import yaml

from cani_validator import BASE_DIR
from cani_validator import CaniValidationResult
from cani_validator import validate_intake_envelope_path

SPEC_REQUIRED_KEYS = frozenset({
    "operator_note_ref",
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


class OperatorNoteNormalizationError(RuntimeError):
    """Raised when operator_note normalization must fail closed."""


@dataclass
class OperatorNoteNormalizationResult:
    output_path: str
    envelope: dict[str, Any]
    validator_result: CaniValidationResult
    persisted_handoff_performed: bool = False


def load_operator_note_spec(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        body = json.loads(text)
    else:
        body = yaml.safe_load(text)
    if not isinstance(body, dict):
        raise OperatorNoteNormalizationError("Operator note normalization input must be a mapping/object.")
    return body


def _is_external_ref(value: str) -> bool:
    return bool(re.match(r"^[a-z]+://", value.strip(), re.IGNORECASE))


def _require_mapping(spec: Mapping[str, Any]) -> None:
    missing = sorted(key for key in SPEC_REQUIRED_KEYS if key not in spec)
    if missing:
        raise OperatorNoteNormalizationError(f"Operator note input is missing required keys: {missing}")
    extras = sorted(set(spec.keys()) - (SPEC_REQUIRED_KEYS | SPEC_OPTIONAL_KEYS))
    if extras:
        raise OperatorNoteNormalizationError(f"Operator note input contains unsupported keys: {extras}")


def _require_nonempty_string(spec: Mapping[str, Any], key: str) -> str:
    value = spec.get(key)
    if not isinstance(value, str) or not value.strip():
        raise OperatorNoteNormalizationError(f"Operator note input requires non-empty string for {key}.")
    return value.strip()


def _require_positive_int(spec: Mapping[str, Any], key: str) -> int:
    value = spec.get(key)
    if not isinstance(value, int) or value < 1:
        raise OperatorNoteNormalizationError(f"Operator note input requires integer >= 1 for {key}.")
    return value


def _resolve_repo_file_ref(value: str, *, key: str, base_dir: Path, require_markdown: bool = False) -> str:
    raw = str(value or "").strip()
    if not raw:
        raise OperatorNoteNormalizationError(f"Operator note input requires repo-local value for {key}.")
    if _is_external_ref(raw):
        raise OperatorNoteNormalizationError(f"{key} must remain repo-local and reviewable, not external.")
    candidate = Path(raw)
    resolved = candidate.resolve() if candidate.is_absolute() else (base_dir / candidate).resolve()
    try:
        rel = resolved.relative_to(base_dir.resolve()).as_posix()
    except Exception as exc:
        raise OperatorNoteNormalizationError(f"{key} escapes the repo authority boundary: {raw}") from exc
    if not resolved.exists() or not resolved.is_file():
        raise OperatorNoteNormalizationError(f"{key} must reference an existing repo-local file: {raw}")
    if require_markdown and resolved.suffix.lower() != ".md":
        raise OperatorNoteNormalizationError(f"{key} must reference a repo-local markdown note: {raw}")
    return rel


def _resolve_repo_output_path(value: str | Path, *, base_dir: Path) -> Path:
    raw_path = Path(value)
    resolved = raw_path.resolve() if raw_path.is_absolute() else (base_dir / raw_path).resolve()
    try:
        resolved.relative_to(base_dir.resolve())
    except Exception as exc:
        raise OperatorNoteNormalizationError(f"Output path escapes the repo authority boundary: {value}") from exc
    if resolved.suffix.lower() not in {".yaml", ".yml"}:
        raise OperatorNoteNormalizationError("Output path must be a YAML file.")
    return resolved


def _normalize_evidence_refs(spec: Mapping[str, Any], *, base_dir: Path) -> list[str]:
    value = spec.get("evidence_refs")
    if not isinstance(value, list) or not value:
        raise OperatorNoteNormalizationError("Operator note input requires non-empty list for evidence_refs.")
    normalized: list[str] = []
    for item in value:
        normalized.append(_resolve_repo_file_ref(item, key="evidence_refs", base_dir=base_dir))
    return normalized


def build_operator_note_envelope(spec: Mapping[str, Any], *, base_dir: Path = BASE_DIR) -> dict[str, Any]:
    _require_mapping(spec)

    operator_note_ref = _resolve_repo_file_ref(
        _require_nonempty_string(spec, "operator_note_ref"),
        key="operator_note_ref",
        base_dir=base_dir,
        require_markdown=True,
    )
    evidence_refs = _normalize_evidence_refs(spec, base_dir=base_dir)

    provenance: dict[str, Any] = {
        "admitted_by": _require_nonempty_string(spec, "admitted_by"),
        "evidence_basis": _require_nonempty_string(spec, "evidence_basis"),
    }
    for key in ("observed_by", "confidence", "interpretation_limit"):
        if key in spec and spec.get(key) is not None:
            provenance[key] = _require_nonempty_string(spec, key)

    sequence: dict[str, Any] = {
        "stream_key": _require_nonempty_string(spec, "stream_key"),
        "sequence_id": _require_positive_int(spec, "sequence_id"),
    }
    for key in ("batch_id", "causal_parent_id", "related_observation_set_id", "related_recommendation_id"):
        if key in spec and spec.get(key) is not None:
            sequence[key] = _require_nonempty_string(spec, key)

    envelope: dict[str, Any] = {
        "ingestion_envelope_id": _require_nonempty_string(spec, "ingestion_envelope_id"),
        "envelope_schema_version": "1",
        "recorded_at": _require_nonempty_string(spec, "recorded_at"),
        "signal_family": _require_nonempty_string(spec, "signal_family"),
        "signal_type": _require_nonempty_string(spec, "signal_type"),
        "source_surface": "operator_note",
        "source_artifact_ref": operator_note_ref,
        "provenance": provenance,
        "sequence": sequence,
        "normalization_state": "normalized",
        "payload_ref": operator_note_ref,
        "evidence_refs": evidence_refs,
    }
    if "notes" in spec and spec.get("notes") is not None:
        envelope["notes"] = _require_nonempty_string(spec, "notes")
    return envelope


def normalize_operator_note_to_intake_envelope(
    spec: Mapping[str, Any],
    *,
    output_path: str | Path,
    base_dir: Path = BASE_DIR,
) -> OperatorNoteNormalizationResult:
    envelope = build_operator_note_envelope(spec, base_dir=base_dir)
    resolved_output = _resolve_repo_output_path(output_path, base_dir=base_dir)
    resolved_output.parent.mkdir(parents=True, exist_ok=True)
    resolved_output.write_text(yaml.safe_dump(envelope, sort_keys=False), encoding="utf-8")

    validator_result = validate_intake_envelope_path(resolved_output, base_dir=base_dir)
    if validator_result.outcome not in {"pass", "advisory_warning"}:
        if resolved_output.exists():
            resolved_output.unlink()
        details = ", ".join(f"{finding.outcome}:{finding.code}" for finding in validator_result.findings) or validator_result.outcome
        raise OperatorNoteNormalizationError(f"Normalized operator_note intake envelope failed validation: {details}")

    return OperatorNoteNormalizationResult(
        output_path=resolved_output.relative_to(base_dir.resolve()).as_posix(),
        envelope=envelope,
        validator_result=validator_result,
        persisted_handoff_performed=False,
    )
