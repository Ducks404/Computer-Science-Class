booking = []
for day in range(14):
    spots = []
    for space in range(20):
        spots.append([])
    booking.append(spots)

#print(booking)

def checkspace(day):
    space = -1
    for index in range(len(day)):
        if day[index] == []:
            space = index
            break
    return space

# pass to loop back to asking
while True:
    try:
        day = input("On what day would you like to book? (1-14) ")
        day = int(day)
    except:
        if day == 'exit':
            break
        else:
            day = -1

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
    else:
        print("Invalid day")
        