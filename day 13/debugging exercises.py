# ============================================================
#  DAY 13 — Debugging
#  PROJECT: Fix the Broken Code
# ============================================================
#
#  SKILLS TODAY:
#    - Reading error messages   → type, line number, message
#    - print() debugging        → add prints to see what's happening
#    - Describe the problem     → rubber duck debugging
#    - Reproduce the error      → find the minimal failing case
#    - Common errors:
#        NameError    → variable doesn't exist / misspelled
#        TypeError    → wrong type (e.g. adding str + int)
#        IndexError   → list index out of range
#        ValueError   → invalid value (e.g. int("hello"))
#        AttributeError → method doesn't exist on that type
#        IndentationError → wrong indentation
#        LogicError   → code runs but gives wrong answer
#
#  INSTRUCTIONS:
#    Each TODO below has broken code. Fix it. Don't just delete —
#    understand WHY it was broken first.
#
# ============================================================

# --------------------------------------------------
#  BUG 1: TypeError — add a debug print first, then fix
# --------------------------------------------------
age = input("What is your age? ")
# Bug: can't multiply a string by a float
# days_lived = age * 365
# TODO: fix the line above and print the result

# --------------------------------------------------
#  BUG 2: NameError — a variable is used before it's created
# --------------------------------------------------
# TODO: figure out what's wrong and fix it without removing lines
# score = 0
# for i in range(10):
#     soore += 1   ← spot the typo
# print(score)

# --------------------------------------------------
#  BUG 3: IndexError
# --------------------------------------------------
fruits = ["apple", "mango", "pear"]
# TODO: fix so it prints "pear" without changing the list
# print(fruits[3])

# --------------------------------------------------
#  BUG 4: Logic error — off-by-one in range
# --------------------------------------------------
# This should print 1 to 10 inclusive. Fix it.
# for i in range(1, 10):
#     print(i)

# --------------------------------------------------
#  BUG 5: Logic error — wrong condition
# --------------------------------------------------
# Should print "even" for even numbers, "odd" for odd.
# Fix the condition.
# number = 4
# if number % 2 = 0:   ← two bugs here
#     print("even")
# else
#     print("odd")

# --------------------------------------------------
#  BUG 6: Debugging a function — use print() to trace it
# --------------------------------------------------
# This should return the average of a list but always returns 0.
# Add print statements inside to find where it goes wrong, then fix it.
def average(numbers):
    total = 0
    for n in numbers:
        total == total + n   # bug here
    return total / len(numbers)

# Uncomment to test once you've fixed the function:
# print(average([4, 8, 15, 16, 23, 42]))   # should print 18.0


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Write your OWN buggy function and swap with a friend to fix
#  2. Look up Python's built-in debugger: import pdb; pdb.set_trace()
#  3. Try using your IDE's debugger to step through code line by line
# ============================================================
