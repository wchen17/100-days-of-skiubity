# ============================================================
#  DAY 94 — Portfolio Project
#  PROJECT: Space Invaders (Turtle)
# ============================================================
#
#  SKILLS USED: Turtle, OOP, collision detection, game loop, sound
#
#  COMPONENTS:
#    Player  → ship at bottom, moves left/right, fires bullets
#    Alien   → grid of aliens, move right then drop and reverse
#    Bullet  → fired upward by player; aliens fire down
#    Barrier → breakable shields
#    Scoreboard
#
# ============================================================

import turtle
import time
import random

screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

ALIEN_ROWS  = 4
ALIEN_COLS  = 10
ALIEN_DROP  = 20
PLAYER_Y    = -300


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("cyan")
        self.penup()
        self.goto(0, PLAYER_Y)
        self.setheading(90)
        self.speed_px = 20
        self.bullets  = []

    def go_left(self):
        if self.xcor() > -380:
            self.setx(self.xcor() - self.speed_px)

    def go_right(self):
        if self.xcor() < 380:
            self.setx(self.xcor() + self.speed_px)

    def fire(self):
        if len(self.bullets) < 3:
            b = Bullet(self.xcor(), self.ycor() + 20, "up")
            self.bullets.append(b)


class Alien(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(["red", "orange", "green", "yellow"]))
        self.penup()
        self.goto(x, y)
        self.shapesize(0.8, 0.8)


class Bullet(turtle.Turtle):
    def __init__(self, x, y, direction):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(0.3, 0.3)
        self.penup()
        self.goto(x, y)
        self.direction = direction  # "up" or "down"
        self.speed_px  = 15

    def move(self):
        if self.direction == "up":
            self.sety(self.ycor() + self.speed_px)
        else:
            self.sety(self.ycor() - self.speed_px)

    def is_off_screen(self):
        return abs(self.ycor()) > 360


# --------------------------------------------------
#  TODO 1: Build the alien grid
# --------------------------------------------------
aliens = []
for row in range(ALIEN_ROWS):
    for col in range(ALIEN_COLS):
        x = -200 + col * 45
        y = 250  - row * 40
        aliens.append(Alien(x, y))

player     = Player()
alien_dir  = 1   # +1 = moving right, -1 = moving left
move_timer = 0


# --------------------------------------------------
#  TODO 2: Alien movement (shift + drop pattern)
# --------------------------------------------------
def move_aliens():
    global alien_dir
    rightmost = max(a.xcor() for a in aliens) if aliens else 0
    leftmost  = min(a.xcor() for a in aliens) if aliens else 0

    if rightmost > 360 or leftmost < -360:
        alien_dir *= -1
        for a in aliens:
            a.sety(a.ycor() - ALIEN_DROP)

    for a in aliens:
        a.setx(a.xcor() + 5 * alien_dir)


screen.listen()
screen.onkeypress(player.go_left,  "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.fire,     "space")


# --------------------------------------------------
#  Game loop (TODO 3: collisions, alien fire, game over)
# --------------------------------------------------
game_on = True
frame   = 0

while game_on:
    time.sleep(0.05)
    screen.update()

    frame += 1
    if frame % 5 == 0:
        move_aliens()

    # Move player bullets
    for bullet in player.bullets[:]:
        bullet.move()
        if bullet.is_off_screen():
            bullet.hideturtle()
            player.bullets.remove(bullet)
            continue
        # TODO: check collision with each alien
        for alien in aliens[:]:
            if bullet.distance(alien) < 20:
                alien.hideturtle()
                aliens.remove(alien)
                bullet.hideturtle()
                player.bullets.remove(bullet)
                break

    # TODO: random alien firing
    # TODO: check if alien reaches player Y → game over
    # TODO: check if all aliens defeated → YOU WIN

    if not aliens:
        print("YOU WIN!")
        game_on = False

screen.exitonclick()
