"""
Compliance validation engine.

Validates primitive JSON (NodeContract, PolicyRecord, etc.) against
their extracted JSON schemas and additional governance rules.

Used by both the MCP server and REST API via the GovernanceService.
"""

import json
from pathlib import Path

from schema_extractor import load_schema, list_available_schemas

try:
    from jsonschema import validate, ValidationError, SchemaError
except ImportError:
    validate = None
    ValidationError = Exception
    SchemaError = Exception


def validate_primitive(primitive_type: str, content: dict) -> dict:
    """Validate a primitive JSON object against its schema.

    Returns a structured result with valid flag and any violations.
    """
    schema = load_schema(primitive_type)
    if not schema:
        available = list_available_schemas()
        return {
            "valid": False,
            "violations": [{
                "rule": "SCHEMA_NOT_FOUND",
                "severity": "critical",
                "message": f"No schema found for primitive type '{primitive_type}'",
                "available_types": available,
            }],
        }

    if validate is None:
        return {
            "valid": False,
            "violations": [{
                "rule": "DEPENDENCY_MISSING",
                "severity": "critical",
                "message": "jsonschema package not installed. Run: pip install jsonschema",
            }],
        }

    violations = []

    try:
        validate(instance=content, schema=schema)
    except ValidationError as e:
        violations.append({
            "rule": "SCHEMA_VALIDATION",
            "severity": "high",
            "message": e.message,
            "path": list(e.absolute_path),
            "schema_path": list(e.absolute_schema_path),
        })
    except SchemaError as e:
        violations.append({
            "rule": "SCHEMA_ERROR",
            "severity": "critical",
            "message": f"Schema itself is invalid: {e.message}",
        })

    violations.extend(_check_governance_rules(primitive_type, content))

    return {
        "valid": len(violations) == 0,
        "primitive_type": primitive_type,
        "violations": violations,
    }


def _check_governance_rules(primitive_type: str, content: dict) -> list[dict]:
    """Apply governance-level rules beyond schema validation."""
    violations = []

    if primitive_type == "NodeContract":
        if content.get("additionalProperties") is not False:
            violations.append({
                "rule": "GOVERNANCE_ADDITIONAL_PROPERTIES",
                "severity": "high",
                "message": "NodeContracts must set additionalProperties: false (Execution Law: deterministic execution)",
                "reference": "governance://documents/AIOS-CORE-001",
            })

        policy_tags = content.get("properties", {}).get("policy_tags", {})
        if not policy_tags:
            violations.append({
                "rule": "GOVERNANCE_POLICY_TAGS",
                "severity": "medium",
                "message": "NodeContracts should define policy_tags for risk tier classification",
                "reference": "governance://documents/AIOS-SPEC-002",
            })

    if primitive_type == "PolicyRecord":
        failure_mode = content.get("properties", {}).get("failure_mode", {})
        if failure_mode:
            enum_vals = failure_mode.get("enum", [])
            if "fail_open" in enum_vals:
                violations.append({
                    "rule": "GOVERNANCE_FAIL_OPEN",
                    "severity": "medium",
                    "message": "PolicyRecords with fail_open must include Tier 3 elevation documentation",
                    "reference": "governance://documents/AIOS-SPEC-002",
                })

    return violations


def validate_kit_manifest(manifest: dict) -> dict:
    """Validate a Kit manifest against Marketplace Terms requirements."""
    violations = []

    required_fields = ["name", "version", "vendor", "node_contracts"]
    for field in required_fields:
        if field not in manifest:
            violations.append({
                "rule": "KIT_REQUIRED_FIELD",
                "severity": "high",
                "message": f"Kit manifest missing required field: '{field}'",
                "reference": "governance://documents/AIOS-COMM-001",
            })

    if "security_attestation" not in manifest:
        violations.append({
            "rule": "KIT_SECURITY_ATTESTATION",
            "severity": "high",
            "message": "Marketplace Terms require a security attestation in the Kit manifest",
            "reference": "governance://documents/AIOS-COMM-001",
        })

    if "license" not in manifest:
        violations.append({
            "rule": "KIT_LICENSE",
            "severity": "medium",
            "message": "Kit manifest should specify a license field",
            "reference": "governance://documents/AIOS-COMM-001",
        })

    return {
        "valid": len(violations) == 0,
        "violations": violations,
    }
