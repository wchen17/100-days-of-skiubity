# ============================================================
#  DAY 11 — Capstone Project
#  PROJECT: Blackjack
# ============================================================
#
#  CAPSTONE = everything from days 1-10 in one project:
#    random, lists, functions, parameters, return values,
#    while loops, if/elif/else, dictionaries
#
#  BLACKJACK RULES (simplified):
#    - You and the dealer each get 2 cards
#    - Number cards = face value; J/Q/K = 10; Ace = 11 (or 1 if over 21)
#    - You can "hit" (get another card) or "stand" (stop)
#    - Get closer to 21 than the dealer without going over
#    - Over 21 = "bust" = you lose
#    - Dealer must hit until they reach 17 or higher
#
# ============================================================

import random
from art import logo   # TODO: create an art.py file with a logo string (optional)

# Deck — infinite shoe (we just pick random cards each time)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# --------------------------------------------------
#  TODO 1: deal_card() — returns one random card from cards
# --------------------------------------------------
def deal_card():
    pass


# --------------------------------------------------
#  TODO 2: calculate_score(hand) — returns the score
# --------------------------------------------------
# hand is a list of card values
# Sum them up
# If sum > 21 and 11 is in the hand → replace the 11 with a 1
# Special rule: if hand has exactly 2 cards and sums to 21 → return 0
#   (0 signals a natural Blackjack — unbeatable hand)

def calculate_score(hand):
    pass


# --------------------------------------------------
#  TODO 3: compare(user_score, computer_score) — print winner
# --------------------------------------------------
# Handle these cases in order:
#   both == 0           → Draw (both have Blackjack)
#   user == 0           → Win with a Blackjack!
#   computer == 0       → Lose, opponent has Blackjack
#   user > 21           → You went over. You lose.
#   computer > 21       → Opponent went over. You win!
#   user > computer     → You win!
#   user < computer     → You lose!
#   else                → Draw

def compare(user_score, computer_score):
    pass


# --------------------------------------------------
#  TODO 4: play_game() — the main game function
# --------------------------------------------------
# Deal 2 cards to both player and computer
# Show player's cards + score; show only computer's FIRST card
# Loop: ask "Type 'y' to get another card, 'n' to pass: "
#   if 'y' → deal another card; if score goes over 21 → stop
#   if 'n' → stop
# Computer hits until score >= 17 or it busts
# Show final hands and scores
# Call compare() to print the result

def play_game():
    pass


# --------------------------------------------------
#  Game entry loop
# --------------------------------------------------
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    # clear screen between games
    print("\n" * 20)
    play_game()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add betting — start with $100, wager before each hand
#  2. Add splitting (when you have two of the same card)
#  3. Add a "double down" option
# ============================================================
