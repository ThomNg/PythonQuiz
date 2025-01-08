class Quiz:
    def __init__(self, qlist):
        self.number = 0
        self.score = 0
        self.qlist = qlist

    def has_question(self):
        return self.number < len(self.qlist)

    def next_question(self):
        current_q = self.qlist[self.number]
        self.number +=1
        user_answer = input(f"Q.{self.number}: {current_q.text} (der/die/das): ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user, answer):
        if user.lower() == answer.lower():
            print("Good job")
            self.score +=1
        else:
            print("Wrong answer")
            print(f"the correct answer was {answer}")

        print(f"Score: {self.score} from {self.number}\n")
