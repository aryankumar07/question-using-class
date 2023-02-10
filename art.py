class quizbrain:

    def __init__(self,q_list):
        self.question_num=0
        self.question_list=q_list
        self.currrent_score=0
        self.d=len(self.question_list)

    def next_question(self):
        if(self.d>self.question_num):
            asked=self.question_list[self.question_num]
            ans=input(f"q.{self.question_num} {asked.text} : (True/False) ")
            if(ans==asked.answer):
                flag=True
                self.currrent_score += 1
                self.question_num += 1
                print("you got it right ")
                print("thre correct answer was : true")
                print(f"your current score is :{self.currrent_score}/{self.question_num}\n \n \n \n")
                return flag
            else:
                flag=False
                return flag
        else:
            flag=False
            print("ran out of questions")
            return flag
            
