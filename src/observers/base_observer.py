from abc import ABC, abstractmethod
"""
Define a interface para Observers que reagem a mudanças de estado 
(Ex.: quando uma nova resposta é escolhida).
"""
class BaseObserver(ABC):
    @abstractmethod
    def update(self, chosen_response: str):
        pass
