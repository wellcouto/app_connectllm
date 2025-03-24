from .base_strategy import BaseStrategy

class SimilarityStrategy(BaseStrategy):
   
    def evaluate(self, responses: list):
        best_response = max(responses, key=lambda r: r["similarity_score"])
        return best_response["text"]
