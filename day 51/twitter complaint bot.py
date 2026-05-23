# ============================================================
#  DAY 51 — Selenium Bot
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
