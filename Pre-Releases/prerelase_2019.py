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

while menu:
    menuPrint()
    choice = input("What option would you like to choose?\n")
    if choice not in ["1","2","3"]:
        print("\n INVALID CHOICE! \n")
    else:
        if choice == "1":
           pass 

        if choice == "2":
            dayName = input("Please input a day:\n")
            if dayName not in array_of_array_names:
                print("Invalid day! Select from: ", array_of_array_names)
            else:
                lateCount = 0
                busIndexes = []
                count = 0
                for i in array_of_arrays[array_of_array_names.index(dayName)]:
                    if not abs(i) == i:
                        lateCount += 1
                        busIndexes.append(bus_names[count])
                    count += 1
                print(f"On {dayName}, {lateCount} busses were late. This includes: {busIndexes}")