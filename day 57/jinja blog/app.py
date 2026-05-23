# ============================================================
#  DAY 57 — Jinja2 Templating
#  PROJECT: Blog with dynamic posts from an API
# ============================================================
#
#  SKILLS TODAY:
#    - Jinja2 syntax inside HTML templates:
#        {{ variable }}           → output a value
#        {% if condition %}       → conditional block
#        {% for item in list %}   → loop
#        {% extends "base.html" %} → template inheritance
#        {% block content %} {% endblock %}
#    - Template inheritance: base layout + child templates
#    - Fetching real data from a JSON API to render dynamically
#
# ============================================================

from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()[:10]   # first 10 posts


@app.route("/")
def home():
    posts = get_posts()
    return render_template("index.html", posts=posts, title="My Blog")


# --------------------------------------------------
#  TODO 1: /post/<int:post_id> route
# --------------------------------------------------
# Fetch a single post: GET https://jsonplaceholder.typicode.com/posts/{id}
# Render post.html with the post data

@app.route("/post/<int:post_id>")
def get_post(post_id):
    pass   # TODO


if __name__ == "__main__":
    app.run(debug=True)
