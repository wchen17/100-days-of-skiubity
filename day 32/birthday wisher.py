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
sample_csv = "name,email,year,month,day\nAlice,alice@example.com,1990,5,23\nBob,bob@example.com,1985,5,23"
with open("birthdays.csv", "w") as f:
    f.write(sample_csv)

# Sample letter templates
import os
os.makedirs("letter_templates", exist_ok=True)
with open("letter_templates/letter_1.txt", "w") as f:
    f.write("Dear [NAME],\n\nWishing you a wonderful birthday! Hope your day is amazing.\n\nCheers!")
with open("letter_templates/letter_2.txt", "w") as f:
    f.write("Happy Birthday [NAME]!\n\nMay this year bring you joy and success.\n\nBest wishes!")


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
    #       msg=f"Subject:Happy Birthday!\n\n{contents}"
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
