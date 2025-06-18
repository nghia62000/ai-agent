from tools import macos_use_wrapper as mac


class OSBridge:
    """Bridge agent to forward OS actions to wrapper."""

    def open_app(self, app_name: str) -> str:
        return mac.open_app(app_name)

    def write_text(self, text: str) -> str:
        return mac.write_text(text)

    def click_button(self, label: str) -> str:
        return mac.click_button(label)

    def run(self, task: str) -> str:
        """Handle a generic OS-related task."""
        lower = task.lower()
        if "safari" in lower:
            return self.open_app("Safari")
        if "finder" in lower:
            return self.open_app("Finder")
        if any(k in lower for k in ["open", "mở", "ứng dụng"]):
            app = task.split()[-1]
            return self.open_app(app)
        raise ValueError(f"Unrecognized OS task: {task}")
