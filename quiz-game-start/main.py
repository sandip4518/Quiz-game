from data import question_data
from question_model import  Question
from quiz_brain import QuizeBrain

Question_bank=[]

for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    Question_bank.append(Question(question_text,question_answer))

ask=QuizeBrain(Question_bank)

while ask.still_has_question():
    ask.next_question()

print("\nYou have completed the quiz😊.")
print(f"Your final score is {ask.score}/{ask.question_number}.")