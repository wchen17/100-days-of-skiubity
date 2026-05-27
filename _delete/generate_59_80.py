import os
base = "/home/user/100-days-of-skiubity"
files = {}

files["day 59/blog capstone 2/app.py"] = """\
# ============================================================
#  DAY 59: Bootstrap + Flask Blog (Capstone Part 2)
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
"""

files["day 60/flask forms/app.py"] = """\
# ============================================================
#  DAY 60: POST Requests & HTML Forms in Flask
#  PROJECT: Contact form that sends an email
# ============================================================
#
#  SKILLS TODAY:
#    - <form method="POST" action="/path">
#    - from flask import request
#    - request.method == "POST"
#    - request.form["field_name"]      → get form data
#    - redirect(url_for("function"))   → redirect after POST
#    - flash(message) / get_flashed_messages()  → one-time messages
#    - The POST-Redirect-GET pattern (prevents double submit on refresh)
#
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os

app = Flask(__name__)
app.secret_key = "your-secret-key-here"   # required for flash messages

MY_EMAIL    = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name    = request.form["name"]
        email   = request.form["email"]
        phone   = request.form["phone"]
        message = request.form["message"]

        print(f"New contact from {name} ({email}): {message}")

        # --------------------------------------------------
        #  TODO: Send email with the contact form data
        # --------------------------------------------------
        # with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        #     smtp.starttls()
        #     smtp.login(MY_EMAIL, MY_PASSWORD)
        #     smtp.sendmail(MY_EMAIL, MY_EMAIL,
        #         f"Subject: New Contact\\n\\nName: {name}\\nEmail: {email}\\nPhone: {phone}\\nMessage: {message}")

        # POST-Redirect-GET: redirect back to avoid double-submit
        return redirect(url_for("home"))

    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 60/flask forms/templates/contact.html"] = """\
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Contact</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
<div class="container mt-5" style="max-width:600px">
    <h1>Contact Me</h1>

    {% if msg_sent %}
    <div class="alert alert-success">Your message has been sent!</div>
    {% endif %}

    <!-- TODO: complete the form -->
    <form method="POST" action="/contact">
        <div class="mb-3">
            <label class="form-label">Name</label>
            <input type="text" name="name" class="form-control" required>
        </div>
        <div class="mb-3">
            <label class="form-label">Email</label>
            <input type="email" name="email" class="form-control" required>
        </div>
        <!-- TODO: add phone number field -->
        <!-- TODO: add message textarea -->
        <button type="submit" class="btn btn-primary">Send</button>
    </form>
</div>
</body>
</html>
"""

files["day 61/wtforms/app.py"] = """\
# ============================================================
#  DAY 61: Flask-WTForms
#  PROJECT: Hardened contact form with validation & CSRF protection
# ============================================================
#
#  SKILLS TODAY:
#    - from flask_wtf import FlaskForm
#    - from wtforms import StringField, SubmitField, TextAreaField
#    - from wtforms.validators import DataRequired, Email, Length
#    - CSRF protection (automatic with Flask-WTF)
#    - form.validate_on_submit()  → checks method + validators
#    - {{ form.hidden_tag() }}    → renders CSRF token in template
#    - {{ form.field() }}         → renders form field as HTML
#    - {{ form.field.errors }}    → display validation errors
#
#  pip install flask-wtf email-validator
#
# ============================================================

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "change-me-in-production")


class ContactForm(FlaskForm):
    name    = StringField("Name",    validators=[DataRequired(), Length(min=2, max=50)])
    email   = StringField("Email",   validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=10)])
    submit  = SubmitField("Send Message")


# --------------------------------------------------
#  TODO: Add a second form: LoginForm
# --------------------------------------------------
# Fields: username (StringField), password (PasswordField)
# Validators: DataRequired on both
# from wtforms import PasswordField

class LoginForm(FlaskForm):
    pass   # TODO


@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        print(f"From: {form.name.data}, {form.email.data}")
        print(f"Message: {form.message.data}")
        return redirect(url_for("success"))
    return render_template("contact.html", form=form)


@app.route("/success")
def success():
    return "<h1>Message sent!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 61/wtforms/templates/contact.html"] = """\
<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
<div class="container mt-5" style="max-width:600px">
    <h1>Contact</h1>
    <form method="POST">
        {{ form.hidden_tag() }}

        <div class="mb-3">
            {{ form.name.label(class="form-label") }}
            {{ form.name(class="form-control") }}
            {% for error in form.name.errors %}
                <span class="text-danger">{{ error }}</span>
            {% endfor %}
        </div>

        <div class="mb-3">
            {{ form.email.label(class="form-label") }}
            {{ form.email(class="form-control") }}
            {% for error in form.email.errors %}
                <span class="text-danger">{{ error }}</span>
            {% endfor %}
        </div>

        <!-- TODO: add message textarea in same pattern -->

        {{ form.submit(class="btn btn-primary") }}
    </form>
</div>
</body>
</html>
"""

files["day 62/coffee wifi/app.py"] = """\
# ============================================================
#  DAY 62: WTForms + CSV
#  PROJECT: Coffee & Wifi: "Where can I work remotely?" site
# ============================================================
#
#  SKILLS TODAY:
#    - Combining Flask-WTF forms with CSV file storage
#    - SelectField in WTForms → dropdown menus
#    - Reading/writing CSV with the csv module
#    - Displaying a table of cafes in a Jinja template
#    - Rating symbols: ☕ ✘ ✅ 💪
#
# ============================================================

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv
import os

app = Flask(__name__)
app.secret_key = "secret"

CSV_FILE = "cafes.csv"

# Create sample CSV if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Cafe Name", "Location", "Open", "Close", "Coffee", "Wifi", "Power"])
        writer.writerow(["Brew Bros", "London", "8am", "6pm", "☕☕☕", "✅", "💪💪"])
        writer.writerow(["The Grind", "Manchester", "7am", "8pm", "☕☕☕☕", "✅", "💪"])


RATINGS = [("", "Rate"), ("✅", "✅"), ("❌", "❌"), ("☕", "☕"), ("☕☕", "☕☕"), ("☕☕☕", "☕☕☕"), ("☕☕☕☕", "☕☕☕☕"), ("☕☕☕☕☕", "☕☕☕☕☕")]


class CafeForm(FlaskForm):
    cafe        = StringField("Cafe Name",     validators=[DataRequired()])
    location    = StringField("Location URL",  validators=[DataRequired(), URL()])
    open_time   = StringField("Opening Time",  validators=[DataRequired()])
    close_time  = StringField("Closing Time",  validators=[DataRequired()])
    coffee      = SelectField("Coffee Rating", choices=RATINGS)
    wifi        = SelectField("Wifi Rating",   choices=RATINGS)
    power       = SelectField("Power Rating",  choices=RATINGS)
    submit      = SubmitField("Add Cafe")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    with open(CSV_FILE, newline="") as f:
        rows = list(csv.reader(f))
    return render_template("cafes.html", cafes=rows[1:], header=rows[0])


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                form.cafe.data, form.location.data,
                form.open_time.data, form.close_time.data,
                form.coffee.data, form.wifi.data, form.power.data
            ])
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 63/sqlite intro/app.py"] = """\
# ============================================================
#  DAY 63: SQLite & SQLAlchemy
#  PROJECT: Book Library Database
# ============================================================
#
#  SKILLS TODAY:
#    - from flask_sqlalchemy import SQLAlchemy
#    - app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///name.db"
#    - class Book(db.Model):  → defines a table
#        id      = db.Column(db.Integer, primary_key=True)
#        title   = db.Column(db.String(250), nullable=False)
#        rating  = db.Column(db.Float, nullable=False)
#    - db.create_all()        → creates the table if not exists
#    - db.session.add(obj)    → stage a new row
#    - db.session.commit()    → save to disk
#    - db.session.delete(obj) → delete a row
#    - Book.query.all()       → SELECT all
#    - Book.query.get(id)     → SELECT by primary key
#    - Book.query.filter_by(title="X").first()
#
#  pip install flask flask-sqlalchemy
#
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)


# --------------------------------------------------
#  Database Model
# --------------------------------------------------
class Book(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()


# --------------------------------------------------
#  Routes
# --------------------------------------------------
@app.route("/")
def home():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title  = request.form["title"],
            author = request.form["author"],
            rating = float(request.form["rating"]),
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


# --------------------------------------------------
#  TODO 1: /edit-rating/<int:book_id> route
# --------------------------------------------------
# GET  → show form pre-filled with current rating
# POST → update book.rating, commit, redirect to home

@app.route("/edit-rating/<int:book_id>", methods=["GET", "POST"])
def edit_rating(book_id):
    book = db.get_or_404(Book, book_id)
    if request.method == "POST":
        pass   # TODO: update rating and commit
    return render_template("edit.html", book=book)


# --------------------------------------------------
#  TODO 2: /delete/<int:book_id> route
# --------------------------------------------------
# Find the book, delete it, commit, redirect to home

@app.route("/delete/<int:book_id>")
def delete(book_id):
    pass   # TODO


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 64/movies website/app.py"] = """\
# ============================================================
#  DAY 64: SQLAlchemy + TMDB API
#  PROJECT: My Top 10 Movies Website
# ============================================================
#
#  SKILLS TODAY:
#    - CRUD with SQLAlchemy (Create, Read, Update, Delete)
#    - TMDB API (themoviedb.org) → search for movies
#    - Ranking movies by personal rating (1-10)
#    - WTForms for add/edit
#    - Rendering a "top 10" card layout with Bootstrap
#
#  SETUP:
#    pip install flask flask-sqlalchemy flask-wtf requests
#    Get a free TMDB API key at themoviedb.org
#
# ============================================================

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.secret_key = "secret"
db  = SQLAlchemy(app)

TMDB_KEY = os.getenv("TMDB_API_KEY", "demo")


class Movie(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(250), unique=True, nullable=False)
    year        = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating      = db.Column(db.Float, nullable=True)
    ranking     = db.Column(db.Integer, nullable=True)
    review      = db.Column(db.String(250), nullable=True)
    img_url     = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating (out of 10)", validators=[DataRequired()])
    review = StringField("Your Review",            validators=[DataRequired()])
    submit = SubmitField("Done")


class FindMovieForm(FlaskForm):
    title  = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i, movie in enumerate(all_movies):
        movie.ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={"api_key": TMDB_KEY, "query": movie_title},
        )
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_api_id}",
            params={"api_key": TMDB_KEY, "language": "en-US"},
        )
        data = response.json()
        new_movie = Movie(
            title       = data["title"],
            year        = data["release_date"].split("-")[0],
            description = data["overview"],
            img_url     = f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


# --------------------------------------------------
#  TODO: Complete edit and delete routes
# --------------------------------------------------
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form     = RateMovieForm()
    movie_id = request.args.get("id")
    movie    = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie    = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 65/web design notes.md"] = """\
# Day 65: Web Design Principles

## What to Study Today

This day is about **design theory**, not coding. Take notes and apply them to your Day 59 blog.

### Colour Theory
- **60-30-10 rule**: 60% dominant colour, 30% secondary, 10% accent
- Use tools: coolors.co, color.adobe.com
- Contrast checker: webaim.org/resources/contrastchecker

### Typography
- Font pairing: serif + sans-serif (heading + body)
- Recommended: Google Fonts (fonts.google.com)
- Rules: max 2 fonts, body >= 16px, line-height >= 1.5

### UI/UX Principles
- **Hierarchy**: biggest/boldest = most important
- **Alignment**: things that belong together should align
- **Whitespace**: breathing room makes things legible
- **Consistency**: same colours, same spacing throughout

### Practical Tools
- Figma (free): design mockups before coding
- Canva: quick graphics
- Coolors: colour palettes
- Unsplash: free high-quality photos
- Font Awesome: icons (fontawesome.com)

## TODO: Redesign Your Blog

1. Go back to your Day 59 blog
2. Choose a colour palette (3 colours max)
3. Pick a Google Fonts pairing (e.g. Playfair Display + Lato)
4. Improve spacing: add more padding/margin to cards
5. Add a hero image using Unsplash
6. Check mobile responsiveness in browser DevTools (F12 → mobile view)

## STRETCH GOALS
1. Build a Figma mockup of your ideal blog before coding it
2. Implement dark mode with CSS variables + a toggle button
3. Add a Google Font to your Day 56 name card
"""

files["day 66/rest api/app.py"] = """\
# ============================================================
#  DAY 66: Building a REST API with Flask
#  PROJECT: Cafe Finder API
# ============================================================
#
#  SKILLS TODAY:
#    - REST principles: GET / POST / PUT / PATCH / DELETE
#    - jsonify()                → return JSON from Flask
#    - request.args.get()       → URL query params
#    - request.get_json()       → JSON request body
#    - HTTP status codes:
#        200 OK, 201 Created, 400 Bad Request, 404 Not Found
#    - Documenting your API
#    - Testing with Postman or curl
#
# ============================================================

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(app)


class Cafe(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(250), unique=True, nullable=False)
    map_url      = db.Column(db.String(500), nullable=False)
    img_url      = db.Column(db.String(500), nullable=False)
    location     = db.Column(db.String(250), nullable=False)
    has_sockets  = db.Column(db.Boolean, nullable=False)
    has_toilet   = db.Column(db.Boolean, nullable=False)
    has_wifi     = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats        = db.Column(db.String(250), nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

with app.app_context():
    db.create_all()


# --------------------------------------------------
#  GET /random  → random cafe
# --------------------------------------------------
@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    if not all_cafes:
        return jsonify(error="No cafes in database"), 404
    cafe = random.choice(all_cafes)
    return jsonify(cafe=cafe.to_dict())


# --------------------------------------------------
#  GET /all  → all cafes
# --------------------------------------------------
@app.route("/all")
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    return jsonify(cafes=[c.to_dict() for c in cafes])


# --------------------------------------------------
#  GET /search?loc=London  → filter by location
# --------------------------------------------------
@app.route("/search")
def search_cafe():
    location = request.args.get("loc")
    cafes    = db.session.execute(db.select(Cafe).filter_by(location=location)).scalars().all()
    if cafes:
        return jsonify(cafes=[c.to_dict() for c in cafes])
    return jsonify(error={"Not Found": f"No cafes found in {location}"}), 404


# --------------------------------------------------
#  POST /add  → add a new cafe
# --------------------------------------------------
@app.route("/add", methods=["POST"])
def post_new_cafe():
    data = request.get_json() or request.form
    new_cafe = Cafe(
        name            = data.get("name"),
        map_url         = data.get("map_url"),
        img_url         = data.get("img_url"),
        location        = data.get("location"),
        has_sockets     = bool(data.get("has_sockets")),
        has_toilet      = bool(data.get("has_toilet")),
        has_wifi        = bool(data.get("has_wifi")),
        can_take_calls  = bool(data.get("can_take_calls")),
        seats           = data.get("seats"),
        coffee_price    = data.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 201


# --------------------------------------------------
#  TODO 1: PATCH /update-price/<cafe_id>  → update coffee price
# --------------------------------------------------
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    new_price = request.args.get("new_price")
    # TODO: update cafe.coffee_price, commit, return success JSON
    pass


# --------------------------------------------------
#  TODO 2: DELETE /report-closed/<cafe_id>  → delete a cafe
# --------------------------------------------------
# Require an api-key param for security: if api-key != "TopSecretAPIKey" → 403
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != "TopSecretAPIKey":
        return jsonify(error="Sorry, that's not allowed."), 403
    # TODO: find and delete the cafe
    pass


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 67/blog rest/app.py"] = """\
# ============================================================
#  DAY 67: Blog Capstone Part 3: RESTful Routing
#  PROJECT: Blog with full CRUD via REST routes
# ============================================================
#
#  SKILLS TODAY:
#    - Full CRUD on a blog:
#        GET  /posts          → list all
#        GET  /posts/<id>     → single post
#        POST /new-post       → create
#        PUT  /edit-post/<id> → update
#        DELETE /delete/<id>  → delete
#    - CKEditor for rich text: pip install flask-ckeditor
#    - Gravatar for author images
#    - datetime in Jinja templates
#
# ============================================================

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from datetime import date
import os

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    title    = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date     = db.Column(db.String(250), nullable=False)
    body     = db.Column(db.Text,        nullable=False)
    author   = db.Column(db.String(250), nullable=False)
    img_url  = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()


class CreatePostForm(FlaskForm):
    title    = StringField("Title",        validators=[DataRequired()])
    subtitle = StringField("Subtitle",     validators=[DataRequired()])
    author   = StringField("Author",       validators=[DataRequired()])
    img_url  = StringField("Image URL",    validators=[DataRequired(), URL()])
    body     = StringField("Blog Content", validators=[DataRequired()])
    submit   = SubmitField("Submit Post")


@app.route("/")
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=post)

@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title    = form.title.data,
            subtitle = form.subtitle.data,
            body     = form.body.data,
            author   = form.author.data,
            img_url  = form.img_url.data,
            date     = date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, is_edit=False)

# --------------------------------------------------
#  TODO 1: /edit-post/<int:post_id>
# --------------------------------------------------
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    # Pre-fill form with existing data, save changes on POST
    pass

# --------------------------------------------------
#  TODO 2: /delete/<int:post_id>
# --------------------------------------------------
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    pass

if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 68/authentication/app.py"] = """\
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
"""

files["day 69/blog with users/app.py"] = """\
# ============================================================
#  DAY 69: Blog Capstone Part 4: Multi-User Blog
#  PROJECT: Full blog with registration, login, comments
# ============================================================
#
#  SKILLS TODAY:
#    - SQLAlchemy relationships (one-to-many):
#        User → many BlogPosts
#        BlogPost → many Comments
#    - db.relationship() and db.ForeignKey()
#    - @admin_only decorator using functools.wraps
#    - Gravatar profile pictures via flask-gravatar
#    - Preventing non-admins from creating/editing/deleting posts
#
#  pip install flask-login flask-gravatar flask-sqlalchemy flask-wtf
#
# ============================================================

from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy(app)
login_manager = LoginManager(app)


# --------------------------------------------------
#  Models with relationships
# --------------------------------------------------
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id       = db.Column(db.Integer, primary_key=True)
    email    = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name     = db.Column(db.String(100))
    posts    = db.relationship("BlogPost", back_populates="author")
    comments = db.relationship("Comment",  back_populates="comment_author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id        = db.Column(db.Integer, primary_key=True)
    title     = db.Column(db.String(250), unique=True, nullable=False)
    body      = db.Column(db.Text,        nullable=False)
    date      = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author    = db.relationship("User", back_populates="posts")
    comments  = db.relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id              = db.Column(db.Integer, primary_key=True)
    text            = db.Column(db.Text, nullable=False)
    author_id       = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author  = db.relationship("User", back_populates="comments")
    post_id         = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post     = db.relationship("BlogPost", back_populates="comments")

with app.app_context():
    db.create_all()


# --------------------------------------------------
#  Admin-only decorator
# --------------------------------------------------
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route("/")
def home():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", posts=posts)


# --------------------------------------------------
#  TODO: Implement register, login, logout (same as Day 68)
#  TODO: Add comment form to post page
#  TODO: Admin-only create/edit/delete post routes
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 70/deployment notes.md"] = """\
# Day 70: Git & Deployment

## Skills Today
- Git: branches, merging, .gitignore
- Deploying a Flask app to the cloud

## Deployment Options (2025/2026)
Heroku removed its free tier, so use one of these instead:

### Option 1: Render (recommended, free tier)
1. Push your Flask app to GitHub
2. Go to render.com → New → Web Service
3. Connect your GitHub repo
4. Set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Add environment variables in the Render dashboard

### Option 2: Railway.app (free trial credits)
1. Push to GitHub
2. railway.app → New Project → Deploy from GitHub repo
3. Set start command: `gunicorn app:app`

### Option 3: PythonAnywhere (free forever for Flask)
1. Sign up at pythonanywhere.com
2. Upload files or clone from GitHub
3. Set up a WSGI config file

## TODO: Deploy Your Day 67 or 69 Blog

### Pre-deployment checklist
- [ ] `requirements.txt` exists (`pip freeze > requirements.txt`)
- [ ] `Procfile` exists: `web: gunicorn app:app`
- [ ] Debug mode is OFF in production: `app.run(debug=False)`
- [ ] SECRET_KEY is an environment variable (not hardcoded)
- [ ] Database URI works in production (use PostgreSQL not SQLite for Render)
- [ ] `.gitignore` excludes `.env`, `*.db`, `__pycache__`

### Sample `.gitignore`
```
.env
*.db
__pycache__/
*.pyc
.DS_Store
token.txt
```

### Sample `requirements.txt` (Flask app)
```
flask
flask-sqlalchemy
flask-login
flask-wtf
gunicorn
psycopg2-binary
python-dotenv
```

## Stretch Goals
1. Set up a custom domain for your deployed app
2. Add HTTPS (Render handles this automatically)
3. Set up continuous deployment: push to GitHub → auto-deploys
"""

files["day 71/pandas college majors.py"] = """\
# ============================================================
#  DAY 71: Pandas Data Exploration
#  PROJECT: College Major vs Salary Analysis
# ============================================================
#
#  SKILLS TODAY:
#    - pd.read_csv()
#    - df.shape, df.columns, df.dtypes
#    - df.head(n) / df.tail(n)
#    - df.describe()           → summary statistics
#    - df.sort_values("col", ascending=False)
#    - df["col"].max() / .min() / .mean()
#    - df[ df["col"] > value ] → boolean filtering
#    - NaN handling: df.dropna() / df.fillna(0)
#    - df[ ["col1", "col2"] ]  → select multiple columns
#
#  pip install pandas
#
# ============================================================

import pandas as pd

# --------------------------------------------------
#  Dataset: Post-university salary by major
#  Source: Wall Street Journal / PayScale (available on Kaggle)
#  For practice, create a mini version:
# --------------------------------------------------
data = {
    "Undergraduate Major":     ["Python/CS", "Electrical Engineering", "Philosophy", "Economics", "Biology", "Art"],
    "Starting Median Salary":  [70200, 63900, 42200, 50100, 36900, 32600],
    "Mid-Career Median Salary":[109000, 112000, 76100, 99200, 62000, 50000],
    "% Change":                [55, 75, 80, 98, 68, 53],
    "Mid-Career 90th Percentile Salary": [162000, 178000, 130000, 201000, 120000, 95000],
}
df = pd.DataFrame(data)

print("Shape:", df.shape)
print("\\nFirst few rows:")
print(df.head())
print("\\nSummary stats:")
print(df.describe())


# --------------------------------------------------
#  TODO 1: Which major has the highest starting salary?
# --------------------------------------------------
# Use df.sort_values() and print the top 3

# --------------------------------------------------
#  TODO 2: Which major has the highest % salary growth?
# --------------------------------------------------
# (highest "% Change")

# --------------------------------------------------
#  TODO 3: Which majors have mid-career salary below 60,000?
# --------------------------------------------------
# Use boolean filtering

# --------------------------------------------------
#  TODO 4: Add a new column "Salary Spread"
# --------------------------------------------------
# Spread = 90th percentile - mid-career median
# df["Salary Spread"] = ...
# Which major has the biggest spread? (means highest earners earn MUCH more than the median)

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download the full dataset from Kaggle and redo this analysis
#  2. Group by category (STEM / Business / Arts / Humanities)
#     using df.groupby("Category")["Starting Median Salary"].mean()
#  3. Plot a bar chart using matplotlib (preview of Day 72)
# ============================================================
"""

files["day 72/matplotlib charts.py"] = """\
# ============================================================
#  DAY 72: Data Visualisation with Matplotlib
#  PROJECT: Programming Language Popularity Over Time
# ============================================================
#
#  SKILLS TODAY:
#    - import matplotlib.pyplot as plt
#    - plt.plot(x, y, label="name")    → line chart
#    - plt.bar(x, height)              → bar chart
#    - plt.xlabel() / plt.ylabel() / plt.title()
#    - plt.legend()
#    - plt.show()
#    - plt.figure(figsize=(width, height))
#    - plt.xticks(rotation=45)
#    - Multiple subplots: plt.subplot(rows, cols, index)
#    - Styling: color, linewidth, marker, linestyle
#
#  pip install matplotlib pandas
#
# ============================================================

import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------------
#  DEMO: Basic line chart
# --------------------------------------------------
years   = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
python  = [6.4,  7.8,  9.5, 11.0, 12.2, 15.0, 17.3, 19.5, 22.1]
java    = [20.1, 18.5, 17.0, 16.0, 14.8, 13.5, 12.0, 11.2, 10.5]
js      = [14.0, 13.5, 13.2, 12.8, 12.5, 12.0, 11.8, 11.5, 11.2]

plt.figure(figsize=(12, 6))
plt.plot(years, python, label="Python",     color="blue",   linewidth=2, marker="o")
plt.plot(years, java,   label="Java",       color="red",    linewidth=2, marker="s")
plt.plot(years, js,     label="JavaScript", color="yellow", linewidth=2, marker="^")
plt.xlabel("Year")
plt.ylabel("Popularity (%)")
plt.title("Programming Language Popularity 2016-2024")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# --------------------------------------------------
#  TODO 1: Bar chart: starting salaries by language
# --------------------------------------------------
languages = ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
salaries  = [90000, 82000, 88000, 95000, 105000, 110000]

# Create a horizontal bar chart (plt.barh) sorted by salary
# Add value labels on each bar

# --------------------------------------------------
#  TODO 2: Pie chart: market share of databases
# --------------------------------------------------
dbs    = ["PostgreSQL", "MySQL", "MongoDB", "SQLite", "Redis", "Other"]
shares = [36, 29, 18, 8, 5, 4]

# plt.pie(shares, labels=dbs, autopct="%1.1f%%", startangle=90)

# --------------------------------------------------
#  TODO 3: Subplot grid: 2x2 layout
# --------------------------------------------------
# Show all four chart types in a 2x2 grid:
# Top-left: line, top-right: bar, bottom-left: pie, bottom-right: scatter

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download Stack Overflow Developer Survey data and replicate
#     the "Most Loved Languages" chart
#  2. Animate your line chart using FuncAnimation
#  3. Save figures to file: plt.savefig("chart.png", dpi=150)
# ============================================================
"""

files["day 73/lego dataset.py"] = """\
# ============================================================
#  DAY 73: Data Aggregation & Merging
#  PROJECT: LEGO Dataset Analysis
# ============================================================
#
#  SKILLS TODAY:
#    - df.groupby("col").count()        → count by group
#    - df.groupby("col")["col2"].mean() → aggregate
#    - pd.merge(df1, df2, on="col")     → join two DataFrames
#    - df["col"].value_counts()         → frequency count
#    - Pivot tables: df.pivot_table()
#    - Reshaping: df.melt()
#
#  Dataset: LEGO database (rebrickable.com/downloads: free)
#  For practice, use a mini version below.
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# Mini LEGO dataset
sets = pd.DataFrame({
    "set_num":  ["001-1", "002-1", "003-1", "004-1", "005-1"],
    "name":     ["Classic Space", "Town Square", "Castle Keep", "Pirate Ship", "Farm Set"],
    "year":     [1978, 1980, 1982, 1990, 1991],
    "theme_id": [1,    2,    3,    4,    2],
    "num_parts":[183,  450,  700,  560,  200],
})

themes = pd.DataFrame({
    "theme_id": [1, 2, 3, 4],
    "name":     ["Space", "Town", "Castle", "Pirates"],
})

# --------------------------------------------------
#  TODO 1: Which theme has the most sets?
# --------------------------------------------------
# Merge sets with themes on theme_id
# Group by theme name and count

# --------------------------------------------------
#  TODO 2: Average parts per theme
# --------------------------------------------------
# groupby + mean on num_parts

# --------------------------------------------------
#  TODO 3: How has LEGO set size (num_parts) changed over time?
# --------------------------------------------------
# Group by year, take mean of num_parts, plot as line chart

# --------------------------------------------------
#  TODO 4: Find the biggest set in each theme
# --------------------------------------------------
# df.groupby("theme")["num_parts"].max()
# or: df.sort_values("num_parts").drop_duplicates("theme", keep="last")
"""

files["day 74/google trends.py"] = """\
# ============================================================
#  DAY 74: Time Series & Google Trends
#  PROJECT: Visualise search trends and spot correlations
# ============================================================
#
#  SKILLS TODAY:
#    - pd.to_datetime()                 → parse date strings
#    - df.resample("M").mean()          → resample to monthly
#    - df.rolling(window=n).mean()      → rolling average (smooth noise)
#    - Correlation: df.corr()           → correlation matrix
#    - Dual-axis charts: ax1 = plt.subplot(), ax2 = ax1.twinx()
#    - fill_between() for shaded areas
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Sample time series data (monthly search interest, 0-100)
dates = pd.date_range(start="2020-01-01", periods=36, freq="MS")

data = pd.DataFrame({
    "Month":        dates,
    "Python":       [60, 58, 62, 70, 68, 72, 75, 80, 78, 82, 85, 90,
                     88, 85, 90, 92, 95, 93, 97, 100, 98, 96, 99, 100,
                     95, 97, 100, 98, 96, 94, 97, 99, 100, 98, 97, 100],
    "Unemployment": [3.5, 3.5, 13.0, 14.7, 13.3, 11.1, 10.2, 8.4, 7.9, 6.9, 6.7, 6.7,
                     6.4, 6.2, 6.0, 5.9, 5.8, 5.9, 5.4, 5.2, 4.8, 4.6, 4.2, 3.9,
                     3.7, 3.6, 3.5, 3.7, 3.8, 3.6, 3.5, 3.4, 3.7, 3.9, 4.0, 3.8],
})
data.set_index("Month", inplace=True)


# --------------------------------------------------
#  TODO 1: Plot Python search trend as a line chart
# --------------------------------------------------
# Use plt.figure, plt.plot, date formatting on x-axis

# --------------------------------------------------
#  TODO 2: Plot unemployment rate on a SECOND y-axis
# --------------------------------------------------
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax2.plot(data.index, data["Unemployment"], color="red")

# --------------------------------------------------
#  TODO 3: Apply a 3-month rolling average to smooth the lines
# --------------------------------------------------
# data["Python_smooth"] = data["Python"].rolling(3).mean()

# --------------------------------------------------
#  TODO 4: Calculate and print the correlation between the two series
# --------------------------------------------------
# print(data.corr())

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download real data from trends.google.com → Download CSV
#  2. Compare "Bitcoin" vs "Tesla" search interest
#  3. Add a shaded recession period using plt.axvspan()
# ============================================================
"""

files["day 75/plotly charts.py"] = """\
# ============================================================
#  DAY 75: Interactive Charts with Plotly
#  PROJECT: Android App Store Analysis Dashboard
# ============================================================
#
#  SKILLS TODAY:
#    - import plotly.express as px          → high-level API
#    - import plotly.graph_objects as go    → low-level API
#    - px.scatter(), px.bar(), px.pie(), px.line()
#    - hover_data, color, size, title parameters
#    - fig.show()  → opens in browser (interactive!)
#    - pip install plotly pandas
#
# ============================================================

import plotly.express as px
import pandas as pd

# Sample app store data
data = pd.DataFrame({
    "App":      ["TikTok", "Instagram", "WhatsApp", "YouTube", "Spotify", "Netflix", "Twitter", "Snapchat"],
    "Category": ["Social", "Social",   "Social",   "Video",   "Music",   "Video",   "Social",  "Social"],
    "Rating":   [4.7, 4.6, 4.4, 4.5, 4.8, 4.5, 4.0, 4.2],
    "Reviews":  [15000000, 12000000, 9000000, 11000000, 8000000, 7000000, 4000000, 5000000],
    "Size_MB":  [170, 45, 50, 110, 80, 170, 60, 75],
    "Installs": [3000, 2000, 5000, 8000, 2000, 1000, 500, 1500],
})


# --------------------------------------------------
#  TODO 1: Scatter plot: Rating vs Size
# --------------------------------------------------
# Color by category, size by installs, hover shows app name

# fig = px.scatter(data, x="Size_MB", y="Rating", color="Category",
#                  size="Installs", hover_name="App", title="App Rating vs Size")
# fig.show()


# --------------------------------------------------
#  TODO 2: Bar chart: Average rating by category
# --------------------------------------------------
avg_by_cat = data.groupby("Category")["Rating"].mean().reset_index()
# fig = px.bar(avg_by_cat, x="Category", y="Rating", ...)
# fig.show()


# --------------------------------------------------
#  TODO 3: Pie chart: Installs by category
# --------------------------------------------------
# fig = px.pie(data, values="Installs", names="Category", title="...")
# fig.show()


# --------------------------------------------------
#  TODO 4: Box plot: Rating distribution by category
# --------------------------------------------------
# fig = px.box(data, x="Category", y="Rating", points="all")
# fig.show()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download the real Google Play Store dataset from Kaggle
#  2. Build a Dash app (pip install dash) to show all charts in one page
#  3. Add a sunburst chart: category → app → install count
# ============================================================
"""

files["day 76/numpy.py"] = """\
# ============================================================
#  DAY 76: NumPy Array Computation
#  PROJECT: Image manipulation + statistical computation
# ============================================================
#
#  SKILLS TODAY:
#    - import numpy as np
#    - np.array([...])                → create array
#    - np.zeros((r, c)) / np.ones()  → pre-filled arrays
#    - np.arange(start, stop, step)  → range as array
#    - np.linspace(a, b, n)          → n evenly spaced points
#    - array.shape / .ndim / .dtype
#    - Array maths: +, -, *, /       → element-wise, no loops needed
#    - np.mean() / np.max() / np.std()
#    - Boolean indexing: arr[arr > 5]
#    - np.random.rand() / np.random.randint()
#    - Broadcasting: operations on different-shaped arrays
#    - pip install numpy matplotlib
#
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
#  DEMO: Array vs Python list
# --------------------------------------------------
py_list  = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

# Element-wise multiplication: lists can't do this:
print(np_array * 2)          # [2 4 6 8 10]
print(np_array ** 2)         # [1 4 9 16 25]
print(np_array[np_array > 3])  # [4 5]


# --------------------------------------------------
#  TODO 1: 2D arrays (matrices)
# --------------------------------------------------
# Create a 5×5 identity matrix using np.eye(5)
# Create a 3×3 matrix of random integers 0-9
# Multiply them together using the @ operator (matrix multiply)

# --------------------------------------------------
#  TODO 2: Statistical analysis
# --------------------------------------------------
# Simulate 1000 dice rolls: np.random.randint(1, 7, size=1000)
# Calculate: mean, std, min, max, and the frequency of each face (1-6)
# Plot as a bar chart

rolls = np.random.randint(1, 7, size=1000)
# your analysis here


# --------------------------------------------------
#  TODO 3: Image as a NumPy array
# --------------------------------------------------
# Create a 100×100 greyscale gradient image
# rows = np.linspace(0, 255, 100).astype(np.uint8)
# image = np.tile(rows, (100, 1))
# plt.imshow(image, cmap="gray")
# plt.show()

# Then: flip it, rotate it, add noise, threshold it


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Load a real image: from PIL import Image; np.array(Image.open("photo.jpg"))
#  2. Apply a blur using np.convolve or scipy.ndimage.uniform_filter
#  3. Create a Mandelbrot set visualisation using NumPy broadcasting
# ============================================================
"""

files["day 77/linear regression.py"] = """\
# ============================================================
#  DAY 77: Linear Regression & Seaborn
#  PROJECT: Predict values with a regression line
# ============================================================
#
#  SKILLS TODAY:
#    - import seaborn as sns            → statistical visualisation
#    - sns.regplot(x, y, data=df)       → scatter + regression line
#    - from sklearn.linear_model import LinearRegression
#    - model = LinearRegression()
#    - model.fit(X, y)                  → train the model
#    - model.predict([[value]])         → make a prediction
#    - model.coef_ / model.intercept_   → slope and y-intercept
#    - r² score: model.score(X, y)      → how well the line fits
#    - pip install scikit-learn seaborn matplotlib pandas
#
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample dataset: study hours vs exam score
np.random.seed(42)
hours = np.random.uniform(1, 10, 50)
scores = 7 * hours + np.random.normal(0, 5, 50) + 30

df = pd.DataFrame({"Study Hours": hours, "Exam Score": scores})


# --------------------------------------------------
#  TODO 1: Plot with seaborn regplot
# --------------------------------------------------
# sns.regplot(x="Study Hours", y="Exam Score", data=df)
# Add title, labels, show


# --------------------------------------------------
#  TODO 2: Fit a LinearRegression model
# --------------------------------------------------
# X = df[["Study Hours"]]   ← must be 2D for sklearn
# y = df["Exam Score"]
# model.fit(X, y)
# Print slope, intercept, r² score

X = df[["Study Hours"]]
y = df["Exam Score"]

model = LinearRegression()
# TODO: fit the model
# print(f"Slope: {model.coef_[0]:.2f}")
# print(f"Intercept: {model.intercept_:.2f}")
# print(f"R² score: {model.score(X, y):.3f}")


# --------------------------------------------------
#  TODO 3: Make predictions
# --------------------------------------------------
# What score would someone who studied 8 hours get?
# prediction = model.predict([[8]])
# print(f"Predicted score for 8 hours study: {prediction[0]:.1f}")


# --------------------------------------------------
#  TODO 4: Residuals analysis
# --------------------------------------------------
# residuals = y - model.predict(X)
# Plot a histogram of residuals: should be roughly normal


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Use multiple regression: add a "Attendance %" feature
#  2. Try polynomial regression for curved relationships
#     from sklearn.preprocessing import PolynomialFeatures
#  3. Split data into train/test sets to evaluate generalisation
#     from sklearn.model_selection import train_test_split
# ============================================================
"""

files["day 78/nobel prize analysis.py"] = """\
# ============================================================
#  DAY 78: Multi-library Data Analysis
#  PROJECT: Nobel Prize Winners Dataset
# ============================================================
#
#  SKILLS TODAY:
#    - Combining pandas, matplotlib, seaborn, and plotly
#    - Categorical data analysis
#    - Time series (prizes over decades)
#    - Choropleth map with plotly (prizes by country)
#    - Sunburst / treemap charts
#
#  Dataset: from Kaggle "Nobel Prize": or use sample below
#
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mini Nobel dataset
data = pd.DataFrame({
    "Year":     [1901, 1903, 1906, 1921, 1964, 1993, 2015, 2020, 2022],
    "Category": ["Physics","Physics","Chemistry","Physics","Chemistry","Peace","Medicine","Medicine","Physics"],
    "Country":  ["Germany","France","Germany","Germany","UK","South Africa","Japan","USA","France"],
    "Gender":   ["Male","Female","Male","Male","Female","Male","Male","Male","Male"],
    "Name":     ["Röntgen","Curie","Moissan","Einstein","Hodgkin","Mandela","Ōmura","Harvey","Aspect"],
})


# --------------------------------------------------
#  TODO 1: Which category has the most prizes?
# --------------------------------------------------
# data["Category"].value_counts()  → plot as bar chart


# --------------------------------------------------
#  TODO 2: Prizes by decade
# --------------------------------------------------
# data["Decade"] = (data["Year"] // 10) * 10
# Group by decade, count, plot as line chart


# --------------------------------------------------
#  TODO 3: Gender breakdown
# --------------------------------------------------
# How many female laureates per category?
# data[data["Gender"] == "Female"].groupby("Category").count()


# --------------------------------------------------
#  TODO 4: Prize distribution by country (choropleth)
# --------------------------------------------------
# import plotly.express as px
# country_counts = data["Country"].value_counts().reset_index()
# fig = px.choropleth(country_counts, locations="Country",
#                     locationmode="country names",
#                     color="count", title="Nobel Prizes by Country")
# fig.show()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Download the full dataset from Kaggle (900+ records)
#  2. Find the average age at prize time (birth year vs prize year)
#  3. Build an interactive Dash dashboard for the full analysis
# ============================================================
"""

files["day 79/handwashing stats.py"] = """\
# ============================================================
#  DAY 79: Statistical Testing
#  PROJECT: Dr. Semmelweis Handwashing Discovery (t-test)
# ============================================================
#
#  SKILLS TODAY:
#    - Hypothesis testing: null hypothesis vs alternative
#    - from scipy import stats
#    - stats.ttest_ind(group1, group2)  → independent t-test
#    - p-value interpretation (p < 0.05 = statistically significant)
#    - Confidence intervals
#    - Before/after comparison
#
#  pip install scipy pandas matplotlib
#
# ============================================================

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dr. Semmelweis found that handwashing dramatically reduced deaths
# Here's monthly death rates (%) before and after mandatory handwashing

before_washing = [10.0, 8.5, 9.2, 11.0, 12.3, 10.8, 9.5, 11.2, 10.1, 9.8, 11.5, 12.0]
after_washing  = [2.1,  1.9,  2.5,  1.8,  2.3,  2.0,  1.7,  2.2,  1.9,  2.1,  2.4,  2.0]

before = np.array(before_washing)
after  = np.array(after_washing)

# --------------------------------------------------
#  TODO 1: Calculate basic statistics for both groups
# --------------------------------------------------
# Print mean, std, and range for before and after

print("Before handwashing:")
print(f"  Mean: {before.mean():.2f}%")
# TODO: print std, min, max

print("\\nAfter handwashing:")
# TODO: same


# --------------------------------------------------
#  TODO 2: Visualise the distributions
# --------------------------------------------------
# Plot two overlapping histograms (before = red, after = blue)
# Add vertical lines for the means


# --------------------------------------------------
#  TODO 3: Run an independent t-test
# --------------------------------------------------
# t_stat, p_value = stats.ttest_ind(before, after)
# If p_value < 0.05 → the difference is statistically significant

t_stat, p_value = stats.ttest_ind(before, after)
print(f"\\nt-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.6f}")

if p_value < 0.05:
    print("Result: The difference IS statistically significant.")
    print("Handwashing made a measurable difference!")
else:
    print("Result: Cannot rule out chance. More data needed.")


# --------------------------------------------------
#  TODO 4: Calculate a 95% confidence interval for the difference
# --------------------------------------------------
# diff = before.mean() - after.mean()
# se   = stats.sem(before - after)   ← standard error of the mean
# ci   = stats.t.interval(0.95, df=len(before)-1, loc=diff, scale=se)
# print(f"95% CI for difference: {ci}")
"""

files["day 80/house price prediction.py"] = """\
# ============================================================
#  DAY 80: Capstone: Machine Learning
#  PROJECT: Predict House Prices (Multivariable Regression)
# ============================================================
#
#  SKILLS TODAY:
#    - Multivariable regression: multiple input features
#    - Feature engineering: log transform skewed data
#    - Train/test split: from sklearn.model_selection import train_test_split
#    - Evaluating model: RMSE, R²
#    - Underfitting vs overfitting
#    - Data cleaning: handle NaN, outliers
#    - pd.get_dummies() → encode categorical variables
#
#  pip install scikit-learn pandas numpy matplotlib seaborn
#
# ============================================================

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Synthetic house price dataset
n = 200
df = pd.DataFrame({
    "Size_sqft":  np.random.randint(500, 4000, n),
    "Bedrooms":   np.random.randint(1, 6, n),
    "Bathrooms":  np.random.randint(1, 4, n),
    "Age_years":  np.random.randint(0, 80, n),
    "Garage":     np.random.choice([0, 1], n),
    "Neighbourhood": np.random.choice(["Downtown", "Suburbs", "Rural"], n),
})
df["Price"] = (
    200 * df["Size_sqft"]
    + 15000 * df["Bedrooms"]
    + 10000 * df["Bathrooms"]
    - 500 * df["Age_years"]
    + 20000 * df["Garage"]
    + np.random.normal(0, 20000, n)
)


# --------------------------------------------------
#  TODO 1: Explore the data
# --------------------------------------------------
print(df.describe())
# Plot correlation heatmap
# sns.heatmap(df.corr(numeric_only=True), annot=True)


# --------------------------------------------------
#  TODO 2: Feature engineering
# --------------------------------------------------
# One-hot encode the Neighbourhood column
df = pd.get_dummies(df, columns=["Neighbourhood"], drop_first=True)

# Log transform Price to reduce skew
df["Log_Price"] = np.log(df["Price"])


# --------------------------------------------------
#  TODO 3: Train/test split
# --------------------------------------------------
features = ["Size_sqft", "Bedrooms", "Bathrooms", "Age_years", "Garage",
            "Neighbourhood_Suburbs", "Neighbourhood_Rural"]
X = df[features]
y = df["Log_Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# --------------------------------------------------
#  TODO 4: Train model and evaluate
# --------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

train_r2 = model.score(X_train, y_train)
test_r2  = model.score(X_test, y_test)
print(f"Train R²: {train_r2:.3f}")
print(f"Test R²:  {test_r2:.3f}")

# RMSE (in original price space → exponentiate predictions back)
y_pred    = model.predict(X_test)
y_pred_price = np.exp(y_pred)
y_test_price = np.exp(y_test)
rmse = np.sqrt(mean_squared_error(y_test_price, y_pred_price))
print(f"RMSE: ${rmse:,.0f}")


# --------------------------------------------------
#  TODO 5: Predict a specific house
# --------------------------------------------------
# new_house = pd.DataFrame([{
#     "Size_sqft": 1500, "Bedrooms": 3, "Bathrooms": 2,
#     "Age_years": 10, "Garage": 1,
#     "Neighbourhood_Suburbs": 1, "Neighbourhood_Rural": 0
# }])
# log_pred = model.predict(new_house)[0]
# price = np.exp(log_pred)
# print(f"Predicted price: ${price:,.0f}")

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Try Random Forest instead of Linear Regression:
#     from sklearn.ensemble import RandomForestRegressor
#  2. Use cross-validation: from sklearn.model_selection import cross_val_score
#  3. Download the Ames Housing dataset from Kaggle for 80 real features
# ============================================================
"""

for filepath, content in files.items():
    full_path = os.path.join(base, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Created: {filepath}")

print("Done: Days 59-80 written.")
