# ============================================================
#  DAY 85 — Portfolio Project
#  PROJECT: Typing Speed Test App
# ============================================================
#
#  SKILLS USED: Tkinter, time, string comparison, WPM calculation
#
#  REQUIREMENTS:
#    - Show a random paragraph of text to type
#    - Start timer on first keypress
#    - Highlight correct characters in green, mistakes in red
#    - When done: show WPM, accuracy %, and time taken
#    - Allow restarting with a new text
#
# ============================================================

import tkinter as tk
import time
import random

TEXTS = [
    "The quick brown fox jumps over the lazy dog and then runs away.",
    "Python is a high-level general-purpose programming language.",
    "Practice makes perfect. The more you code, the better you get.",
    "Every expert was once a beginner. Keep going, one day at a time.",
]

class TypingTest:
    def __init__(self, root):
        self.root       = root
        self.root.title("Typing Speed Test")
        self.root.config(padx=40, pady=40)
        self.start_time = None
        self.setup_ui()
        self.new_test()

    def setup_ui(self):
        self.sample_label = tk.Label(self.root, font=("Courier", 16), wraplength=600,
                                     justify=tk.LEFT, bg="#f0f0f0", relief="ridge", padx=10, pady=10)
        self.sample_label.pack(fill=tk.X, pady=(0, 20))

        self.text_entry = tk.Text(self.root, font=("Courier", 16), height=4, width=60)
        self.text_entry.pack()
        self.text_entry.bind("<KeyRelease>", self.check_typing)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        tk.Button(self.root, text="New Test", command=self.new_test,
                  font=("Arial", 12), bg="#4CAF50", fg="white").pack()

    def new_test(self):
        self.target     = random.choice(TEXTS)
        self.start_time = None
        self.sample_label.config(text=self.target)
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="Start typing to begin the timer...")
        self.text_entry.focus()

    # --------------------------------------------------
    #  TODO 1: check_typing(event)
    # --------------------------------------------------
    # On first keypress: record start_time = time.time()
    # Get typed = self.text_entry.get("1.0", "end-1c")
    # Compare typed to self.target char by char:
    #   correct chars → tag green, wrong → tag red
    # If len(typed) >= len(self.target): call show_results()

    def check_typing(self, event):
        typed = self.text_entry.get("1.0", "end-1c")
        if not typed:
            return
        if self.start_time is None:
            self.start_time = time.time()
        # TODO: highlight correct/incorrect characters
        # TODO: check if typing is complete

    # --------------------------------------------------
    #  TODO 2: show_results()
    # --------------------------------------------------
    # elapsed = time.time() - start_time
    # wpm     = (len(target.split()) / elapsed) * 60
    # correct = count matching characters
    # accuracy = correct / len(target) * 100
    # Display in result_label

    def show_results(self):
        pass   # TODO


root = tk.Tk()
app  = TypingTest(root)
root.mainloop()
