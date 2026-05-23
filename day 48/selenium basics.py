# ============================================================
#  DAY 48 — Selenium WebDriver
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

# TODO: 5-minute loop — click cookie, check upgrades every 60 seconds


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
