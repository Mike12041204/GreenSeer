from stock import Stock
from investor import Investor
from parameter import Parameter
import locale

class Simulation:
    def __init__(self):
        self.parameter = Parameter()
        self.month = 1
        name = input("Enter Investor Name: ")
        self.investor = Investor(name)
        print()

    def simulate(self):
        print("Info:")
        print("Enter all numbers as percentages.")
        print("Consider all parameters as they apply yearly.")
        print()

        running = True
        skip = 0

        while running:
            print("-------------------------------------------")
            print(f"Investor: {self.investor.name}   Month: {self.month}")
            if skip == 0:
                print("-------------------------------------------")
                print("Menu:")
                print("0: End Simulation")
                print("1: Finish Month")
                print("2: Add Investment")
                print("3: Manage Investment")
                print("4: Change Salary and Expenses")
                print("5: Simulate Year")
                print("-------------------------------------------")

            while skip == 0:
                selection = -1
                while selection < 0 or selection > 5:
                    selection = int(input("Make a Selection: "))
                
                if selection == 0:
                    running = False
                    break
                elif selection == 1:
                    break
                elif selection == 2:
                    self.add_investment()
                elif selection == 3:
                    self.manage_investment()   
                elif selection == 4:
                    self.change_salary()
                elif selection == 5:
                    skip = 12

            if skip > 0:
                skip -= 1   

            print("-------------------------------------------")
            self.simulate_month()
            print(f"Net Worth: {self.fc(self.investor.net_worth)}   Month Income: {self.fc(self.investor.month_profit)}")
            print("-------------------------------------------")
            print()
            print()
            print()
    
    def simulate_month(self):
        # reset monthly values
        self.investor.net_worth = 0
        self.investor.month_profit = 0

        # simulate and track income and expenses for the month
        witheld_taxes = 0
        month_income = self.investor.salary / 12
        # apply Social Security tax
        if self.investor.job_income < self.parameter.social_limit:
            witheld_taxes += month_income * (self.parameter.social_security / 100)

        # add month income to total to overestimate taxes witheld
        self.investor.job_income += month_income
        
        # apply Medicare tax
        if self.investor.job_income < self.parameter.medicare_threshold:
            witheld_taxes += month_income * (self.parameter.medicare / 100)
        else:
            witheld_taxes += month_income * ((self.parameter.medicare + self.parameter.medicare_additional) / 100)

        self.investor.cash += month_income - witheld_taxes
        self.investor.taxes_paid += witheld_taxes

        # simulate and track investments for the month
        for investment in self.investor.investments:
            investment.simulate_month(self.month)
            print(f"{investment}")

            # keep track of changed income and net worth
            self.investor.month_profit += investment.investment_income
            self.investor.investment_income += investment.investment_income
            self.investor.cash += investment.investment_income
            self.investor.net_worth += investment.net_worth

        # every year
        if self.month % 12 == 0:
            # calculate taxes
            taxes = self.calculate_taxes()
            # pay or recieve difference in taxes witheld from income
            tax_difference = taxes - self.investor.taxes_paid
            self.investor.cash -= tax_difference

            total_income = self.investor.investment_income + self.investor.capital_gains + self.investor.job_income
            print(f"Taxes: {self.fc(taxes)}   Effective Rate: {self.fp(taxes / total_income)}")

            # reset incomes
            self.investor.investment_income = 0
            self.investor.capital_gains = 0
            self.investor.job_income = 0
            self.investor.retirement_income = 0
            self.investor.taxes_paid = 0

        self.investor.net_worth += self.investor.cash

        self.month += 1

    def calculate_taxes(self):
        return 0
    
        # fica_taxes = 0

        # # handle FICA
        # fica_taxes += self.investor.yearly_income * (self.parameter.fica / 100)

        # # handle State
        # state_taxes = 0
        # state_income = (self.investor.yearly_income - self.parameter.state_deduction) 
        
        # if state_income > self.parameter.mun6:
        #     state_taxes += (state_income - self.parameter.mun6) * (self.parameter.mun7r / 100)
        #     state_income = self.parameter.mun6
        # if state_income > self.parameter.mun5:
        #     state_taxes += (state_income - self.parameter.mun5) * (self.parameter.mun6r / 100)
        #     state_income = self.parameter.mun5
        # if state_income > self.parameter.mun4:
        #     state_taxes += (state_income - self.parameter.mun4) * (self.parameter.mun5r / 100)
        #     state_income = self.parameter.mun4
        # if state_income > self.parameter.mun3:
        #     state_taxes += (state_income - self.parameter.mun3) * (self.parameter.mun4r / 100)
        #     state_income = self.parameter.mun3
        # if state_income > self.parameter.mun2:
        #     state_taxes += (state_income - self.parameter.mun2) * (self.parameter.mun3r / 100)
        #     state_income = self.parameter.mun2
        # if state_income > self.parameter.mun1:
        #     state_taxes += (state_income - self.parameter.mun1) * (self.parameter.mun2r / 100)
        #     state_income = self.parameter.mun1
        # if state_income > 0:
        #     state_taxes += state_income * (self.parameter.mun1r / 100)

        # # handle Federal
        # federal_taxes = 0
        # deduction = max(self.parameter.standard_deduction, self.investor.itemized_deduction)
        # federal_income = (self.investor.yearly_income - deduction - state_taxes)

        # if federal_income > self.parameter.fed6:
        #     federal_taxes += (federal_income - self.parameter.fed6) * (self.parameter.fed7r / 100)
        #     federal_income = self.parameter.fed6
        # if federal_income > self.parameter.fed5:
        #     federal_taxes += (federal_income - self.parameter.fed5) * (self.parameter.fed6r / 100)
        #     federal_income = self.parameter.fed5
        # if federal_income > self.parameter.fed4:
        #     federal_taxes += (federal_income - self.parameter.fed4) * (self.parameter.fed5r / 100)
        #     federal_income = self.parameter.fed4
        # if federal_income > self.parameter.fed3:
        #     federal_taxes += (federal_income - self.parameter.fed3) * (self.parameter.fed4r / 100)
        #     federal_income = self.parameter.fed3
        # if federal_income > self.parameter.fed2:
        #     federal_taxes += (federal_income - self.parameter.fed2) * (self.parameter.fed3r / 100)
        #     federal_income = self.parameter.fed2
        # if federal_income > self.parameter.fed1:
        #     federal_taxes += (federal_income - self.parameter.fed1) * (self.parameter.fed2r / 100)
        #     federal_income = self.parameter.fed1
        # if federal_income > 0:
        #     federal_taxes += federal_income * (self.parameter.fed1r / 100)

        # return fica_taxes + state_taxes + federal_taxes

    def add_investment(self):
        print("-------------------------------------------")
        print("Menu:")
        print("0: End Selection")
        print("1: Add Stock")
        print("-------------------------------------------")

        while True:
            selection = -1
            while selection < 0 or selection > 1:
                selection = int(input("Make a Selection: "))
            
            if selection == 0:
                running = False
                break
            elif selection == 1:
                self.add_stock()

        print("-------------------------------------------")


    def add_stock(self):
        name = input("Enter the Name: ")
        while name in self.investor.investment_names:
            name = input("Enter a Name: ")
        self.investor.investment_names.add(name)
        
        value = float(input("Enter the Value: "))
        while value <= 0:
            value = float(input("Enter a Value: "))
        
        appreciation = float(input("Enter the Appreciation: "))
        while appreciation < -100:
            appreciation = float(input("Enter a Appreciation: "))
        
        dividend = float(input("Enter the Dividend: "))
        while dividend < 0 or dividend > 100:
            dividend = float(input("Enter a Dividend: "))
        
        expense_ratio = float(input("Enter the Expense Ratio: "))
        while expense_ratio < 0 or expense_ratio > 100:
            expense_ratio = float(input("Enter a Expense Ratio: "))

        stock = Stock(name, value, appreciation, dividend, expense_ratio)

        self.investor.investments.append(stock)


    # TODO - implement
    def manage_investment(self):
        pass

    # TODO - implement
    def change_salary(self):
        pass

    def fc(self, number):
        return f"${number:,.2f}"
    
    def fp(self,number):
        return f"{number * 100:.2f}%"