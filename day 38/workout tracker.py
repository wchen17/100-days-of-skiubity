# ============================================================
#  DAY 38: Google Sheets Integration
#  PROJECT: Workout Tracker (NLP → Google Sheets)
# ============================================================
#
#  SKILLS TODAY:
#    - Nutritionix API  → parse natural language exercise descriptions
#    - Sheety API       → write to a Google Sheet via REST
#    - HTTP Basic Auth  → requests.post(..., auth=(user, pass))
#    - datetime         → timestamp each workout entry
#
#  SETUP:
#    1. Sign up at nutritionix.com (free) → get App ID + API key
#    2. Sign up at sheety.co → connect a Google Sheet, enable POST
#    3. Your sheet columns: Date, Time, Exercise, Duration, Calories
#
# ============================================================

import requests
from datetime import datetime
import os

NUTRITIONIX_APP_ID  = os.getenv("NUTRITIONIX_APP_ID", "demo")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY", "demo")
SHEETY_ENDPOINT     = os.getenv("SHEETY_ENDPOINT", "https://example.com/workouts")
SHEETY_USERNAME     = os.getenv("SHEETY_USERNAME", "demo")
SHEETY_PASSWORD     = os.getenv("SHEETY_PASSWORD", "demo")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# --------------------------------------------------
#  TODO 1: Ask user what exercise they did and call Nutritionix
# --------------------------------------------------
# POST https://trackapi.nutritionix.com/v2/natural/exercise
# headers: x-app-id, x-app-key, Content-Type: application/json
# body: {"query": user_input, "gender": "male", "weight_kg": 75, ...}
# Response: list of exercises with "name", "duration_min", "nf_calories"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id":  NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}
body = {"query": exercise_text}

# response = requests.post(exercise_endpoint, json=body, headers=headers)
# exercises = response.json()["exercises"]

# Demo placeholder:
exercises = [{"name": "running", "duration_min": 30, "nf_calories": 300}]


# --------------------------------------------------
#  TODO 2: Log each exercise to Google Sheets via Sheety
# --------------------------------------------------
# For each exercise in exercises:
#   POST to SHEETY_ENDPOINT
#   auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
#   body JSON (match your sheet column names):
#     {"workout": {
#         "date": today.strftime("%d/%m/%Y"),
#         "time": now.strftime("%X"),
#         "exercise": exercise["name"].title(),
#         "duration": exercise["duration_min"],
#         "calories": exercise["nf_calories"]
#     }}

today = datetime.now()

for exercise in exercises:
    sheet_row = {
        "workout": {
            "date":     today.strftime("%d/%m/%Y"),
            "time":     today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # response = requests.post(SHEETY_ENDPOINT, json=sheet_row, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
    # print(response.text)
    print(f"Would log: {sheet_row}")
