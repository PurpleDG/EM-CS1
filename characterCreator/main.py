#Evan McCabe Raid: Character Creator

characterClass = input("\nWelcome to the caharacter creator.\n\nWhat class is your character?\n(r for ranger)\n(f for fighter)\n(w for wizard)\n(s for sigma 🤫🧏)\n(l for rogue)\n")
if characterClass == "r":
    dexterity = 10
    intelligence = 8
    characterClass = "Ranger"
elif characterClass == "f":
    dexterity = 4
    intelligence = 6
    characterClass = "Fighter"
elif characterClass == "w":
    dexterity = 5
    intelligence = 10
    characterClass = "Wizard"
elif characterClass == "s":
    dexterity = 999
    intelligence = 999
    characterClass = "Sigma (🤫🧏)"
elif characterClass == "l":
    dexterity = 10
    intelligence = 0
    characterClass = "Rogue"
else:
    print("\nINVALID INPUT\n")
    exit()

if characterClass == "Ranger" or "Fighter" or "Wizard" or "Sigma (🤫🧏)" or "Rogue":
    characterRace = input("\nThank you.\n\nWhat race is your character?\n(d for dragonborn)\n(e for elf)\n(l for dwarf)\n")
    if characterRace == "d":
            health = 10
            strength = 10
            characterRace = "Dragonborn"
    elif characterRace == "e":
            health = 4
            strength = 8
            characterRace = "Elf"
    elif characterRace == "l":
            health = 100
            strength = 1
            characterRace = "Dwarf"

if characterRace == "Dragonborn" or "Elf" or "Dwarf":
     print("\nThank you.\n\nSo, you are a(n) " + characterRace + " " + characterClass + ". Here are your stats:\n")
     print("Health = " + str(health) + "\nStrength = " + str(strength) + "\nDexterity = " + str(dexterity) + "\nIntelligence = " + str(intelligence) + "\n")
     print("Thank you!\n")