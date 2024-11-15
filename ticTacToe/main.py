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
    print(" " + board1[0] + " | " + board1[1] + " | " + board1[2] + "¯")
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
    
def playerTurn():
    choice = input("\nWhere would you like to place a tile")

while playing == True:
    while turn == "player":
        playerTurn()