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
