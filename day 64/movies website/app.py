# ============================================================
#  DAY 64 — SQLAlchemy + TMDB API
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
