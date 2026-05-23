# ============================================================
#  DAY 56 — Static Files & Templates
#  PROJECT: Personal Name Card Website
# ============================================================
#
#  SKILLS TODAY:
#    - static/ folder for CSS, images, JS
#    - url_for("static", filename="style.css")  → correct static URL
#    - render_template with variables
#    - Creating a multi-file Flask project:
#        app.py
#        templates/index.html
#        static/style.css
#        static/profile.jpg (optional)
#
# ============================================================

from flask import Flask, render_template

app = Flask(__name__)

# User data (in a real app, this would come from a database)
user = {
    "name":       "wchen17",
    "title":      "Aspiring Python Developer",
    "email":      "apexofficial21@gmail.com",
    "github":     "https://github.com/wchen17",
    "bio":        "100 Days of Code — building skills one day at a time.",
    "skills":     ["Python", "Flask", "Selenium", "APIs", "Data Science"],
    "days_done":  56,
}


@app.route("/")
def home():
    return render_template("index.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
