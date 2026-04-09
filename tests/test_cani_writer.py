from __future__ import annotations

from pathlib import Path
import sys

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from cani_validator import validate_observation_set_dir, validate_recommendation_dir  # pyright: ignore[reportMissingImports]
from cani_writer import CaniWriterError  # pyright: ignore[reportMissingImports]
from cani_writer import append_observation_event  # pyright: ignore[reportMissingImports]
from cani_writer import append_recommendation_event  # pyright: ignore[reportMissingImports]
from cani_writer import materialize_observation_set  # pyright: ignore[reportMissingImports]
from cani_writer import materialize_recommendation_packet  # pyright: ignore[reportMissingImports]
from cani_writer import update_recommendation_status  # pyright: ignore[reportMissingImports]


def _read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _materialize_valid_recommendation_packet(tmp_path: Path) -> Path:
    target_dir = tmp_path / "reviews" / "cani" / "recommendations" / "rec-alpha"
    linked_plan = tmp_path / "reviews" / "amd_2026_015" / "planning" / "ARCHITECT_PLAN.md"
    linked_plan.parent.mkdir(parents=True, exist_ok=True)
    linked_plan.write_text("# Architect plan\n", encoding="utf-8")

    materialize_recommendation_packet(
        target_dir,
        base_dir=tmp_path,
        identity={
            "recommendation_id": "rec-001",
            "recommendation_slug": "rec-alpha",
            "storage_schema_version": "1",
            "recommendation_path": "reviews/cani/recommendations/rec-alpha",
            "source_schema_document_id": "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001",
            "created_at": "2026-04-09T00:00:00Z",
            "created_by": "test",
            "source_observation_refs": ["ob-001"],
        },
        status={
            "recommendation_id": "rec-001",
            "recommendation_slug": "rec-alpha",
            "authority_status": "advisory_only",
            "routing_target": "architect_planning",
            "routing_state": "proposed",
            "review_status": "not_started",
            "artifact_health": "healthy",
            "supersedes": "",
            "superseded_by": "",
            "status_updated_at": "2026-04-09T00:00:00Z",
            "status_updated_by": "test",
            "linked_planning_path": "reviews/amd_2026_015/planning/ARCHITECT_PLAN.md",
            "routing_note": "Prepared for architect review.",
        },
        first_event={
            "event_id": "evt-001",
            "timestamp": "2026-04-09T00:00:00Z",
            "actor": "test",
            "event_type": "recommendation_initialized",
            "from_state": "",
            "to_state": "proposed",
            "summary": "Recommendation created.",
            "evidence_paths": [],
        },
        handoff_note="# Recommendation handoff (non-authoritative)\n\nYAML wins over prose.\n",
    )
    return target_dir


def test_materialize_valid_observation_set(tmp_path: Path):
    target_dir = tmp_path / "reviews" / "cani" / "observation_sets" / "set-alpha"

    materialize_observation_set(
        target_dir,
        base_dir=tmp_path,
        identity={
            "observation_set_id": "obs-set-001",
            "set_slug": "set-alpha",
            "storage_schema_version": "1",
            "set_path": "reviews/cani/observation_sets/set-alpha",
            "source_schema_document_id": "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001",
            "created_at": "2026-04-09T00:00:00Z",
            "created_by": "test",
        },
        first_event={
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
        },
    )

    result = validate_observation_set_dir(target_dir, base_dir=tmp_path)
    identity = _read_yaml(target_dir / "OBSERVATION_SET_IDENTITY.yaml")

    assert result.outcome == "pass"
    assert identity["set_path"] == "reviews/cani/observation_sets/set-alpha"


def test_materialize_valid_recommendation_packet(tmp_path: Path):
    target_dir = _materialize_valid_recommendation_packet(tmp_path)

    result = validate_recommendation_dir(target_dir, base_dir=tmp_path)
    status = _read_yaml(target_dir / "RECOMMENDATION_STATUS.yaml")

    assert result.outcome == "pass"
    assert status["routing_state"] == "proposed"


def test_append_recommendation_event_success(tmp_path: Path):
    target_dir = _materialize_valid_recommendation_packet(tmp_path)

    append_recommendation_event(
        target_dir,
        base_dir=tmp_path,
        event={
            "event_id": "evt-002",
            "timestamp": "2026-04-09T00:01:00Z",
            "actor": "test",
            "event_type": "recommendation_status_corrected",
            "from_state": "proposed",
            "to_state": "proposed",
            "summary": "Metadata corrected without lifecycle transition.",
            "evidence_paths": [],
        },
    )

    events = _read_yaml(target_dir / "RECOMMENDATION_EVENTS.yaml")["events"]
    result = validate_recommendation_dir(target_dir, base_dir=tmp_path)

    assert len(events) == 2
    assert events[-1]["event_id"] == "evt-002"
    assert result.outcome == "pass"


def test_append_observation_event_preserves_append_only_history(tmp_path: Path):
    target_dir = tmp_path / "reviews" / "cani" / "observation_sets" / "set-alpha"
    materialize_observation_set(
        target_dir,
        base_dir=tmp_path,
        identity={
            "observation_set_id": "obs-set-001",
            "set_slug": "set-alpha",
            "storage_schema_version": "1",
            "set_path": "reviews/cani/observation_sets/set-alpha",
            "source_schema_document_id": "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001",
            "created_at": "2026-04-09T00:00:00Z",
            "created_by": "test",
        },
        first_event={
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
        },
    )

    append_observation_event(
        target_dir,
        base_dir=tmp_path,
        event={
            "observation_id": "ob-002",
            "observed_at": "2026-04-09T00:01:00Z",
            "path_signature": "intent/path/a",
            "step_action": "confirm",
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
            "event_id": "evt-002",
        },
    )

    events = _read_yaml(target_dir / "OBSERVATION_SET_EVENTS.yaml")["events"]

    assert len(events) == 2
    assert events[0]["event_id"] == "evt-001"
    assert events[1]["event_id"] == "evt-002"

    with pytest.raises(CaniWriterError):
        materialize_observation_set(
            target_dir,
            base_dir=tmp_path,
            identity={
                "observation_set_id": "obs-set-001",
                "set_slug": "set-alpha",
                "storage_schema_version": "1",
                "set_path": "reviews/cani/observation_sets/set-alpha",
                "source_schema_document_id": "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001",
                "created_at": "2026-04-09T00:00:00Z",
                "created_by": "test",
            },
            first_event={
                "observation_id": "ob-999",
                "observed_at": "2026-04-09T00:02:00Z",
                "path_signature": "intent/path/b",
                "step_action": "rewrite",
                "outcome_state": "failed",
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
                "event_id": "evt-999",
            },
        )


def test_writer_refuses_invalid_path_boundary_escape(tmp_path: Path):
    outside_dir = tmp_path.parent / "outside" / "set-alpha"

    with pytest.raises(CaniWriterError):
        materialize_observation_set(
            outside_dir,
            base_dir=tmp_path,
            identity={
                "observation_set_id": "obs-set-001",
                "set_slug": "set-alpha",
                "storage_schema_version": "1",
                "set_path": "reviews/cani/observation_sets/set-alpha",
                "source_schema_document_id": "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001",
                "created_at": "2026-04-09T00:00:00Z",
                "created_by": "test",
            },
            first_event={
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
            },
        )


def test_writer_refuses_invalid_artifact_mutation(tmp_path: Path):
    target_dir = tmp_path / "reviews" / "cani" / "recommendations" / "rec-alpha"

    with pytest.raises(CaniWriterError):
        materialize_recommendation_packet(
            target_dir,
            base_dir=tmp_path,
            identity={
                "recommendation_id": "rec-001",
                "recommendation_slug": "rec-alpha",
                "storage_schema_version": "1",
                "recommendation_path": "reviews/cani/recommendations/rec-alpha",
                "source_schema_document_id": "AIOS-CANI-OBSERVATION-AND-RECOMMENDATION-SCHEMA-001",
                "created_at": "2026-04-09T00:00:00Z",
                "created_by": "test",
                "source_observation_refs": ["ob-001"],
                "routing_state": "proposed",
            },
            status={
                "recommendation_id": "rec-001",
                "recommendation_slug": "rec-alpha",
                "authority_status": "advisory_only",
                "routing_target": "architect_planning",
                "routing_state": "proposed",
                "review_status": "not_started",
                "artifact_health": "healthy",
                "supersedes": "",
                "superseded_by": "",
                "status_updated_at": "2026-04-09T00:00:00Z",
                "status_updated_by": "test",
            },
            first_event={
                "event_id": "evt-001",
                "timestamp": "2026-04-09T00:00:00Z",
                "actor": "test",
                "event_type": "recommendation_initialized",
                "from_state": "",
                "to_state": "proposed",
                "summary": "Recommendation created.",
                "evidence_paths": [],
            },
            handoff_note="# Recommendation handoff (non-authoritative)\n\nYAML wins over prose.\n",
        )


def test_update_recommendation_status_refuses_lifecycle_change_and_rolls_back(tmp_path: Path):
    target_dir = _materialize_valid_recommendation_packet(tmp_path)
    status_path = target_dir / "RECOMMENDATION_STATUS.yaml"
    before = status_path.read_text(encoding="utf-8")

    with pytest.raises(CaniWriterError):
        update_recommendation_status(
            target_dir,
            base_dir=tmp_path,
            status={
                "recommendation_id": "rec-001",
                "recommendation_slug": "rec-alpha",
                "authority_status": "routed_for_review",
                "routing_target": "architect_planning",
                "routing_state": "routed",
                "review_status": "pending",
                "artifact_health": "healthy",
                "supersedes": "",
                "superseded_by": "",
                "status_updated_at": "2026-04-09T00:02:00Z",
                "status_updated_by": "test",
                "linked_planning_path": "reviews/amd_2026_015/planning/ARCHITECT_PLAN.md",
                "routing_note": "Attempt routed transition without event.",
            },
        )

    after = status_path.read_text(encoding="utf-8")
    validated = validate_recommendation_dir(target_dir, base_dir=tmp_path)

    assert before == after
    assert validated.outcome == "pass"
