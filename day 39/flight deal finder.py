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
