from agents.planner import Planner
from agents.code_writer import CodeWriter
from agents.executor import Executor
from agents.critic import Critic
from agents.fixer import Fixer
from agents.os_bridge import OSBridge


class GroupChat:
    """Simple group chat simulation."""

    def __init__(self, agents: list):
        self.agents = agents

    def run(self, request: str):
        planner, code_writer, executor, critic, fixer, os_bridge = self.agents
        print(f"[Planner] analyzing request: {request}")
        tasks = planner.plan(request)
        if not tasks:
            print("[Planner] no tasks")
            return
        for task in tasks:
            print(f"[Planner] new task: {task}")
            prompt = task
            while True:
                code = code_writer.write_code(prompt)
                success, out, err = executor.execute_python(code)
                if success:
                    print(f"[Executor] success output: {out}")
                    break
                print(f"[Executor] error: {err}")
                summary = critic.analyze(err)
                prompt = fixer.create_fix_prompt(summary)


def main():
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
