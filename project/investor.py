class Investor:
    def __init__(self, name):
        self.name = name
        self.cash = 0
        self.net_worth = 0
        self.monthly_income = 0
        self.yearly_income = 0
        self.investments = []
        self.investment_names = set()