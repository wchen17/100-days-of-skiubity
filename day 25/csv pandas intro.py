# ============================================================
#  DAY 25 — CSV Data & Pandas Introduction
#  PROJECT: States Game (US States Quiz)
# ============================================================
#
#  SKILLS TODAY:
#    - import pandas as pd         → data analysis library
#    - pd.read_csv("file.csv")     → load CSV into a DataFrame
#    - df.to_csv("file.csv")       → save DataFrame to CSV
#    - df["column"]                → get a column (Series)
#    - df[df["col"] == value]      → filter rows
#    - df.to_dict("records")       → list of row dicts
#    - Series.tolist()             → convert to plain list
#    - pip install pandas          → install if needed
#
# ============================================================

import pandas

# --------------------------------------------------
#  DEMO: Pandas basics
# --------------------------------------------------
df = pandas.read_csv("weather_data.csv")   # example file
# Create a sample CSV to practice with:
import io
sample_csv = """Day,Temp,Condition
Monday,28,Sunny
Tuesday,22,Cloudy
Wednesday,30,Sunny
Thursday,18,Rainy
Friday,25,Sunny"""

with open("weather_data.csv", "w") as f:
    f.write(sample_csv)

df = pandas.read_csv("weather_data.csv")
print(df)
print(df["Temp"])              # one column
print(df[df["Condition"] == "Sunny"])  # filter
print(df["Temp"].max())        # highest temp
print(df[df["Temp"] == df["Temp"].max()])  # row with highest temp


# --------------------------------------------------
#  PROJECT: States Game
# --------------------------------------------------
# Create a CSV of US state names + their x,y coordinates on a map image
# (a pre-made states CSV is available in the Angela Yu course files)
#
# For now, create a mini version with 5 states to practice the concepts:

import io
states_csv = """state,x,y
California,-120,37
Texas,-99,31
Florida,-82,27
New York,-74,43
Ohio,-83,40"""

with open("50_states.csv", "w") as f:
    f.write(states_csv)

df = pandas.read_csv("50_states.csv")
all_states = df["state"].tolist()
guessed_states = []


# --------------------------------------------------
#  TODO 1: Main game loop
# --------------------------------------------------
# While len(guessed_states) < len(all_states):
#   Prompt: "Guess a state (or type Exit): "
#   If "Exit":
#     Create a DataFrame of unguessed states and save as "states_to_learn.csv"
#     break
#   If answer in all_states and not already guessed:
#     Add to guessed_states
#     Print how many guessed so far
#   Else:
#     Print "Not a state" or "Already guessed"

# your loop here


# --------------------------------------------------
#  TODO 2: Save unguessed states to CSV
# --------------------------------------------------
# Filter df to rows where state NOT in guessed_states
# Save to "states_to_learn.csv" with df.to_csv(index=False)

# your code here


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Use turtle to display a US map image and plot guessed states
#     at their x,y coordinates
#  2. Load states_to_learn.csv on startup to continue from last session
#  3. Add a timer — how fast can you name all 50 states?
# ============================================================
