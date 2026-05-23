# ============================================================
#  DAY 33 — APIs: Endpoints, Parameters, HTTP Codes
#  PROJECT: ISS Overhead Notifier
# ============================================================
#
#  SKILLS TODAY:
#    - import requests              → make HTTP requests
#    - requests.get(url)            → GET request
#    - response.status_code         → HTTP status (200 = OK)
#    - response.json()              → parse JSON response
#    - API parameters: requests.get(url, params={...})
#    - Chaining: response.json()["key"]["nested_key"]
#    - raise_for_status()           → auto-raise on 4xx/5xx
#
#  APIS USED (free, no key required):
#    ISS position: http://api.open-notify.org/iss-now.json
#    Sunrise/Sunset: https://api.sunrise-sunset.org/json
#
#  pip install requests
#
# ============================================================

import requests
import smtplib
import datetime
import time

MY_EMAIL    = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"
MY_LAT  = 51.507351   # TODO: change to your latitude
MY_LONG = -0.127758   # TODO: change to your longitude (London by default)


# --------------------------------------------------
#  TODO 1: is_iss_overhead() → bool
# --------------------------------------------------
# GET http://api.open-notify.org/iss-now.json
# Parse: response.json()["iss_position"]["latitude"] and ["longitude"]
# Return True if ISS is within ±5 degrees of MY_LAT and MY_LONG

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat  = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    # TODO: return True if ISS within ±5 of your position
    pass


# --------------------------------------------------
#  TODO 2: is_night() → bool
# --------------------------------------------------
# GET https://api.sunrise-sunset.org/json
# params: lat=MY_LAT, lng=MY_LONG, formatted=0
# Parse sunrise and sunset as datetime.datetime.fromisoformat()
# Return True if current hour is before sunrise or after sunset

def is_night():
    params = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()

    # TODO: parse sunrise and sunset, compare with datetime.datetime.now().hour
    pass


# --------------------------------------------------
#  TODO 3: Main loop — check every 60 seconds
# --------------------------------------------------
# If is_iss_overhead() AND is_night():
#   Send email: "Look Up! ISS is above you!"
# Loop with time.sleep(60)

while True:
    if is_iss_overhead() and is_night():
        print("ISS is overhead and it's dark — sending email!")
        # TODO: send email with smtplib (same as Day 32)
    else:
        print("ISS not visible right now.")
    time.sleep(60)

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Also show how many astronauts are on the ISS right now
#     → GET http://api.open-notify.org/astros.json
#  2. Send a push notification via Pushover or Ntfy instead of email
#  3. Plot the ISS path on a map using folium
# ============================================================
