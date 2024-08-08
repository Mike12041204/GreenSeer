import common
import sys
from taxes import Taxes
from decimal import getcontext

# Test bench class should be used to test features while being implented
def main():
    getcontext().prec = common.DECIMAL_PRECISION

    Taxes.calculate_tax(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), 0, int(sys.argv[4]))

if __name__ == "__main__":
    main()