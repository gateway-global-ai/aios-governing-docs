"""
AIOS Governance MCP Server.

Exposes the governing document set as MCP resources and tools for AI agents.
Uses FastMCP for protocol handling and the shared GovernanceService for logic.

Usage:
    python governance_mcp_server.py
"""

from fastmcp import FastMCP

from governance_service import GovernanceService, GovernanceError

mcp = FastMCP(
    "AIOS Governance",
    description="Machine-readable interface to the AIOS governing document set",
)

service = GovernanceService()


def _format_result(result) -> str:
    """Convert a service result to a string response for MCP."""
    if isinstance(result, GovernanceError):
        return f"Error [{result.code}]: {result.message}"
    if isinstance(result, dict):
        import json
        return json.dumps(result, indent=2, default=str)
    if isinstance(result, list):
        import json
        return json.dumps(result, indent=2, default=str)
    return str(result)


# ── Resources ─────────────────────────────────────────────────────

@mcp.resource("governance://documents")
def resource_documents() -> str:
    """List of all governing documents with metadata."""
    docs = service.list_documents(include_drafts=True)
    import json
    return json.dumps(docs, indent=2)


@mcp.resource("governance://style-guide")
def resource_style_guide() -> str:
    """The AIOS Style Guide (binding writing conventions)."""
    return service.get_style_guide()


# ── Tools ─────────────────────────────────────────────────────────

@mcp.tool()
def list_documents(
    status: str | None = None,
    category: str | None = None,
    include_drafts: bool = False,
) -> str:
    """List all AIOS governing documents with optional filters.

    Args:
        status: Filter by status (e.g., 'ratified', 'draft')
        category: Filter by category (e.g., 'core', 'specification', 'commercial')
        include_drafts: Include draft documents (default: False)
    """
    result = service.list_documents(status=status, category=category, include_drafts=include_drafts)
    return _format_result(result)


@mcp.tool()
def get_document(document_id: str, include_drafts: bool = False) -> str:
    """Retrieve a specific AIOS governing document by its ID.

    Args:
        document_id: The document identifier (e.g., 'AIOS-CORE-001')
        include_drafts: Allow retrieving draft documents (default: False)
    """
    result = service.get_document(document_id, include_drafts=include_drafts)
    return _format_result(result)


@mcp.tool()
def get_document_versions(document_id: str) -> str:
    """List all available versions of a document (current + archived ratified versions).

    Args:
        document_id: The document identifier
    """
    result = service.get_document_versions(document_id)
    return _format_result(result)


@mcp.tool()
def search_documents(query: str) -> str:
    """Full-text search across all governing documents.

    Args:
        query: Search string to find in document content
    """
    result = service.search_documents(query)
    return _format_result(result)


@mcp.tool()
def list_primitives() -> str:
    """List all available primitive schemas (e.g., NodeContract, PolicyRecord)."""
    result = service.list_primitives()
    return _format_result(result)


@mcp.tool()
def get_primitive_schema(primitive_type: str) -> str:
    """Get the JSON Schema for a primitive type.

    Args:
        primitive_type: Name of the primitive (e.g., 'NodeContract', 'PolicyRecord')
    """
    result = service.get_primitive_schema(primitive_type)
    return _format_result(result)


@mcp.tool()
def get_glossary() -> str:
    """Get the canonical glossary from the Technical Manifesto."""
    result = service.get_glossary()
    return _format_result(result)


@mcp.tool()
def check_compliance(primitive_type: str, content: str) -> str:
    """Validate a primitive JSON object against its schema and governance rules.

    Args:
        primitive_type: Type of primitive ('NodeContract', 'PolicyRecord')
        content: JSON string of the primitive to validate
    """
    import json
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError as e:
        return _format_result(GovernanceError("INVALID_JSON", f"Could not parse JSON: {e}"))
    result = service.check_compliance(primitive_type, parsed)
    return _format_result(result)


@mcp.tool()
def check_conflicts(document_id: str | None = None) -> str:
    """Scan documents for cross-document conflicts (term mismatches, broken references).

    Args:
        document_id: Optional. Scan a single document against the set, or scan all if omitted.
    """
    result = service.check_conflicts(document_id)
    return _format_result(result)


@mcp.tool()
def diff_documents(document_id: str, version_a: str, version_b: str = "latest") -> str:
    """Compare two versions of a document and return a unified diff.

    Args:
        document_id: The document identifier (e.g., 'AIOS-CORE-001')
        version_a: First version to compare (e.g., '1.0.0')
        version_b: Second version to compare (default: 'latest' for current)
    """
    result = service.diff_documents(document_id, version_a, version_b)
    return _format_result(result)


@mcp.tool()
def propose_amendment(
    source_type: str,
    source_content: str,
    rationale: str,
    affected_documents: str,
) -> str:
    """Submit an amendment proposal for governance review.

    Args:
        source_type: Type of source ('article', 'research', 'standard', 'analysis')
        source_content: The source material text or URL
        rationale: Why this amendment is needed
        affected_documents: Comma-separated document IDs (e.g., 'AIOS-CORE-001,AIOS-SPEC-002')
    """
    doc_list = [d.strip() for d in affected_documents.split(",") if d.strip()]
    result = service.propose_amendment(source_type, source_content, rationale, doc_list)
    return _format_result(result)


@mcp.tool()
def get_amendment_status(amendment_id: str) -> str:
    """Check the status of an amendment proposal.

    Args:
        amendment_id: The amendment identifier (e.g., 'AMD-2026-abc123')
    """
    result = service.get_amendment_status(amendment_id)
    return _format_result(result)


@mcp.tool()
def get_source_status(source_name: str) -> str:
    """Check the quarantine status of an analyzed source.

    Args:
        source_name: The source folder name
    """
    result = service.get_source_status(source_name)
    return _format_result(result)


if __name__ == "__main__":
    mcp.run()
