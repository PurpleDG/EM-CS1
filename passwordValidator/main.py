#Evan McCabe SkillPractice: Password Validator

print("\nCHANGE PASSWORD\n\nYour password must:\n-be at least 8 characters long")
print("-include at least 1 number\n-include at least 1 special character")

secure = False

while secure == False:
    includesSpecial = False
    includesNumber = False
    password = input("\nInput your new password:\n")
    specialCharacters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"]
    for i in specialCharacters:
        if i in password:
            includesSpecial = True
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in numbers:
        if i in password:
            includesNumber = True
    if includesNumber == False:
        print("\nPLEASE INCLUDE A NUMBER\nPlease try again.")
    elif includesSpecial == False:
        print("\nPLEASE INCLUDE A SPECIAL CHARACTER\nPlease try again.")
    elif len(password) < 8:
        print("\nTOO SHORT\nPlease try again.")
    else:
        print("\nPassword set.\n")
        secure = True