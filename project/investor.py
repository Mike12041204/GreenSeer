import common

class Investor:
    """TODO
    """
    
    def __init__(self, name):
        self.name = name
        self.cash = 0
        self.salary = 0
        self.expenses = 0

        self.period_investment_income = 0
        self.period_ltcg = 0
        self.period_expense = 0
        self.period_deduction = 0
        # these values are overall and do not reset every period
        self.total_value = 0
        self.total_liability = 0

        self.investments = []
        self.investment_names = set()

    def simulate_period(self, period) -> None:
        # reset values that do not reset in each investment
        self.total_value = 0
        self.total_liability = 0

        # TODO - account for periods per year for realized salary, also handle witholding
        # simulate investor earned and spent
        #self.cash += self.salary - self.expenses

        # simulate period for every investment
        for investment in self.investments:
            self.period_investment_income, self.period_ltcg, self.period_expense, self.period_deduction, self.total_value, self.total_liability += investment.simulate_period(period)
            self.cash += investment.period_investment_income + investment.period_ltcg - investment.period_expense

        