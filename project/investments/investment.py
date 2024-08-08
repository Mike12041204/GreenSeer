import common
from abc import ABC, abstractmethod

class Investment(ABC):
    def __init__(self, name):
        self.name = name
        self.investment_income = 0
        self.capital_gains = 0
        self.net_worth = 0
    
    @abstractmethod
    def simulate_month(self, month):
        pass

    @abstractmethod
    def __str__(self, month):
        pass

    def fc(self, amount):
        return f"${amount:,.2f}"