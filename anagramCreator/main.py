#Evan McCabe Raid: Anagram Creator

import random

userName = list(input("\nHello I am the Anagram Creator. I can generate 5 anagrams from your name(though they may not be the best).\nWhat is your name? ").lower())
userNameCopy = userName

print("\n")
for i in range(5):
    random.shuffle(userNameCopy)
    print(''.join(userNameCopy))
    userNameCopy = userName

print("\nThere you go! (:\n")