from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    text = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz", f"Your final score was: {quiz.score}/{len(question_bank)}", sep="\n")