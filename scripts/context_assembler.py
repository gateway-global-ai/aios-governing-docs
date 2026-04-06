"""
Shared module for assembling prompts with full governing context.
Used by all pipeline scripts (peer_review, revise_document, create_document, analyze_source).
"""

import asyncio
import json
import os
import re
from pathlib import Path
from datetime import date
from dotenv import load_dotenv
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")
# Repo-local secrets (e.g. Cursor workspace); overrides .env for the same keys.
load_dotenv(BASE_DIR / ".env.local", override=True)
# Optional: share LLM keys with ai-os-voice-interface (single .env.local in Apps).
# override=True so newer keys in .env.local win over stale copies in governing_docs/.env.
_voice_env = BASE_DIR.parent / "ai-os-voice-interface" / ".env.local"
if _voice_env.exists():
    load_dotenv(_voice_env, override=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CORE_DOCS = {
    "technical_manifesto": BASE_DIR / "core" / "technical_manifesto.md",
    "governance_constitution": BASE_DIR / "core" / "governance_constitution.md",
    "mpoa": BASE_DIR / "core" / "master_platform_operating_agreement.md",
}

CATEGORY_DIRS = {
    "core": "core",
    "specification": "specifications",
    "commercial": "commercial",
    "amendment": "amendments",
    "reference": "reference",
}

STYLE_GUIDE_PATH = BASE_DIR / "STYLE_GUIDE.md"
GRADING_RUBRIC_PATH = BASE_DIR / "templates" / "grading_rubric.md"
GRADING_RUBRIC_LIGHT_PATH = BASE_DIR / "templates" / "grading_rubric_light.md"
PEER_REVIEW_TEMPLATE_PATH = BASE_DIR / "templates" / "peer_review_template.md"
DOCUMENT_TEMPLATE_PATH = BASE_DIR / "templates" / "document_template.md"
AMENDMENT_TEMPLATE_PATH = BASE_DIR / "templates" / "amendment_template.md"
INTRODUCTION_PATH = BASE_DIR / "introduction.md"
DOCUMENT_REGISTRY_PATH = BASE_DIR / "DOCUMENT_REGISTRY.md"
DOCUMENT_REGISTRY_JSON_PATH = BASE_DIR / "DOCUMENT_REGISTRY.json"


def read_file(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"[File not found: {path}]"


def read_core_docs() -> dict[str, str]:
    return {name: read_file(path) for name, path in CORE_DOCS.items()}


def load_registry_json() -> list[dict]:
    """Load the JSON document registry. Falls back to scanning if JSON doesn't exist."""
    if DOCUMENT_REGISTRY_JSON_PATH.exists():
        return json.loads(DOCUMENT_REGISTRY_JSON_PATH.read_text(encoding="utf-8"))
    return []


def read_relevant_context(doc_path: str) -> dict[str, str]:
    """Read only the documents referenced in the target doc's front-matter cross_references.

    Uses the JSON registry to map document IDs to file paths. For core documents
    that cross-reference each other, this still returns all related core docs.
    For specifications, it returns only the specific docs they reference.
    """
    content = read_file(BASE_DIR / doc_path)
    metadata, _ = parse_front_matter(content)
    refs = metadata.get("cross_references", [])
    ref_ids = {r.get("doc_id") for r in refs if r.get("doc_id")}

    if not ref_ids:
        return read_core_docs()

    registry = load_registry_json()
    id_to_path = {d.get("document_id"): d.get("_path") for d in registry if d.get("document_id")}

    context = {}
    for doc_id in ref_ids:
        path = id_to_path.get(doc_id)
        if path:
            context[doc_id] = read_file(BASE_DIR / path)

    return context


def read_style_guide() -> str:
    return read_file(STYLE_GUIDE_PATH)


def read_grading_rubric(variant: str = "full") -> str:
    if variant == "light":
        return read_file(GRADING_RUBRIC_LIGHT_PATH)
    return read_file(GRADING_RUBRIC_PATH)


def read_peer_review_template() -> str:
    return read_file(PEER_REVIEW_TEMPLATE_PATH)


def read_document_template() -> str:
    return read_file(DOCUMENT_TEMPLATE_PATH)


def read_introduction() -> str:
    return read_file(INTRODUCTION_PATH)


def read_document_registry() -> str:
    return read_file(DOCUMENT_REGISTRY_PATH)


def read_prompt_template(prompt_name: str) -> str:
    path = BASE_DIR / "prompts" / prompt_name
    return read_file(path)


def get_doc_slug(doc_path: str) -> str:
    """Extract a slug from a document path for use in review folder names."""
    name = Path(doc_path).stem
    return re.sub(r"[^a-z0-9_]", "_", name.lower())


def find_reviews(doc_path: str, review_round: int | None = None) -> list[str]:
    """Find all existing reviews for a document, optionally filtered by round."""
    slug = get_doc_slug(doc_path)
    reviews_dir = BASE_DIR / "reviews" / slug

    if not reviews_dir.exists():
        return []

    results = []
    if review_round:
        round_dir = reviews_dir / f"round_{review_round}"
        if round_dir.exists():
            for f in sorted(round_dir.glob("*.md")):
                results.append(read_file(f))
    else:
        for round_dir in sorted(reviews_dir.glob("round_*")):
            for f in sorted(round_dir.glob("*.md")):
                results.append(read_file(f))

    return results


def find_revision_log(doc_path: str) -> str | None:
    """Find the revision log for a document, if it exists."""
    slug = get_doc_slug(doc_path)
    log_path = BASE_DIR / "reviews" / slug / "revision_log.md"
    if log_path.exists():
        return read_file(log_path)
    return None


def read_existing_specs() -> str:
    """Read all specification documents for cross-reference context."""
    specs_dir = BASE_DIR / "specifications"
    if not specs_dir.exists():
        return "[No specifications found]"

    parts = []
    for f in sorted(specs_dir.glob("*.md")):
        content = read_file(f)
        parts.append(f"### {f.stem}\n\n{content}")
    return "\n\n---\n\n".join(parts)


def get_next_review_number(doc_path: str, review_round: int) -> int:
    """Get the next sequential review number for a document and round."""
    slug = get_doc_slug(doc_path)
    round_dir = BASE_DIR / "reviews" / slug / f"round_{review_round}"
    round_dir.mkdir(parents=True, exist_ok=True)

    existing = list(round_dir.glob("review_*.md"))
    if not existing:
        return 1

    numbers = []
    for f in existing:
        match = re.search(r"review_(\d+)", f.stem)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def assemble_prompt(template_content: str, replacements: dict[str, str]) -> str:
    """Replace {{PLACEHOLDER}} tokens in a template with actual content."""
    result = template_content
    for key, value in replacements.items():
        result = result.replace(f"{{{{{key}}}}}", value)
    return result


def parse_front_matter(content: str) -> tuple[dict, str]:
    """Parse YAML front matter from a markdown document."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                metadata = yaml.safe_load(parts[1])
                body = parts[2].strip()
                return metadata or {}, body
            except yaml.YAMLError:
                pass
    return {}, content


def add_front_matter(content: str, metadata: dict) -> str:
    """Add or replace YAML front matter in a markdown document."""
    _, body = parse_front_matter(content)
    fm = yaml.dump(metadata, default_flow_style=False, sort_keys=False, allow_unicode=True)
    return f"---\n{fm}---\n\n{body}"


# --- API Clients ---

async def call_openai(
    system_prompt: str,
    user_prompt: str,
    model: str = "gpt-4o",
    *,
    max_tokens: int = 16000,
) -> str:
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        max_tokens=max_tokens,
        temperature=0.3,
    )
    return response.choices[0].message.content


async def call_deepseek(system_prompt: str, user_prompt: str, model: str = "deepseek-chat") -> str:
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        # DeepSeek API allows max_tokens in [1, 8192] (stricter than OpenAI).
        max_tokens=8192,
        temperature=0.3,
    )
    return response.choices[0].message.content


async def call_gemini(system_prompt: str, user_prompt: str, model: str = "gemini-2.5-pro") -> str:
    from google import genai
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = await asyncio.to_thread(
        client.models.generate_content,
        model=model,
        contents=f"{system_prompt}\n\n---\n\n{user_prompt}",
    )
    return response.text


MODEL_CALLERS = {
    "deepseek": call_deepseek,
    "openai": call_openai,
    "gemini": call_gemini,
}


async def call_models_parallel(
    models: list[str],
    system_prompt: str,
    user_prompt: str,
) -> dict[str, str]:
    """Call multiple models in parallel, return dict of model_name -> response."""
    tasks = {}
    for model_name in models:
        caller = MODEL_CALLERS[model_name]
        tasks[model_name] = asyncio.create_task(caller(system_prompt, user_prompt))

    results = {}
    for model_name, task in tasks.items():
        try:
            results[model_name] = await task
        except Exception as e:
            results[model_name] = f"[ERROR calling {model_name}: {e}]"

    return results


def save_review(doc_path: str, review_round: int, model_name: str, content: str) -> Path:
    """Save a review to the appropriate location and return the path."""
    slug = get_doc_slug(doc_path)
    num = get_next_review_number(doc_path, review_round)
    round_dir = BASE_DIR / "reviews" / slug / f"round_{review_round}"
    round_dir.mkdir(parents=True, exist_ok=True)

    filename = f"review_{num:03d}_{model_name}.md"
    out_path = round_dir / filename
    out_path.write_text(content, encoding="utf-8")
    return out_path


def today() -> str:
    return date.today().isoformat()
