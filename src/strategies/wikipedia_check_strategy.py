# src/strategies/wikipedia_check_strategy.py
from .base_strategy import BaseStrategy
import wikipedia
from sentence_transformers import SentenceTransformer, util

class WikipediaCheckStrategy(BaseStrategy):
    """
    Faz busca na Wikipedia com base na pergunta do usuário e compara
    (via similaridade de embeddings) a resposta do modelo com o sumário retornado.
    """

    def __init__(self, user_question: str, embed_model: str = "all-MiniLM-L6-v2"):
        """
        :param user_question: Pergunta do usuário, usada como consulta ao Wikipedia.
        :param embed_model: Modelo de embeddings do Sentence Transformers.
        """
        self.user_question = user_question
        self.embedder = SentenceTransformer(embed_model)

        # Configuração básica da biblioteca wikipedia
        # Ex.: definir o idioma 'pt' para português:
        # wikipedia.set_lang("pt")

    def evaluate(self, responses: list):
        """
        Recebe uma lista de respostas, ex:
            [
              {"text": "Resposta gerada pelo LLM", "similarity_score": 0},
              ...
            ]
        Retorna o texto da melhor resposta, isto é, a que tem
        maior similaridade com o sumário da Wikipedia (ou 0 se nenhuma página for encontrada).
        """

        if not responses:
            return None

        best_response_text = None
        best_score = float("-inf")

        try:
            # 1) Faz uma busca no Wikipedia com base na pergunta do usuário
            search_results = wikipedia.search(self.user_question, results=1)  # Pega só o melhor match
            if not search_results:
                print("[WikipediaCheck] Nenhum resultado encontrado para a pergunta.")
                return responses[0]["text"]  # Retorna a 1ª resposta por default

            best_title = search_results[0]
            # 2) Tenta obter sumário dessa página
            wiki_summary = wikipedia.summary(best_title, sentences=3)  # Pegamos 3 frases

            # 3) Gera embeddings do sumário
            summary_emb = self.embedder.encode(wiki_summary, convert_to_tensor=True)

            # 4) Compara cada resposta com o sumário
            for resp in responses:
                resp_text = resp["text"]
                resp_emb = self.embedder.encode(resp_text, convert_to_tensor=True)
                similarity = util.cos_sim(summary_emb, resp_emb).item()

                # Armazena num campo "wikipedia_score"
                resp["wikipedia_score"] = similarity

                if similarity > best_score:
                    best_score = similarity
                    best_response_text = resp_text

        except Exception as e:
            print(f"[WikipediaCheck] Ocorreu um erro ao buscar no Wikipedia: {e}")
            # Se der erro (por exemplo, ausência de internet), retorna a primeira por default
            best_response_text = responses[0]["text"]

        return best_response_text
