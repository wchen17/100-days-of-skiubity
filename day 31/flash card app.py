# ============================================================
#  DAY 31: Capstone: Intermediate Phase
#  PROJECT: Flash Card Language Learning App
# ============================================================
#
#  CAPSTONE: everything from days 15-30:
#    OOP, Tkinter, pandas, JSON, file I/O, try/except
#
#  HOW IT WORKS:
#    - Show a French word on the front of a card
#    - After 3 seconds, flip to show the English translation
#    - ✓ button → you knew it → remove from practice list
#    - ✗ button → you didn't → keep it in
#    - Save remaining words to a file so progress persists
#
# ============================================================

import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# --------------------------------------------------
#  TODO 1: Load the word list
# --------------------------------------------------
# Try to read "words_to_learn.csv" (the user's remaining cards)
# Except FileNotFoundError → read the original "french_words.csv"
# Store as a list of dicts: to_learn
#
# Create a sample CSV if you don't have the course files:
sample = "French,English\nBien,Well\nBonjour,Hello\nMerci,Thank you\nOui,Yes\nNon,No\nChat,Cat\nChien,Dog\nMaison,House\nVoiture,Car\nEau,Water"
with open("french_words.csv", "w") as f:
    f.write(sample)

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# --------------------------------------------------
#  TODO 2: next_card()
# --------------------------------------------------
# Pick a random card from to_learn → current_card
# Cancel any pending flip timer (window.after_cancel)
# Show FRONT of card: canvas background = "#B1DDC6"
#   Title text = "French", word text = current_card["French"]
# Set a timer: window.after(3000, flip_card)

flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # TODO: update canvas texts and start flip timer


# --------------------------------------------------
#  TODO 3: flip_card()
# --------------------------------------------------
# Show BACK of card: canvas background = "#2d2d2d" (dark)
#   Title text = "English", word text = current_card["English"]

def flip_card():
    pass


# --------------------------------------------------
#  TODO 4: is_known()
# --------------------------------------------------
# Remove current_card from to_learn
# Save remaining to "words_to_learn.csv" using pandas DataFrame
# Call next_card()

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


# --------------------------------------------------
#  UI Setup
# --------------------------------------------------
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Ideally: load card_front.png / card_back.png images for the card design
# Fallback rectangle:
canvas.create_rectangle(50, 50, 750, 476, fill="white", outline="")
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word  = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = tk.Button(text="✗ Don't Know", bg="red",    fg="white", command=next_card)
right_button = tk.Button(text="✓ Know It",    bg="green",  fg="white", command=is_known)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_card()   # show first card on startup
window.mainloop()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add more languages: load a different CSV based on user choice
#  2. Show a progress bar (words learned / total words)
#  3. Add a "hard mode" where you type the translation instead of clicking
# ============================================================
