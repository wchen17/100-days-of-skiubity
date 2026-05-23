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

print("\nAll Day 26 drills passed! Now go build the NATO alphabet project.")
