codex/refactor-multi-agent-system-and-optimize-roles
# AI Agent System

This project demonstrates a minimal multi-agent setup built with Python. The
agents collaborate to analyse a user request, generate code, run it and react to
errors until the execution succeeds.

## Agents

- **Planner** (`planner.py`) – analyses the user request and splits it into
  smaller tasks.
- **CodeWriter** (`code_writer.py`) – only generates source code from a task
  description.
- **Executor** (`executor.py`) – runs Python code or shell commands and returns
  the output.
- **Critic** (`critic.py`) – summarises any error from the executor.
- **Fixer** (`fixer.py`) – creates a new prompt for the CodeWriter based on the
  critic summary.
- **OSBridge** (`os_bridge.py`) – forwards macOS related commands to
  `tools/macos_use_wrapper.py`.

## Running locally

1. Install [Ollama](https://ollama.com) and pull the DeepSeek model:
   ```bash
   ollama pull deepseek-coder:6b
   ```
2. Adjust `OAI_CONFIG_LIST.json` with your local model configuration. See the
   example below:
   ```json
   [
     {
       "model": "http://localhost:11434/v1/chat/completions",
       "api_type": "openai"
     }
   ]
   ```
3. Run the program:
   ```bash
   python main.py
   ```
4. Enter a request such as `Viết app Flask và chạy thử` and observe the agents
   interacting.

## File `macos_use_wrapper.py`

This helper exposes three functions used by `OSBridge`:

- `open_app(app_name)` – open the given application.
- `write_text(text)` – type text in the active window.
- `click_button(label)` – click a button with the specified label.

They are simple placeholders and can be adapted to real automation tools.
=======
# ai-agent

This repository demonstrates a simple multi-agent system.

## 🛠 Cài đặt macOS-use và khởi động hệ thống

```bash
chmod +x scripts/setup_full.sh
./scripts/setup_full.sh
```
 main
