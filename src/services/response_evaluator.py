from observers.base_observer import BaseObserver
from strategies.base_strategy import BaseStrategy

class ResponseEvaluator:
    def __init__(self, strategy: BaseStrategy):
        self.strategy = strategy
        self.observers = []

    def attach(self, observer: BaseObserver):
        self.observers.append(observer)

    def detach(self, observer: BaseObserver):
        self.observers.remove(observer)

    def notify(self, chosen_response: str):
        for obs in self.observers:
            obs.update(chosen_response)

    def evaluate_and_notify(self, responses: list):
        best = self.strategy.evaluate(responses)
        self.notify(best)
        return best