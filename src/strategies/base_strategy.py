from abc import ABC, abstractmethod
"""
Define a interface para estratégias de avaliação das respostas dos modelos.
"""
class BaseStrategy(ABC):
    @abstractmethod
    def evaluate(self, responses: list):
        pass
