# main.py: run this file to play the quiz

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# --------------------------------------------------
#  TODO: Build the question bank
# --------------------------------------------------
# Loop through question_data
# Create a Question object for each dict: Question(item["text"], item["answer"])
# Append each to question_bank list

question_bank = []
# your list-building loop here

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
