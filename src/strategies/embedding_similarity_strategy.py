# src/strategies/embedding_similarity_strategy.py
from .base_strategy import BaseStrategy
from sentence_transformers import SentenceTransformer, util
"""
Strategy que calcula similaridade semântica usando embeddings e coseno
via SentenceTransformers, para escolher a melhor resposta.
"""
class EmbeddingSimilarityStrategy(BaseStrategy):
    
    def __init__(self, user_question: str, model_name="all-MiniLM-L6-v2"):
        self.user_question = user_question
        self.model = SentenceTransformer(model_name)

    def evaluate(self, responses: list):
       
        if not responses:
            return None

        # Gera embedding para a pergunta
        question_embedding = self.model.encode(self.user_question, convert_to_tensor=True)
        
        best = None
        best_score = float("-inf")

        # Para cada resposta, calcula embedding e similaridade
        for resp in responses:
            text = resp["text"]
            resp_emb = self.embedder.encode(text, convert_to_tensor=True)
            similarity = util.cos_sim(question_embedding, resp_emb).item()

            resp["similarity_score"] = similarity  # registra o score

            if similarity > best_score:
                best_score = similarity
                best= text

        return best
