import sys
from taxes import Taxes

# Test bench class should be used to test features while being implented
def main():
    earned_income = int(sys.argv[1])
    long_term_capital_gains = int(sys.argv[2])
    itemized_deduction = 0
    current_salt_deduction = 0
    fltcg = Taxes._Taxes__federal_long_term_capital_gains_tax(earned_income, long_term_capital_gains, itemized_deduction)
    print(f"Capital Gains:\nFederal: {fltcg}")

if __name__ == "__main__":
    main()