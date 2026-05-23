# ============================================================
#  DAY 26 — List & Dictionary Comprehension
#  PROJECT: NATO Phonetic Alphabet Converter
# ============================================================
#
#  SKILLS TODAY:
#    new_list = [expression for item in iterable]
#    filtered = [expr for item in iterable if condition]
#    new_dict = {key: value for item in iterable}
#    Squash multiple lines of append() into one line
#
# ============================================================

import pandas

# --------------------------------------------------
#  DEMO: List comprehension vs traditional loop
# --------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Old way:
squared = []
for n in numbers:
    squared.append(n ** 2)

# New way (list comprehension):
squared = [n ** 2 for n in numbers]
print(squared)

# With filter:
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)

# Dict comprehension:
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(word_lengths)


# --------------------------------------------------
#  TODO 1: Practice comprehensions
# --------------------------------------------------
# a) Make a list of all words in this sentence that are longer than 3 letters
sentence = "I am learning Python and it is really fun"
# long_words = [...]

# b) Make a dict mapping each number 1-10 to its cube
# cubes = {...}

# c) Filter a list to only the temperatures above 25
temps = [18, 22, 30, 15, 28, 33, 20]
# hot_days = [...]


# --------------------------------------------------
#  PROJECT: NATO Alphabet Converter
# --------------------------------------------------
# The NATO phonetic alphabet assigns a word to each letter:
# A → Alpha, B → Bravo, C → Charlie, ...

nato_csv = """letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
F,Foxtrot
G,Golf
H,Hotel
I,India
J,Juliett
K,Kilo
L,Lima
M,Mike
N,November
O,Oscar
P,Papa
Q,Quebec
R,Romeo
S,Sierra
T,Tango
U,Uniform
V,Victor
W,Whiskey
X,X-ray
Y,Yankee
Z,Zulu"""

with open("nato_phonetic_alphabet.csv", "w") as f:
    f.write(nato_csv)

df = pandas.read_csv("nato_phonetic_alphabet.csv")


# --------------------------------------------------
#  TODO 2: Build the nato_dict using dict comprehension
# --------------------------------------------------
# { row.letter: row.code for row in df.itertuples() }
# itertuples() gives you each row as a named tuple

nato_dict = {}  # TODO: use dict comprehension


# --------------------------------------------------
#  TODO 3: Convert user input to NATO
# --------------------------------------------------
# Loop until valid input:
#   Ask: "Enter a word: "
#   Convert to uppercase
#   Use a list comprehension to build output:
#     [nato_dict[letter] for letter in word]
#   Handle KeyError — if input has numbers/spaces, try/except or if/else

word = input("Enter a word: ").upper()
# your comprehension + output here


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Reverse it: given a NATO word, decode back to the letter
#  2. Convert an entire sentence, keeping spaces intact
#  3. Build a quiz: show the NATO word, ask the user for the letter
# ============================================================
