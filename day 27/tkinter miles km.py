# ============================================================
#  DAY 27: Tkinter GUI & Layout
#  PROJECT: Miles-to-Kilometres Converter
# ============================================================
#
#  SKILLS TODAY:
#    - import tkinter as tk       → GUI library
#    - tk.Tk()                    → create the main window
#    - tk.Label(window, text="")  → display text
#    - tk.Entry(window)           → text input field
#    - tk.Button(window, text="", command=func)
#    - widget.grid(row, column, padx, pady)
#    - widget.get()               → read Entry value
#    - widget.config(text="")     → update a label's text
#    - window.mainloop()          → start the event loop
#    - *args and **kwargs         → flexible arguments
#
# ============================================================

import tkinter as tk

# --------------------------------------------------
#  DEMO: Minimal Tkinter window
# --------------------------------------------------
# window = tk.Tk()
# window.title("My App")
# my_label = tk.Label(text="Hello, Tkinter!")
# my_label.pack()
# window.mainloop()


# --------------------------------------------------
#  PROJECT: Miles → Km Converter
# --------------------------------------------------
# Layout:
#   Row 0: [Entry field]  "Miles"
#   Row 1: "is equal to"  [Result label]  "Km"
#   Row 2:                [Calculate button]

def miles_to_km():
    # --------------------------------------------------
    #  TODO: Read miles from entry, convert, update result label
    # --------------------------------------------------
    # miles = float(miles_input.get())
    # km    = miles * 1.60934
    # km_result_label.config(text=f"{km:.2f}")
    pass


window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Miles input
miles_input = tk.Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

# "is equal to" label
equal_label = tk.Label(text="is equal to")
equal_label.grid(row=1, column=0)

# Result label
km_result_label = tk.Label(text=0)
km_result_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)

# Calculate button
calc_button = tk.Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a reverse converter (Km → Miles)
#  2. Add a dropdown to choose the unit type:
#     Miles/Km, Celsius/Fahrenheit, Kg/Lbs
#  3. Style it with background colours and fonts:
#     tk.Label(bg="#1e1e2e", fg="white", font=("Arial", 14))
# ============================================================
