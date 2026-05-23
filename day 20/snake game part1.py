# ============================================================
#  DAY 20 — Snake Game Part 1
#  PROJECT: Snake Game (Animation & Coordinates)
# ============================================================
#
#  SKILLS TODAY:
#    - Creating a class with multiple objects (the snake body segments)
#    - turtle.Turtle() attributes: shape, color, penup, goto
#    - Animating with screen.tracer(0) + screen.update()
#    - Moving the snake: each segment copies the position of the one ahead
#    - turtle.Screen() / screen.bgcolor() / screen.title()
#    - time.sleep(0.1)  → controls speed
#
#  PLAN FOR TODAY (Part 1):
#    1. Create the screen
#    2. Create the Snake class that builds the initial 3-segment body
#    3. Move the snake: head moves in direction, each segment follows
#    4. Allow turning: UP, DOWN, LEFT, RIGHT arrow keys
#
# ============================================================

import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)   # turn off animation — we call screen.update() manually

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE      = 20
UP    =  90
DOWN  = 270
LEFT  = 180
RIGHT =  0


# --------------------------------------------------
#  TODO 1: Create the Snake class (put in snake.py ideally)
# --------------------------------------------------
# __init__:
#   self.segments = []
#   Call create_snake() to build 3 starting segments
#   self.head = self.segments[0]
#
# create_snake():
#   For each position in STARTING_POSITIONS:
#     create a square white turtle at that position
#     append to self.segments
#
# add_segment(position):
#   Create a new square white turtle at position
#   Append to self.segments
#
# move():
#   Move each segment (from tail to head) to the position of the one ahead:
#     for i in range(len-1, 0, -1):
#         segments[i].goto(segments[i-1].position())
#   Then move the head forward by MOVE_DISTANCE
#
# up() / down() / left() / right():
#   Change head's heading but DON'T allow 180° turns
#   (can't go right if currently going left, etc.)

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        pass  # TODO

    def move(self):
        pass  # TODO

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        pass  # TODO: same pattern, block UP

    def left(self):
        pass  # TODO: block RIGHT

    def right(self):
        pass  # TODO: block LEFT


snake = Snake()

# --------------------------------------------------
#  TODO 2: Bind arrow keys
# --------------------------------------------------
screen.listen()
# screen.onkey(snake.up, "Up")   ← bind all four directions

# --------------------------------------------------
#  Game loop
# --------------------------------------------------
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()

# ============================================================
#  STRETCH GOALS (save for Part 2)
# ============================================================
#  - Add food that the snake eats to grow
#  - Add collision detection (walls + self)
#  - Add a scoreboard
# ============================================================
