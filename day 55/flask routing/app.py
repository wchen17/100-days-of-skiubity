# ============================================================
#  DAY 55: Flask Routing & HTML Parsing
#  PROJECT: Higher or Lower Game (web version)
# ============================================================
#
#  SKILLS TODAY:
#    - Multiple routes in one app
#    - url_for("function_name")     → generate URLs safely
#    - redirect(url_for("..."))     → redirect the browser
#    - Dynamic URL segments         → /guess/<int:number>
#    - Passing variables to templates → render_template("x.html", var=value)
#    - request.args                 → URL query parameters (?key=value)
#    - global variables in Flask    → careful with state between requests
#    - random number game logic across routes
#
# ============================================================

from flask import Flask, render_template, redirect, url_for
import random

app   = Flask(__name__)
LIMIT = 10
random_number = random.randint(1, LIMIT)


@app.route("/")
def home():
    global random_number
    random_number = random.randint(1, LIMIT)
    return render_template("home.html", limit=LIMIT)


# --------------------------------------------------
#  TODO 1: /guess/<int:guess> route
# --------------------------------------------------
# Compare guess to random_number
# Return render_template for:
#   "too_high.html" if guess > random_number
#   "too_low.html"  if guess < random_number
#   "correct.html"  if guess == random_number

@app.route("/guess/<int:guess>")
def check_guess(guess):
    pass   # TODO


if __name__ == "__main__":
    app.run(debug=True)
