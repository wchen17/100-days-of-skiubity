# ============================================================
#  DAY 37 — API POST Requests & Pixela
#  PROJECT: Habit Tracker (Graph your daily coding/exercise)
# ============================================================
#
#  SKILLS TODAY:
#    - HTTP POST requests: requests.post(url, json={...})
#    - HTTP PUT / DELETE requests
#    - Custom request headers: {"X-USER-TOKEN": token}
#    - Pixela API (free): graph your habits at pixe.la
#    - datetime.date.today().strftime("%Y%m%d")
#
#  SETUP (run once):
#    1. Create Pixela account (run TODO 1 once)
#    2. Create a graph (run TODO 2 once)
#    3. Post/update pixels daily (TODO 3/4)
#
# ============================================================

import requests
from datetime import datetime

USERNAME  = "your_username"    # TODO: pick a unique Pixela username
TOKEN     = "your_token"       # TODO: any string, acts as your password
GRAPH_ID  = "coding-graph"

pixela_endpoint = "https://pixe.la/v1/users"
headers = {"X-USER-TOKEN": TOKEN}


# --------------------------------------------------
#  TODO 1: Create Pixela account (run ONCE, then comment out)
# --------------------------------------------------
# POST https://pixe.la/v1/users
# body JSON: {"token": TOKEN, "username": USERNAME,
#             "agreeTermsOfService": "yes", "notMinor": "yes"}

user_params = {
    "token":                TOKEN,
    "username":             USERNAME,
    "agreeTermsOfService":  "yes",
    "notMinor":             "yes",
}
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)


# --------------------------------------------------
#  TODO 2: Create a graph (run ONCE, then comment out)
# --------------------------------------------------
# POST https://pixe.la/v1/users/{USERNAME}/graphs
# headers: X-USER-TOKEN
# body: {"id": GRAPH_ID, "name": "Coding Graph",
#        "unit": "hours", "type": "float", "color": "momiji"}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":    GRAPH_ID,
    "name":  "Coding Graph",
    "unit":  "hours",
    "type":  "float",
    "color": "momiji",
}
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# Your graph will be at: https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html


# --------------------------------------------------
#  TODO 3: Post today's pixel (run daily)
# --------------------------------------------------
# POST https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}
# body: {"date": "YYYYMMDD", "quantity": "hours coded today"}

today = datetime.now().strftime("%Y%m%d")
hours = input("How many hours did you code today? ")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {"date": today, "quantity": hours}
# response = requests.post(pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# --------------------------------------------------
#  TODO 4: Update a pixel (if you made a mistake)
# --------------------------------------------------
# PUT https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}
# body: {"quantity": "new_value"}

update_date = input("Which date to update? (YYYYMMDD): ")
new_hours   = input("Corrected hours: ")
update_endpoint = f"{pixel_endpoint}/{update_date}"
# response = requests.put(update_endpoint, json={"quantity": new_hours}, headers=headers)
# print(response.text)


# --------------------------------------------------
#  TODO 5: Delete a pixel
# --------------------------------------------------
# DELETE https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{DATE}
delete_date = input("Which date to delete? (YYYYMMDD): ")
delete_endpoint = f"{pixel_endpoint}/{delete_date}"
# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)
