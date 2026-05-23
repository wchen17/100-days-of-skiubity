# ============================================================
#  DAY 45 — Web Scraping with BeautifulSoup
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
print(f"Found {len(books)} books on this page\n")

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
#  1. Scrape https://quotes.toscrape.com/ — get quote text, author, tags
#  2. Find the top 5 rated books from the full 1000-book catalogue
#  3. Automatically open the cheapest book's detail page
# ============================================================
