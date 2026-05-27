# ============================================================
#  DAY 89: Portfolio Project
#  PROJECT: Disappearing Text Writing App
# ============================================================
#
#  CONCEPT: If you stop typing for 5 seconds, all text is erased.
#  Forces you to keep writing without stopping: great for overcoming
#  writer's block and practicing stream-of-consciousness writing.
#
#  SKILLS USED: Tkinter, after(), cancel_after(), Text widget events
#
# ============================================================

import tkinter as tk

class DisappearingTextApp:
    def __init__(self, root):
        self.root        = root
        self.root.title("Keep Writing or Lose It All")
        self.root.config(bg="#1e1e2e")
        self.timer_id    = None
        self.TIMEOUT_MS  = 5000   # 5 seconds

        self.setup_ui()

    def setup_ui(self):
        self.status_label = tk.Label(
            self.root, text="Start typing...", fg="#cdd6f4", bg="#1e1e2e",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=(10, 0))

        self.countdown_label = tk.Label(
            self.root, text="", fg="#f38ba8", bg="#1e1e2e", font=("Arial", 24, "bold")
        )
        self.countdown_label.pack()

        self.text_area = tk.Text(
            self.root, font=("Courier New", 14), wrap=tk.WORD,
            bg="#313244", fg="#cdd6f4", insertbackground="white",
            relief="flat", padx=20, pady=20
        )
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        self.text_area.bind("<Key>", self.on_keypress)

        self.word_count_label = tk.Label(
            self.root, text="Words: 0", fg="#a6e3a1", bg="#1e1e2e", font=("Arial", 11)
        )
        self.word_count_label.pack()

    # --------------------------------------------------
    #  TODO 1: on_keypress(event)
    # --------------------------------------------------
    # Reset the countdown timer on every keypress:
    #   Cancel existing timer if any: self.root.after_cancel(self.timer_id)
    #   Start new timer: self.timer_id = self.root.after(TIMEOUT_MS, self.erase_all)
    # Update word count label
    # Show "5 seconds remaining" warning at 5s, update countdown

    def on_keypress(self, event):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.timer_id = self.root.after(self.TIMEOUT_MS, self.erase_all)
        self.update_word_count()
        # TODO: start a visual countdown

    def update_word_count(self):
        text  = self.text_area.get("1.0", "end-1c")
        words = len(text.split()) if text.strip() else 0
        self.word_count_label.config(text=f"Words: {words}")

    # --------------------------------------------------
    #  TODO 2: erase_all()
    # --------------------------------------------------
    # Delete all text: self.text_area.delete("1.0", tk.END)
    # Show "TOO SLOW! Everything erased." in status label
    # Flash the background red briefly

    def erase_all(self):
        pass   # TODO

    # --------------------------------------------------
    #  TODO 3: countdown(seconds_left)
    # --------------------------------------------------
    # Called once per second when typing has paused
    # Update countdown_label with seconds_left
    # If seconds_left == 0 → call erase_all()
    # Otherwise: self.timer_id = self.root.after(1000, self.countdown, seconds_left - 1)

    def countdown(self, seconds_left):
        pass   # TODO


root = tk.Tk()
root.geometry("800x600")
app = DisappearingTextApp(root)
root.mainloop()
