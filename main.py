from questions import questions
from storage import score
print("The Quiz is Starting ")
for question, answer in questions.items():
    print("Length of questions", len(questions))
    user_answer = input(question + "")
    if user_answer.lower() == answer.lower():
        print("Correct")
        score += 1
        print(score)
    else:
        gameover = True
        print("Wrong the correct answer is", answer)
    if score >= len(questions):
        print("You are a Genius Congratz")
