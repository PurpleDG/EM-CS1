#Evan McCabe SkillPractice: Counr up and down

def countDown():
    a = 20
    for i in range(20):
        print(a)
        a -= 1

for i in range(20):
    print(i)
    i -= 1
    if i == 18:
        countDown()
        break