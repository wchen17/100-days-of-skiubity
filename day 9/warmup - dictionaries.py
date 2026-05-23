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

print("\nAll Day 9 drills passed! Now go build secret auction.py")
