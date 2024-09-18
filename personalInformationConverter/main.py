#Evan McCabe ProficiencyTest: Personal Information Converter

print("\nHello! I hope you are having a good day. Here is a survey for you!")

userName = input("\nWhat is your name? ")
userAge = input("How old are you? ")
userHeight = input("How tall are you, in meters? ")
userNumber = input("What is your favorite number? ")

convertedUserAge = int(userAge)
convertedUserNumber = int(userNumber)
convertedUserHeight = float(userHeight)

print("\nName: " + userName + "\nAge: " + userAge + " -> " + str(convertedUserAge) + "\nFavorite Number: " + userNumber + " -> " + str(convertedUserNumber) + "\nHeight: " + userHeight + " -> " + str(convertedUserHeight) + "")

print("\nThanks for participating!")