#Evan McCabe ProficinecyTest: Authorized

import time
print("\nServer booting...")
time.sleep(2)
print("\nSign in to\n-ChimknNuggs-\n")
user = input("Username: ")
admins = ["Vincent", "Pedro", "Dean"]
users = ["Sam", "Xavier", "Alec","Addison", "Eve", "Cadence", "Josephine", "Red"]
if user in admins:
    print("\n- AUTHORIZED -\n\nWelcome, " + user + "(admin)!\n")
elif user in users:
    print("\n- AUTHORIZED -\n\nWelcome, " + user + "(user)!\n")
else:
    print("\n- UNAUTHORIZED -\n")