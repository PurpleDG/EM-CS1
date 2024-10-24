#Evan McCabe SkillPractice: Password Validator

print("\nCHANGE PASSWORD\n\nYour password must:\n-be at least 8 characters long")
print("-include at least 1 number\n-include at least 1 special character")

secure = False

cheese = [""]
s = "please work"
cheese.append(s.find("p"))
print(cheese)

while secure == False:
    password = input("\nInput your new password:\n")
    specialCharacters = [""]
    characterCheck = [""]
    specialCharacters.append(password.find("`"))
    specialCharacters.append(password.find("~"))
    specialCharacters.append(password.find("!"))
    specialCharacters.append(password.find("@"))
    specialCharacters.append(password.find("#"))
    specialCharacters.append(password.find("$"))
    specialCharacters.append(password.find("%"))
    specialCharacters.append(password.find("^"))
    specialCharacters.append(password.find("&"))
    specialCharacters.append(password.find("*"))
    specialCharacters.append(password.find("("))
    specialCharacters.append(password.find(")"))
    specialCharacters.append(password.find("-"))
    specialCharacters.append(password.find("_"))
    specialCharacters.append(password.find("="))
    specialCharacters.append(password.find("+"))
    specialCharacters.append(password.find("["))
    specialCharacters.append(password.find("{"))
    specialCharacters.append(password.find("]"))
    specialCharacters.append(password.find("}"))
    specialCharacters.append(password.find("\\"))
    specialCharacters.append(password.find("|"))
    specialCharacters.append(password.find(";"))
    specialCharacters.append(password.find(":"))
    specialCharacters.append(password.find("'"))
    specialCharacters.append(password.find('"'))
    specialCharacters.append(password.find(","))
    specialCharacters.append(password.find("<"))
    specialCharacters.append(password.find("."))
    specialCharacters.append(password.find(">"))
    specialCharacters.append(password.find("/"))
    specialCharacters.append(password.find("?"))
    specialCharacters.append(password.find("/"))
    if specialCharacters == characterCheck:
        print("\nPLEASE INCLUDE A SPECIAL CHARACTER\nPlease try again.")
    elif len(password) < 8:
        print("\nTOO SHORT\nPlease try again.")
    elif str.isalpha(password):
        print("\nPLEASE INCLUDE A NUMBER\nPlease try again.")