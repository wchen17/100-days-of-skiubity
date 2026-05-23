# ============================================================
#  DAY 54 — Flask Web Framework Intro
#  PROJECT: Your first Flask web server
# ============================================================
#
#  SKILLS TODAY:
#    - from flask import Flask
#    - app = Flask(__name__)
#    - @app.route("/path")       → bind a URL to a function
#    - return "HTML string"      → simplest response
#    - return render_template()  → serve an HTML file
#    - app.run(debug=True)       → start dev server with auto-reload
#    - HTTP methods: GET (default), POST
#    - Dynamic routes: /user/<name>
#
#  pip install flask
#
# ============================================================

from flask import Flask, render_template

app = Flask(__name__)


# --------------------------------------------------
#  Route 1: Home page
# --------------------------------------------------
@app.route("/")
def home():
    return "<h1>Hello, World!</h1><p>My first Flask app.</p>"


# --------------------------------------------------
#  TODO 1: Add a /hello route
# --------------------------------------------------
# Return a personalised greeting as an HTML string

# @app.route("/hello")
# def hello():
#     return ...


# --------------------------------------------------
#  TODO 2: Dynamic route /hello/<name>
# --------------------------------------------------
# The <name> part of the URL becomes a parameter
# Return "Hello, {name.title()}!" as HTML

# @app.route("/hello/<name>")
# def greet(name):
#     return ...


# --------------------------------------------------
#  TODO 3: /about route — render an HTML template
# --------------------------------------------------
# Create templates/about.html (see below)
# Use render_template("about.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")


# --------------------------------------------------
#  TODO 4: Return different HTTP status codes
# --------------------------------------------------
# Flask lets you return a tuple: (response, status_code)
# @app.route("/not-found")
# def not_found():
#     return "This page doesn't exist.", 404


if __name__ == "__main__":
    app.run(debug=True)

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a /random route that returns a random number on each visit
#  2. Use jsonify() to return JSON instead of HTML
#     from flask import jsonify
#  3. Add a decorator that prints a log message before every request:
#     @app.before_request
#     def log_request(): print("Request incoming!")
# ============================================================
