from question import Question
from quiz import Quiz
from data import question_data


question = []

for item in question_data:
    text = item["question"]
    ans = item["answer"]
    q = Question(text, ans)
    question.append(q)

quiz = Quiz(question)

while quiz.has_question():
    quiz.next_question()

print("Quiz is completed")
print(f"Chook dee, your score was {quiz.score} from {quiz.number}")
