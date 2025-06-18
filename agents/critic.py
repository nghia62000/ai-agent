class Critic:
    """Summarize and analyze execution errors."""

    def analyze(self, error_output: str) -> str:
        print("[Critic] analyzing error")
        lines = [line.strip() for line in error_output.splitlines() if line.strip()]
        summary = lines[-1] if lines else "Unknown error"
        print(f"[Critic] summary: {summary}")
        return summary
