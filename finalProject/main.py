#Evan McCabe Final Project

import random

origamiConstructStats = {
    "health": 15,
    "attack": 40,
    "defense": 2
}

ghostyStats = {
    "health": 1,
    "attack": 0,
    "defense": 0
}

dustBunniesStats = {
    "health": 15,
    "attack": 35,
    "defense": 5
}

cactusManStats = {
    "health": 20,
    "attack": 45,
    "defense": 5
}

shoutyBeetStats = {
    "health": 11,
    "attack": 35,
    "defense": 0
}

seaMonsterStats = {
    "health": 35,
    "attack": 40,
    "defense": 7
}

starKingStats = {
    "health": 150,
    "attack": 50,
    "defense": 9
}

    #IMPORTANT: All enemies' defense < 10!!!

enemies = {
    "Origami Construct": origamiConstructStats,
    "Ghosty": ghostyStats,
    "Dust Bunnies": dustBunniesStats,
    "Cactus Man": cactusManStats,
    "Shouty Beet": shoutyBeetStats,
    "Sea Monster": seaMonsterStats,
    "Star King": starKingStats
}

attackInventory = {
    
}

healthInventory = {
    
}

health = 150
attack = 30
defense = 30
visitedRooms = []

def runGame():

    attackInventory = {
    
    }

    healthInventory = {
        
    }

    health = 150
    attack = 30
    defense = 30
    visitedRooms = []

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

def playerStats():
    print("\n" + "HP: " + str(health))
    print("Attack: " + str(attack))
    print("Defense: " + str(defense))

def combat(enemy):
    global enemies
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    enemyHealth = enemies[enemy]["health"]
    enemyAttack = enemies[enemy]["attack"]
    enemyDefense = enemies[enemy]["defense"]

    print("\nYou are approached by " + enemy + "!")

    while True:
        useItem = input("\nWould you like to use an item? (y = yes, n = no)\n")
        if useItem == "y":
            itemType = input("\nWould you like to use a healing item, or an attack item? (h = healing, a = attack)\n")
            if itemType == "h":
                print("\nHealing Items:\n")
                a = 1
                for i in healthInventory:
                    print(str(a) + ". " + i)
                    a += 1
                whichItem = input("\nInput the number of the item you would like to use:\n")
                x = int(whichItem)
                itemName = (list(healthInventory)[x - 1])
                itemValue = healthInventory[itemName]
                health += itemValue
                print("You used your " + itemName + ".")
                del healthInventory[itemName]

            else:
                print("\nAttack Items:\n")
                a = 1
                for i in attackInventory:
                    print(str(a) + ". " + i)
                    a += 1
                whichItem = input("\nInput the number of the item you would like to use:\n")
                x = int(whichItem)
                itemName = (list(attackInventory)[x - 1])
                itemValue = attackInventory[itemName]
                damageDealt = itemValue - enemyDefense
                enemyHealth -= damageDealt
                print("You dealt " + str(damageDealt) + " damage to the " + enemy + " using your " + itemName + "! (after applying defense)")
                del attackInventory[itemName]

        else:
            damageDealt = 10 - enemyDefense
            enemyHealth -= damageDealt
            print("\nYou use a basic attack. You deal " + str(damageDealt) + " damage.")

        if enemyHealth <= 0:
            print("\nYou defeated the " + enemy + "!")
            break
        else:
            damageDealt = enemyAttack - defense
            health -= damageDealt
            print("\nThe enemy attacks! You take " + str(damageDealt) + " damage!")
            playerStats()
        if health <= 0:
            print("\nYou were defeated by the " + enemy + "! DX")
            playAgain = input("Would you like to try again? (y = yes, n = no)\n")
            if playAgain == "y":
                runGame()
            else:
                print("\nThanks for playing!\n")
                break
                exit

#DONE
def bookRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

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
    if nextRoom == "1":
        paperRoom()
    else:
        dustRoom()

#DONE
def paperRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    print("\nYou enter a room that seems to have pieces of lined paper for walls. There are masses of paper in various forms all over the room, some crumpled paper balls, some origami figures, etc.")

    playerStats()

    if "Paper Room" not in visitedRooms:
        combat("Origami Construct")
        takeItem = input("\nYou find an unusually large (and unusually sharp) pen. Would you like to pick it up? (y = yes, n = no)\n")
        if takeItem == "y":
            attackInventory.update({"Pen": 20})
            print("\nYou pick up the pen. (combat, 20)")
        else:
            print("\nYou do not pick up the pen.")

        takeItem = input("\nYou find a ginormous pair of scissors. Would you like to pick it up? (y = yes, n = no)\n")
        if takeItem == "y":
            attackInventory.update({"Scissors": 45})
            print("\nYou pick up the pen. (combat, 45)")
                 
        visitedRooms.append("Paper Room")

        print("\n2... doors? are drawn on the wall in front of you. One is a drawing of a book, and one has an apple scribbled over it.")

    else:
        print("\nYou've already been to this room.")

    nextRoom = input("\nWhich door would you like to go through? (1 = book, 2 = cafeteria)")
    if nextRoom == "1":
        bookRoom()
    else:
        cafeteria()

#DONE
def cafeteria():
    global attackInventory
    global healthInventory
    global health
    global defense
    global visitedRooms    

    playerStats()

    print("\nYou enter what appears to be an elementary school cafeteria, full of short, lengthy tables.")

    if "Cafeteria" not in visitedRooms:
        takeItem = input("Upon one table, you find a tomato. It appears to have been rotting there for some time now. Would you like to pick it up? (y = yes, n = no)\n")
        if takeItem == "y":
            attackInventory.update({"Rotten Tomato": 5})
            print("\nYou pick up the rotten tomato. (combat, 5)")
        else:
            print("\nYou do not pick up the rotten tomato.")

        takeItem = input("\nOn another table, you find a mango. Unusual. Would you like to pick it up? (y = yes, n = no)\n")
        if takeItem == "y":
            healthInventory.update({"Mango": 50})
            print("\nYou pick up the mango. (health, 50)")
        else:
            print("\nYou do not pick up the mango.")
            visitedRooms.append("Cafeteria")

        takeItem = input("\nOn yet another table, you find a green, glowing orb. Do you want to eat it? (y = yes, n = no)\n")
        if takeItem == "y":
            print("\nYou shove the green orb in your mouth and swallow. You feel energized.\nDEFENSE + 5")
            defense += 5
        else:
            print("Best not to eat random orbs, anyways.")

        print("\nTwo doors lie ahead of you. One seems to be made entirely out of paper, and another strikes fear into your heart.")

    else:
        print("\nYou've already been to this room.")

    nextRoom = input("\nWhich door would you like to go through? (1 = paper, 2 = ghosty)")
    if nextRoom == "1":
        paperRoom()
    else:
        ghostyRoom()

#DONE
def ghostyRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    print("\nYou enter a room that inexplicably makes you fear for your life. You see figures dragging their feet along the ground... GHOSTS!")

    playerStats()

    if "Ghosty Room" not in visitedRooms:
        combat("Ghosty")

        visitedRooms.append("Ghosty Room")

        takeItem = input("\nYou find a purple orb floating in the air. Do you want to eat it? (y = yes, n = no)\n")
        if takeItem == "y":
            print("\nYou shove the orb in your mouth and swallow. You feel an increased sense of power.\nATTACK + 5")
            attack += 5
        else:
            print("Best not to eat random orbs, anyways.")

        print("\nTwo doorways rise from the ground, almost directly beneath your feet. From one, multiple pounds of sand pour out, and from the other, a smell of food emenates.")

    else:
        print("\nYou've already been to this room.")

    nextRoom = input("\nWhich door would you like to go through? (1 = desert, 2 = cafeteria)")
    if nextRoom == "1":
        desertRoom()
    else:
        cafeteria()

#COMPLETE
def dustRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    playerStats()

    print("\nYou enter a room that is ABSOLUTELY FILLED with dust.")

    if "Dust Room" not in visitedRooms:
        combat("Dust Bunnies")
        visitedRooms.append("Dust Room")
        print("\nAs the dust settles, you see that three doors have been waiting for you. The first smells of beets, the second looks like the door to a library, and the third seems to have been worn down by sand.")
    else:
        print("You've already been to this room.")

    nextRoom = input("\nWhich door would you like to go through? (1 = garden, 2 = book, 3 = desert)")
    if nextRoom == "1":
        gardenRoom()
    elif nextRoom == "2":
        bookRoom()
    else:
        desertRoom()

#DONE
def spaceRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    playerStats()

    print("\nYou... ARE IN SPACE?!! Yes, a glass box somehow filled with air, in space.")

    if "Space Room" not in visitedRooms:
        visitedRooms.append("Space Room")
        print("There are two portals in the glass box. One is intimidating somehow, and you can hear the sound of moving water coming from the other.")
    else:
        print("You've already been to this room.")

    nextRoom = input("\nWhich portal would you like to go through? (1 = Star King, 2 = submarine)")
    if nextRoom == "1":
        starKingRoom()
    else:
        submarineRoom()

#DONE
def desertRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    playerStats()

    print("\nYou enter a room... No you don't. You are transported to a seemingly endless dessert that expands out in all directions for eternity.")

    if "Desert Room" not in visitedRooms:
        combat("Cactus Man")
        visitedRooms.append("Desert Room")
        takeItem = input("\nThe spiky man drops some venomous spines upon his death. Would you like to pick them up? (y = yes, n = no)\n")
        if takeItem == "y":
            print("\nYou pick up the venomous spines. (combat, 30)")
            attackInventory.update({"Venomous Spines": 30})
        else:
            print("\nYou do not pick up the venemous spines.")
        print("\n3 doors emerge from the sand. One looks like the metal door of a submarine, another has a ghostly appearance, and the third is covered in a layer of dust.")
    else:
        print("You've already been to this place.")

    nextRoom = input("\nWhich door would you like to go through? (1 = submarine, 2 = ghosty, 3 = dust)")
    if nextRoom == "1":
        submarineRoom()
    elif nextRoom == "2":
        ghostyRoom()
    else:
        dustRoom()

#DONE
def gardenRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    playerStats()

    print("\nYou enter a greenhouse full of beets. Beets? Yes, beets. Everywhere  you look, there is some kind of garden plot full of healthy-looking beets.")

    if "Garden Room" not in visitedRooms:
        visitedRooms.append("Garden Room")
        takeItem = input("\nYou see one beet that has already been picked, and it looks particularly scrumptious. Will you pick it up? (y = yes, n = no)\n")
        if takeItem == "y":
            print("\nYou pick up the yummy beet. (health, 25)")
            healthInventory.update({"Yummy Beet": 25})
        else:
            print("\nYou do not pick up the yummy beet.")
        takeItem = input("\nYou stumble upon another beet! Shocker. This one, though, looks rather deadly. Will you pick it up? (y = yes, n = no)\n")
        if takeItem == "y":
            print("\nYou pick up the deadly beet. (combat, 25)")
            attackInventory.update({"Deadly Beet": 25})
        else:
            print("\nYou do not pick up the deadly beet.")
        fight = input("\nYou see a weird looking beet stem. Will you uproot it? (y for yes, n for no)\n")
        if fight == "y":
            combat("Shouty Beet")
        else:
            print("\nBest to leave it alone, eh?")
        print("\nOn the opposite side of the greenhouse, you find 2 doors. One is cold and wet, while the other looks like it has been dipped in a vat of pure dust.")
    else:
        print("You've already been to this room.")

    nextRoom = input("\nWhich door would you like to go through? (1 = submarine, 2 = dust)")
    if nextRoom == "1":
        submarineRoom()
    else:
        dustRoom()

#DONE
def submarineRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    playerStats()

    print("\nYou enter an abandoned submarine, filled to your knees with water. There is a window on the wall to your left, through wich you can see fish swimming through the ocean.")

    if "Submarine Room" not in visitedRooms:
        combat("Sea Monster")
        visitedRooms.append("Submarine Room")
        takeItem = input("\nYou find a sea pickle growing on some dirt lying on the floor of the submarine. Will you take it? (y = yes, n = no)\n")
        if takeItem == "y":
            print("\nYou pick up the sea pickle. (health, 10)")
            healthInventory.update({"Sea Pickle": 10})
        else:
            print("\nYou do not pick up the sea pickle.")
        takeItem = input("\nYou see a small naval mine floating in the water. Lucky you didn't run into that! Will you pick it up? (y = yes, n = no)\n")
        if takeItem == "y":
            print("\nYou pick up the naval mine. (combat, 30)")
            attackInventory.update({"Naval Mine": 30})
        else:
            print("\nYou do not pick up the naval mine.")

        print("\n3 steel doorways are installed on the far wall. The first has dirt all over it, the second has sand all over it, and the third has little (waterproof) star stickers all over it.")
    else:
        print("You've already been to this room.")

    nextRoom = input("\nWhich door would you like to go through? (1 = garden, 2 = desert, 3 = space)")
    if nextRoom == "1":
        gardenRoom()
    elif nextRoom == "2":
        desertRoom()
    else:
        spaceRoom()

#DONE
def starKingRoom():
    global attackInventory
    global healthInventory
    global health
    global attack
    global defense
    global visitedRooms

    playerStats()

    print("\nYou've finally made it. You approach... the Star King. He greets you.")
    print('"I must thank you. You made it all the way through my little dollhouse, and defeated all my, well, dolls. Definitely the best performance I have seen. Defeat me, and you can go home."')
    print("\nFINAL BOSS\n--FIGHT--")

    combat("Star King")

    print("\nYou did it.\n\nYou wake up in a cold sweat. It's sunrise, and the first sweet drop of sunlight has just hit your eyes through the window.\nOh. It was just a dream, then? No... No. It wasn't. It was far too real to be a dream. How did it happen? Maybe you'll never know. But it happened.")

    playAgain = ("\n...\n\nPlay again? (y = yes, n = no)\n")
    if playAgain == "y":
        runGame()
    else:
        print("\nThank you for playing! I hope you enjoyed the game!\n")
        exit

runGame()