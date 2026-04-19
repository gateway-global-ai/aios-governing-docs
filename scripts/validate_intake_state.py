#!/usr/bin/env python3
"""
Validate amendment intake scaffold artifacts under reviews/<slug>/intake/.

Exit 0 = PASS
Exit non-zero = FAIL
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from intake_architect import validate_architect_output_conformance
from intake_paths import BASE_DIR
from intake_state import (
    HANDOFF_AUTHORITY_LINE,
    IntakeStateError,
    validate_events,
    validate_handoff,
    validate_identity,
    validate_status,
)


def _err(msg: str) -> None:
    print(msg, file=sys.stderr)


def _load_yaml(path: Path) -> dict:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        raise IntakeStateError(f"Unreadable YAML: {path}: {exc}") from exc


def validate_intake_dir(intake_dir: Path, base_dir: Path) -> tuple[str, list[str]]:
    msgs: list[str] = []
    overall = "PASS"

    identity_path = intake_dir / "INTAKE_IDENTITY.yaml"
    status_path = intake_dir / "INTAKE_STATUS.yaml"
    events_path = intake_dir / "INTAKE_EVENTS.yaml"
    handoff_path = intake_dir / "HANDOFF_NOTE.md"

    for required in (identity_path, status_path, events_path, handoff_path):
        if not required.exists():
            msgs.append(f"FAIL: missing required artifact: {required.name}")
            overall = "FAIL"

    if overall == "FAIL":
        return overall, msgs

    try:
        identity = _load_yaml(identity_path)
        validate_identity(identity)
    except IntakeStateError as exc:
        msgs.append(f"FAIL: {exc}")
        overall = "FAIL"
        identity = {}

    try:
        status = _load_yaml(status_path)
        validate_status(status)
    except IntakeStateError as exc:
        msgs.append(f"FAIL: {exc}")
        overall = "FAIL"
        status = {}

    try:
        events_doc = _load_yaml(events_path)
        validate_events(events_doc)
    except IntakeStateError as exc:
        msgs.append(f"FAIL: {exc}")
        overall = "FAIL"
        events_doc = {}

    try:
        handoff = handoff_path.read_text(encoding="utf-8")
        validate_handoff(handoff)
    except (IntakeStateError, OSError) as exc:
        msgs.append(f"FAIL: {exc}")
        overall = "FAIL"
        handoff = ""

    if identity and status:
        for key in ("document_id", "amendment_slug", "current_head_version"):
            identity_key = "amendment_slug" if key == "amendment_slug" else key
            status_key = key
            if str(identity.get(identity_key) or "") != str(status.get(status_key) or ""):
                msgs.append(f"FAIL: identity/status mismatch for {key}")
                overall = "FAIL"

        intake_path = identity.get("intake_path")
        if intake_path and intake_path != intake_dir.relative_to(base_dir).as_posix():
            msgs.append("FAIL: INTAKE_IDENTITY intake_path does not match actual path")
            overall = "FAIL"

        planning_required_states = {
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
        }
        kernel_required_states = {
            "kernel_review_pending",
            "kernel_review_advisory_complete",
            "ratification_handoff_pending",
            "blocked_ratification_manual",
            "ratification_handoff_ready",
            "closed_executed",
        }
        ratification_required_states = {
            "blocked_ratification_manual",
            "ratification_handoff_ready",
            "closed_executed",
        }

        if status.get("lifecycle_state") in planning_required_states:
            rel = identity.get("planning_path")
            if rel and not (base_dir / rel).exists():
                msgs.append(f"FAIL: INTAKE_IDENTITY planning_path missing on disk for current lifecycle: {rel}")
                overall = "FAIL"

        if status.get("lifecycle_state") in kernel_required_states or status.get("kernel_status") in {
            "advisory_complete",
            "skipped_with_reason",
        }:
            rel = identity.get("kernel_path")
            if rel and not (base_dir / rel).exists():
                msgs.append(f"FAIL: INTAKE_IDENTITY kernel_path missing on disk for current lifecycle: {rel}")
                overall = "FAIL"

        if status.get("lifecycle_state") in ratification_required_states or status.get("ratification_handoff_status") in {
            "ready",
            "executed",
        }:
            rel = identity.get("ratification_path")
            if rel and not (base_dir / rel).exists():
                msgs.append(f"FAIL: INTAKE_IDENTITY ratification_path missing on disk for current lifecycle: {rel}")
                overall = "FAIL"

    if identity and events_doc:
        for key in ("document_id", "amendment_slug"):
            events_key = "amendment_slug" if key == "amendment_slug" else key
            if str(identity.get(key) or "") != str(events_doc.get(events_key) or ""):
                msgs.append(f"FAIL: identity/events mismatch for {key}")
                overall = "FAIL"

    if handoff and HANDOFF_AUTHORITY_LINE not in handoff:
        msgs.append("FAIL: HANDOFF_NOTE.md missing YAML authority line")
        overall = "FAIL"

    if identity and status and events_doc:
        events = events_doc.get("events") or []
        if events:
            last_state = events[-1].get("to_state")
            if last_state != status.get("lifecycle_state"):
                msgs.append("FAIL: latest INTAKE_EVENTS to_state does not match INTAKE_STATUS lifecycle_state")
                overall = "FAIL"

        if status.get("architect_verification_status") == "verified" and not any(
            ev.get("event_type") == "architect_verified" for ev in events
        ):
            msgs.append("FAIL: architect verification claimed without architect_verified event")
            overall = "FAIL"

        architect_completion_states = {
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
        }
        if status.get("lifecycle_state") in architect_completion_states:
            rel = str((Path(identity.get("planning_path") or "") / "ARCHITECT_PLAN.md").as_posix()).lstrip("/")
            if rel and not (base_dir / rel).is_file():
                msgs.append(f"FAIL: architect output missing on disk for lifecycle_state {status.get('lifecycle_state')}: {rel}")
                overall = "FAIL"
            for event_type in (
                "architect_started",
                "architect_drafted",
                "architect_output_verified",
                "architect_output_conformance_validated",
                "architect_human_verification_blocked",
            ):
                if not any(ev.get("event_type") == event_type for ev in events):
                    msgs.append(f"FAIL: architect lane state claimed without {event_type} event")
                    overall = "FAIL"
            template_rel = str((Path(identity.get("planning_path") or "") / "ARCHITECT_PLAN_TEMPLATE.md").as_posix()).lstrip("/")
            if template_rel and not (base_dir / template_rel).is_file():
                msgs.append(f"FAIL: architect template missing on disk for conformance validation: {template_rel}")
                overall = "FAIL"
            elif rel:
                result = validate_architect_output_conformance(base_dir / rel, base_dir / template_rel)
                if not result.ok:
                    msgs.append(
                        "FAIL: architect output failed structural conformance validation: " + "; ".join(result.reasons)
                    )
                    overall = "FAIL"

        if status.get("ui_verification_status") == "verified" and not any(
            ev.get("event_type") == "ui_verified" for ev in events
        ):
            msgs.append("FAIL: UI verification claimed without ui_verified event")
            overall = "FAIL"

        if status.get("committee_status") != "open":
            committee_events = [ev for ev in events if ev.get("event_type") == "committee_state_recorded"]
            if not committee_events:
                msgs.append("FAIL: committee status claimed without committee_state_recorded event")
                overall = "FAIL"
            elif not any(ev.get("evidence_paths") for ev in committee_events):
                msgs.append("FAIL: committee state recorded without evidence_paths")
                overall = "FAIL"

        if status.get("kernel_status") == "skipped_with_reason" and not any(
            ev.get("event_type") == "kernel_skipped" for ev in events
        ):
            msgs.append("FAIL: kernel skipped claimed without kernel_skipped event")
            overall = "FAIL"

        if status.get("kernel_status") == "advisory_complete" and not any(
            ev.get("event_type") == "kernel_findings_recorded" for ev in events
        ):
            msgs.append("FAIL: kernel advisory completion claimed without kernel_findings_recorded event")
            overall = "FAIL"

        if status.get("ratification_handoff_status") in {"ready", "executed"} and not any(
            ev.get("event_type") == "ratification_handoff_prepared" for ev in events
        ):
            msgs.append("FAIL: ratification handoff claimed without ratification_handoff_prepared event")
            overall = "FAIL"

    return overall, msgs


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate amendment intake scaffold state")
    parser.add_argument(
        "--intake-dir",
        required=True,
        help="Path to reviews/<slug>/intake",
    )
    args = parser.parse_args()

    intake_dir = Path(args.intake_dir).resolve()
    if not intake_dir.is_dir():
        _err(f"Not a directory: {intake_dir}")
        return 1

    overall, msgs = validate_intake_dir(intake_dir, BASE_DIR)
    for msg in msgs:
        _err(msg)
    _err(f"Result: {overall}")
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

