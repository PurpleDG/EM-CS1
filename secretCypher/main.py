#Evan McCabe ProfieciencyTest: Secret Cypher

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# i j k l m n o p q r s t u v w x y z a b c d e f g h

uncoded = input("\nI am the Secret Cypher Bot.\nWhat message would you like to be turned into a code? ")
coded = uncoded
coded = coded.lower()

def code():
    global coded
    if "a" in coded:
        coded = coded.replace("a", "i")
    if "b" in coded:
        coded = coded.replace("b", "j")
    if "c" in coded:
        coded = coded.replace("c", "k")
    if "d" in coded:
        coded = coded.replace("d", "l")
    if "e" in coded:
        coded = coded.replace("e", "m")
    if "f" in coded:
        coded = coded.replace("f", "n")
    if "g" in coded:
        coded = coded.replace("g", "o")
    if "h" in coded:
        coded = coded.replace("h", "p")
    if "i" in coded:
        coded = coded.replace("i", "q")
    if "j" in coded:
        coded = coded.replace("j", "r")
    if "k" in coded:
        coded = coded.replace("k", "s")
    if "l" in coded:
        coded = coded.replace("l", "t")
    if "m" in coded:
        coded = coded.replace("m", "u")
    if "n" in coded:
        coded = coded.replace("n", "v")
    if "o" in coded:
        coded = coded.replace("o", "w")
    if "p" in coded:
        coded = coded.replace("p", "x")
    if "q" in coded:
        coded = coded.replace("q", "y")
    if "r" in coded:
        coded = coded.replace("r", "z")
    if "s" in coded:
        coded = coded.replace("s", "a")
    if "t" in coded:
        coded = coded.replace("t", "b")
    if "u" in coded:
        coded = coded.replace("u", "c")
    if "v" in coded:
        coded = coded.replace("v", "d")
    if "w" in coded:
        coded = coded.replace("w", "e")
    if "x" in coded:
        coded = coded.replace("x", "f")
    if "y" in coded:
        coded = coded.replace("y", "g")
    if "z" in coded:
        coded = coded.replace("z", "h")

code()
print("\nYour message: " + uncoded + "\n\nCoded message: " + coded + "\n")