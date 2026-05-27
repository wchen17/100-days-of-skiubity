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
