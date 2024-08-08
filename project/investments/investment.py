import common
from abc import ABC, abstractmethod
from typing import Tuple

class Investment(ABC):
    """TODO
    """
    
    def __init__(self, name, period, value, liability):
        self.name = name
        # variables to track investment progress
        self.inception_period = period
        self.inception_value = value
        # the following size fields make up the return tuple suggested by simulate_period
        self.period_investment_income = 0
        self.period_ltcg = 0
        self.period_expense = 0
        self.period_deduction = 0
        # these values are overall and do not reset every period
        self.total_value = value
        self.total_liability = liability
    
    def simulate_period(self, period) -> Tuple[float, float, float, float, float, float]:
        """Simulates all happenings of the investment for a single period.

        Args:

        Returns:
            Tuple[float, float, float, float, float, float]: A tuple which contains all possible
            relevant investment information for the month. In the form Tuple[period investment 
            income, period ltcg, period expenses, period deductions, total value, total liability]
        """

        self._reset_values()

        # happens every month
        if period % common.PERIODS_PER_MONTH == 0:
            self.handle_month()

        # happens every quarter
        if period % common.PERIODS_PER_QUARTER == 0:
            self.handle_quarter()

        # happens every year
        if period % common.PERIODS_PER_YEAR == 0:
            self.handle_year()

        return self.period_investment_income, self.period_ltcg, self.period_expense, self.period_deduction, self.total_value, self.total_liability
    
    @abstractmethod
    def handle_month(self) -> None:
        """Handles the operations the investment must perform every month.
        
        Does not return anything. Instead the method should modify the object fields.
        """

        pass

    @abstractmethod
    def handle_quarter(self) -> None:
        """Handles the operations the investment must perform every quarter.
        
        Does not return anything. Instead the method should modify the object fields.
        """

        pass

    @abstractmethod
    def handle_year(self) -> None:
        """Handles the operations the investment must perform every year.
        
        Does not return anything. Instead the method should modify the object fields.
        """

        pass

    def _reset_values(self) -> None:
        self.period_investment_income = 0
        self.period_ltcg = 0
        self.period_expenses = 0
        self.period_deduction = 0

    def __str__(self) -> str:
        """Displays the period return tuple as a formatted string"""

        return (f"Investment Income: {self.period_investment_income}   LTCG: {self.period_ltcg} " +
                f"  Expenses:{self.period_expense}\nValue: {self.total_value}   Liability: " +
                f"{self.total_liability}   Deduction: {self.period_deduction}\nNet Worth: " +
                f"{self.total_value - self.total_liability}   Profit: " +
                f"{self.period_investment_income + self.period_ltcg - self.period_expenses}")