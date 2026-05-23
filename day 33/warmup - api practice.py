# ============================================================
#  DAY 33 — WARM-UP DRILLS: First API Calls
# ============================================================
#  APIs need the internet, so these can't be self-checked with
#  asserts offline. This one has light scaffold + TODOs.
#  All APIs below are FREE and need NO key.
#  Do these BEFORE iss notifier.py
#
#  pip install requests
# ============================================================

import requests


# --- Drill 1: guess an age from a name ----------------------
# API: https://api.agify.io?name=SOMENAME
# It returns JSON like: {"name": "michael", "age": 56, "count": ...}
def guess_age(name):
    # TODO:
    #   1. response = requests.get("https://api.agify.io", params={"name": name})
    #   2. response.raise_for_status()
    #   3. data = response.json()
    #   4. return data["age"]
    pass


# --- Drill 2: a random useless fact -------------------------
# API: https://uselessfacts.jsph.pl/api/v2/facts/random
# Returns JSON with a "text" key.
def random_fact():
    # TODO: GET the url, parse json, return the "text" field
    pass


# --- Drill 3: check a status code ---------------------------
# GET https://httpbin.org/status/404 and RETURN the numeric
# status code (response.status_code). It should be 404.
# Then try /status/200 and /status/500 to see them change.
def get_status(code):
    # TODO: requests.get(f"https://httpbin.org/status/{code}")
    #       return response.status_code
    pass


# --- Drill 4: API with parameters ---------------------------
# API: https://api.coindesk.com/v1/bpi/currentprice.json (Bitcoin price)
# OR:  https://api.frankfurter.app/latest?from=USD&to=EUR (exchange rate)
# Use params={} and dig into the nested JSON to return the EUR rate.
def usd_to_eur():
    # TODO: GET frankfurter, params {"from": "USD", "to": "EUR"}
    #       return response.json()["rates"]["EUR"]
    pass


# ============================================================
#  TRY IT (uncomment once you've filled the functions in):
# ============================================================
# print("Age for 'Michael':", guess_age("Michael"))
# print("Random fact:", random_fact())
# print("Status test:", get_status(404))
# print("1 USD in EUR:", usd_to_eur())

print("Fill in the functions above, then uncomment the TRY IT block.")
print("If a call works, you're ready for the ISS notifier project.")
