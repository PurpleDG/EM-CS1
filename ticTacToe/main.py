#Evan McCabe ProficiencyTest: Tic-Tac-Toe Game

playing = True

turn = "player"

import random

win = ""

board1 = [" ", " ", " "]
board2 = ["¯", "¯", "¯"]
board3 = ["¯", "¯", "¯"]

print("\nHello, welcome to Tic-Tac-Toe!")

def printBoard():
    print("\n " + board1[0] + " | " + board1[1] + " | " + board1[2] + " ")
    print("¯" + board2[0] + "¯|¯" + board2[1] + "¯|¯" + board2[2] + "¯")
    print("¯" + board3[0] + "¯|¯" + board3[1] + "¯|¯" + board3[2] + "¯")

def checkEnd():
    global playing
    global win
    if board1 == ["O", "O", "O"]:
        win = True
        playing = False
    if board2 == ["O̅", "O̅", "O̅"]:
        win = True
        playing = False
    if board3 == ["O̅", "O̅", "O̅"]:
        win = True
        playing = False
    if board1[0] == "O" and board2[0] == "O̅" and board3[0] == "O̅":
        win = True
        playing = False
    if board1[1] == "O" and board2[1] == "O̅" and board3[1] == "O̅":
        win = True
        playing = False
    if board1[2] == "O" and board2[2] == "O̅" and board3[2] == "O̅":
        win = True
        playing = False
    if board1[0] == "O" and board2[1] == "O̅" and board3[2] == "O̅":
        win = True
        playing = False
    if board1[2] == "O" and board2[1] == "O̅" and board3[0] == "O̅":
        win = True
        playing = False
    if board1 == ["X", "X", "X"]:
        win = False
        playing = False
    if board2 == ["X̅", "X̅", "X̅"]:
        win = False
        playing = False
    if board3 == ["X̅", "X̅", "X̅"]:
        win = False
        playing = False
    if board1[0] == "X" and board2[0] == "X̅" and board3[0] == "X̅":
        win = False
        playing = False
    if board1[1] == "X" and board2[1] == "X̅" and board3[1] == "X̅":
        win = False
        playing = False
    if board1[2] == "X" and board2[2] == "X̅" and board3[2] == "X̅":
        win = False
        playing = False
    if board1[0] == "X" and board2[1] == "X̅" and board3[2] == "X̅":
        win = False
        playing = False
    if board1[2] == "X" and board2[1] == "X̅" and board3[0] == "X̅":
        win = False
        playing = False
    if board1[0] != " " and board1[1] != " " and board1[2] != " " and board2[0] != "¯" and board2[1] != "¯" and board2[2] != "¯" and board3[0] != "¯" and board3[1] != "¯" and board3[2] != "¯":
        win = "Tie"
        playing = False
    
def playerTurn():
    global turn
    choice = input("\n 1 | 2 | 3 \n¯4¯|¯5¯|¯6¯\n¯7¯|¯8¯|¯9¯\nWhere would you like to place a tile?\n")
    if choice == "1" and board1[0] == " ":
        board1[0] = "O"
        printBoard()
        checkEnd()
    elif choice == "2" and board1[1] == " ":
        board1[1] = "O"
        printBoard()
        checkEnd()
    elif choice == "3" and board1[2] == " ":
        board1[2] = "O"
        printBoard()
        checkEnd()
    elif choice == "4" and board2[0] == "¯":
        board2[0] = "O̅"
        printBoard()
        checkEnd()
    elif choice == "5" and board2[1] == "¯":
        board2[1] = "O̅"
        printBoard()
        checkEnd()
    elif choice == "6" and board2[2] == "¯":
        board2[2] = "O̅"
        printBoard()
        checkEnd()
    elif choice == "7" and board3[0] == "¯":
        board3[0] = "O̅"
        printBoard()
        checkEnd()
    elif choice == "8" and board3[1] == "¯":
        board3[1] = "O̅"
        printBoard()
        checkEnd()
    elif choice == "9" and board3[2] == "¯":
        board3[2] = "O̅"
        printBoard()
        checkEnd()
    else:
        print("\nInvalid choice.")
        playerTurn()
    turn = "computer"

def computerTurn():
    global turn
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    comChoice = random.choice(options)
    if board1[0] != " " and board1[1] != " " and board1[2] != " " and board2[0] != "¯" and board2[1] != "¯" and board2[2] != "¯" and board3[0] != "¯" and board3[1] != "¯" and board3[2] != "¯":
        print("")
    else:
        if comChoice == 1 and board1[0] == " ":
            board1[0] = "X"
            printBoard()
            checkEnd()
        elif comChoice == 2 and board1[1] == " ":
            board1[1] = "X"
            printBoard()
            checkEnd()
        elif comChoice == 3 and board1[2] == " ":
            board1[2] = "X"
            printBoard()
            checkEnd()
        elif comChoice == 4 and board2[0] == "¯":
            board2[0] = "X̅"
            printBoard()
            checkEnd()
        elif comChoice == 5 and board2[1] == "¯":
            board2[1] = "X̅"
            printBoard()
            checkEnd()
        elif comChoice == 6 and board2[2] == "¯":
            board2[2] = "X̅"
            printBoard()
            checkEnd()
        elif comChoice == 7 and board3[0] == "¯":
            board3[0] = "X̅"
            printBoard()
            checkEnd()
        elif comChoice == 8 and board3[1] == "¯":
            board3[1] = "X̅"
            printBoard()
            checkEnd()
        elif comChoice == 9 and board3[2] == "¯":
            board3[2] = "X̅"
            printBoard()
            checkEnd()
        else:
            computerTurn()
    turn = "player"

while playing == True:
    while turn == "player":
        playerTurn()
    while turn == "computer":
        computerTurn()

if win == False:
    print("\nGAME OVER\nYou lost. :/\n")
if win == True:
    print("\nGAME OVER\nYou won! XD\n")
if win == "Tie":
    print("\nGAME OVER\nIt's a tie... :O\n")