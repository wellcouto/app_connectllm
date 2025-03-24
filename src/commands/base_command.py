from abc import ABC, abstractmethod
"""
Define a interface para comandos, seguindo o padrão Command.
"""
class BaseCommand(ABC):
    @abstractmethod
    def execute(self):
        pass