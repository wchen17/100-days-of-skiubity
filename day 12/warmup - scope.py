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

print("\nAll Day 12 drills passed! Now go build number guessing game.py")
