# ============================================================
#  DAY 59 — Bootstrap + Flask Blog (Capstone Part 2)
#  PROJECT: Full styled blog with real post data
# ============================================================
#
#  SKILLS TODAY:
#    - Bootstrap blog theme (Start Bootstrap "Clean Blog" template)
#    - ntoJson API → real blog posts from npoint.io or jsonplaceholder
#    - Jinja for loop over real post data
#    - header images per post
#    - Footer with social links
#
#  SETUP:
#    Download the "Clean Blog" template from startbootstrap.com
#    Or build from scratch using Day 58's Bootstrap skills
#
# ============================================================

from flask import Flask, render_template
import requests

app = Flask(__name__)

# Store posts on npoint.io (free JSON storage) or use jsonplaceholder
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"

@app.route("/")
def home():
    posts = requests.get(POSTS_URL).json()[:5]
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post_data = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}").json()
    return render_template("post.html", post=post_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
