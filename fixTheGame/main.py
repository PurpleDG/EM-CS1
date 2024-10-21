#Evan McCabe Raid: Fix The Game

import random
def start_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        #In the line below, guess was a string instead of an integer, so it couldn't work with < or > later in the code. This is a runtime error.
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            #This if statement previously allowed the following if statement to run, even though the user had lost, therefore printing a "too low" or "too high" message. This is a logic error.
            break
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            #This elif statement previously lacked a line of code to increase the number of attempts the user has used, allowing the user to have infinite guesses. This is a logic error.
            attempts += 1
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            #This elif statement previously lacked a line of code to increase the number of attempts the user has used, allowing the user to have infinite guesses. This is a logic error.
            attempts += 1
        continue
    print("Game Over. Thanks for playing!\n")
start_game()
