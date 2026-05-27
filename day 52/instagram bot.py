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
