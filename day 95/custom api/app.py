# ============================================================
#  DAY 95: Portfolio Project
#  PROJECT: Custom REST API: Random Quote / Joke / Fact Service
# ============================================================
#
#  SKILLS USED: Flask, SQLAlchemy, REST, authentication, rate limiting
#
#  ENDPOINTS:
#    GET  /api/random          → random item
#    GET  /api/all             → all items
#    GET  /api/search?q=...    → filter by keyword
#    POST /api/add             → add new item (API key required)
#    DELETE /api/delete/<id>   → delete (admin key required)
#
# ============================================================

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quotes.db"
db = SQLAlchemy(app)

API_KEY       = os.getenv("API_KEY", "user-key-123")
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY", "admin-key-secret")


class Quote(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    text   = db.Column(db.Text,        nullable=False)
    author = db.Column(db.String(100), nullable=False)
    tags   = db.Column(db.String(200))  # comma-separated

    def to_dict(self):
        return {"id": self.id, "text": self.text, "author": self.author, "tags": self.tags}

with app.app_context():
    db.create_all()
    # Seed with some quotes if empty
    if not db.session.execute(db.select(Quote)).scalars().first():
        seeds = [
            Quote(text="The only way to do great work is to love what you do.", author="Steve Jobs", tags="motivation,work"),
            Quote(text="Code is like humor. When you have to explain it, it's bad.", author="Cory House", tags="programming"),
            Quote(text="Programs must be written for people to read.", author="Harold Abelson", tags="programming"),
        ]
        db.session.add_all(seeds)
        db.session.commit()


@app.route("/api/random")
def get_random():
    all_quotes = db.session.execute(db.select(Quote)).scalars().all()
    if not all_quotes:
        return jsonify(error="No quotes available"), 404
    return jsonify(quote=random.choice(all_quotes).to_dict())


@app.route("/api/all")
def get_all():
    quotes = db.session.execute(db.select(Quote)).scalars().all()
    return jsonify(quotes=[q.to_dict() for q in quotes])


@app.route("/api/search")
def search():
    keyword = request.args.get("q", "").lower()
    all_q   = db.session.execute(db.select(Quote)).scalars().all()
    results = [q for q in all_q if keyword in q.text.lower() or keyword in (q.tags or "").lower()]
    if results:
        return jsonify(quotes=[q.to_dict() for q in results])
    return jsonify(error="No quotes matched."), 404


@app.route("/api/add", methods=["POST"])
def add_quote():
    api_key = request.args.get("api-key")
    if api_key != API_KEY:
        return jsonify(error="Unauthorized."), 403
    data = request.get_json()
    if not data or not data.get("text") or not data.get("author"):
        return jsonify(error="text and author are required."), 400
    new_quote = Quote(text=data["text"], author=data["author"], tags=data.get("tags", ""))
    db.session.add(new_quote)
    db.session.commit()
    return jsonify(success="Quote added!", quote=new_quote.to_dict()), 201


@app.route("/api/delete/<int:quote_id>", methods=["DELETE"])
def delete_quote(quote_id):
    api_key = request.args.get("api-key")
    if api_key != ADMIN_API_KEY:
        return jsonify(error="Admin key required."), 403
    quote = db.get_or_404(Quote, quote_id)
    db.session.delete(quote)
    db.session.commit()
    return jsonify(success="Quote deleted.")


if __name__ == "__main__":
    app.run(debug=True)
