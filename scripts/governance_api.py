"""
AIOS Governance REST API.

Exposes the governing document set as a standard REST API with OpenAPI/Swagger.
Uses FastAPI for HTTP handling and the shared GovernanceService for logic.

Swagger UI available at: http://localhost:8100/docs

Usage:
    python governance_api.py
    uvicorn governance_api:app --host 0.0.0.0 --port 8100
"""

import os
from typing import Any

from fastapi import FastAPI, HTTPException, Query, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

from governance_service import GovernanceService, GovernanceError
import amendment_workflow as amendment_workflow_mod

app = FastAPI(
    title="AIOS Governance API",
    description=(
        "Machine-readable interface to the AIOS governing document set. "
        "Provides document retrieval, primitive schemas, compliance validation, "
        "amendment proposals, and conflict detection."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

service = GovernanceService()

API_KEY_READ = os.getenv("GOVERNANCE_API_KEY_READ")
API_KEY_WRITE = os.getenv("GOVERNANCE_API_KEY_WRITE")


def _check_read_key(x_api_key: str | None = Header(None)):
    if API_KEY_READ and x_api_key != API_KEY_READ:
        if API_KEY_WRITE and x_api_key == API_KEY_WRITE:
            return
        if API_KEY_READ:
            raise HTTPException(status_code=401, detail={"code": "UNAUTHORIZED", "message": "Invalid API key"})


def _check_write_key(x_api_key: str | None = Header(None)):
    if API_KEY_WRITE and x_api_key != API_KEY_WRITE:
        raise HTTPException(status_code=401, detail={"code": "UNAUTHORIZED", "message": "Write API key required"})


def _handle_result(result: Any):
    if isinstance(result, GovernanceError):
        code_map = {"NOT_FOUND": 404, "NOT_RATIFIED": 403, "FILE_MISSING": 404}
        status = code_map.get(result.code, 400)
        raise HTTPException(status_code=status, detail=result.to_dict())
    return result


# ── Models ────────────────────────────────────────────────────────

class CompliancePrimitiveRequest(BaseModel):
    primitive_type: str = Field(..., description="e.g., 'NodeContract', 'PolicyRecord'")
    content: dict = Field(..., description="The primitive JSON to validate")


class ComplianceKitRequest(BaseModel):
    kit_manifest: dict = Field(..., description="The Kit manifest JSON")


class AmendmentRequest(BaseModel):
    source_type: str = Field(..., description="'article', 'research', 'standard', 'analysis'")
    source_content: str = Field(..., description="Source material text or URL")
    rationale: str = Field(..., description="Why this amendment is needed")
    affected_documents: list[str] = Field(..., description="List of affected document IDs")


# ── Documents ─────────────────────────────────────────────────────

@app.get("/v1/documents", tags=["Documents"])
def list_documents_endpoint(
    status: str | None = Query(None, description="Filter by status"),
    category: str | None = Query(None, description="Filter by category"),
    include_drafts: bool = Query(False, description="Include drafts"),
    _key=Depends(_check_read_key),
):
    """List all governing documents with optional filters."""
    return service.list_documents(status=status, category=category, include_drafts=include_drafts)


@app.get("/v1/documents/{document_id}", tags=["Documents"])
def get_document_endpoint(
    document_id: str,
    include_drafts: bool = Query(False),
    _key=Depends(_check_read_key),
):
    """Get a specific document by ID."""
    return _handle_result(service.get_document(document_id, include_drafts=include_drafts))


@app.get("/v1/documents/{document_id}/versions", tags=["Documents"])
def get_document_versions_endpoint(
    document_id: str,
    _key=Depends(_check_read_key),
):
    """List all available versions of a document."""
    return _handle_result(service.get_document_versions(document_id))


@app.get("/v1/documents/{document_id}/diff", tags=["Documents"])
def diff_documents_endpoint(
    document_id: str,
    version_a: str = Query(..., description="First version (e.g., '1.0.0')"),
    version_b: str = Query("latest", description="Second version (default: 'latest')"),
    _key=Depends(_check_read_key),
):
    """Compare two versions of a document and return a unified diff."""
    return _handle_result(service.diff_documents(document_id, version_a, version_b))


@app.get("/v1/documents/search", tags=["Documents"])
def search_documents_endpoint(
    q: str = Query(..., description="Search query"),
    _key=Depends(_check_read_key),
):
    """Full-text search across all governing documents."""
    return service.search_documents(q)


# ── Primitives ────────────────────────────────────────────────────

@app.get("/v1/primitives", tags=["Primitives"])
def list_primitives_endpoint(_key=Depends(_check_read_key)):
    """List all available primitive schemas."""
    return service.list_primitives()


@app.get("/v1/primitives/{primitive_type}", tags=["Primitives"])
def get_primitive_endpoint(
    primitive_type: str,
    _key=Depends(_check_read_key),
):
    """Get the JSON schema for a primitive type."""
    return _handle_result(service.get_primitive_schema(primitive_type))


# ── Reference ─────────────────────────────────────────────────────

@app.get("/v1/glossary", tags=["Reference"])
def get_glossary_endpoint(_key=Depends(_check_read_key)):
    """Get the canonical glossary from the Technical Manifesto."""
    return service.get_glossary()


@app.get("/v1/style-guide", tags=["Reference"], response_class=PlainTextResponse)
def get_style_guide_endpoint(_key=Depends(_check_read_key)):
    """Get the AIOS Style Guide as markdown."""
    return service.get_style_guide()


# ── Compliance ────────────────────────────────────────────────────

@app.post("/v1/compliance/primitive", tags=["Compliance"])
def check_compliance_primitive(
    request: CompliancePrimitiveRequest,
    _key=Depends(_check_read_key),
):
    """Validate a NodeContract or PolicyRecord against its schema and governance rules."""
    return service.check_compliance(request.primitive_type, request.content)


@app.post("/v1/compliance/kit", tags=["Compliance"])
def check_compliance_kit(
    request: ComplianceKitRequest,
    _key=Depends(_check_read_key),
):
    """Validate a Kit manifest against Marketplace Terms requirements."""
    from compliance_engine import validate_kit_manifest
    return validate_kit_manifest(request.kit_manifest)


# ── Conflicts ─────────────────────────────────────────────────────

@app.get("/v1/conflicts", tags=["Conflicts"])
def check_conflicts_endpoint(
    document_id: str | None = Query(None, description="Scan single doc or all"),
    _key=Depends(_check_read_key),
):
    """Scan for cross-document conflicts."""
    return service.check_conflicts(document_id)


# ── Amendments ────────────────────────────────────────────────────

@app.post("/v1/amendments", tags=["Amendments"])
def propose_amendment_endpoint(
    request: AmendmentRequest,
    _key=Depends(_check_write_key),
):
    """Submit an amendment proposal."""
    result = service.propose_amendment(
        request.source_type,
        request.source_content,
        request.rationale,
        request.affected_documents,
    )
    return _handle_result(result)


@app.get("/v1/amendments/{amendment_id}", tags=["Amendments"])
def get_amendment_status_endpoint(
    amendment_id: str,
    _key=Depends(_check_read_key),
):
    """Get the status of an amendment proposal."""
    return _handle_result(service.get_amendment_status(amendment_id))


@app.get("/v1/sources/{source_name}/status", tags=["Amendments"])
def get_source_status_endpoint(
    source_name: str,
    _key=Depends(_check_read_key),
):
    """Get the quarantine status of an analyzed source."""
    return _handle_result(service.get_source_status(source_name))


# ── Amendment workflow (demo / founder program) ─────────────────

class AmendmentWorkflowCreate(BaseModel):
    template_id: str = Field(..., description="e.g. AMD-2026-004")


@app.get("/v1/amendment-workflow/templates", tags=["Amendment workflow"])
def amendment_workflow_list_templates(_key=Depends(_check_read_key)):
    """List amendment proposal templates available for a workflow run."""
    return amendment_workflow_mod.list_templates()


@app.post("/v1/amendment-workflow/runs", tags=["Amendment workflow"])
def amendment_workflow_create_run(
    request: AmendmentWorkflowCreate,
    _key=Depends(_check_read_key),
):
    """Start a new amendment program run (simulated reviews; no repo merge)."""
    try:
        return amendment_workflow_mod.create_run(request.template_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail={"error": {"code": "BAD_REQUEST", "message": str(e)}})


@app.get("/v1/amendment-workflow/runs/{run_id}", tags=["Amendment workflow"])
def amendment_workflow_get_run(run_id: str, _key=Depends(_check_read_key)):
    """Get run state: proposal, peer reviews, plan, console log."""
    try:
        return amendment_workflow_mod.get_run(run_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail={"error": {"code": "NOT_FOUND", "message": str(e)}})


@app.post("/v1/amendment-workflow/runs/{run_id}/advance", tags=["Amendment workflow"])
def amendment_workflow_advance(run_id: str, _key=Depends(_check_read_key)):
    """Advance the workflow to the next step (simulated)."""
    try:
        return amendment_workflow_mod.advance_run(run_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail={"error": {"code": "NOT_FOUND", "message": str(e)}})


# ── Action plan (synthesized from impact reports) ─────────────────

class ActionPlanBody(BaseModel):
    plan: dict = Field(..., description="Full action_plan.json object")


class ExecutePlanBody(BaseModel):
    dry_run: bool = Field(False, description="If true, subprocess steps are not run")


@app.get("/v1/sources/{source_name}/action-plan", tags=["Action plan"])
def get_action_plan_endpoint(source_name: str, _key=Depends(_check_read_key)):
    """Get synthesized action plan + execution log tail."""
    return _handle_result(service.get_action_plan(source_name))


@app.put("/v1/sources/{source_name}/action-plan", tags=["Action plan"])
def put_action_plan_endpoint(
    source_name: str,
    body: ActionPlanBody,
    _key=Depends(_check_write_key),
):
    """Replace action_plan.json (e.g. after UI approval edits)."""
    return _handle_result(service.put_action_plan(source_name, body.plan))


@app.post("/v1/sources/{source_name}/action-plan/execute", tags=["Action plan"])
def execute_action_plan_endpoint(
    source_name: str,
    body: ExecutePlanBody | None = None,
    _key=Depends(_check_write_key),
):
    """Run execute_action_plan.py logic for approved actions."""
    dry = body.dry_run if body else False
    return _handle_result(service.execute_action_plan_cli(source_name, dry_run=dry))


# ── Startup ───────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8100)
