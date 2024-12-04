#Evan McCabe SkillPractice: Counr up and down

def countDown():
    a = 19
    for i in range(19):
        print(a)
        a -= 1

for i in range(20):
    print(i + 1)
    i -= 1
    if i == 18:
        countDown()
        break