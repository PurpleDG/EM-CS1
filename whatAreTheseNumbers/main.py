#Evan McCave ProficiencyTest: What are these numbers?

print("\nHello, I am the number formatter.")

def formatNum():
    num = int(input("What number would you like formatted? "))
    print("Here it is, formatted:\n")
    f1 = f"{num:,}"
    print(f1)
    f2 = f"{num:.4f}"
    print(f2)
    f3 = f"{num:.0%}"
    print(f3)
    f4 = f"{num:.2f}"
    print("$" + f4 + "\n")

formatNum()