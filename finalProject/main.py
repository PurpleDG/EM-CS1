#Evan McCabe Final Project

import random

inventory = {
    "Apple": 20

}
health = 150
attack = 30
defense = 30
visitedRooms = []

cactusManStats = {
    "health": 50,
    "attack": 10,
    "defense": 10
}

enemies = {
    "Cactus Man": cactusManStats
}

understand = enemies["Cactus Man"]["health"]

def playerStats():
    print("\n" + str(health))
    print(attack)
    print(defense)

def combat(enemy):
    playerStats()

    print("\nYou are approached by " + enemy + "!")

    useItem = input("\nWould you like to use an item? (y = yes, n = no)\n")
    if useItem == "y":
            Attack Item:
                Item Used As Attack
            Health Item:
                Item Health Added
    else:
             Basic Attack

        Is Enemy At 0 Health?
            Yes:
                Print Win Message
                Break
             No:
                Enemy Attack
                Is Player at 0 health?
                    Yes:
                        Print Lose Message
                        Play Again?
                            Yes:
                                Game Function Call
                            No:
                                 Exit
                    No:
                        Combat Function Call



def bookRoom():

    print("\nYou enter a small room, fulled to the brim with books. The walls are hidden by bookshelves, and even the floor and ceiling are out of sight.")

    playerStats()

    if "Book Room" not in visitedRooms:
        answer = input("\nA wooden board hangs on the far wall. The words inscribed on it read:\nIf book A has a volume of 2 units, book C is triple the size of book A, and book B is half the size of book C, what is the volume of book B?\n(a = 2, b = 3, c = 4)\n")

        if answer == "b":
            print("\nCORRECT")
            visitedRooms.append("Book Room")
            print("\nA bookshelf opens in front of you. Behind it are two doors, one seemingly made entirely out of paper, and another with absurd amounts of dust pouring out of it.")
        else:
            print("\nINCORRECT")
            bookRoom()
    else:
        print("\nYou've already been to this room.")

    nextRoom = input("\nWhich door would you like to go through? (1 = paper, 2 = dust)")
    if nextroom == "1":
        paperRoom()
    else:
        dustRoom()

Paper Room Function:

    Player Stats Function Call

    Is Rooms NOT in Rooms Visited List?
        Yes:
            Combat Function Call (Origami Construct)
            User Picks up Pen?
                Pen (combat) added to Inventory Dictionary
            User Picks up Scissors?
                Scissors (combat) added to Inventory Dictionary
                 
            Paper Room added to Rooms Visited List

    Which Room To Travel To Next?
        Book Room:
            Book Room Function Call
        Cafeteria:
            Cafeteria Function Call

Cafeteria Function:

    Player Stats Function Call

    Is Rooms NOT in Rooms Visited List?
        Yes:
           User Picks up Rotten Tomato?
               Tomato (combat) added to Inventory Dictionary
           User Picks up Mango?
               Mango (health) added to Inventory Dictionary

            Cafeteria added to Rooms Visited List

    Which Room To Travel To Next?
        Paper Room:
            Paper Room Function Call
        Ghosty Room:
            Ghosty Room Function Call

Ghosty Room Function:

    Player Stats Function Call

    Is Rooms NOT in Rooms Visited List?
        Yes:
            Combat Function Call (ghosty)

            Ghosty Room added to Rooms Visited List

    Which Room To Travel To Next?
        Desert Room:
            Desert Room Function Call
        Cafeteria Room:
            Cafeteria Room Function Call

Dust Room Function:

    Player Stats Function Call

    Is Rooms NOT in Rooms Visited List?
        Yes:
            Combat Function Call (dust bunnies)

            Dust Room added to Rooms Visited List

    Which Room To Travel To Next?
        Garden Room:
            Garden Room Function Call
        Book Room:
            Book Room Function Call
        Desert Room:
            Desert Room Function Call

Space Room Function:

    Player Stats Function Call

    Is Rooms NOT in Rooms Visited List?
        Yes:

            Space Room added to Rooms Visited List

        Which Room To Travel To Next?
            Star King Room:
                Star King Room Function Call
            Submarine Room:
                Submarine Room Function Call

Desert Room Function:

    Player Stats Function Call

    Is Rooms NOT in Rooms Visited List?
        Yes:
            Combat Function Call (cactus man)

            User Picks up Venomous Spines?
                Venomous Spines (combat) added to Inventory Dictionary

            Desert Room added to Rooms Visited List

        Which Room To Travel To Next?
            Submarine Room:
                Submarine Room Function Call
            Ghosty Room:
                Ghosty Room Function Call
            Dust Room:
                Dust Room Function Call

Garden Room Function:

    Player Stats Function Call

    Is Rooms NOT in Rooms Visited List?
        Yes:
            User Picks up Yummy Beet?
                Yummy Beet (health) added to Inventory Dictionary

            User Picks up Deadly Beet?
                Deadly Beet (combat) added to Inventory Dictionary

            User Fight Shouty Beet?
                Combat Function Call (shouty beet)

                Deadbeet added to Inventory Dictionary

            Garden Room added to Rooms Visited List

        Which Room To Travel To Next?
            Desert Room:
                Desert Room Function Call
            Dust Room:
                Dust Room Function Call

Submarine Room Function:

    Player Stats Function Call

    Is Rooms NOT in Rooms Visited List?
        Yes:
            Combat Function Call (sea monster)
 
            User Picks Up Sea Pickle?
                Sea Pickle (health) added to Inventory Dictionary

            User Picks Up Naval Mine?
                Naval Mine (combat)

            Submarine Room added to Rooms Visited List

        Which Room To Travel To Next?
            Garden Room:
                Garden Room Function Call
            Ghosty Room:
                Ghosty Room Function Call
            Space Room:
                Space Room Function Call

Star King Room Function:

    Print Star King Introduction

    Combat Function Call (Star King)

    Print Win Message

    Play Again?
        Yes:
            Game Function Call
        No:
             Break

def runGame():

    print("\nWelcome to THE STAR KING'S LABYRINTH\n\nYou wake up in a strange room, with no recollection of how you got there, or anything about yourself or your life at all. Before you have time to freak out, you hear a booming voice shout to you:\nI AM THE STAR KING!!! Find and defeat me, and I will release you. Catch me if you can...")

    num = random.randint(1, 4)
    if num == 1:
        bookRoom()
    if num == 2:
       paperRoom()
    if num == 3:
        cafeteria()
    if num == 4:
        ghostyRoom()

runGame()