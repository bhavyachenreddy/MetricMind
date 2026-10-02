import re

from llm_integration import ask_llm


def detect_query_type(question: str) -> str:
    """Detect the type of business metric question."""

    question = question.lower()

    if "revenue" in question and "profit" in question:
        return "revenue_and_profit"

    if "revenue" in question:
        return "revenue"

    if "profit" in question:
        return "profit"

    if "quantity" in question:
        return "quantity"

    return "general"


def build_metric_prompt(question: str) -> str:
    """Create a prompt for the LLM from a natural-language question."""

    query_type = detect_query_type(question)

    return f"""
You are MetricMind, a business metrics assistant.

User question:
{question}

Detected query type:
{query_type}

Explain what metric information the user is asking for.
Do not invent numerical results.
"""


if __name__ == "__main__":
    question = "Show me revenue and profit by region"

    prompt = build_metric_prompt(question)

    print("Query type:", detect_query_type(question))
    print("\nLLM Response:")
    print(ask_llm(prompt))