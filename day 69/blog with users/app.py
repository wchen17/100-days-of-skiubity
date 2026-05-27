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
