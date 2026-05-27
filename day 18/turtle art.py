# ============================================================
#  DAY 18: Turtle Graphics & GUIs
#  PROJECT: Hirst Painting (dot art) + Shapes
# ============================================================
#
#  SKILLS TODAY:
#    - import turtle              → graphical drawing library
#    - turtle.Turtle()            → create a turtle object
#    - t.forward(n) / t.backward(n)
#    - t.left(deg) / t.right(deg)
#    - t.penup() / t.pendown()    → lift/place the pen
#    - t.goto(x, y)               → move to coordinates
#    - t.color("colour name")
#    - t.dot(size, colour)
#    - t.speed("fastest")
#    - turtle.colormode(255)      → use RGB tuples instead of names
#    - turtle.Screen().exitonclick()
#
# ============================================================

import turtle
import random

t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()
screen = turtle.Screen()
screen.colormode(255)   # allows RGB tuples like (255, 0, 128)


# --------------------------------------------------
#  DEMO: Draw a square
# --------------------------------------------------
def draw_square(side=100):
    t.pendown()
    for _ in range(4):
        t.forward(side)
        t.right(90)
    t.penup()

draw_square()


# --------------------------------------------------
#  TODO 1: draw_dashed_line(length)
# --------------------------------------------------
# Use a loop: alternate pendown-forward(10) and penup-forward(10)
# Total length = length parameter

def draw_dashed_line(length):
    pass


# --------------------------------------------------
#  TODO 2: draw_shape(sides)
# --------------------------------------------------
# An n-sided regular polygon: exterior angle = 360 / sides
# Use turtle to draw it

def draw_shape(sides):
    angle = 360 / sides
    pass  # your loop here

for sides in range(3, 11):
    draw_shape(sides)


# --------------------------------------------------
#  TODO 3: Hirst-style dot painting
# --------------------------------------------------
# Create a colour list with at least 10 random RGB tuples
# Or use colorgram library: pip install colorgram.py
# Then draw a 10×10 grid of dots, each a random colour
#
# HINT for grid:
#   Start at (-200, -200) using t.goto
#   Nested loops: 10 rows × 10 columns
#   t.dot(20, random.choice(colour_list))
#   Move forward for next dot in row
#   At end of each row: goto start of next row (y += 50)

colour_list = [
    (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    for _ in range(20)
]

# your grid code here


screen.exitonclick()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Use the colorgram library to extract colours from a real image
#  2. Draw a spirograph using a loop + t.circle(radius)
#  3. Draw a turtle race: 6 turtles, each moves a random distance each turn
# ============================================================
