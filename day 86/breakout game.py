# ============================================================
#  DAY 86: Portfolio Project
#  PROJECT: Breakout Game (Atari classic)
# ============================================================
#
#  SKILLS USED: Turtle, OOP, collision detection, game loop
#
#  COMPONENTS:
#    Paddle  → moves left/right with arrow keys
#    Ball    → bounces off walls and paddle, breaks bricks
#    Brick   → grid of coloured rectangles (use Turtle squares)
#    Scoreboard → tracks score and lives
#
# ============================================================

import turtle
import time
import random

screen = turtle.Screen()
screen.setup(600, 700)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

PADDLE_Y    = -280
BRICK_ROWS  = 5
BRICK_COLS  = 10
COLORS      = ["red", "orange", "yellow", "green", "blue"]


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, PADDLE_Y)

    def go_left(self):
        if self.xcor() > -220:
            self.setx(self.xcor() - 20)

    def go_right(self):
        if self.xcor() < 220:
            self.setx(self.xcor() + 20)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -100)
        self.dx = 3
        self.dy = 3

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_x(self): self.dx *= -1
    def bounce_y(self): self.dy *= -1
    def reset(self):    self.goto(0, -100); self.dy = abs(self.dy)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 310)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  Lives: {self.lives}", align="center", font=("Arial", 14, "normal"))

    def add_score(self):  self.score += 10; self.update()
    def lose_life(self):  self.lives -= 1; self.update(); return self.lives > 0
    def game_over(self, won):
        self.goto(0, 0)
        msg = "YOU WIN! 🎉" if won else "GAME OVER"
        self.write(msg, align="center", font=("Arial", 24, "bold"))


# --------------------------------------------------
#  TODO 1: Create the brick grid
# --------------------------------------------------
# For each row (0 to BRICK_ROWS-1):
#   colour = COLORS[row]
#   For each column (0 to BRICK_COLS-1):
#     Create a square Turtle, colour it, position it
#     x = -225 + col * 50; y = 200 - row * 30
# Store all bricks in a list

bricks = []
# your grid-building loop here


paddle     = Paddle()
ball       = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.go_left,  "Left")
screen.onkeypress(paddle.go_right, "Right")


# --------------------------------------------------
#  TODO 2: Game loop
# --------------------------------------------------
# Move the ball
# Wall collisions: left/right → bounce_x; top → bounce_y
# Bottom wall → lose life; if no lives left → game over
# Paddle collision → bounce_y (adjust y_move to be positive)
# Brick collision: loop through bricks, if distance < 20:
#   hide the brick, remove from list, bounce_y, add score
# If bricks is empty → YOU WIN

game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()
    # TODO: your collision and movement logic

screen.exitonclick()
