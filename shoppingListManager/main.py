#Evan McCabe ProficiencyTest: Shopping list manager

shoppingList = []

while True:
    action = input("""\nWhat would you like to do?\nEnter 1 to add item\nEnter 2 to remove item\nEnter 3 to print the list\nEnter 4 to leave the list\n""")
    if action =="1":
        add = input("What would you like to add to the list?\n")
        shoppingList.append(add)
    elif action =="2":
        remove = input("What would you like to remove from the list?\n")
        shoppingList.remove(remove)
    elif action =="3":
        print(shoppingList)
    else:
        print("\nHave a nice day!\n")
        break
    