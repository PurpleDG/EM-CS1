#Evan McCabe SkillPractice: Palandrom

print("\nHello! I am the palindrome checker. I will tell you if a given word is a palindrome(If it is the same forwards and backwards).\n")
input = input("Input the word you want checked: ")
input = input.replace(" ","")

if input == input[::-1]:
    print("That is a palindrome.")
else:
    print("That is not a palindrome.")