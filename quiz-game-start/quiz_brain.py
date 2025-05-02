class QuizeBrain:
    def __init__(self,q_list):
        self.score=0
        self.question_number=0
        self.question_list=q_list
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        answer=input(f"\nQ.{self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(answer,current_question.answer)

    def check_answer(self,user_answer,curr_question_answer):
        if user_answer == curr_question_answer:
            self.score+=1
            print("You are right.")
            print(f"Your Score : {self.score}/{self.question_number}.")
        else:
            print("You are wrong.")
            print(f"Your Score : {self.score}/{self.question_number}.")





