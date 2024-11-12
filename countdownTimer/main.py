#Evan McCabe Raid: Countdown Timer

import time

seconds = int(input("\nCOUNTDOWN\nHow many seconds? "))

for i in range(seconds):
    print("\n" + str(seconds))
    seconds -= 1
    time.sleep(1)

print("\nDone.\n")