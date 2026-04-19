#!/usr/bin/env python3
"""
Phase functions for the amendment intake scaffold.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from intake_architect import (
    validate_architect_output_conformance,
    validate_bundle_manifest_correspondence,
    validate_snapshot_freshness,
    validate_ui_output_conformance,
)
from intake_paths import (
    DEFAULT_PRODUCT_CONTEXT_SNAPSHOT,
    IntakePaths,
    default_lane_build_manifest_path,
    default_lane_bundle_dir,
    default_lane_bundle_path,
    default_lane_manifest_path,
    manifest_declares_path,
    resolve_architect_lane_contract,
)
from intake_ratification import prepare_ratification_artifacts
from intake_runtime import IntakeRuntimeError, ensure_exists, env_has_peer_review_credentials, python_command, run_command
from intake_state import (
    IntakeStateError,
    append_event,
    initialize_intake,
    load_status,
    set_committee_status,
    transition_status,
)
from intake_templates import ensure_committee_packet, ensure_kernel_files, ensure_planning_templates


@dataclass
class PhaseResult:
    phase: str
    dry_run: bool
    changed_paths: list[str]
    message: str
    status: dict[str, Any] | None = None


def _status(paths: IntakePaths) -> dict[str, Any]:
    status = load_status(paths)
    if not status:
        raise IntakeStateError("Intake is not initialized. Run --init first.")
    return status


def _expect_state(paths: IntakePaths, allowed: set[str] | frozenset[str]) -> dict[str, Any]:
    status = _status(paths)
    if status["lifecycle_state"] not in allowed:
        raise IntakeStateError(
            f"Phase blocked: current lifecycle_state {status['lifecycle_state']!r} not in {sorted(allowed)}"
        )
    return status


def _packet_round_dir(paths: IntakePaths, round_number: int) -> Path:
    return paths.round_1_dir if round_number == 1 else paths.round_2_dir


def _packet_review_status(paths: IntakePaths, round_number: int) -> str:
    packet_status = _packet_round_dir(paths, round_number) / "PACKET_STATUS.yaml"
    if not packet_status.exists():
        return "incomplete"
    data = yaml.safe_load(packet_status.read_text(encoding="utf-8")) or {}
    gate = str(data.get("review_gate_status") or "incomplete")
    if gate == "pass":
        return "pass"
    if gate == "fail":
        return "fail"
    return "incomplete"


def _architect_plan_paths(paths: IntakePaths) -> list[str]:
    return [
        paths.planning_dir.joinpath("ARCHITECT_PLAN_TEMPLATE.md").relative_to(paths.base_dir).as_posix(),
        paths.planning_dir.joinpath("UI_PLAN_TEMPLATE.md").relative_to(paths.base_dir).as_posix(),
        paths.planning_dir.joinpath("ARCHITECT_PLAN.md").relative_to(paths.base_dir).as_posix(),
    ]


def _ui_plan_paths(paths: IntakePaths) -> list[str]:
    return [
        paths.planning_dir.joinpath("UI_PLAN_TEMPLATE.md").relative_to(paths.base_dir).as_posix(),
        paths.planning_dir.joinpath("ARCHITECT_PLAN.md").relative_to(paths.base_dir).as_posix(),
        paths.planning_dir.joinpath("UI_PLAN.md").relative_to(paths.base_dir).as_posix(),
    ]


def _record_planning_override_event(
    paths: IntakePaths,
    *,
    actor: str,
    lifecycle_state: str,
    lane_name: str,
    bundle_override: str | None,
    manifest_override: str | None,
) -> None:
    if not bundle_override and not manifest_override:
        return
    evidence_paths: list[str] = []
    if manifest_override:
        evidence_paths.append(manifest_override.replace("\\", "/"))
    if bundle_override:
        evidence_paths.append(bundle_override.replace("\\", "/"))
    append_event(
        paths,
        actor=actor,
        event_type=f"{lane_name}_input_override_recorded",
        from_state=lifecycle_state,
        to_state=lifecycle_state,
        summary=f"{lane_name.capitalize()} lane invoked with non-default manifest and/or bundle input path.",
        evidence_paths=evidence_paths,
    )


def _record_planning_run_identity(
    paths: IntakePaths,
    *,
    actor: str,
    lane_name: str,
    lifecycle_state: str,
    evidence_paths: list[str],
) -> None:
    append_event(
        paths,
        actor=actor,
        event_type=f"{lane_name}_run_identity_recorded",
        from_state=lifecycle_state,
        to_state=lifecycle_state,
        summary=(
            f"{lane_name.capitalize()} lane recorded the manifest, bundle, build manifest, "
            "and run-record paths selected for this drafting run."
        ),
        evidence_paths=evidence_paths,
    )


def _block_planning_lane(
    paths: IntakePaths,
    *,
    actor: str,
    lane_name: str,
    summary: str,
    evidence_paths: list[str],
    dry_run: bool,
    artifact_health: str,
    event_type: str,
    next_action: str,
) -> None:
    if dry_run:
        raise IntakeRuntimeError(summary)
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="failed",
        next_action=next_action,
        event_type=event_type,
        summary=summary,
        evidence_paths=evidence_paths,
        patch={"artifact_health": artifact_health},
    )
    raise IntakeRuntimeError(
        f"{lane_name.capitalize()} lane failure recorded: {summary} Current status: {status['lifecycle_state']}"
    )


def init_intake(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    changed = [
        paths.intake_identity.relative_to(paths.base_dir).as_posix(),
        paths.intake_status.relative_to(paths.base_dir).as_posix(),
        paths.intake_events.relative_to(paths.base_dir).as_posix(),
        paths.intake_handoff.relative_to(paths.base_dir).as_posix(),
    ]
    if dry_run:
        return PhaseResult("init", True, changed, "Would initialize intake artifacts.")
    initialize_intake(paths, actor=actor)
    return PhaseResult("init", False, changed, "Initialized intake artifacts.", status=load_status(paths))


def refresh_evidence(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"intake_open", "blocked_missing_inputs", "phase_a_evidence_pending", "phase_a_evidence_ready", "failed"})
    lane_manifest = default_lane_manifest_path(paths)
    lane_bundle_dir = default_lane_bundle_dir(paths)
    manifest_rel = lane_manifest.relative_to(paths.base_dir).as_posix()
    required_snapshot_rel = DEFAULT_PRODUCT_CONTEXT_SNAPSHOT.relative_to(paths.base_dir).as_posix()
    needs_product_snapshot = lane_manifest.is_file() and manifest_declares_path(lane_manifest, required_snapshot_rel)
    changed = [
        manifest_rel,
        default_lane_bundle_path(paths).relative_to(paths.base_dir).as_posix(),
        default_lane_build_manifest_path(paths).relative_to(paths.base_dir).as_posix(),
    ]
    if needs_product_snapshot:
        changed.insert(1, required_snapshot_rel)
    if not lane_manifest.is_file():
        raise IntakeRuntimeError(
            "Evidence refresh blocked: required lane knowledge packet missing: "
            f"{manifest_rel}"
        )
    if dry_run:
        return PhaseResult(
            "refresh_evidence",
            True,
            changed,
            f"Would rebuild the declared knowledge bundle from {manifest_rel}.",
        )

    if needs_product_snapshot:
        run_command(python_command("scripts/generate_product_context_bundle.py"))
    run_command(
        python_command(
            "scripts/build_agent_kb.py",
            "--manifest",
            manifest_rel,
            "--output-dir",
            lane_bundle_dir.relative_to(paths.base_dir).as_posix(),
        )
    )
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_a_evidence_ready",
        next_action="run_architect",
        event_type="evidence_refreshed",
        summary=f"Evidence refreshed and knowledge bundle rebuilt from declared lane packet {manifest_rel}.",
        evidence_paths=changed,
        patch={"artifact_health": "healthy"},
    )
    return PhaseResult("refresh_evidence", False, changed, "Evidence refreshed.", status=status)


def run_architect(
    paths: IntakePaths,
    *,
    actor: str,
    dry_run: bool,
    bundle_override: str | None = None,
    manifest_override: str | None = None,
) -> PhaseResult:
    status = _expect_state(paths, {"phase_a_evidence_ready", "phase_b_architect_pending", "failed"})
    try:
        contract = resolve_architect_lane_contract(
            paths,
            invoked_slug=paths.amendment_slug,
            bundle_override=bundle_override,
            manifest_override=manifest_override,
        )
    except ValueError as exc:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary=f"Architect lane blocked: {exc}",
            evidence_paths=[paths.planning_dir.relative_to(paths.base_dir).as_posix()],
            dry_run=dry_run,
            artifact_health="identity_mismatch",
            event_type="architect_precondition_blocked",
            next_action="run_architect",
        )
    changed = _architect_plan_paths(paths)
    required_snapshot_rel = contract.repo_rel(contract.product_snapshot_path)
    manifest_rel = contract.repo_rel(contract.manifest_path)
    bundle_rel = contract.repo_rel(contract.bundle_path)
    build_manifest_rel = contract.repo_rel(contract.build_manifest_path)
    output_rel = contract.repo_rel(contract.architect_output_path)

    if not contract.manifest_path.is_file():
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary=f"Architect lane blocked: required manifest missing: {manifest_rel}",
            evidence_paths=[manifest_rel],
            dry_run=dry_run,
            artifact_health="stale_supporting_artifacts",
            event_type="architect_precondition_blocked",
            next_action="run_architect",
        )
    if not contract.bundle_path.is_file():
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary=f"Architect lane blocked: required KB bundle missing: {bundle_rel}",
            evidence_paths=[bundle_rel],
            dry_run=dry_run,
            artifact_health="stale_supporting_artifacts",
            event_type="architect_precondition_blocked",
            next_action="run_architect",
        )
    if not contract.build_manifest_path.is_file():
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary=f"Architect lane blocked: required build manifest missing: {build_manifest_rel}",
            evidence_paths=[build_manifest_rel],
            dry_run=dry_run,
            artifact_health="stale_supporting_artifacts",
            event_type="architect_precondition_blocked",
            next_action="run_architect",
        )
    try:
        correspondence = validate_bundle_manifest_correspondence(
            contract.manifest_path,
            contract.bundle_path,
            contract.build_manifest_path,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary=f"Architect lane blocked: unable to validate manifest/bundle correspondence: {exc}",
            evidence_paths=[manifest_rel, bundle_rel, build_manifest_rel],
            dry_run=dry_run,
            artifact_health="identity_mismatch",
            event_type="architect_bundle_manifest_mismatch_blocked",
            next_action="run_architect",
        )
    if not correspondence.ok:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary="Architect lane blocked: selected manifest does not correspond to selected KB bundle/build manifest pair: "
            + "; ".join(correspondence.reasons),
            evidence_paths=[manifest_rel, bundle_rel, build_manifest_rel],
            dry_run=dry_run,
            artifact_health="identity_mismatch",
            event_type="architect_bundle_manifest_mismatch_blocked",
            next_action="run_architect",
        )
    if manifest_declares_path(contract.manifest_path, required_snapshot_rel) and not contract.product_snapshot_path.is_file():
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary=f"Architect lane blocked: required product snapshot missing: {required_snapshot_rel}",
            evidence_paths=[manifest_rel, required_snapshot_rel],
            dry_run=dry_run,
            artifact_health="stale_supporting_artifacts",
            event_type="architect_precondition_blocked",
            next_action="build_evidence",
        )
    if manifest_declares_path(contract.manifest_path, required_snapshot_rel):
        freshness = validate_snapshot_freshness(contract.product_snapshot_path, contract.build_manifest_path)
        if not freshness.ok:
            _block_planning_lane(
                paths,
                actor=actor,
                lane_name="architect",
                summary="Architect lane blocked: required product snapshot freshness could not be proven: "
                + "; ".join(freshness.reasons),
                evidence_paths=[manifest_rel, build_manifest_rel, required_snapshot_rel],
                dry_run=dry_run,
                artifact_health="stale_supporting_artifacts",
                event_type="architect_evidence_freshness_blocked",
                next_action="build_evidence",
            )

    if dry_run:
        return PhaseResult("run_architect", True, changed, "Would run Ollama architect planning step.")

    created = ensure_planning_templates(paths)
    _record_planning_override_event(
        paths,
        actor=actor,
        lifecycle_state=str(status["lifecycle_state"]),
        lane_name="architect",
        bundle_override=bundle_override,
        manifest_override=manifest_override,
    )
    transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_b_architect_pending",
        next_action="run_architect",
        event_type="architect_started",
        summary="Architect planning started after precondition and path reconciliation checks.",
        evidence_paths=(created or []) + [manifest_rel, bundle_rel, build_manifest_rel],
    )
    try:
        run_command(python_command("scripts/preflight_local_agents.py"))
        architect_command = [
            *python_command(
                "scripts/ollama_planning_agent.py",
                "--role",
                "architect",
                "--amd-slug",
                paths.amendment_slug,
                "--manifest",
                manifest_rel,
            )
        ]
        architect_command.extend(["--bundle", bundle_rel])
        run_command(architect_command)
        ensure_exists(contract.architect_output_path, kind="architect output")
        ensure_exists(contract.architect_output_path.with_suffix(".md.run_record.json"), kind="architect run record")
    except (IntakeRuntimeError, FileNotFoundError) as exc:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary=f"Architect lane failed before verified output was recorded: {exc}",
            evidence_paths=[
                manifest_rel,
                bundle_rel,
                build_manifest_rel,
                output_rel,
                contract.repo_rel(contract.architect_output_path.with_suffix(".md.run_record.json")),
            ],
            dry_run=False,
            artifact_health="incomplete_packet",
            event_type="architect_failed",
            next_action="run_architect",
        )
    try:
        conformance = validate_architect_output_conformance(
            contract.architect_output_path,
            paths.planning_dir / "ARCHITECT_PLAN_TEMPLATE.md",
        )
    except OSError as exc:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary=f"Architect lane blocked: output conformance validation could not be executed: {exc}",
            evidence_paths=[output_rel],
            dry_run=False,
            artifact_health="incomplete_packet",
            event_type="architect_output_validation_failed",
            next_action="run_architect",
        )
    if not conformance.ok:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="architect",
            summary="Architect lane blocked: output failed architect-plan conformance validation: "
            + "; ".join(conformance.reasons),
            evidence_paths=[output_rel],
            dry_run=False,
            artifact_health="incomplete_packet",
            event_type="architect_output_validation_failed",
            next_action="run_architect",
        )

    transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_b_architect_drafted",
        next_action="verify_architect",
        event_type="architect_drafted",
        summary="Architect planning draft generated.",
        evidence_paths=[output_rel],
        patch={"artifact_health": "healthy"},
    )
    append_event(
        paths,
        actor=actor,
        event_type="architect_output_verified",
        from_state="phase_b_architect_drafted",
        to_state="phase_b_architect_drafted",
        summary="Architect output file existence verified before success recording.",
        evidence_paths=[output_rel],
    )
    append_event(
        paths,
        actor=actor,
        event_type="architect_output_conformance_validated",
        from_state="phase_b_architect_drafted",
        to_state="phase_b_architect_drafted",
        summary="Architect output passed template-based structural conformance validation.",
        evidence_paths=[
            output_rel,
            paths.planning_dir.joinpath("ARCHITECT_PLAN_TEMPLATE.md").relative_to(paths.base_dir).as_posix(),
        ],
    )
    _record_planning_run_identity(
        paths,
        actor=actor,
        lane_name="architect",
        lifecycle_state="phase_b_architect_drafted",
        evidence_paths=[
            manifest_rel,
            bundle_rel,
            build_manifest_rel,
            contract.repo_rel(contract.architect_output_path.with_suffix(".md.run_record.json")),
        ],
    )
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="blocked_architect_human_verification",
        next_action="verify_architect",
        event_type="architect_human_verification_blocked",
        summary="Architect draft now awaits human verification.",
        evidence_paths=[output_rel],
    )
    return PhaseResult("run_architect", False, created + [output_rel], "Architect draft generated.", status=status)


def verify_architect(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"blocked_architect_human_verification"})
    changed = [paths.intake_status.relative_to(paths.base_dir).as_posix()]
    if dry_run:
        return PhaseResult("verify_architect", True, changed, "Would record architect verification.")
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_c_ui_pending",
        next_action="run_ui",
        event_type="architect_verified",
        summary="Architect draft verified by human reviewer.",
        evidence_paths=[
            paths.planning_dir.joinpath("ARCHITECT_PLAN.md").relative_to(paths.base_dir).as_posix(),
            paths.intake_status.relative_to(paths.base_dir).as_posix(),
        ],
        patch={
            "architect_verification_status": "verified",
            "architect_verified_by": actor,
            "architect_verified_at": status_time(),
        },
    )
    return PhaseResult("verify_architect", False, changed, "Architect verification recorded.", status=status)


def verify_ui(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"blocked_ui_human_verification"})
    changed = [paths.intake_status.relative_to(paths.base_dir).as_posix()]
    if dry_run:
        return PhaseResult("verify_ui", True, changed, "Would record UI verification.")
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_d_committee_pending",
        next_action="prepare_committee",
        event_type="ui_verified",
        summary="UI draft verified by human reviewer.",
        evidence_paths=[
            paths.planning_dir.joinpath("UI_PLAN.md").relative_to(paths.base_dir).as_posix(),
            paths.intake_status.relative_to(paths.base_dir).as_posix(),
        ],
        patch={
            "ui_verification_status": "verified",
            "ui_verified_by": actor,
            "ui_verified_at": status_time(),
        },
    )
    return PhaseResult("verify_ui", False, changed, "UI verification recorded.", status=status)


def run_ui(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    status = _expect_state(paths, {"phase_c_ui_pending", "failed"})
    if status.get("architect_verification_status") != "verified":
        raise IntakeStateError("UI phase blocked until architect verification is recorded.")
    try:
        contract = resolve_architect_lane_contract(paths, invoked_slug=paths.amendment_slug)
    except ValueError as exc:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary=f"UI lane blocked: {exc}",
            evidence_paths=[paths.planning_dir.relative_to(paths.base_dir).as_posix()],
            dry_run=dry_run,
            artifact_health="identity_mismatch",
            event_type="ui_precondition_blocked",
            next_action="run_ui",
        )
    created = ensure_planning_templates(paths)
    out = paths.planning_dir / "UI_PLAN.md"
    manifest_rel = contract.repo_rel(contract.manifest_path)
    bundle_rel = contract.repo_rel(contract.bundle_path)
    build_manifest_rel = contract.repo_rel(contract.build_manifest_path)
    output_rel = out.relative_to(paths.base_dir).as_posix()
    required_snapshot_rel = contract.repo_rel(contract.product_snapshot_path)
    changed = created + [output_rel]
    if not contract.manifest_path.is_file():
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary=f"UI lane blocked: required manifest missing: {manifest_rel}",
            evidence_paths=[manifest_rel],
            dry_run=dry_run,
            artifact_health="stale_supporting_artifacts",
            event_type="ui_precondition_blocked",
            next_action="run_ui",
        )
    if not contract.bundle_path.is_file():
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary=f"UI lane blocked: required KB bundle missing: {bundle_rel}",
            evidence_paths=[bundle_rel],
            dry_run=dry_run,
            artifact_health="stale_supporting_artifacts",
            event_type="ui_precondition_blocked",
            next_action="run_ui",
        )
    if not contract.build_manifest_path.is_file():
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary=f"UI lane blocked: required build manifest missing: {build_manifest_rel}",
            evidence_paths=[build_manifest_rel],
            dry_run=dry_run,
            artifact_health="stale_supporting_artifacts",
            event_type="ui_precondition_blocked",
            next_action="run_ui",
        )
    try:
        correspondence = validate_bundle_manifest_correspondence(
            contract.manifest_path,
            contract.bundle_path,
            contract.build_manifest_path,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary=f"UI lane blocked: unable to validate manifest/bundle correspondence: {exc}",
            evidence_paths=[manifest_rel, bundle_rel, build_manifest_rel],
            dry_run=dry_run,
            artifact_health="identity_mismatch",
            event_type="ui_bundle_manifest_mismatch_blocked",
            next_action="run_ui",
        )
    if not correspondence.ok:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary="UI lane blocked: selected manifest does not correspond to selected KB bundle/build manifest pair: "
            + "; ".join(correspondence.reasons),
            evidence_paths=[manifest_rel, bundle_rel, build_manifest_rel],
            dry_run=dry_run,
            artifact_health="identity_mismatch",
            event_type="ui_bundle_manifest_mismatch_blocked",
            next_action="run_ui",
        )
    if manifest_declares_path(contract.manifest_path, required_snapshot_rel) and not contract.product_snapshot_path.is_file():
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary=f"UI lane blocked: required product snapshot missing: {required_snapshot_rel}",
            evidence_paths=[manifest_rel, required_snapshot_rel],
            dry_run=dry_run,
            artifact_health="stale_supporting_artifacts",
            event_type="ui_precondition_blocked",
            next_action="build_evidence",
        )
    if manifest_declares_path(contract.manifest_path, required_snapshot_rel):
        freshness = validate_snapshot_freshness(contract.product_snapshot_path, contract.build_manifest_path)
        if not freshness.ok:
            _block_planning_lane(
                paths,
                actor=actor,
                lane_name="ui",
                summary="UI lane blocked: required product snapshot freshness could not be proven: "
                + "; ".join(freshness.reasons),
                evidence_paths=[manifest_rel, build_manifest_rel, required_snapshot_rel],
                dry_run=dry_run,
                artifact_health="stale_supporting_artifacts",
                event_type="ui_evidence_freshness_blocked",
                next_action="build_evidence",
            )
    if dry_run:
        return PhaseResult("run_ui", True, changed, "Would run Ollama UI planning step.")

    transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_c_ui_pending",
        next_action="run_ui",
        event_type="ui_started",
        summary="UI planning started after precondition and path reconciliation checks.",
        evidence_paths=(created or []) + [manifest_rel, bundle_rel, build_manifest_rel],
    )
    try:
        run_command(python_command("scripts/preflight_local_agents.py"))
        run_command(
            python_command(
                "scripts/ollama_planning_agent.py",
                "--role",
                "ui",
                "--amd-slug",
                paths.amendment_slug,
                "--manifest",
                manifest_rel,
                "--bundle",
                bundle_rel,
            )
        )
        ensure_exists(out, kind="ui output")
        ensure_exists(out.with_suffix(".md.run_record.json"), kind="ui run record")
    except (IntakeRuntimeError, FileNotFoundError) as exc:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary=f"UI lane failed before verified output was recorded: {exc}",
            evidence_paths=[
                manifest_rel,
                bundle_rel,
                build_manifest_rel,
                output_rel,
                contract.repo_rel(out.with_suffix(".md.run_record.json")),
            ],
            dry_run=False,
            artifact_health="incomplete_packet",
            event_type="ui_failed",
            next_action="run_ui",
        )
    try:
        conformance = validate_ui_output_conformance(out, paths.planning_dir / "UI_PLAN_TEMPLATE.md")
    except OSError as exc:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary=f"UI lane blocked: output conformance validation could not be executed: {exc}",
            evidence_paths=[output_rel],
            dry_run=False,
            artifact_health="incomplete_packet",
            event_type="ui_output_validation_failed",
            next_action="run_ui",
        )
    if not conformance.ok:
        _block_planning_lane(
            paths,
            actor=actor,
            lane_name="ui",
            summary="UI lane blocked: output failed ui-plan conformance validation: " + "; ".join(conformance.reasons),
            evidence_paths=[output_rel],
            dry_run=False,
            artifact_health="incomplete_packet",
            event_type="ui_output_validation_failed",
            next_action="run_ui",
        )
    transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_c_ui_drafted",
        next_action="verify_ui",
        event_type="ui_drafted",
        summary="UI planning draft generated.",
        evidence_paths=[output_rel],
        patch={"artifact_health": "healthy"},
    )
    append_event(
        paths,
        actor=actor,
        event_type="ui_output_verified",
        from_state="phase_c_ui_drafted",
        to_state="phase_c_ui_drafted",
        summary="UI output file existence verified before success recording.",
        evidence_paths=[output_rel],
    )
    append_event(
        paths,
        actor=actor,
        event_type="ui_output_conformance_validated",
        from_state="phase_c_ui_drafted",
        to_state="phase_c_ui_drafted",
        summary="UI output passed template-based structural conformance validation.",
        evidence_paths=[
            output_rel,
            paths.planning_dir.joinpath("UI_PLAN_TEMPLATE.md").relative_to(paths.base_dir).as_posix(),
        ],
    )
    _record_planning_run_identity(
        paths,
        actor=actor,
        lane_name="ui",
        lifecycle_state="phase_c_ui_drafted",
        evidence_paths=[
            manifest_rel,
            bundle_rel,
            build_manifest_rel,
            contract.repo_rel(out.with_suffix(".md.run_record.json")),
        ],
    )
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="blocked_ui_human_verification",
        next_action="verify_ui",
        event_type="ui_human_verification_blocked",
        summary="UI draft now awaits human verification.",
        evidence_paths=[output_rel],
    )
    return PhaseResult("run_ui", False, changed, "UI draft generated.", status=status)


def prepare_committee(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"phase_d_committee_pending"})
    changed = [
        paths.planning_dir.joinpath("COMMITTEE_PACKET.md").relative_to(paths.base_dir).as_posix(),
    ]
    if dry_run:
        return PhaseResult("prepare_committee", True, changed, "Would scaffold committee packet.")
    created = ensure_committee_packet(paths)
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="blocked_committee_manual",
        next_action="record_committee",
        event_type="committee_packet_prepared",
        summary="Committee packet prepared; manual committee action required.",
        evidence_paths=created or changed,
    )
    return PhaseResult("prepare_committee", False, created or changed, "Committee packet prepared.", status=status)


def record_committee_state(
    paths: IntakePaths,
    *,
    actor: str,
    committee_status: str,
    note: str,
    dry_run: bool,
) -> PhaseResult:
    _expect_state(paths, {"blocked_committee_manual", "phase_d_committee_approved", "phase_e_author_revision_pending"})
    changed = [paths.intake_status.relative_to(paths.base_dir).as_posix()]
    if dry_run:
        return PhaseResult("record_committee_state", True, changed, f"Would record committee state {committee_status}.")

    evidence = [paths.planning_dir.joinpath("COMMITTEE_PACKET.md").relative_to(paths.base_dir).as_posix()]
    if committee_status in {"approved", "approved_with_changes"}:
        lifecycle_state = "phase_d_committee_approved"
        next_action = "author_revision"
    elif committee_status == "closed_superseded_by_review":
        lifecycle_state = "phase_e_author_revision_pending"
        next_action = "author_revision"
    else:
        lifecycle_state = "blocked_committee_manual"
        next_action = "record_committee"

    status = set_committee_status(
        paths,
        actor=actor,
        committee_status=committee_status,
        note=note,
        evidence_paths=evidence,
        lifecycle_state=lifecycle_state,
        next_action=next_action,
    )
    return PhaseResult("record_committee_state", False, changed, "Committee state recorded.", status=status)


def flag_author_revision(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"phase_d_committee_approved", "phase_e_author_revision_pending"})
    changed = [paths.intake_status.relative_to(paths.base_dir).as_posix()]
    if dry_run:
        return PhaseResult("flag_author_revision", True, changed, "Would mark author revision as a manual gate.")
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="blocked_author_revision_manual",
        next_action="author_revision",
        event_type="author_revision_flagged",
        summary="Author revision is required and remains manual.",
        evidence_paths=[paths.document_path],
    )
    return PhaseResult("flag_author_revision", False, changed, "Author revision gate recorded.", status=status)


def mark_author_revision_complete(paths: IntakePaths, *, actor: str, dry_run: bool, round_number: int) -> PhaseResult:
    _expect_state(paths, {"blocked_author_revision_manual", "phase_e_author_revision_pending"})
    changed = [paths.intake_status.relative_to(paths.base_dir).as_posix()]
    if round_number not in (1, 2):
        raise IntakeStateError("Author revision completion requires round_number 1 or 2.")
    if dry_run:
        return PhaseResult(
            "mark_author_revision_complete",
            True,
            changed,
            f"Would record author revision completion and unblock peer review Round {round_number}.",
        )
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_f_peer_review_pending",
        next_action=f"run_peer_review_round_{round_number}",
        event_type="author_revision_flagged",
        summary=f"Author revision completion recorded; peer review Round {round_number} is now pending.",
        evidence_paths=[paths.document_path],
    )
    return PhaseResult("mark_author_revision_complete", False, changed, "Author revision completion recorded.", status=status)


def run_peer_review(paths: IntakePaths, *, actor: str, round_number: int, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"phase_f_peer_review_pending", "blocked_peer_review_credentials"})
    if round_number not in (1, 2):
        raise IntakeStateError("Peer review round must be 1 or 2.")

    review_args = [
        "scripts/peer_review.py",
        paths.document_path,
        "--round",
        str(round_number),
        "--smart-context",
    ]
    product_snapshot = paths.base_dir / "reference" / "knowledge_base" / "snapshots" / "product_context_bundle.md"
    if product_snapshot.exists():
        review_args.append("--product-context")

    changed = [_packet_round_dir(paths, round_number).relative_to(paths.base_dir).as_posix()]
    if dry_run:
        return PhaseResult("run_peer_review", True, changed, f"Would run binding peer review Round {round_number}.")

    if not env_has_peer_review_credentials():
        status = transition_status(
            paths,
            actor=actor,
            lifecycle_state="blocked_peer_review_credentials",
            next_action=f"run_peer_review_round_{round_number}",
            event_type="intake_status_corrected",
            summary="Peer review blocked: required credentials are missing.",
            evidence_paths=[".env", ".env.local"],
            patch={"peer_review_status": "not_run"},
        )
        raise IntakeRuntimeError(f"Peer review credentials missing. Current status: {status['lifecycle_state']}")

    transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_f_peer_review_running",
        next_action="validate_packet",
        event_type="peer_review_started",
        summary=f"Peer review Round {round_number} started.",
        evidence_paths=[paths.document_path],
        patch={"peer_review_status": "running"},
    )
    run_command(python_command(*review_args))
    peer_status = _packet_review_status(paths, round_number)
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="phase_f_peer_review_complete",
        next_action="validate_packet",
        event_type="peer_review_completed",
        summary=f"Peer review Round {round_number} completed.",
        evidence_paths=changed,
        patch={
            "peer_review_status": peer_status,
            "last_reviewed_version": paths.current_head_version,
        },
    )
    return PhaseResult("run_peer_review", False, changed, "Peer review completed.", status=status)


def validate_peer_review_packet(paths: IntakePaths, *, actor: str, round_number: int, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"phase_f_peer_review_complete", "blocked_packet_invalid"})
    round_dir = _packet_round_dir(paths, round_number)
    changed = [round_dir.relative_to(paths.base_dir).as_posix()]
    if dry_run:
        return PhaseResult("validate_peer_review_packet", True, changed, f"Would validate review packet for round {round_number}.")

    try:
        run_command(
            python_command(
                "scripts/validate_review_packet.py",
                "--round-dir",
                round_dir.relative_to(paths.base_dir).as_posix(),
            )
        )
    except IntakeRuntimeError:
        status = transition_status(
            paths,
            actor=actor,
            lifecycle_state="blocked_packet_invalid",
            next_action="validate_packet",
            event_type="peer_review_packet_invalid",
            summary=f"Peer review packet validation failed for round {round_number}.",
            evidence_paths=changed,
            patch={"artifact_health": "incomplete_packet"},
        )
        raise IntakeRuntimeError(f"Peer review packet invalid. Current status: {status['lifecycle_state']}")

    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="kernel_review_pending",
        next_action="prepare_kernel_review",
        event_type="peer_review_packet_validated",
        summary=f"Peer review packet validated for round {round_number}.",
        evidence_paths=changed,
        patch={"artifact_health": "healthy"},
    )
    return PhaseResult("validate_peer_review_packet", False, changed, "Peer review packet validated.", status=status)


def prepare_kernel_review(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"kernel_review_pending"})
    changed = [
        paths.kernel_dir.joinpath("KERNEL_SHADOW_BRIEF.md").relative_to(paths.base_dir).as_posix(),
        paths.kernel_dir.joinpath("KERNEL_SHADOW_FINDINGS.md").relative_to(paths.base_dir).as_posix(),
    ]
    if dry_run:
        return PhaseResult("prepare_kernel_review", True, changed, "Would scaffold advisory kernel review artifacts.")
    created = ensure_kernel_files(paths)
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="kernel_review_pending",
        next_action="record_kernel_review",
        event_type="kernel_brief_prepared",
        summary="Kernel review scaffolds prepared.",
        evidence_paths=created or changed,
        patch={"kernel_status": "pending"},
    )
    return PhaseResult("prepare_kernel_review", False, created or changed, "Kernel scaffolds prepared.", status=status)


def record_kernel_review(
    paths: IntakePaths,
    *,
    actor: str,
    completed: bool,
    skipped: bool,
    skip_reason: str,
    dry_run: bool,
) -> PhaseResult:
    _expect_state(paths, {"kernel_review_pending", "kernel_review_advisory_complete"})
    changed = [paths.intake_status.relative_to(paths.base_dir).as_posix()]
    if completed and skipped:
        raise IntakeStateError("Kernel review cannot be both completed and skipped.")
    if not completed and not skipped:
        raise IntakeStateError("Kernel review recording requires either completed or skipped.")
    if skipped and not skip_reason.strip():
        raise IntakeStateError("Kernel skip requires a reason.")

    if dry_run:
        action = "skip" if skipped else "complete"
        return PhaseResult("record_kernel_review", True, changed, f"Would {action} kernel advisory review.")

    if skipped:
        status = transition_status(
            paths,
            actor=actor,
            lifecycle_state="kernel_review_advisory_complete",
            next_action="prepare_ratification_handoff",
            event_type="kernel_skipped",
            summary="Kernel advisory review skipped with recorded reason.",
            evidence_paths=[paths.kernel_dir.relative_to(paths.base_dir).as_posix()],
            patch={
                "kernel_status": "skipped_with_reason",
                "kernel_skip_reason": skip_reason,
            },
        )
    else:
        status = transition_status(
            paths,
            actor=actor,
            lifecycle_state="kernel_review_advisory_complete",
            next_action="prepare_ratification_handoff",
            event_type="kernel_findings_recorded",
            summary="Kernel advisory review completed.",
            evidence_paths=[paths.kernel_dir.relative_to(paths.base_dir).as_posix()],
            patch={"kernel_status": "advisory_complete"},
        )
    return PhaseResult("record_kernel_review", False, changed, "Kernel advisory state recorded.", status=status)


def prepare_ratification_handoff(paths: IntakePaths, *, actor: str, dry_run: bool) -> PhaseResult:
    _expect_state(paths, {"kernel_review_advisory_complete", "ratification_handoff_pending"})
    changed = [
        paths.ratification_dir.joinpath("README.md").relative_to(paths.base_dir).as_posix(),
        paths.ratification_dir.joinpath("RATIFICATION_HANDOFF.md").relative_to(paths.base_dir).as_posix(),
    ]
    if dry_run:
        return PhaseResult("prepare_ratification_handoff", True, changed, "Would scaffold ratification handoff artifacts.")

    created = prepare_ratification_artifacts(paths)
    status = transition_status(
        paths,
        actor=actor,
        lifecycle_state="ratification_handoff_ready",
        next_action="manual_resolution",
        event_type="ratification_handoff_prepared",
        summary="Ratification handoff artifacts prepared. Manual authority remains required.",
        evidence_paths=created or changed,
        patch={"ratification_handoff_status": "ready"},
    )
    return PhaseResult("prepare_ratification_handoff", False, created or changed, "Ratification handoff prepared.", status=status)


def status_time() -> str:
    from intake_state import utc_now_iso

    return utc_now_iso()

