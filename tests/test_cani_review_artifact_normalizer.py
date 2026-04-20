from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from cani_review_artifact_normalizer import ReviewArtifactNormalizationError  # pyright: ignore[reportMissingImports]
from cani_review_artifact_normalizer import normalize_review_artifact_to_intake_envelope  # pyright: ignore[reportMissingImports]


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _read_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _valid_spec() -> dict:
    return {
        "review_artifact_ref": "reviews/cani/review_artifacts/review-001.md",
        "ingestion_envelope_id": "env-review-artifact-001",
        "recorded_at": "2026-04-09T00:00:00Z",
        "signal_family": "observation_intake",
        "signal_type": "review_artifact_observation",
        "admitted_by": "review-operator-test",
        "evidence_basis": "Governed review artifact captured for intake review.",
        "stream_key": "review-artifact-stream-1",
        "sequence_id": 1,
        "evidence_refs": [
            "reviews/cani/review_artifacts/review-001.md",
            "reviews/cani/review_artifacts/evidence-001.md",
        ],
        "observed_by": "review-operator-test",
        "confidence": "high",
        "notes": "Deterministic review-artifact normalization slice.",
    }


def test_normalize_review_artifact_validates_to_pass(tmp_path: Path):
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "review-001.md", "# Review artifact\n")
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "evidence-001.md", "# Evidence\n")
    output_path = tmp_path / "reviews" / "cani" / "intake" / "env-review-artifact-001.yaml"

    result = normalize_review_artifact_to_intake_envelope(_valid_spec(), output_path=output_path, base_dir=tmp_path)

    assert result.validator_result.outcome == "pass"
    assert result.output_path == "reviews/cani/intake/env-review-artifact-001.yaml"
    assert result.persisted_handoff_performed is False

    envelope = _read_yaml(output_path)
    assert envelope["source_surface"] == "review_artifact"
    assert envelope["payload_ref"] == "reviews/cani/review_artifacts/review-001.md"
    assert envelope["source_artifact_ref"] == "reviews/cani/review_artifacts/review-001.md"
    assert envelope["normalization_state"] == "normalized"
    assert envelope["provenance"]["admitted_by"] == "review-operator-test"
    assert envelope["sequence"]["sequence_id"] == 1


def test_normalize_review_artifact_refuses_repo_boundary_escape(tmp_path: Path):
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "evidence-001.md", "# Evidence\n")
    spec = _valid_spec()
    spec["review_artifact_ref"] = "../../outside.md"
    output_path = tmp_path / "reviews" / "cani" / "intake" / "env-review-artifact-escape.yaml"

    try:
        normalize_review_artifact_to_intake_envelope(spec, output_path=output_path, base_dir=tmp_path)
    except ReviewArtifactNormalizationError as exc:
        assert "escapes the repo authority boundary" in str(exc)
    else:
        raise AssertionError("Expected repo-boundary escape to be refused.")

    assert not output_path.exists()


def test_normalize_review_artifact_refuses_missing_required_provenance_or_evidence(tmp_path: Path):
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "review-001.md", "# Review artifact\n")
    output_path = tmp_path / "reviews" / "cani" / "intake" / "env-review-artifact-missing.yaml"
    spec = _valid_spec()
    spec.pop("evidence_basis")

    try:
        normalize_review_artifact_to_intake_envelope(spec, output_path=output_path, base_dir=tmp_path)
    except ReviewArtifactNormalizationError as exc:
        assert "missing required keys" in str(exc)
    else:
        raise AssertionError("Expected missing provenance/evidence field to be refused.")

    assert not output_path.exists()


def test_normalize_review_artifact_refuses_input_normalization_state_override(tmp_path: Path):
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "review-001.md", "# Review artifact\n")
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "evidence-001.md", "# Evidence\n")
    output_path = tmp_path / "reviews" / "cani" / "intake" / "env-review-artifact-override.yaml"
    spec = _valid_spec()
    spec["normalization_state"] = "raw_captured"

    try:
        normalize_review_artifact_to_intake_envelope(spec, output_path=output_path, base_dir=tmp_path)
    except ReviewArtifactNormalizationError as exc:
        assert "unsupported keys" in str(exc)
        assert "normalization_state" in str(exc)
    else:
        raise AssertionError("Expected normalization_state override to be refused.")

    assert not output_path.exists()


def test_normalize_review_artifact_refuses_invalid_normalized_output_via_validator(tmp_path: Path):
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "review-001.md", "# Review artifact\n")
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "evidence-001.md", "# Evidence\n")
    output_path = tmp_path / "reviews" / "cani" / "intake" / "env-review-artifact-invalid.yaml"
    spec = _valid_spec()
    spec["confidence"] = "certain"

    try:
        normalize_review_artifact_to_intake_envelope(spec, output_path=output_path, base_dir=tmp_path)
    except ReviewArtifactNormalizationError as exc:
        assert "failed validation" in str(exc)
        assert "intake_envelope provenance_confidence_invalid" not in str(exc)
    else:
        raise AssertionError("Expected validator refusal for invalid normalized envelope.")

    assert not output_path.exists()


def test_normalize_review_artifact_stops_at_validator_output_without_writer_persistence(tmp_path: Path):
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "review-001.md", "# Review artifact\n")
    _write_text(tmp_path / "reviews" / "cani" / "review_artifacts" / "evidence-001.md", "# Evidence\n")
    output_path = tmp_path / "reviews" / "cani" / "intake" / "env-review-artifact-stop.yaml"

    result = normalize_review_artifact_to_intake_envelope(_valid_spec(), output_path=output_path, base_dir=tmp_path)

    assert result.validator_result.outcome == "pass"
    assert result.persisted_handoff_performed is False
    assert output_path.exists()
    assert not (tmp_path / "reviews" / "cani" / "observation_sets").exists()
    assert not (tmp_path / "reviews" / "cani" / "recommendations").exists()
