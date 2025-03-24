from .base_strategy import BaseStrategy

class ReferenceCheckStrategy(BaseStrategy):

    def __init__(self, reference_facts: dict):
       
        self.reference_facts = reference_facts

    def evaluate(self, responses: list):
        if not responses:
            return None

        best_text = None
        best_score = float("-inf")

        for resp in responses:
            text = resp["text"]
            score = 0.0

            for key, desc in self.reference_facts.items():
                if key.lower() in text.lower():
                    score += 1.0  

            resp["reference_score"] = score

            if score > best_score:
                best_score = score
                best_text = text

        return best_text
