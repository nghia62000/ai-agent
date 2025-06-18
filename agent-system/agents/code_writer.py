"""Agent that writes code based on planner instructions."""

from autogen import ConversableAgent


class CodeWriterAgent(ConversableAgent):
    """Generate code to accomplish a step."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.system_message = (
            "You are a helpful coding assistant. Return Python code snippets when requested."
        )

    def generate_code(self, instruction: str) -> str:
        messages = self.chat(messages=[{"role": "user", "content": instruction}])
        return messages[-1]["content"]
