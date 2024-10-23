#Evan McCabe ProfiencyTest: Rock, Paper, Scissors

import random

print("\nHello! Ready to play Rock, Paper, Scissors?\n")

playing = True

cpuOptions = ["r", "p", "s"]

def runGame():
    global playing
    global cpuOptions
    while playing == True:
        move = input("What's your move? (r = rock, p = paper, s = scissors)\n")
        cpuMove = random.choice(cpuOptions)
        if move == cpuMove:
            playAgain = input("\nTIE\n\nWant to play again? (y for yes, no for no)\n")
        else:
            print("\nInvalid input. Please try again.\n")
            runGame()        


runGame()