from __future__ import annotations

from pathlib import Path

import yaml

from cani_validator import (
    PERSISTED_OBSERVATION_ARTIFACT,
    PERSISTED_RECOMMENDATION_ARTIFACT,
    TELEMETRY_INTAKE_ENVELOPE,
    detect_cani_artifact_class,
    validate_intake_envelope_path,
    validate_observation_set_dir,
    validate_recommendation_dir,
)


def _write_yaml(path: Path, body: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(body, sort_keys=False), encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _make_valid_observation_set(base_dir: Path) -> Path:
    obs_dir = base_dir / "reviews" / "cani" / "observation_sets" / "set-alpha"
    obs_dir.mkdir(parents=True, exist_ok=True)
    _write_yaml(
        obs_dir / "OBSERVATION_SET_IDENTITY.yaml",
        {
            "observation_set_id": "obs-set-001",
            "set_slug": "set-alpha",
            "storage_schema_version": "1",
            "set_path": "reviews/cani/observation_sets/set-alpha",
            "source_schema_document_id": "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001",
            "created_at": "2026-04-09T00:00:00Z",
            "created_by": "test",
        },
    )
    _write_yaml(
        obs_dir / "OBSERVATION_SET_EVENTS.yaml",
        {
            "storage_schema_version": "1",
            "observation_set_id": "obs-set-001",
            "set_slug": "set-alpha",
            "events": [
                {
                    "observation_id": "ob-001",
                    "observed_at": "2026-04-09T00:00:00Z",
                    "path_signature": "intent/path/a",
                    "step_action": "open_surface",
                    "outcome_state": "success",
                    "fallback_occurred": False,
                    "backtrack_occurred": False,
                    "burden_summary": {
                        "visible_burden_level": "low",
                        "context_burden_level": "low",
                        "explanation_burden_level": "low",
                        "path_efficiency_state": "direct",
                    },
                    "evidence_surface": "shell",
                    "event_type": "observation_recorded",
                    "event_id": "evt-001",
                }
            ],
        },
    )
    return obs_dir


def _make_valid_recommendation_packet(base_dir: Path) -> Path:
    packet_dir = base_dir / "reviews" / "cani" / "recommendations" / "rec-alpha"
    packet_dir.mkdir(parents=True, exist_ok=True)
    _write_yaml(
        packet_dir / "RECOMMENDATION_IDENTITY.yaml",
        {
            "recommendation_id": "rec-001",
            "recommendation_slug": "rec-alpha",
            "storage_schema_version": "1",
            "recommendation_path": "reviews/cani/recommendations/rec-alpha",
            "source_schema_document_id": "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001",
            "created_at": "2026-04-09T00:00:00Z",
            "created_by": "test",
            "source_observation_refs": ["ob-001"],
        },
    )
    _write_text(
        packet_dir / "HANDOFF_NOTE.md",
        "# Recommendation handoff (non-authoritative)\n\nYAML wins over prose.\n",
    )
    return packet_dir


def test_validate_observation_set_pass(tmp_path: Path):
    obs_dir = _make_valid_observation_set(tmp_path)

    result = validate_observation_set_dir(obs_dir, base_dir=tmp_path)

    assert result.outcome == "pass"
    assert result.findings == []


def test_validate_observation_set_advisory_warning_for_handoff_text(tmp_path: Path):
    obs_dir = _make_valid_observation_set(tmp_path)
    _write_text(obs_dir / "HANDOFF_NOTE.md", "# Handoff\n\nOperator orientation only.\n")

    result = validate_observation_set_dir(obs_dir, base_dir=tmp_path)

    assert result.outcome == "advisory_warning"
    assert any(f.code == "observation_handoff_authority_line_missing" for f in result.findings)


def test_validate_recommendation_packet_blocked_for_missing_linked_path(tmp_path: Path):
    packet_dir = _make_valid_recommendation_packet(tmp_path)
    _write_yaml(
        packet_dir / "RECOMMENDATION_STATUS.yaml",
        {
            "recommendation_id": "rec-001",
            "recommendation_slug": "rec-alpha",
            "authority_status": "routed_for_review",
            "routing_target": "architect_planning",
            "routing_state": "routed",
            "review_status": "pending",
            "artifact_health": "healthy",
            "supersedes": "",
            "superseded_by": "",
            "status_updated_at": "2026-04-09T00:00:00Z",
            "status_updated_by": "test",
            "linked_planning_path": "reviews/amd_2026_015/planning/ARCHITECT_PLAN.md",
            "routing_note": "Route into architect lane.",
        },
    )
    _write_yaml(
        packet_dir / "RECOMMENDATION_EVENTS.yaml",
        {
            "storage_schema_version": "1",
            "recommendation_id": "rec-001",
            "recommendation_slug": "rec-alpha",
            "events": [
                {
                    "event_id": "evt-001",
                    "timestamp": "2026-04-09T00:00:00Z",
                    "actor": "test",
                    "event_type": "recommendation_initialized",
                    "from_state": "",
                    "to_state": "proposed",
                    "summary": "Recommendation created.",
                    "evidence_paths": [],
                },
                {
                    "event_id": "evt-002",
                    "timestamp": "2026-04-09T00:01:00Z",
                    "actor": "test",
                    "event_type": "recommendation_routed",
                    "from_state": "proposed",
                    "to_state": "routed",
                    "summary": "Recommendation routed for review.",
                    "evidence_paths": [],
                },
            ],
        },
    )

    result = validate_recommendation_dir(packet_dir, base_dir=tmp_path)

    assert result.outcome == "blocked"
    assert any(f.code == "recommendation_linked_planning_path_missing_ref" for f in result.findings)


def test_validate_recommendation_packet_fail_for_authority_lifecycle_mismatch(tmp_path: Path):
    packet_dir = _make_valid_recommendation_packet(tmp_path)
    linked_plan = tmp_path / "reviews" / "amd_2026_015" / "planning" / "ARCHITECT_PLAN.md"
    _write_text(linked_plan, "# Architect plan\n")
    _write_yaml(
        packet_dir / "RECOMMENDATION_STATUS.yaml",
        {
            "recommendation_id": "rec-001",
            "recommendation_slug": "rec-alpha",
            "authority_status": "accepted_for_planning",
            "routing_target": "architect_planning",
            "routing_state": "accepted",
            "review_status": "pending",
            "artifact_health": "healthy",
            "supersedes": "",
            "superseded_by": "",
            "status_updated_at": "2026-04-09T00:00:00Z",
            "status_updated_by": "test",
            "linked_planning_path": "reviews/amd_2026_015/planning/ARCHITECT_PLAN.md",
            "routing_note": "Accepted into architect planning.",
        },
    )
    _write_yaml(
        packet_dir / "RECOMMENDATION_EVENTS.yaml",
        {
            "storage_schema_version": "1",
            "recommendation_id": "rec-001",
            "recommendation_slug": "rec-alpha",
            "events": [
                {
                    "event_id": "evt-001",
                    "timestamp": "2026-04-09T00:00:00Z",
                    "actor": "test",
                    "event_type": "recommendation_initialized",
                    "from_state": "",
                    "to_state": "proposed",
                    "summary": "Recommendation created.",
                    "evidence_paths": [],
                },
                {
                    "event_id": "evt-002",
                    "timestamp": "2026-04-09T00:01:00Z",
                    "actor": "test",
                    "event_type": "recommendation_accepted_for_planning",
                    "from_state": "proposed",
                    "to_state": "accepted",
                    "summary": "Recommendation accepted for planning.",
                    "evidence_paths": [],
                },
            ],
        },
    )

    result = validate_recommendation_dir(packet_dir, base_dir=tmp_path)

    assert result.outcome == "fail"
    assert any(f.code == "recommendation_accepted_state_mismatch" for f in result.findings)


def test_validate_intake_envelope_pass(tmp_path: Path):
    payload = tmp_path / "reviews" / "cani" / "raw" / "payload.json"
    evidence = tmp_path / "reviews" / "cani" / "raw" / "evidence.md"
    _write_text(payload, '{"sample": true}\n')
    _write_text(evidence, "# Evidence\n")
    envelope_path = tmp_path / "reviews" / "cani" / "intake" / "env-001.yaml"
    _write_yaml(
        envelope_path,
        {
            "ingestion_envelope_id": "env-001",
            "envelope_schema_version": "1",
            "recorded_at": "2026-04-09T00:00:00Z",
            "signal_family": "observation_intake",
            "signal_type": "observed_path",
            "source_surface": "shell",
            "provenance": {
                "admitted_by": "test",
                "evidence_basis": "Observed from governed shell flow.",
                "confidence": "high",
            },
            "sequence": {
                "stream_key": "session-1",
                "sequence_id": 1,
            },
            "normalization_state": "normalized",
            "payload_ref": "reviews/cani/raw/payload.json",
            "evidence_refs": ["reviews/cani/raw/evidence.md"],
        },
    )

    result = validate_intake_envelope_path(envelope_path, base_dir=tmp_path)

    assert result.outcome == "pass"
    assert result.findings == []


def test_validate_intake_envelope_fail_for_external_payload_ref(tmp_path: Path):
    evidence = tmp_path / "reviews" / "cani" / "raw" / "evidence.md"
    _write_text(evidence, "# Evidence\n")
    envelope_path = tmp_path / "reviews" / "cani" / "intake" / "env-002.yaml"
    _write_yaml(
        envelope_path,
        {
            "ingestion_envelope_id": "env-002",
            "envelope_schema_version": "1",
            "recorded_at": "2026-04-09T00:00:00Z",
            "signal_family": "recommendation_intake",
            "signal_type": "recommendation_candidate",
            "source_surface": "review_artifact",
            "provenance": {
                "admitted_by": "test",
                "evidence_basis": "Observed from review synthesis.",
            },
            "sequence": {
                "stream_key": "session-2",
                "sequence_id": 1,
            },
            "normalization_state": "normalized",
            "payload_ref": "https://example.com/raw.json",
            "evidence_refs": ["reviews/cani/raw/evidence.md"],
        },
    )

    result = validate_intake_envelope_path(envelope_path, base_dir=tmp_path)

    assert result.outcome == "fail"
    assert any(f.code == "intake_envelope_payload_ref_external_authority" for f in result.findings)


def test_validate_intake_envelope_blocked_for_missing_payload_target(tmp_path: Path):
    evidence = tmp_path / "reviews" / "cani" / "raw" / "evidence.md"
    _write_text(evidence, "# Evidence\n")
    envelope_path = tmp_path / "reviews" / "cani" / "intake" / "env-003.yaml"
    _write_yaml(
        envelope_path,
        {
            "ingestion_envelope_id": "env-003",
            "envelope_schema_version": "1",
            "recorded_at": "2026-04-09T00:00:00Z",
            "signal_family": "observation_intake",
            "signal_type": "observed_path",
            "source_surface": "shell",
            "provenance": {
                "admitted_by": "test",
                "evidence_basis": "Observed from governed shell flow.",
            },
            "sequence": {
                "stream_key": "session-3",
                "sequence_id": 1,
            },
            "normalization_state": "raw_captured",
            "payload_ref": "reviews/cani/raw/missing-payload.json",
            "evidence_refs": ["reviews/cani/raw/evidence.md"],
        },
    )

    result = validate_intake_envelope_path(envelope_path, base_dir=tmp_path)

    assert result.outcome == "blocked"
    assert any(f.code == "intake_envelope_payload_ref_missing_target" for f in result.findings)


def test_validate_intake_envelope_fail_for_relative_payload_escape(tmp_path: Path):
    evidence = tmp_path / "reviews" / "cani" / "raw" / "evidence.md"
    _write_text(evidence, "# Evidence\n")
    envelope_path = tmp_path / "reviews" / "cani" / "intake" / "env-004.yaml"
    _write_yaml(
        envelope_path,
        {
            "ingestion_envelope_id": "env-004",
            "envelope_schema_version": "1",
            "recorded_at": "2026-04-09T00:00:00Z",
            "signal_family": "observation_intake",
            "signal_type": "observed_path",
            "source_surface": "shell",
            "provenance": {
                "admitted_by": "test",
                "evidence_basis": "Observed from governed shell flow.",
            },
            "sequence": {
                "stream_key": "session-4",
                "sequence_id": 1,
            },
            "normalization_state": "raw_captured",
            "payload_ref": "../../outside.json",
            "evidence_refs": ["reviews/cani/raw/evidence.md"],
        },
    )

    result = validate_intake_envelope_path(envelope_path, base_dir=tmp_path)

    assert result.outcome == "fail"
    assert any(f.code == "intake_envelope_payload_ref_invalid" for f in result.findings)


def test_detect_cani_artifact_class_for_supported_targets(tmp_path: Path):
    obs_dir = _make_valid_observation_set(tmp_path)
    packet_dir = _make_valid_recommendation_packet(tmp_path)
    envelope_path = tmp_path / "reviews" / "cani" / "intake" / "env-detect.yaml"
    _write_yaml(
        envelope_path,
        {
            "ingestion_envelope_id": "env-detect",
            "envelope_schema_version": "1",
            "recorded_at": "2026-04-09T00:00:00Z",
            "signal_family": "observation_intake",
            "signal_type": "observed_path",
            "source_surface": "shell",
            "provenance": {
                "admitted_by": "test",
                "evidence_basis": "Observed from governed shell flow.",
            },
            "sequence": {
                "stream_key": "session-detect",
                "sequence_id": 1,
            },
            "normalization_state": "raw_captured",
            "payload_ref": "reviews/cani/intake/env-detect.yaml",
            "evidence_refs": ["reviews/cani/intake/env-detect.yaml"],
        },
    )

    assert detect_cani_artifact_class(obs_dir) == PERSISTED_OBSERVATION_ARTIFACT
    assert detect_cani_artifact_class(packet_dir) == PERSISTED_RECOMMENDATION_ARTIFACT
    assert detect_cani_artifact_class(envelope_path) == TELEMETRY_INTAKE_ENVELOPE
