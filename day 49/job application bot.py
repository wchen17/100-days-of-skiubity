# ============================================================
#  DAY 49 — Selenium Bot
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
