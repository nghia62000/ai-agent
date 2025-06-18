"""Wrapper for macos-use commands."""

import subprocess


def open_app(app_name: str) -> None:
    """Open a macOS application using macos-use command."""
    subprocess.run(["macos-use", "open", app_name], check=False)


def run_applescript(script: str) -> None:
    """Run an AppleScript via macos-use."""
    subprocess.run(["macos-use", "osascript", script], check=False)

