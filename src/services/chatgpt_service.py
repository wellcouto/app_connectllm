import openai

class ChatGPTService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def ask(self, question: str, context: str = "") -> dict:
        try:
            prompt_content = f"Contexto: {context}\nPergunta: {question}"
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # ou outra versão
                messages=[{"role": "user", "content": question}],
                temperature=0.5,
            )
        
            answer_text = response.choices[0].message["content"]
        except openai.error.OpenAIError as e:
            # Tratamento de exceções na chamada da API
            answer_text = f"Erro ao consultar ChatGPT: {str(e)}"
        # Você pode retornar algo mais estruturado para facilitar a avaliação
        return {
            "text": response.choices[0].message["content"],
            "similarity_score": 0,  # placeholder
            "relevance_score": 0    # placeholder
        }
