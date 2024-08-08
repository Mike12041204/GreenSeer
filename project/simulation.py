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
            common.println1()
            print(f"Investor: {self.investor.name}   Period: {self.period}")
            if skip == 0:
                common.println2()
                print("Menu:")
                print("0: End Simulation")
                print("1: Finish Period")
                print("2: Add Investment")
                print("3: Manage Investment")
                print("4: Modify Investor")
                print("5: Simulate Periods")
                common.println3()

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
                    self.modify_investor()
                elif selection == 5:
                    periods = int(input("How many periods to simulate: "))
                    while periods < 1:
                        periods = int(input("How many periods to simulate: "))
                    skip = periods

            if skip > 0:
                skip -= 1   

            common.println2()
            self.simulate_period()
            print(f"Net Worth: " + str(self.investor.cash + self.investor.total_value - 
                                       self.investor.total_liability))
            common.println1()
            print()
            print()
            print()
    
    def simulate_period(self) -> None:
        self.investor.simulate_period(self.period)

        self.period += 1
    
    # only pertaining to non-owned assets 
    def add_investment(self) -> None:
        common.println3()
        print("Menu:")
        print("0: End Selection")
        print("1: Add Stock")
        common.println3()

        while True:
            selection = int(input("Make a Selection: "))
            while selection < 0 or selection > 1:
                selection = int(input("Make a Selection: "))
            
            if selection == 0:
                break
            elif selection == 1:
                self.add_stock()

        common.println3()
 
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
    def modify_investor(self) -> None:
        pass