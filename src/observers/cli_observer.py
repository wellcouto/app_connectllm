from .base_observer import BaseObserver
"""
Observer que notifica via Linha de Comando (CLI) a resposta escolhida.
"""
class CLIObserver(BaseObserver):
    def update(self, chosen_response: str):
        print("\n[Observer] Resposta escolhida:")
        print(chosen_response)
