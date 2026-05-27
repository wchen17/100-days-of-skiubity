# ============================================================
#  DAY 29: Tkinter App: Password Manager
#  PROJECT: Password Manager with File Storage
# ============================================================
#
#  SKILLS TODAY:
#    - tkinter messagebox         → popup dialogs
#    - pyperclip                  → copy text to clipboard
#    - File append ("a" mode)     → save passwords to a file
#    - Entry.delete(0, END)       → clear an input field
#    - PhotoImage                 → display a logo
#    - Generating random passwords (reuse Day 5 logic)
#
#  pip install pyperclip
#
# ============================================================

import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
import string


# --------------------------------------------------
#  TODO 1: generate_password()
# --------------------------------------------------
# Build a random strong password (letters + numbers + symbols)
# Insert it into the password_entry field
# Copy it to clipboard with pyperclip.copy(password)

def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols)  for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers)  for _ in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# --------------------------------------------------
#  TODO 2: save()
# --------------------------------------------------
# Get website, email, password from entries
# If any field is empty → show messagebox.showwarning(...)
# Otherwise:
#   Show messagebox.askokcancel() with details to confirm
#   If OK:
#     Append to "data.txt" in format:  website | email | password\n
#     Clear website and password fields
#     Focus cursor back on website field

def save():
    website  = website_entry.get()
    email    = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?"
    )

    if is_ok:
        pass  # TODO: write to file, clear fields


# --------------------------------------------------
#  UI Setup
# --------------------------------------------------
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo placeholder (replace with canvas + image if you have the file)
canvas = tk.Canvas(height=200, width=200)
canvas.create_rectangle(0, 0, 200, 200, fill="#4a90d9")
canvas.create_text(100, 100, text="🔐", font=("Arial", 60))
canvas.grid(row=0, column=1)

# Website row
tk.Label(text="Website:").grid(row=1, column=0)
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email row
tk.Label(text="Email/Username:").grid(row=2, column=0)
email_entry = tk.Entry(width=35)
email_entry.insert(0, "apexofficial21@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Password row
tk.Label(text="Password:").grid(row=3, column=0)
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)
gen_button = tk.Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2)

# Add button
add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
