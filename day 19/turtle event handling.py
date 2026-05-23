# ============================================================
#  DAY 19 — Higher Order Functions & Event Listeners
#  PROJECT: Turtle Etch-A-Sketch + Turtle Race
# ============================================================
#
#  SKILLS TODAY:
#    - Higher order functions   → passing a function as an argument
#    - screen.listen()          → activate keyboard listening
#    - screen.onkey(func, key)  → call func when key is pressed
#    - screen.onkeypress(func, key)
#    - State in objects         → track score/position in a class
#
# ============================================================

import turtle
import random

# ==============================
#  PART A: Etch-A-Sketch
# ==============================

screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()

# --------------------------------------------------
#  TODO 1: Define movement functions
# --------------------------------------------------
# move_forward()  → t.forward(10)
# move_backward() → t.backward(10)
# turn_left()     → t.left(10)
# turn_right()    → t.right(10)
# clear_drawing() → t.reset()

def move_forward():
    pass

def move_backward():
    pass

def turn_left():
    pass

def turn_right():
    pass

def clear_drawing():
    pass


# --------------------------------------------------
#  TODO 2: Bind keys using screen.onkey()
# --------------------------------------------------
# W → forward, S → backward, A → left, D → right
# C → clear

screen.listen()
# screen.onkey(move_forward, "w")  ← example, bind the rest


# ==============================
#  PART B: Turtle Race
# ==============================

screen2 = turtle.Screen()
screen2.setup(width=500, height=400)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

# --------------------------------------------------
#  TODO 3: Set up 6 turtles in a vertical line on the left side
# --------------------------------------------------
# Create 6 Turtle objects, each a different colour
# Position them at x=-230, y starting from -100, spacing 40 apart
# Each turtle.shape("turtle") looks nice

racers = []
# your setup code here

# --------------------------------------------------
#  TODO 4: Run the race
# --------------------------------------------------
# Ask user: "Which turtle will win? Enter a colour: "
# user_bet = input(...)
# Loop until one turtle crosses x=230:
#   Each turtle moves forward a random distance (1-10)
# Print who won and whether the user bet correctly

is_race_on = True
while is_race_on:
    for racer in racers:
        # TODO: move each racer a random distance
        # TODO: check if racer has crossed the finish line
        pass

screen.exitonclick()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a speedometer that shows how fast each turtle moved overall
#  2. Let the user bet money on the race
#  3. Add obstacles that slow turtles down
# ============================================================
