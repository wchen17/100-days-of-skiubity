# ============================================================
#  DAY 66 — Building a REST API with Flask
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
