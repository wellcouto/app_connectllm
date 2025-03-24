from .base_strategy import BaseStrategy

class RelevanceStrategy(BaseStrategy):
    
    def evaluate(self, responses: list):
        if not responses:
            return None

        best_response = max(responses, key=lambda r: r.get("relevance_score", 0))
        return best_response.get("text", "")
