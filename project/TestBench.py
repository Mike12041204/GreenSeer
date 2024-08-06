import sys
from taxes import Taxes

# Test bench class should be used to test features while being implented
def main():
    Taxes.calculate_tax(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), 0)

if __name__ == "__main__":
    main()