
#Evan McCabe Raid: What's in a name?

print("\nHello! My name is Namey(It's a long story). I can calculate the area of a rectangle and a rectangular prism for you, if you like. (:")

rectangleLength = int(input("\nPlease input the length of your rectangle: "))
rectangleWidth = int(input("Nice! Please input the width of your rectangle: "))

rectangularPrismLength = int(input("\nGreat job! Now, if you would, the length of your rectangular prism: "))
rectangularPrismWidth = int(input("Thanks! The width of the rectangular prism?: "))
rectangularPrismHeight = int(input("Almost done! B)\nFinally, what's the height of the prism?: "))

def rectangleCalculation(x, y):
    z = x * y
    return z

def cubeCalculation(a, b, c):
    rectangle = rectangleCalculation(a, b)
    result = rectangle * c
    return result

rectangle = rectangleCalculation(rectangleLength, rectangleWidth)
print(f"\nThe rectangle's area is: {rectangle}.\n")

rectangularPrism = cubeCalculation(rectangularPrismLength, rectangularPrismWidth, rectangularPrismHeight)
print(f"The rectangular prism's area is: {rectangularPrism}.\n")

print("I hope I helped, have good day! XD\n")