# ============================================================
#  DAY 22: Pong Game
#  PROJECT: Classic Pong (2-player)
# ============================================================
#
#  SKILLS TODAY:
#    - Multiple classes working together
#    - Controlling speed with ball.dx, ball.dy (direction vectors)
#    - Bouncing: reverse dx or dy on collision
#    - Paddle class, Ball class, Scoreboard class
#    - screen.onkeypress() vs screen.onkeyrelease() for smooth movement
#
#  PLAN:
#    Paddle class  → right paddle (W/S) and left paddle (Up/Down)
#    Ball class    → moves on its own, bounces off walls/paddles
#    Scoreboard    → tracks L and R score, updates display
#
# ============================================================

import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


# --------------------------------------------------
#  TODO 1: Paddle class
# --------------------------------------------------
# __init__(self, position):
#   Create a white rectangle turtle at the given (x, y) position
#   shape="square", shapesize(stretch_wid=5, stretch_len=1)
#
# go_up():    y += 20  (don't go above 250)
# go_down():  y -= 20  (don't go below -250)

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        pass  # TODO

    def go_up(self):
        pass

    def go_down(self):
        pass


# --------------------------------------------------
#  TODO 2: Ball class
# --------------------------------------------------
# __init__:
#   White circle, starts at centre, moves diagonally
#   self.x_move = 10
#   self.y_move = 10
#
# move():
#   self.goto(xcor() + x_move, ycor() + y_move)
#
# bounce_y():  y_move *= -1   (hit top/bottom wall)
# bounce_x():  x_move *= -1   (hit paddle or miss = point scored)
# reset_position():  back to (0,0), reverse x_move for next serve

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        pass  # TODO

    def move(self):
        pass

    def bounce_y(self):
        pass

    def bounce_x(self):
        pass

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


# --------------------------------------------------
#  TODO 3: Scoreboard class
# --------------------------------------------------
# Tracks l_score and r_score
# update_scoreboard() → clear and rewrite at top of screen

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        pass

    def update_scoreboard(self):
        pass

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


r_paddle   = Paddle((350, 0))
l_paddle   = Paddle((-350, 0))
ball       = Ball()
scoreboard = Scoreboard()

screen.listen()
# TODO: bind W/S for right paddle, Up/Down for left paddle

# --------------------------------------------------
#  Game loop
# --------------------------------------------------
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO: Detect collision with top/bottom walls → bounce_y()
    # TODO: Detect collision with paddles → bounce_x(), speed up ball
    # TODO: Detect when ball goes past left/right edge → award point, reset

screen.exitonclick()
