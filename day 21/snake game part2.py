# ============================================================
#  DAY 21: Snake Game Part 2
#  PROJECT: Snake Game (Inheritance, List Slicing, Collision)
# ============================================================
#
#  SKILLS TODAY:
#    - Class inheritance:  class Child(Parent):
#    - super().__init__()  → call the parent's constructor
#    - Overriding methods
#    - List slicing:  my_list[start:stop:step]
#    - Collision detection: distance() method on Turtle
#    - Writing classes in separate files and importing them
#
#  BUILD ON DAY 20: add these three classes:
#    Food      → extends Turtle, refreshes to random position
#    Scoreboard→ extends Turtle, displays + updates score
#    Then wire collision detection into the game loop
#
# ============================================================

import turtle
import time
import random

# Import your Day 20 Snake class (or paste it here)
# from snake import Snake

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


# --------------------------------------------------
#  TODO 1: Food class (inherits from Turtle)
# --------------------------------------------------
# __init__:
#   super().__init__()
#   self.shape("circle")
#   self.color("blue")
#   self.penup()
#   self.speed("fastest")
#   self.refresh()
#
# refresh():
#   Move to a random position within the screen
#   x = random.randint(-280, 280)
#   y = random.randint(-280, 280)

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        pass  # TODO

    def refresh(self):
        pass  # TODO


# --------------------------------------------------
#  TODO 2: Scoreboard class (inherits from Turtle)
# --------------------------------------------------
# __init__:
#   super().__init__()
#   self.score = 0
#   self.high_score = 0  (load from file if it exists)
#   Position at top of screen, white colour, no pen
#   Call update_scoreboard()
#
# update_scoreboard():
#   Clear old text
#   Write "Score: {score}  High Score: {high_score}" at top center
#
# increase_score():
#   self.score += 1
#   update_scoreboard()
#
# reset():
#   if score > high_score → update high_score, save to file
#   self.score = 0
#   update_scoreboard()

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score      = 0
        self.high_score = 0
        pass  # TODO: full init

    def update_scoreboard(self):
        pass

    def increase_score(self):
        pass

    def reset(self):
        pass


# --------------------------------------------------
#  TODO 3: Paste/import Snake from Day 20, add grow() method
# --------------------------------------------------
# grow(): add a new segment at the position of the current tail

# Instantiate
# snake      = Snake()
food       = Food()
scoreboard = Scoreboard()

screen.listen()
# bind keys...

# --------------------------------------------------
#  Game loop with collision detection
# --------------------------------------------------
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # snake.move()

    # TODO: Food collision
    # if snake.head.distance(food) < 15:
    #   food.refresh()
    #   snake.grow()
    #   scoreboard.increase_score()

    # TODO: Wall collision
    # if head x or y goes beyond ±290 → scoreboard.reset(), snake reset

    # TODO: Self collision
    # loop through segments[1:]: if head gets within 10 of any segment → reset

screen.exitonclick()
