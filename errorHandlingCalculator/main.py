#Evan McCabe SkillPractice: Error Handling Calculator

print("\nHello! I am a simple calculator.")

def askNum():
    try:
        num1 = int(input("\nWhat is the first number in the equation?\n"))
    except:
        print("\nINVALID INPUT")
        askNum()

def askNum2():
    try:
        num2 = int(input("\nWhat is the second number in the equation?\n"))
    except:
        print("\nINVALID INPUT")
        askNum2()

def calculate():
    operation = input("What operation would you like to perform?\n(1 - addition)\n(2 - subtraction)\n(3 - multiplication)\n(4 - division)\n")
    valid = False

    if operation == "1":
        valid = True
    elif operation == "2":
        valid = True
    elif operation == "3":
        valid = True
    elif operation == "4":
        valid = True
    else:
        print("\nINVALID INPUT\n")
        calculate()

    if valid == True:
        askNum()
        askNum2()

    if operation == "1":
        print("\n" + num1 + " + " + num2 + " = ")

calculate()
    