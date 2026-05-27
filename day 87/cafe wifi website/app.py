# ============================================================
#  DAY 87: Portfolio Project
#  PROJECT: Café & Wifi Website (full stack)
# ============================================================
#
#  SKILLS USED: Flask, SQLAlchemy, Bootstrap, REST API, WTForms
#
#  REQUIREMENTS:
#    - Public site: browse cafes with wifi/power ratings
#    - API: GET /api/cafes, POST /api/cafe, DELETE /api/cafe/<id>
#    - Add café form (login required)
#    - Search by location
#    - Filter by wifi/power/sockets
#    - Deploy to Render
#
# ============================================================

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "secret")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(app)

API_KEY = os.getenv("API_KEY", "TopSecretAPIKey")


class Cafe(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(250), unique=True, nullable=False)
    map_url      = db.Column(db.String(500), nullable=False)
    img_url      = db.Column(db.String(500), nullable=False)
    location     = db.Column(db.String(250), nullable=False)
    seats        = db.Column(db.String(250))
    has_toilet   = db.Column(db.Boolean)
    has_wifi     = db.Column(db.Boolean)
    has_sockets  = db.Column(db.Boolean)
    can_take_calls = db.Column(db.Boolean)
    coffee_price = db.Column(db.String(250))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

with app.app_context():
    db.create_all()


# --------------------------------------------------
#  Web Routes
# --------------------------------------------------
@app.route("/")
def home():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return render_template("index.html", cafes=cafes)

@app.route("/cafe/<int:cafe_id>")
def cafe_detail(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    return render_template("cafe.html", cafe=cafe)

# TODO: /add route with WTForms (login required)
# TODO: /search?q=London route


# --------------------------------------------------
#  REST API Routes
# --------------------------------------------------
@app.route("/api/cafes")
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[c.to_dict() for c in cafes])

@app.route("/api/cafe", methods=["POST"])
def add_cafe():
    # TODO: validate API key in headers or params, then add cafe
    pass

@app.route("/api/cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != API_KEY:
        return jsonify(error="Not authorised."), 403
    cafe = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(success="Cafe deleted."), 200


if __name__ == "__main__":
    app.run(debug=True)
