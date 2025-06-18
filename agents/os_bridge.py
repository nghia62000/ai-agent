from tools import macos_use_wrapper as mac


class OSBridge:
    """Bridge agent to forward OS actions to wrapper."""

    def open_app(self, app_name: str) -> None:
        mac.open_app(app_name)

    def write_text(self, text: str) -> None:
        mac.write_text(text)

    def click_button(self, label: str) -> None:
        mac.click_button(label)
