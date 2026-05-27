# ============================================================
#  DAY 23: Capstone: Turtle Crossing Game
#  PROJECT: Frogger-style road crossing game
# ============================================================
#
#  SKILLS TODAY:
#    - Combining all OOP skills: multiple classes, inheritance
#    - Increasing difficulty over time
#    - Level system
#    - Collision detection with multiple objects
#
#  CLASSES TO BUILD:
#    Player     → turtle that moves Up only (W key)
#    CarManager → creates cars, moves them, speeds up each level
#    Scoreboard → shows level, game over message
#
# ============================================================

import turtle
import time
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

STARTING_POSITION = (0, -280)
MOVE_DISTANCE     = 10
FINISH_LINE_Y     = 280
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


# --------------------------------------------------
#  TODO 1: Player class
# --------------------------------------------------
# Starts at STARTING_POSITION, facing North (heading 90)
# go_up() → move forward MOVE_DISTANCE
# If ycor() > FINISH_LINE_Y → return True (reached finish)

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        pass

    def go_up(self):
        pass

    def is_at_finish_line(self):
        pass

    def go_to_start(self):
        self.goto(STARTING_POSITION)


# --------------------------------------------------
#  TODO 2: CarManager class
# --------------------------------------------------
# self.all_cars = []
# self.car_speed = 5
#
# create_car():
#   10% chance each frame to create a new car
#   random y position (between -250 and 250, snapped to lanes)
#   random colour, speed = car_speed
#   Start at x = 300 (off right edge), move LEFT
#
# move_cars():
#   Move every car left by car_speed
#   Remove cars that go off the left edge (x < -320)
#
# level_up():
#   car_speed += 5

class CarManager:
    def __init__(self):
        self.all_cars  = []
        self.car_speed = 5

    def create_car(self):
        pass

    def move_cars(self):
        pass

    def level_up(self):
        self.car_speed += 5


# --------------------------------------------------
#  TODO 3: Scoreboard class
# --------------------------------------------------
# Show "Level: X" at top left
# level_up() → increment level, update display
# game_over() → write "GAME OVER" in red in the centre

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        pass

    def update_scoreboard(self):
        pass

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        pass


player     = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

# --------------------------------------------------
#  Game loop
# --------------------------------------------------
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # TODO: Check if player reached finish line
    # → player.go_to_start(), car_manager.level_up(), scoreboard.level_up()

    # TODO: Check collision with any car (distance < 20)
    # → scoreboard.game_over(), game_is_on = False

screen.exitonclick()
