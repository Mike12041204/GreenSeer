from abc import ABC, abstractmethod

class Investment(ABC):
    def __init__(self, name):
        self.name = name
        self.income = 0
        self.net_worth = 0
    
    @abstractmethod
    def simulate_month(self, month):
        pass