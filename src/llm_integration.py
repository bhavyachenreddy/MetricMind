import os
from openai import OpenAI


def ask_llm(prompt: str) -> str:
    """Send a prompt to the LLM and return its response."""

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Please configure your API key."
        )

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-6-luna"),
        input=prompt,
    )

    return response.output_text


if __name__ == "__main__":
    answer = ask_llm(
        "You are MetricMind. Explain what business revenue means in one simple sentence."
    )

    print("LLM Response:")
    print(answer)