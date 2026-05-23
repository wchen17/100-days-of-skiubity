# ============================================================
#  DAY 10 — WARM-UP DRILLS: Functions with Return Values
# ============================================================
#  Do these BEFORE calculator.py
# ============================================================


# --- Drill 1: format a name ---------------------------------
# Given a first and last name in any casing, return them
# title-cased and joined with a space.
# Example: format_name("aNGela", "yU") -> "Angela Yu"
def format_name(first, last):
    pass


# --- Drill 2: absolute value without abs() ------------------
# Return the absolute (non-negative) value of n.
def absolute(n):
    pass


# --- Drill 3: days in a month -------------------------------
# Return the number of days in the given month of the given year.
# Months: [31,28,31,30,31,30,31,31,30,31,30,31] for a normal year.
# LEAP YEAR rule: divisible by 4 AND (not divisible by 100, OR
# divisible by 400). In a leap year February has 29 days.
# month is 1-12.  (This is the classic Day 10 challenge.)
def days_in_month(year, month):
    pass


# --- Drill 4: early return ----------------------------------
# Return "FizzBuzz" / "Fizz" / "Buzz" / str(n) for a SINGLE number.
# Practise returning early instead of nesting if/else.
def fizz_one(n):
    pass


# ============================================================
#  SELF-CHECKS
# ============================================================
assert format_name("aNGela", "yU") == "Angela Yu"
assert format_name("ROSS", "geller") == "Ross Geller"
print("Drill 1 passed: format_name")

assert absolute(-5) == 5 and absolute(5) == 5 and absolute(0) == 0
print("Drill 2 passed: absolute")

assert days_in_month(2024, 2) == 29   # leap year
assert days_in_month(2023, 2) == 28   # not a leap year
assert days_in_month(1900, 2) == 28   # divisible by 100 but not 400
assert days_in_month(2000, 2) == 29   # divisible by 400
assert days_in_month(2023, 1) == 31 and days_in_month(2023, 4) == 30
print("Drill 3 passed: days_in_month")

assert fizz_one(3) == "Fizz" and fizz_one(5) == "Buzz"
assert fizz_one(15) == "FizzBuzz" and fizz_one(7) == "7"
print("Drill 4 passed: fizz_one")

print("\nAll Day 10 drills passed! Now go build calculator.py")
