#Evan McCabe Raidd: Number Guessing Game

# The goal of this project is to generate a number 1-10, have the user guess a number 1-10,
# and check if they match. It needs to choose a number, let the user guess a number, and then
# check if they're correct. If they are, the program should tell them, and ask if they want
# to play again. Otherwise, the program should let them keep trying until they get it. Once
# the user guesses correctly, the program should tell them how many tries it took them.

# (Psuedocode was written, and then converted to actual code.)

import random

#Intro Message:
print("\nHello! Welcome to the Number Guessing Game. \nYour goal is to guess the number 1-10 that I generate.")


#function for running the game:
def runGame():
    #Initialize the user's number of guesses to 0:
    guesses = 0
    #Pick the number for the user to guess:
    numToGuess = random.randint(1, 10)
    #Allow the user to guess the number:
    guess = int(input("\nI picked a number!\nWhat is your guess? "))
    #if the user is right(less likely):
    if guess == numToGuess:
        #Tell the user they've won, how many guesses they took, and ask if they'd like to play again:
        playAgain = input("\nCorrect! You win! XD\nYou guessed in 1 attempt.\nPlay again? (y for yes, n for no)\n")
        #if the user DOES want to play again:
        if playAgain == "y":
            #run the game again:
            runGame()
        #if the user DOES NOT want to play again:
        else:
            print("\nThanks for playing!\n")
            #stop the program:
            exit()
    #if the user is wrong(more likely):
    else:
        #Tell the user they got it wrong:
        print("\nWrong! DX")
        #add 1 to the number of user guesses:
        guesses += 1

        #Keep letting the user guess the number until they get it right:
        def wrong():
            global guesses
            guess = int(input("What is your next guess? "))
            #Check if the user got it right this time:
            #if they DID:
            if guess == numToGuess:
                #Make sure that the number of guesses can be used in a print statement:
                guesses = str(guesses)
                #Tell the user they won, how many guesses they took, and ask if they want to play again:
                playAgain = input("\nCorrect! You win! XD\nYou guessed in " + guesses + " attempts.\nWould you like to play again (y for yes , n for no)\n")
                if playAgain == "y":
                #run the game again:
                  runGame()
                #if the user DOES NOT want to play again:
                else:
                  print("\nThanks for playing!\n")
                  #stop the program:
                  exit()
            #if they DID not guess correctly:
            else:
                #Tell the user they were wrong:
                print("\nWrong!")
                #Add 1 to the number of user guesses:\
                guesses += 1
                #run the function again so the user can keep guessing:
                wrong()
        #run the function to let the user try again:
        wrong()
        
#run the game:
runGame()