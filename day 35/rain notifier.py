# ============================================================
#  DAY 35: API Authentication & Environment Variables
#  PROJECT: Rain Notifier (SMS alert for rain today)
# ============================================================
#
#  SKILLS TODAY:
#    - API keys / authentication
#    - Environment variables:
#        import os; os.environ.get("KEY_NAME")
#        or python-dotenv: load_dotenv() then os.getenv()
#    - Twilio SMS API (free trial)
#    - OpenWeatherMap API (free tier)
#    - List comprehension on API results
#    - Weather condition IDs < 700 = rain/snow/storms
#
#  SETUP:
#    pip install twilio python-dotenv requests
#    Create a .env file:
#        OWM_API_KEY=your_key
#        TWILIO_SID=your_sid
#        TWILIO_AUTH=your_auth_token
#        TWILIO_FROM=+1...
#        MY_PHONE=+1...
#
# ============================================================

import requests
import os
from dotenv import load_dotenv

load_dotenv()

OWM_API_KEY = os.getenv("OWM_API_KEY", "demo_key")
MY_LAT  = 51.507351
MY_LONG = -0.127758

# --------------------------------------------------
#  TODO 1: Fetch hourly weather forecast
# --------------------------------------------------
# GET https://api.openweathermap.org/data/2.5/forecast
# params: lat, lon, appid, cnt=4 (next 4 x 3-hour slots = 12 hours)
# Inspect response.json() to find the list of forecasts
# Each entry has "weather"[0]["id"]: condition code

params = {
    "lat":   MY_LAT,
    "lon":   MY_LONG,
    "appid": OWM_API_KEY,
    "cnt":   4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)

if response.status_code == 200:
    weather_data = response.json()
    # --------------------------------------------------
    #  TODO 2: Check if it will rain in the next 12 hours
    # --------------------------------------------------
    # Extract condition IDs: [slot["weather"][0]["id"] for slot in weather_data["list"]]
    # Rain/snow/storm = condition ID < 700
    # will_rain = any(id < 700 for id in condition_ids)

    condition_ids = []   # TODO: list comprehension
    will_rain = False    # TODO: any(id < 700 for id in condition_ids)

    if will_rain:
        print("Bring an umbrella! It's going to rain.")
        # --------------------------------------------------
        #  TODO 3: Send SMS via Twilio
        # --------------------------------------------------
        # from twilio.rest import Client
        # client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))
        # message = client.messages.create(
        #     body="It's going to rain today. Remember to bring an umbrella!",
        #     from_=os.getenv("TWILIO_FROM"),
        #     to=os.getenv("MY_PHONE")
        # )
        # print(message.status)
    else:
        print("No rain expected. Enjoy the day!")
else:
    print(f"API error: {response.status_code}")

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add snow and storm alerts with different messages
#  2. Schedule this to run every morning at 7am (cron / Task Scheduler)
#  3. Send via email instead of SMS so no Twilio account needed
# ============================================================
