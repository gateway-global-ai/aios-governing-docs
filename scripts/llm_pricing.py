"""
Rough USD cost helpers for LLM calls used in this repo.

Rates are approximate paid-tier list prices; providers change pricing - verify on:
  https://openai.com/api/pricing/
  https://api-docs.deepseek.com/quick_start/pricing
  https://ai.google.dev/gemini-api/docs/pricing

`max_tokens` / completion limits cap the *worst-case output bill* per request;
input cost depends on prompt size (core docs + source can be ~50k-200k+ tokens).
"""

from __future__ import annotations

# USD per 1 million tokens (paid tier, typical; prompts under 200k context where split)
OPENAI_GPT4O = {"input": 2.50, "output": 10.00}
DEEPSEEK_CHAT = {"input": 0.14, "output": 0.28}
# Align with call_gemini default (gemini-2.5-pro); same ballpark as 2.5 Pro family.
GEMINI_25_PRO = {"input": 1.25, "output": 10.00}


def usd_per_token(usd_per_million: float) -> float:
    return usd_per_million / 1_000_000.0


def max_output_cost_usd(max_output_tokens: int, usd_per_million_output: float) -> float:
    """Upper bound on output cost if the model uses the full completion budget."""
    return max_output_tokens * usd_per_token(usd_per_million_output)


def format_parallel_review_ceiling() -> str:
    """Explain output-token caps configured in context_assembler.call_openai / call_deepseek."""
    openai_cap = 16000
    deepseek_cap = 8192
    o_max = max_output_cost_usd(openai_cap, OPENAI_GPT4O["output"])
    d_max = max_output_cost_usd(deepseek_cap, DEEPSEEK_CHAT["output"])
    lines = [
        "Estimated output cost CEILING per call (if completion fills the cap):",
        f"  OpenAI (gpt-4o, max_tokens={openai_cap}): up to ~${o_max:.4f} output tokens only",
        f"  DeepSeek (deepseek-chat, max_tokens={deepseek_cap}): up to ~${d_max:.4f} output tokens only",
        "  Gemini (call_gemini): no max_tokens in code - billing is per token in+out;",
        f"      2.5 Pro-class rate ~ ${GEMINI_25_PRO['input']}/1M in, ${GEMINI_25_PRO['output']}/1M out",
        "",
        "Example: 100,000 input tokens to Gemini 2.5 Pro class ~ "
        f"${100_000 * usd_per_token(GEMINI_25_PRO['input']):.4f} (input only).",
        "Actual source-analysis runs vary with prompt size; check provider dashboards for usage.",
    ]
    return "\n".join(lines)


def format_source_analysis_three_way_note() -> str:
    """One block for analyze_source.py (3 parallel models)."""
    return (
        format_parallel_review_ceiling()
        + "\n"
        + "Triple parallel run: sum the three models' actual usage (not just these ceilings)."
    )
