#Evan McCabe SkillPractice: What is My Grade

numOfClasses = int(input("\nHello! I can tell you your letter grade in a class from a percentage.\nHow many classes do you have? "))
print("\nGreat! Let's get started.")

classNames = []

classGrades = []

for i in range(numOfClasses):
    className = input("\nWhat is the name of your next class?\n")
    classNames.append(className)
    classGrade = float(input("\nWhat percentage grade do you have in that class?\n"))
    if classGrade >= 94.00:
        classGrade = "A"
    elif classGrade >= 90.00:
        classGrade = "A-"
    elif classGrade >= 87.00:
        classGrade = "B+"
    elif classGrade >= 84.00:
        classGrade = "B"
    elif classGrade >= 80.00:
        classGrade = "B-"
    elif classGrade >= 77.00:
        classGrade = "C+"
    elif classGrade >= 74.00:
        classGrade = "C"
    elif classGrade >= 70.00:
        classGrade = "C-"
    elif classGrade >= 67.00:
        classGrade = "D+"
    elif classGrade >= 64.00:
        classGrade = "D"
    elif classGrade >= 60.00:
        classGrade = "D-"
    else:
        classGrade = "F"
    classGrades.append(classGrade)

print("\nHere are your grades:\n")

for i in range(numOfClasses):
    print(classNames[i] + " · " + classGrades[i])

print("")