# ============================================================
#  DAY 14 — Capstone: Beginner Phase
#  PROJECT: Higher or Lower (Instagram Follower Game)
# ============================================================
#
#  CAPSTONE — uses EVERYTHING from Days 1-13:
#    random, lists, dicts, functions, return values, loops, scope
#
#  GAME RULES:
#    - Show two accounts (A and B) with their follower counts hidden
#    - Player guesses which has MORE followers: 'A' or 'B'
#    - Correct → score goes up, B becomes the new A, new B revealed
#    - Wrong   → game over, show final score
#
# ============================================================

import random

# Sample data — each entry: name, description, country, follower_count
data = [
    {"name": "Instagram",      "description": "Social media platform", "country": "USA",   "follower_count": 346},
    {"name": "Cristiano Ronaldo","description":"Footballer",           "country": "Portugal","follower_count": 475},
    {"name": "Ariana Grande",   "description": "Musician",             "country": "USA",   "follower_count": 284},
    {"name": "Dwayne Johnson",  "description": "Actor",                "country": "USA",   "follower_count": 289},
    {"name": "Selena Gomez",    "description": "Musician and actress", "country": "USA",   "follower_count": 320},
    {"name": "Kylie Jenner",    "description": "Reality TV star",      "country": "USA",   "follower_count": 300},
    {"name": "Kim Kardashian",  "description": "Reality TV star",      "country": "USA",   "follower_count": 270},
    {"name": "Beyoncé",         "description": "Musician",             "country": "USA",   "follower_count": 240},
    {"name": "NASA",            "description": "Space agency",         "country": "USA",   "follower_count": 75},
    {"name": "National Geographic","description":"Nature & science",   "country": "USA",   "follower_count": 150},
]

logo = """
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ /_/_/\__, /_/ /_/\___/_/  or
        /____/
 __
/ /  ______      _____ _ __
/ /  / _ \ \ /\ / / _ \ '__|
/ /__| (_) \ V  V /  __/ |
\____/\___/ \_/\_/ \___|_|
"""


# --------------------------------------------------
#  TODO 1: format_data(account) → returns a display string
# --------------------------------------------------
# "Compare A: Instagram, a Social media platform, from USA"

def format_data(account):
    pass


# --------------------------------------------------
#  TODO 2: check_answer(guess, a_followers, b_followers)
# --------------------------------------------------
# Return True if the guess was correct, False otherwise
# A is correct if a_followers >= b_followers and guess == 'A'
# B is correct if b_followers > a_followers and guess == 'B'

def check_answer(guess, a_followers, b_followers):
    pass


# --------------------------------------------------
#  TODO 3: game() — main game loop
# --------------------------------------------------
# Print logo
# Pick a random account for A
# score = 0
# game_should_continue = True
#
# While game_should_continue:
#   Pick a different random account for B (make sure it's not A)
#   Display A and B with format_data
#   Ask: "Who has more followers? Type 'A' or 'B': "
#   Clear screen (print "\n" * 20)
#   If check_answer correct:
#     score += 1
#     Print "You're right! Current score: {score}"
#     A = B  (the winner becomes the new comparison point)
#   Else:
#     Print "Sorry, that's wrong. Final score: {score}"
#     game_should_continue = False

def game():
    pass

game()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Pull real data from the Instagram / Twitter API
#  2. Add more accounts to the data list (at least 20)
#  3. Show the actual follower counts after each round
# ============================================================
