from .base_strategy import BaseStrategy

class RelevanceStrategy(BaseStrategy):
    
    def evaluate(self, responses: list):
        best_response = max(responses, key=lambda r: r["relevance_score"])
        return best_response["text"]
