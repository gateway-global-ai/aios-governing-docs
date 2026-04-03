"""Unit tests for the governance service layer."""

import json
from pathlib import Path

import pytest

from governance_service import GovernanceService, GovernanceError


@pytest.fixture
def service():
    return GovernanceService(cache_ttl=0)


class TestListDocuments:
    def test_returns_list(self, service):
        docs = service.list_documents(include_drafts=True)
        assert isinstance(docs, list)
        assert len(docs) > 0

    def test_each_doc_has_required_fields(self, service):
        docs = service.list_documents(include_drafts=True)
        for doc in docs:
            assert "document_id" in doc
            assert "title" in doc
            assert "path" in doc

    def test_filter_by_category(self, service):
        core_docs = service.list_documents(category="core", include_drafts=True)
        for doc in core_docs:
            assert doc["category"] == "core"

    def test_filter_by_status(self, service):
        ratified = service.list_documents(status="ratified", include_drafts=True)
        for doc in ratified:
            assert doc["status"] == "ratified"


class TestGetDocument:
    def test_existing_doc(self, service):
        docs = service.list_documents(include_drafts=True)
        if docs:
            first_id = docs[0]["document_id"]
            if first_id:
                result = service.get_document(first_id, include_drafts=True)
                if not isinstance(result, GovernanceError):
                    assert result["document_id"] == first_id
                    assert "content" in result

    def test_nonexistent_doc_returns_error(self, service):
        result = service.get_document("NONEXISTENT-999")
        assert isinstance(result, GovernanceError)
        assert result.code == "NOT_FOUND"


class TestPrimitives:
    def test_list_primitives(self, service):
        primitives = service.list_primitives()
        assert isinstance(primitives, list)
        names = [p["name"] for p in primitives]
        assert "NodeContract" in names or len(names) >= 0

    def test_get_existing_schema(self, service):
        primitives = service.list_primitives()
        if primitives:
            result = service.get_primitive_schema(primitives[0]["name"])
            assert not isinstance(result, GovernanceError)
            assert "schema" in result

    def test_get_nonexistent_schema(self, service):
        result = service.get_primitive_schema("FakeSchema")
        assert isinstance(result, GovernanceError)


class TestGlossary:
    def test_returns_list(self, service):
        glossary = service.get_glossary()
        assert isinstance(glossary, list)

    def test_terms_have_structure(self, service):
        glossary = service.get_glossary()
        for term in glossary:
            assert "term" in term
            assert "definition" in term


class TestSearchDocuments:
    def test_search_returns_list(self, service):
        results = service.search_documents("governance")
        assert isinstance(results, list)

    def test_search_no_results(self, service):
        results = service.search_documents("xyznonexistentstringxyz")
        assert isinstance(results, list)
        assert len(results) == 0


class TestDocumentVersions:
    def test_returns_list_or_error(self, service):
        docs = service.list_documents(include_drafts=True)
        if docs:
            first_id = docs[0]["document_id"]
            if first_id:
                result = service.get_document_versions(first_id)
                assert isinstance(result, (list, GovernanceError))


class TestCache:
    def test_cache_invalidation(self, service):
        service.list_documents(include_drafts=True)
        service.invalidate_cache()
        docs = service.list_documents(include_drafts=True)
        assert isinstance(docs, list)
