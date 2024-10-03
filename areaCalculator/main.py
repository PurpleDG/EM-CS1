#Evan McCabe Raid: Area Calculator
import math

def squareCalculator(s):
    square = str(s*s)
    print("\nThe area of the square is " + square + ".\n")

def rectangleCalculator(h, w):
    rectangle = str(h*w)
    print("\nThe are of the rectangle is " + rectangle + ".\n")

def triangleCalculator(h, s):
    triangle = str((h*s)/2)
    print("\nThe area of the triangle is " + triangle + ".\n")

def circleCalculator(r):
    circle = str((r**2)*math.pi)
    print("\nThe area of the circle is " + circle + ".\n")

def trapezoidCalculator(a, b, h):
    trapezoid = str(((a+b)/2)*h)
    print("\nThe area of the trapezoid is " + trapezoid + ".\n")

def interface():
    shapeChoice = input("\nHello! I am a simple calculator. I can tell you the area of a 2-demensional object, given certain dimensions.\nWhat shape would you like me to calculate?\n(s = square)\n(r = rectangle)\n(t = triangle)\n(c = circle)\n(tr = trapezoid)\n")
    if shapeChoice == "s":
        s = int(input("\nWhat is the length of 1 side of the square? "))
        squareCalculator(s)
        again = input("\nWould you like to calculate something else now? (y or n) ")
        if again == "y":
            interface()
        else:
            print("\nGoodbye, now!")
    elif shapeChoice == "r":
        h = int(input("\nWhat is the height of the rectangle? "))
        w = int(input("What is the width of the rectangle? "))
        rectangleCalculator(h, w)
        again = input("\nWould you like to calculate something else now? (y or n) ")
        if again == "y":
            interface()
        else:
            print("\nGoodbye, now!")
    elif shapeChoice == "t":
        h = int(input("\nWhat is the height of the triangle? "))
        s = int(input("How long is the base of the triangle? "))
        triangleCalculator(h, s)
        again = input("\nWould you like to calculate something else now? (y or n) ")
        if again == "y":
            interface()
        else:
            print("\nGoodbye, now!")
    elif shapeChoice == "c":
        r = int(input("\nWhat is the radius of the circle? "))
        circleCalculator(r)
        again = input("\nWould you like to calculate something else now? (y or n) ")
        if again == "y":
            interface()
        else:
            print("\nGoodbye, now!")
    elif shapeChoice == "tr":
        a = int(input("\nHow long is the top side of the trapezoid? "))
        b = int(input("How long is the bottom side of the trapezoid? "))
        h = int(input("What is the height of the trapezoid? "))
        trapezoidCalculator(a, b, h)
        again = input("\nWould you like to calculate something else now? (y or n) ")
        if again == "y":
            interface()
        else:
            print("\nGoodbye, now!")

    else:
        print("\nThat is not a valid input, please try again.")
        interface()

interface()