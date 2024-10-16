#Evan McCave ProficiencyTest: What are these numbers?

print("\nHello, I am the number formatter.")

def formatNum():
    txt0 = "{:,}"
    num = input("What number would you like formatted? ")
    print("\nHere it is, formatted:")
    print(txt0.format(num))
    


formatNum()