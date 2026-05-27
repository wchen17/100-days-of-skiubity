import os
base = "/home/user/100-days-of-skiubity"
files = {}

files["day 32/birthday wisher.py"] = """\
# ============================================================
#  DAY 32: Email Automation & datetime
#  PROJECT: Automated Birthday Wisher
# ============================================================
#
#  SKILLS TODAY:
#    - import smtplib                    → send emails
#    - smtp.sendmail(from, to, msg)
#    - from datetime import datetime
#    - datetime.now().month / .day
#    - Reading CSV with pandas
#    - random.choice() for varied messages
#
#  SETUP:
#    Gmail: enable "App Passwords" (2FA required)
#    Create a file "birthdays.csv" with columns: name,email,year,month,day
#    Create a folder "letter_templates/" with files letter_1.txt, letter_2.txt
#    Each letter has a [NAME] placeholder
#
# ============================================================

import smtplib
import datetime
import pandas
import random

MY_EMAIL    = "your_email@gmail.com"   # TODO: replace
MY_PASSWORD = "your_app_password"      # TODO: replace: use env var in real use

# Sample birthday data (replace with real CSV file)
import io
sample_csv = "name,email,year,month,day\\nAlice,alice@example.com,1990,5,23\\nBob,bob@example.com,1985,5,23"
with open("birthdays.csv", "w") as f:
    f.write(sample_csv)

# Sample letter templates
import os
os.makedirs("letter_templates", exist_ok=True)
with open("letter_templates/letter_1.txt", "w") as f:
    f.write("Dear [NAME],\\n\\nWishing you a wonderful birthday! Hope your day is amazing.\\n\\nCheers!")
with open("letter_templates/letter_2.txt", "w") as f:
    f.write("Happy Birthday [NAME]!\\n\\nMay this year bring you joy and success.\\n\\nBest wishes!")


# --------------------------------------------------
#  TODO 1: Get today's month and day
# --------------------------------------------------
# today = datetime.datetime.now()
# today_tuple = (today.month, today.day)

today = datetime.datetime.now()
today_tuple = (today.month, today.day)


# --------------------------------------------------
#  TODO 2: Load birthday data and check for matches
# --------------------------------------------------
# Read birthdays.csv into a DataFrame
# Build a dict keyed by (month, day): { (5, 23): row, ... }
# Check if today_tuple is in the dict

df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for _, row in df.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # --------------------------------------------------
    #  TODO 3: Pick a random letter template and personalise it
    # --------------------------------------------------
    # Use random.randint(1, 3) to pick a letter file (assuming 1-3)
    # Read the file, replace [NAME] with birthday_person.name
    # Store as contents

    letter_num = random.randint(1, 2)
    with open(f"letter_templates/letter_{letter_num}.txt") as f:
        contents = f.read()
    contents = contents.replace("[NAME]", birthday_person.name)

    # --------------------------------------------------
    #  TODO 4: Send the email with smtplib
    # --------------------------------------------------
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #   connection.starttls()                            → encrypt
    #   connection.login(MY_EMAIL, MY_PASSWORD)
    #   connection.sendmail(
    #       from_addr=MY_EMAIL,
    #       to_addrs=birthday_person.email,
    #       msg=f"Subject:Happy Birthday!\\n\\n{contents}"
    #   )
    # print(f"Email sent to {birthday_person.name}")

    print(f"Would send to {birthday_person.name}:")
    print(contents)
    # Uncomment the smtplib block above once you have real credentials

else:
    print("No birthdays today!")

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Schedule this script to run daily using cron (Linux/Mac) or
#     Task Scheduler (Windows)
#  2. Send to multiple people if several birthdays share a date
#  3. Add a WhatsApp message via Twilio as well
# ============================================================
"""

files["day 33/iss notifier.py"] = """\
# ============================================================
#  DAY 33: APIs: Endpoints, Parameters, HTTP Codes
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
#  TODO 3: Main loop: check every 60 seconds
# --------------------------------------------------
# If is_iss_overhead() AND is_night():
#   Send email: "Look Up! ISS is above you!"
# Loop with time.sleep(60)

while True:
    if is_iss_overhead() and is_night():
        print("ISS is overhead and it's dark: sending email!")
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
"""

files["day 34/gui quiz app.py"] = """\
# ============================================================
#  DAY 34: API Practice + GUI
#  PROJECT: Trivia Quiz App (Open Trivia DB + Tkinter)
# ============================================================
#
#  SKILLS TODAY:
#    - Fetching data from a real API (no key needed)
#    - Passing API parameters: amount, type, category
#    - Combining OOP (QuizBrain from Day 17) with a GUI
#    - html.unescape()   → fix HTML entities in API responses (&amp; → &)
#    - Updating Tkinter widgets with .config()
#
#  API: https://opentdb.com/api.php?amount=10&type=boolean
#
# ============================================================

import requests
import html
import tkinter as tk

THEME_COLOR = "#375362"


# --------------------------------------------------
#  TODO 1: Fetch questions from the API
# --------------------------------------------------
# GET https://opentdb.com/api.php with params:
#   amount=10, type="boolean" (True/False questions)
# Parse response.json()["results"]
# Each result has: "question", "correct_answer", "category", "difficulty"

def fetch_questions():
    params = {"amount": 10, "type": "boolean"}
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    return response.json()["results"]


question_data = fetch_questions()


# --------------------------------------------------
#  TODO 2: Question and QuizBrain classes
# --------------------------------------------------
# Reuse / adapt from Day 17
# Question(text, answer)  → just stores text and answer
# QuizBrain(question_list):
#   still_has_questions() → bool
#   next_question()       → updates the GUI (call from QuizInterface)
#   check_answer(answer)  → returns True/False, updates score

class Question:
    def __init__(self, q_text, q_answer):
        self.text   = q_text
        self.answer = q_answer


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score           = 0
        self.question_list   = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number  += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct = self.current_question.answer
        if user_answer.lower() == correct.lower():
            self.score += 1
            return True
        return False


question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]
quiz = QuizBrain(question_bank)


# --------------------------------------------------
#  TODO 3: QuizInterface class (Tkinter UI)
# --------------------------------------------------
# __init__(quiz_brain):
#   self.quiz = quiz_brain
#   Build the window: dark background, score label, question canvas,
#   True button (green), False button (red)
#   Call get_next_question()
#
# get_next_question():
#   If quiz.still_has_questions():
#     Update canvas text with quiz.next_question()
#   Else:
#     Show "You've reached the end! Score: X/10"
#
# true_pressed() / false_pressed():
#   Check the answer, flash the canvas green (correct) or red (wrong)
#   Use window.after(1000, get_next_question) to pause before moving on
#
# give_feedback(is_right):
#   canvas.config(bg="green") if right, else red
#   window.after(1000, ...) to reset to white and load next question

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Question", font=("Arial", 20, "italic"),
            fill=THEME_COLOR, width=280, anchor="center"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button  = tk.Button(text="True",  bg="green", fg="white", command=self.true_pressed)
        false_button = tk.Button(text="False", bg="red",   fg="white", command=self.false_pressed)
        true_button.grid(row=2, column=0)
        false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've finished!\\nScore: {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        color = "green" if is_right else "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)


quiz_ui = QuizInterface(quiz)
"""

files["day 35/rain notifier.py"] = """\
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
"""

files["day 36/stock alert.py"] = """\
# ============================================================
#  DAY 36: Stock API + News API
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
# Format each as: "Headline: ...\nBrief: ..."

if pct > 5:
    news_params = {"qInTitle": COMPANY, "apiKey": NEWS_KEY}
    # response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    # articles = response.json()["articles"][:3]
    # for article in articles:
    #     print(f"Headline: {article['title']}\nBrief: {article['description']}\n")
    #   # TODO: send each as an SMS with Twilio
    print(f"Big move! Would send news alerts for {COMPANY}")

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Monitor multiple stocks simultaneously
#  2. Store the last price in a file so you compare across runs
#  3. Build a web dashboard with Flask to show live alerts
# ============================================================
"""

files["day 37/habit tracker.py"] = """\
# ============================================================
#  DAY 37: API POST Requests & Pixela
#  PROJECT: Habit Tracker (Graph your daily coding/exercise)
# ============================================================
#
#  SKILLS TODAY:
#    - HTTP POST requests: requests.post(url, json={...})
#    - HTTP PUT / DELETE requests
#    - Custom request headers: {"X-USER-TOKEN": token}
#    - Pixela API (free): graph your habits at pixe.la
#    - datetime.date.today().strftime("%Y%m%d")
#
#  SETUP (run once):
#    1. Create Pixela account (run TODO 1 once)
#    2. Create a graph (run TODO 2 once)
#    3. Post/update pixels daily (TODO 3/4)
#
# ============================================================

import requests
from datetime import datetime

USERNAME  = "your_username"    # TODO: pick a unique Pixela username
TOKEN     = "your_token"       # TODO: any string, acts as your password
GRAPH_ID  = "coding-graph"

pixela_endpoint = "https://pixe.la/v1/users"
headers = {"X-USER-TOKEN": TOKEN}


# --------------------------------------------------
#  TODO 1: Create Pixela account (run ONCE, then comment out)
# --------------------------------------------------
# POST https://pixe.la/v1/users
# body JSON: {"token": TOKEN, "username": USERNAME,
#             "agreeTermsOfService": "yes", "notMinor": "yes"}

user_params = {
    "token":                TOKEN,
    "username":             USERNAME,
    "agreeTermsOfService":  "yes",
    "notMinor":             "yes",
}
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)


# --------------------------------------------------
#  TODO 2: Create a graph (run ONCE, then comment out)
# --------------------------------------------------
# POST https://pixe.la/v1/users/{USERNAME}/graphs
# headers: X-USER-TOKEN
# body: {"id": GRAPH_ID, "name": "Coding Graph",
#        "unit": "hours", "type": "float", "color": "momiji"}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":    GRAPH_ID,
    "name":  "Coding Graph",
    "unit":  "hours",
    "type":  "float",
    "color": "momiji",
}
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# Your graph will be at: https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html


# --------------------------------------------------
#  TODO 3: Post today's pixel (run daily)
# --------------------------------------------------
# POST https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}
# body: {"date": "YYYYMMDD", "quantity": "hours coded today"}

today = datetime.now().strftime("%Y%m%d")
hours = input("How many hours did you code today? ")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {"date": today, "quantity": hours}
# response = requests.post(pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# --------------------------------------------------
#  TODO 4: Update a pixel (if you made a mistake)
# --------------------------------------------------
# PUT https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}
# body: {"quantity": "new_value"}

update_date = input("Which date to update? (YYYYMMDD): ")
new_hours   = input("Corrected hours: ")
update_endpoint = f"{pixel_endpoint}/{update_date}"
# response = requests.put(update_endpoint, json={"quantity": new_hours}, headers=headers)
# print(response.text)


# --------------------------------------------------
#  TODO 5: Delete a pixel
# --------------------------------------------------
# DELETE https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}
delete_date = input("Which date to delete? (YYYYMMDD): ")
delete_endpoint = f"{pixel_endpoint}/{delete_date}"
# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)
"""

files["day 38/workout tracker.py"] = """\
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
"""

files["day 39/flight deal finder.py"] = """\
# ============================================================
#  DAY 39-40: Capstone: Flight Deal Finder
#  PROJECT: Find cheap flights and notify by SMS/email
# ============================================================
#
#  SKILLS TODAY:
#    - Multi-file OOP project (FlightSearch, DataManager, NotificationManager)
#    - Kiwi Tequila API (free) → search flights
#    - Sheety → read/write destination data from Google Sheet
#    - Twilio / SMTP → send alerts
#    - IATA airport codes
#
#  FILES IN THIS PROJECT:
#    flight_search.py        → FlightSearch class (API calls)
#    data_manager.py         → DataManager class (Google Sheet CRUD)
#    notification_manager.py → NotificationManager (SMS/email)
#    flight_data.py          → FlightData dataclass
#    main.py                 → orchestrator (THIS FILE)
#
# ============================================================

# main.py

# from data_manager import DataManager
# from flight_search import FlightSearch
# from notification_manager import NotificationManager

# data_manager         = DataManager()
# sheet_data           = data_manager.get_destination_data()
# flight_search        = FlightSearch()
# notification_manager = NotificationManager()

# --------------------------------------------------
#  TODO 1: Ensure all destinations have IATA codes
# --------------------------------------------------
# Loop through sheet_data
# If a row is missing its iata_code:
#   Use FlightSearch to look up the IATA code for the city name
#   Update the Google Sheet row with data_manager.update_destination_codes()

# --------------------------------------------------
#  TODO 2: Search for cheap flights for each destination
# --------------------------------------------------
# For each destination in sheet_data:
#   Call flight_search.check_flights(origin_city_iata, destination_iata,
#                                    from_time=tomorrow, to_time=6_months_out)
#   If cheapest price < row["lowestPrice"]:
#     Send SMS/email with flight details

# --------------------------------------------------
#  SKELETON: FlightSearch class
# --------------------------------------------------
import requests
import os
from datetime import datetime, timedelta

TEQUILA_KEY      = os.getenv("TEQUILA_KEY", "demo")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
ORIGIN_CITY_IATA = "LON"

class FlightSearch:

    def get_destination_code(self, city_name):
        # GET {TEQUILA_ENDPOINT}/locations/query?term={city_name}&location_types=city
        # Return the first result's "code"
        headers = {"apikey": TEQUILA_KEY}
        # response = requests.get(...)
        pass

    def check_flights(self, origin_city_iata, destination_iata, from_time, to_time):
        # GET {TEQUILA_ENDPOINT}/v2/search
        # params: fly_from, fly_to, date_from, date_to, nights_in_dst_from=7,
        #         nights_in_dst_to=28, flight_type="round", one_for_city=1,
        #         curr="GBP", apikey=TEQUILA_KEY
        # Return a FlightData object with: price, origin, destination, dates
        pass

# --------------------------------------------------
#  SKELETON: DataManager class
# --------------------------------------------------
class DataManager:
    def get_destination_data(self):
        # GET from Sheety, return list of row dicts
        pass

    def update_destination_codes(self, data):
        # PUT each updated row back to Sheety
        pass

# --------------------------------------------------
#  SKELETON: NotificationManager class
# --------------------------------------------------
class NotificationManager:
    def send_sms(self, message):
        # Use Twilio (same as Day 35)
        pass

    def send_email(self, email_list, message):
        # Use smtplib (same as Day 32)
        pass

# ============================================================
#  STRETCH GOALS (Day 40)
# ============================================================
#  1. Store a list of user emails in the sheet
#     and email ALL of them when a deal is found
#  2. Add a web form (Flask, Day 54) for users to sign up
#     and add their email to the "users" sheet
#  3. Support direct flights only (add stopNumbers=0 param)
# ============================================================
"""

files["day 41/html intro.html"] = """\
<!-- ============================================================
     DAY 41: HTML Basics
     PROJECT: Build your first web page from scratch
     ============================================================

     SKILLS TODAY:
       <!DOCTYPE html>       → tell browser this is HTML5
       <html>                → root element
       <head>                → metadata (title, charset, links)
       <body>                → visible content
       Heading tags          → <h1> through <h6>
       Paragraph             → <p>
       Links                 → <a href="url">text</a>
       Images                → <img src="url" alt="description">
       Lists                 → <ul>, <ol>, <li>
       Bold / Italic         → <strong>, <em>
       Line break            → <br>
       Horizontal rule       → <hr>
       Comments              → <!-- like this - ->

     ============================================================ -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title>
</head>
<body>

    <!-- TODO 1: Add a main heading with your name -->
    <h1>Your Name Here</h1>

    <!-- TODO 2: Add a paragraph introducing yourself -->
    <p>Write a short bio here.</p>

    <!-- TODO 3: Add an image (use any URL or a local file) -->
    <!-- <img src="profile.jpg" alt="My photo" width="200"> -->

    <!-- TODO 4: Add an unordered list of your top 3 skills -->
    <h2>My Skills</h2>
    <ul>
        <li>Python</li>
        <!-- add more -->
    </ul>

    <!-- TODO 5: Add an ordered list of your goals for this 100 days -->
    <h2>My Goals</h2>
    <ol>
        <li>Learn Python basics</li>
        <!-- add more -->
    </ol>

    <!-- TODO 6: Add a link to your GitHub profile -->
    <p>Check out my work: <a href="https://github.com/wchen17" target="_blank">GitHub</a></p>

    <!-- STRETCH: Add a table showing your weekly coding schedule -->
    <!--
    <table border="1">
        <tr><th>Day</th><th>Topic</th><th>Hours</th></tr>
        <tr><td>Monday</td><td>Python</td><td>2</td></tr>
    </table>
    -->

</body>
</html>
"""

files["day 42/intermediate html.html"] = """\
<!-- ============================================================
     DAY 42: Intermediate HTML
     PROJECT: Personal Portfolio Page (HTML only)
     ============================================================

     SKILLS TODAY:
       <form>                → collect user input
       <input type="text/email/submit/checkbox/radio">
       <textarea>            → multi-line text input
       <select> / <option>   → dropdown
       <table>               → tabular data
       <div>                 → generic block container
       <span>                → generic inline container
       id="name"             → unique identifier
       class="name"          → reusable grouping (for CSS tomorrow)
       HTML entities         → &amp; &lt; &gt; &copy; &nbsp;

     ============================================================ -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Portfolio</title>
</head>
<body>

    <div id="header">
        <h1>My Developer Portfolio</h1>
        <p>100 Days of Code: Work in Progress</p>
    </div>

    <hr>

    <!-- TODO 1: Projects table -->
    <h2>Projects</h2>
    <table border="1" cellpadding="8">
        <thead>
            <tr>
                <th>Day</th>
                <th>Project</th>
                <th>Skills Used</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Name Generator</td>
                <td>print, input, strings</td>
            </tr>
            <!-- TODO: add rows for days 2, 3, and a few more -->
        </tbody>
    </table>

    <hr>

    <!-- TODO 2: Contact form -->
    <h2>Contact Me</h2>
    <form action="#" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" placeholder="Your name"><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" placeholder="your@email.com"><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" cols="40"></textarea><br><br>

        <!-- TODO: add a dropdown asking "How did you find me?" -->
        <!-- <select name="source"> <option>...</option> </select> -->

        <input type="submit" value="Send">
    </form>

</body>
</html>
"""

files["day 43/css intro/index.html"] = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Intro</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1 class="title">CSS Makes Things Pretty</h1>
    <p id="intro">This paragraph has an id selector applied.</p>
    <p class="highlight">This paragraph uses a class selector.</p>
    <div class="card">
        <h2>I am a card</h2>
        <p>Cards use borders, padding, and box-shadow.</p>
    </div>
    <button class="btn">Click Me</button>
</body>
</html>
"""

files["day 43/css intro/style.css"] = """\
/* ============================================================
   DAY 43: CSS Fundamentals
   PROJECT: Style the Day 42 portfolio page
   ============================================================

   SKILLS TODAY:
     Selectors:   element, .class, #id, *
     Properties:  color, background-color, font-size, font-family
                  margin, padding, border, border-radius
                  width, height, display
     Box model:   content → padding → border → margin
     Colours:     named, hex (#rrggbb), rgb(r,g,b)
     Inheritance  → children inherit font from parents
     Specificity  → id > class > element

   ============================================================ */

/* --- Reset (remove default browser spacing) --- */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    padding: 20px;
}

/* TODO 1: Style the h1.title */
.title {
    /* add: color, font-size, text-align, margin-bottom */
}

/* TODO 2: Style the #intro paragraph */
#intro {
    /* add: font-style: italic, color, margin */
}

/* TODO 3: Style .highlight */
.highlight {
    background-color: yellow;
    /* add: padding, border-left */
}

/* TODO 4: Style .card */
.card {
    background: white;
    border-radius: 8px;
    /* add: padding, margin, box-shadow */
}

/* TODO 5: Style .btn */
.btn {
    background-color: #4a90d9;
    color: white;
    border: none;
    border-radius: 4px;
    /* add: padding, cursor: pointer, font-size */
}

/* TODO 6: Hover effect */
.btn:hover {
    /* add: background-color change, transition */
}
"""

files["day 44/intermediate css/style.css"] = """\
/* ============================================================
   DAY 44: Intermediate CSS
   PROJECT: Style a full portfolio page with layout
   ============================================================

   SKILLS TODAY:
     display: flex / grid
     flexbox: justify-content, align-items, flex-wrap, gap
     CSS Grid: grid-template-columns, grid-gap
     position: static / relative / absolute / fixed / sticky
     z-index
     Media queries: @media (max-width: 768px) { }
     CSS variables: --primary-color: #4a90d9;
     Pseudo-classes: :hover, :focus, :nth-child()

   ============================================================ */

:root {
    --primary:    #4a90d9;
    --secondary:  #2d2d2d;
    --bg:         #f9f9f9;
    --text:       #333;
    --radius:     8px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body { font-family: "Segoe UI", sans-serif; background: var(--bg); color: var(--text); }

/* --- Navbar (position: sticky) --- */
nav {
    background: var(--secondary);
    color: white;
    padding: 16px 32px;
    /* TODO: position sticky, top: 0, z-index: 100 */
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav a { color: white; text-decoration: none; margin-left: 16px; }
nav a:hover { color: var(--primary); }

/* --- Hero section (flexbox centred) --- */
.hero {
    height: 60vh;
    display: flex;
    flex-direction: column;
    /* TODO: justify-content and align-items to centre content */
    text-align: center;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
}

/* --- Project cards (CSS Grid) --- */
.projects {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    padding: 40px;
}

.card {
    background: white;
    border-radius: var(--radius);
    padding: 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    /* TODO: add hover: transform: translateY(-4px), transition */
}

/* --- Mobile responsive --- */
@media (max-width: 768px) {
    .projects {
        /* TODO: change to single column grid */
    }
}
"""

files["day 44/intermediate css/index.html"] = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<nav>
    <span>wchen17</span>
    <div>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>
</nav>

<section class="hero">
    <h1>100 Days of Code</h1>
    <p>Building skills one day at a time.</p>
</section>

<section id="projects">
    <h2 style="text-align:center; padding:24px;">Projects</h2>
    <div class="projects">
        <div class="card"><h3>Day 4</h3><p>Rock Paper Scissors</p></div>
        <div class="card"><h3>Day 7</h3><p>Hangman</p></div>
        <div class="card"><h3>Day 11</h3><p>Blackjack</p></div>
        <!-- TODO: add more cards for your completed projects -->
    </div>
</section>

</body>
</html>
"""

files["day 45/web scraping.py"] = """\
# ============================================================
#  DAY 45: Web Scraping with BeautifulSoup
#  PROJECT: Scrape a website and extract structured data
# ============================================================
#
#  SKILLS TODAY:
#    - import requests                     → fetch the HTML
#    - from bs4 import BeautifulSoup       → parse HTML
#    - soup = BeautifulSoup(html, "html.parser")
#    - soup.find("tag")                    → first match
#    - soup.find_all("tag")                → all matches
#    - soup.find("tag", class_="name")     → match by class
#    - element.get_text()                  → inner text
#    - element["href"]                     → attribute value
#    - pip install requests beautifulsoup4
#
# ============================================================

import requests
from bs4 import BeautifulSoup

# --------------------------------------------------
#  DEMO: Scrape a simple page
# --------------------------------------------------
URL = "https://books.toscrape.com/"   # a practice scraping site

response = requests.get(URL)
soup     = BeautifulSoup(response.text, "html.parser")

# Find all book titles
books = soup.find_all("article", class_="product_pod")
print(f"Found {len(books)} books on this page\\n")

for book in books[:5]:   # just the first 5
    title  = book.find("h3").find("a")["title"]
    price  = book.find("p", class_="price_color").get_text()
    rating = book.find("p", class_="star-rating")["class"][1]
    print(f"{title} | {price} | Rating: {rating}")


# --------------------------------------------------
#  TODO 1: Scrape ALL pages (pagination)
# --------------------------------------------------
# The site has multiple pages: books.toscrape.com/catalogue/page-2.html etc.
# Loop through pages 1-50:
#   Fetch each page URL
#   Parse and extract book data
#   Stop when there's no "next" button

all_books = []

# for page_num in range(1, 51):
#     url  = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
#     resp = requests.get(url)
#     if resp.status_code != 200:
#         break
#     soup  = BeautifulSoup(resp.text, "html.parser")
#   TODO: extract books and append to all_books


# --------------------------------------------------
#  TODO 2: Save results to a CSV
# --------------------------------------------------
# import csv
# with open("books.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Title", "Price", "Rating"])
#     for book in all_books:
#         writer.writerow([book["title"], book["price"], book["rating"]])

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Scrape https://quotes.toscrape.com/: get quote text, author, tags
#  2. Find the top 5 rated books from the full 1000-book catalogue
#  3. Automatically open the cheapest book's detail page
# ============================================================
"""

files["day 46/spotify time machine.py"] = """\
# ============================================================
#  DAY 46: Web Scraping Project
#  PROJECT: Spotify Time Machine (Billboard → Playlist)
# ============================================================
#
#  SKILLS TODAY:
#    - Scrape Billboard Hot 100 for a given date
#    - Spotipy (Spotify API wrapper): pip install spotipy
#    - OAuth authentication with Spotipy
#    - Creating a private Spotify playlist
#    - Searching for tracks by name + year
#
#  pip install requests beautifulsoup4 spotipy
#
# ============================================================

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD: ")
URL  = f"https://www.billboard.com/charts/hot-100/{date}"

# --------------------------------------------------
#  TODO 1: Scrape the Billboard Hot 100 for that date
# --------------------------------------------------
# Fetch the URL and parse with BeautifulSoup
# Find the song title elements (inspect the page to find the right selector)
# Hint: look for <li> with class containing "chart-results-list" or
#       <h3> with id="title-of-a-story"

response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# song_titles_spans = soup.select("li ul li h3")  ← adjust selector as needed
# songs = [song.get_text().strip() for song in song_titles_spans]
songs = ["Song A", "Song B", "Song C"]   # placeholder until you scrape

print(f"Top songs from {date}:")
for i, song in enumerate(songs[:10], 1):
    print(f"  {i}. {song}")


# --------------------------------------------------
#  TODO 2: Authenticate with Spotify
# --------------------------------------------------
# Set up a Spotify app at developer.spotify.com
# Get Client ID, Client Secret, and set Redirect URI to http://example.com
# Add to .env: SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI", "http://example.com"),
        scope="playlist-modify-private",
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]


# --------------------------------------------------
#  TODO 3: Search for each song on Spotify
# --------------------------------------------------
# For each song name:
#   result = sp.search(q=f"track:{song} year:{date[:4]}", type="track")
#   If result found → get the URI from result["tracks"]["items"][0]["uri"]
#   Else → print that song wasn't found

song_uris = []
year = date.split("-")[0]

for song in songs:
    # result = sp.search(q=f"track:{song} year:{year}", type="track")
    # try:
    #     uri = result["tracks"]["items"][0]["uri"]
    #     song_uris.append(uri)
    # except IndexError:
    #     print(f"{song} not found on Spotify.")
    pass


# --------------------------------------------------
#  TODO 4: Create a private playlist and add the tracks
# --------------------------------------------------
# playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)
# sp.playlist_add_items(playlist["id"], song_uris)
# print(f"Playlist created: {playlist['external_urls']['spotify']}")
"""

files["day 47/amazon price tracker.py"] = """\
# ============================================================
#  DAY 47: Web Scraping Project
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
        f"Subject:Amazon Price Alert!\\n\\n"
        f"{title} is now ${price}\\n"
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
"""

files["day 48/selenium basics.py"] = """\
# ============================================================
#  DAY 48: Selenium WebDriver
#  PROJECT: Automate a Browser + Game Bot
# ============================================================
#
#  SKILLS TODAY:
#    - from selenium import webdriver
#    - driver.get(url)                         → open a page
#    - driver.find_element(By.NAME, "q")       → find element
#    - driver.find_element(By.ID, "id")
#    - driver.find_element(By.CSS_SELECTOR, ".class")
#    - driver.find_element(By.XPATH, "//tag")
#    - element.click()                         → click it
#    - element.send_keys("text")               → type into it
#    - element.text                            → get its text
#    - driver.execute_script("JS code")        → run JavaScript
#    - pip install selenium
#    - Also install the correct ChromeDriver for your Chrome version
#
# ============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# --------------------------------------------------
#  DEMO: Open a browser and search Google
# --------------------------------------------------
driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("Python selenium tutorial")
search_bar.send_keys(Keys.RETURN)
time.sleep(3)   # wait for results

print(driver.title)
driver.quit()


# --------------------------------------------------
#  TODO 1: Scrape Wikipedia with Selenium
# --------------------------------------------------
# Open https://en.wikipedia.org/wiki/Python_(programming_language)
# Find the first paragraph under "General-purpose language"
# Print its text

# driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
# TODO: find and print the first paragraph


# --------------------------------------------------
#  TODO 2: Fill in and submit a form
# --------------------------------------------------
# Open https://orteil.dashnet.org/cookieclicker/  (Cookie Clicker)
# Click the big cookie as fast as possible for 5 minutes
# Every minute, check if you can afford any upgrades and buy them
# Print your final score after 5 minutes

# driver = webdriver.Chrome()
# driver.get("https://orteil.dashnet.org/cookieclicker/")
# time.sleep(5)   # wait for page to load
# cookie = driver.find_element(By.ID, "bigCookie")

# TODO: 5-minute loop: click cookie, check upgrades every 60 seconds


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Use Selenium to automatically fill in your GitHub profile info
#  2. Add WebDriverWait for dynamic pages (better than time.sleep):
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#  3. Run headlessly (no visible window):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
# ============================================================
"""

files["day 49/job application bot.py"] = """\
# ============================================================
#  DAY 49: Selenium Bot
#  PROJECT: Automated Job Application Bot (LinkedIn Easy Apply)
# ============================================================
#
#  SKILLS TODAY:
#    - Logging in to a site with Selenium
#    - Navigating multiple pages
#    - Handling pop-ups and modals
#    - WebDriverWait for dynamic content
#    - Filling multi-step forms
#    - try/except for elements that may or may not appear
#
#  NOTE: Automating LinkedIn Easy Apply may violate their ToS.
#        Use this on a personal/test account and be responsible.
#
# ============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

EMAIL    = os.getenv("LINKEDIN_EMAIL",    "your@email.com")
PASSWORD = os.getenv("LINKEDIN_PASSWORD", "yourpassword")
JOB_URL  = "https://www.linkedin.com/jobs/search/?keywords=python+developer&f_LF=f_AL"

driver = webdriver.Chrome()
wait   = WebDriverWait(driver, 10)


# --------------------------------------------------
#  TODO 1: Log in to LinkedIn
# --------------------------------------------------
# driver.get("https://www.linkedin.com/login")
# Find email and password fields, fill them in, submit
# Wait for the home page to load

# --------------------------------------------------
#  TODO 2: Navigate to job listings
# --------------------------------------------------
# driver.get(JOB_URL)
# Find all "Easy Apply" job cards
# Loop through them

# --------------------------------------------------
#  TODO 3: Click "Easy Apply" and fill the form
# --------------------------------------------------
# Click the job listing
# Find and click the "Easy Apply" button
# Fill in phone number if asked
# Handle multi-step forms (click "Next", then "Submit")
# Handle the "follow company" checkbox
# Click "Submit application" on the final step

# --------------------------------------------------
#  TODO 4: Handle errors gracefully
# --------------------------------------------------
# Wrap each step in try/except
# If form is too complex (not single-step), close modal and skip

driver.quit()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Filter jobs by keyword, location, and date posted
#  2. Log each application (company, role, date) to a CSV
#  3. Add a delay between applications to avoid rate limiting
# ============================================================
"""

files["day 50/tinder bot.py"] = """\
# ============================================================
#  DAY 50: Selenium Bot
#  PROJECT: Tinder Auto-Swipe Bot
# ============================================================
#
#  SKILLS TODAY:
#    - Logging in via Facebook (OAuth flow in Selenium)
#    - execute_script() to bypass JS-blocked clicks
#    - Handling pop-ups (location access, notifications)
#    - ActionChains for complex interactions
#    - Exception handling when elements don't appear
#
#  NOTE: Use responsibly on your own account.
#        Tinder may block automated activity.
#
# ============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

driver = webdriver.Chrome()
driver.get("https://tinder.com")
time.sleep(2)


# --------------------------------------------------
#  TODO 1: Log in via Facebook
# --------------------------------------------------
# Click "Log in" → "Log in with Facebook"
# Switch to the Facebook popup window:
#   base_window = driver.current_window_handle
#   for window_handle in driver.window_handles:
#       if window_handle != base_window:
#           driver.switch_to.window(window_handle); break
# Fill in FB email + password, click Login
# Switch back to base_window


# --------------------------------------------------
#  TODO 2: Dismiss pop-ups (location, notifications, cookies)
# --------------------------------------------------
# Use try/except to click "Allow" or "Deny" buttons
# These appear randomly so wrap each in try/except NoSuchElementException

def dismiss_popups():
    try:
        deny_btn = driver.find_element(By.XPATH, "//button[text()='Deny']")
        deny_btn.click()
    except NoSuchElementException:
        pass
    # TODO: handle other popups (notifications, etc.)


# --------------------------------------------------
#  TODO 3: Auto-swipe right on a loop
# --------------------------------------------------
# Find the "Like" button and click it
# If a "It's a Match!" modal appears, close it
# Delay slightly between swipes to avoid detection

def like():
    try:
        like_btn = driver.find_element(By.XPATH, "//button[@aria-label='Like']")
        like_btn.click()
    except (NoSuchElementException, ElementClickInterceptedException):
        pass

for _ in range(100):
    time.sleep(1)
    like()
    # TODO: detect and close match pop-up if it appears

driver.quit()
"""

files["day 51/twitter complaint bot.py"] = """\
# ============================================================
#  DAY 51: Selenium Bot
#  PROJECT: Internet Speed Twitter Complaint Bot
# ============================================================
#
#  SKILLS TODAY:
#    - Scraping speedtest.net result with Selenium
#    - Conditional logic on scraped data
#    - Logging in to Twitter/X and posting a tweet via Selenium
#    - String formatting with f-strings in generated tweets
#
# ============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

PROMISED_DOWN = 150   # Mbps you pay for (download)
PROMISED_UP   = 10    # Mbps you pay for (upload)
TWITTER_EMAIL    = os.getenv("TWITTER_EMAIL", "your@email.com")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD", "yourpassword")

driver = webdriver.Chrome()


# --------------------------------------------------
#  TODO 1: Run a speed test at speedtest.net
# --------------------------------------------------
# driver.get("https://www.speedtest.net")
# Click the "Go" button
# Wait ~60 seconds for the test to complete
# Scrape the download and upload speed values
# Store as down_speed and up_speed (float)

def get_internet_speed():
    driver.get("https://www.speedtest.net")
    # Find and click the start button
    # Wait for results
    # Scrape download and upload
    return 80.0, 5.0   # placeholder

down_speed, up_speed = get_internet_speed()
print(f"Down: {down_speed} Mbps | Up: {up_speed} Mbps")


# --------------------------------------------------
#  TODO 2: Tweet a complaint if speed is below promised
# --------------------------------------------------
def tweet_complaint():
    driver.get("https://twitter.com/login")
    # Log in with email + password
    # Find the tweet compose box
    # Type the complaint message
    # Click "Post" / "Tweet"
    message = (
        f"Hey @ISPname, why is my internet so slow? "
        f"I'm paying for {PROMISED_DOWN}Mbps download but only getting "
        f"{down_speed}Mbps. Fix this! 😤"
    )
    print(f"Would tweet: {message}")

if down_speed < PROMISED_DOWN or up_speed < PROMISED_UP:
    tweet_complaint()
else:
    print("Speed is good! No complaint needed.")

driver.quit()
"""

files["day 52/instagram bot.py"] = """\
# ============================================================
#  DAY 52: Selenium Bot
#  PROJECT: Instagram Follower Bot
# ============================================================
#
#  SKILLS TODAY:
#    - Instagram login automation
#    - Navigating to a competitor's follower list
#    - Scrolling a modal to load more followers
#    - Clicking "Follow" on each account
#    - Handling "Already following" and dialog states
#
#  NOTE: Instagram actively detects bots. Use slowly,
#        on a test account, with long delays.
#
# ============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
import os

USERNAME  = os.getenv("IG_USERNAME", "your_username")
PASSWORD  = os.getenv("IG_PASSWORD", "your_password")
TARGET    = "natgeo"   # account whose followers you'll follow

driver = webdriver.Chrome()


# --------------------------------------------------
#  TODO 1: Log in to Instagram
# --------------------------------------------------
# driver.get("https://www.instagram.com/accounts/login/")
# time.sleep(3)
# Find username + password fields, fill in, click Log In
# Handle "Save Info?" and "Turn on Notifications?" pop-ups


# --------------------------------------------------
#  TODO 2: Navigate to target account's followers list
# --------------------------------------------------
# driver.get(f"https://www.instagram.com/{TARGET}/")
# Find and click the "X followers" link
# Wait for the modal to open


# --------------------------------------------------
#  TODO 3: Scroll the follower modal and follow everyone
# --------------------------------------------------
# Scroll the modal window down to load more followers
# Find all "Follow" buttons
# Click each one
# If a pop-up appears (rate limited) → close it
# Add time.sleep(1) between follows to be less suspicious

def follow_all_visible():
    follow_buttons = driver.find_elements(By.XPATH, "//button[text()='Follow']")
    for btn in follow_buttons:
        try:
            btn.click()
            time.sleep(1)
        except ElementClickInterceptedException:
            pass   # skip if blocked

# Loop: scroll and follow in batches
for _ in range(10):
    follow_all_visible()
    # TODO: scroll the follower list modal down to load more

driver.quit()
"""

files["day 53/data entry bot.py"] = """\
# ============================================================
#  DAY 53: Web Scraping Capstone
#  PROJECT: Automated Data Entry (Zillow → Google Form)
# ============================================================
#
#  SKILLS TODAY:
#    - Multi-step scraping pipeline
#    - BeautifulSoup to collect structured data
#    - Selenium to fill and submit a Google Form automatically
#    - Combining scraping + automation in one script
#
# ============================================================

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --------------------------------------------------
#  TODO 1: Scrape rental listings from Zillow (or similar site)
# --------------------------------------------------
# Some sites block scrapers: use https://appbrewery.github.io/Zillow-Clone/
# (a practice clone made for this exercise)

ZILLOW_CLONE = "https://appbrewery.github.io/Zillow-Clone/"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(ZILLOW_CLONE, headers=headers)
soup     = BeautifulSoup(response.text, "html.parser")

# --------------------------------------------------
#  TODO 2: Extract addresses, prices, and links
# --------------------------------------------------
# Inspect the page HTML and find the right selectors
# Build three parallel lists: addresses, prices, links

addresses = []   # TODO: soup.find_all(...)
prices    = []   # TODO
links     = []   # TODO

print(f"Found {len(addresses)} listings")


# --------------------------------------------------
#  TODO 3: Create a Google Form with 3 questions:
#          Address | Monthly Rent | Link
# --------------------------------------------------
# Go to forms.google.com and create the form
# Copy the form's "Fill out form" URL
FORM_URL = "YOUR_GOOGLE_FORM_URL_HERE"   # TODO: replace


# --------------------------------------------------
#  TODO 4: Use Selenium to submit one entry per listing
# --------------------------------------------------
driver = webdriver.Chrome()

for i in range(len(addresses)):
    driver.get(FORM_URL)
    time.sleep(2)

    # TODO: find the three input fields and fill them in
    # field1 = driver.find_element(By.XPATH, "//input[1]")
    # field1.send_keys(addresses[i])
    # ... fill price and link similarly
    # submit_btn = driver.find_element(By.XPATH, "//span[text()='Submit']")
    # submit_btn.click()

    print(f"Submitted: {addresses[i] if addresses else 'placeholder'}")

driver.quit()
"""

files["day 54/flask intro/app.py"] = """\
# ============================================================
#  DAY 54: Flask Web Framework Intro
#  PROJECT: Your first Flask web server
# ============================================================
#
#  SKILLS TODAY:
#    - from flask import Flask
#    - app = Flask(__name__)
#    - @app.route("/path")       → bind a URL to a function
#    - return "HTML string"      → simplest response
#    - return render_template()  → serve an HTML file
#    - app.run(debug=True)       → start dev server with auto-reload
#    - HTTP methods: GET (default), POST
#    - Dynamic routes: /user/<name>
#
#  pip install flask
#
# ============================================================

from flask import Flask, render_template

app = Flask(__name__)


# --------------------------------------------------
#  Route 1: Home page
# --------------------------------------------------
@app.route("/")
def home():
    return "<h1>Hello, World!</h1><p>My first Flask app.</p>"


# --------------------------------------------------
#  TODO 1: Add a /hello route
# --------------------------------------------------
# Return a personalised greeting as an HTML string

# @app.route("/hello")
# def hello():
#     return ...


# --------------------------------------------------
#  TODO 2: Dynamic route /hello/<name>
# --------------------------------------------------
# The <name> part of the URL becomes a parameter
# Return "Hello, {name.title()}!" as HTML

# @app.route("/hello/<name>")
# def greet(name):
#     return ...


# --------------------------------------------------
#  TODO 3: /about route: render an HTML template
# --------------------------------------------------
# Create templates/about.html (see below)
# Use render_template("about.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")


# --------------------------------------------------
#  TODO 4: Return different HTTP status codes
# --------------------------------------------------
# Flask lets you return a tuple: (response, status_code)
# @app.route("/not-found")
# def not_found():
#     return "This page doesn't exist.", 404


if __name__ == "__main__":
    app.run(debug=True)

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a /random route that returns a random number on each visit
#  2. Use jsonify() to return JSON instead of HTML
#     from flask import jsonify
#  3. Add a decorator that prints a log message before every request:
#     @app.before_request
#     def log_request(): print("Request incoming!")
# ============================================================
"""

files["day 54/flask intro/templates/about.html"] = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
    <h1>About Me</h1>
    <p>This page is served by Flask via render_template().</p>
    <a href="/">Back to Home</a>
</body>
</html>
"""

files["day 55/flask routing/app.py"] = """\
# ============================================================
#  DAY 55: Flask Routing & HTML Parsing
#  PROJECT: Higher or Lower Game (web version)
# ============================================================
#
#  SKILLS TODAY:
#    - Multiple routes in one app
#    - url_for("function_name")     → generate URLs safely
#    - redirect(url_for("..."))     → redirect the browser
#    - Dynamic URL segments         → /guess/<int:number>
#    - Passing variables to templates → render_template("x.html", var=value)
#    - request.args                 → URL query parameters (?key=value)
#    - global variables in Flask    → careful with state between requests
#    - random number game logic across routes
#
# ============================================================

from flask import Flask, render_template, redirect, url_for
import random

app   = Flask(__name__)
LIMIT = 10
random_number = random.randint(1, LIMIT)


@app.route("/")
def home():
    global random_number
    random_number = random.randint(1, LIMIT)
    return render_template("home.html", limit=LIMIT)


# --------------------------------------------------
#  TODO 1: /guess/<int:guess> route
# --------------------------------------------------
# Compare guess to random_number
# Return render_template for:
#   "too_high.html" if guess > random_number
#   "too_low.html"  if guess < random_number
#   "correct.html"  if guess == random_number

@app.route("/guess/<int:guess>")
def check_guess(guess):
    pass   # TODO


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 55/flask routing/templates/home.html"] = """\
<!DOCTYPE html>
<html>
<head><title>Guess the Number</title></head>
<body>
    <h1>Guess a number between 1 and {{ limit }}</h1>
    <!-- TODO: make each number 1-limit a clickable link to /guess/{number} -->
    {% for n in range(1, limit + 1) %}
        <a href="/guess/{{ n }}">{{ n }}</a>
    {% endfor %}
</body>
</html>
"""

files["day 56/name card/app.py"] = """\
# ============================================================
#  DAY 56: Static Files & Templates
#  PROJECT: Personal Name Card Website
# ============================================================
#
#  SKILLS TODAY:
#    - static/ folder for CSS, images, JS
#    - url_for("static", filename="style.css")  → correct static URL
#    - render_template with variables
#    - Creating a multi-file Flask project:
#        app.py
#        templates/index.html
#        static/style.css
#        static/profile.jpg (optional)
#
# ============================================================

from flask import Flask, render_template

app = Flask(__name__)

# User data (in a real app, this would come from a database)
user = {
    "name":       "wchen17",
    "title":      "Aspiring Python Developer",
    "email":      "apexofficial21@gmail.com",
    "github":     "https://github.com/wchen17",
    "bio":        "100 Days of Code: building skills one day at a time.",
    "skills":     ["Python", "Flask", "Selenium", "APIs", "Data Science"],
    "days_done":  56,
}


@app.route("/")
def home():
    return render_template("index.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 56/name card/templates/index.html"] = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ user.name }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="card">
        <h1>{{ user.name }}</h1>
        <h2>{{ user.title }}</h2>
        <p>{{ user.bio }}</p>

        <h3>Skills</h3>
        <ul>
        {% for skill in user.skills %}
            <li>{{ skill }}</li>
        {% endfor %}
        </ul>

        <p>Days completed: <strong>{{ user.days_done }}/100</strong></p>

        <div class="links">
            <a href="mailto:{{ user.email }}">Email</a>
            <a href="{{ user.github }}" target="_blank">GitHub</a>
        </div>
    </div>
    <!-- TODO: add your own styling in static/style.css -->
</body>
</html>
"""

files["day 56/name card/static/style.css"] = """\
/* TODO: Style your name card */
body { font-family: Arial, sans-serif; background: #1e1e2e; color: #cdd6f4; display: flex; justify-content: center; padding: 40px; }
.card { background: #313244; border-radius: 12px; padding: 40px; max-width: 500px; width: 100%; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
h1 { color: #cba6f7; }
h2 { color: #89b4fa; font-weight: normal; }
.links a { margin-right: 16px; color: #89dceb; }
"""

files["day 57/jinja blog/app.py"] = """\
# ============================================================
#  DAY 57: Jinja2 Templating
#  PROJECT: Blog with dynamic posts from an API
# ============================================================
#
#  SKILLS TODAY:
#    - Jinja2 syntax inside HTML templates:
#        {{ variable }}           → output a value
#        {% if condition %}       → conditional block
#        {% for item in list %}   → loop
#        {% extends "base.html" %} → template inheritance
#        {% block content %} {% endblock %}
#    - Template inheritance: base layout + child templates
#    - Fetching real data from a JSON API to render dynamically
#
# ============================================================

from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()[:10]   # first 10 posts


@app.route("/")
def home():
    posts = get_posts()
    return render_template("index.html", posts=posts, title="My Blog")


# --------------------------------------------------
#  TODO 1: /post/<int:post_id> route
# --------------------------------------------------
# Fetch a single post: GET https://jsonplaceholder.typicode.com/posts/{id}
# Render post.html with the post data

@app.route("/post/<int:post_id>")
def get_post(post_id):
    pass   # TODO


if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 57/jinja blog/templates/base.html"] = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Blog{% endblock %}</title>
    <style>
        body { font-family: Georgia, serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        nav a { margin-right: 16px; }
        .post-card { border-bottom: 1px solid #ddd; padding: 16px 0; }
    </style>
</head>
<body>
    <nav><a href="/">Home</a><a href="/about">About</a></nav>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
"""

files["day 57/jinja blog/templates/index.html"] = """\
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<h1>{{ title }}</h1>

{% for post in posts %}
<div class="post-card">
    <h2><a href="/post/{{ post.id }}">{{ post.title | title }}</a></h2>
    <p>{{ post.body[:100] }}...</p>
</div>
{% endfor %}

{% endblock %}
"""

files["day 57/jinja blog/templates/post.html"] = """\
{% extends "base.html" %}

{% block title %}{{ post.title | title }}{% endblock %}

{% block content %}
<!-- TODO: display the full post title and body -->
<!-- Also add a "Back to all posts" link -->
{% endblock %}
"""

files["day 58/bootstrap blog/app.py"] = """\
# ============================================================
#  DAY 58: Bootstrap CSS Framework
#  PROJECT: Bootstrap-styled Blog
# ============================================================
#
#  SKILLS TODAY:
#    - Bootstrap via CDN (no install needed)
#    - Bootstrap grid: container, row, col-md-X
#    - Bootstrap components: navbar, cards, buttons, badges
#    - Bootstrap utilities: m-3, p-4, text-center, bg-dark, etc.
#    - Combining Bootstrap with Jinja2 templates
#
#  HOW TO USE BOOTSTRAP:
#    Add to <head>:
#    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
#    Add before </body>:
#    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
#
# ============================================================

from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_posts():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    return resp.json()[:6]

@app.route("/")
def home():
    return render_template("index.html", posts=get_posts())

@app.route("/post/<int:post_id>")
def post(post_id):
    resp = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    return render_template("post.html", post=resp.json())

if __name__ == "__main__":
    app.run(debug=True)
"""

files["day 58/bootstrap blog/templates/base.html"] = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}Blog{% endblock %}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="/">My Blog</a>
        <div class="navbar-nav">
            <a class="nav-link" href="/">Home</a>
            <a class="nav-link" href="/about">About</a>
        </div>
    </div>
</nav>

<div class="container mt-4">
    {% block content %}{% endblock %}
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

files["day 58/bootstrap blog/templates/index.html"] = """\
{% extends "base.html" %}
{% block title %}Home: My Blog{% endblock %}
{% block content %}

<h1 class="mb-4">Latest Posts</h1>

<!-- TODO: display posts in a Bootstrap card grid (3 columns) -->
<div class="row g-4">
{% for post in posts %}
<div class="col-md-4">
    <div class="card h-100">
        <div class="card-body">
            <h5 class="card-title">{{ post.title | title }}</h5>
            <p class="card-text text-muted">{{ post.body[:80] }}...</p>
        </div>
        <div class="card-footer">
            <a href="/post/{{ post.id }}" class="btn btn-primary btn-sm">Read More</a>
        </div>
    </div>
</div>
{% endfor %}
</div>

{% endblock %}
"""

for filepath, content in files.items():
    full_path = os.path.join(base, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Created: {filepath}")

print("Done: Days 32-58 written.")
