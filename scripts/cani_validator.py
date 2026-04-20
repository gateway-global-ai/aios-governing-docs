#!/usr/bin/env python3
"""
Runtime validator helpers for CANI artifacts and intake envelopes.

This module implements the first validator-facing slice only:
  - persisted observation artifacts
  - persisted recommendation artifacts
  - telemetry/intake envelopes
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

BASE_DIR = Path(__file__).resolve().parent.parent

VALIDATOR_OUTCOMES = ("pass", "fail", "blocked", "advisory_warning")

PERSISTED_OBSERVATION_ARTIFACT = "persisted_observation_artifact"
PERSISTED_RECOMMENDATION_ARTIFACT = "persisted_recommendation_artifact"
TELEMETRY_INTAKE_ENVELOPE = "telemetry_intake_envelope"

OBSERVATION_IDENTITY_REQUIRED_KEYS = frozenset({
    "observation_set_id",
    "set_slug",
    "storage_schema_version",
    "set_path",
    "source_schema_document_id",
    "created_at",
    "created_by",
})

OBSERVATION_MUTABLE_FORBIDDEN_KEYS = frozenset({
    "authority_status",
    "routing_state",
    "review_status",
    "artifact_health",
    "status_updated_at",
    "status_updated_by",
})

OBSERVATION_EVENT_REQUIRED_KEYS = frozenset({
    "observation_id",
    "observed_at",
    "path_signature",
    "step_action",
    "outcome_state",
    "fallback_occurred",
    "backtrack_occurred",
    "burden_summary",
    "evidence_surface",
    "event_type",
    "event_id",
})

OBSERVATION_EVENT_TYPES = frozenset({
    "observation_recorded",
    "observation_correction_recorded",
    "observation_set_status_corrected",
})

OUTCOME_STATE_VALUES = frozenset({"success", "partial_success", "failed", "abandoned", "unknown"})
EVIDENCE_SURFACE_VALUES = frozenset({"shell", "ui_surface", "planning_artifact", "review_artifact", "operator_note", "unknown"})
CONFIDENCE_VALUES = frozenset({"low", "medium", "high"})
BURDEN_LEVEL_VALUES = frozenset({"low", "medium", "high", "unknown"})
PATH_EFFICIENCY_VALUES = frozenset({"direct", "detoured", "recovered", "stalled", "unknown"})
FALLBACK_TYPE_VALUES = frozenset({"manual_fallback", "broader_path_fallback", "explanation_fallback", "surface_fallback", "unknown"})
REVERSAL_MARKER_VALUES = frozenset({"restart", "undo", "reverse_navigation", "repeat_attempt", "unknown"})
REPEAT_SUCCESS_HINT_VALUES = frozenset({"low", "mixed", "high", "unknown"})
FAMILIARITY_STATE_VALUES = frozenset({"none", "emerging", "engrained", "unknown"})

RECOMMENDATION_IDENTITY_REQUIRED_KEYS = frozenset({
    "recommendation_id",
    "recommendation_slug",
    "storage_schema_version",
    "recommendation_path",
    "source_schema_document_id",
    "created_at",
    "created_by",
    "source_observation_refs",
})

RECOMMENDATION_STATUS_REQUIRED_KEYS = frozenset({
    "recommendation_id",
    "recommendation_slug",
    "authority_status",
    "routing_target",
    "routing_state",
    "review_status",
    "artifact_health",
    "supersedes",
    "superseded_by",
    "status_updated_at",
    "status_updated_by",
})

RECOMMENDATION_STATUS_OPTIONAL_KEYS = frozenset({
    "linked_amendment_slug",
    "linked_planning_path",
    "linked_intake_path",
    "linked_review_path",
    "routing_note",
})

RECOMMENDATION_EVENT_REQUIRED_KEYS = frozenset({
    "event_id",
    "timestamp",
    "actor",
    "event_type",
    "from_state",
    "to_state",
    "summary",
    "evidence_paths",
})

RECOMMENDATION_EVENT_TYPES = frozenset({
    "recommendation_initialized",
    "recommendation_routed",
    "recommendation_accepted_for_planning",
    "recommendation_rejected",
    "recommendation_superseded",
    "recommendation_archived",
    "recommendation_status_corrected",
})

AUTHORITY_STATUS_VALUES = frozenset({
    "advisory_only",
    "routed_for_review",
    "accepted_for_planning",
    "rejected",
    "superseded",
    "archived",
})

ROUTING_TARGET_VALUES = frozenset({
    "architect_planning",
    "ui_planning",
    "amendment_intake",
    "review_preparation",
    "manual_governance_review",
})

ROUTING_STATE_VALUES = frozenset({"proposed", "routed", "accepted", "rejected", "superseded", "archived"})
REVIEW_STATUS_VALUES = frozenset({"not_started", "pending", "in_review", "accepted", "rejected", "superseded", "archived"})
RECOMMENDATION_ARTIFACT_HEALTH_VALUES = frozenset({"healthy", "stale_evidence", "routing_mismatch", "incomplete_packet"})

ENVELOPE_REQUIRED_KEYS = frozenset({
    "ingestion_envelope_id",
    "envelope_schema_version",
    "recorded_at",
    "signal_family",
    "signal_type",
    "source_surface",
    "provenance",
    "sequence",
    "normalization_state",
    "payload_ref",
    "evidence_refs",
})

ENVELOPE_OPTIONAL_KEYS = frozenset({
    "source_artifact_ref",
    "notes",
})

SIGNAL_FAMILY_VALUES = frozenset({"observation_intake", "recommendation_intake", "governance_correction"})
NORMALIZATION_STATE_VALUES = frozenset({"raw_captured", "normalized", "mapped_to_persisted_artifact", "rejected"})
PROVENANCE_REQUIRED_KEYS = frozenset({"admitted_by", "evidence_basis"})
PROVENANCE_OPTIONAL_KEYS = frozenset({"observed_by", "confidence", "interpretation_limit"})
SEQUENCE_REQUIRED_KEYS = frozenset({"stream_key", "sequence_id"})
SEQUENCE_OPTIONAL_KEYS = frozenset({"batch_id", "causal_parent_id", "related_observation_set_id", "related_recommendation_id"})

RECOMMENDATION_HANDOFF_AUTHORITY_HINTS = ("non-authoritative", "yaml")
OBSERVATION_HANDOFF_AUTHORITY_HINTS = ("non-authoritative", "yaml")


@dataclass
class CaniValidationFinding:
    outcome: str
    code: str
    message: str


@dataclass
class CaniValidationResult:
    artifact_class: str
    target_path: str
    findings: list[CaniValidationFinding] = field(default_factory=list)

    @property
    def outcome(self) -> str:
        outcomes = {finding.outcome for finding in self.findings}
        if "fail" in outcomes:
            return "fail"
        if "blocked" in outcomes:
            return "blocked"
        if "advisory_warning" in outcomes:
            return "advisory_warning"
        return "pass"

    def add(self, outcome: str, code: str, message: str) -> None:
        if outcome not in VALIDATOR_OUTCOMES:
            raise ValueError(f"Unsupported validator outcome: {outcome!r}")
        self.findings.append(CaniValidationFinding(outcome=outcome, code=code, message=message))

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_class": self.artifact_class,
            "target_path": self.target_path,
            "outcome": self.outcome,
            "findings": [finding.__dict__ for finding in self.findings],
        }


def _load_yaml_or_json(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def _load_required_structured_file(
    result: CaniValidationResult,
    path: Path,
    *,
    blocked_code: str,
    fail_code: str,
) -> Any | None:
    if not path.exists():
        result.add("blocked", blocked_code, f"Required artifact missing: {path.name}")
        return None
    try:
        return _load_yaml_or_json(path) or {}
    except Exception as exc:
        result.add("fail", fail_code, f"Unreadable structured artifact {path.name}: {exc}")
        return None


def _normalize_repo_rel(path: Path, base_dir: Path) -> str:
    return path.resolve().relative_to(base_dir.resolve()).as_posix()


def _is_external_ref(value: str) -> bool:
    return bool(re.match(r"^[a-z]+://", value.strip(), re.IGNORECASE))


def _resolve_repo_ref(value: str, base_dir: Path) -> Path | None:
    raw = str(value or "").strip()
    if not raw:
        return None
    if _is_external_ref(raw):
        return None
    candidate = Path(raw)
    if candidate.is_absolute():
        try:
            candidate.resolve().relative_to(base_dir.resolve())
        except Exception:
            return None
        return candidate.resolve()
    return (base_dir / candidate).resolve()


def _require_keys(result: CaniValidationResult, label: str, body: dict[str, Any], required: frozenset[str]) -> None:
    missing = sorted(required - set(body.keys()))
    if missing:
        result.add("fail", f"{label}_missing_keys", f"{label} missing required keys: {missing}")


def _warn_extra_keys(result: CaniValidationResult, label: str, body: dict[str, Any], allowed: frozenset[str]) -> None:
    extra = sorted(set(body.keys()) - allowed)
    if extra:
        result.add("advisory_warning", f"{label}_extra_keys", f"{label} has undocumented extra keys: {extra}")


def _check_enum(
    result: CaniValidationResult,
    *,
    label: str,
    key: str,
    value: Any,
    allowed: frozenset[str],
) -> None:
    if value not in allowed:
        result.add("fail", f"{label}_{key}_invalid", f"{label} {key} invalid: {value!r}")


def _check_repo_ref(
    result: CaniValidationResult,
    *,
    code_prefix: str,
    value: Any,
    base_dir: Path,
    required_exists: bool = True,
) -> None:
    raw = str(value or "").strip()
    if not raw:
        return
    if _is_external_ref(raw):
        result.add("fail", f"{code_prefix}_external_ref", f"Reference must remain repo-local and reviewable: {raw}")
        return
    candidate = _resolve_repo_ref(raw, base_dir)
    if candidate is None:
        result.add("fail", f"{code_prefix}_invalid_ref", f"Reference escapes repo authority boundary: {raw}")
        return
    try:
        candidate.relative_to(base_dir.resolve())
    except Exception:
        result.add("fail", f"{code_prefix}_invalid_ref", f"Reference escapes repo authority boundary: {raw}")
        return
    if required_exists and not candidate.exists():
        result.add("blocked", f"{code_prefix}_missing_ref", f"Referenced repo artifact is missing: {raw}")


def _validate_handoff_text(
    result: CaniValidationResult,
    *,
    text: str,
    required: bool,
    advisory_only: bool,
    code_prefix: str,
) -> None:
    normalized = text.lower()
    has_hints = all(hint in normalized for hint in ("yaml", "non-authoritative")) or (
        "yaml" in normalized and "win" in normalized
    )
    if has_hints:
        return
    outcome = "advisory_warning" if advisory_only else "fail"
    message = "HANDOFF_NOTE.md should state non-authoritative posture and YAML precedence."
    result.add(outcome, f"{code_prefix}_handoff_authority_line_missing", message)


def _validate_burden_summary(result: CaniValidationResult, burden: Any, *, label: str) -> None:
    if not isinstance(burden, dict):
        result.add("fail", f"{label}_burden_summary_type", f"{label} burden_summary must be an object")
        return
    required_keys = {
        "visible_burden_level": BURDEN_LEVEL_VALUES,
        "context_burden_level": BURDEN_LEVEL_VALUES,
        "explanation_burden_level": BURDEN_LEVEL_VALUES,
        "path_efficiency_state": PATH_EFFICIENCY_VALUES,
    }
    for key, allowed in required_keys.items():
        if key not in burden:
            result.add("fail", f"{label}_{key}_missing", f"{label} burden_summary missing {key}")
            continue
        _check_enum(result, label=label, key=key, value=burden.get(key), allowed=allowed)


def _validate_repeat_signal(result: CaniValidationResult, repeat_signal: Any, *, label: str) -> None:
    if repeat_signal is None:
        return
    if not isinstance(repeat_signal, dict):
        result.add("fail", f"{label}_repeat_path_signal_type", f"{label} repeat_path_signal must be an object")
        return
    if "repeat_path_observed" not in repeat_signal:
        result.add("fail", f"{label}_repeat_path_observed_missing", f"{label} repeat_path_signal missing repeat_path_observed")
    elif not isinstance(repeat_signal.get("repeat_path_observed"), bool):
        result.add("fail", f"{label}_repeat_path_observed_type", f"{label} repeat_path_observed must be boolean")
    if "repeat_path_success_rate_hint" in repeat_signal:
        _check_enum(
            result,
            label=label,
            key="repeat_path_success_rate_hint",
            value=repeat_signal.get("repeat_path_success_rate_hint"),
            allowed=REPEAT_SUCCESS_HINT_VALUES,
        )
    if "familiarity_state" in repeat_signal:
        _check_enum(
            result,
            label=label,
            key="familiarity_state",
            value=repeat_signal.get("familiarity_state"),
            allowed=FAMILIARITY_STATE_VALUES,
        )


def validate_observation_set_dir(observation_dir: Path, base_dir: Path = BASE_DIR) -> CaniValidationResult:
    result = CaniValidationResult(
        artifact_class=PERSISTED_OBSERVATION_ARTIFACT,
        target_path=str(observation_dir.resolve()),
    )
    identity_path = observation_dir / "OBSERVATION_SET_IDENTITY.yaml"
    events_path = observation_dir / "OBSERVATION_SET_EVENTS.yaml"
    handoff_path = observation_dir / "HANDOFF_NOTE.md"

    identity = _load_required_structured_file(
        result,
        identity_path,
        blocked_code="observation_identity_missing",
        fail_code="observation_identity_unreadable",
    )
    events_doc = _load_required_structured_file(
        result,
        events_path,
        blocked_code="observation_events_missing",
        fail_code="observation_events_unreadable",
    )
    if identity is None or events_doc is None:
        return result

    _require_keys(result, "OBSERVATION_SET_IDENTITY", identity, OBSERVATION_IDENTITY_REQUIRED_KEYS)
    _warn_extra_keys(result, "OBSERVATION_SET_IDENTITY", identity, OBSERVATION_IDENTITY_REQUIRED_KEYS)

    forbidden = sorted(set(identity.keys()) & OBSERVATION_MUTABLE_FORBIDDEN_KEYS)
    if forbidden:
        result.add(
            "fail",
            "observation_identity_mutable_keys_present",
            f"OBSERVATION_SET_IDENTITY.yaml must not hold mutable workflow state: {forbidden}",
        )

    if identity.get("source_schema_document_id") != "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001":
        result.add(
            "fail",
            "observation_identity_source_schema_invalid",
            "OBSERVATION_SET_IDENTITY.yaml source_schema_document_id must reference AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001.",
        )

    expected_set_path = _normalize_repo_rel(observation_dir, base_dir)
    if str(identity.get("set_path") or "") != expected_set_path:
        result.add(
            "fail",
            "observation_identity_set_path_mismatch",
            f"OBSERVATION_SET_IDENTITY.yaml set_path must match actual repo-relative path {expected_set_path!r}.",
        )

    for key in ("linked_planning_path", "linked_intake_path", "linked_review_path"):
        if key in identity:
            _check_repo_ref(result, code_prefix=f"observation_{key}", value=identity.get(key), base_dir=base_dir)
    if "routing_target" in identity:
        _check_enum(result, label="OBSERVATION_SET_IDENTITY", key="routing_target", value=identity.get("routing_target"), allowed=ROUTING_TARGET_VALUES)

    required_top_level = frozenset({"storage_schema_version", "observation_set_id", "set_slug", "events"})
    _require_keys(result, "OBSERVATION_SET_EVENTS", events_doc, required_top_level)
    _warn_extra_keys(result, "OBSERVATION_SET_EVENTS", events_doc, required_top_level)

    if str(events_doc.get("observation_set_id") or "") != str(identity.get("observation_set_id") or ""):
        result.add("fail", "observation_events_id_mismatch", "OBSERVATION_SET_EVENTS.yaml observation_set_id does not match identity.")
    if str(events_doc.get("set_slug") or "") != str(identity.get("set_slug") or ""):
        result.add("fail", "observation_events_slug_mismatch", "OBSERVATION_SET_EVENTS.yaml set_slug does not match identity.")
    if str(events_doc.get("storage_schema_version") or "") != str(identity.get("storage_schema_version") or ""):
        result.add("fail", "observation_events_schema_version_mismatch", "OBSERVATION_SET_EVENTS.yaml storage_schema_version does not match identity.")

    events = events_doc.get("events")
    if not isinstance(events, list) or not events:
        result.add("fail", "observation_events_list_invalid", "OBSERVATION_SET_EVENTS.yaml events must be a non-empty list.")
        events = []

    seen_event_ids: set[str] = set()
    seen_observation_ids: set[str] = set()
    for idx, event in enumerate(events):
        label = f"OBSERVATION_SET_EVENTS events[{idx}]"
        if not isinstance(event, dict):
            result.add("fail", "observation_event_type_invalid", f"{label} must be an object.")
            continue
        _require_keys(result, label, event, OBSERVATION_EVENT_REQUIRED_KEYS)
        _warn_extra_keys(
            result,
            label,
            event,
            OBSERVATION_EVENT_REQUIRED_KEYS
            | frozenset({
                "subject_context",
                "intent_id",
                "repeat_path_signal",
                "interpretation_confidence",
                "notes",
                "supersedes_observation_id",
                "fallback_type",
                "fallback_count",
                "backtrack_count",
                "reversal_marker",
                "linked_planning_path",
                "linked_intake_path",
                "linked_review_path",
                "routing_target",
                "routing_note",
            }),
        )
        _check_enum(result, label=label, key="event_type", value=event.get("event_type"), allowed=OBSERVATION_EVENT_TYPES)
        _check_enum(result, label=label, key="outcome_state", value=event.get("outcome_state"), allowed=OUTCOME_STATE_VALUES)
        _check_enum(result, label=label, key="evidence_surface", value=event.get("evidence_surface"), allowed=EVIDENCE_SURFACE_VALUES)
        if "interpretation_confidence" in event:
            _check_enum(result, label=label, key="interpretation_confidence", value=event.get("interpretation_confidence"), allowed=CONFIDENCE_VALUES)
        if "fallback_type" in event:
            _check_enum(result, label=label, key="fallback_type", value=event.get("fallback_type"), allowed=FALLBACK_TYPE_VALUES)
        if "reversal_marker" in event:
            _check_enum(result, label=label, key="reversal_marker", value=event.get("reversal_marker"), allowed=REVERSAL_MARKER_VALUES)

        if not isinstance(event.get("fallback_occurred"), bool):
            result.add("fail", "observation_fallback_flag_invalid", f"{label} fallback_occurred must be boolean.")
        if not isinstance(event.get("backtrack_occurred"), bool):
            result.add("fail", "observation_backtrack_flag_invalid", f"{label} backtrack_occurred must be boolean.")

        if event.get("fallback_occurred") is False and int(event.get("fallback_count") or 0) > 0:
            result.add("fail", "observation_fallback_count_inconsistent", f"{label} fallback_count cannot be > 0 when fallback_occurred is false.")
        if event.get("backtrack_occurred") is False and int(event.get("backtrack_count") or 0) > 0:
            result.add("fail", "observation_backtrack_count_inconsistent", f"{label} backtrack_count cannot be > 0 when backtrack_occurred is false.")

        _validate_burden_summary(result, event.get("burden_summary"), label=label)
        _validate_repeat_signal(result, event.get("repeat_path_signal"), label=label)

        event_id = str(event.get("event_id") or "")
        if event_id in seen_event_ids:
            result.add("fail", "observation_event_id_duplicate", f"{label} event_id must be unique within the observation set.")
        seen_event_ids.add(event_id)

        observation_id = str(event.get("observation_id") or "")
        if event.get("event_type") == "observation_recorded" and observation_id in seen_observation_ids:
            result.add("fail", "observation_id_duplicate", f"{label} observation_id must not be silently rewritten or reused.")
        if event.get("event_type") == "observation_correction_recorded":
            supersedes = str(event.get("supersedes_observation_id") or "")
            if not supersedes:
                result.add("fail", "observation_correction_missing_supersedes", f"{label} correction events require supersedes_observation_id.")
            elif supersedes not in seen_observation_ids:
                result.add("fail", "observation_correction_unknown_target", f"{label} supersedes_observation_id must refer to a previously recorded observation.")
        seen_observation_ids.add(observation_id)

        for path_key in ("linked_planning_path", "linked_intake_path", "linked_review_path"):
            if path_key in event:
                _check_repo_ref(result, code_prefix=f"observation_{path_key}", value=event.get(path_key), base_dir=base_dir)
        if "routing_target" in event:
            _check_enum(result, label=label, key="routing_target", value=event.get("routing_target"), allowed=ROUTING_TARGET_VALUES)

    if handoff_path.exists():
        try:
            handoff = handoff_path.read_text(encoding="utf-8")
        except Exception as exc:
            result.add("fail", "observation_handoff_unreadable", f"HANDOFF_NOTE.md unreadable: {exc}")
        else:
            _validate_handoff_text(
                result,
                text=handoff,
                required=False,
                advisory_only=True,
                code_prefix="observation",
            )

    return result


def validate_recommendation_dir(recommendation_dir: Path, base_dir: Path = BASE_DIR) -> CaniValidationResult:
    result = CaniValidationResult(
        artifact_class=PERSISTED_RECOMMENDATION_ARTIFACT,
        target_path=str(recommendation_dir.resolve()),
    )
    identity_path = recommendation_dir / "RECOMMENDATION_IDENTITY.yaml"
    status_path = recommendation_dir / "RECOMMENDATION_STATUS.yaml"
    events_path = recommendation_dir / "RECOMMENDATION_EVENTS.yaml"
    handoff_path = recommendation_dir / "HANDOFF_NOTE.md"

    identity = _load_required_structured_file(
        result,
        identity_path,
        blocked_code="recommendation_identity_missing",
        fail_code="recommendation_identity_unreadable",
    )
    status = _load_required_structured_file(
        result,
        status_path,
        blocked_code="recommendation_status_missing",
        fail_code="recommendation_status_unreadable",
    )
    events_doc = _load_required_structured_file(
        result,
        events_path,
        blocked_code="recommendation_events_missing",
        fail_code="recommendation_events_unreadable",
    )
    if not handoff_path.exists():
        result.add("blocked", "recommendation_handoff_missing", "Required artifact missing: HANDOFF_NOTE.md")
    elif identity is None or status is None or events_doc is None:
        return result

    if identity is None or status is None or events_doc is None:
        return result

    _require_keys(result, "RECOMMENDATION_IDENTITY", identity, RECOMMENDATION_IDENTITY_REQUIRED_KEYS)
    _warn_extra_keys(result, "RECOMMENDATION_IDENTITY", identity, RECOMMENDATION_IDENTITY_REQUIRED_KEYS)

    forbidden_identity_status_keys = (RECOMMENDATION_STATUS_REQUIRED_KEYS - {"recommendation_id", "recommendation_slug"}) | RECOMMENDATION_STATUS_OPTIONAL_KEYS
    forbidden = sorted(set(identity.keys()) & forbidden_identity_status_keys)
    if forbidden:
        result.add(
            "fail",
            "recommendation_identity_mutable_keys_present",
            f"RECOMMENDATION_IDENTITY.yaml must not hold mutable routing or review status: {forbidden}",
        )

    if identity.get("source_schema_document_id") != "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001":
        result.add(
            "fail",
            "recommendation_identity_source_schema_invalid",
            "RECOMMENDATION_IDENTITY.yaml source_schema_document_id must reference AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001.",
        )

    expected_path = _normalize_repo_rel(recommendation_dir, base_dir)
    if str(identity.get("recommendation_path") or "") != expected_path:
        result.add(
            "fail",
            "recommendation_identity_path_mismatch",
            f"RECOMMENDATION_IDENTITY.yaml recommendation_path must match actual repo-relative path {expected_path!r}.",
        )

    source_refs = identity.get("source_observation_refs")
    if not isinstance(source_refs, list) or not source_refs or not all(str(ref).strip() for ref in source_refs):
        result.add("fail", "recommendation_identity_source_refs_invalid", "RECOMMENDATION_IDENTITY.yaml source_observation_refs must be a non-empty list.")

    _require_keys(result, "RECOMMENDATION_STATUS", status, RECOMMENDATION_STATUS_REQUIRED_KEYS)
    _warn_extra_keys(
        result,
        "RECOMMENDATION_STATUS",
        status,
        RECOMMENDATION_STATUS_REQUIRED_KEYS | RECOMMENDATION_STATUS_OPTIONAL_KEYS,
    )

    if str(status.get("recommendation_id") or "") != str(identity.get("recommendation_id") or ""):
        result.add("fail", "recommendation_status_id_mismatch", "RECOMMENDATION_STATUS.yaml recommendation_id does not match identity.")
    if str(status.get("recommendation_slug") or "") != str(identity.get("recommendation_slug") or ""):
        result.add("fail", "recommendation_status_slug_mismatch", "RECOMMENDATION_STATUS.yaml recommendation_slug does not match identity.")

    _check_enum(result, label="RECOMMENDATION_STATUS", key="authority_status", value=status.get("authority_status"), allowed=AUTHORITY_STATUS_VALUES)
    _check_enum(result, label="RECOMMENDATION_STATUS", key="routing_target", value=status.get("routing_target"), allowed=ROUTING_TARGET_VALUES)
    _check_enum(result, label="RECOMMENDATION_STATUS", key="routing_state", value=status.get("routing_state"), allowed=ROUTING_STATE_VALUES)
    _check_enum(result, label="RECOMMENDATION_STATUS", key="review_status", value=status.get("review_status"), allowed=REVIEW_STATUS_VALUES)
    _check_enum(result, label="RECOMMENDATION_STATUS", key="artifact_health", value=status.get("artifact_health"), allowed=RECOMMENDATION_ARTIFACT_HEALTH_VALUES)

    authority = status.get("authority_status")
    routing_state = status.get("routing_state")
    review_status = status.get("review_status")
    if authority == "advisory_only" and routing_state != "proposed":
        result.add("fail", "recommendation_authority_routing_mismatch", "advisory_only recommendations must remain in proposed routing_state.")
    if authority == "routed_for_review" and routing_state != "routed":
        result.add("fail", "recommendation_routed_state_mismatch", "routed_for_review recommendations must use routing_state routed.")
    if authority == "accepted_for_planning":
        if routing_state != "accepted" or review_status != "accepted":
            result.add("fail", "recommendation_accepted_state_mismatch", "accepted_for_planning requires accepted routing_state and accepted review_status.")
    if authority == "rejected":
        if routing_state != "rejected" or review_status != "rejected":
            result.add("fail", "recommendation_rejected_state_mismatch", "rejected recommendations must use rejected routing_state and rejected review_status.")
    if authority == "superseded":
        if routing_state != "superseded" or review_status != "superseded":
            result.add("fail", "recommendation_superseded_state_mismatch", "superseded recommendations must use superseded routing_state and review_status.")
        if not str(status.get("superseded_by") or "").strip():
            result.add("fail", "recommendation_superseded_by_missing", "superseded recommendations require superseded_by.")
    if authority == "archived":
        if routing_state != "archived" or review_status != "archived":
            result.add("fail", "recommendation_archived_state_mismatch", "archived recommendations must use archived routing_state and review_status.")

    if routing_state in {"routed", "accepted"}:
        route_evidence = any(str(status.get(key) or "").strip() for key in RECOMMENDATION_STATUS_OPTIONAL_KEYS if key != "routing_note")
        if not route_evidence:
            result.add(
                "blocked",
                "recommendation_routing_link_missing",
                "Routed or accepted recommendation packets must expose a governed routing link.",
            )

    for key in ("linked_planning_path", "linked_intake_path", "linked_review_path"):
        if key in status:
            _check_repo_ref(result, code_prefix=f"recommendation_{key}", value=status.get(key), base_dir=base_dir)

    _require_keys(result, "RECOMMENDATION_EVENTS", events_doc, frozenset({"storage_schema_version", "recommendation_id", "recommendation_slug", "events"}))
    _warn_extra_keys(result, "RECOMMENDATION_EVENTS", events_doc, frozenset({"storage_schema_version", "recommendation_id", "recommendation_slug", "events"}))

    if str(events_doc.get("recommendation_id") or "") != str(identity.get("recommendation_id") or ""):
        result.add("fail", "recommendation_events_id_mismatch", "RECOMMENDATION_EVENTS.yaml recommendation_id does not match identity.")
    if str(events_doc.get("recommendation_slug") or "") != str(identity.get("recommendation_slug") or ""):
        result.add("fail", "recommendation_events_slug_mismatch", "RECOMMENDATION_EVENTS.yaml recommendation_slug does not match identity.")

    events = events_doc.get("events")
    if not isinstance(events, list) or not events:
        result.add("fail", "recommendation_events_list_invalid", "RECOMMENDATION_EVENTS.yaml events must be a non-empty list.")
        events = []

    seen_event_ids: set[str] = set()
    previous_state: str | None = None
    for idx, event in enumerate(events):
        label = f"RECOMMENDATION_EVENTS events[{idx}]"
        if not isinstance(event, dict):
            result.add("fail", "recommendation_event_type_invalid", f"{label} must be an object.")
            continue
        _require_keys(result, label, event, RECOMMENDATION_EVENT_REQUIRED_KEYS)
        _warn_extra_keys(result, label, event, RECOMMENDATION_EVENT_REQUIRED_KEYS)
        _check_enum(result, label=label, key="event_type", value=event.get("event_type"), allowed=RECOMMENDATION_EVENT_TYPES)
        _check_enum(result, label=label, key="from_state", value=event.get("from_state"), allowed=ROUTING_STATE_VALUES | frozenset({""}))
        _check_enum(result, label=label, key="to_state", value=event.get("to_state"), allowed=ROUTING_STATE_VALUES)

        event_id = str(event.get("event_id") or "")
        if event_id in seen_event_ids:
            result.add("fail", "recommendation_event_id_duplicate", f"{label} event_id must be unique.")
        seen_event_ids.add(event_id)

        if previous_state is not None and event.get("from_state") != previous_state:
            result.add(
                "fail",
                "recommendation_event_chain_broken",
                f"{label} from_state must continue the previous event to_state.",
            )
        previous_state = str(event.get("to_state") or "")

        evidence_paths = event.get("evidence_paths")
        if not isinstance(evidence_paths, list):
            result.add("fail", "recommendation_event_evidence_paths_invalid", f"{label} evidence_paths must be a list.")
        else:
            for evidence_path in evidence_paths:
                if str(evidence_path or "").strip():
                    _check_repo_ref(result, code_prefix="recommendation_event_evidence", value=evidence_path, base_dir=base_dir)

        expected_states = {
            "recommendation_initialized": "proposed",
            "recommendation_routed": "routed",
            "recommendation_accepted_for_planning": "accepted",
            "recommendation_rejected": "rejected",
            "recommendation_superseded": "superseded",
            "recommendation_archived": "archived",
        }
        event_type = event.get("event_type")
        expected_state = expected_states.get(event_type)
        if expected_state and event.get("to_state") != expected_state:
            result.add("fail", "recommendation_event_state_mismatch", f"{label} {event_type} must transition to {expected_state}.")

    if events and str(events[-1].get("to_state") or "") != str(status.get("routing_state") or ""):
        result.add("fail", "recommendation_latest_state_mismatch", "Latest recommendation event to_state must match RECOMMENDATION_STATUS routing_state.")

    try:
        handoff = handoff_path.read_text(encoding="utf-8")
    except Exception as exc:
        result.add("fail", "recommendation_handoff_unreadable", f"HANDOFF_NOTE.md unreadable: {exc}")
    else:
        _validate_handoff_text(
            result,
            text=handoff,
            required=True,
            advisory_only=False,
            code_prefix="recommendation",
        )

    return result


def validate_intake_envelope_path(envelope_path: Path, base_dir: Path = BASE_DIR) -> CaniValidationResult:
    result = CaniValidationResult(
        artifact_class=TELEMETRY_INTAKE_ENVELOPE,
        target_path=str(envelope_path.resolve()),
    )
    body = _load_required_structured_file(
        result,
        envelope_path,
        blocked_code="intake_envelope_missing",
        fail_code="intake_envelope_unreadable",
    )
    if body is None:
        return result
    if not isinstance(body, dict):
        result.add("fail", "intake_envelope_type_invalid", "Intake envelope must be a mapping/object.")
        return result

    _require_keys(result, "INTAKE_ENVELOPE", body, ENVELOPE_REQUIRED_KEYS)
    _warn_extra_keys(result, "INTAKE_ENVELOPE", body, ENVELOPE_REQUIRED_KEYS | ENVELOPE_OPTIONAL_KEYS)

    _check_enum(result, label="INTAKE_ENVELOPE", key="signal_family", value=body.get("signal_family"), allowed=SIGNAL_FAMILY_VALUES)
    _check_enum(result, label="INTAKE_ENVELOPE", key="source_surface", value=body.get("source_surface"), allowed=EVIDENCE_SURFACE_VALUES)
    _check_enum(result, label="INTAKE_ENVELOPE", key="normalization_state", value=body.get("normalization_state"), allowed=NORMALIZATION_STATE_VALUES)

    provenance = body.get("provenance")
    if not isinstance(provenance, dict):
        result.add("fail", "intake_envelope_provenance_invalid", "INTAKE_ENVELOPE provenance must be an object.")
    else:
        _require_keys(result, "INTAKE_ENVELOPE provenance", provenance, PROVENANCE_REQUIRED_KEYS)
        _warn_extra_keys(result, "INTAKE_ENVELOPE provenance", provenance, PROVENANCE_REQUIRED_KEYS | PROVENANCE_OPTIONAL_KEYS)
        if "confidence" in provenance:
            _check_enum(result, label="INTAKE_ENVELOPE provenance", key="confidence", value=provenance.get("confidence"), allowed=CONFIDENCE_VALUES)

    sequence = body.get("sequence")
    if not isinstance(sequence, dict):
        result.add("fail", "intake_envelope_sequence_invalid", "INTAKE_ENVELOPE sequence must be an object.")
        sequence = {}
    else:
        _require_keys(result, "INTAKE_ENVELOPE sequence", sequence, SEQUENCE_REQUIRED_KEYS)
        _warn_extra_keys(result, "INTAKE_ENVELOPE sequence", sequence, SEQUENCE_REQUIRED_KEYS | SEQUENCE_OPTIONAL_KEYS)
        sequence_id = sequence.get("sequence_id")
        if not isinstance(sequence_id, int) or sequence_id < 1:
            result.add("fail", "intake_envelope_sequence_id_invalid", "INTAKE_ENVELOPE sequence.sequence_id must be an integer >= 1.")

    payload_ref = str(body.get("payload_ref") or "").strip()
    if not payload_ref:
        result.add("fail", "intake_envelope_payload_ref_missing", "INTAKE_ENVELOPE payload_ref is required.")
    elif _is_external_ref(payload_ref):
        result.add("fail", "intake_envelope_payload_ref_external_authority", "payload_ref must remain repo-local and reviewable, not an external authority surface.")
    else:
        payload_candidate = _resolve_repo_ref(payload_ref, base_dir)
        if payload_candidate is None:
            result.add("fail", "intake_envelope_payload_ref_invalid", "payload_ref escapes the repo authority boundary.")
        else:
            try:
                payload_candidate.relative_to(base_dir.resolve())
            except Exception:
                result.add("fail", "intake_envelope_payload_ref_invalid", "payload_ref escapes the repo authority boundary.")
            else:
                if not payload_candidate.exists():
                    result.add("blocked", "intake_envelope_payload_ref_missing_target", f"payload_ref target is missing: {payload_ref}")

    evidence_refs = body.get("evidence_refs")
    if not isinstance(evidence_refs, list) or not evidence_refs:
        result.add("fail", "intake_envelope_evidence_refs_invalid", "INTAKE_ENVELOPE evidence_refs must be a non-empty list.")
    else:
        for evidence_ref in evidence_refs:
            _check_repo_ref(result, code_prefix="intake_envelope_evidence_ref", value=evidence_ref, base_dir=base_dir)

    if "source_artifact_ref" in body:
        _check_repo_ref(result, code_prefix="intake_envelope_source_artifact_ref", value=body.get("source_artifact_ref"), base_dir=base_dir)

    normalization_state = body.get("normalization_state")
    related_observation_set_id = str(sequence.get("related_observation_set_id") or "").strip()
    related_recommendation_id = str(sequence.get("related_recommendation_id") or "").strip()
    signal_family = body.get("signal_family")

    if normalization_state == "mapped_to_persisted_artifact":
        if signal_family == "observation_intake" and not related_observation_set_id:
            result.add(
                "fail",
                "intake_envelope_mapped_observation_target_missing",
                "Mapped observation_intake envelopes require related_observation_set_id.",
            )
        if signal_family == "recommendation_intake" and not related_recommendation_id:
            result.add(
                "fail",
                "intake_envelope_mapped_recommendation_target_missing",
                "Mapped recommendation_intake envelopes require related_recommendation_id.",
            )
        if signal_family == "governance_correction" and not (related_observation_set_id or related_recommendation_id):
            result.add(
                "fail",
                "intake_envelope_governance_correction_target_missing",
                "Mapped governance_correction envelopes require a related observation or recommendation target.",
            )
    if normalization_state == "rejected" and (related_observation_set_id or related_recommendation_id):
        result.add(
            "fail",
            "intake_envelope_rejected_mapping_conflict",
            "Rejected intake envelopes must not claim mapping into persisted artifacts.",
        )

    return result


def detect_cani_artifact_class(path: Path) -> str:
    if path.is_dir():
        if (path / "OBSERVATION_SET_IDENTITY.yaml").exists() or (path / "OBSERVATION_SET_EVENTS.yaml").exists():
            return PERSISTED_OBSERVATION_ARTIFACT
        if (path / "RECOMMENDATION_IDENTITY.yaml").exists() or (path / "RECOMMENDATION_STATUS.yaml").exists():
            return PERSISTED_RECOMMENDATION_ARTIFACT
    return TELEMETRY_INTAKE_ENVELOPE


def validate_cani_target(
    path: Path,
    *,
    artifact_class: str | None = None,
    base_dir: Path = BASE_DIR,
) -> CaniValidationResult:
    selected = artifact_class or detect_cani_artifact_class(path)
    if selected == PERSISTED_OBSERVATION_ARTIFACT:
        return validate_observation_set_dir(path, base_dir=base_dir)
    if selected == PERSISTED_RECOMMENDATION_ARTIFACT:
        return validate_recommendation_dir(path, base_dir=base_dir)
    if selected == TELEMETRY_INTAKE_ENVELOPE:
        return validate_intake_envelope_path(path, base_dir=base_dir)
    raise ValueError(f"Unsupported CANI artifact class: {selected!r}")
