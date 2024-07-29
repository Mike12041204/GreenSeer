from simulation import Simulation

# 0 - no high information debugging messages, 1 - debugging messages
DEBUG_TOGGLE = 1

# The main class, creates and runs a simulation.
# Later may be expanded to develop a deep learning model on the game.
def main():
    simulation = Simulation()

    simulation.simulate()

if __name__ == "__main__":
    main()