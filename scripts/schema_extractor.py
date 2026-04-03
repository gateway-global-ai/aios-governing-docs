"""
Extracts JSON schemas embedded in specification markdown files and saves them
as standalone .json files in specifications/schemas/.

Also provides functions for loading schemas programmatically (used by the
compliance engine and governance service layer).

Usage:
    python schema_extractor.py              # Extract all schemas
    python schema_extractor.py --list       # List available schemas
"""

import argparse
import json
import re
from pathlib import Path

from brand_config import expand_gateway_placeholders
from context_assembler import BASE_DIR, read_file

SPECS_DIR = BASE_DIR / "specifications"
SCHEMAS_DIR = SPECS_DIR / "schemas"


def extract_json_blocks(markdown: str) -> list[dict]:
    """Extract all fenced JSON code blocks from markdown that look like JSON schemas."""
    pattern = r"```json\s*\n(.*?)```"
    blocks = re.findall(pattern, markdown, re.DOTALL)

    schemas = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        try:
            parsed = json.loads(block)
            if isinstance(parsed, dict) and ("$schema" in parsed or "$id" in parsed or "type" in parsed):
                schemas.append(parsed)
        except json.JSONDecodeError:
            continue
    return schemas


def extract_schemas_from_specs() -> dict[str, dict]:
    """Scan all specification .md files and extract JSON schemas.

    Returns a dict mapping schema name (e.g., 'NodeContract') to the parsed schema.
    """
    if not SPECS_DIR.exists():
        return {}

    result = {}
    for md_file in sorted(SPECS_DIR.glob("*.md")):
        content = read_file(md_file)
        schemas = extract_json_blocks(content)
        if schemas:
            result[md_file.stem] = schemas[0]
    return result


def save_schemas_to_disk(schemas: dict[str, dict]):
    """Write extracted schemas as standalone .json files."""
    SCHEMAS_DIR.mkdir(parents=True, exist_ok=True)
    for name, schema in schemas.items():
        out_path = SCHEMAS_DIR / f"{name}.json"
        out_path.write_text(json.dumps(schema, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Extracted: specifications/schemas/{name}.json")


def load_schema(name: str) -> dict | None:
    """Load a schema by name, preferring the standalone .json file.

    Resolves {{GATEWAY_*}} placeholders from environment so $id and URLs match deployment.
    """
    json_path = SCHEMAS_DIR / f"{name}.json"
    if json_path.exists():
        raw = expand_gateway_placeholders(json_path.read_text(encoding="utf-8"))
        return json.loads(raw)

    md_path = SPECS_DIR / f"{name}.md"
    if md_path.exists():
        content = expand_gateway_placeholders(read_file(md_path))
        schemas = extract_json_blocks(content)
        if schemas:
            return schemas[0]
    return None


def list_available_schemas() -> list[str]:
    """List names of all available schemas."""
    names = set()
    if SCHEMAS_DIR.exists():
        for f in SCHEMAS_DIR.glob("*.json"):
            names.add(f.stem)
    if SPECS_DIR.exists():
        for f in SPECS_DIR.glob("*.md"):
            content = read_file(f)
            if extract_json_blocks(content):
                names.add(f.stem)
    return sorted(names)


def main():
    parser = argparse.ArgumentParser(description="AIOS Schema Extractor")
    parser.add_argument("--list", action="store_true", help="List available schemas")
    args = parser.parse_args()

    if args.list:
        names = list_available_schemas()
        print(f"Available schemas ({len(names)}):")
        for n in names:
            print(f"  - {n}")
        return

    print("Extracting JSON schemas from specification documents...")
    schemas = extract_schemas_from_specs()
    if not schemas:
        print("No schemas found in specification documents.")
        return

    save_schemas_to_disk(schemas)
    print(f"\n{len(schemas)} schema(s) extracted to specifications/schemas/")


if __name__ == "__main__":
    main()
