#Evan McCabe Fibonacci Sequence Generator

print("\nI am Fibonacci Sequence Generator. I can make a Fibonacci Sequence from two starting numbers.")
startingNum1 = int(input("\nWhat should the first number be? "))
startingNum2 = int(input("What would you like the second number to be? "))
length = int(input("How many numbers would you like in the sequence? "))
a = 0

while a < length:
    print(startingNum1)
    startingNum1 = startingNum1+startingNum2
    a += 1
    if a == length:
        break
    else:
     print(startingNum2)
     startingNum2 = startingNum1+startingNum2
     a +=1