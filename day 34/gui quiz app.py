# ============================================================
#  DAY 34 — API Practice + GUI
#  PROJECT: Trivia Quiz App (Open Trivia DB + Tkinter)
# ============================================================
#
#  SKILLS TODAY:
#    - Fetching data from a real API (no key needed)
#    - Passing API parameters: amount, type, category
#    - Combining OOP (QuizBrain from Day 17) with a GUI
#    - html.unescape()   → fix HTML entities in API responses (&amp; → &)
#    - Updating Tkinter widgets with .config()
#
#  API: https://opentdb.com/api.php?amount=10&type=boolean
#
# ============================================================

import requests
import html
import tkinter as tk

THEME_COLOR = "#375362"


# --------------------------------------------------
#  TODO 1: Fetch questions from the API
# --------------------------------------------------
# GET https://opentdb.com/api.php with params:
#   amount=10, type="boolean" (True/False questions)
# Parse response.json()["results"]
# Each result has: "question", "correct_answer", "category", "difficulty"

def fetch_questions():
    params = {"amount": 10, "type": "boolean"}
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    return response.json()["results"]


question_data = fetch_questions()


# --------------------------------------------------
#  TODO 2: Question and QuizBrain classes
# --------------------------------------------------
# Reuse / adapt from Day 17
# Question(text, answer)  → just stores text and answer
# QuizBrain(question_list):
#   still_has_questions() → bool
#   next_question()       → updates the GUI (call from QuizInterface)
#   check_answer(answer)  → returns True/False, updates score

class Question:
    def __init__(self, q_text, q_answer):
        self.text   = q_text
        self.answer = q_answer


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score           = 0
        self.question_list   = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number  += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        correct = self.current_question.answer
        if user_answer.lower() == correct.lower():
            self.score += 1
            return True
        return False


question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]
quiz = QuizBrain(question_bank)


# --------------------------------------------------
#  TODO 3: QuizInterface class (Tkinter UI)
# --------------------------------------------------
# __init__(quiz_brain):
#   self.quiz = quiz_brain
#   Build the window: dark background, score label, question canvas,
#   True button (green), False button (red)
#   Call get_next_question()
#
# get_next_question():
#   If quiz.still_has_questions():
#     Update canvas text with quiz.next_question()
#   Else:
#     Show "You've reached the end! Score: X/10"
#
# true_pressed() / false_pressed():
#   Check the answer, flash the canvas green (correct) or red (wrong)
#   Use window.after(1000, get_next_question) to pause before moving on
#
# give_feedback(is_right):
#   canvas.config(bg="green") if right, else red
#   window.after(1000, ...) to reset to white and load next question

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Question", font=("Arial", 20, "italic"),
            fill=THEME_COLOR, width=280, anchor="center"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button  = tk.Button(text="True",  bg="green", fg="white", command=self.true_pressed)
        false_button = tk.Button(text="False", bg="red",   fg="white", command=self.false_pressed)
        true_button.grid(row=2, column=0)
        false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've finished!\nScore: {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        color = "green" if is_right else "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)


quiz_ui = QuizInterface(quiz)
