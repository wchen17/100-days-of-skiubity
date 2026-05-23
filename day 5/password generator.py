# ============================================================
#  DAY 5 — Python Loops
#  PROJECT: Password Generator
# ============================================================
#
#  SKILLS TODAY:
#    - for item in list:      → loop through every item
#    - for i in range(n):     → loop n times
#    - range(start, stop)     → sequence of numbers
#    - while condition:       → loop while something is True
#    - break                  → exit a loop early
#    - continue               → skip to the next iteration
#    - random.shuffle(list)   → shuffle a list in place
#    - random.choice(list)    → pick one random item
#    - "".join(list)          → stick list items into one string
#
# ============================================================

import random

# Character sets to build passwords from
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','+']

print("Welcome to the Password Generator!")

# --------------------------------------------------
#  TODO 1: Ask the user how many of each they want
# --------------------------------------------------
# nr_letters → how many letters?  (int)
# nr_symbols → how many symbols?  (int)
# nr_numbers → how many numbers?  (int)



# --------------------------------------------------
#  TODO 2: Build an EASY (predictable) password first
# --------------------------------------------------
# Loop nr_letters times → pick a random letter, add to password string
# Loop nr_symbols times → pick a random symbol, add to password string
# Loop nr_numbers times → pick a random number, add to password string
# Print the result — this is the EASY level (characters in order)

password_easy = ""
# your loops here
print(f"Easy password: {password_easy}")


# --------------------------------------------------
#  TODO 3: Build a HARD (shuffled) password
# --------------------------------------------------
# Instead of building a string directly, build a LIST of characters
# (same loops as above but append to a list instead)
# Then use random.shuffle() on the list
# Then use "".join(list) to turn the list back into a string
# Print the result

password_list = []
# your loops here
# shuffle here
password_hard = ""  # join here
print(f"Hard password: {password_hard}")


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Let the user generate multiple passwords in a row
#     using a while loop — stop when they type "quit"
#  2. Add a strength checker: count letters/symbols/numbers
#     and print "Weak / Medium / Strong"
#  3. Let the user set a minimum password length instead of
#     picking each character type count separately
# ============================================================
