import os
base = "/home/user/100-days-of-skiubity"
files = {}

# ----------------------------------------------------------------
files["day 4/warmup - random and lists.py"] = """\
# ============================================================
#  DAY 4 — WARM-UP DRILLS: Randomisation & Lists
# ============================================================
#
#  HOW TO USE THIS FILE:
#    Run it. It will FAIL at the first unfinished drill with a
#    clear message. Fill in that one function, re-run, watch it
#    pass, then move to the next. Do these BEFORE rock paper scissors.py
#
#  No fill-in-the-blank here — you write the whole function body.
#  The asserts at the bottom of each drill tell you if you got it right.
# ============================================================

import random


# --- Drill 1: dice ------------------------------------------
# Return a random whole number between 1 and 6 (inclusive).
def roll_dice():
    pass   # write your code here, then delete this line


# --- Drill 2: coin flip -------------------------------------
# Return either the string "Heads" or "Tails" at random.
def flip_coin():
    pass


# --- Drill 3: indexing --------------------------------------
# Return the THIRD item of any list (remember: lists start at index 0).
def third_item(items):
    pass


# --- Drill 4: append ----------------------------------------
# Add `item` to the end of `items` and return the whole list.
def add_item(items, item):
    pass


# --- Drill 5: banker roulette -------------------------------
# Given a list of names, pick ONE name at random and return it.
# (This is literally the Day 4 "who pays the bill" project in miniature.)
def pick_random(names):
    pass


# ============================================================
#  SELF-CHECKS — do not edit below this line
# ============================================================
for _ in range(50):
    assert 1 <= roll_dice() <= 6, "roll_dice() must return 1-6"
print("Drill 1 passed: roll_dice")

for _ in range(50):
    assert flip_coin() in ("Heads", "Tails"), "flip_coin() must return 'Heads' or 'Tails'"
print("Drill 2 passed: flip_coin")

assert third_item([10, 20, 30, 40]) == 30, "third_item should return the item at index 2"
assert third_item(["a", "b", "c"]) == "c"
print("Drill 3 passed: third_item")

assert add_item([1, 2], 3) == [1, 2, 3], "add_item should append and return the list"
assert add_item([], "x") == ["x"]
print("Drill 4 passed: add_item")

names = ["Angela", "Ben", "Cara"]
for _ in range(50):
    assert pick_random(names) in names, "pick_random must return one of the names"
print("Drill 5 passed: pick_random")

print("\\nAll Day 4 drills passed! Now go build rock paper scissors.py")
"""

# ----------------------------------------------------------------
files["day 5/warmup - loops.py"] = """\
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

print("\\nAll Day 5 drills passed! Now go build password generator.py")
"""

# ----------------------------------------------------------------
files["day 8/warmup - function inputs.py"] = """\
# ============================================================
#  DAY 8 — WARM-UP DRILLS: Function Parameters
# ============================================================
#  Do these BEFORE caesar cipher.py
# ============================================================


# --- Drill 1: positional arguments --------------------------
# Return the area of a rectangle (width * height).
def rectangle_area(width, height):
    pass


# --- Drill 2: using two arguments together ------------------
# Return a greeting like:  "Hello Sam, welcome to Tokyo!"
# given the name and the place.
def greet(name, place):
    pass


# --- Drill 3: is it a prime number? -------------------------
# Return True if n is prime, False otherwise.
# A prime is only divisible by 1 and itself. (1 is NOT prime.)
# This is the classic Day 8 challenge — loop and test divisibility.
def is_prime(n):
    pass


# --- Drill 4: keyword arguments -----------------------------
# Return total cost = (price * quantity), then apply a discount
# percentage. discount is a keyword arg defaulting to 0.
# Example: order_total(10, 3) -> 30
#          order_total(10, 3, discount=50) -> 15.0
def order_total(price, quantity, discount=0):
    pass


# ============================================================
#  SELF-CHECKS
# ============================================================
assert rectangle_area(4, 5) == 20 and rectangle_area(3, 3) == 9
print("Drill 1 passed: rectangle_area")

assert greet("Sam", "Tokyo") == "Hello Sam, welcome to Tokyo!"
print("Drill 2 passed: greet")

assert is_prime(7) is True and is_prime(2) is True
assert is_prime(1) is False and is_prime(9) is False and is_prime(15) is False
print("Drill 3 passed: is_prime")

assert order_total(10, 3) == 30
assert order_total(10, 3, discount=50) == 15.0
print("Drill 4 passed: order_total")

print("\\nAll Day 8 drills passed! Now go build caesar cipher.py")
"""

# ----------------------------------------------------------------
files["day 9/warmup - dictionaries.py"] = """\
# ============================================================
#  DAY 9 — WARM-UP DRILLS: Dictionaries & Nesting
# ============================================================
#  Do these BEFORE secret auction.py
# ============================================================


# --- Drill 1: look up a value -------------------------------
# scores is a dict like {"Alice": 90, "Bob": 75}.
# Return the score for the given name.
def get_score(scores, name):
    pass


# --- Drill 2: add / update an entry -------------------------
# Add name->score into the scores dict (or overwrite if it
# already exists) and return the whole dict.
def set_score(scores, name, score):
    pass


# --- Drill 3: grading program -------------------------------
# Given a numeric score, return a letter grade:
#   90-100 -> "A"   80-89 -> "B"   70-79 -> "C"
#   60-69  -> "D"   below 60 -> "F"
# (This is the exact Day 9 grading exercise.)
def grade_for(score):
    pass


# --- Drill 4: loop through a dict ---------------------------
# Return the NAME of the person with the highest score.
def top_student(scores):
    pass


# --- Drill 5: nested dictionary -----------------------------
# travel_log looks like:
#   {"France": {"cities": ["Paris", "Lille"], "visits": 12}, ...}
# Return the list of cities for the given country.
def cities_in(travel_log, country):
    pass


# ============================================================
#  SELF-CHECKS
# ============================================================
sample = {"Alice": 90, "Bob": 75}
assert get_score(sample, "Alice") == 90
print("Drill 1 passed: get_score")

assert set_score({"Bob": 75}, "Cara", 88) == {"Bob": 75, "Cara": 88}
assert set_score({"Bob": 75}, "Bob", 80) == {"Bob": 80}
print("Drill 2 passed: set_score")

assert grade_for(95) == "A" and grade_for(82) == "B" and grade_for(71) == "C"
assert grade_for(65) == "D" and grade_for(40) == "F"
print("Drill 3 passed: grade_for")

assert top_student({"Alice": 90, "Bob": 99, "Cara": 88}) == "Bob"
print("Drill 4 passed: top_student")

log = {"France": {"cities": ["Paris", "Lille"], "visits": 12},
       "Japan":  {"cities": ["Tokyo"], "visits": 2}}
assert cities_in(log, "France") == ["Paris", "Lille"]
assert cities_in(log, "Japan") == ["Tokyo"]
print("Drill 5 passed: cities_in")

print("\\nAll Day 9 drills passed! Now go build secret auction.py")
"""

# ----------------------------------------------------------------
files["day 10/warmup - return values.py"] = """\
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

print("\\nAll Day 10 drills passed! Now go build calculator.py")
"""

# ----------------------------------------------------------------
files["day 12/warmup - scope.py"] = """\
# ============================================================
#  DAY 12 — WARM-UP DRILLS: Scope (fix-the-bug style)
# ============================================================
#  Scope drills are about UNDERSTANDING, so this one has a bit
#  more scaffold: buggy code is shown, you predict + fix it.
#  Do these BEFORE number guessing game.py
# ============================================================


# --- Drill 1: predict the output ----------------------------
# BEFORE running, write down what you think this prints.
# Then run it and see if you were right.
def drill1():
    x = 10            # local to drill1
    def inner():
        x = 20        # a DIFFERENT x, local to inner
        return x
    inner()
    return x          # which x is this?

# TODO: write your prediction here as a comment:
# PREDICTION: drill1() returns ____


# --- Drill 2: the broken counter ----------------------------
# This is SUPPOSED to count up, but it crashes / doesn't work.
# The function tries to change a global variable without permission.
# FIX it so add_enemy() correctly increases enemy_count.
enemy_count = 0

def add_enemy():
    # BUG: this line tries to modify the global but Python treats
    #      enemy_count as a NEW local variable -> UnboundLocalError
    enemy_count = enemy_count + 1     # <-- fix this
    return enemy_count


# --- Drill 3: keep it local ---------------------------------
# Rewrite add_enemy as a CLEAN function that takes the current
# count as a parameter and RETURNS the new count — no globals.
# (This is the better pattern: avoid globals, pass values in/out.)
def next_count(current):
    pass


# ============================================================
#  SELF-CHECKS
# ============================================================
assert drill1() == 10, "The outer x is untouched by inner()'s local x"
print("Drill 1 passed: scope prediction")

enemy_count = 0
assert add_enemy() == 1 and add_enemy() == 2 and add_enemy() == 3
print("Drill 2 passed: add_enemy")

assert next_count(0) == 1 and next_count(41) == 42
print("Drill 3 passed: next_count")

print("\\nAll Day 12 drills passed! Now go build number guessing game.py")
"""

# ----------------------------------------------------------------
files["day 26/warmup - comprehensions.py"] = """\
# ============================================================
#  DAY 26 — WARM-UP DRILLS: List & Dict Comprehensions
# ============================================================
#  Each of these is ONE LINE using a comprehension. Try to avoid
#  writing a traditional for-loop with append().
#  Do these BEFORE the NATO alphabet project.
# ============================================================


# --- Drill 1: squares ---------------------------------------
# Return a list of the squares of 0..n-1.
# Example: squares(5) -> [0, 1, 4, 9, 16]
def squares(n):
    pass


# --- Drill 2: filter evens ----------------------------------
# Return only the even numbers from the input list.
def evens(numbers):
    pass


# --- Drill 3: uppercase each word ---------------------------
def shout(words):
    pass


# --- Drill 4: dict comprehension ----------------------------
# Return a dict mapping each word to its length.
# Example: lengths(["hi", "bye"]) -> {"hi": 2, "bye": 3}
def lengths(words):
    pass


# --- Drill 5: comprehension with a condition ----------------
# From a dict of {name: score}, return a LIST of the names
# of everyone who scored 60 or higher (a "pass").
def passed(scores):
    pass


# ============================================================
#  SELF-CHECKS
# ============================================================
assert squares(5) == [0, 1, 4, 9, 16]
print("Drill 1 passed: squares")

assert evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
print("Drill 2 passed: evens")

assert shout(["hi", "there"]) == ["HI", "THERE"]
print("Drill 3 passed: shout")

assert lengths(["hi", "bye"]) == {"hi": 2, "bye": 3}
print("Drill 4 passed: lengths")

assert sorted(passed({"Al": 90, "Bo": 55, "Cy": 60})) == ["Al", "Cy"]
print("Drill 5 passed: passed")

print("\\nAll Day 26 drills passed! Now go build the NATO alphabet project.")
"""

# ----------------------------------------------------------------
files["day 30/warmup - exceptions.py"] = """\
# ============================================================
#  DAY 30 — WARM-UP DRILLS: Error Handling
# ============================================================
#  Practise try / except so the improved password manager
#  doesn't crash on missing files or bad input.
#  Do these BEFORE improved password manager.py
# ============================================================


# --- Drill 1: safe divide -----------------------------------
# Return a / b, BUT if b is 0, catch the ZeroDivisionError and
# return None instead of crashing.
def safe_divide(a, b):
    pass


# --- Drill 2: safe int conversion ---------------------------
# Try to convert the string s to an int. If it can't (ValueError),
# return None.  Example: to_int("42") -> 42 ; to_int("hi") -> None
def to_int(s):
    pass


# --- Drill 3: safe list access ------------------------------
# Return items[index]. If the index is out of range (IndexError),
# return a default value (the `default` parameter).
def get_at(items, index, default=None):
    pass


# --- Drill 4: safe dict lookup ------------------------------
# Return data[key]. If the key is missing (KeyError), return the
# string "not found".  (Bonus: could you do this with .get()? Try both.)
def lookup(data, key):
    pass


# ============================================================
#  SELF-CHECKS
# ============================================================
assert safe_divide(10, 2) == 5 and safe_divide(5, 0) is None
print("Drill 1 passed: safe_divide")

assert to_int("42") == 42 and to_int("hello") is None
print("Drill 2 passed: to_int")

assert get_at([1, 2, 3], 1) == 2
assert get_at([1, 2, 3], 99, default="oops") == "oops"
print("Drill 3 passed: get_at")

assert lookup({"a": 1}, "a") == 1 and lookup({"a": 1}, "z") == "not found"
print("Drill 4 passed: lookup")

print("\\nAll Day 30 drills passed! Now go build improved password manager.py")
"""

# ----------------------------------------------------------------
files["day 33/warmup - api practice.py"] = """\
# ============================================================
#  DAY 33 — WARM-UP DRILLS: First API Calls
# ============================================================
#  APIs need the internet, so these can't be self-checked with
#  asserts offline. This one has light scaffold + TODOs.
#  All APIs below are FREE and need NO key.
#  Do these BEFORE iss notifier.py
#
#  pip install requests
# ============================================================

import requests


# --- Drill 1: guess an age from a name ----------------------
# API: https://api.agify.io?name=SOMENAME
# It returns JSON like: {"name": "michael", "age": 56, "count": ...}
def guess_age(name):
    # TODO:
    #   1. response = requests.get("https://api.agify.io", params={"name": name})
    #   2. response.raise_for_status()
    #   3. data = response.json()
    #   4. return data["age"]
    pass


# --- Drill 2: a random useless fact -------------------------
# API: https://uselessfacts.jsph.pl/api/v2/facts/random
# Returns JSON with a "text" key.
def random_fact():
    # TODO: GET the url, parse json, return the "text" field
    pass


# --- Drill 3: check a status code ---------------------------
# GET https://httpbin.org/status/404 and RETURN the numeric
# status code (response.status_code). It should be 404.
# Then try /status/200 and /status/500 to see them change.
def get_status(code):
    # TODO: requests.get(f"https://httpbin.org/status/{code}")
    #       return response.status_code
    pass


# --- Drill 4: API with parameters ---------------------------
# API: https://api.coindesk.com/v1/bpi/currentprice.json (Bitcoin price)
# OR:  https://api.frankfurter.app/latest?from=USD&to=EUR (exchange rate)
# Use params={} and dig into the nested JSON to return the EUR rate.
def usd_to_eur():
    # TODO: GET frankfurter, params {"from": "USD", "to": "EUR"}
    #       return response.json()["rates"]["EUR"]
    pass


# ============================================================
#  TRY IT (uncomment once you've filled the functions in):
# ============================================================
# print("Age for 'Michael':", guess_age("Michael"))
# print("Random fact:", random_fact())
# print("Status test:", get_status(404))
# print("1 USD in EUR:", usd_to_eur())

print("Fill in the functions above, then uncomment the TRY IT block.")
print("If a call works, you're ready for the ISS notifier project.")
"""

for filepath, content in files.items():
    full_path = os.path.join(base, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Created: {filepath}")

print(f"\\nDone — {len(files)} warm-up drill files written.")
