# ============================================================
#  DAY 58: Bootstrap CSS Framework
#  PROJECT: Bootstrap-styled Blog
# ============================================================
#
#  SKILLS TODAY:
#    - Bootstrap via CDN (no install needed)
#    - Bootstrap grid: container, row, col-md-X
#    - Bootstrap components: navbar, cards, buttons, badges
#    - Bootstrap utilities: m-3, p-4, text-center, bg-dark, etc.
#    - Combining Bootstrap with Jinja2 templates
#
#  HOW TO USE BOOTSTRAP:
#    Add to <head>:
#    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
#    Add before </body>:
#    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
#
# ============================================================

from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_posts():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    return resp.json()[:6]

@app.route("/")
def home():
    return render_template("index.html", posts=get_posts())

@app.route("/post/<int:post_id>")
def post(post_id):
    resp = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    return render_template("post.html", post=resp.json())

if __name__ == "__main__":
    app.run(debug=True)
