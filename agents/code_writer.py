from llm_client import LLMClient


class CodeWriter:
    """Generate Python code for a task using an LLM."""

    def __init__(self, client: LLMClient | None = None) -> None:
        self.client = client or LLMClient()

    def write_code(self, task: str) -> str:
        print(f"[CodeWriter] generating code for task: {task}")
        messages = [
            {
                "role": "system",
                "content": "You write Python 3 code and nothing else.",
            },
            {"role": "user", "content": task},
        ]
        return self.client.chat(messages)
