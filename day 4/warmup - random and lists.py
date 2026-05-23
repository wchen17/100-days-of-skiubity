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

print("\nAll Day 4 drills passed! Now go build rock paper scissors.py")
