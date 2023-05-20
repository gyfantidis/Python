class QuizBrain:

    def __init__(self, qList):
        self.qNumber = 0
        self.score = 0
        self.qList = qList

    def still_has_question(self):
        return self.qNumber < len(self.qList)

    def next_question(self):
        current_question = self.qList[self.qNumber]
        self.qNumber += 1
        user_answer = input(f"Q.{self.qNumber}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"The current score is: {self.score}/{self.qNumber}")
        print("\n")