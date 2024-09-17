#Evan McCabe SkillPractice: Setting, Resetting, and Resetting

facultyAndStaff = 32
students = 100
guests = students*2
tableSeats = 12

#Changes
students -= 1
guests -= 2
facultyAndStaff -= 3
guests -= 15
facultyAndStaff += 1

#Equation
totalGuests = facultyAndStaff + students + guests
tablesNeeded = totalGuests // tableSeats
tablesNeeded = str(tablesNeeded)

print("\n" + tablesNeeded + " tables will be needed.\n")