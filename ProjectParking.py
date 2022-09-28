booking = []
for day in range(14):
    spots = []
    for space in range(20):
        spots.append([])
    booking.append(spots)

#print(booking)

def checkspace(day):
    space = -1
    for index, i in enumerate(day):
        if i == []:
            space = index
    return space

# pass to loop back to asking
n=2
while n>0:
    day = int(input("On what day would you like to book? (1-14) "))

    if day >= 1 and day <= 14:
        day-=1
        space = checkspace(booking[day])
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
        