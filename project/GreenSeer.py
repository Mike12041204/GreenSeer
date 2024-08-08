import common
from simulation import Simulation
from decimal import getcontext
import sys

# The main class, creates and runs a simulation.
# Later may be expanded to develop a deep learning model on the game.
def main():
    # set decimal precision for use in calculations
    getcontext().prec = common.DECIMAL_PRECISION
    common.DEBUG_TOGGLE = int(sys.argv[1])

    simulation = Simulation()

    simulation.simulate()

if __name__ == "__main__":
    main()