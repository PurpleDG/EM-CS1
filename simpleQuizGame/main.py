#Evan McCabe ProficiencyTest: Simple Quiz Game

print("\nVAMPIRE WEEKEND QUIZ <3\n")

correct = False

score = 0

#Question 1
answer = input("Question 1.\nWhen was Vampire Weekend formed?\nA. 2000\nB. 2006\nC. 2015\nD. 1998\n")
if answer.lower() == "a":
    print("\nWRONG\ncorrect answer: B\n")
elif answer.lower() == "b":
    print("\nCORRECT\n")
    correct = True
    score += 1
elif answer.lower() == "c":
    print("\nWRONG\ncorrect answer: B\n")
elif answer.lower() == "d":
    print("\nWRONG\ncorrect answer: B\n")
else:
    print("\nINVALID INPUT\nNext question. :/\n")

#Question 2
if correct == False:
    answer = input("Question 2.\nHow many members of Vampire Weekend are female?\nA. 2\nB. 4\nC. 0\nD. 1\n")
    if answer.lower() == "a":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    elif answer.lower() == "c":
        print("\nCORRECT\n")
        correct = True
        score += 1
    elif answer.lower() == "b":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    elif answer.lower() == "d":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    else:
        print("\nINVALID INPUT\nNext question. :/\n")
else:
    answer = input("Question 2.\nWhat country are the members of Vampire Weekend from?\nA. America\nB. Canada\nC. Finland\nD. Ireland\n")
    if answer.lower() == "b":
        print("\nWRONG\ncorrect answer: A\n")
        correct = False
    elif answer.lower() == "a":
        print("\nCORRECT\n")
        correct = True
        score += 1
    elif answer.lower() == "c":
        print("\nWRONG\ncorrect answer: A\n")
        correct = False
    elif answer.lower() == "d":
        print("\nWRONG\ncorrect answer: A\n")
        correct = False
    else:
        print("\nINVALID INPUT\nNext question. :/\n")

#Question 3
if correct == False:
    answer = input("Question 3.\nWhich of these is NOT a Vampire Weekend album?\nA. Only God Was Above Us\nB. Vampire Weekend\nC. Contra\nD. Aim and Ignite\n")
    if answer.lower() == "a":
        print("\nWRONG\ncorrect answer: D\n")
        correct = False
    elif answer.lower() == "d":
        print("\nCORRECT\n")
        correct = True
        score += 1
    elif answer.lower() == "b":
        print("\nWRONG\ncorrect answer: D\n")
        correct = False
    elif answer.lower() == "c":
        print("\nWRONG\ncorrect answer: D\n")
        correct = False
    else:
        print("\nINVALID INPUT\nNext question. :/\n")
else:
    answer = input("Question 3.\nWhat city is the main singer of Vampire Weekend, Ezra Koenig, from?\nA. Washington D.C.\nB. Provo\nC. New York City\nD. Bronxville\n")
    if answer.lower() == "b":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    elif answer.lower() == "c":
        print("\nCORRECT\n")
        correct = True
        score += 1
    elif answer.lower() == "a":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    elif answer.lower() == "d":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    else:
        print("\nINVALID INPUT\nNext question. :/\n")

#Question 4
if correct == False:
    answer = input("Question 4.\nHas Vampire Weekend ever gone on tour?\nA. No\nB. Yes\n")
    if answer.lower() == "a":
        print("\nWRONG\ncorrect answer: D\n")
        correct = False
    elif answer.lower() == "d":
        print("\nCORRECT\n")
        correct = True
        score += 1
    elif answer.lower() == "b":
        print("\nWRONG\ncorrect answer: D\n")
        correct = False
    elif answer.lower() == "c":
        print("\nWRONG\ncorrect answer: D\n")
        correct = False
    else:
        print("\nINVALID INPUT\nNext question. :/\n")
else:
    answer = input("Question 4.\nWhat city is the main singer of Vampire Weekend, Ezra Koenig, from?\nA. Washington D.C.\nB. Provo\nC. New York City\nD. Bronxville\n")
    if answer.lower() == "b":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    elif answer.lower() == "c":
        print("\nCORRECT\n")
        correct = True
        score += 1
    elif answer.lower() == "a":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    elif answer.lower() == "d":
        print("\nWRONG\ncorrect answer: C\n")
        correct = False
    else:
        print("\nINVALID INPUT\nNext question. :/\n")




print("Congrats, you finished! Your score was " + str(score) + "/5. (:\n")