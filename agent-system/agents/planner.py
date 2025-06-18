"""Planner agent using autogen to break down user requests."""

from autogen import ConversableAgent


class PlannerAgent(ConversableAgent):
    """Agent that plans tasks from a user request."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.system_message = (
            "You are a planner. Break the user's request into small executable steps."
        )

    def plan(self, user_request: str) -> str:
        """Return a plan for the request."""
        messages = self.chat(messages=[{"role": "user", "content": user_request}])
        return messages[-1]["content"]
