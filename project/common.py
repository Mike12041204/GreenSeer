"""TODO
"""

# --- RUN PARAMETERS ---
# 0 - no high information debugging messages, 1 - debugging messages
DEBUG_TOGGLE = 1
DECIMAL_PRECISION = 100
# simulation time parameters
DAYS_PER_PERIOD = 30
DAYS_PER_YEAR = 360
DAYS_PER_QUARTER = 90
DAYS_PER_MONTH = 30
PERIODS_PER_YEAR = DAYS_PER_YEAR / DAYS_PER_PERIOD
PERIODS_PER_QUARTER = DAYS_PER_QUARTER / DAYS_PER_PERIOD
PERIODS_PER_MONTH = DAYS_PER_MONTH / DAYS_PER_PERIOD


# format number in accounting manner
def fa(number) -> str:
        return f"$ {number:,.2f}"

# format number in percent manner
def fp(number) -> str:
        return f"{number * 100:.2f}%"

def println1():
        print("---------+---------+---------+---------+---------+---------+---------+---------+-" +
              "--------+---------+")

def println2():
        print("---------------------------------------------------------------------------------" +
              "-------------------")
        
def println3():
        print("  ------    ------    ------    ------    ------    ------    ------    ------   " +
              " ------    ------  ")
        
def println4():
        print("    --        --        --        --        --        --        --        --     " +
              "   --        --    ")