"""Bridge agent for executing macOS GUI commands."""

from autogen import ConversableAgent
from ..tools import macos_use_wrapper


class OSBridgeAgent(ConversableAgent):
    """Agent that runs OS operations."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.system_message = "You operate macOS via provided functions."

    def open_application(self, name: str) -> str:
        macos_use_wrapper.open_app(name)
        return f"Requested to open {name}"

    def run_script(self, script: str) -> str:
        macos_use_wrapper.run_applescript(script)
        return "AppleScript executed"
