from main import question
from game_data import question_data
from art import quizbrain


question_bank=[]

for i in question_data:
    que=question(i["text"],i["answer"])
    question_bank.append(que)

ask=quizbrain(question_bank)

flag=True

while flag:
    flag=ask.next_question()
