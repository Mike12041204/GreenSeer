import common
from taxes import Taxes

class Investor:
    """TODO
    """
    
    def __init__(self, name):
        self.name = name
        self.cash = 0
        self.salary = 0
        self.expenses = 0

        self.yearly_earned_income = 0
        self.yearly_salt_deduction = 0
        self.yearly_taxes_witheld = 0

        # start return tuple variables
        self.yearly_investment_income = 0
        self.yearly_ltcg = 0
        self.yearly_expense = 0
        self.yearly_deduction = 0
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
            # handle investment return tuple
            investment_income, ltcg, expense, deduction, value, liability = investment.simulate_period(period)
            self.yearly_investment_income += investment_income
            self.yearly_ltcg += ltcg
            self.yearly_expense += expense
            self.yearly_deduction += deduction
            self.total_value += value
            self.total_liability += liability

            print(investment)

            # handle cash
            self.cash += investment.period_investment_income + investment.period_ltcg - investment.period_expense

        # apply yearly happenings
        if period % common.PERIODS_PER_YEAR == 0:
            # apply taxes
            taxes_owed = Taxes.calculate_tax(self.yearly_earned_income, self.yearly_deduction, self.yearly_ltcg, self.yearly_salt_deduction, self.yearly_investment_income)
            # tax return
            self.cash -= taxes_owed + self.yearly_taxes_witheld

            # reset yearly trackers
            self.reset_values()

    def reset_values(self) -> None:
        self.yearly_earned_income = 0
        self.yearly_salt_deduction = 0
        self.yearly_taxes_witheld = 0
        self.yearly_investment_income = 0
        self.yearly_ltcg = 0
        self.yearly_expense = 0
        self.yearly_deduction = 0


    def __str__(self) -> str:
        """Displays the investor as a formatted string"""

        return (f"Net Worth: {self.cash + self.total_value - self.total_liability}")        