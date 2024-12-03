#Evan McCabe SkillPractice: Counting Characters

grid = [
['A', 'B', 'C', 'A', 'D'],
['C', 'A', 'B', 'D', 'E'],
['A', 'D', 'C', 'E', 'A'],
['B', 'A', 'C', 'A', 'D'],
['D', 'C', 'B', 'E', 'A'] ]

print(grid)

numOfA = 0
numOfB = 0
numOfC = 0
numOfD = 0
numOfE = 0

for i in grid:
    for a in i:
        if a == "A":
            numOfA += 1
        if a == "B":
            numOfB += 1
        if a == "C":
            numOfC += 1
        if a == "D":
            numOfD += 1
        if a == "E":
            numOfE += 1

print("\nA: " + str(numOfA) + "\nB: " + str(numOfB) + "\nC: " + str(numOfC) + "\nD: " + str(numOfD) + "\nE: " + str(numOfE) + "\n")