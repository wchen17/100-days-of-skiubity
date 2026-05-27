# ============================================================
#  DAY 13 PRACTICE: Debugging Drills
# ============================================================
#  No new code. Fix the broken functions below using the 6-step
#  process in day_13_concepts.md. PREDICT each bug in a comment
#  BEFORE running, then confirm with print() or the debugger.
#
#  TOOLS: reading errors, print(var, type(var)), the debugger.
# ============================================================

# --- BUG 1: always returns 0. Why? ---
def average(numbers):
    total = 0
    for n in numbers:
        total == total + n        # something is off on this line
    return total / len(numbers)
# average([4, 8, 15, 16, 23, 42]) should be 18.0


# --- BUG 2: crashes. What error, and why? ---
fruits = ["apple", "mango", "pear"]
# print(fruits[3])                # should print "pear"


# --- BUG 3: prints "odd" for 4. Two bugs on one line, plus one more. ---
# number = 4
# if number % 2 = 0:
#     print("even")
# else
#     print("odd")


# --- BUG 4: prints 1 to 9, should print 1 to 10 inclusive. ---
# for i in range(1, 10):
#     print(i)

# Fix each one at a time. Describe the bug in a comment before you fix it.
