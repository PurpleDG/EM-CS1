#Evan McCabe SkillPractice: Average Grade

print("AVERAGE GRADE CALCULATOR\n")
grade1 = float(input("Please input the grade of your first class: "))
grade2 = float(input("Please input the grade of your second class: "))
grade3 = float(input("Please input the grade of your third class: "))
grade4 = float(input("Please input the grade of your fourth class: "))
grade5 = float(input("Please input the grade of your fifth class: "))
grade6 = float(input("Please input the grade of your sixth class: "))

addedGrades = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6)
gradeAverage = str((addedGrades // 6))

print("Your average grade is " + gradeAverage + ".")