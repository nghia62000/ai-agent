from typing import List

from llm_client import LLMClient


class Planner:
    """Analyze user request and break it into actionable tasks using an LLM."""

    def __init__(self, client: LLMClient | None = None) -> None:
        self.client = client or LLMClient()

    def plan(self, request: str) -> List[str]:
        request = request.strip()
        if not request:
            return []

        messages = [
            {
                "role": "system",
                "content": "You are an assistant that converts user requests into a numbered list of short tasks.",
            },
            {
                "role": "user",
                "content": f"Break the following request into tasks:\n{request}",
            },
        ]
        response = self.client.chat(messages)
        parts = [line.lstrip("- ").strip() for line in response.splitlines() if line.strip()]
        return parts or [request]
