# ============================================================
#  DAY 10: Functions with Return Values
#  PROJECT: Calculator
# ============================================================
#
#  SKILLS TODAY:
#    - return value            → send a result back from a function
#    - Storing return values   → result = my_func()
#    - Functions as values     → storing functions in a dictionary
#    - Recursive-style loop    → using the result as next input
#
# ============================================================

# --------------------------------------------------
#  TODO 1: Write the four maths functions
# --------------------------------------------------
# Each takes two numbers (n1, n2) and RETURNS the result.
# Do NOT print inside them: just return.

def add(n1, n2):
    pass  # TODO: return n1 + n2

def subtract(n1, n2):
    pass  # TODO

def multiply(n1, n2):
    pass  # TODO

def divide(n1, n2):
    pass  # TODO: handle division by zero: return None or print a warning


# --------------------------------------------------
#  DEMO: Functions stored in a dictionary
# --------------------------------------------------
# This lets you look up which function to call based on user input.

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# --------------------------------------------------
#  TODO 2: Build the calculator loop
# --------------------------------------------------
# Start by asking for the first number (float)
# Show the available operations: + - * /
# Ask which operation to use
# Ask for the second number (float)
# Look up the function in the operations dict and CALL it
# Print the result: e.g.  "10.0 + 5.0 = 15.0"
# Ask: "Type 'y' to continue with result, 'n' for new calc, 'quit' to exit"
#   'y'    → use the result as the new first_number, loop again
#   'n'    → restart from scratch
#   'quit' → exit

def calculator():
    first_number = float(input("What's the first number?: "))
    should_accumulate = True

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        second_number    = float(input("What's the next number?: "))

        # TODO: get the right function from operations dict and call it
        answer = None

        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        # TODO: ask user what to do next and handle their choice

calculator()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add % (modulo) and ** (exponent) to the operations dict
#  2. Show a history of all calculations in the session
#  3. Add a memory function: store a result and recall it later
# ============================================================
