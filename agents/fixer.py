from llm_client import LLMClient


class Fixer:
    """Craft follow-up prompts for the code writer using an LLM."""

    def __init__(self, client: LLMClient | None = None) -> None:
        self.client = client or LLMClient()

    def create_fix_prompt(self, error_summary: str) -> str:
        print(f"[Fixer] creating fix prompt from: {error_summary}")
        messages = [
            {
                "role": "system",
                "content": "You help improve instructions for code generation.",
            },
            {
                "role": "user",
                "content": f"Given the following error summary, provide updated instructions:\n{error_summary}",
            },
        ]
        return self.client.chat(messages)
