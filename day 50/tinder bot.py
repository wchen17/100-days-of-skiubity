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
