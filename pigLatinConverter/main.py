#Evan McCabe SkillPractice: Pig Latin Converter

print("\nHello, I am the pig latin converter!")

vowels = ["a", "e", "i", "o", "u", "y"]

def convert():
    word = list(input("\nWhat word would you like me to convert?\n"))
    if word[0] in vowels:
        word.append("yay")
    else:
        while word[0] not in vowels:
            word.append(word[0])
            word.pop(0)
        word.append("ay")
    finalWord = "".join(word)
    finalWord = finalWord.lower()
    print("")
    print(finalWord)
    print("")

    playAgain = input("Would you like me to translate another word? (y for yes, n for no)\n")
    if playAgain == "y":
        convert()
    else:
        print("\nThank you, have a good day!\n")

convert()