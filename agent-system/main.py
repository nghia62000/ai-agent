"""Entry point for the multi-agent system."""

from __future__ import annotations

import json
from pathlib import Path

from agents.planner import PlannerAgent
from agents.code_writer import CodeWriterAgent
from agents.executor import ExecutorAgent
from agents.critic import CriticAgent
from agents.os_bridge import OSBridgeAgent

CONFIG_PATH = Path(__file__).parent / "config" / "OAI_CONFIG_LIST.json"


def load_config() -> list[dict[str, str]]:
    with open(CONFIG_PATH) as f:
        return json.load(f)


def main() -> None:
    config_list = load_config()

    planner = PlannerAgent(name="planner", config_list=config_list)
    coder = CodeWriterAgent(name="coder", config_list=config_list)
    executor = ExecutorAgent(name="executor", config_list=config_list)
    critic = CriticAgent(name="critic", config_list=config_list)
    os_bridge = OSBridgeAgent(name="os_bridge", config_list=config_list)

    user_request = input("Enter command: ")
    plan = planner.plan(user_request)
    print("Plan:", plan)

    if any(word in user_request.lower() for word in ["open", "launch"]):
        # naive OS command detection
        app = user_request.split()[-1]
        print(os_bridge.open_application(app))
        return

    code = coder.generate_code(plan)
    print("Generated code:\n", code)
    result = executor.run_code(code)
    print("Execution result:\n", result)

    if "error" in result.lower():
        feedback = critic.analyze(result)
        print("Critic feedback:\n", feedback)


if __name__ == "__main__":
    main()
