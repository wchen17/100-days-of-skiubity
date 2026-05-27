# ============================================================
#  DAY 28: Tkinter + Dynamic Typing
#  PROJECT: Pomodoro Focus Timer
# ============================================================
#
#  SKILLS TODAY:
#    - tk.Canvas             → draw shapes and images
#    - canvas.create_image() → place a photo on canvas
#    - canvas.create_text()  → draw text on canvas
#    - canvas.itemconfig()   → update canvas items dynamically
#    - window.after(ms, func)→ call func after ms milliseconds
#    - Math: convert seconds to mm:ss display
#
#  POMODORO TECHNIQUE:
#    25 min work → 5 min short break → repeat
#    After 4 rounds → 20 min long break
#
# ============================================================

import tkinter as tk
import math

PINK  = "#e2979c"
RED   = "#e7305b"
GREEN = "#9bdeac"
YELLOW= "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN  = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN  = 20

reps   = 0
timer  = None   # will hold the "after" callback reference


# --------------------------------------------------
#  TODO 1: reset_timer()
# --------------------------------------------------
# Cancel the pending after() call:  window.after_cancel(timer)
# Reset canvas timer text to "00:00"
# Reset title label to "Timer"
# Reset check marks label to ""
# Reset reps to 0

def reset_timer():
    pass


# --------------------------------------------------
#  TODO 2: start_timer()
# --------------------------------------------------
# Increment reps
# Calculate work_sec, short_break_sec, long_break_sec
#
# if reps % 8 == 0  → long break
# elif reps % 2 == 0 → short break
# else               → work session
#
# Update the title label colour (GREEN for work, PINK for short, RED for long)
# Call count_down(seconds)

def start_timer():
    global reps
    reps += 1
    # TODO: determine session type and duration


# --------------------------------------------------
#  TODO 3: count_down(count)
# --------------------------------------------------
# count = total seconds remaining
# Display as mm:ss:
#   count_min = math.floor(count / 60)
#   count_sec = count % 60
#   if count_sec < 10: count_sec = f"0{count_sec}"
#
# Update the canvas timer text
#
# If count > 0:
#   global timer = window.after(1000, count_down, count - 1)
# Else:
#   start_timer() again (next session)
#   Add a ✔ check mark for each completed work session

def count_down(count):
    pass


# --------------------------------------------------
#  UI Setup
# --------------------------------------------------
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=1)

# Canvas with tomato image (optional: use a placeholder rectangle if no image)
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = tk.PhotoImage(file="tomato.png")   # uncomment if you have the image
# canvas.create_image(100, 112, image=tomato_img)
canvas.create_rectangle(20, 20, 180, 200, fill=RED, outline="")  # placeholder
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button  = tk.Button(text="Start",  highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button  = tk.Button(text="Reset",  highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = tk.Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()

# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Play a sound when a session ends (use playsound or winsound)
#  2. Show a desktop notification
#  3. Let the user configure work/break durations in the UI
# ============================================================
