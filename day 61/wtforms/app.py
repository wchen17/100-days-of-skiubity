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
