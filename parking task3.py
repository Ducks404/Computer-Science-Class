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
        for index in range(5,20)[::-1]:
            if day[index] == []:
                space = index
                break
    elif accesible == 'y':
        for index in range(20):
            if day[index] == []:
                space = index
                break
    return space

def AccesibleInputted(booking):
    total = 0 
    day = int(input("what day of the period do you want to see? (1-14) "))
    for spot in booking[day-1][:5]:
        if spot != []:
            total += 1
    print("There were " + str(total) + " accesible space/s used in day " + str(day) + "\n")

def GeneralInputted(booking):
    total = 0 
    day = int(input("what day of the period do you want to see? (1-14) "))
    for spot in booking[day-1][5:]:
        if spot != []:
            total += 1
    print("There were " + str(total) + " general space/s used in day " + str(day) + "\n")

def TotalInputted(booking):
    total = 0 
    day = int(input("what day of the period do you want to see? (1-14) "))
    for spot in booking[day-1]:
        if spot != []:
            total += 1
    print("There were " + str(total) + " space/s used in day " + str(day) + "\n")

def Accesible(booking):
    total = 0 
    for day in booking:
        for spot in day[:5]:
            if spot != []:
                total += 1
    print("There were " + str(total) + " general space/s used in the whole 14 day period\n")
    

def General(booking):
    total = 0
    for day in booking:
        for spot in day[5:]:
            if spot != []:
                total += 1
    print("There were " + str(total) + " general space/s used in the whole 14 day period\n")

def Total(booking):
    total = 0
    for day in booking:
        for spot in day:
            if spot != []:
                total += 1
    print("There were " + str(total) + " space/s used in the whole 14 day period\n")

# pass to loop back to asking
done = False
while not done:
    try:
        day = int(input("On what day would you like to book? (1-14) "))
    except:
        print("Invalid day")
        continue

    if day >= 1 and day <= 14:
        # input 'admin' to check the statistics
        accesible = input("Do you need an accesible spot? (Y/N) ").lower()  
        if (accesible == 'y' or accesible == 'n'):
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
        elif accesible == "admin":
            choice = -1
            while choice != 7:
                print("1. Number of accesible spaces used on inputted day")
                print("2. Number of general spaces used on inputted day")
                print("3. Total number of spaces used on inputted day")
                print("4. Number of accesible spaces used")
                print("5. Number of general spaces used")
                print("6. Total number of spaces used")
                print("7. End the whole program")
                print("8. Exit out of admin page")
                choice = int(input("What do you want to see? ")) 
                if choice == 1:
                    AccesibleInputted(booking)
                elif choice == 2:
                    GeneralInputted(booking)
                elif choice == 3:
                    TotalInputted(booking)
                elif choice == 4:
                    Accesible(booking)
                elif choice == 5:
                    General(booking)
                elif choice == 6:
                    Total(booking)
                elif choice == 7:
                    print("See you next time")
                    done = True
                    break
                elif choice == 8:
                    print("Thank you")
                    break
                else:
                    print("Invalid input")

        else:
            print("Invalid answer")
    else:
        print("Invalid day")
        