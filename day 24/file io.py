# ============================================================
#  DAY 24 — File I/O: Reading and Writing Files
#  PROJECT: Mail Merge Letter Generator
# ============================================================
#
#  SKILLS TODAY:
#    - open(path, mode)            → modes: "r", "w", "a", "r+"
#    - with open(...) as f:        → auto-closes the file
#    - f.read()                    → entire file as a string
#    - f.readlines()               → list of lines
#    - f.write(text)               → write to file
#    - f.writelines(list)          → write multiple lines
#    - Relative vs absolute paths
#    - os.path.join(), os.listdir(), os.makedirs()
#
# ============================================================

import os

# --------------------------------------------------
#  DEMO: Reading a file
# --------------------------------------------------
# Create a test file first, then read it back

with open("test.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")
    f.write("Line 3.")

with open("test.txt", "r") as f:
    contents = f.read()
    print(contents)

with open("test.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())   # .strip() removes the \n at the end


# --------------------------------------------------
#  TODO 1: Append to a file
# --------------------------------------------------
# Open "test.txt" in append mode and add two more lines
# Then read it back and print the whole thing

# your code here


# --------------------------------------------------
#  PROJECT: Mail Merge
# --------------------------------------------------
# You have:
#   - A file "letter_template.txt" with a placeholder [name]
#   - A file "invited_names.txt" with one name per line
#
# Goal: for each name, replace [name] in the template, then
#       save a personalised letter as "letters/letter_for_{name}.txt"

# Create sample files so you can test without external files
os.makedirs("letters", exist_ok=True)

with open("letter_template.txt", "w") as f:
    f.write("Dear [name],\n\nYou are invited to my party.\nPlease RSVP.\n\nCheers,\nYour Friend")

with open("invited_names.txt", "w") as f:
    f.write("Aang\nZuko\nKatara\nToph\nSokka")


# --------------------------------------------------
#  TODO 2: Mail Merge logic
# --------------------------------------------------
# 1. Read invited_names.txt → get a list of names
# 2. Read letter_template.txt → get the template string
# 3. For each name:
#      Replace "[name]" with the actual name
#      Write the personalised letter to letters/letter_for_{name}.txt

# your code here


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a second placeholder [date] and fill it in with today's date
#  2. Read the names from a CSV instead of plain text
#  3. Email each letter automatically using smtplib (preview of Day 32)
# ============================================================
