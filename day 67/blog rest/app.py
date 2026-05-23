# ============================================================
#  DAY 67 — Blog Capstone Part 3: RESTful Routing
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
