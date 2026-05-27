# ============================================================
#  DAY 92: Portfolio Project
#  PROJECT: Custom Web Scraper CLI Tool
# ============================================================
#
#  SKILLS USED: requests, BeautifulSoup, argparse, pandas, CSV
#
#  REQUIREMENTS:
#    - Accept a URL and CSS selector via command line arguments
#    - Scrape all matching elements from the page
#    - Save results to CSV or JSON
#    - Optional: follow pagination (?page=N) up to a limit
#    - Handle errors gracefully (bad URL, no results)
#
#  Usage:
#    python scraper.py --url https://books.toscrape.com --selector "h3 a" --output books.csv
#
# ============================================================

import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Web scraper CLI tool")
    parser.add_argument("--url",      required=True,    help="URL to scrape")
    parser.add_argument("--selector", required=True,    help="CSS selector for target elements")
    parser.add_argument("--output",   default="output.csv", help="Output file (csv or json)")
    parser.add_argument("--pages",    type=int, default=1, help="Number of pages to scrape")
    parser.add_argument("--delay",    type=float, default=1.0, help="Delay between page requests (seconds)")
    return parser.parse_args()


def scrape_page(url, selector):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    soup     = BeautifulSoup(response.text, "html.parser")
    elements = soup.select(selector)

    results = []
    for el in elements:
        results.append({
            "text": el.get_text(strip=True),
            "href": el.get("href", ""),
            "src":  el.get("src",  ""),
        })
    return results


def save_results(data, output_path):
    if output_path.endswith(".json"):
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)
    else:
        pd.DataFrame(data).to_csv(output_path, index=False)
    print(f"Saved {len(data)} results to {output_path}")


# --------------------------------------------------
#  TODO: Add pagination support
# --------------------------------------------------
# For pages 1 to args.pages:
#   Construct page URL (try appending ?page=N or /page/N)
#   Scrape and append results
#   time.sleep(args.delay) between requests

def main():
    args    = parse_args()
    all_data = []

    import time
    for page_num in range(1, args.pages + 1):
        if args.pages > 1:
            url = f"{args.url.rstrip('/')}/page/{page_num}"
        else:
            url = args.url

        print(f"Scraping page {page_num}: {url}")
        results = scrape_page(url, args.selector)
        if not results:
            print("No results found or page doesn't exist. Stopping.")
            break
        all_data.extend(results)
        if page_num < args.pages:
            time.sleep(args.delay)

    if all_data:
        save_results(all_data, args.output)
    else:
        print("No data collected.")
        sys.exit(1)

if __name__ == "__main__":
    main()
