import os
base = "/home/user/100-days-of-skiubity"
files = {}

files["day 81/morse code converter.py"] = """\
# ============================================================
#  DAY 81: Portfolio Project
#  PROJECT: Text to Morse Code Converter (CLI tool)
# ============================================================
#
#  SKILLS USED: dicts, string manipulation, file I/O, CLI args
#
#  REQUIREMENTS:
#    - Convert plain text to Morse code (dots and dashes)
#    - Convert Morse code back to plain text
#    - Accept input from command line args OR interactive prompt
#    - Save output to a file optionally
#    - Support letters A-Z, digits 0-9, and common punctuation
#
# ============================================================

import sys

MORSE_CODE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',  'J': '.---',
    'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',  'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-','Y': '-.--',
    'Z': '--..',
    '0': '-----','1': '.----','2': '..---','3': '...--','4': '....-',
    '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', ' ': '/',
}

# Reverse the dictionary for decoding
REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


# --------------------------------------------------
#  TODO 1: encode(text) → Morse string
# --------------------------------------------------
# Convert each character to its Morse code (skip unknown chars)
# Separate letters with a space, words with " / "

def encode(text):
    pass   # TODO


# --------------------------------------------------
#  TODO 2: decode(morse) → plain text
# --------------------------------------------------
# Split on " / " to get words
# Split each word on " " to get letter codes
# Look up each code in REVERSE_MORSE

def decode(morse):
    pass   # TODO


# --------------------------------------------------
#  TODO 3: CLI interface
# --------------------------------------------------
# If called with args: python morse.py encode "Hello World"
#                  or: python morse.py decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
# If no args: show interactive menu

def main():
    if len(sys.argv) == 3:
        mode  = sys.argv[1].lower()
        text  = sys.argv[2]
        if mode == "encode":
            print(encode(text))
        elif mode == "decode":
            print(decode(text))
    else:
        print("Morse Code Converter")
        print("1. Encode text to Morse")
        print("2. Decode Morse to text")
        choice = input("Choose (1/2): ")
        if choice == "1":
            text = input("Enter text: ")
            result = encode(text)
            print(f"Morse: {result}")
        elif choice == "2":
            morse = input("Enter Morse (separate letters with space, words with /): ")
            result = decode(morse)
            print(f"Text: {result}")

main()
"""

files["day 82/portfolio website/app.py"] = """\
# ============================================================
#  DAY 82: Portfolio Project
#  PROJECT: Personal Portfolio Website
# ============================================================
#
#  SKILLS USED: Flask, Jinja2, Bootstrap, SQLAlchemy, File upload
#
#  REQUIREMENTS:
#    - Home page with hero section and skills
#    - Projects page listing all 100 days projects
#    - About page
#    - Contact form (with email sending)
#    - Admin panel to add/edit projects (password protected)
#    - Mobile responsive
#
# ============================================================

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change-me")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    day         = db.Column(db.Integer, nullable=False)
    title       = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text,        nullable=False)
    skills      = db.Column(db.String(200), nullable=False)  # comma-separated
    github_url  = db.Column(db.String(200), nullable=True)
    demo_url    = db.Column(db.String(200), nullable=True)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    project_count = db.session.execute(db.select(db.func.count(Project.id))).scalar()
    return render_template("index.html", days_done=project_count)


@app.route("/projects")
def projects():
    all_projects = db.session.execute(db.select(Project).order_by(Project.day)).scalars().all()
    return render_template("projects.html", projects=all_projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # TODO: send email with form data (same as Day 60)
        return redirect(url_for("home"))
    return render_template("contact.html")


# --------------------------------------------------
#  TODO: Admin routes (password protected with session)
# --------------------------------------------------
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if request.form["password"] == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
    return render_template("admin_login.html")


@app.route("/admin")
def admin_dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    projects = db.session.execute(db.select(Project).order_by(Project.day)).scalars().all()
    return render_template("admin.html", projects=projects)


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 83/tic tac toe.py"] = """\
# ============================================================
#  DAY 83: Portfolio Project
#  PROJECT: Tic-Tac-Toe with an AI opponent
# ============================================================
#
#  SKILLS USED: OOP, 2D lists, recursion, minimax algorithm
#
#  REQUIREMENTS:
#    - Play on a 3×3 grid
#    - Human vs AI (computer plays perfectly using minimax)
#    - Display the board after each move
#    - Detect win, loss, and draw
#    - Allow the human to choose X or O
#
# ============================================================

import math

# Board: 3x3 grid, cells are " ", "X", or "O"
board = [[" " for _ in range(3)] for _ in range(3)]


def print_board(b):
    print()
    for i, row in enumerate(b):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()


def check_winner(b, player):
    # Check rows, columns, diagonals
    for row in b:
        if all(c == player for c in row):
            return True
    for col in range(3):
        if all(b[row][col] == player for row in range(3)):
            return True
    if all(b[i][i] == player for i in range(3)):
        return True
    if all(b[i][2-i] == player for i in range(3)):
        return True
    return False


def is_full(b):
    return all(cell != " " for row in b for cell in row)


# --------------------------------------------------
#  TODO 1: minimax(board, is_maximising) → int score
# --------------------------------------------------
# Base cases:
#   AI wins   → return +10
#   Human wins → return -10
#   Draw       → return 0
# Recursive case:
#   If maximising (AI's turn):
#     Try every empty cell, recurse, return the max score
#   If minimising (human's turn):
#     Try every empty cell, recurse, return the min score
#
# This lets the AI pick the move that maximises its score
# (or minimises human's score)

def minimax(b, is_maximising, ai, human):
    if check_winner(b, ai):
        return 10
    if check_winner(b, human):
        return -10
    if is_full(b):
        return 0

    if is_maximising:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == " ":
                    b[r][c] = ai
                    score = minimax(b, False, ai, human)
                    b[r][c] = " "
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == " ":
                    b[r][c] = human
                    score = minimax(b, True, ai, human)
                    b[r][c] = " "
                    best = min(best, score)
        return best


# --------------------------------------------------
#  TODO 2: best_move(board, ai, human) → (row, col)
# --------------------------------------------------
# Try every empty cell, run minimax, return the move with highest score

def best_move(b, ai, human):
    best_score = -math.inf
    move       = None
    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = ai
                score   = minimax(b, False, ai, human)
                b[r][c] = " "
                if score > best_score:
                    best_score = score
                    move       = (r, c)
    return move


# --------------------------------------------------
#  TODO 3: Main game loop
# --------------------------------------------------
def play():
    human = input("Do you want to be X or O? ").upper()
    ai    = "O" if human == "X" else "X"
    print(f"You are {human}, AI is {ai}")
    print_board(board)

    turn = "X"   # X always goes first
    while True:
        if turn == human:
            try:
                row = int(input("Row (0-2): "))
                col = int(input("Col (0-2): "))
                if board[row][col] != " ":
                    print("Cell taken, try again.")
                    continue
                board[row][col] = human
            except (ValueError, IndexError):
                print("Invalid input.")
                continue
        else:
            print("AI is thinking...")
            r, c = best_move(board, ai, human)
            board[r][c] = ai
            print(f"AI played at ({r}, {c})")

        print_board(board)

        if check_winner(board, turn):
            print("You win!" if turn == human else "AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        turn = "O" if turn == "X" else "X"

play()
"""

files["day 84/watermark tool.py"] = """\
# ============================================================
#  DAY 84: Portfolio Project
#  PROJECT: Image Watermarking Desktop App
# ============================================================
#
#  SKILLS USED: Tkinter, PIL/Pillow, file dialogs, OOP
#
#  REQUIREMENTS:
#    - Open any image via file dialog
#    - Let user type custom watermark text
#    - Choose font size and opacity
#    - Preview the watermarked image
#    - Save the result to a new file
#
#  pip install pillow
#
# ============================================================

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

class WatermarkApp:
    def __init__(self, root):
        self.root  = root
        self.root.title("Image Watermarker")
        self.image = None
        self.tk_image = None
        self.setup_ui()

    def setup_ui(self):
        # Control panel
        controls = tk.Frame(self.root)
        controls.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Button(controls, text="Open Image", command=self.open_image).pack(fill=tk.X, pady=4)

        tk.Label(controls, text="Watermark Text:").pack()
        self.text_var = tk.StringVar(value="© wchen17")
        tk.Entry(controls, textvariable=self.text_var, width=20).pack()

        tk.Label(controls, text="Font Size:").pack()
        self.size_var = tk.IntVar(value=36)
        tk.Scale(controls, from_=12, to=120, variable=self.size_var, orient=tk.HORIZONTAL).pack(fill=tk.X)

        tk.Label(controls, text="Opacity (0-255):").pack()
        self.opacity_var = tk.IntVar(value=128)
        tk.Scale(controls, from_=0, to=255, variable=self.opacity_var, orient=tk.HORIZONTAL).pack(fill=tk.X)

        tk.Button(controls, text="Preview",   command=self.preview,   bg="blue",  fg="white").pack(fill=tk.X, pady=4)
        tk.Button(controls, text="Save",      command=self.save,       bg="green", fg="white").pack(fill=tk.X)

        # Image canvas
        self.canvas = tk.Canvas(self.root, width=600, height=500, bg="#1e1e2e")
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if path:
            self.image = Image.open(path).convert("RGBA")
            self.display_image(self.image)

    def display_image(self, img):
        display = img.copy()
        display.thumbnail((600, 500))
        self.tk_image = ImageTk.PhotoImage(display)
        self.canvas.delete("all")
        self.canvas.create_image(300, 250, image=self.tk_image)

    # --------------------------------------------------
    #  TODO 1: apply_watermark(image) → Image
    # --------------------------------------------------
    # Create a transparent overlay: Image.new("RGBA", image.size, (0,0,0,0))
    # Use ImageDraw to write the text at the bottom-right corner
    # Use opacity_var for the text fill alpha: (255, 255, 255, opacity)
    # Composite: Image.alpha_composite(image, overlay)
    # Return the composited image

    def apply_watermark(self, image):
        pass   # TODO

    def preview(self):
        if self.image is None:
            messagebox.showwarning("No Image", "Please open an image first.")
            return
        result = self.apply_watermark(self.image.copy())
        self.display_image(result)

    # --------------------------------------------------
    #  TODO 2: save()
    # --------------------------------------------------
    # Open a save dialog (asksaveasfilename)
    # Apply watermark to the original (full-size) image
    # Convert to RGB before saving as JPEG (JPEG doesn't support alpha)
    # Save the file

    def save(self):
        pass   # TODO


root = tk.Tk()
app  = WatermarkApp(root)
root.mainloop()
"""

files["day 85/typing speed test.py"] = """\
# ============================================================
#  DAY 85: Portfolio Project
#  PROJECT: Typing Speed Test App
# ============================================================
#
#  SKILLS USED: Tkinter, time, string comparison, WPM calculation
#
#  REQUIREMENTS:
#    - Show a random paragraph of text to type
#    - Start timer on first keypress
#    - Highlight correct characters in green, mistakes in red
#    - When done: show WPM, accuracy %, and time taken
#    - Allow restarting with a new text
#
# ============================================================

import tkinter as tk
import time
import random

TEXTS = [
    "The quick brown fox jumps over the lazy dog and then runs away.",
    "Python is a high-level general-purpose programming language.",
    "Practice makes perfect. The more you code, the better you get.",
    "Every expert was once a beginner. Keep going, one day at a time.",
]

class TypingTest:
    def __init__(self, root):
        self.root       = root
        self.root.title("Typing Speed Test")
        self.root.config(padx=40, pady=40)
        self.start_time = None
        self.setup_ui()
        self.new_test()

    def setup_ui(self):
        self.sample_label = tk.Label(self.root, font=("Courier", 16), wraplength=600,
                                     justify=tk.LEFT, bg="#f0f0f0", relief="ridge", padx=10, pady=10)
        self.sample_label.pack(fill=tk.X, pady=(0, 20))

        self.text_entry = tk.Text(self.root, font=("Courier", 16), height=4, width=60)
        self.text_entry.pack()
        self.text_entry.bind("<KeyRelease>", self.check_typing)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        tk.Button(self.root, text="New Test", command=self.new_test,
                  font=("Arial", 12), bg="#4CAF50", fg="white").pack()

    def new_test(self):
        self.target     = random.choice(TEXTS)
        self.start_time = None
        self.sample_label.config(text=self.target)
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="Start typing to begin the timer...")
        self.text_entry.focus()

    # --------------------------------------------------
    #  TODO 1: check_typing(event)
    # --------------------------------------------------
    # On first keypress: record start_time = time.time()
    # Get typed = self.text_entry.get("1.0", "end-1c")
    # Compare typed to self.target char by char:
    #   correct chars → tag green, wrong → tag red
    # If len(typed) >= len(self.target): call show_results()

    def check_typing(self, event):
        typed = self.text_entry.get("1.0", "end-1c")
        if not typed:
            return
        if self.start_time is None:
            self.start_time = time.time()
        # TODO: highlight correct/incorrect characters
        # TODO: check if typing is complete

    # --------------------------------------------------
    #  TODO 2: show_results()
    # --------------------------------------------------
    # elapsed = time.time() - start_time
    # wpm     = (len(target.split()) / elapsed) * 60
    # correct = count matching characters
    # accuracy = correct / len(target) * 100
    # Display in result_label

    def show_results(self):
        pass   # TODO


root = tk.Tk()
app  = TypingTest(root)
root.mainloop()
"""

files["day 86/breakout game.py"] = """\
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
"""

files["day 87/cafe wifi website/app.py"] = """\
# ============================================================
#  DAY 87: Portfolio Project
#  PROJECT: Café & Wifi Website (full stack)
# ============================================================
#
#  SKILLS USED: Flask, SQLAlchemy, Bootstrap, REST API, WTForms
#
#  REQUIREMENTS:
#    - Public site: browse cafes with wifi/power ratings
#    - API: GET /api/cafes, POST /api/cafe, DELETE /api/cafe/<id>
#    - Add café form (login required)
#    - Search by location
#    - Filter by wifi/power/sockets
#    - Deploy to Render
#
# ============================================================

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "secret")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(app)

API_KEY = os.getenv("API_KEY", "TopSecretAPIKey")


class Cafe(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(250), unique=True, nullable=False)
    map_url      = db.Column(db.String(500), nullable=False)
    img_url      = db.Column(db.String(500), nullable=False)
    location     = db.Column(db.String(250), nullable=False)
    seats        = db.Column(db.String(250))
    has_toilet   = db.Column(db.Boolean)
    has_wifi     = db.Column(db.Boolean)
    has_sockets  = db.Column(db.Boolean)
    can_take_calls = db.Column(db.Boolean)
    coffee_price = db.Column(db.String(250))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

with app.app_context():
    db.create_all()


# --------------------------------------------------
#  Web Routes
# --------------------------------------------------
@app.route("/")
def home():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return render_template("index.html", cafes=cafes)

@app.route("/cafe/<int:cafe_id>")
def cafe_detail(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    return render_template("cafe.html", cafe=cafe)

# TODO: /add route with WTForms (login required)
# TODO: /search?q=London route


# --------------------------------------------------
#  REST API Routes
# --------------------------------------------------
@app.route("/api/cafes")
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[c.to_dict() for c in cafes])

@app.route("/api/cafe", methods=["POST"])
def add_cafe():
    # TODO: validate API key in headers or params, then add cafe
    pass

@app.route("/api/cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != API_KEY:
        return jsonify(error="Not authorised."), 403
    cafe = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(success="Cafe deleted."), 200


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 88/todo app/app.py"] = """\
# ============================================================
#  DAY 88: Portfolio Project
#  PROJECT: Todo / Agenda App
# ============================================================
#
#  SKILLS USED: Flask, SQLAlchemy, Bootstrap, WTForms, due dates
#
#  REQUIREMENTS:
#    - Add tasks with title, description, due date, priority
#    - Mark tasks complete (strikethrough, move to bottom)
#    - Delete tasks
#    - Filter: All / Active / Completed / Overdue
#    - Sort by due date or priority
#    - Data persists in SQLite
#
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    due_date    = db.Column(db.Date)
    priority    = db.Column(db.Integer, default=2)   # 1=high, 2=med, 3=low
    completed   = db.Column(db.Boolean, default=False)
    created_at  = db.Column(db.Date, default=date.today)

    @property
    def is_overdue(self):
        return self.due_date and self.due_date < date.today() and not self.completed

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    filter_by = request.args.get("filter", "all")
    query     = db.select(Todo).order_by(Todo.priority, Todo.due_date)
    todos     = db.session.execute(query).scalars().all()

    if filter_by == "active":
        todos = [t for t in todos if not t.completed]
    elif filter_by == "completed":
        todos = [t for t in todos if t.completed]
    elif filter_by == "overdue":
        todos = [t for t in todos if t.is_overdue]

    return render_template("index.html", todos=todos, filter=filter_by, today=date.today())


@app.route("/add", methods=["POST"])
def add_todo():
    title    = request.form.get("title")
    due_str  = request.form.get("due_date")
    priority = int(request.form.get("priority", 2))
    due_date = date.fromisoformat(due_str) if due_str else None

    if title:
        db.session.add(Todo(title=title, due_date=due_date, priority=priority))
        db.session.commit()
    return redirect(url_for("index"))


# --------------------------------------------------
#  TODO 1: /toggle/<id> route → flip completed boolean
# --------------------------------------------------
@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("index"))


# --------------------------------------------------
#  TODO 2: /delete/<id> route
# --------------------------------------------------
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    pass   # TODO


# --------------------------------------------------
#  TODO 3: /edit/<id> route (GET=form, POST=save)
# --------------------------------------------------
@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit(todo_id):
    pass   # TODO


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 89/disappearing text.py"] = """\
# ============================================================
#  DAY 89: Portfolio Project
#  PROJECT: Disappearing Text Writing App
# ============================================================
#
#  CONCEPT: If you stop typing for 5 seconds, all text is erased.
#  Forces you to keep writing without stopping: great for overcoming
#  writer's block and practicing stream-of-consciousness writing.
#
#  SKILLS USED: Tkinter, after(), cancel_after(), Text widget events
#
# ============================================================

import tkinter as tk

class DisappearingTextApp:
    def __init__(self, root):
        self.root        = root
        self.root.title("Keep Writing or Lose It All")
        self.root.config(bg="#1e1e2e")
        self.timer_id    = None
        self.TIMEOUT_MS  = 5000   # 5 seconds

        self.setup_ui()

    def setup_ui(self):
        self.status_label = tk.Label(
            self.root, text="Start typing...", fg="#cdd6f4", bg="#1e1e2e",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=(10, 0))

        self.countdown_label = tk.Label(
            self.root, text="", fg="#f38ba8", bg="#1e1e2e", font=("Arial", 24, "bold")
        )
        self.countdown_label.pack()

        self.text_area = tk.Text(
            self.root, font=("Courier New", 14), wrap=tk.WORD,
            bg="#313244", fg="#cdd6f4", insertbackground="white",
            relief="flat", padx=20, pady=20
        )
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.text_area.bind("<Key>", self.on_keypress)

        self.word_count_label = tk.Label(
            self.root, text="Words: 0", fg="#a6e3a1", bg="#1e1e2e", font=("Arial", 11)
        )
        self.word_count_label.pack()

    # --------------------------------------------------
    #  TODO 1: on_keypress(event)
    # --------------------------------------------------
    # Reset the countdown timer on every keypress:
    #   Cancel existing timer if any: self.root.after_cancel(self.timer_id)
    #   Start new timer: self.timer_id = self.root.after(TIMEOUT_MS, self.erase_all)
    # Update word count label
    # Show "5 seconds remaining" warning at 5s, update countdown

    def on_keypress(self, event):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.timer_id = self.root.after(self.TIMEOUT_MS, self.erase_all)
        self.update_word_count()
        # TODO: start a visual countdown

    def update_word_count(self):
        text  = self.text_area.get("1.0", "end-1c")
        words = len(text.split()) if text.strip() else 0
        self.word_count_label.config(text=f"Words: {words}")

    # --------------------------------------------------
    #  TODO 2: erase_all()
    # --------------------------------------------------
    # Delete all text: self.text_area.delete("1.0", tk.END)
    # Show "TOO SLOW! Everything erased." in status label
    # Flash the background red briefly

    def erase_all(self):
        pass   # TODO

    # --------------------------------------------------
    #  TODO 3: countdown(seconds_left)
    # --------------------------------------------------
    # Called once per second when typing has paused
    # Update countdown_label with seconds_left
    # If seconds_left == 0 → call erase_all()
    # Otherwise: self.timer_id = self.root.after(1000, self.countdown, seconds_left - 1)

    def countdown(self, seconds_left):
        pass   # TODO


root = tk.Tk()
root.geometry("800x600")
app = DisappearingTextApp(root)
root.mainloop()
"""

files["day 90/pdf to audiobook.py"] = """\
# ============================================================
#  DAY 90: Portfolio Project
#  PROJECT: PDF to Audiobook Converter
# ============================================================
#
#  SKILLS USED: PyPDF2/pypdf, pyttsx3 or gtts, file dialogs, Tkinter
#
#  REQUIREMENTS:
#    - Select a PDF file via file dialog
#    - Extract text from each page
#    - Convert text to speech (offline with pyttsx3 or online with gTTS)
#    - Play audio directly or save as .mp3
#    - Show page progress
#
#  pip install pypdf pyttsx3 gtts
#
# ============================================================

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os

# Try pyttsx3 (offline TTS): falls back gracefully if not installed
try:
    import pyttsx3
    TTS_ENGINE = "pyttsx3"
except ImportError:
    TTS_ENGINE = None

# Try gTTS (online TTS, saves to mp3)
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

# PDF reader
try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        PdfReader = None


class AudiobookApp:
    def __init__(self, root):
        self.root      = root
        self.root.title("PDF to Audiobook")
        self.root.config(padx=20, pady=20)
        self.pdf_path  = None
        self.is_playing = False
        self.setup_ui()

    def setup_ui(self):
        tk.Button(self.root, text="Open PDF", command=self.open_pdf,
                  bg="#4a90d9", fg="white", font=("Arial", 12)).pack(pady=5)

        self.file_label = tk.Label(self.root, text="No file selected", wraplength=400)
        self.file_label.pack()

        self.page_label = tk.Label(self.root, text="Page: -/-")
        self.page_label.pack()

        tk.Button(self.root, text="▶ Read Aloud (pyttsx3)",
                  command=self.read_aloud, bg="#45ba78", fg="white").pack(pady=5)
        tk.Button(self.root, text="💾 Save as MP3 (gTTS)",
                  command=self.save_mp3, bg="#f59e0b", fg="white").pack(pady=5)
        tk.Button(self.root, text="⏹ Stop",
                  command=self.stop, bg="#ef4444", fg="white").pack(pady=5)

        self.status = tk.Label(self.root, text="", font=("Arial", 11), fg="gray")
        self.status.pack()

    def open_pdf(self):
        path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if path:
            self.pdf_path = path
            self.file_label.config(text=os.path.basename(path))
            self.status.config(text="PDF loaded. Ready to read.")

    # --------------------------------------------------
    #  TODO 1: extract_text(pdf_path) → list of page strings
    # --------------------------------------------------
    def extract_text(self, path):
        if PdfReader is None:
            messagebox.showerror("Error", "pypdf not installed. pip install pypdf")
            return []
        reader = PdfReader(path)
        pages  = [page.extract_text() or "" for page in reader.pages]
        return pages

    # --------------------------------------------------
    #  TODO 2: read_aloud(): run in a thread so UI stays responsive
    # --------------------------------------------------
    # Extract pages, loop through each:
    #   Update page_label
    #   engine = pyttsx3.init()
    #   engine.say(page_text)
    #   engine.runAndWait()
    #   If not self.is_playing: break

    def read_aloud(self):
        if not self.pdf_path:
            messagebox.showwarning("No PDF", "Open a PDF first.")
            return
        self.is_playing = True
        thread = threading.Thread(target=self._read_thread, daemon=True)
        thread.start()

    def _read_thread(self):
        pages = self.extract_text(self.pdf_path)
        if TTS_ENGINE == "pyttsx3":
            engine = pyttsx3.init()
            for i, page in enumerate(pages, 1):
                if not self.is_playing:
                    break
                self.page_label.config(text=f"Page: {i}/{len(pages)}")
                engine.say(page)
                engine.runAndWait()
        else:
            self.status.config(text="pyttsx3 not available. Use Save as MP3 instead.")

    # --------------------------------------------------
    #  TODO 3: save_mp3(): use gTTS to save each page as mp3
    # --------------------------------------------------
    def save_mp3(self):
        pass   # TODO

    def stop(self):
        self.is_playing = False
        self.status.config(text="Stopped.")


root = tk.Tk()
app  = AudiobookApp(root)
root.mainloop()
"""

files["day 91/color palette generator.py"] = """\
# ============================================================
#  DAY 91: Portfolio Project
#  PROJECT: Image to Colour Palette Generator
# ============================================================
#
#  SKILLS USED: PIL/Pillow, colorgram, Tkinter, k-means clustering
#
#  REQUIREMENTS:
#    - Open any image
#    - Extract the dominant colours (k-means or colorgram)
#    - Display a colour swatch palette
#    - Show hex codes for each colour
#    - Copy a hex code to clipboard on click
#
#  pip install pillow colorgram.py pyperclip
#
# ============================================================

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import colorgram
import pyperclip

class PaletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colour Palette Generator")
        self.root.config(padx=20, pady=20, bg="#1e1e2e")
        self.setup_ui()

    def setup_ui(self):
        tk.Button(self.root, text="Open Image", command=self.open_image,
                  bg="#89b4fa", fg="#1e1e2e", font=("Arial", 12, "bold")).pack(pady=10)

        self.img_label = tk.Label(self.root, bg="#1e1e2e")
        self.img_label.pack()

        self.palette_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.palette_frame.pack(pady=10)

        self.status = tk.Label(self.root, text="", bg="#1e1e2e", fg="#cdd6f4")
        self.status.pack()

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")])
        if not path:
            return

        # Show thumbnail
        img = Image.open(path)
        img.thumbnail((400, 300))
        self.tk_img = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.tk_img)

        # --------------------------------------------------
        #  TODO 1: Extract 10 dominant colours using colorgram
        # --------------------------------------------------
        # colours = colorgram.extract(path, 10)
        # Each colour has .rgb (r,g,b tuple) and .proportion

        colours = colorgram.extract(path, 10)
        self.show_palette(colours)

    def show_palette(self, colours):
        # Clear old swatches
        for widget in self.palette_frame.winfo_children():
            widget.destroy()

        # --------------------------------------------------
        #  TODO 2: Create a colour swatch for each colour
        # --------------------------------------------------
        # For each colour:
        #   hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
        #   Create a Frame with background = hex_code
        #   Create a Label inside showing the hex code
        #   Bind a click to copy the hex to clipboard

        for colour in colours:
            r, g, b = colour.rgb
            hex_code = f"#{r:02x}{g:02x}{b:02x}"

            swatch = tk.Frame(self.palette_frame, bg=hex_code, width=80, height=80, cursor="hand2")
            swatch.pack(side=tk.LEFT, padx=4)
            swatch.pack_propagate(False)

            # Choose readable text colour (white on dark, black on light)
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            text_color = "white" if brightness < 128 else "black"

            label = tk.Label(swatch, text=hex_code, bg=hex_code, fg=text_color, font=("Courier", 8))
            label.place(relx=0.5, rely=0.5, anchor="center")

            # TODO: bind click to copy hex_code to clipboard
            # swatch.bind("<Button-1>", lambda e, h=hex_code: pyperclip.copy(h))
            # label.bind("<Button-1>", lambda e, h=hex_code: ...)

        self.status.config(text=f"Extracted {len(colours)} colours. Click a swatch to copy hex.")


root = tk.Tk()
app  = PaletteApp(root)
root.mainloop()
"""

files["day 92/web scraper tool.py"] = """\
# ============================================================
#  DAY 92: Portfolio Project
#  PROJECT: Custom Web Scraper CLI Tool
# ============================================================
#
#  SKILLS USED: requests, BeautifulSoup, argparse, pandas, CSV
#
#  REQUIREMENTS:
#    - Accept a URL and CSS selector via command line arguments
#    - Scrape all matching elements from the page
#    - Save results to CSV or JSON
#    - Optional: follow pagination (?page=N) up to a limit
#    - Handle errors gracefully (bad URL, no results)
#
#  Usage:
#    python scraper.py --url https://books.toscrape.com --selector "h3 a" --output books.csv
#
# ============================================================

import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Web scraper CLI tool")
    parser.add_argument("--url",      required=True,    help="URL to scrape")
    parser.add_argument("--selector", required=True,    help="CSS selector for target elements")
    parser.add_argument("--output",   default="output.csv", help="Output file (csv or json)")
    parser.add_argument("--pages",    type=int, default=1, help="Number of pages to scrape")
    parser.add_argument("--delay",    type=float, default=1.0, help="Delay between page requests (seconds)")
    return parser.parse_args()


def scrape_page(url, selector):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup     = BeautifulSoup(response.text, "html.parser")
    elements = soup.select(selector)

    results = []
    for el in elements:
        results.append({
            "text": el.get_text(strip=True),
            "href": el.get("href", ""),
            "src":  el.get("src",  ""),
        })
    return results


def save_results(data, output_path):
    if output_path.endswith(".json"):
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
    else:
        pd.DataFrame(data).to_csv(output_path, index=False)
    print(f"Saved {len(data)} results to {output_path}")


# --------------------------------------------------
#  TODO: Add pagination support
# --------------------------------------------------
# For pages 1 to args.pages:
#   Construct page URL (try appending ?page=N or /page/N)
#   Scrape and append results
#   time.sleep(args.delay) between requests

def main():
    args    = parse_args()
    all_data = []

    import time
    for page_num in range(1, args.pages + 1):
        if args.pages > 1:
            url = f"{args.url.rstrip('/')}/page/{page_num}"
        else:
            url = args.url

        print(f"Scraping page {page_num}: {url}")
        results = scrape_page(url, args.selector)
        if not results:
            print("No results found or page doesn't exist. Stopping.")
            break
        all_data.extend(results)
        if page_num < args.pages:
            time.sleep(args.delay)

    if all_data:
        save_results(all_data, args.output)
    else:
        print("No data collected.")
        sys.exit(1)

if __name__ == "__main__":
    main()
"""

files["day 94/space invaders/main.py"] = """\
# ============================================================
#  DAY 94: Portfolio Project
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
"""

files["day 95/custom api/app.py"] = """\
# ============================================================
#  DAY 95: Portfolio Project
#  PROJECT: Custom REST API: Random Quote / Joke / Fact Service
# ============================================================
#
#  SKILLS USED: Flask, SQLAlchemy, REST, authentication, rate limiting
#
#  ENDPOINTS:
#    GET  /api/random          → random item
#    GET  /api/all             → all items
#    GET  /api/search?q=...    → filter by keyword
#    POST /api/add             → add new item (API key required)
#    DELETE /api/delete/<id>   → delete (admin key required)
#
# ============================================================

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quotes.db"
db = SQLAlchemy(app)

API_KEY       = os.getenv("API_KEY", "user-key-123")
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY", "admin-key-secret")


class Quote(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    text   = db.Column(db.Text,        nullable=False)
    author = db.Column(db.String(100), nullable=False)
    tags   = db.Column(db.String(200))  # comma-separated

    def to_dict(self):
        return {"id": self.id, "text": self.text, "author": self.author, "tags": self.tags}

with app.app_context():
    db.create_all()
    # Seed with some quotes if empty
    if not db.session.execute(db.select(Quote)).scalars().first():
        seeds = [
            Quote(text="The only way to do great work is to love what you do.", author="Steve Jobs", tags="motivation,work"),
            Quote(text="Code is like humor. When you have to explain it, it's bad.", author="Cory House", tags="programming"),
            Quote(text="Programs must be written for people to read.", author="Harold Abelson", tags="programming"),
        ]
        db.session.add_all(seeds)
        db.session.commit()


@app.route("/api/random")
def get_random():
    all_quotes = db.session.execute(db.select(Quote)).scalars().all()
    if not all_quotes:
        return jsonify(error="No quotes available"), 404
    return jsonify(quote=random.choice(all_quotes).to_dict())


@app.route("/api/all")
def get_all():
    quotes = db.session.execute(db.select(Quote)).scalars().all()
    return jsonify(quotes=[q.to_dict() for q in quotes])


@app.route("/api/search")
def search():
    keyword = request.args.get("q", "").lower()
    all_q   = db.session.execute(db.select(Quote)).scalars().all()
    results = [q for q in all_q if keyword in q.text.lower() or keyword in (q.tags or "").lower()]
    if results:
        return jsonify(quotes=[q.to_dict() for q in results])
    return jsonify(error="No quotes matched."), 404


@app.route("/api/add", methods=["POST"])
def add_quote():
    api_key = request.args.get("api-key")
    if api_key != API_KEY:
        return jsonify(error="Unauthorized."), 403
    data = request.get_json()
    if not data or not data.get("text") or not data.get("author"):
        return jsonify(error="text and author are required."), 400
    new_quote = Quote(text=data["text"], author=data["author"], tags=data.get("tags", ""))
    db.session.add(new_quote)
    db.session.commit()
    return jsonify(success="Quote added!", quote=new_quote.to_dict()), 201


@app.route("/api/delete/<int:quote_id>", methods=["DELETE"])
def delete_quote(quote_id):
    api_key = request.args.get("api-key")
    if api_key != ADMIN_API_KEY:
        return jsonify(error="Admin key required."), 403
    quote = db.get_or_404(Quote, quote_id)
    db.session.delete(quote)
    db.session.commit()
    return jsonify(success="Quote deleted.")


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 96/online shop/app.py"] = """\
# ============================================================
#  DAY 96: Portfolio Project
#  PROJECT: Simple Online Shop with Stripe Payments
# ============================================================
#
#  SKILLS USED: Flask, SQLAlchemy, Stripe API, Bootstrap, sessions
#
#  REQUIREMENTS:
#    - Product listing page
#    - Product detail page
#    - Add to cart (session-based)
#    - Checkout with Stripe (test mode)
#    - Order confirmation page
#
#  pip install flask flask-sqlalchemy stripe python-dotenv
#  Get Stripe test keys at dashboard.stripe.com
#
# ============================================================

from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import stripe
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
db  = SQLAlchemy(app)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_...")
STRIPE_PUB_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "pk_test_...")


class Product(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price_cents = db.Column(db.Integer, nullable=False)  # price in cents
    image_url   = db.Column(db.String(300))
    stock       = db.Column(db.Integer, default=100)

    @property
    def price_display(self):
        return f"${self.price_cents / 100:.2f}"

with app.app_context():
    db.create_all()
    if not db.session.execute(db.select(Product)).scalars().first():
        db.session.add_all([
            Product(name="Python Book",   description="Learn Python fast",    price_cents=2999, stock=50),
            Product(name="Coding Course", description="100 Days of Code",     price_cents=1999, stock=999),
            Product(name="Dev Stickers",  description="Laptop sticker pack",  price_cents=499,  stock=200),
        ])
        db.session.commit()


@app.route("/")
def shop():
    products = db.session.execute(db.select(Product)).scalars().all()
    cart_count = sum(session.get("cart", {}).values())
    return render_template("shop.html", products=products, cart_count=cart_count)


@app.route("/cart")
def cart():
    cart      = session.get("cart", {})
    products  = []
    total     = 0
    for product_id, qty in cart.items():
        product = db.get_or_404(Product, int(product_id))
        subtotal = product.price_cents * qty
        total   += subtotal
        products.append({"product": product, "qty": qty, "subtotal": subtotal})
    return render_template("cart.html", items=products, total=total, stripe_pub_key=STRIPE_PUB_KEY)


# --------------------------------------------------
#  TODO 1: /add-to-cart/<product_id>
# --------------------------------------------------
@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session["cart"] = cart
    return redirect(url_for("shop"))


# --------------------------------------------------
#  TODO 2: /checkout: create a Stripe payment intent
# --------------------------------------------------
@app.route("/checkout", methods=["POST"])
def checkout():
    cart  = session.get("cart", {})
    total = sum(
        db.get_or_404(Product, int(pid)).price_cents * qty
        for pid, qty in cart.items()
    )
    # intent = stripe.PaymentIntent.create(amount=total, currency="usd")
    # return jsonify(client_secret=intent.client_secret)
    return jsonify(client_secret="test_secret_for_now")


@app.route("/success")
def success():
    session.pop("cart", None)
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 97/percentage calculator.py"] = """\
# ============================================================
#  DAY 97: Portfolio Project
#  PROJECT: Multi-purpose Percentage Calculator (CLI + GUI)
# ============================================================
#
#  SKILLS USED: Tkinter, OOP, string formatting, maths
#
#  CALCULATIONS:
#    1. X% of Y            → what is 15% of 200?
#    2. X is what % of Y?  → 30 is what % of 200?
#    3. % increase/decrease → 50 to 75 is what % increase?
#    4. Add/subtract %      → 200 + 15% = ?
#    5. Reverse % (% before increase) → 230 after 15% increase = what was original?
#
# ============================================================

import tkinter as tk
from tkinter import ttk

def percent_of(x, y):        return x / 100 * y
def what_percent(x, y):      return (x / y) * 100 if y != 0 else 0
def percent_change(old, new): return ((new - old) / old) * 100 if old != 0 else 0
def add_percent(value, pct): return value + (value * pct / 100)
def reverse_percent(final, pct): return final / (1 + pct / 100)


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Percentage Calculator")
        self.root.config(padx=30, pady=30)
        self.build_tabs()

    def build_tabs(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill=tk.BOTH)

        self.build_tab(notebook, "X% of Y",
            ["Percentage (X)", "Value (Y)"],
            lambda vals: f"{vals[0]}% of {vals[1]} = {percent_of(vals[0], vals[1]):.2f}")

        self.build_tab(notebook, "X is what %",
            ["Value (X)", "Total (Y)"],
            lambda vals: f"{vals[0]} is {what_percent(vals[0], vals[1]):.2f}% of {vals[1]}")

        self.build_tab(notebook, "% Change",
            ["Old Value", "New Value"],
            lambda vals: f"Change: {percent_change(vals[0], vals[1]):+.2f}%")

        # --------------------------------------------------
        #  TODO: Add tabs for "Add/subtract %" and "Reverse %"
        # --------------------------------------------------

    def build_tab(self, notebook, title, labels, formula):
        frame = tk.Frame(notebook, padx=20, pady=20)
        notebook.add(frame, text=title)

        entries = []
        for label in labels:
            tk.Label(frame, text=label + ":").pack()
            entry = tk.Entry(frame, width=20, font=("Arial", 14))
            entry.pack(pady=4)
            entries.append(entry)

        result_var = tk.StringVar(value="Enter values above")
        tk.Label(frame, textvariable=result_var, font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

        def calculate():
            try:
                vals = [float(e.get()) for e in entries]
                result_var.set(formula(vals))
            except ValueError:
                result_var.set("Please enter valid numbers")

        tk.Button(frame, text="Calculate", command=calculate,
                  bg="#4CAF50", fg="white", font=("Arial", 12)).pack()


root = tk.Tk()
app  = CalculatorApp(root)
root.mainloop()
"""

files["day 98/space race analysis.py"] = """\
# ============================================================
#  DAY 98: Portfolio Project
#  PROJECT: Space Race Data Analysis
# ============================================================
#
#  SKILLS USED: pandas, matplotlib, plotly, groupby, time series
#
#  QUESTIONS TO ANSWER:
#    1. How many launches per year? (line chart)
#    2. Which country launched the most rockets? (bar chart)
#    3. What % of launches were successful over time?
#    4. Mission failure rates by country
#    5. Cold War era vs post-Cold War launches
#
#  Dataset: "mission_launches.csv" from Maven Analytics / Kaggle
#  (search "space missions" on Kaggle: it's free)
#  For now, use the sample data below.
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Sample data (download the real 4,324-row dataset from Kaggle)
data = {
    "Company":  ["NASA", "NASA", "Roscosmos", "SpaceX", "SpaceX", "NASA", "JAXA", "ESA"],
    "Location": ["USA", "USA", "Russia", "USA", "USA", "USA", "Japan", "France"],
    "Date":     ["1969-07-16", "1972-12-07", "1975-05-24", "2015-12-21",
                 "2020-05-30", "2023-05-05", "2023-07-01", "2023-10-13"],
    "Mission":  ["Apollo 11", "Apollo 17", "Soyuz 18", "OG2 Mission", "Crew Dragon", "Artemis", "H-IIB", "Vega"],
    "Status":   ["Success", "Success", "Success", "Success", "Success", "Success", "Failure", "Success"],
    "Cost_$M":  [355, 450, None, 60, 200, 4100, 90, 80],
}
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year


# --------------------------------------------------
#  TODO 1: Launches per year (line chart)
# --------------------------------------------------
launches_per_year = df.groupby("Year").size()
# plt.plot(launches_per_year.index, launches_per_year.values)
# plt.title("Space Launches Per Year")


# --------------------------------------------------
#  TODO 2: Launches by country (bar chart)
# --------------------------------------------------
by_country = df["Location"].value_counts()
# plt.bar(by_country.index, by_country.values)


# --------------------------------------------------
#  TODO 3: Success rate over time
# --------------------------------------------------
df["Success"] = (df["Status"] == "Success").astype(int)
# success_by_year = df.groupby("Year")["Success"].mean() * 100
# plot as line chart


# --------------------------------------------------
#  TODO 4: Choropleth map: launches by country
# --------------------------------------------------
# fig = px.choropleth(
#     df.groupby("Location").size().reset_index(name="count"),
#     locations="Location", locationmode="country names",
#     color="count", title="Space Launches by Country"
# )
# fig.show()

print(df.describe())
print("\\nLaunches by country:\\n", by_country)
"""

files["day 99/police killings analysis.py"] = """\
# ============================================================
#  DAY 99: Portfolio Project
#  PROJECT: Data Analysis: Fatal Police Encounters in the US
# ============================================================
#
#  SKILLS USED: pandas, seaborn, plotly, statistical analysis
#
#  This dataset covers a sensitive, real-world topic.
#  Approach the analysis with care and present findings factually.
#
#  Dataset: FatalEncounters.org / The Guardian "The Counted"
#  For practice, use the sample below or download from Kaggle.
#
#  QUESTIONS TO ANSWER:
#    1. How many incidents per year?
#    2. Breakdown by race (adjusted for population share)?
#    3. By state: choropleth map
#    4. By age distribution
#    5. Trend over time: is it increasing or decreasing?
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    "Year":  [2015, 2015, 2016, 2016, 2017, 2017, 2018, 2018, 2019, 2020],
    "State": ["CA", "TX", "FL", "NY", "CA", "TX", "FL", "NY", "CA", "TX"],
    "Race":  ["White", "Black", "Hispanic", "White", "Black", "White", "Hispanic", "Black", "White", "Hispanic"],
    "Age":   [34, 28, 45, 52, 23, 38, 29, 41, 55, 31],
    "Armed": ["Firearm", "Knife", "Unarmed", "Firearm", "Unarmed", "Firearm", "Vehicle", "Knife", "Firearm", "Unarmed"],
}
df = pd.DataFrame(data)


# --------------------------------------------------
#  TODO 1: Incidents per year
# --------------------------------------------------
print("Incidents per year:")
print(df.groupby("Year").size())


# --------------------------------------------------
#  TODO 2: By race: bar chart
# --------------------------------------------------
# sns.countplot(data=df, x="Race", order=df["Race"].value_counts().index)


# --------------------------------------------------
#  TODO 3: Age distribution: histogram + KDE
# --------------------------------------------------
# sns.histplot(df["Age"], kde=True, bins=10)


# --------------------------------------------------
#  TODO 4: Armed status breakdown: pie chart
# --------------------------------------------------
# armed_counts = df["Armed"].value_counts()
# plt.pie(armed_counts.values, labels=armed_counts.index, autopct="%1.1f%%")


# --------------------------------------------------
#  TODO 5: State-level choropleth (plotly)
# --------------------------------------------------
# import plotly.express as px
# state_counts = df["State"].value_counts().reset_index()
# fig = px.choropleth(state_counts, locations="State", locationmode="USA-states",
#                     color="count", scope="usa")
# fig.show()

print("\\nArmed status breakdown:")
print(df["Armed"].value_counts())
"""

files["day 100/final capstone.py"] = """\
# ============================================================
#  DAY 100: FINAL CAPSTONE 🎉
#  PROJECT: Choose Your Own: Multivariable Regression or Personal Project
# ============================================================
#
#  OPTION A: Earnings Prediction (Multivariable Regression)
#    - Dataset: Census income data (UCI Machine Learning Repository)
#    - Predict whether someone earns >$50k/year
#    - Features: age, education, occupation, hours per week, etc.
#    - Techniques: logistic regression, decision trees, feature importance
#
#  OPTION B: Your Personal Dream Project
#    - What would you actually use every day?
#    - What problem have you wanted to automate?
#    - Build it. You have all the skills now.
#
#  SKILLS TO DEMONSTRATE ON DAY 100:
#    ✅ Data cleaning and feature engineering
#    ✅ Model training and evaluation
#    ✅ Web interface or CLI
#    ✅ Deployment (optional)
#    ✅ Clean, documented code
#    ✅ README with how to run it
#
# ============================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------
#  OPTION A: Census Earnings Classifier
# --------------------------------------------------

# Sample data (the real dataset has ~48,000 rows: download from UCI)
np.random.seed(42)
n = 500
df = pd.DataFrame({
    "age":          np.random.randint(18, 70, n),
    "education_yrs": np.random.randint(8, 18, n),
    "hours_per_week": np.random.randint(10, 80, n),
    "occupation":    np.random.choice(["Tech", "Sales", "Management", "Labour"], n),
    "sex":           np.random.choice(["Male", "Female"], n),
    "income":        np.random.choice([0, 1], n),  # 0 = <=50k, 1 = >50k
})


# --------------------------------------------------
#  TODO 1: Explore and clean the data
# --------------------------------------------------
print(df.head())
print(df.describe())
print("\\nMissing values:\\n", df.isnull().sum())


# --------------------------------------------------
#  TODO 2: Feature engineering
# --------------------------------------------------
# One-hot encode occupation and sex
# Check for class imbalance

df_encoded = pd.get_dummies(df, columns=["occupation", "sex"], drop_first=True)
print("\\nClass balance:")
print(df["income"].value_counts(normalize=True))


# --------------------------------------------------
#  TODO 3: Train/test split and fit LogisticRegression
# --------------------------------------------------
X = df_encoded.drop("income", axis=1)
y = df_encoded["income"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# --------------------------------------------------
#  TODO 4: Evaluate
# --------------------------------------------------
y_pred = model.predict(X_test)
print("\\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix heatmap
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["<=50k", ">50k"], yticklabels=["<=50k", ">50k"])
plt.title("Confusion Matrix")
plt.show()


# --------------------------------------------------
#  TODO 5: Predict for a specific person
# --------------------------------------------------
# new_person = pd.DataFrame([{
#     "age": 35, "education_yrs": 16, "hours_per_week": 45,
#     "occupation_Sales": 0, "occupation_Management": 1, "occupation_Tech": 0,
#     "sex_Male": 1
# }])
# prediction = model.predict(new_person)[0]
# prob = model.predict_proba(new_person)[0]
# print(f"Predicted income: {'> $50k' if prediction else '<= $50k'}")
# print(f"Confidence: {max(prob)*100:.1f}%")


# ============================================================
#  CONGRATULATIONS! YOU'VE COMPLETED 100 DAYS OF CODE! 🎉
# ============================================================
#
#  What you've built over 100 days:
#    ✅ CLI games and tools (hangman, blackjack, calculator)
#    ✅ Turtle graphics games (snake, pong, breakout)
#    ✅ GUI desktop apps (Pomodoro, password manager, flash cards)
#    ✅ Web automation bots (Selenium, BeautifulSoup)
#    ✅ API-powered apps (weather, stocks, flights, Spotify)
#    ✅ Full-stack web apps (Flask + SQLAlchemy + Bootstrap)
#    ✅ User authentication and deployment
#    ✅ Data analysis and visualisation (pandas, matplotlib, plotly)
#    ✅ Machine learning (regression, classification)
#
#  Where to go from here:
#    → Contribute to open source (GitHub)
#    → Build a SaaS product with your Flask skills
#    → Learn FastAPI (faster, modern REST APIs)
#    → Explore Django (larger web framework)
#    → Learn React (pair it with your Flask API)
#    → Dive deeper into ML: TensorFlow, PyTorch
#    → Get certified: AWS, Google Cloud, Azure
#
# ============================================================
"""

for filepath, content in files.items():
    full_path = os.path.join(base, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Created: {filepath}")

print("Done: Days 81-100 written.")
