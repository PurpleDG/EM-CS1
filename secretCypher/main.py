#Evan McCabe ProfieciencyTest: Secret Cypher

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# i j k l m n o p q r s t u v w x y z a b c d e f g h

uncoded = input("\nI am the Secret Cypher Bot.\nWhat message would you like to be turned into a code? ")
coded = uncoded
coded = coded.lower()

def code():
    global coded
    if "a" in coded:
        coded = coded.replace("a", "I")
    if "b" in coded:
        coded = coded.replace("b", "J")
    if "c" in coded:
        coded = coded.replace("c", "K")
    if "d" in coded:
        coded = coded.replace("d", "L")
    if "e" in coded:
        coded = coded.replace("e", "M")
    if "f" in coded:
        coded = coded.replace("f", "N")
    if "g" in coded:
        coded = coded.replace("g", "O")
    if "h" in coded:
        coded = coded.replace("h", "P")
    if "i" in coded:
        coded = coded.replace("i", "Q")
    if "j" in coded:
        coded = coded.replace("j", "R")
    if "k" in coded:
        coded = coded.replace("k", "S")
    if "l" in coded:
        coded = coded.replace("l", "T")
    if "m" in coded:
        coded = coded.replace("m", "U")
    if "n" in coded:
        coded = coded.replace("n", "V")
    if "o" in coded:
        coded = coded.replace("o", "W")
    if "p" in coded:
        coded = coded.replace("p", "X")
    if "q" in coded:
        coded = coded.replace("q", "Y")
    if "r" in coded:
        coded = coded.replace("r", "Z")
    if "s" in coded:
        coded = coded.replace("s", "A")
    if "t" in coded:
        coded = coded.replace("t", "B")
    if "u" in coded:
        coded = coded.replace("u", "C")
    if "v" in coded:
        coded = coded.replace("v", "D")
    if "w" in coded:
        coded = coded.replace("w", "E")
    if "x" in coded:
        coded = coded.replace("x", "F")
    if "y" in coded:
        coded = coded.replace("y", "G")
    if "z" in coded:
        coded = coded.replace("z", "H")
    coded = coded.lower()

code()
print("\nYour message: " + uncoded + "\n\nCoded message: " + coded + "\n")