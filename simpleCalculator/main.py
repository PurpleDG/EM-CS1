#Evan McCabe ProfiencyTest: Simple Calculator

print("\nI am a simple calculator. I can make simple calculations, given a function and two numbers.")
function =input(("\nWhat function would you like me to perform?\n(a = addition, s = subtraction, m = multiplication, d = division, e = exponents, mo = modulo)\n"))
num1 = float(input("What is the first number in the equation? "))
num2 = float(input("What is the second number in the equation? "))

def calculate():
    if function == "a":
     answer =str(num1 + num2)
     print("\nThe answer is " + answer + ".\n")
    elif function == "s":
       answer =str(num1 - num2)
       print("\nThe answer is " + answer + ".\n")
    elif function == "m":
       answer =str(num1 * num2)
       print("\nThe answer is " + answer + ".\n")
    elif function == "d":
       answer =str(num1 // num2)
       print("\nThe answer is " + answer + ".\n")
    elif function == "e":
       answer =str(num1 ** num2)
       print("\nThe answer is " + answer + ".\n")
    elif function == "mo":
       answer =str(num1 % num2)
       print("\nThe answer is " + answer + ".\n")

calculate()