from llm_client import LLMClient


class Critic:
    """Summarize and analyze execution errors using an LLM."""

    def __init__(self, client: LLMClient | None = None) -> None:
        self.client = client or LLMClient()

    def analyze(self, error_output: str) -> str:
        print("[Critic] analyzing error")
        messages = [
            {
                "role": "system",
                "content": "You are a Python debugging assistant that summarises errors succinctly.",
            },
            {"role": "user", "content": error_output},
        ]
        summary = self.client.chat(messages)
        print(f"[Critic] summary: {summary}")
        return summary
