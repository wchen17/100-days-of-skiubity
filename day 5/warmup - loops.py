# ============================================================
#  DAY 5 — WARM-UP DRILLS: Loops
# ============================================================
#  Run, fail at the first unfinished drill, fix, re-run, repeat.
#  Do these BEFORE password generator.py
# ============================================================


# --- Drill 1: sum 1..n --------------------------------------
# Return the sum of every number from 1 to n (inclusive).
# Example: sum_to(5) -> 1+2+3+4+5 = 15
def sum_to(n):
    pass


# --- Drill 2: sum of even numbers ---------------------------
# Return the sum of all EVEN numbers from 1 to n (inclusive).
# Example: sum_even(10) -> 2+4+6+8+10 = 30
def sum_even(n):
    pass


# --- Drill 3: FizzBuzz --------------------------------------
# Return a LIST of strings for 1..n where:
#   multiples of 3 and 5  -> "FizzBuzz"
#   multiples of 3        -> "Fizz"
#   multiples of 5        -> "Buzz"
#   everything else       -> the number as a string, e.g. "7"
# Example: fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
def fizzbuzz(n):
    pass


# --- Drill 4: countdown with a while loop -------------------
# Using a WHILE loop (not range), return a list counting DOWN
# from n to 1.  Example: countdown(3) -> [3, 2, 1]
def countdown(n):
    pass


# --- Drill 5: highest score without max() -------------------
# Return the largest number in the list WITHOUT using max().
# Loop through and keep track of the biggest you've seen.
def highest(scores):
    pass


# ============================================================
#  SELF-CHECKS
# ============================================================
assert sum_to(5) == 15 and sum_to(1) == 1 and sum_to(100) == 5050
print("Drill 1 passed: sum_to")

assert sum_even(10) == 30 and sum_even(1) == 0
print("Drill 2 passed: sum_even")

assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizzbuzz(15)[-1] == "FizzBuzz"
print("Drill 3 passed: fizzbuzz")

assert countdown(3) == [3, 2, 1] and countdown(1) == [1]
print("Drill 4 passed: countdown")

assert highest([4, 8, 2, 9, 1]) == 9 and highest([-5, -2, -9]) == -2
print("Drill 5 passed: highest")

print("\nAll Day 5 drills passed! Now go build password generator.py")
