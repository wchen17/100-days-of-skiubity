# ============================================================
#  DAY 53 — Web Scraping Capstone
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
# Some sites block scrapers — use https://appbrewery.github.io/Zillow-Clone/
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
