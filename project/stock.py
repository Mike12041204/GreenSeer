from investment import Investment

# TODO - handling selling long term and short term capital gains
class Stock(Investment):
    def __init__(self, name, value, appreciation, dividend, expense_ratio):
        super().__init__(name)
        self.value = value
        self.appreciation = appreciation
        self.dividend = dividend
        self.expense_ratio = expense_ratio
        self.purchase_price = value
        self.realized_gains = 0
    
    def simulate_month(self, month):
        self.investment_income = 0
        self.net_worth = 0

        # happens every month
        self.value *= (1 + self.appreciation / 100) ** (1 / 12)

        # happens every quarter
        if month % 3 == 0:
            self.investment_income += self.value * (self.dividend / 100) / 4
            self.realized_gains += self.investment_income

        # happens every year
        if month % 12 == 0:
            self.value *= (1 - self.expense_ratio / 100)

        self.net_worth = self.value

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}   Value: {self.fc(self.value)}   Unrealized Gains: {self.fc(self.value - self.purchase_price)}   Realized Gains: {self.fc(self.realized_gains)}"