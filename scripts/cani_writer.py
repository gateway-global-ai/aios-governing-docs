#!/usr/bin/env python3
"""
Narrow runtime writer / persistence service bridge for CANI artifacts.

This module materializes governed repo-local persisted artifacts only:
  - observation sets
  - recommendation packets
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

from cani_validator import (
    BASE_DIR,
    OBSERVATION_IDENTITY_REQUIRED_KEYS,
    OBSERVATION_MUTABLE_FORBIDDEN_KEYS,
    RECOMMENDATION_IDENTITY_REQUIRED_KEYS,
    RECOMMENDATION_STATUS_OPTIONAL_KEYS,
    RECOMMENDATION_STATUS_REQUIRED_KEYS,
    validate_observation_set_dir,
    validate_recommendation_dir,
)

OBSERVATION_ROOT = "reviews/cani/observation_sets"
RECOMMENDATION_ROOT = "reviews/cani/recommendations"
RECOMMENDATION_STATUS_METADATA_ONLY_KEYS = frozenset({
    "status_updated_at",
    "status_updated_by",
    "linked_amendment_slug",
    "linked_planning_path",
    "linked_intake_path",
    "linked_review_path",
    "routing_note",
})


class CaniWriterError(RuntimeError):
    """Raised when a CANI write operation would violate the writer boundary."""


def _read_structured(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def _write_yaml(path: Path, body: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(body, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def _resolve_repo_dir(target_dir: str | Path, *, base_dir: Path, root_rel: str) -> tuple[Path, str]:
    base_dir = base_dir.resolve()
    candidate = Path(target_dir)
    resolved = candidate.resolve() if candidate.is_absolute() else (base_dir / candidate).resolve()
    try:
        rel = resolved.relative_to(base_dir).as_posix()
    except Exception as exc:
        raise CaniWriterError(f"Target path escapes repo boundary: {target_dir}") from exc
    root = root_rel.rstrip("/")
    if rel != root and not rel.startswith(root + "/"):
        raise CaniWriterError(f"Target path must live under {root_rel}: {rel}")
    return resolved, rel


def _snapshot(paths: list[Path]) -> dict[Path, str | None]:
    snap: dict[Path, str | None] = {}
    for path in paths:
        snap[path] = path.read_text(encoding="utf-8") if path.exists() else None
    return snap


def _restore(snapshot: dict[Path, str | None]) -> None:
    for path, body in snapshot.items():
        if body is None:
            if path.exists():
                path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body, encoding="utf-8")


def _ensure_validation_passes(result: Any, *, context: str, snapshot: dict[Path, str | None]) -> None:
    if result.outcome in {"fail", "blocked"}:
        _restore(snapshot)
        reasons = "; ".join(f"[{f.code}] {f.message}" for f in result.findings) or "unknown validation failure"
        raise CaniWriterError(f"{context} refused: {reasons}")


def _ensure_observation_identity_safe(identity: dict[str, Any], expected_rel: str, expected_slug: str) -> dict[str, Any]:
    missing = sorted(OBSERVATION_IDENTITY_REQUIRED_KEYS - set(identity.keys()))
    if missing:
        raise CaniWriterError(f"Observation identity missing required keys: {missing}")
    forbidden = sorted(set(identity.keys()) & OBSERVATION_MUTABLE_FORBIDDEN_KEYS)
    if forbidden:
        raise CaniWriterError(f"Observation identity must not hold mutable workflow status: {forbidden}")
    if str(identity.get("set_slug") or "") != expected_slug:
        raise CaniWriterError("Observation identity set_slug must match target directory name.")
    if "set_path" in identity and str(identity.get("set_path") or "") != expected_rel:
        raise CaniWriterError("Observation identity set_path must match the repo-relative target path.")
    body = deepcopy(identity)
    body["set_path"] = expected_rel
    return body


def _ensure_recommendation_identity_safe(identity: dict[str, Any], expected_rel: str, expected_slug: str) -> dict[str, Any]:
    missing = sorted(RECOMMENDATION_IDENTITY_REQUIRED_KEYS - set(identity.keys()))
    if missing:
        raise CaniWriterError(f"Recommendation identity missing required keys: {missing}")
    forbidden = sorted(set(identity.keys()) & ((RECOMMENDATION_STATUS_REQUIRED_KEYS - {"recommendation_id", "recommendation_slug"}) | RECOMMENDATION_STATUS_OPTIONAL_KEYS))
    if forbidden:
        raise CaniWriterError(f"Recommendation identity must not hold mutable routing or review status: {forbidden}")
    if str(identity.get("recommendation_slug") or "") != expected_slug:
        raise CaniWriterError("Recommendation identity recommendation_slug must match target directory name.")
    if "recommendation_path" in identity and str(identity.get("recommendation_path") or "") != expected_rel:
        raise CaniWriterError("Recommendation identity recommendation_path must match the repo-relative target path.")
    body = deepcopy(identity)
    body["recommendation_path"] = expected_rel
    return body


def _ensure_recommendation_status_consistent(status: dict[str, Any], identity: dict[str, Any]) -> dict[str, Any]:
    missing = sorted(RECOMMENDATION_STATUS_REQUIRED_KEYS - set(status.keys()))
    if missing:
        raise CaniWriterError(f"Recommendation status missing required keys: {missing}")
    if str(status.get("recommendation_id") or "") != str(identity.get("recommendation_id") or ""):
        raise CaniWriterError("Recommendation status recommendation_id must match identity.")
    if str(status.get("recommendation_slug") or "") != str(identity.get("recommendation_slug") or ""):
        raise CaniWriterError("Recommendation status recommendation_slug must match identity.")
    return deepcopy(status)


def _refuse_lifecycle_bearing_recommendation_status_change(
    current: dict[str, Any],
    proposed: dict[str, Any],
) -> None:
    changed = {
        key
        for key in RECOMMENDATION_STATUS_REQUIRED_KEYS | RECOMMENDATION_STATUS_OPTIONAL_KEYS
        if current.get(key) != proposed.get(key)
    }
    lifecycle_bearing = sorted(changed - RECOMMENDATION_STATUS_METADATA_ONLY_KEYS)
    if lifecycle_bearing:
        raise CaniWriterError(
            "Lifecycle-bearing recommendation status changes require a separate append-only event flow and are refused by update_recommendation_status: "
            + ", ".join(lifecycle_bearing)
        )


def _load_existing_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def materialize_observation_set(
    target_dir: str | Path,
    *,
    identity: dict[str, Any],
    first_event: dict[str, Any],
    handoff_note: str | None = None,
    base_dir: Path = BASE_DIR,
) -> Path:
    target_path, rel = _resolve_repo_dir(target_dir, base_dir=base_dir, root_rel=OBSERVATION_ROOT)
    expected_slug = target_path.name
    identity_body = _ensure_observation_identity_safe(identity, rel, expected_slug)

    identity_path = target_path / "OBSERVATION_SET_IDENTITY.yaml"
    events_path = target_path / "OBSERVATION_SET_EVENTS.yaml"
    handoff_path = target_path / "HANDOFF_NOTE.md"
    existing_paths = [identity_path, events_path, handoff_path]
    if any(path.exists() for path in (identity_path, events_path)):
        raise CaniWriterError("Observation set already exists. Use append_observation_event for append-only history updates.")

    events_doc = {
        "storage_schema_version": identity_body["storage_schema_version"],
        "observation_set_id": identity_body["observation_set_id"],
        "set_slug": identity_body["set_slug"],
        "events": [deepcopy(first_event)],
    }

    snapshot = _snapshot(existing_paths)
    try:
        _write_yaml(identity_path, identity_body)
        _write_yaml(events_path, events_doc)
        if handoff_note is not None:
            _write_text(handoff_path, handoff_note)
        result = validate_observation_set_dir(target_path, base_dir=base_dir)
        _ensure_validation_passes(result, context="Observation set materialization", snapshot=snapshot)
    except Exception:
        _restore(snapshot)
        raise
    return target_path


def append_observation_event(
    target_dir: str | Path,
    *,
    event: dict[str, Any],
    base_dir: Path = BASE_DIR,
) -> Path:
    target_path, _ = _resolve_repo_dir(target_dir, base_dir=base_dir, root_rel=OBSERVATION_ROOT)
    current = validate_observation_set_dir(target_path, base_dir=base_dir)
    if current.outcome in {"fail", "blocked"}:
        raise CaniWriterError("Cannot append to an observation set that does not currently validate.")

    events_path = target_path / "OBSERVATION_SET_EVENTS.yaml"
    snapshot = _snapshot([events_path])
    try:
        events_doc = _load_existing_yaml(events_path)
        events = list(events_doc.get("events") or [])
        events.append(deepcopy(event))
        events_doc["events"] = events
        _write_yaml(events_path, events_doc)
        result = validate_observation_set_dir(target_path, base_dir=base_dir)
        _ensure_validation_passes(result, context="Observation event append", snapshot=snapshot)
    except Exception:
        _restore(snapshot)
        raise
    return target_path


def materialize_recommendation_packet(
    target_dir: str | Path,
    *,
    identity: dict[str, Any],
    status: dict[str, Any],
    first_event: dict[str, Any],
    handoff_note: str,
    base_dir: Path = BASE_DIR,
) -> Path:
    target_path, rel = _resolve_repo_dir(target_dir, base_dir=base_dir, root_rel=RECOMMENDATION_ROOT)
    expected_slug = target_path.name
    identity_body = _ensure_recommendation_identity_safe(identity, rel, expected_slug)
    status_body = _ensure_recommendation_status_consistent(status, identity_body)

    identity_path = target_path / "RECOMMENDATION_IDENTITY.yaml"
    status_path = target_path / "RECOMMENDATION_STATUS.yaml"
    events_path = target_path / "RECOMMENDATION_EVENTS.yaml"
    handoff_path = target_path / "HANDOFF_NOTE.md"
    if any(path.exists() for path in (identity_path, status_path, events_path, handoff_path)):
        raise CaniWriterError("Recommendation packet already exists. Use append_recommendation_event or update_recommendation_status.")

    events_doc = {
        "storage_schema_version": identity_body["storage_schema_version"],
        "recommendation_id": identity_body["recommendation_id"],
        "recommendation_slug": identity_body["recommendation_slug"],
        "events": [deepcopy(first_event)],
    }

    snapshot = _snapshot([identity_path, status_path, events_path, handoff_path])
    try:
        _write_yaml(identity_path, identity_body)
        _write_yaml(status_path, status_body)
        _write_yaml(events_path, events_doc)
        _write_text(handoff_path, handoff_note)
        result = validate_recommendation_dir(target_path, base_dir=base_dir)
        _ensure_validation_passes(result, context="Recommendation packet materialization", snapshot=snapshot)
    except Exception:
        _restore(snapshot)
        raise
    return target_path


def append_recommendation_event(
    target_dir: str | Path,
    *,
    event: dict[str, Any],
    base_dir: Path = BASE_DIR,
) -> Path:
    target_path, _ = _resolve_repo_dir(target_dir, base_dir=base_dir, root_rel=RECOMMENDATION_ROOT)
    current = validate_recommendation_dir(target_path, base_dir=base_dir)
    if current.outcome in {"fail", "blocked"}:
        raise CaniWriterError("Cannot append to a recommendation packet that does not currently validate.")

    events_path = target_path / "RECOMMENDATION_EVENTS.yaml"
    snapshot = _snapshot([events_path])
    try:
        events_doc = _load_existing_yaml(events_path)
        events = list(events_doc.get("events") or [])
        events.append(deepcopy(event))
        events_doc["events"] = events
        _write_yaml(events_path, events_doc)
        result = validate_recommendation_dir(target_path, base_dir=base_dir)
        _ensure_validation_passes(result, context="Recommendation event append", snapshot=snapshot)
    except Exception:
        _restore(snapshot)
        raise
    return target_path


def update_recommendation_status(
    target_dir: str | Path,
    *,
    status: dict[str, Any],
    base_dir: Path = BASE_DIR,
) -> Path:
    target_path, _ = _resolve_repo_dir(target_dir, base_dir=base_dir, root_rel=RECOMMENDATION_ROOT)
    identity_path = target_path / "RECOMMENDATION_IDENTITY.yaml"
    status_path = target_path / "RECOMMENDATION_STATUS.yaml"

    identity = _load_existing_yaml(identity_path)
    if not identity:
        raise CaniWriterError("Cannot update recommendation status before the packet is materialized.")
    current_status = _load_existing_yaml(status_path)
    if not current_status:
        raise CaniWriterError("Cannot update recommendation status before RECOMMENDATION_STATUS.yaml exists.")
    status_body = _ensure_recommendation_status_consistent(status, identity)
    _refuse_lifecycle_bearing_recommendation_status_change(current_status, status_body)

    snapshot = _snapshot([status_path])
    try:
        _write_yaml(status_path, status_body)
        result = validate_recommendation_dir(target_path, base_dir=base_dir)
        _ensure_validation_passes(result, context="Recommendation status update", snapshot=snapshot)
    except Exception:
        _restore(snapshot)
        raise
    return target_path
