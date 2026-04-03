"""Unit tests for schema extraction."""

import json

import pytest

from schema_extractor import (
    extract_json_blocks,
    list_available_schemas,
    load_schema,
    extract_schemas_from_specs,
)


class TestExtractJsonBlocks:
    def test_extracts_valid_schema(self):
        md = '''# Example

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "name": {"type": "string"}
  }
}
```

Some other text.
'''
        blocks = extract_json_blocks(md)
        assert len(blocks) == 1
        assert blocks[0]["type"] == "object"

    def test_ignores_non_schema_json(self):
        md = '''```json
["just", "an", "array"]
```'''
        blocks = extract_json_blocks(md)
        assert len(blocks) == 0

    def test_handles_empty_markdown(self):
        blocks = extract_json_blocks("")
        assert blocks == []

    def test_handles_invalid_json(self):
        md = '''```json
{not valid json}
```'''
        blocks = extract_json_blocks(md)
        assert blocks == []


class TestListAvailableSchemas:
    def test_returns_list(self):
        names = list_available_schemas()
        assert isinstance(names, list)

    def test_includes_known_schemas(self):
        names = list_available_schemas()
        assert "NodeContract" in names or "PolicyRecord" in names


class TestLoadSchema:
    def test_load_existing(self):
        names = list_available_schemas()
        if names:
            schema = load_schema(names[0])
            assert schema is not None
            assert isinstance(schema, dict)

    def test_load_nonexistent(self):
        schema = load_schema("FakeNonexistentSchema")
        assert schema is None


class TestExtractFromSpecs:
    def test_returns_dict(self):
        schemas = extract_schemas_from_specs()
        assert isinstance(schemas, dict)
