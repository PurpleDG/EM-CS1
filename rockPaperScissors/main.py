#Evan McCabe ProfiencyTest: Rock, Paper, Scissors

import random

print("\nHello! Ready to play Rock, Paper, Scissors?")

playing = True

cpuOptions = ["r", "p", "s"]

def runGame():
    global playing
    global cpuOptions
    while playing == True:
        move = input("\nWhat's your move? (r = rock, p = paper, s = scissors)\n")
        cpuMove = random.choice(cpuOptions)
        if move == cpuMove:
            playAgain = input("\nI chose the same thing!\n\nTIE\n\nWant to play again? (y for yes, no for no)\n")
            if playAgain == "y":
                runGame()
            else:
                print("\nThanks for playing!\n")
                break
        elif move == "r" and cpuMove == "p":
            playAgain = input("\nI choose paper!\n\nYOU LOSE\n\nWant to play again? (y for yes, n for no)\n")
            if playAgain == "y":
                runGame()
            else:
                print("\nThanks for playing!\n")
                break
        elif move == "r" and cpuMove == "s":
            playAgain = input("\nI choose scissors!\n\nYOU WIN\n\nWant to play again? (y for yes, n for no)\n")
            if playAgain == "y":
                runGame()
            else:
                print("\nThanks for playing!\n")
                break
        elif move == "p" and cpuMove == "r":
            playAgain = input("\nI choose rock!\n\nYOU WIN\n\nWant to play again? (y for yes, n for no)\n")
            if playAgain == "y":
                runGame()
            else:
                print("\nThanks for playing!\n")
                break
        elif move == "p" and cpuMove == "s":
            playAgain = input("\nI choose scissors!\n\nYOU LOSE\n\nWant to play again? (y for yes, n for no)\n")
            if playAgain == "y":
                runGame()
            else:
                print("\nThanks for playing!\n")
                break
        elif move == "s" and cpuMove == "p":
            playAgain = input("\nI choose paper!\n\nYOU WIN\n\nWant to play again? (y for yes, n for no)\n")
            if playAgain == "y":
                runGame()
            else:
                print("\nThanks for playing!\n")
                break
        elif move == "s" and cpuMove == "r":
            playAgain = input("\nI choose rock!\n\nYOU LOSE\n\nWant to play again? (y for yes, n for no)\n")
            if playAgain == "y":
                runGame()
            else:
                print("\nThanks for playing!\n")
                break
        else:
            print("\nInvalid input. Please try again.")
            runGame()        

runGame()