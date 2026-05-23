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

print("\nAll Day 30 drills passed! Now go build improved password manager.py")
