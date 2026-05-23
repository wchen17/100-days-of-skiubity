# ============================================================
#  DAY 17 — OOP: The Quiz Project
#  PROJECT: True/False Quiz Game (multi-file OOP)
# ============================================================
#
#  SKILLS TODAY:
#    - Splitting code across multiple files (modules)
#    - Creating objects from a class defined elsewhere
#    - Class attributes vs instance attributes
#    - Building an object list: [Class(data) for data in dataset]
#    - Type hints (optional but good habit): def method(self) -> bool:
#
#  FILES IN THIS PROJECT:
#    question_model.py  → Question class
#    data.py            → question bank (list of dicts)
#    quiz_brain.py      → QuizBrain class  (THIS FILE)
#    main.py            → entry point
#
# ============================================================

# This is quiz_brain.py
# QuizBrain drives the quiz: tracks score, asks questions, checks answers.

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score           = 0
        self.question_list   = q_list  # list of Question objects

    # --------------------------------------------------
    #  TODO 1: still_has_questions() → bool
    # --------------------------------------------------
    # Return True if question_number < len(question_list)

    def still_has_questions(self):
        pass

    # --------------------------------------------------
    #  TODO 2: next_question()
    # --------------------------------------------------
    # Get the current Question object from question_list
    # Increment question_number
    # Ask: "Q{number}: {question.text} (True/False): "
    # Call check_answer() with the user's input

    def next_question(self):
        pass

    # --------------------------------------------------
    #  TODO 3: check_answer(user_answer, correct_answer)
    # --------------------------------------------------
    # Compare (case-insensitive)
    # If correct → score += 1, print "You got it!"
    # Else       → print "That's wrong."
    # Always print: "The correct answer was: {correct_answer}"
    # Always print: "Your current score is: {score}/{question_number}"

    def check_answer(self, user_answer, correct_answer):
        pass
