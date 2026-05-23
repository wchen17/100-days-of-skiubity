# ============================================================
#  DAY 36 — Stock API + News API
#  PROJECT: Stock Trading News Alert Bot
# ============================================================
#
#  SKILLS TODAY:
#    - Alpha Vantage API   → stock price data
#    - NewsAPI             → fetch relevant news articles
#    - Comparing yesterday vs day-before-yesterday close price
#    - Percentage change calculation
#    - Sending formatted SMS with Twilio
#
#  APIs:
#    Alpha Vantage: https://www.alphavantage.co (free key)
#    NewsAPI:       https://newsapi.org (free key)
#
# ============================================================

import requests
import os

STOCK      = "TSLA"
COMPANY    = "Tesla Inc"

AV_KEY     = os.getenv("ALPHA_VANTAGE_KEY", "demo")
NEWS_KEY   = os.getenv("NEWS_API_KEY", "demo")


# --------------------------------------------------
#  TODO 1: Get yesterday's and day-before's closing prices
# --------------------------------------------------
# GET https://www.alphavantage.co/query
# params: function="TIME_SERIES_DAILY", symbol=STOCK, apikey=AV_KEY
# response.json()["Time Series (Daily)"] → dict of date strings → OHLCV
# Sort by date descending, take [0] and [1]

av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol":   STOCK,
    "apikey":   AV_KEY,
}
# response = requests.get("https://www.alphavantage.co/query", params=av_params)
# data = response.json()["Time Series (Daily)"]
# date_list = [key for key in data.keys()]
# yesterday_data = data[date_list[0]]
# day_before_data = data[date_list[1]]

yesterday_close  = 300.0   # TODO: parse from API
day_before_close = 280.0   # TODO: parse from API

# --------------------------------------------------
#  TODO 2: Calculate percent change
# --------------------------------------------------
# diff = yesterday_close - day_before_close
# pct  = abs(diff / day_before_close * 100)
# up_down = "🔺" if diff > 0 else "🔻"

diff    = yesterday_close - day_before_close
pct     = abs(diff / day_before_close * 100)
up_down = "🔺" if diff > 0 else "🔻"

print(f"{STOCK}: {up_down} {pct:.2f}%")


# --------------------------------------------------
#  TODO 3: If change > 5%, fetch top 3 news articles
# --------------------------------------------------
# GET https://newsapi.org/v2/everything
# params: qInTitle=COMPANY, apiKey=NEWS_KEY
# Take first 3 articles from response.json()["articles"]
# Format each as: "Headline: ...
Brief: ..."

if pct > 5:
    news_params = {"qInTitle": COMPANY, "apiKey": NEWS_KEY}
    # response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    # articles = response.json()["articles"][:3]
    # for article in articles:
    #     print(f"Headline: {article['title']}
Brief: {article['description']}
")
    #   # TODO: send each as an SMS with Twilio
    print(f"Big move! Would send news alerts for {COMPANY}")

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Monitor multiple stocks simultaneously
#  2. Store the last price in a file so you compare across runs
#  3. Build a web dashboard with Flask to show live alerts
# ============================================================
