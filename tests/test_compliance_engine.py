"""Unit tests for the compliance engine."""

import pytest

from compliance_engine import validate_primitive, validate_kit_manifest


class TestValidatePrimitive:
    def test_nonexistent_schema(self):
        result = validate_primitive("FakeType", {})
        assert result["valid"] is False
        assert any(v["rule"] == "SCHEMA_NOT_FOUND" for v in result["violations"])

    def test_valid_structure(self):
        result = validate_primitive("NodeContract", {"type": "object"})
        assert "valid" in result
        assert "violations" in result
        assert isinstance(result["violations"], list)


class TestValidateKitManifest:
    def test_empty_manifest(self):
        result = validate_kit_manifest({})
        assert result["valid"] is False
        required_rules = [v["rule"] for v in result["violations"]]
        assert "KIT_REQUIRED_FIELD" in required_rules

    def test_minimal_valid_manifest(self):
        manifest = {
            "name": "test-kit",
            "version": "1.0.0",
            "vendor": "test-vendor",
            "node_contracts": [],
            "security_attestation": {"level": "basic"},
            "license": "MIT",
        }
        result = validate_kit_manifest(manifest)
        assert result["valid"] is True

    def test_missing_security_attestation(self):
        manifest = {
            "name": "test-kit",
            "version": "1.0.0",
            "vendor": "test-vendor",
            "node_contracts": [],
            "license": "MIT",
        }
        result = validate_kit_manifest(manifest)
        assert result["valid"] is False
        rules = [v["rule"] for v in result["violations"]]
        assert "KIT_SECURITY_ATTESTATION" in rules
