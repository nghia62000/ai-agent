"""Agent that criticizes execution errors and suggests fixes."""

from autogen import ConversableAgent


class CriticAgent(ConversableAgent):
    """Critique errors and produce analysis."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.system_message = (
            "You are a code critic. Analyze failures and suggest fixes succinctly."
        )

    def analyze(self, error: str) -> str:
        messages = self.chat(messages=[{"role": "user", "content": error}])
        return messages[-1]["content"]
