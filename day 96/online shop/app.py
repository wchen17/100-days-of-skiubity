# ============================================================
#  DAY 96 — Portfolio Project
#  PROJECT: Simple Online Shop with Stripe Payments
# ============================================================
#
#  SKILLS USED: Flask, SQLAlchemy, Stripe API, Bootstrap, sessions
#
#  REQUIREMENTS:
#    - Product listing page
#    - Product detail page
#    - Add to cart (session-based)
#    - Checkout with Stripe (test mode)
#    - Order confirmation page
#
#  pip install flask flask-sqlalchemy stripe python-dotenv
#  Get Stripe test keys at dashboard.stripe.com
#
# ============================================================

from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import stripe
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
db  = SQLAlchemy(app)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_...")
STRIPE_PUB_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY", "pk_test_...")


class Product(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price_cents = db.Column(db.Integer, nullable=False)  # price in cents
    image_url   = db.Column(db.String(300))
    stock       = db.Column(db.Integer, default=100)

    @property
    def price_display(self):
        return f"${self.price_cents / 100:.2f}"

with app.app_context():
    db.create_all()
    if not db.session.execute(db.select(Product)).scalars().first():
        db.session.add_all([
            Product(name="Python Book",   description="Learn Python fast",    price_cents=2999, stock=50),
            Product(name="Coding Course", description="100 Days of Code",     price_cents=1999, stock=999),
            Product(name="Dev Stickers",  description="Laptop sticker pack",  price_cents=499,  stock=200),
        ])
        db.session.commit()


@app.route("/")
def shop():
    products = db.session.execute(db.select(Product)).scalars().all()
    cart_count = sum(session.get("cart", {}).values())
    return render_template("shop.html", products=products, cart_count=cart_count)


@app.route("/cart")
def cart():
    cart      = session.get("cart", {})
    products  = []
    total     = 0
    for product_id, qty in cart.items():
        product = db.get_or_404(Product, int(product_id))
        subtotal = product.price_cents * qty
        total   += subtotal
        products.append({"product": product, "qty": qty, "subtotal": subtotal})
    return render_template("cart.html", items=products, total=total, stripe_pub_key=STRIPE_PUB_KEY)


# --------------------------------------------------
#  TODO 1: /add-to-cart/<product_id>
# --------------------------------------------------
@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session["cart"] = cart
    return redirect(url_for("shop"))


# --------------------------------------------------
#  TODO 2: /checkout — create a Stripe payment intent
# --------------------------------------------------
@app.route("/checkout", methods=["POST"])
def checkout():
    cart  = session.get("cart", {})
    total = sum(
        db.get_or_404(Product, int(pid)).price_cents * qty
        for pid, qty in cart.items()
    )
    # intent = stripe.PaymentIntent.create(amount=total, currency="usd")
    # return jsonify(client_secret=intent.client_secret)
    return jsonify(client_secret="test_secret_for_now")


@app.route("/success")
def success():
    session.pop("cart", None)
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
