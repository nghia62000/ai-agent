class Planner:
    """Analyze user request and break into tasks."""

    def plan(self, request: str) -> list[str]:
        request = request.strip()
        if not request:
            return []
        # simple split by 'and' for demonstration
        parts = [p.strip() for p in request.split(' and ') if p.strip()]
        return parts or [request]
