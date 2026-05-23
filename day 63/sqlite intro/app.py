# ============================================================
#  DAY 63 — SQLite & SQLAlchemy
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
