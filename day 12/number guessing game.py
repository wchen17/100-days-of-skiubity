# ============================================================
#  DAY 12 — Scope
#  PROJECT: Number Guessing Game
# ============================================================
#
#  SKILLS TODAY:
#    - Local scope    → variable created inside a function only exists there
#    - Global scope   → variable created outside all functions
#    - global keyword → let a function modify a global variable
#    - Constants      → UPPER_CASE names signal "don't change this"
#    - Why global is usually a bad idea → prefer return values instead
#
# ============================================================

import random

# Global constant — lives per difficulty
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# --------------------------------------------------
#  TODO 1: set_difficulty() → returns number of turns
# --------------------------------------------------
# Ask "Choose a difficulty. Type 'easy' or 'hard': "
# Return the right constant

def set_difficulty():
    pass


# --------------------------------------------------
#  TODO 2: check_answer(guess, answer, turns)
# --------------------------------------------------
# Compare guess to answer
# If too low  → print "Too low." and return turns - 1
# If too high → print "Too high." and return turns - 1
# If correct  → print "You got it! The answer was {answer}." and return 0

def check_answer(guess, answer, turns):
    pass


# --------------------------------------------------
#  TODO 3: game() — wire it all together
# --------------------------------------------------
# Print the logo / welcome message
# Pick a random number between 1 and 100
# Set turns based on difficulty
# Loop: ask for a guess, call check_answer, update turns
#   If turns == 0 → game over
#   If correct    → exit loop
#   Otherwise     → print how many turns are left

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns  = set_difficulty()

    # TODO: game loop

game()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a "medium" difficulty (7 turns)
#  2. After winning, show how many turns were used
#  3. Ask to play again without restarting the script
# ============================================================
