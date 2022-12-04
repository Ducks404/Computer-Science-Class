booking = []
for day in range(14):
    spots = []
    for space in range(20):
        spots.append([])
    booking.append(spots)

#print(booking)

def checkspace(day, accessible):
    space = -1
    if accessible == 'n':
        for index in range(5,20)[::-1]:
            if day[index] == []:
                space = index
                break
    elif accessible == 'y':
        for index in range(20):
            if day[index] == []:
                space = index
                break
    return space

# pass to loop back to asking
n=2
while n>0:
    try:
        day = int(input("On what day would you like to book? (1-14) "))
    except:
        print("Invalid day")
    accessible = input("Do you need an accessible spot? (Y/N) ").lower()

    if day >= 1 and day <= 14:
        if (accessible == 'y' or accessible == 'n'):
            day-=1
            space = checkspace(booking[day], accessible)
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
            print("Invalid answer")
    else:
        print("Invalid day")
        
