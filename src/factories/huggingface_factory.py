from .base_factory import BaseFactory
from services.huggingface_service import HuggingFaceService

class HuggingFaceFactory(BaseFactory):
    def __init__(self, model_name: str = "deepset/roberta-base-squad2"):
        self.model_name = model_name
    
    def create_llm_service(self):
        return HuggingFaceService(model_name=self.model_name)
        
        """
        Cria e retorna um HuggingFaceService configurado com o 'model_name' fornecido.
        """
