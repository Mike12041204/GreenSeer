class Investor:
    def __init__(self, name):
        self.name = name
        self.cash = 0.0
        self.net_worth = 0.0
        self.salary = 0.0
        self.expenses = 0.0

        self.investments = []
        self.investment_names = set()

        self.month_profit = 0.0
        self.job_income = 0.0
        self.taxes_paid = 0.0
        self.investment_income = 0.0
        self.capital_gains = 0.0
        self.retirement_income = 0.0

        self.itemized_deduction = 0.0