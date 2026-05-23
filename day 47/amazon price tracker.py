# ============================================================
#  DAY 47 — Web Scraping Project
#  PROJECT: Amazon Price Tracker (email alert when price drops)
# ============================================================
#
#  SKILLS TODAY:
#    - BeautifulSoup with custom headers (spoof a browser)
#    - Extracting prices (remove currency symbols, convert to float)
#    - Comparing against a target price
#    - Sending email with smtplib when price is below target
#    - Scheduling to run daily
#
# ============================================================

import requests
from bs4 import BeautifulSoup
import smtplib
import os

# TODO: replace with any Amazon product URL you want to track
URL = "https://www.amazon.com/dp/B08N5WRWNW"
BUY_PRICE = 100.00

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# --------------------------------------------------
#  TODO 1: Scrape the product price
# --------------------------------------------------
# Inspect the Amazon page → find the price element (it changes over time)
# Common selectors: span.a-price-whole, span#priceblock_ourprice
# Clean the price: remove "$", ",", strip whitespace → float

response = requests.get(URL, headers=headers)
soup     = BeautifulSoup(response.text, "html.parser")

# price_tag = soup.find("span", class_="a-price-whole")
# price     = float(price_tag.get_text().strip().replace(",", "").replace("$", ""))
price    = 90.00     # placeholder
title    = "Sample Product"   # TODO: also scrape the product title

print(f"{title}: ${price}")


# --------------------------------------------------
#  TODO 2: Compare to target and send email if cheap enough
# --------------------------------------------------
if price < BUY_PRICE:
    MY_EMAIL    = os.getenv("MY_EMAIL")
    MY_PASSWORD = os.getenv("MY_PASSWORD")

    message = (
        f"Subject:Amazon Price Alert!\n\n"
        f"{title} is now ${price}\n"
        f"Link: {URL}"
    )

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        # connection.login(MY_EMAIL, MY_PASSWORD)
        # connection.sendmail(MY_EMAIL, MY_EMAIL, message)
        print("Would send email:", message)
else:
    print(f"Price ${price} is still above target ${BUY_PRICE}")

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Track multiple products by storing URLs + target prices in a CSV
#  2. Log price history to a JSON file and plot with matplotlib
#  3. Build a Flask web form where you paste the URL + set target price
# ============================================================
