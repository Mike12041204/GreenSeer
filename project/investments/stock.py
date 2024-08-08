import common
from investment import Investment

class Stock(Investment):
    """TODO
    """

    def __init__(self, name, period, value, appreciation, dividend, expense_ratio):
        super().__init__(name, period, value)
        self.appreciation = appreciation
        self.dividend = dividend
        self.expense_ratio = expense_ratio

    def handle_month(self) -> None:
        # add appreciation to stocks value
        self.total_value *= (1 + self.appreciation / 100) ** (1 / 12)

    def handle_quarter(self) -> None:
        # stock pays out dividend giving investment income with an equivalent drop in value
        self.period_investment_income += self.total_value * (self.dividend / 100) / 4

    def handle_year(self) -> None:
        # stock pays expense ratio based on value at the end of the year
        self.total_value *= (1 - self.expense_ratio / 100)