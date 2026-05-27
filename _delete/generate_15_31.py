import os

base = "/home/user/100-days-of-skiubity"

files = {}

files["day 15/coffee machine.py"] = """\
# ============================================================
#  DAY 15: Local Dev Environment & Procedural Programming
#  PROJECT: Coffee Machine (procedural version)
# ============================================================
#
#  SKILLS TODAY:
#    - Running Python locally (not in a browser REPL)
#    - Breaking a big problem into small functions
#    - Nested dictionaries as a data store
#    - while True / break pattern for a menu loop
#
#  MACHINE RESOURCES:
#    water (ml), milk (ml), coffee (g), money ($)
#
#  DRINKS MENU:
#    espresso  → 50ml water, 0ml milk, 18g coffee  → $1.50
#    latte     → 200ml water, 150ml milk, 24g coffee → $2.50
#    cappuccino→ 250ml water, 100ml milk, 24g coffee → $3.00
#
# ============================================================

MENU = {
    "espresso": {"ingredients": {"water": 50,  "milk": 0,   "coffee": 18}, "cost": 1.50},
    "latte":    {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.50},
    "cappuccino":{"ingredients":{"water": 250, "milk": 100, "coffee": 24}, "cost": 3.00},
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


# --------------------------------------------------
#  TODO 1: is_resource_sufficient(order_ingredients)
# --------------------------------------------------
# Loop through each ingredient in order_ingredients
# If resources[ingredient] < order_ingredients[ingredient]:
#   print "Sorry there is not enough {ingredient}."
#   return False
# return True

def is_resource_sufficient(order_ingredients):
    pass


# --------------------------------------------------
#  TODO 2: process_coins() → returns total value inserted
# --------------------------------------------------
# Ask how many quarters (0.25), dimes (0.10), nickles (0.05), pennies (0.01)
# Return total as a float

def process_coins():
    print("Please insert coins.")
    pass


# --------------------------------------------------
#  TODO 3: is_transaction_successful(money_received, drink_cost)
# --------------------------------------------------
# If money_received >= drink_cost:
#   add profit to resources["money"]
#   calculate change and print it
#   return True
# Else:
#   print "Sorry that's not enough money. Money refunded."
#   return False

def is_transaction_successful(money_received, drink_cost):
    pass


# --------------------------------------------------
#  TODO 4: make_coffee(drink_name, order_ingredients)
# --------------------------------------------------
# Deduct each ingredient from resources
# Print "Here is your {drink_name} ☕. Enjoy!"

def make_coffee(drink_name, order_ingredients):
    pass


# --------------------------------------------------
#  TODO 5: Main loop
# --------------------------------------------------
# Print "What would you like? (espresso/latte/cappuccino): "
# If "report" → print current resources
# If "off"    → break (turn off the machine)
# Otherwise:
#   get drink from MENU
#   check resources → if not sufficient, loop again
#   process coins
#   check transaction → if not enough, loop again
#   make the coffee

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    pass  # TODO: handle choice


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Rewrite this tomorrow as a CoffeeMachine class (Day 16!)
#  2. Save the money total to a file so it persists between runs
#  3. Add a maintenance mode that refills resources
# ============================================================
"""

files["day 16/oop intro.py"] = """\
# ============================================================
#  DAY 16: Object-Oriented Programming
#  PROJECT: OOP Concepts + Coffee Machine (OOP version begins)
# ============================================================
#
#  SKILLS TODAY:
#    - class ClassName:           → blueprint for objects
#    - def __init__(self, ...):   → constructor / setup
#    - self.attribute = value     → instance attribute
#    - def method(self):          → function belonging to the class
#    - object = ClassName(args)   → create an instance
#    - object.attribute           → access attribute
#    - object.method()            → call a method
#
#  KEY IDEA:
#    A class bundles DATA (attributes) and BEHAVIOUR (methods) together.
#    Every object made from the class gets its own copy of the data.
#
# ============================================================

# --------------------------------------------------
#  DEMO 1: A simple class
# --------------------------------------------------
class Dog:
    # __init__ runs automatically when you create a Dog object
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age  = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")

# Create instances
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

dog1.bark()
dog2.birthday()
print(dog1.age)   # 3: dog1 is unaffected by dog2's birthday


# --------------------------------------------------
#  TODO 1: Create a Car class
# --------------------------------------------------
# Attributes:  make, model, year, speed (starts at 0)
# Methods:
#   accelerate(amount) → increase speed by amount, print new speed
#   brake(amount)      → decrease speed by amount (don't go below 0)
#   describe()         → print "{year} {make} {model}"

class Car:
    def __init__(self, make, model, year):
        pass  # TODO: set up attributes

    def accelerate(self, amount):
        pass

    def brake(self, amount):
        pass

    def describe(self):
        pass

# Test your Car:
my_car = Car("Toyota", "Supra", 1998)
my_car.describe()
my_car.accelerate(30)
my_car.accelerate(20)
my_car.brake(10)


# --------------------------------------------------
#  TODO 2: Create a BankAccount class
# --------------------------------------------------
# Attributes: owner (str), balance (float, default 0)
# Methods:
#   deposit(amount)    → add to balance, print new balance
#   withdraw(amount)   → subtract if funds available, else print error
#   get_balance()      → print "Balance: ${balance}"

class BankAccount:
    def __init__(self, owner, balance=0):
        pass

# Test:
account = BankAccount("Wendy", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)   # should print an error
account.get_balance()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a transfer(amount, other_account) method to BankAccount
#  2. Add a __str__ method to both classes so print(obj) shows something nice
#  3. Rewrite your Day 15 coffee machine using a CoffeeMachine class
# ============================================================
"""

files["day 17/quiz project/quiz brain.py"] = """\
# ============================================================
#  DAY 17: OOP: The Quiz Project
#  PROJECT: True/False Quiz Game (multi-file OOP)
# ============================================================
#
#  SKILLS TODAY:
#    - Splitting code across multiple files (modules)
#    - Creating objects from a class defined elsewhere
#    - Class attributes vs instance attributes
#    - Building an object list: [Class(data) for data in dataset]
#    - Type hints (optional but good habit): def method(self) -> bool:
#
#  FILES IN THIS PROJECT:
#    question_model.py  → Question class
#    data.py            → question bank (list of dicts)
#    quiz_brain.py      → QuizBrain class  (THIS FILE)
#    main.py            → entry point
#
# ============================================================

# This is quiz_brain.py
# QuizBrain drives the quiz: tracks score, asks questions, checks answers.

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score           = 0
        self.question_list   = q_list  # list of Question objects

    # --------------------------------------------------
    #  TODO 1: still_has_questions() → bool
    # --------------------------------------------------
    # Return True if question_number < len(question_list)

    def still_has_questions(self):
        pass

    # --------------------------------------------------
    #  TODO 2: next_question()
    # --------------------------------------------------
    # Get the current Question object from question_list
    # Increment question_number
    # Ask: "Q{number}: {question.text} (True/False): "
    # Call check_answer() with the user's input

    def next_question(self):
        pass

    # --------------------------------------------------
    #  TODO 3: check_answer(user_answer, correct_answer)
    # --------------------------------------------------
    # Compare (case-insensitive)
    # If correct → score += 1, print "You got it!"
    # Else       → print "That's wrong."
    # Always print: "The correct answer was: {correct_answer}"
    # Always print: "Your current score is: {score}/{question_number}"

    def check_answer(self, user_answer, correct_answer):
        pass
"""

files["day 17/quiz project/question model.py"] = """\
# question_model.py

class Question:
    def __init__(self, q_text, q_answer):
        self.text   = q_text
        self.answer = q_answer
"""

files["day 17/quiz project/data.py"] = """\
# data.py: question bank
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of two human lungs is approximately 70 square metres.", "answer": "True"},
    {"text": "In West Virginia, USA, it is legal to take a bear to school.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are technically entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A group of ferrets is called a business.", "answer": "True"},
]
"""

files["day 17/quiz project/main.py"] = """\
# main.py: run this file to play the quiz

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# --------------------------------------------------
#  TODO: Build the question bank
# --------------------------------------------------
# Loop through question_data
# Create a Question object for each dict: Question(item["text"], item["answer"])
# Append each to question_bank list

question_bank = []
# your list-building loop here

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
"""

files["day 18/turtle art.py"] = """\
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
"""

files["day 19/turtle event handling.py"] = """\
# ============================================================
#  DAY 19: Higher Order Functions & Event Listeners
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
"""

files["day 20/snake game part1.py"] = """\
# ============================================================
#  DAY 20: Snake Game Part 1
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
screen.tracer(0)   # turn off animation: we call screen.update() manually

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
"""

files["day 21/snake game part2.py"] = """\
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
"""

files["day 22/pong game.py"] = """\
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
"""

files["day 23/turtle crossing.py"] = """\
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
"""

files["day 24/file io.py"] = """\
# ============================================================
#  DAY 24: File I/O: Reading and Writing Files
#  PROJECT: Mail Merge Letter Generator
# ============================================================
#
#  SKILLS TODAY:
#    - open(path, mode)            → modes: "r", "w", "a", "r+"
#    - with open(...) as f:        → auto-closes the file
#    - f.read()                    → entire file as a string
#    - f.readlines()               → list of lines
#    - f.write(text)               → write to file
#    - f.writelines(list)          → write multiple lines
#    - Relative vs absolute paths
#    - os.path.join(), os.listdir(), os.makedirs()
#
# ============================================================

import os

# --------------------------------------------------
#  DEMO: Reading a file
# --------------------------------------------------
# Create a test file first, then read it back

with open("test.txt", "w") as f:
    f.write("Hello, World!\\n")
    f.write("This is a test file.\\n")
    f.write("Line 3.")

with open("test.txt", "r") as f:
    contents = f.read()
    print(contents)

with open("test.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())   # .strip() removes the \\n at the end


# --------------------------------------------------
#  TODO 1: Append to a file
# --------------------------------------------------
# Open "test.txt" in append mode and add two more lines
# Then read it back and print the whole thing

# your code here


# --------------------------------------------------
#  PROJECT: Mail Merge
# --------------------------------------------------
# You have:
#   - A file "letter_template.txt" with a placeholder [name]
#   - A file "invited_names.txt" with one name per line
#
# Goal: for each name, replace [name] in the template, then
#       save a personalised letter as "letters/letter_for_{name}.txt"

# Create sample files so you can test without external files
os.makedirs("letters", exist_ok=True)

with open("letter_template.txt", "w") as f:
    f.write("Dear [name],\\n\\nYou are invited to my party.\\nPlease RSVP.\\n\\nCheers,\\nYour Friend")

with open("invited_names.txt", "w") as f:
    f.write("Aang\\nZuko\\nKatara\\nToph\\nSokka")


# --------------------------------------------------
#  TODO 2: Mail Merge logic
# --------------------------------------------------
# 1. Read invited_names.txt → get a list of names
# 2. Read letter_template.txt → get the template string
# 3. For each name:
#      Replace "[name]" with the actual name
#      Write the personalised letter to letters/letter_for_{name}.txt

# your code here


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a second placeholder [date] and fill it in with today's date
#  2. Read the names from a CSV instead of plain text
#  3. Email each letter automatically using smtplib (preview of Day 32)
# ============================================================
"""

files["day 25/csv pandas intro.py"] = """\
# ============================================================
#  DAY 25: CSV Data & Pandas Introduction
#  PROJECT: States Game (US States Quiz)
# ============================================================
#
#  SKILLS TODAY:
#    - import pandas as pd         → data analysis library
#    - pd.read_csv("file.csv")     → load CSV into a DataFrame
#    - df.to_csv("file.csv")       → save DataFrame to CSV
#    - df["column"]                → get a column (Series)
#    - df[df["col"] == value]      → filter rows
#    - df.to_dict("records")       → list of row dicts
#    - Series.tolist()             → convert to plain list
#    - pip install pandas          → install if needed
#
# ============================================================

import pandas

# --------------------------------------------------
#  DEMO: Pandas basics
# --------------------------------------------------
df = pandas.read_csv("weather_data.csv")   # example file
# Create a sample CSV to practice with:
import io
sample_csv = \"\"\"Day,Temp,Condition
Monday,28,Sunny
Tuesday,22,Cloudy
Wednesday,30,Sunny
Thursday,18,Rainy
Friday,25,Sunny\"\"\"

with open("weather_data.csv", "w") as f:
    f.write(sample_csv)

df = pandas.read_csv("weather_data.csv")
print(df)
print(df["Temp"])              # one column
print(df[df["Condition"] == "Sunny"])  # filter
print(df["Temp"].max())        # highest temp
print(df[df["Temp"] == df["Temp"].max()])  # row with highest temp


# --------------------------------------------------
#  PROJECT: States Game
# --------------------------------------------------
# Create a CSV of US state names + their x,y coordinates on a map image
# (a pre-made states CSV is available in the Angela Yu course files)
#
# For now, create a mini version with 5 states to practice the concepts:

import io
states_csv = \"\"\"state,x,y
California,-120,37
Texas,-99,31
Florida,-82,27
New York,-74,43
Ohio,-83,40\"\"\"

with open("50_states.csv", "w") as f:
    f.write(states_csv)

df = pandas.read_csv("50_states.csv")
all_states = df["state"].tolist()
guessed_states = []


# --------------------------------------------------
#  TODO 1: Main game loop
# --------------------------------------------------
# While len(guessed_states) < len(all_states):
#   Prompt: "Guess a state (or type Exit): "
#   If "Exit":
#     Create a DataFrame of unguessed states and save as "states_to_learn.csv"
#     break
#   If answer in all_states and not already guessed:
#     Add to guessed_states
#     Print how many guessed so far
#   Else:
#     Print "Not a state" or "Already guessed"

# your loop here


# --------------------------------------------------
#  TODO 2: Save unguessed states to CSV
# --------------------------------------------------
# Filter df to rows where state NOT in guessed_states
# Save to "states_to_learn.csv" with df.to_csv(index=False)

# your code here


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Use turtle to display a US map image and plot guessed states
#     at their x,y coordinates
#  2. Load states_to_learn.csv on startup to continue from last session
#  3. Add a timer: how fast can you name all 50 states?
# ============================================================
"""

files["day 26/list comprehension.py"] = """\
# ============================================================
#  DAY 26: List & Dictionary Comprehension
#  PROJECT: NATO Phonetic Alphabet Converter
# ============================================================
#
#  SKILLS TODAY:
#    new_list = [expression for item in iterable]
#    filtered = [expr for item in iterable if condition]
#    new_dict = {key: value for item in iterable}
#    Squash multiple lines of append() into one line
#
# ============================================================

import pandas

# --------------------------------------------------
#  DEMO: List comprehension vs traditional loop
# --------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Old way:
squared = []
for n in numbers:
    squared.append(n ** 2)

# New way (list comprehension):
squared = [n ** 2 for n in numbers]
print(squared)

# With filter:
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print(even_squares)

# Dict comprehension:
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(word_lengths)


# --------------------------------------------------
#  TODO 1: Practice comprehensions
# --------------------------------------------------
# a) Make a list of all words in this sentence that are longer than 3 letters
sentence = "I am learning Python and it is really fun"
# long_words = [...]

# b) Make a dict mapping each number 1-10 to its cube
# cubes = {...}

# c) Filter a list to only the temperatures above 25
temps = [18, 22, 30, 15, 28, 33, 20]
# hot_days = [...]


# --------------------------------------------------
#  PROJECT: NATO Alphabet Converter
# --------------------------------------------------
# The NATO phonetic alphabet assigns a word to each letter:
# A → Alpha, B → Bravo, C → Charlie, ...

nato_csv = \"\"\"letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
F,Foxtrot
G,Golf
H,Hotel
I,India
J,Juliett
K,Kilo
L,Lima
M,Mike
N,November
O,Oscar
P,Papa
Q,Quebec
R,Romeo
S,Sierra
T,Tango
U,Uniform
V,Victor
W,Whiskey
X,X-ray
Y,Yankee
Z,Zulu\"\"\"

with open("nato_phonetic_alphabet.csv", "w") as f:
    f.write(nato_csv)

df = pandas.read_csv("nato_phonetic_alphabet.csv")


# --------------------------------------------------
#  TODO 2: Build the nato_dict using dict comprehension
# --------------------------------------------------
# { row.letter: row.code for row in df.itertuples() }
# itertuples() gives you each row as a named tuple

nato_dict = {}  # TODO: use dict comprehension


# --------------------------------------------------
#  TODO 3: Convert user input to NATO
# --------------------------------------------------
# Loop until valid input:
#   Ask: "Enter a word: "
#   Convert to uppercase
#   Use a list comprehension to build output:
#     [nato_dict[letter] for letter in word]
#   Handle KeyError: if input has numbers/spaces, try/except or if/else

word = input("Enter a word: ").upper()
# your comprehension + output here


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Reverse it: given a NATO word, decode back to the letter
#  2. Convert an entire sentence, keeping spaces intact
#  3. Build a quiz: show the NATO word, ask the user for the letter
# ============================================================
"""

files["day 27/tkinter miles km.py"] = """\
# ============================================================
#  DAY 27: Tkinter GUI & Layout
#  PROJECT: Miles-to-Kilometres Converter
# ============================================================
#
#  SKILLS TODAY:
#    - import tkinter as tk       → GUI library
#    - tk.Tk()                    → create the main window
#    - tk.Label(window, text="")  → display text
#    - tk.Entry(window)           → text input field
#    - tk.Button(window, text="", command=func)
#    - widget.grid(row, column, padx, pady)
#    - widget.get()               → read Entry value
#    - widget.config(text="")     → update a label's text
#    - window.mainloop()          → start the event loop
#    - *args and **kwargs         → flexible arguments
#
# ============================================================

import tkinter as tk

# --------------------------------------------------
#  DEMO: Minimal Tkinter window
# --------------------------------------------------
# window = tk.Tk()
# window.title("My App")
# my_label = tk.Label(text="Hello, Tkinter!")
# my_label.pack()
# window.mainloop()


# --------------------------------------------------
#  PROJECT: Miles → Km Converter
# --------------------------------------------------
# Layout:
#   Row 0: [Entry field]  "Miles"
#   Row 1: "is equal to"  [Result label]  "Km"
#   Row 2:                [Calculate button]

def miles_to_km():
    # --------------------------------------------------
    #  TODO: Read miles from entry, convert, update result label
    # --------------------------------------------------
    # miles = float(miles_input.get())
    # km    = miles * 1.60934
    # km_result_label.config(text=f"{km:.2f}")
    pass


window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Miles input
miles_input = tk.Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

# "is equal to" label
equal_label = tk.Label(text="is equal to")
equal_label.grid(row=1, column=0)

# Result label
km_result_label = tk.Label(text=0)
km_result_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

# Calculate button
calc_button = tk.Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a reverse converter (Km → Miles)
#  2. Add a dropdown to choose the unit type:
#     Miles/Km, Celsius/Fahrenheit, Kg/Lbs
#  3. Style it with background colours and fonts:
#     tk.Label(bg="#1e1e2e", fg="white", font=("Arial", 14))
# ============================================================
"""

files["day 28/pomodoro timer.py"] = """\
# ============================================================
#  DAY 28: Tkinter + Dynamic Typing
#  PROJECT: Pomodoro Focus Timer
# ============================================================
#
#  SKILLS TODAY:
#    - tk.Canvas             → draw shapes and images
#    - canvas.create_image() → place a photo on canvas
#    - canvas.create_text()  → draw text on canvas
#    - canvas.itemconfig()   → update canvas items dynamically
#    - window.after(ms, func)→ call func after ms milliseconds
#    - Math: convert seconds to mm:ss display
#
#  POMODORO TECHNIQUE:
#    25 min work → 5 min short break → repeat
#    After 4 rounds → 20 min long break
#
# ============================================================

import tkinter as tk
import math

PINK  = "#e2979c"
RED   = "#e7305b"
GREEN = "#9bdeac"
YELLOW= "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN  = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN  = 20

reps   = 0
timer  = None   # will hold the "after" callback reference


# --------------------------------------------------
#  TODO 1: reset_timer()
# --------------------------------------------------
# Cancel the pending after() call:  window.after_cancel(timer)
# Reset canvas timer text to "00:00"
# Reset title label to "Timer"
# Reset check marks label to ""
# Reset reps to 0

def reset_timer():
    pass


# --------------------------------------------------
#  TODO 2: start_timer()
# --------------------------------------------------
# Increment reps
# Calculate work_sec, short_break_sec, long_break_sec
#
# if reps % 8 == 0  → long break
# elif reps % 2 == 0 → short break
# else               → work session
#
# Update the title label colour (GREEN for work, PINK for short, RED for long)
# Call count_down(seconds)

def start_timer():
    global reps
    reps += 1
    # TODO: determine session type and duration


# --------------------------------------------------
#  TODO 3: count_down(count)
# --------------------------------------------------
# count = total seconds remaining
# Display as mm:ss:
#   count_min = math.floor(count / 60)
#   count_sec = count % 60
#   if count_sec < 10: count_sec = f"0{count_sec}"
#
# Update the canvas timer text
#
# If count > 0:
#   global timer = window.after(1000, count_down, count - 1)
# Else:
#   start_timer() again (next session)
#   Add a ✔ check mark for each completed work session

def count_down(count):
    pass


# --------------------------------------------------
#  UI Setup
# --------------------------------------------------
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)

# Canvas with tomato image (optional: use a placeholder rectangle if no image)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = tk.PhotoImage(file="tomato.png")   # uncomment if you have the image
# canvas.create_image(100, 112, image=tomato_img)
canvas.create_rectangle(20, 20, 180, 200, fill=RED, outline="")  # placeholder
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button  = tk.Button(text="Start",  highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button  = tk.Button(text="Reset",  highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = tk.Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Play a sound when a session ends (use playsound or winsound)
#  2. Show a desktop notification
#  3. Let the user configure work/break durations in the UI
# ============================================================
"""

files["day 29/password manager.py"] = """\
# ============================================================
#  DAY 29: Tkinter App: Password Manager
#  PROJECT: Password Manager with File Storage
# ============================================================
#
#  SKILLS TODAY:
#    - tkinter messagebox         → popup dialogs
#    - pyperclip                  → copy text to clipboard
#    - File append ("a" mode)     → save passwords to a file
#    - Entry.delete(0, END)       → clear an input field
#    - PhotoImage                 → display a logo
#    - Generating random passwords (reuse Day 5 logic)
#
#  pip install pyperclip
#
# ============================================================

import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
import string


# --------------------------------------------------
#  TODO 1: generate_password()
# --------------------------------------------------
# Build a random strong password (letters + numbers + symbols)
# Insert it into the password_entry field
# Copy it to clipboard with pyperclip.copy(password)

def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols)  for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers)  for _ in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# --------------------------------------------------
#  TODO 2: save()
# --------------------------------------------------
# Get website, email, password from entries
# If any field is empty → show messagebox.showwarning(...)
# Otherwise:
#   Show messagebox.askokcancel() with details to confirm
#   If OK:
#     Append to "data.txt" in format:  website | email | password\\n
#     Clear website and password fields
#     Focus cursor back on website field

def save():
    website  = website_entry.get()
    email    = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \\nEmail: {email} \\nPassword: {password} \\nIs it ok to save?"
    )

    if is_ok:
        pass  # TODO: write to file, clear fields


# --------------------------------------------------
#  UI Setup
# --------------------------------------------------
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo placeholder (replace with canvas + image if you have the file)
canvas = tk.Canvas(height=200, width=200)
canvas.create_rectangle(0, 0, 200, 200, fill="#4a90d9")
canvas.create_text(100, 100, text="🔐", font=("Arial", 60))
canvas.grid(row=0, column=1)

# Website row
tk.Label(text="Website:").grid(row=1, column=0)
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email row
tk.Label(text="Email/Username:").grid(row=2, column=0)
email_entry = tk.Entry(width=35)
email_entry.insert(0, "apexofficial21@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password row
tk.Label(text="Password:").grid(row=3, column=0)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)
gen_button = tk.Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)

# Add button
add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
"""

files["day 30/improved password manager.py"] = """\
# ============================================================
#  DAY 30: Error Handling & JSON
#  PROJECT: Improved Password Manager (search + JSON storage)
# ============================================================
#
#  SKILLS TODAY:
#    - try / except / else / finally
#    - except ExceptionType as e:
#    - import json
#    - json.loads(str)     → parse JSON string to dict
#    - json.dumps(dict)    → dict to JSON string
#    - json.load(file)     → read JSON from file
#    - json.dump(dict, file, indent=4) → write JSON to file
#    - FileNotFoundError   → handle missing files gracefully
#    - KeyError            → handle missing dict keys
#
# ============================================================

import tkinter as tk
from tkinter import messagebox
import json
import random
import string
import pyperclip


# --------------------------------------------------
#  TODO 1: Upgrade save() to use JSON instead of plain text
# --------------------------------------------------
# Data format in data.json:
# {
#   "Amazon": {"email": "user@gmail.com", "password": "abc123"},
#   "GitHub": {"email": "user@gmail.com", "password": "xyz789"}
# }
#
# Steps:
#   1. Try to open data.json and json.load() it → existing_data dict
#   2. Except FileNotFoundError → existing_data = {}
#   3. Update: existing_data[website] = {"email": email, "password": password}
#   4. Write back with json.dump(existing_data, f, indent=4)

def save():
    website  = website_entry.get().title()
    email    = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showwarning(title="Oops", message="Don't leave fields empty!")
        return

    new_data = {website: {"email": email, "password": password}}

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # TODO: merge new_data into data, then write back to file


# --------------------------------------------------
#  TODO 2: find_password()
# --------------------------------------------------
# Get website from entry (title-case it)
# Try to open data.json → json.load
# Except FileNotFoundError → messagebox "No data file found"
# Try data[website] → get email + password
# Except KeyError → messagebox "No details for {website} exist"
# On success → messagebox.showinfo with email and password

def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        pass  # TODO: look up website and show details or error


# --------------------------------------------------
#  TODO 3: generate_password(): same as Day 29
# --------------------------------------------------
def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '*', '+']
    pw = [random.choice(letters) for _ in range(8)] + \\
         [random.choice(symbols)  for _ in range(3)] + \\
         [random.choice(numbers)  for _ in range(3)]
    random.shuffle(pw)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, "".join(pw))
    pyperclip.copy("".join(pw))


# --------------------------------------------------
#  UI (same as Day 29, with a Search button added)
# --------------------------------------------------
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

tk.Label(text="Website:").grid(row=1, column=0)
website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tk.Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

tk.Label(text="Email/Username:").grid(row=2, column=0)
email_entry = tk.Entry(width=35)
email_entry.insert(0, "apexofficial21@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

tk.Label(text="Password:").grid(row=3, column=0)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)
tk.Button(text="Generate Password", command=generate_password).grid(row=3, column=2)

tk.Button(text="Add", width=36, command=save).grid(row=4, column=1, columnspan=2)

window.mainloop()
"""

files["day 31/flash card app.py"] = """\
# ============================================================
#  DAY 31: Capstone: Intermediate Phase
#  PROJECT: Flash Card Language Learning App
# ============================================================
#
#  CAPSTONE: everything from days 15-30:
#    OOP, Tkinter, pandas, JSON, file I/O, try/except
#
#  HOW IT WORKS:
#    - Show a French word on the front of a card
#    - After 3 seconds, flip to show the English translation
#    - ✓ button → you knew it → remove from practice list
#    - ✗ button → you didn't → keep it in
#    - Save remaining words to a file so progress persists
#
# ============================================================

import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# --------------------------------------------------
#  TODO 1: Load the word list
# --------------------------------------------------
# Try to read "words_to_learn.csv" (the user's remaining cards)
# Except FileNotFoundError → read the original "french_words.csv"
# Store as a list of dicts: to_learn
#
# Create a sample CSV if you don't have the course files:
sample = "French,English\\nBien,Well\\nBonjour,Hello\\nMerci,Thank you\\nOui,Yes\\nNon,No\\nChat,Cat\\nChien,Dog\\nMaison,House\\nVoiture,Car\\nEau,Water"
with open("french_words.csv", "w") as f:
    f.write(sample)

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# --------------------------------------------------
#  TODO 2: next_card()
# --------------------------------------------------
# Pick a random card from to_learn → current_card
# Cancel any pending flip timer (window.after_cancel)
# Show FRONT of card: canvas background = "#B1DDC6"
#   Title text = "French", word text = current_card["French"]
# Set a timer: window.after(3000, flip_card)

flip_timer = None

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # TODO: update canvas texts and start flip timer


# --------------------------------------------------
#  TODO 3: flip_card()
# --------------------------------------------------
# Show BACK of card: canvas background = "#2d2d2d" (dark)
#   Title text = "English", word text = current_card["English"]

def flip_card():
    pass


# --------------------------------------------------
#  TODO 4: is_known()
# --------------------------------------------------
# Remove current_card from to_learn
# Save remaining to "words_to_learn.csv" using pandas DataFrame
# Call next_card()

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


# --------------------------------------------------
#  UI Setup
# --------------------------------------------------
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# Ideally: load card_front.png / card_back.png images for the card design
# Fallback rectangle:
canvas.create_rectangle(50, 50, 750, 476, fill="white", outline="")
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word  = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = tk.Button(text="✗ Don't Know", bg="red",    fg="white", command=next_card)
right_button = tk.Button(text="✓ Know It",    bg="green",  fg="white", command=is_known)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_card()   # show first card on startup
window.mainloop()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add more languages: load a different CSV based on user choice
#  2. Show a progress bar (words learned / total words)
#  3. Add a "hard mode" where you type the translation instead of clicking
# ============================================================
"""

# Write all files
for filepath, content in files.items():
    full_path = os.path.join(base, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Created: {filepath}")

print("Done: Days 15-31 written.")
