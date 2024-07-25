from investment import Investment

class Stock(Investment):
    def __init__(self, name, value, appreciation, dividend, expense_ratio):
        super().__init__(name)
        self.value = value
        self.appreciation = appreciation
        self.dividend = dividend
        self.expense_ratio = expense_ratio
    
    def simulate_month(self, month):
        self.income = 0
        self.net_worth = 0

        # happens every month
        self.value *= (1 + self.appreciation / 100) ** (1 / 12)

        # happens every quarter
        if month % 3 == 0:
            self.income += self.value * (self.dividend / 100) / 4

        # happens every year
        if month % 12 == 0:
            self.value *= (1 - self.expense_ratio / 100)

        self.net_worth = self.value