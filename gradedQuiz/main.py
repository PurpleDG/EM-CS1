#Evan McCabe ProfiencyTest: Graded Quiz

score = 0
print("\nThis is a true/false quiz about ROCKS. Try to get 100%!\n")

answer = input("Scientists do not currently know how geodes are formed. (t for true, f for false)\n")
if answer == "f":
    score += 1

answer = input("\nThere are 3 main catgories of rock that every rock can be sorted into.\n")
if answer == "t":
    score += 1

answer = input("\nThousands of meteorites hit Earth every year.\n")
if answer == "t":
    score += 1

answer = input("\nThe larges asteroid thought to hit Earth was over 100km in diameter.\n")
if answer == "f":
    score += 1

answer = input("\nRock collecting is a popular hobby.\n")
if answer == "t":
    score += 1

score = str(score)

print("\nYou got " + score + " out of 5 questions correct.\n")