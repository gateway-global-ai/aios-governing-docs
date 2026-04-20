from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


@dataclass(frozen=True)
class _RepoLocalIntakeSurfaceConfig:
    input_label: str
    artifact_ref_key: str
    source_surface: str
    markdown_artifact_label: str
    required_keys: frozenset[str]
    optional_keys: frozenset[str]


def _is_external_ref(value: str) -> bool:
    return bool(re.match(r"^[a-z]+://", value.strip(), re.IGNORECASE))


def _require_allowed_keys(
    spec: Mapping[str, Any],
    *,
    input_label: str,
    required_keys: frozenset[str],
    optional_keys: frozenset[str],
) -> None:
    missing = sorted(key for key in required_keys if key not in spec)
    if missing:
        raise ValueError(f"{input_label} is missing required keys: {missing}")
    extras = sorted(set(spec.keys()) - (required_keys | optional_keys))
    if extras:
        raise ValueError(f"{input_label} contains unsupported keys: {extras}")


def _require_nonempty_string(spec: Mapping[str, Any], *, key: str, input_label: str) -> str:
    value = spec.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{input_label} requires non-empty string for {key}.")
    return value.strip()


def _require_positive_int(spec: Mapping[str, Any], *, key: str, input_label: str) -> int:
    value = spec.get(key)
    if not isinstance(value, int) or value < 1:
        raise ValueError(f"{input_label} requires integer >= 1 for {key}.")
    return value


def _resolve_repo_file_ref(
    value: str,
    *,
    key: str,
    base_dir: Path,
    input_label: str,
    markdown_artifact_label: str | None = None,
) -> str:
    raw = str(value or "").strip()
    if not raw:
        raise ValueError(f"{input_label} requires repo-local value for {key}.")
    if _is_external_ref(raw):
        raise ValueError(f"{key} must remain repo-local and reviewable, not external.")
    candidate = Path(raw)
    resolved = candidate.resolve() if candidate.is_absolute() else (base_dir / candidate).resolve()
    try:
        rel = resolved.relative_to(base_dir.resolve()).as_posix()
    except Exception as exc:
        raise ValueError(f"{key} escapes the repo authority boundary: {raw}") from exc
    if not resolved.exists() or not resolved.is_file():
        raise ValueError(f"{key} must reference an existing repo-local file: {raw}")
    if markdown_artifact_label and resolved.suffix.lower() != ".md":
        raise ValueError(f"{key} must reference a {markdown_artifact_label}: {raw}")
    return rel


def _normalize_evidence_refs(spec: Mapping[str, Any], *, base_dir: Path, input_label: str) -> list[str]:
    value = spec.get("evidence_refs")
    if not isinstance(value, list) or not value:
        raise ValueError(f"{input_label} requires non-empty list for evidence_refs.")
    normalized: list[str] = []
    for item in value:
        normalized.append(
            _resolve_repo_file_ref(
                item,
                key="evidence_refs",
                base_dir=base_dir,
                input_label=input_label,
            )
        )
    return normalized


def _build_common_repo_local_intake_envelope(
    spec: Mapping[str, Any],
    *,
    config: _RepoLocalIntakeSurfaceConfig,
    base_dir: Path,
) -> dict[str, Any]:
    _require_allowed_keys(
        spec,
        input_label=config.input_label,
        required_keys=config.required_keys,
        optional_keys=config.optional_keys,
    )
    artifact_ref = _resolve_repo_file_ref(
        _require_nonempty_string(spec, key=config.artifact_ref_key, input_label=config.input_label),
        key=config.artifact_ref_key,
        base_dir=base_dir,
        input_label=config.input_label,
        markdown_artifact_label=config.markdown_artifact_label,
    )
    evidence_refs = _normalize_evidence_refs(spec, base_dir=base_dir, input_label=config.input_label)

    provenance: dict[str, Any] = {
        "admitted_by": _require_nonempty_string(spec, key="admitted_by", input_label=config.input_label),
        "evidence_basis": _require_nonempty_string(spec, key="evidence_basis", input_label=config.input_label),
    }
    for key in ("observed_by", "confidence", "interpretation_limit"):
        if key in spec and spec.get(key) is not None:
            provenance[key] = _require_nonempty_string(spec, key=key, input_label=config.input_label)

    sequence: dict[str, Any] = {
        "stream_key": _require_nonempty_string(spec, key="stream_key", input_label=config.input_label),
        "sequence_id": _require_positive_int(spec, key="sequence_id", input_label=config.input_label),
    }
    for key in ("batch_id", "causal_parent_id", "related_observation_set_id", "related_recommendation_id"):
        if key in spec and spec.get(key) is not None:
            sequence[key] = _require_nonempty_string(spec, key=key, input_label=config.input_label)

    envelope: dict[str, Any] = {
        "ingestion_envelope_id": _require_nonempty_string(spec, key="ingestion_envelope_id", input_label=config.input_label),
        "envelope_schema_version": "1",
        "recorded_at": _require_nonempty_string(spec, key="recorded_at", input_label=config.input_label),
        "signal_family": _require_nonempty_string(spec, key="signal_family", input_label=config.input_label),
        "signal_type": _require_nonempty_string(spec, key="signal_type", input_label=config.input_label),
        "source_surface": config.source_surface,
        "source_artifact_ref": artifact_ref,
        "provenance": provenance,
        "sequence": sequence,
        "normalization_state": "normalized",
        "payload_ref": artifact_ref,
        "evidence_refs": evidence_refs,
    }
    if "notes" in spec and spec.get("notes") is not None:
        envelope["notes"] = _require_nonempty_string(spec, key="notes", input_label=config.input_label)
    return envelope
