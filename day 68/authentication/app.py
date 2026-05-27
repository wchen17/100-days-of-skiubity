# ============================================================
#  DAY 68: User Authentication with Flask
#  PROJECT: Secrets page (login required)
# ============================================================
#
#  SKILLS TODAY:
#    - werkzeug.security:
#        generate_password_hash(password)  → hash a password
#        check_password_hash(hash, password) → verify it
#    - flask_login:
#        LoginManager, UserMixin
#        login_user(user), logout_user(), login_required
#        current_user.is_authenticated
#    - Sessions: Flask uses signed cookies to remember who's logged in
#
#  pip install flask flask-sqlalchemy flask-login werkzeug flask-wtf
#
# ============================================================

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"


class User(UserMixin, db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    email    = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name     = db.Column(db.String(100))

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


# --------------------------------------------------
#  TODO 1: /register route
# --------------------------------------------------
# GET  → show registration form (email, name, password)
# POST → hash password, create User, save to DB, login_user, redirect /secrets
# If email already exists → flash error, redirect /login

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email    = request.form["email"]
        if db.session.execute(db.select(User).filter_by(email=email)).scalar():
            flash("Email already registered, log in instead.")
            return redirect(url_for("login"))
        hashed_pw = generate_password_hash(request.form["password"], method="pbkdf2:sha256", salt_length=8)
        new_user  = User(email=email, name=request.form["name"], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


# --------------------------------------------------
#  TODO 2: /login route
# --------------------------------------------------
# POST → find user by email, check_password_hash, login_user, redirect /secrets
# Wrong password or email → flash error

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email    = request.form["email"]
        password = request.form["password"]
        user     = db.session.execute(db.select(User).filter_by(email=email)).scalar()
        if not user:
            flash("Email not found.")
        elif not check_password_hash(user.password, password):
            flash("Incorrect password.")
        else:
            login_user(user)
            return redirect(url_for("secrets"))
    return render_template("login.html", logged_in=current_user.is_authenticated)


# --------------------------------------------------
#  Secrets page: only logged-in users can see this
# --------------------------------------------------
@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


# --------------------------------------------------
#  TODO 3: Protected file download
# --------------------------------------------------
# @app.route("/download")
# @login_required
# def download():
#     from flask import send_from_directory
#     return send_from_directory("static/files", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
