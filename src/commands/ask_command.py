from .base_command import BaseCommand
from factories.base_factory import BaseFactory
"""
Comando concreto que encapsula a ação de "fazer uma pergunta" a um LLM.
"""
class AskCommand(BaseCommand):
    def __init__(self, factory: BaseFactory, question: str, context: str = ""):
        self.factory = factory
        self.question = question
        self.context = context
    
    def execute(self):
        llm_service = self.factory.create_llm_service()
        response = llm_service.ask(self.question, self.context)
        return response
