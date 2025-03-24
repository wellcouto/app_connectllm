from .base_factory import BaseFactory
from services.chatgpt_service import ChatGPTService

class ChatGPTFactory(BaseFactory):
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def create_llm_service(self):
        return ChatGPTService(api_key=self.api_key)
    
        """
        Cria e retorna um ChatGPTService configurado com a API key fornecida.
        """
