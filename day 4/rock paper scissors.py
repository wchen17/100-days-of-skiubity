# ============================================================
#  DAY 4 — Randomisation & Python Lists
#  PROJECT: Rock Paper Scissors
# ============================================================
#
#  SKILLS TODAY:
#    - import random           → bring in the random module
#    - random.randint(a, b)    → pick a random int between a and b
#    - random.choice(list)     → pick a random item from a list
#    - Lists []                → ordered collection of items
#    - list[index]             → access item by position (0-based)
#    - len(list)               → number of items in a list
#    - list.append(item)       → add item to end of list
#
#  WHAT TO BUILD:
#    A Rock Paper Scissors game vs the computer.
#    Player types their choice, computer picks randomly.
#    Print who won and why.
#
# ============================================================

import random

# Lists store multiple values in one variable
options = ["rock", "paper", "scissors"]

# ASCII art makes the output look cool
rock     = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper    = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art = [rock, paper, scissors]

# --------------------------------------------------
#  TODO 1: Get the player's choice
# --------------------------------------------------
# Ask the player: "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "
# Store their answer in a variable called player_choice (convert to int)
# Print the art for the player's choice using art[player_choice]

player_choice = int(input("What is thy choice? rock paper or scissor?(0,1,2)"))

if player_choice >= 3 or player_choice <= -1:
    print("Invalid choice. You lose.")
else:
    print(art[player_choice])


    # --------------------------------------------------
    #  TODO 2: Generate the computer's choice
    # --------------------------------------------------
    # Use random.randint(0, 2) to get a random number 0-2
    # Store it in computer_choice
    # Print "Computer chose:" and the art for the computer's choice

    computer_choice = random.randint(0,2)
    print("computer chose:")
    print(art[computer_choice])

# --------------------------------------------------
#  TODO 3: Decide the winner
# --------------------------------------------------
# Rules:
#   rock(0) beats scissors(2)
#   scissors(2) beats paper(1)
#   paper(1) beats rock(0)
#
# Use if/elif/else to compare player_choice and computer_choice
# Print "You win!", "You lose!", or "It's a draw!"
#
# HINT: handle the draw first (player_choice == computer_choice)
# then handle each winning condition for the player,
# then the else = computer wins

# your logic here

    if player_choice == computer_choice:
        print("it's a draw")
    elif player_choice == 0 and computer_choice == 2:
        print("you win")
    elif player_choice == 2 and computer_choice == 1:
        print("you win")
    elif player_choice == 1 and computer_choice == 0:
        print("you win")
    else:
        print("you lose")
# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Wrap the whole game in a while loop so it keeps playing
#     until the player types "quit"
#  2. Track score across multiple rounds
#  3. Validate input — what if the player types 5? Print an
#     error and ask again instead of crashing
# ============================================================
