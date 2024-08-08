'''TODO
'''

# --- RUN PARAMETERS ---
# 0 - no high information debugging messages, 1 - debugging messages
DEBUG_TOGGLE = 1
DECIMAL_PRECISION = 100

# format number in accounting manner
def fa(number):
        return f"$ {number:,.2f}"

# format number in percent manner
def fp(number):
        return f"{number * 100:.2f}%"