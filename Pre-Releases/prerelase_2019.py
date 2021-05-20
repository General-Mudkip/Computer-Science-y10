def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj][0]

def menuPrint():
    print("\n****************************")
    print("!! Bus Menu !!")
    print("Choose an option from below:")
    print("")
    print("1. Enter Data")
    print("2. Check Data")
    print("3. Statistics")
    print("****************************\n")

# Arrays
Mon1 = [0,0,2,1,-1,0]
Tue1 = [0,1,0,0,-1,-5]
Wed1 = [0,0,-1,0,-1,-5]
Thu1 = [2,1,-2,0,-2,-5]
Fri1 = [2,1,-1,0,-4,-4]
Mon2 = [4,2,-2,0,-10,-3]
Tue2 = [0,0,-3,0,-2,-5]
Wed2 = [3,0,-1,0,0,0]
Thu2 = [4,0,0,0,0,0]
Fri2 = [-2,0,0,0,0,0]
Mon3 = [-5,1,-2,2,0,0]
Tue3 = [0,0,0,0,1,-2]
Wed3 = [0,0,1,0,2,-3]
Thu3 = [3,0,1,0,-1,1]
Fri3 = [4,2,1,0,1,1]
Mon4 = [-1,0,1,0,1,1]
Tue4 = [8,0,1,0,3,0]
Wed4 = [1,1,-1,0,-1,0]
Thu4 = [1,0,2,0,0,-2]
Fri4 = [-2,0,-2,0,0,-5]

array_of_arrays = [Mon1,Tue1, Wed1, Thu1, Fri1, Mon2,Tue2, Wed2, Thu2, Fri2, Mon3,Tue3, Wed3, Thu3, Fri3, Mon4,Tue4, Wed4, Thu4, Fri4]
array_of_array_names = ["Mon1","Tue1", "Wed1", "Thu1", "Fri1", "Mon2","Tue2", "Wed2", "Thu2", "Fri2", "Mon3","Tue3", "Wed3", "Thu3", "Fri3", "Mon4","Tue4", "Wed4", "Thu4", "Fri4"]
bus_names = ["Bus A", "Bus B", "Bus C", "Bus D", "Bus E", "Bus F"]

menu = True

def dataEntry():
    print("\nWhich day's data would you like to modify?\n")
    dayName = input("")
    if dayName not in array_of_array_names:
        print(f"Invalid day! Select from: {array_of_array_names}")
    else:
        data = input("Input your data for each of the bus routes.\nThe data should be seperated with commas, for example '1,0,0,2,3'.\n")
        try:
            # Splits string into a list
            data = data.split(",")
            # Checks if the user has entered all 5 bus routes
            if len(data) != 5:
                print("Incorrect amount of data.")
            else:
                array = array_of_arrays[array_of_array_names.index(dayName)]
                for i in range(5):
                    # Changes each value in the array to the float of each data in the data array
                    array[i] = float(data[i])

                print("\nData entry complete! \n")
        except BaseException:
            print("Invalid entry! Please enter the correct values.")

def statistics():
    daysLateArray = [0,0,0,0,0,0]
    for busRoute in bus_names:
        p = input(f"\nOutputting {busRoute}. Press enter to continue.")
        bIndex = bus_names.index(busRoute)
        totalMin = 0
        daysLate = 0
        for i in range(len(array_of_arrays)):
            minutes = array_of_arrays[i][bIndex]
            print(f"{array_of_array_names[i]} - {minutes} Minutes")
            if minutes < 0:
                daysLate += 1
                totalMin += minutes

        daysLateArray[bus_names.index(busRoute)] = daysLate
        avTime = totalMin/20
        print(f"When it was late, {busRoute} arrived, on average, {abs(avTime)} minutes late.")

    print(f"\n{bus_names[daysLateArray.index(max(daysLateArray))]} was the bus route with the most late days; {max(daysLateArray)} days late in total.\n")

while menu:
    menuPrint()
    choice = input("What option would you like to choose?\n")
    if choice not in ["1","2","3"]:
        print("\n INVALID CHOICE! \n")
    else:
        if choice == "1":
           dataEntry() 

        if choice == "2":
            dayName = input("Please input a day:\n")
            if dayName not in array_of_array_names:
                print("Invalid day! Select from: ", array_of_array_names)
            else:
                lateCount = 0
                minutesLate = 0
                busIndexes = []
                count = 0
                print("\n")
                for i in array_of_arrays[array_of_array_names.index(dayName)]:
                    if not abs(i) == i:
                        lateCount += 1
                        minutesLate += array_of_arrays[array_of_array_names.index(dayName)][count]
                        busIndexes.append(bus_names[count])
                        print(f"- {bus_names[count]}: {abs(array_of_arrays[array_of_array_names.index(dayName)][count])} Minutes Late")
                    count += 1
                print(f"\nOn {dayName}, {lateCount} busses were late. This includes: {busIndexes}")
                try:
                    print(f"The busses were, on average, {round(abs(minutesLate/lateCount),2)} minutes late.")
                except ZeroDivisionError:
                    print("No busses were late.")
        
        if choice == "3":
            statistics()

        wait = input("Continue?\n")