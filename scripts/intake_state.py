#!/usr/bin/env python3
"""
Schema-aware state helpers for the amendment intake scaffold.

This module owns the intake artifact taxonomy:
  - INTAKE_IDENTITY.yaml
  - INTAKE_STATUS.yaml
  - INTAKE_EVENTS.yaml
  - HANDOFF_NOTE.md
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from intake_paths import IntakePaths

INTAKE_SCHEMA_VERSION_CURRENT = "1"
HANDOFF_AUTHORITY_LINE = "If this note contradicts `INTAKE_STATUS.yaml` or `INTAKE_EVENTS.yaml`, the YAML artifacts win."

INTAKE_IDENTITY_ALLOWED_KEYS = frozenset({
    "document_id",
    "document_path",
    "amendment_slug",
    "intake_schema_version",
    "intake_path",
    "planning_path",
    "kernel_path",
    "ratification_path",
    "current_head_version",
    "created_at",
    "created_by",
})

INTAKE_STATUS_REQUIRED_KEYS = frozenset({
    "document_id",
    "amendment_slug",
    "lifecycle_state",
    "artifact_health",
    "committee_status",
    "architect_verification_status",
    "ui_verification_status",
    "kernel_status",
    "peer_review_status",
    "ratification_handoff_status",
    "next_action",
    "current_head_version",
    "last_reviewed_version",
    "status_updated_at",
    "status_updated_by",
})

INTAKE_STATUS_OPTIONAL_KEYS = frozenset({
    "architect_verified_by",
    "architect_verified_at",
    "ui_verified_by",
    "ui_verified_at",
    "committee_recorded_by",
    "committee_recorded_at",
    "committee_note",
    "kernel_skip_reason",
    "phase_ledger",
})

INTAKE_STATUS_ALLOWED_KEYS = INTAKE_STATUS_REQUIRED_KEYS | INTAKE_STATUS_OPTIONAL_KEYS

INTAKE_EVENTS_TOP_LEVEL_KEYS = frozenset({
    "intake_schema_version",
    "document_id",
    "amendment_slug",
    "events",
})

INTAKE_EVENT_REQUIRED_KEYS = frozenset({
    "event_id",
    "timestamp",
    "actor",
    "event_type",
    "from_state",
    "to_state",
    "summary",
    "evidence_paths",
})

INTAKE_EVENT_OPTIONAL_KEYS = frozenset({
    "phase_id",
})

INTAKE_EVENT_ALLOWED_KEYS = INTAKE_EVENT_REQUIRED_KEYS | INTAKE_EVENT_OPTIONAL_KEYS

LIFECYCLE_STATES = frozenset({
    "intake_open",
    "blocked_missing_inputs",
    "phase_a_evidence_pending",
    "phase_a_evidence_ready",
    "phase_b_architect_pending",
    "phase_b_architect_drafted",
    "blocked_architect_human_verification",
    "phase_c_ui_pending",
    "phase_c_ui_drafted",
    "blocked_ui_human_verification",
    "phase_d_committee_pending",
    "blocked_committee_manual",
    "phase_d_committee_approved",
    "phase_e_author_revision_pending",
    "blocked_author_revision_manual",
    "phase_f_peer_review_pending",
    "blocked_peer_review_credentials",
    "phase_f_peer_review_running",
    "phase_f_peer_review_complete",
    "blocked_packet_invalid",
    "kernel_review_pending",
    "kernel_review_advisory_complete",
    "ratification_handoff_pending",
    "blocked_ratification_manual",
    "ratification_handoff_ready",
    "closed_executed",
    "failed",
})

ARTIFACT_HEALTH = frozenset({
    "healthy",
    "stale_supporting_artifacts",
    "identity_mismatch",
    "incomplete_packet",
})

COMMITTEE_STATUS = frozenset({
    "open",
    "answered",
    "closed_superseded_by_review",
    "approved",
    "approved_with_changes",
    "reopened_by_council",
})

ARCHITECT_VERIFICATION_STATUS = frozenset({
    "pending",
    "verified",
    "rejected",
})

UI_VERIFICATION_STATUS = frozenset({
    "pending",
    "verified",
    "rejected",
})

KERNEL_STATUS = frozenset({
    "not_applicable",
    "pending",
    "advisory_complete",
    "skipped_with_reason",
})

PEER_REVIEW_STATUS = frozenset({
    "not_run",
    "running",
    "pass",
    "fail",
    "incomplete",
})

RATIFICATION_HANDOFF_STATUS = frozenset({
    "not_ready",
    "pending_manual",
    "ready",
    "executed",
})

NEXT_ACTIONS = frozenset({
    "build_evidence",
    "run_architect",
    "verify_architect",
    "run_ui",
    "verify_ui",
    "prepare_committee",
    "record_committee",
    "author_revision",
    "run_peer_review_round_1",
    "run_peer_review_round_2",
    "validate_packet",
    "prepare_kernel_review",
    "record_kernel_review",
    "prepare_ratification_handoff",
    "manual_resolution",
    "archive",
})

PHASE_LEDGER_ALLOWED_PHASE_IDS = (
    "discovery",
    "evidence",
    "architect",
    "ui",
    "committee",
    "author_revision",
    "peer_review",
    "kernel",
    "ratification_handoff",
    "review_surface",
)

PHASE_LEDGER_OWNER_ROLES: dict[str, str] = {
    "discovery": "discover agent",
    "evidence": "intake coordinator",
    "architect": "architect planner",
    "ui": "ui planner",
    "committee": "committee reviewer",
    "author_revision": "author / reviser",
    "peer_review": "peer-review coordinator",
    "kernel": "kernel reviewer",
    "ratification_handoff": "ratification coordinator",
    "review_surface": "systems reviewer",
}

PHASE_LEDGER_PHASE_STATUS = frozenset({
    "not_started",
    "in_progress",
    "completed",
    "blocked",
    "failed",
})

PHASE_LEDGER_VERIFICATION_STATUS = frozenset({
    "not_run",
    "running",
    "pass",
    "fail",
    "manual_pending",
    "not_applicable",
})

PHASE_LEDGER_HUMAN_DECISION_STATUS = frozenset({
    "not_required",
    "pending",
    "approved",
    "approved_with_changes",
    "rejected",
    "superseded",
})

INTAKE_EVENT_TYPES = frozenset({
    "intake_initialized",
    "evidence_refreshed",
    "architect_started",
    "architect_drafted",
    "architect_output_verified",
    "architect_output_conformance_validated",
    "architect_output_validation_failed",
    "architect_human_verification_blocked",
    "architect_precondition_blocked",
    "architect_evidence_freshness_blocked",
    "architect_bundle_manifest_mismatch_blocked",
    "architect_input_override_recorded",
    "architect_run_identity_recorded",
    "architect_failed",
    "architect_verified",
    "ui_started",
    "ui_drafted",
    "ui_output_verified",
    "ui_output_conformance_validated",
    "ui_output_validation_failed",
    "ui_human_verification_blocked",
    "ui_precondition_blocked",
    "ui_evidence_freshness_blocked",
    "ui_bundle_manifest_mismatch_blocked",
    "ui_input_override_recorded",
    "ui_run_identity_recorded",
    "ui_failed",
    "ui_verified",
    "committee_packet_prepared",
    "committee_state_recorded",
    "author_revision_flagged",
    "peer_review_started",
    "peer_review_completed",
    "peer_review_packet_validated",
    "peer_review_packet_invalid",
    "kernel_brief_prepared",
    "kernel_findings_recorded",
    "kernel_skipped",
    "ratification_handoff_prepared",
    "intake_status_corrected",
    "intake_validation_passed",
    "intake_validation_failed",
    "phase_verification_started",
    "phase_verification_passed",
    "phase_verification_failed",
    "pre_hitl_report_generated",
})

ALLOWED_LIFECYCLE_TRANSITIONS: dict[str, frozenset[str]] = {
    "intake_open": frozenset({"blocked_missing_inputs", "phase_a_evidence_pending", "phase_a_evidence_ready", "failed"}),
    "blocked_missing_inputs": frozenset({"phase_a_evidence_pending", "phase_a_evidence_ready", "failed"}),
    "phase_a_evidence_pending": frozenset({"phase_a_evidence_ready", "failed"}),
    "phase_a_evidence_ready": frozenset({"phase_b_architect_pending", "failed"}),
    "phase_b_architect_pending": frozenset({"phase_b_architect_drafted", "failed"}),
    "phase_b_architect_drafted": frozenset({"blocked_architect_human_verification", "failed"}),
    "blocked_architect_human_verification": frozenset({"phase_c_ui_pending", "phase_b_architect_pending", "failed"}),
    "phase_c_ui_pending": frozenset({"phase_c_ui_drafted", "failed"}),
    "phase_c_ui_drafted": frozenset({"blocked_ui_human_verification", "failed"}),
    "blocked_ui_human_verification": frozenset({"phase_d_committee_pending", "phase_b_architect_pending", "failed"}),
    "phase_d_committee_pending": frozenset({"blocked_committee_manual", "failed"}),
    "blocked_committee_manual": frozenset({"phase_d_committee_approved", "phase_b_architect_pending", "failed"}),
    "phase_d_committee_approved": frozenset({"phase_e_author_revision_pending", "failed"}),
    "phase_e_author_revision_pending": frozenset({"blocked_author_revision_manual", "phase_f_peer_review_pending", "failed"}),
    "blocked_author_revision_manual": frozenset({"phase_f_peer_review_pending", "failed"}),
    "phase_f_peer_review_pending": frozenset({"blocked_peer_review_credentials", "phase_f_peer_review_running", "failed"}),
    "blocked_peer_review_credentials": frozenset({"phase_f_peer_review_running", "failed"}),
    "phase_f_peer_review_running": frozenset({"phase_f_peer_review_complete", "blocked_packet_invalid", "failed"}),
    "phase_f_peer_review_complete": frozenset({"kernel_review_pending", "ratification_handoff_pending", "failed"}),
    "blocked_packet_invalid": frozenset({"phase_f_peer_review_pending", "failed"}),
    "kernel_review_pending": frozenset({"kernel_review_advisory_complete", "ratification_handoff_pending", "failed"}),
    "kernel_review_advisory_complete": frozenset({"ratification_handoff_pending", "failed"}),
    "ratification_handoff_pending": frozenset({"blocked_ratification_manual", "ratification_handoff_ready", "failed"}),
    "blocked_ratification_manual": frozenset({"ratification_handoff_ready", "closed_executed", "failed"}),
    "ratification_handoff_ready": frozenset({"closed_executed", "failed"}),
    "closed_executed": frozenset(),
    "failed": frozenset({"phase_a_evidence_pending", "phase_b_architect_pending", "phase_f_peer_review_pending"}),
}

ALLOWED_COMMITTEE_TRANSITIONS: dict[str, frozenset[str]] = {
    "open": frozenset({"answered", "approved", "approved_with_changes", "closed_superseded_by_review"}),
    "answered": frozenset({"approved", "approved_with_changes", "closed_superseded_by_review"}),
    "approved": frozenset({"reopened_by_council"}),
    "approved_with_changes": frozenset({"reopened_by_council"}),
    "closed_superseded_by_review": frozenset({"reopened_by_council"}),
    "reopened_by_council": frozenset({"answered", "approved", "approved_with_changes", "closed_superseded_by_review"}),
}

DEFAULT_HANDOFF_NOTE = """# Intake handoff note (non-authoritative)

If this note contradicts `INTAKE_STATUS.yaml` or `INTAKE_EVENTS.yaml`, the YAML artifacts win.

- Use this folder for orchestration state only.
- Binding peer review remains under `reviews/<slug>/round_1/` and `round_2/`.
- Ratification remains a distinct manual handoff and approval path.
"""


class IntakeStateError(ValueError):
    """Raised when intake state or schema validation fails."""


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_event_id(events: list[dict[str, Any]]) -> str:
    return f"evt-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{len(events) + 1:03d}"


def _assert_exact_keys(label: str, actual: set[str], allowed: frozenset[str]) -> None:
    extra = actual - allowed
    if extra:
        raise IntakeStateError(f"{label} has disallowed keys: {sorted(extra)}")


def _require_keys(label: str, actual: set[str], required: frozenset[str]) -> None:
    missing = required - actual
    if missing:
        raise IntakeStateError(f"{label} missing keys: {sorted(missing)}")


def make_initial_phase_ledger() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for index, phase_id in enumerate(PHASE_LEDGER_ALLOWED_PHASE_IDS, start=1):
        records.append({
            "phase_id": phase_id,
            "sequence_index": index,
            "owner_role": PHASE_LEDGER_OWNER_ROLES[phase_id],
            "phase_status": "not_started",
            "started_at": "",
            "completed_at": "",
            "verification_status": "not_run",
            "verification_run_at": "",
            "verification_actor": "",
            "evidence_paths": [],
            "pre_hitl_report_path": "",
            "human_decision_status": "not_required",
        })
    return records


def validate_phase_ledger(phase_ledger: Any) -> None:
    if not isinstance(phase_ledger, list):
        raise IntakeStateError("INTAKE_STATUS phase_ledger must be a list")

    expected_ids = set(PHASE_LEDGER_ALLOWED_PHASE_IDS)
    seen_ids: set[str] = set()
    sequence_numbers: list[int] = []
    required_keys = {
        "phase_id",
        "sequence_index",
        "owner_role",
        "phase_status",
        "started_at",
        "completed_at",
        "verification_status",
        "verification_run_at",
        "verification_actor",
        "evidence_paths",
        "pre_hitl_report_path",
        "human_decision_status",
    }

    for index, record in enumerate(phase_ledger):
        label = f"INTAKE_STATUS phase_ledger[{index}]"
        if not isinstance(record, dict):
            raise IntakeStateError(f"{label} must be an object")
        actual_keys = set(record.keys())
        extra = actual_keys - required_keys
        if extra:
            raise IntakeStateError(f"{label} has disallowed keys: {sorted(extra)}")
        missing = required_keys - actual_keys
        if missing:
            raise IntakeStateError(f"{label} missing keys: {sorted(missing)}")

        phase_id = str(record.get("phase_id") or "")
        if phase_id not in expected_ids:
            raise IntakeStateError(f"{label} invalid phase_id: {phase_id!r}")
        if phase_id in seen_ids:
            raise IntakeStateError(f"{label} duplicates phase_id: {phase_id!r}")
        seen_ids.add(phase_id)

        sequence_index = record.get("sequence_index")
        if not isinstance(sequence_index, int):
            raise IntakeStateError(f"{label} sequence_index must be an integer")
        sequence_numbers.append(sequence_index)

        owner_role = str(record.get("owner_role") or "").strip()
        if not owner_role:
            raise IntakeStateError(f"{label} owner_role must be non-empty")

        phase_status = record.get("phase_status")
        if phase_status not in PHASE_LEDGER_PHASE_STATUS:
            raise IntakeStateError(f"{label} invalid phase_status: {phase_status!r}")

        verification_status = record.get("verification_status")
        if verification_status not in PHASE_LEDGER_VERIFICATION_STATUS:
            raise IntakeStateError(f"{label} invalid verification_status: {verification_status!r}")

        human_decision_status = record.get("human_decision_status")
        if human_decision_status not in PHASE_LEDGER_HUMAN_DECISION_STATUS:
            raise IntakeStateError(f"{label} invalid human_decision_status: {human_decision_status!r}")

        evidence_paths = record.get("evidence_paths")
        if not isinstance(evidence_paths, list):
            raise IntakeStateError(f"{label} evidence_paths must be a list")

        started_at = str(record.get("started_at") or "")
        completed_at = str(record.get("completed_at") or "")
        verification_run_at = str(record.get("verification_run_at") or "")
        verification_actor = str(record.get("verification_actor") or "")
        pre_hitl_report_path = str(record.get("pre_hitl_report_path") or "")

        if phase_status in {"in_progress", "completed", "blocked", "failed"} and not started_at:
            raise IntakeStateError(f"{label} requires started_at when phase_status is {phase_status!r}")
        if phase_status == "completed" and not completed_at:
            raise IntakeStateError(f"{label} requires completed_at when phase_status is 'completed'")
        if completed_at and not started_at:
            raise IntakeStateError(f"{label} completed_at requires started_at")

        if verification_status in {"running", "pass", "fail"} and not verification_run_at:
            raise IntakeStateError(
                f"{label} requires verification_run_at when verification_status is {verification_status!r}"
            )
        if verification_status in {"pass", "fail"} and not verification_actor:
            raise IntakeStateError(
                f"{label} requires verification_actor when verification_status is {verification_status!r}"
            )
        if pre_hitl_report_path and phase_status not in {"completed", "blocked"}:
            raise IntakeStateError(
                f"{label} pre_hitl_report_path requires phase_status 'completed' or 'blocked'"
            )

    if seen_ids != expected_ids:
        missing_ids = sorted(expected_ids - seen_ids)
        raise IntakeStateError(f"INTAKE_STATUS phase_ledger missing phase rows: {missing_ids}")
    if sorted(sequence_numbers) != list(range(1, len(PHASE_LEDGER_ALLOWED_PHASE_IDS) + 1)):
        raise IntakeStateError("INTAKE_STATUS phase_ledger sequence_index values must be contiguous starting at 1")


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        raise IntakeStateError(f"Unreadable YAML: {path}: {exc}") from exc


def _write_yaml(path: Path, body: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.dump(body, default_flow_style=False, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def validate_identity(identity: dict[str, Any]) -> None:
    _assert_exact_keys("INTAKE_IDENTITY", set(identity.keys()), INTAKE_IDENTITY_ALLOWED_KEYS)
    _require_keys("INTAKE_IDENTITY", set(identity.keys()), INTAKE_IDENTITY_ALLOWED_KEYS)
    if str(identity.get("intake_schema_version")) != INTAKE_SCHEMA_VERSION_CURRENT:
        raise IntakeStateError(
            f"INTAKE_IDENTITY intake_schema_version {identity.get('intake_schema_version')!r} != {INTAKE_SCHEMA_VERSION_CURRENT!r}"
        )


def validate_status(status: dict[str, Any]) -> None:
    _assert_exact_keys("INTAKE_STATUS", set(status.keys()), INTAKE_STATUS_ALLOWED_KEYS)
    _require_keys("INTAKE_STATUS", set(status.keys()), INTAKE_STATUS_REQUIRED_KEYS)

    controlled_values = {
        "lifecycle_state": LIFECYCLE_STATES,
        "artifact_health": ARTIFACT_HEALTH,
        "committee_status": COMMITTEE_STATUS,
        "architect_verification_status": ARCHITECT_VERIFICATION_STATUS,
        "ui_verification_status": UI_VERIFICATION_STATUS,
        "kernel_status": KERNEL_STATUS,
        "peer_review_status": PEER_REVIEW_STATUS,
        "ratification_handoff_status": RATIFICATION_HANDOFF_STATUS,
        "next_action": NEXT_ACTIONS,
    }
    for key, allowed in controlled_values.items():
        if status.get(key) not in allowed:
            raise IntakeStateError(f"INTAKE_STATUS {key} invalid: {status.get(key)!r}")

    if status.get("architect_verification_status") == "verified":
        for key in ("architect_verified_by", "architect_verified_at"):
            if not str(status.get(key) or "").strip():
                raise IntakeStateError(f"INTAKE_STATUS requires {key} when architect is verified")

    if status.get("ui_verification_status") == "verified":
        for key in ("ui_verified_by", "ui_verified_at"):
            if not str(status.get(key) or "").strip():
                raise IntakeStateError(f"INTAKE_STATUS requires {key} when UI is verified")

    if status.get("committee_status") != "open":
        for key in ("committee_recorded_by", "committee_recorded_at", "committee_note"):
            if not str(status.get(key) or "").strip():
                raise IntakeStateError(f"INTAKE_STATUS requires {key} when committee state is recorded")

    if status.get("kernel_status") == "skipped_with_reason" and not str(status.get("kernel_skip_reason") or "").strip():
        raise IntakeStateError("INTAKE_STATUS requires kernel_skip_reason when kernel review is skipped")

    if status.get("peer_review_status") == "pass" and status.get("ratification_handoff_status") == "executed":
        # allowed, but only if lifecycle has moved to closed_executed
        if status.get("lifecycle_state") != "closed_executed":
            raise IntakeStateError("INTAKE_STATUS executed ratification requires lifecycle_state closed_executed")

    if status.get("ratification_handoff_status") == "ready" and status.get("lifecycle_state") not in {
        "ratification_handoff_ready",
        "closed_executed",
    }:
        raise IntakeStateError("INTAKE_STATUS handoff ready requires ratification_handoff_ready or closed_executed lifecycle")

    if "phase_ledger" in status:
        validate_phase_ledger(status["phase_ledger"])


def validate_events(events_doc: dict[str, Any]) -> None:
    _assert_exact_keys("INTAKE_EVENTS", set(events_doc.keys()), INTAKE_EVENTS_TOP_LEVEL_KEYS)
    _require_keys("INTAKE_EVENTS", set(events_doc.keys()), INTAKE_EVENTS_TOP_LEVEL_KEYS)

    if str(events_doc.get("intake_schema_version")) != INTAKE_SCHEMA_VERSION_CURRENT:
        raise IntakeStateError(
            f"INTAKE_EVENTS intake_schema_version {events_doc.get('intake_schema_version')!r} != {INTAKE_SCHEMA_VERSION_CURRENT!r}"
        )

    events = events_doc.get("events")
    if not isinstance(events, list):
        raise IntakeStateError("INTAKE_EVENTS events must be a list")

    prev_state = None
    prev_committee = "open"
    for idx, event in enumerate(events):
        if not isinstance(event, dict):
            raise IntakeStateError(f"INTAKE_EVENTS events[{idx}] must be an object")
        _assert_exact_keys(f"INTAKE_EVENTS events[{idx}]", set(event.keys()), INTAKE_EVENT_ALLOWED_KEYS)
        _require_keys(f"INTAKE_EVENTS events[{idx}]", set(event.keys()), INTAKE_EVENT_REQUIRED_KEYS)
        if event.get("event_type") not in INTAKE_EVENT_TYPES:
            raise IntakeStateError(f"INTAKE_EVENTS events[{idx}] invalid event_type: {event.get('event_type')!r}")
        if event.get("from_state") not in LIFECYCLE_STATES and event.get("from_state") not in ("", None):
            raise IntakeStateError(f"INTAKE_EVENTS events[{idx}] invalid from_state: {event.get('from_state')!r}")
        if event.get("to_state") not in LIFECYCLE_STATES:
            raise IntakeStateError(f"INTAKE_EVENTS events[{idx}] invalid to_state: {event.get('to_state')!r}")
        if not isinstance(event.get("evidence_paths"), list):
            raise IntakeStateError(f"INTAKE_EVENTS events[{idx}] evidence_paths must be a list")
        phase_id = str(event.get("phase_id") or "")
        if phase_id and phase_id not in PHASE_LEDGER_ALLOWED_PHASE_IDS:
            raise IntakeStateError(f"INTAKE_EVENTS events[{idx}] invalid phase_id: {phase_id!r}")
        if prev_state is not None and event.get("from_state") != prev_state:
            raise IntakeStateError(
                f"INTAKE_EVENTS events[{idx}] from_state {event.get('from_state')!r} does not continue prior to_state {prev_state!r}"
            )
        if event.get("from_state") and event.get("to_state") != event.get("from_state"):
            allowed = ALLOWED_LIFECYCLE_TRANSITIONS.get(str(event.get("from_state")), frozenset())
            if event.get("to_state") not in allowed:
                raise IntakeStateError(
                    f"INTAKE_EVENTS events[{idx}] illegal lifecycle transition {event.get('from_state')!r} -> {event.get('to_state')!r}"
                )
        prev_state = event.get("to_state")


def validate_handoff(text: str) -> None:
    if not text.strip():
        raise IntakeStateError("HANDOFF_NOTE.md is empty")
    if HANDOFF_AUTHORITY_LINE not in text:
        raise IntakeStateError("HANDOFF_NOTE.md missing YAML authority warning")


def make_identity(paths: IntakePaths, *, actor: str) -> dict[str, Any]:
    body = {
        "document_id": paths.document_id,
        "document_path": paths.document_path,
        "amendment_slug": paths.amendment_slug,
        "intake_schema_version": INTAKE_SCHEMA_VERSION_CURRENT,
        "intake_path": paths.intake_dir.relative_to(paths.base_dir).as_posix(),
        "planning_path": paths.planning_dir.relative_to(paths.base_dir).as_posix(),
        "kernel_path": paths.kernel_dir.relative_to(paths.base_dir).as_posix(),
        "ratification_path": paths.ratification_dir.relative_to(paths.base_dir).as_posix(),
        "current_head_version": paths.current_head_version,
        "created_at": utc_now_iso(),
        "created_by": actor,
    }
    validate_identity(body)
    return body


def make_initial_status(paths: IntakePaths, *, actor: str) -> dict[str, Any]:
    body = {
        "document_id": paths.document_id,
        "amendment_slug": paths.amendment_slug,
        "lifecycle_state": "intake_open",
        "artifact_health": "healthy",
        "committee_status": "open",
        "architect_verification_status": "pending",
        "ui_verification_status": "pending",
        "kernel_status": "pending",
        "peer_review_status": "not_run",
        "ratification_handoff_status": "not_ready",
        "next_action": "build_evidence",
        "current_head_version": paths.current_head_version,
        "last_reviewed_version": "",
        "status_updated_at": utc_now_iso(),
        "status_updated_by": actor,
        "phase_ledger": make_initial_phase_ledger(),
    }
    validate_status(body)
    return body


def make_initial_events(paths: IntakePaths, *, actor: str) -> dict[str, Any]:
    event = {
        "event_id": "evt-001",
        "timestamp": utc_now_iso(),
        "actor": actor,
        "event_type": "intake_initialized",
        "from_state": "",
        "to_state": "intake_open",
        "summary": "Intake scaffold initialized for amendment orchestration.",
        "evidence_paths": [
            paths.document_path,
            paths.intake_dir.relative_to(paths.base_dir).as_posix(),
        ],
    }
    out = {
        "intake_schema_version": INTAKE_SCHEMA_VERSION_CURRENT,
        "document_id": paths.document_id,
        "amendment_slug": paths.amendment_slug,
        "events": [event],
    }
    validate_events(out)
    return out


def load_identity(paths: IntakePaths) -> dict[str, Any]:
    body = _load_yaml(paths.intake_identity)
    if body:
        validate_identity(body)
    return body


def load_status(paths: IntakePaths) -> dict[str, Any]:
    body = _load_yaml(paths.intake_status)
    if body:
        validate_status(body)
    return body


def load_events(paths: IntakePaths) -> dict[str, Any]:
    body = _load_yaml(paths.intake_events)
    if body:
        validate_events(body)
    return body


def load_handoff(paths: IntakePaths) -> str:
    if not paths.intake_handoff.exists():
        return ""
    text = paths.intake_handoff.read_text(encoding="utf-8")
    validate_handoff(text)
    return text


def write_identity(paths: IntakePaths, identity: dict[str, Any]) -> None:
    validate_identity(identity)
    _write_yaml(paths.intake_identity, identity)


def write_status(paths: IntakePaths, status: dict[str, Any]) -> None:
    validate_status(status)
    _write_yaml(paths.intake_status, status)


def write_events(paths: IntakePaths, events_doc: dict[str, Any]) -> None:
    validate_events(events_doc)
    _write_yaml(paths.intake_events, events_doc)


def write_handoff(paths: IntakePaths, text: str) -> None:
    validate_handoff(text)
    paths.intake_handoff.parent.mkdir(parents=True, exist_ok=True)
    paths.intake_handoff.write_text(text.strip() + "\n", encoding="utf-8")


def initialize_intake(paths: IntakePaths, *, actor: str) -> None:
    paths.intake_dir.mkdir(parents=True, exist_ok=True)
    write_identity(paths, make_identity(paths, actor=actor))
    write_status(paths, make_initial_status(paths, actor=actor))
    write_events(paths, make_initial_events(paths, actor=actor))
    write_handoff(paths, DEFAULT_HANDOFF_NOTE)


def get_phase_record(status: dict[str, Any], phase_id: str) -> dict[str, Any]:
    phase_ledger = status.get("phase_ledger")
    if not phase_ledger:
        raise IntakeStateError("INTAKE_STATUS phase_ledger is not present")
    for record in phase_ledger:
        if record.get("phase_id") == phase_id:
            return deepcopy(record)
    raise IntakeStateError(f"INTAKE_STATUS phase_ledger missing phase_id {phase_id!r}")


def patch_phase_record(
    paths: IntakePaths,
    *,
    actor: str,
    phase_id: str,
    patch: dict[str, Any],
) -> dict[str, Any]:
    status = load_status(paths)
    if not status:
        raise IntakeStateError("Cannot patch phase ledger before intake is initialized")
    phase_ledger = deepcopy(status.get("phase_ledger") or [])
    if not phase_ledger:
        raise IntakeStateError("INTAKE_STATUS phase_ledger is not present")

    updated_record: dict[str, Any] | None = None
    for index, record in enumerate(phase_ledger):
        if record.get("phase_id") == phase_id:
            candidate = deepcopy(record)
            candidate.update(patch)
            updated_record = candidate
            phase_ledger[index] = candidate
            break
    if updated_record is None:
        raise IntakeStateError(f"INTAKE_STATUS phase_ledger missing phase_id {phase_id!r}")

    updated = deepcopy(status)
    updated["phase_ledger"] = phase_ledger
    updated["status_updated_at"] = utc_now_iso()
    updated["status_updated_by"] = actor
    validate_status(updated)
    write_status(paths, updated)
    return updated_record


def append_event(
    paths: IntakePaths,
    *,
    actor: str,
    event_type: str,
    from_state: str,
    to_state: str,
    summary: str,
    evidence_paths: list[str],
    phase_id: str | None = None,
) -> dict[str, Any]:
    if event_type not in INTAKE_EVENT_TYPES:
        raise IntakeStateError(f"Invalid event_type: {event_type!r}")
    if phase_id and phase_id not in PHASE_LEDGER_ALLOWED_PHASE_IDS:
        raise IntakeStateError(f"Invalid phase_id: {phase_id!r}")

    events_doc = load_events(paths)
    if not events_doc:
        raise IntakeStateError("Cannot append event before intake is initialized")

    event = {
        "event_id": next_event_id(events_doc["events"]),
        "timestamp": utc_now_iso(),
        "actor": actor,
        "event_type": event_type,
        "from_state": from_state,
        "to_state": to_state,
        "summary": summary,
        "evidence_paths": evidence_paths,
    }
    if phase_id:
        event["phase_id"] = phase_id
    candidate = deepcopy(events_doc)
    candidate["events"].append(event)
    validate_events(candidate)
    write_events(paths, candidate)
    return event


def transition_status(
    paths: IntakePaths,
    *,
    actor: str,
    lifecycle_state: str,
    next_action: str,
    event_type: str,
    summary: str,
    evidence_paths: list[str],
    patch: dict[str, Any] | None = None,
    phase_id: str | None = None,
) -> dict[str, Any]:
    status = load_status(paths)
    if not status:
        raise IntakeStateError("Cannot transition status before intake is initialized")
    from_state = str(status["lifecycle_state"])
    allowed = ALLOWED_LIFECYCLE_TRANSITIONS.get(from_state, frozenset())
    if lifecycle_state != from_state and lifecycle_state not in allowed:
        raise IntakeStateError(f"Illegal lifecycle transition {from_state!r} -> {lifecycle_state!r}")

    updated = deepcopy(status)
    updated["lifecycle_state"] = lifecycle_state
    updated["next_action"] = next_action
    updated["status_updated_at"] = utc_now_iso()
    updated["status_updated_by"] = actor
    if patch:
        updated.update(patch)
    validate_status(updated)
    write_status(paths, updated)
    append_event(
        paths,
        actor=actor,
        event_type=event_type,
        from_state=from_state,
        to_state=lifecycle_state,
        summary=summary,
        evidence_paths=evidence_paths,
        phase_id=phase_id,
    )
    return updated


def set_committee_status(
    paths: IntakePaths,
    *,
    actor: str,
    committee_status: str,
    note: str,
    evidence_paths: list[str],
    lifecycle_state: str,
    next_action: str,
) -> dict[str, Any]:
    status = load_status(paths)
    if not status:
        raise IntakeStateError("Cannot record committee state before intake is initialized")
    previous = str(status["committee_status"])
    if committee_status not in COMMITTEE_STATUS:
        raise IntakeStateError(f"Invalid committee_status: {committee_status!r}")
    allowed = ALLOWED_COMMITTEE_TRANSITIONS.get(previous, frozenset())
    if committee_status != previous and committee_status not in allowed:
        raise IntakeStateError(f"Illegal committee_status transition {previous!r} -> {committee_status!r}")

    patch = {
        "committee_status": committee_status,
        "committee_recorded_by": actor,
        "committee_recorded_at": utc_now_iso(),
        "committee_note": note,
    }
    return transition_status(
        paths,
        actor=actor,
        lifecycle_state=lifecycle_state,
        next_action=next_action,
        event_type="committee_state_recorded",
        summary=f"Committee state recorded as {committee_status}.",
        evidence_paths=evidence_paths,
        patch=patch,
    )

