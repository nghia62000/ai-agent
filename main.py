import os
from agents.planner import Planner
from agents.code_writer import CodeWriter
from agents.executor import Executor
from agents.critic import Critic
from agents.fixer import Fixer
from agents.os_bridge import OSBridge


class GroupChat:
    """Orchestrates agent collaboration."""

    MAX_RETRIES = 3

    def __init__(self, agents: list):
        (
            self.planner,
            self.code_writer,
            self.executor,
            self.critic,
            self.fixer,
            self.os_bridge,
        ) = agents

    def run(self, request: str) -> None:
        print(f"[Planner] analyzing request: {request}")
        tasks = self.planner.plan(request)
        if not tasks:
            print("[Planner] no tasks")
            return

        for task in tasks:
            print(f"[Planner] new task: {task}")
            self._handle_task(task)

    def _handle_task(self, task: str) -> None:
        is_os_task = any(k in task.lower() for k in ["mở", "safari", "finder", "ứng dụng"])
        last_error = ""

        for attempt in range(1, self.MAX_RETRIES + 1):
            print(f"[Task] attempt {attempt}")
            if is_os_task:
                try:
                    result = self.os_bridge.run(task)
                    print(f"[OSBridge] {result}")
                    return
                except Exception as exc:  # pragma: no cover - simple logging
                    last_error = str(exc)
                    print(f"[OSBridge] error: {last_error}")
            else:
                code = self.code_writer.write_code(task)
                success, out, err = self.executor.execute_python(code)
                if success:
                    print(f"[Executor] success output: {out}")
                    return
                print(f"[Executor] error: {err}")
                task = self.fixer.create_fix_prompt(self.critic.analyze(err))
                last_error = err

        print(f"[Task] failed after {self.MAX_RETRIES} attempts: {last_error}")


def main() -> None:
    os.makedirs("workspace", exist_ok=True)

    request = input("User request: ")
    planner = Planner()
    code_writer = CodeWriter()
    executor = Executor()
    critic = Critic()
    fixer = Fixer()
    os_bridge = OSBridge()

    chat = GroupChat([planner, code_writer, executor, critic, fixer, os_bridge])
    chat.run(request)


if __name__ == "__main__":
    main()
