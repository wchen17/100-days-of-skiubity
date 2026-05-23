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

print("\nAll Day 8 drills passed! Now go build caesar cipher.py")
