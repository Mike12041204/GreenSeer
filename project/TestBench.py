import sys
from taxes import Taxes

# Test bench class should be used to test features while being implented
def main():
    income = int(sys.argv[1])
    itemized_deduction = 0
    current_salt_deduction = 0
    Taxes.calculate_earned_income_tax(income, itemized_deduction, current_salt_deduction)

if __name__ == "__main__":
    main()