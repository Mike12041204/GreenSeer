from stock import Stock
from investor import Investor

class Simulation:
    def __init__(self):
        self.month = 1
        name = input("Enter Investor Name: ")
        self.investor = Investor(name)
        print()

    def simulate(self):
        print("Info:")
        print("Enter all numbers as percentages.")
        print()

        running = True

        while running:
            print("-------------------------------------------")
            print(f"Investor: {self.investor.name}   Month: {self.month}")
            print("-------------------------------------------")
            print("Menu:")
            print("0: End Simulation")
            print("1: Finish Month")
            print("2: Add Investment")
            print("3: Manage Investment")
            print("-------------------------------------------")

            while True:
                selection = -1
                while selection < 0 or selection > 3:
                    selection = int(input("Make a Selection: "))
                
                if selection == 0:
                    running = False
                    break
                elif selection == 1:
                    self.simulate_month()
                    break
                elif selection == 2:
                    self.add_investment()
                elif selection == 3:
                    self.manage_investment()       

            print("-------------------------------------------")
            print(f"Net Worth: {self.investor.net_worth}   Month Income: {self.investor.monthly_income}")
            print("-------------------------------------------")
            print()
            print()
            print()
    
    def simulate_month(self):
        self.investor.net_worth = 0
        self.investor.monthly_income = 0

        # every month
        for investment in self.investor.investments:
            investment.simulate_month(self.month)
            self.investor.monthly_income += investment.income
            self.investor.cash += investment.income
            self.investor.net_worth += investment.net_worth

        self.investor.yearly_income += self.investor.monthly_income

        # every year
        if self.month % 12 == 0:
            self.investor.yearly_income = 0
            # TODO - pay taxes

        self.investor.net_worth += self.investor.cash

        self.month += 1

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


    def manage_investment(self):
        print()