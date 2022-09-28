booking = []
for day in range(14):
    spots = []
    for space in range(20):
        spots.append([])
    booking.append(spots)

#print(booking)

def checkspace(day, accesible):
    space = -1
    if accesible == 'n':
        for index in range(6,20)[::-1]:
            if day[index] == []:
                space = index
                break
    elif accesible == 'y':
        for index in range(20):
            if day[index] == []:
                space = index
                break
    return space

# pass to loop back to asking
n=2
while n>0:
    day = int(input("On what day would you like to book? (1-14) "))
    accesible = input("Do you need an accesible spot? (Y/N) ").lower()

    if day >= 1 and day <= 14 and (accesible == 'y' or accesible == 'n'):
        day-=1
        space = checkspace(booking[day], accesible)
        if space == -1:
            print("Sorry, unavailable day")
        else:
            name = input("Please enter name: ")
            license = input("Please enter license: ")
            booking[day][space] = [name, license]
            space += 1
            print(f"Your space is {space}")
            n -= 1
    else:
        print("Invalid day")
        