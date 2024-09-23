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

numberOfLetters = numberOfLetters + 1
for x in range(numberOfLetters):
    whichLetter = random.randint(0,numberOfLetters)
    anagram.append(letters[whichLetter])
    letters.remove(letters[whichLetter])
"".join(anagram)