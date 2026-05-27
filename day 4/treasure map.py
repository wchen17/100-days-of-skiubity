# ============================================================
#  DAY 4 PRACTICE: Treasure Map
# ============================================================
#  A warm-up for Rock Paper Scissors. Tests nested lists.
#
#  TOOLS IN SCOPE: nested lists, list[row][col]
#
#  BUILD: a 3x3 map. The user gives a position like "B2".
#  Mark that spot with an "X".
#
#  DONE WHEN:
#    - "B2" places the X at the correct row and column
#      (pick a convention: letter = column, digit = row, or your
#       own, just be consistent and correct)
#    - printing the map shows the X in the right place
#
#  The trap: "B2" is a string. You turn the letter into a column
#  index and the digit into a row index. Off-by-one and row/col
#  swaps are the entire challenge.
# ============================================================

row1 = ["X1", "X2", "X3"]
row2 = ["Y1", "Y2", "Y3"]
row3 = ["Z1", "Z2", "Z3"]
game_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

# Your code from here.
