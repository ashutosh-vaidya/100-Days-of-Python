from question_model import Question
from data import question_data
from quiz_master import QuizMaster

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

qm = QuizMaster(question_bank)

while qm.still_has_questions():
    qm.next_question()

print("You've completed the quiz")
print(f"Your final score was: {qm.score}/{qm.question_number}")
