#Evan McCabe Raid: Simple Histogram

numOfNums = int(input("\nI am the simple histogram bot.\nHow many numbers do you want to make a graph of? "))

numList = []

num = int(input("\nWhat is the first number? "))
numList.append(num)

for i in range(numOfNums - 1):
    num = int(input("\nWhat is the mext number? "))
    numList.append(num)

print("\nHere is your graph:\n")

for num in numList:
    for y in range(0, num):
        print("*", end = "")
    print("")

print("")