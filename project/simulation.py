import common
from investments.stock import Stock
from investor import Investor

class Simulation:
    """Simulation class is repsonsible for handling input and triggering events.
    
    The class also keeps track of the enviroment. The class should not perform complex arithmetic.
    """
    
    def __init__(self):
        self.period = 1
        name = input("Enter Investor Name: ")
        self.investor = Investor(name)
        print()

    def simulate(self) -> None:
        print("Info:")
        print("Enter all numbers as percentages.")
        print("Consider all parameters as they apply yearly.")
        print()

        running = True
        skip = 0

        while running:
            print("-------------------------------------------")
            print(f"Investor: {self.investor.name}   Period: {self.period}")
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
                selection = int(input("Make a Selection: "))
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
            self.simulate_period()
            print(self.investor)
            print("-------------------------------------------")
            print()
            print()
            print()
    
    def simulate_period(self) -> None:
        self.investor.simulate_period(self.period)

        self.period += 1
    
    # only pertaining to non-owned assets 
    def add_investment(self) -> None:
        print("-------------------------------------------")
        print("Menu:")
        print("0: End Selection")
        print("1: Add Stock")
        print("-------------------------------------------")

        while True:
            selection = int(input("Make a Selection: "))
            while selection < 0 or selection > 1:
                selection = int(input("Make a Selection: "))
            
            if selection == 0:
                running = False
                break
            elif selection == 1:
                self.add_stock()

        print("-------------------------------------------")

 
    def add_stock(self) -> None:
        name = input("Enter the Name: ")
        while name in self.investor.investment_names:
            name = input("Enter the Name: ")
        self.investor.investment_names.add(name)
        
        value = float(input("Enter the Value: "))
        while value <= 0:
            value = float(input("Enter the Value: "))
        
        appreciation = float(input("Enter the Appreciation: "))
        while appreciation < -100:
            appreciation = float(input("Enter the Appreciation: "))
        
        dividend = float(input("Enter the Dividend: "))
        while dividend < 0 or dividend > 100:
            dividend = float(input("Enter the Dividend: "))
        
        expense_ratio = float(input("Enter the Expense Ratio: "))
        while expense_ratio < 0 or expense_ratio > 100:
            expense_ratio = float(input("Enter the Expense Ratio: "))

        stock = Stock(name, self.period, value, 0, appreciation, dividend, expense_ratio)

        self.investor.investments.append(stock)


    # TODO - implement
    # involves selling, refinancing, or other actions pertaining to owned assets
    def manage_investment(self) -> None:
        pass

    # TODO - implement
    def change_salary(self) -> None:
        pass