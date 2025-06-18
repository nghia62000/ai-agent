import subprocess
import textwrap


class Executor:
    """Execute Python code or shell commands."""

    def execute_python(self, code: str) -> tuple[bool, str, str]:
        wrapped = textwrap.dedent(code)
        try:
            proc = subprocess.run(
                ['python3', '-c', wrapped],
                capture_output=True,
                text=True,
            )
            success = proc.returncode == 0
            return success, proc.stdout.strip(), proc.stderr.strip()
        except Exception as exc:
            return False, '', str(exc)

    def execute_shell(self, command: str) -> tuple[bool, str, str]:
        try:
            proc = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
            )
            success = proc.returncode == 0
            return success, proc.stdout.strip(), proc.stderr.strip()
        except Exception as exc:
            return False, '', str(exc)
