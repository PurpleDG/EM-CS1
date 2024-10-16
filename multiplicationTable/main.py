#Evan McCabe ProficiencyTest: Multiplication Table

num = int(input("\nHello, user! I am the Multiplication Table bot. I can find the multiples of a number 1-12.\nWhat number would you like the multiples of? "))
print("\n")

a = 1

def findMultiples():
    global a
    global num
    for i in range(12):
        if num % a == 0:
            print(a, ' | ', num // a)
        a +=1
    print("\nThere you go!\n")

findMultiples()