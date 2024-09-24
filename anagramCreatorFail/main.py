#Evan McCabe Raid: Anagram Creator

import random

lettersInName = int(input("\nHello! I am the Anagram Generator. I can give you anagrams from your name(though they may not be the greatest).\n\nHow many letters are in your name? "))
numberOfLetters = lettersInName

letters = []
anagram = []

nextLetter = input("\nWhat is the first letter of your name? ")
letters.append(nextLetter)

numberOfLetters = numberOfLetters - 1
for x in range(numberOfLetters):
    nextLetter = input("\nWhat is the next letter of your name? ")
    letters.append(nextLetter)

currentLetters = letters
print("\n")

def generateAnagram():
    global letters
    global currentLetters
    global numberOfLetters
    for x in range(numberOfLetters + 1):
        whichLetter = random.randint(0,numberOfLetters)
        anagram.append(currentLetters[whichLetter])
        currentLetters.remove(currentLetters[whichLetter])
        numberOfLetters -= 1

for x in range (5):
    currentLetters = letters
    numberOfLetters = lettersInName - 1
    anagram = []
    generateAnagram()
    print(anagram)

print("\n")