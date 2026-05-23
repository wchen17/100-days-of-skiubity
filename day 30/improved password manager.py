# ============================================================
#  DAY 30 — Error Handling & JSON
#  PROJECT: Improved Password Manager (search + JSON storage)
# ============================================================
#
#  SKILLS TODAY:
#    - try / except / else / finally
#    - except ExceptionType as e:
#    - import json
#    - json.loads(str)     → parse JSON string to dict
#    - json.dumps(dict)    → dict to JSON string
#    - json.load(file)     → read JSON from file
#    - json.dump(dict, file, indent=4) → write JSON to file
#    - FileNotFoundError   → handle missing files gracefully
#    - KeyError            → handle missing dict keys
#
# ============================================================

import tkinter as tk
from tkinter import messagebox
import json
import random
import string
import pyperclip


# --------------------------------------------------
#  TODO 1: Upgrade save() to use JSON instead of plain text
# --------------------------------------------------
# Data format in data.json:
# {
#   "Amazon": {"email": "user@gmail.com", "password": "abc123"},
#   "GitHub": {"email": "user@gmail.com", "password": "xyz789"}
# }
#
# Steps:
#   1. Try to open data.json and json.load() it → existing_data dict
#   2. Except FileNotFoundError → existing_data = {}
#   3. Update: existing_data[website] = {"email": email, "password": password}
#   4. Write back with json.dump(existing_data, f, indent=4)

def save():
    website  = website_entry.get().title()
    email    = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showwarning(title="Oops", message="Don't leave fields empty!")
        return

    new_data = {website: {"email": email, "password": password}}

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # TODO: merge new_data into data, then write back to file


# --------------------------------------------------
#  TODO 2: find_password()
# --------------------------------------------------
# Get website from entry (title-case it)
# Try to open data.json → json.load
# Except FileNotFoundError → messagebox "No data file found"
# Try data[website] → get email + password
# Except KeyError → messagebox "No details for {website} exist"
# On success → messagebox.showinfo with email and password

def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        pass  # TODO: look up website and show details or error


# --------------------------------------------------
#  TODO 3: generate_password() — same as Day 29
# --------------------------------------------------
def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '*', '+']
    pw = [random.choice(letters) for _ in range(8)] + \
         [random.choice(symbols)  for _ in range(3)] + \
         [random.choice(numbers)  for _ in range(3)]
    random.shuffle(pw)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, "".join(pw))
    pyperclip.copy("".join(pw))


# --------------------------------------------------
#  UI (same as Day 29, with a Search button added)
# --------------------------------------------------
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

tk.Label(text="Website:").grid(row=1, column=0)
website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = tk.Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

tk.Label(text="Email/Username:").grid(row=2, column=0)
email_entry = tk.Entry(width=35)
email_entry.insert(0, "apexofficial21@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

tk.Label(text="Password:").grid(row=3, column=0)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)
tk.Button(text="Generate Password", command=generate_password).grid(row=3, column=2)

tk.Button(text="Add", width=36, command=save).grid(row=4, column=1, columnspan=2)

window.mainloop()
