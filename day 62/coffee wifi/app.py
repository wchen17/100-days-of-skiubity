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
