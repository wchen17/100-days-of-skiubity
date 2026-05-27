# ============================================================
#  DAY 97: Portfolio Project
#  PROJECT: Multi-purpose Percentage Calculator (CLI + GUI)
# ============================================================
#
#  SKILLS USED: Tkinter, OOP, string formatting, maths
#
#  CALCULATIONS:
#    1. X% of Y            → what is 15% of 200?
#    2. X is what % of Y?  → 30 is what % of 200?
#    3. % increase/decrease → 50 to 75 is what % increase?
#    4. Add/subtract %      → 200 + 15% = ?
#    5. Reverse % (% before increase) → 230 after 15% increase = what was original?
#
# ============================================================

import tkinter as tk
from tkinter import ttk

def percent_of(x, y):        return x / 100 * y
def what_percent(x, y):      return (x / y) * 100 if y != 0 else 0
def percent_change(old, new): return ((new - old) / old) * 100 if old != 0 else 0
def add_percent(value, pct): return value + (value * pct / 100)
def reverse_percent(final, pct): return final / (1 + pct / 100)


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Percentage Calculator")
        self.root.config(padx=30, pady=30)
        self.build_tabs()

    def build_tabs(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill=tk.BOTH)

        self.build_tab(notebook, "X% of Y",
            ["Percentage (X)", "Value (Y)"],
            lambda vals: f"{vals[0]}% of {vals[1]} = {percent_of(vals[0], vals[1]):.2f}")

        self.build_tab(notebook, "X is what %",
            ["Value (X)", "Total (Y)"],
            lambda vals: f"{vals[0]} is {what_percent(vals[0], vals[1]):.2f}% of {vals[1]}")

        self.build_tab(notebook, "% Change",
            ["Old Value", "New Value"],
            lambda vals: f"Change: {percent_change(vals[0], vals[1]):+.2f}%")

        # --------------------------------------------------
        #  TODO: Add tabs for "Add/subtract %" and "Reverse %"
        # --------------------------------------------------

    def build_tab(self, notebook, title, labels, formula):
        frame = tk.Frame(notebook, padx=20, pady=20)
        notebook.add(frame, text=title)

        entries = []
        for label in labels:
            tk.Label(frame, text=label + ":").pack()
            entry = tk.Entry(frame, width=20, font=("Arial", 14))
            entry.pack(pady=4)
            entries.append(entry)

        result_var = tk.StringVar(value="Enter values above")
        tk.Label(frame, textvariable=result_var, font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

        def calculate():
            try:
                vals = [float(e.get()) for e in entries]
                result_var.set(formula(vals))
            except ValueError:
                result_var.set("Please enter valid numbers")

        tk.Button(frame, text="Calculate", command=calculate,
                  bg="#4CAF50", fg="white", font=("Arial", 12)).pack()


root = tk.Tk()
app  = CalculatorApp(root)
root.mainloop()
