class Fixer:
    """Create new prompts for code correction based on errors."""

    def create_fix_prompt(self, error_summary: str) -> str:
        print(f"[Fixer] creating fix prompt from: {error_summary}")
        return f"Fix the code considering the error: {error_summary}"
