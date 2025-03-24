import openai

class ChatGPTService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def ask(self, question: str) -> dict:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # ou outra versão
            messages=[{"role": "user", "content": question}],
            temperature=0.5,
        )
        # Você pode retornar algo mais estruturado para facilitar a avaliação
        return {
            "text": response.choices[0].message["content"],
            "similarity_score": 0,  # placeholder
            "relevance_score": 0    # placeholder
        }
