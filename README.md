# AI Agent System

This project showcases a lightweight multi-agent workflow. Each agent focuses on a single responsibility and communicates via a simple `GroupChat` controller.

## Agents

- **Planner** – analyse the user request and split it into smaller tasks.
- **CodeWriter** – generate Python code for a given task.
- **Executor** – execute the generated code or shell commands.
- **Critic** – summarise any errors from the executor.
- **Fixer** – craft a new prompt for the code writer based on critic feedback.
- **OSBridge** – dispatch macOS-related tasks to `tools/macos_use_wrapper.py`.

## Configuration

Model endpoints are defined in `config/OAI_CONFIG_LIST.json`. Edit this file with your local `Ollama` or OpenAI settings before running the program.

The `workspace/` directory holds any temporary files created during execution. It will be created automatically if missing.

## Running locally

1. Install [Ollama](https://ollama.com) and pull the model:

   ```bash
   ollama pull deepseek-coder:6b
   ```

2. Install dependencies and macOS helpers:

   ```bash
   chmod +x scripts/setup_full.sh
   ./scripts/setup_full.sh
   ```

3. Start the chat:

   ```bash
   python main.py
   ```

Follow the prompts and enter a natural language request, for example "Viết app Flask và chạy thử". The agents will collaborate until the task succeeds or the retries are exhausted.
