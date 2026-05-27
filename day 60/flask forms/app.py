# ============================================================
#  DAY 60: POST Requests & HTML Forms in Flask
#  PROJECT: Contact form that sends an email
# ============================================================
#
#  SKILLS TODAY:
#    - <form method="POST" action="/path">
#    - from flask import request
#    - request.method == "POST"
#    - request.form["field_name"]      → get form data
#    - redirect(url_for("function"))   → redirect after POST
#    - flash(message) / get_flashed_messages()  → one-time messages
#    - The POST-Redirect-GET pattern (prevents double submit on refresh)
#
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os

app = Flask(__name__)
app.secret_key = "your-secret-key-here"   # required for flash messages

MY_EMAIL    = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name    = request.form["name"]
        email   = request.form["email"]
        phone   = request.form["phone"]
        message = request.form["message"]

        print(f"New contact from {name} ({email}): {message}")

        # --------------------------------------------------
        #  TODO: Send email with the contact form data
        # --------------------------------------------------
        # with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        #     smtp.starttls()
        #     smtp.login(MY_EMAIL, MY_PASSWORD)
        #     smtp.sendmail(MY_EMAIL, MY_EMAIL,
        #         f"Subject: New Contact\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")

        # POST-Redirect-GET: redirect back to avoid double-submit
        return redirect(url_for("home"))

    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
