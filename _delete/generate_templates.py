import os

days = {}

days[4] = ("day 4", "rock paper scissors.py", """\
# ============================================================
#  DAY 4: Randomisation & Python Lists
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
rock     = \"\"\"
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\"\"\"
paper    = \"\"\"
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
\"\"\"
scissors = \"\"\"
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\"\"\"

art = [rock, paper, scissors]

# --------------------------------------------------
#  TODO 1: Get the player's choice
# --------------------------------------------------
# Ask the player: "What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "
# Store their answer in a variable called player_choice (convert to int)
# Print the art for the player's choice using art[player_choice]

player_choice = None  # replace this line


# --------------------------------------------------
#  TODO 2: Generate the computer's choice
# --------------------------------------------------
# Use random.randint(0, 2) to get a random number 0-2
# Store it in computer_choice
# Print "Computer chose:" and the art for the computer's choice

computer_choice = None  # replace this line


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


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Wrap the whole game in a while loop so it keeps playing
#     until the player types "quit"
#  2. Track score across multiple rounds
#  3. Validate input: what if the player types 5? Print an
#     error and ask again instead of crashing
# ============================================================
""")

days[5] = ("day 5", "password generator.py", """\
# ============================================================
#  DAY 5: Python Loops
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
# Print the result: this is the EASY level (characters in order)

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
#     using a while loop: stop when they type "quit"
#  2. Add a strength checker: count letters/symbols/numbers
#     and print "Weak / Medium / Strong"
#  3. Let the user set a minimum password length instead of
#     picking each character type count separately
# ============================================================
""")

days[6] = ("day 6", "functions intro.py", """\
# ============================================================
#  DAY 6: Python Functions & Reeborg's World
#  PROJECT: Maze Solver (simulated with functions)
# ============================================================
#
#  SKILLS TODAY:
#    - def function_name():   → define a function
#    - function_name()        → call / invoke a function
#    - Indentation            → everything inside the def is indented
#    - Code reuse             → write once, call many times
#    - Karel-style thinking   → break a big problem into small steps
#
#  NOTE: Reeborg's World is an online tool at reeborg.ca/reeborg.html
#        but we'll simulate the idea here with printed steps.
#
# ============================================================

# --------------------------------------------------
#  DEMO: How functions work
# --------------------------------------------------
# A function is a named block of code you can reuse.

def greet():
    print("Hello! I am a robot.")
    print("I follow instructions one step at a time.")

greet()   # calling the function runs its code
greet()   # you can call it as many times as you want


# --------------------------------------------------
#  TODO 1: Define these basic movement functions
# --------------------------------------------------
# def turn_right():   → print "Turning right"
# def turn_around():  → call turn_left() TWICE (reuse your functions!)
#
# Remember: Reeborg only has turn_left() built in,
# but you can MAKE turn_right by turning left 3 times.

def turn_left():
    print("Turning left")

def turn_right():
    pass  # TODO: replace pass: call turn_left() 3 times

def turn_around():
    pass  # TODO: replace pass: call turn_left() twice


# --------------------------------------------------
#  TODO 2: Define a jump() function
# --------------------------------------------------
# A "jump" in Reeborg's World = move forward, turn, climb, turn back
# Simulate it by printing the steps in order.
# Then call jump() 6 times to clear a row of 6 hurdles.

def jump():
    pass  # TODO: print the steps of a jump, then move forward


# --------------------------------------------------
#  TODO 3: Solve a maze using only your functions
# --------------------------------------------------
# Imagine a simple maze:
#   → go forward 3 steps
#   → turn right
#   → go forward 2 steps
#   → turn left
#   → go forward 1 step  → FINISH
#
# Write out the solution by CALLING your functions.
# Don't repeat raw print statements: use the functions you made.

def move():
    print("Moving forward")

# your maze solution here (just function calls in order)


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Try Reeborg's World online (reeborg.ca) and paste your
#     functions there to solve an actual graphical maze
#  2. Add a parameter to move(): def move(steps=1)
#     so move(3) moves 3 times in one call
#  3. Write a function that solves a WHILE-loop maze:
#     keep going until you "reach the end" flag
# ============================================================
""")

days[7] = ("day 7", "hangman.py", """\
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
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
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
""")

days[8] = ("day 8", "caesar cipher.py", """\
# ============================================================
#  DAY 8: Function Parameters & Caesar Cipher
#  PROJECT: Caesar Cipher Encoder/Decoder
# ============================================================
#
#  SKILLS TODAY:
#    - def func(param):         → function with a parameter
#    - def func(p1, p2, p3):    → multiple parameters
#    - Positional arguments     → order matters when calling
#    - Keyword arguments        → func(name="Alice"): order doesn't matter
#    - string.lower()           → normalise case
#    - chr() and ord()          → convert between char and ASCII number
#    - % (modulo)               → wrap numbers around (e.g. 26 % 26 == 0)
#
#  HOW CAESAR CIPHER WORKS:
#    Shift every letter by a fixed number of positions in the alphabet.
#    "abc" shifted by 3 → "def"
#    "xyz" shifted by 3 → "abc"  ← wraps around using modulo
#
# ============================================================

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

# --------------------------------------------------
#  TODO 1: Write the caesar() function
# --------------------------------------------------
# Parameters:
#   start_text  → the message to encode/decode
#   shift_amount → how many positions to shift
#   direction   → "encode" or "decode"
#
# Logic:
#   - If direction == "decode", flip the shift: shift_amount = -shift_amount
#   - Loop through each letter in start_text
#   - If the letter is in the alphabet:
#       find its index, add the shift, wrap with % 26
#       look up that index in alphabet → new letter
#   - If the letter is NOT in alphabet (space, punctuation, number):
#       keep it unchanged
#   - Print the final encoded/decoded string

def caesar(start_text, shift_amount, direction):
    pass  # TODO: implement the cipher logic


# --------------------------------------------------
#  TODO 2: Build the game loop
# --------------------------------------------------
# Ask: "Type 'encode' to encrypt, 'decode' to decrypt: "
# Ask: "Type your message: "   (lower-case it)
# Ask: "Type the shift number: "  (int)
# Call caesar() with those three values
# Ask: "Go again? yes or no: "
# Loop while they say yes

should_continue = True
while should_continue:
    direction  = input("Type 'encode' to encrypt, type 'decode' to decrypt:\\n").lower()
    text       = input("Type your message:\\n").lower()
    shift      = int(input("Type the shift number:\\n"))

    caesar(start_text=text, shift_amount=shift, direction=direction)

    restart = input("Type 'yes' if you want to go again, 'no' to quit:\\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Make the cipher work with UPPER-CASE letters too
#  2. Support numbers in the cipher (shift 0-9 by shift_amount % 10)
#  3. Add a "brute force" mode: try all 26 shifts and print them all
#     so the user can spot which one looks like real text
# ============================================================
""")

days[9] = ("day 9", "secret auction.py", """\
# ============================================================
#  DAY 9: Dictionaries & Nesting
#  PROJECT: Secret Auction
# ============================================================
#
#  SKILLS TODAY:
#    - {key: value}             → create a dictionary
#    - dict[key]                → access a value
#    - dict[key] = value        → add or update an entry
#    - dict.items()             → loop through key-value pairs
#    - Nesting: dict inside dict, list inside dict
#    - for key, value in dict.items():
#
# ============================================================

print("Welcome to the secret auction program.")

bids = {}   # will store  { "Name": bid_amount, ... }

bidding_finished = False

# --------------------------------------------------
#  TODO 1: Collect bids in a loop
# --------------------------------------------------
# Ask: "What is your name?: "
# Ask: "What is your bid?: $"  (convert to int/float)
# Store in bids dict as  bids[name] = bid
# Ask: "Are there any other bidders? Type 'yes' or 'no': "
# If "no" → set bidding_finished = True to exit the loop
# If "yes" → clear the screen so bids stay secret
#   hint: print("\\n" * 20)

while not bidding_finished:
    pass  # TODO: replace with your bid-collection logic


# --------------------------------------------------
#  TODO 2: Find the winner
# --------------------------------------------------
# Write a function find_highest_bidder(bidding_record)
# It should:
#   - Loop through bidding_record.items()
#   - Track the highest bid and who made it
#   - Print "The winner is {name} with a bid of ${amount}"

def find_highest_bidder(bidding_record):
    pass  # TODO: implement

find_highest_bidder(bids)


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Store each bid as a dict itself:
#       bids[name] = {"bid": amount, "email": email}
#  2. Handle ties: what if two people bid the same highest amount?
#  3. Show a sorted leaderboard of all bids after the winner
# ============================================================
""")

days[10] = ("day 10", "calculator.py", """\
# ============================================================
#  DAY 10: Functions with Return Values
#  PROJECT: Calculator
# ============================================================
#
#  SKILLS TODAY:
#    - return value            → send a result back from a function
#    - Storing return values   → result = my_func()
#    - Functions as values     → storing functions in a dictionary
#    - Recursive-style loop    → using the result as next input
#
# ============================================================

# --------------------------------------------------
#  TODO 1: Write the four maths functions
# --------------------------------------------------
# Each takes two numbers (n1, n2) and RETURNS the result.
# Do NOT print inside them: just return.

def add(n1, n2):
    pass  # TODO: return n1 + n2

def subtract(n1, n2):
    pass  # TODO

def multiply(n1, n2):
    pass  # TODO

def divide(n1, n2):
    pass  # TODO: handle division by zero: return None or print a warning


# --------------------------------------------------
#  DEMO: Functions stored in a dictionary
# --------------------------------------------------
# This lets you look up which function to call based on user input.

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# --------------------------------------------------
#  TODO 2: Build the calculator loop
# --------------------------------------------------
# Start by asking for the first number (float)
# Show the available operations: + - * /
# Ask which operation to use
# Ask for the second number (float)
# Look up the function in the operations dict and CALL it
# Print the result: e.g.  "10.0 + 5.0 = 15.0"
# Ask: "Type 'y' to continue with result, 'n' for new calc, 'quit' to exit"
#   'y'    → use the result as the new first_number, loop again
#   'n'    → restart from scratch
#   'quit' → exit

def calculator():
    first_number = float(input("What's the first number?: "))
    should_accumulate = True

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        second_number    = float(input("What's the next number?: "))

        # TODO: get the right function from operations dict and call it
        answer = None

        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        # TODO: ask user what to do next and handle their choice

calculator()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add % (modulo) and ** (exponent) to the operations dict
#  2. Show a history of all calculations in the session
#  3. Add a memory function: store a result and recall it later
# ============================================================
""")

days[11] = ("day 11", "blackjack.py", """\
# ============================================================
#  DAY 11: Capstone Project
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

# Deck: infinite shoe (we just pick random cards each time)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# --------------------------------------------------
#  TODO 1: deal_card(): returns one random card from cards
# --------------------------------------------------
def deal_card():
    pass


# --------------------------------------------------
#  TODO 2: calculate_score(hand): returns the score
# --------------------------------------------------
# hand is a list of card values
# Sum them up
# If sum > 21 and 11 is in the hand → replace the 11 with a 1
# Special rule: if hand has exactly 2 cards and sums to 21 → return 0
#   (0 signals a natural Blackjack: unbeatable hand)

def calculate_score(hand):
    pass


# --------------------------------------------------
#  TODO 3: compare(user_score, computer_score): print winner
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
#  TODO 4: play_game(): the main game function
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
    print("\\n" * 20)
    play_game()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add betting: start with $100, wager before each hand
#  2. Add splitting (when you have two of the same card)
#  3. Add a "double down" option
# ============================================================
""")

days[12] = ("day 12", "number guessing game.py", """\
# ============================================================
#  DAY 12: Scope
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

# Global constant: lives per difficulty
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
#  TODO 3: game(): wire it all together
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
""")

days[13] = ("day 13", "debugging exercises.py", """\
# ============================================================
#  DAY 13: Debugging
#  PROJECT: Fix the Broken Code
# ============================================================
#
#  SKILLS TODAY:
#    - Reading error messages   → type, line number, message
#    - print() debugging        → add prints to see what's happening
#    - Describe the problem     → rubber duck debugging
#    - Reproduce the error      → find the minimal failing case
#    - Common errors:
#        NameError    → variable doesn't exist / misspelled
#        TypeError    → wrong type (e.g. adding str + int)
#        IndexError   → list index out of range
#        ValueError   → invalid value (e.g. int("hello"))
#        AttributeError → method doesn't exist on that type
#        IndentationError → wrong indentation
#        LogicError   → code runs but gives wrong answer
#
#  INSTRUCTIONS:
#    Each TODO below has broken code. Fix it. Don't just delete:
#    understand WHY it was broken first.
#
# ============================================================

# --------------------------------------------------
#  BUG 1: TypeError: add a debug print first, then fix
# --------------------------------------------------
age = input("What is your age? ")
# Bug: can't multiply a string by a float
# days_lived = age * 365
# TODO: fix the line above and print the result

# --------------------------------------------------
#  BUG 2: NameError: a variable is used before it's created
# --------------------------------------------------
# TODO: figure out what's wrong and fix it without removing lines
# score = 0
# for i in range(10):
#     soore += 1   ← spot the typo
# print(score)

# --------------------------------------------------
#  BUG 3: IndexError
# --------------------------------------------------
fruits = ["apple", "mango", "pear"]
# TODO: fix so it prints "pear" without changing the list
# print(fruits[3])

# --------------------------------------------------
#  BUG 4: Logic error: off-by-one in range
# --------------------------------------------------
# This should print 1 to 10 inclusive. Fix it.
# for i in range(1, 10):
#     print(i)

# --------------------------------------------------
#  BUG 5: Logic error: wrong condition
# --------------------------------------------------
# Should print "even" for even numbers, "odd" for odd.
# Fix the condition.
# number = 4
# if number % 2 = 0:   ← two bugs here
#     print("even")
# else
#     print("odd")

# --------------------------------------------------
#  BUG 6: Debugging a function: use print() to trace it
# --------------------------------------------------
# This should return the average of a list but always returns 0.
# Add print statements inside to find where it goes wrong, then fix it.
def average(numbers):
    total = 0
    for n in numbers:
        total == total + n   # bug here
    return total / len(numbers)

# Uncomment to test once you've fixed the function:
# print(average([4, 8, 15, 16, 23, 42]))   # should print 18.0


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Write your OWN buggy function and swap with a friend to fix
#  2. Look up Python's built-in debugger: import pdb; pdb.set_trace()
#  3. Try using your IDE's debugger to step through code line by line
# ============================================================
""")

days[14] = ("day 14", "higher lower game.py", """\
# ============================================================
#  DAY 14: Capstone: Beginner Phase
#  PROJECT: Higher or Lower (Instagram Follower Game)
# ============================================================
#
#  CAPSTONE: uses EVERYTHING from Days 1-13:
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

# Sample data: each entry: name, description, country, follower_count
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

logo = \"\"\"
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \\/ _ \\/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ /_/_/\\__, /_/ /_/\\___/_/  or
        /____/
 __
/ /  ______      _____ _ __
/ /  / _ \\ \\ /\\ / / _ \\ '__|
/ /__| (_) \\ V  V /  __/ |
\\____/\\___/ \\_/\\_/ \\___|_|
\"\"\"


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
#  TODO 3: game(): main game loop
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
#   Clear screen (print "\\n" * 20)
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
""")

# --- Now write all the files ---
base = "/home/user/100-days-of-skiubity"

for day_num, (folder, filename, content) in days.items():
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, filename)
    with open(filepath, "w") as f:
        f.write(content)
    print(f"Created: {folder}/{filename}")

print("Done: Days 4-14 written.")
