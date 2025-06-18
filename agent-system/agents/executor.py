"""Agent responsible for executing code or shell commands."""

import subprocess
from autogen import ConversableAgent


class ExecutorAgent(ConversableAgent):
    """Execute provided code or shell commands."""

    def __init__(self, *args, workspace: str = "workspace", **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.workspace = workspace
        self.system_message = "You execute shell commands or run Python code."

    def run_code(self, code: str) -> str:
        """Execute Python code in the workspace."""
        try:
            exec_globals: dict[str, object] = {}
            exec(code, exec_globals)
            return "Execution completed"
        except Exception as exc:  # pragma: no cover - simple wrapper
            return str(exc)

    def run_shell(self, command: str) -> str:
        """Run a shell command."""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        return output
