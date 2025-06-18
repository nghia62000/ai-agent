"""Wrapper functions for macOS-use commands."""

from __future__ import annotations

import subprocess
import logging


def _run(args: list[str]) -> str:
    try:
        completed = subprocess.run(
            args,
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()
    except subprocess.CalledProcessError as exc:  # pragma: no cover - thin wrapper
        logging.error(exc.stderr.strip())
        return exc.stderr.strip()


def open_app(app_name: str) -> str:
    return _run(["macos-use", "open", app_name])


def write_text(text: str) -> str:
    return _run(["macos-use", "write", text])


def click_button(label: str) -> str:
    return _run(["macos-use", "click", label])


def run_applescript(script: str) -> str:
    return _run(["macos-use", "osascript", script])
