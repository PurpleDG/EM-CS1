#Evan McCabe Raid: Full Multiplication Table

a = 1
x = 1
y = 2

for i in range(12):
    for i in range(12):
        numLen = len(str(x))
        if numLen == 1:
            print(x, end = "   ")
        if numLen == 2:
            print(x, end = "  ")
        if numLen == 3:
            print(x, end = " ")
        x += a
    x = y
    y = y + 1
    print("")
    a += 1

print("")