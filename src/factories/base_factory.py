from abc import ABC, abstractmethod
"""
Define a interface para fábricas que criam serviços de LLM.
"""

class BaseFactory(ABC):
    @abstractmethod
    def create_llm_service(self):
        pass
        """
        Retorna um objeto de serviço LLM capaz de receber perguntas 
        e retornar respostas.
        """
            