
# AI Agent System

This project demonstrates a minimal multi-agent setup built with Python. The
agents collaborate to analyse a user request, generate code, run it and react to
errors until the execution succeeds.

## Agents

- **Planner** (`planner.py`) – Analyses the user request and splits it into
  smaller tasks.
- **CodeWriter** (`code_writer.py`) – Generates source code from a task
  description.
- **Executor** (`executor.py`) – Runs Python code or shell commands and returns
  the output.
- **Critic** (`critic.py`) – Summarises any error from the executor.
- **Fixer** (`fixer.py`) – Creates a new prompt for the CodeWriter based on the
  critic summary.
- **OSBridge** (`os_bridge.py`) – Forwards macOS-related commands to
  `tools/macos_use_wrapper.py`.

## Running locally

1. Install [Ollama](https://ollama.com) and pull the DeepSeek model:

   ```bash
   ollama pull deepseek-coder:6b

2. Adjust `config/OAI_CONFIG_LIST.json` with your local model configuration:

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

4. Enter a request such as:

   ```
   Viết app Flask và chạy thử
   ```

   and observe the agents interacting.

---

## 🛠 Cài đặt macOS-use và khởi động hệ thống

To allow the agents to interact with your macOS system (e.g., open Safari, type text), install the [`macOS-use`](https://github.com/browser-use/macOS-use) tool:

```bash
chmod +x scripts/setup_full.sh
./scripts/setup_full.sh
```

---

## File `macos_use_wrapper.py`

This helper exposes three functions used by `OSBridge`:

* `open_app(app_name)` – Open the given application.
* `write_text(text)` – Type text in the active window.
* `click_button(label)` – Click a button with the specified label.

These are simple wrappers around `macos-use` commands and can be extended.

````

---

## ✅ Hành động tiếp theo:

1. Ghi đè nội dung này vào `README.md`.
2. Commit:

```bash
git add README.md
git commit -m "Fix README formatting and finalize agent system docs"
git push origin main
````

