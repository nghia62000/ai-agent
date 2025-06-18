import json
from typing import List, Dict

import openai


class LLMClient:
    """Wrapper around OpenAI chat models loaded from config."""

    def __init__(self, config_path: str = "config/OAI_CONFIG_LIST.json") -> None:
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)[0]
        self.model = cfg.get("model", "gpt-3.5-turbo")
        openai.api_key = cfg.get("api_key")
        if base := cfg.get("api_base"):
            openai.api_base = base

    def chat(self, messages: List[Dict[str, str]]) -> str:
        response = openai.ChatCompletion.create(model=self.model, messages=messages)
        return response.choices[0].message["content"].strip()
