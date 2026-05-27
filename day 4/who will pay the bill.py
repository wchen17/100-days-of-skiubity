# ============================================================
#  DAY 4 PRACTICE: Who Will Pay the Bill
# ============================================================
#  A warm-up for Rock Paper Scissors. Do this first.
#
#  TOOLS IN SCOPE: list, random.randint, len(), list[index]
#
#  BUILD: a group of friends are at dinner. Pick one at random to
#  pay the whole bill, fairly (everyone equally likely).
#
#  DONE WHEN:
#    - the chosen payer is random each run (run it a few times)
#    - it's fair for ANY number of names: use len(), don't hardcode
#      the range to 0-2 or whatever
#    - it announces who pays
#
#  The point: turning "a random person from an any-length list"
#  into code. That's the rep. No steps given.
# ============================================================

import random

# Boilerplate: read names and split into a list. Parsing isn't the lesson.
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

# Your code from here.
