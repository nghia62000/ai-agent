# Multi-Agent System with AutoGen

This project demonstrates a simple multi-agent workflow using Microsoft's
[AutoGen](https://github.com/microsoft/autogen). Agents collaborate to plan,
write code, execute tasks, and handle macOS GUI commands.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your API key in `config/OAI_CONFIG_LIST.json`.

## Usage
Run the system with:
```bash
python main.py
```
Enter a natural language command and the agents will attempt to fulfil it.

## Folder Structure
- `agents/` – individual agent implementations
- `tools/` – wrappers for OS-level commands (e.g. `macos-use`)
- `config/` – model configuration
- `workspace/` – scratch space for executed code
