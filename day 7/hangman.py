# ============================================================
#  DAY 7: Combining Skills
#  PROJECT: Hangman
# ============================================================
#
#  SKILLS TODAY (putting it all together):
#    - random.choice(list)         → pick a random word
#    - list * n                    → create a list of n items
#    - "char" in string            → check membership
#    - list[i] = value             → update an item by index
#    - "_".join(list)              → display blanks nicely
#    - while with multiple exits   → game loop with win/lose check
#
# ============================================================

import random

# Word bank: the game picks one of these
word_list = ["ardvark", "baboon", "camel", "python", "javascript",
             "keyboard", "monitor", "algorithm", "variable", "function"]

# Hangman art: each stage is one fewer life
HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# --------------------------------------------------
#  TODO 1: Set up the game state
# --------------------------------------------------
# chosen_word  → use random.choice() on word_list
# word_length  → len(chosen_word)
# lives        → start at 6 (0 = dead, as in HANGMAN_PICS)
# display      → a list of "_" repeated word_length times
#                hint: ["_"] * word_length
# guessed      → an empty list to track letters already tried

chosen_word = None   # TODO
lives       = 6
display     = []     # TODO: list of "_" * word_length
guessed     = []


# --------------------------------------------------
#  TODO 2: Print the welcome message
# --------------------------------------------------
# Tell the player how many letters the word has
# Print the display list joined with spaces so it looks like: _ _ _ _ _


# --------------------------------------------------
#  TODO 3: The main game loop
# --------------------------------------------------
# Loop while lives > 0 AND "_" is still in display
#
# Inside the loop:
#   a) Ask for a letter guess (lower-case it with .lower())
#   b) If the letter was already guessed, warn the player
#   c) Otherwise add it to guessed
#   d) Loop through each position in chosen_word:
#        if chosen_word[position] == guess → set display[position] = guess
#   e) If the guess wasn't in chosen_word → subtract a life
#   f) Print HANGMAN_PICS[6 - lives] to show the gallows
#   g) Print the current display
#   h) Check win/lose conditions and print a message

game_over = False
while not game_over:
    pass  # TODO: replace with your game logic


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Import a bigger word list from a separate file
#  2. Add difficulty: easy (8+ letter words), hard (4 letter words)
#  3. Show a hint if the player has only 1 life left
#  4. Track score across multiple rounds
# ============================================================
