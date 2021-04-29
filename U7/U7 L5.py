months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
annualRainfallDict = {
                        1:{"l":31,"rd":[],"average":0, "name":"January"}, 
                        2:{"l":28,"rd":[],"average":0, "name":"February"}, 
                        3:{"l":31,"rd":[],"average":0, "name":"March"}, 
                        4:{"l":30,"rd":[],"average":0, "name":"April"}, 
                        5:{"l":31,"rd":[],"average":0, "name":"May"}, 
                        6:{"l":30,"rd":[],"average":0, "name":"June"}, 
                        7:{"l":31,"rd":[],"average":0, "name":"July"}, 
                        8:{"l":31,"rd":[],"average":0}, "name":"August", 
                        9:{"l":30,"rd":[],"average":0, "name":"September"}, 
                        10:{"l":31,"rd":[],"average":0, "name":"October"}, 
                        11:{"l":30,"rd":[],"average":0, "name":"November"}, 
                        12:{"l":31,"rd":[],"average":0, "name":"December"}
                    }
totalRainfall = 0


for i in range(1,13):
    mName = annualRainfallDict[i].get("name")
    print(f"Now entering rainfall data for {mName}")
    monthlySum = 0
    for day in range(1,annualRainfallDict[i]["l"]+1):
        rainfallData = ""
        while rainfallData == "":
            try:
                rainfallData = float(input(f"Please enter the rainfall data for day {day}.\n"))
                if rainfallData < 0:
                    print("Number is less than 0!")
                    rainfallData = ""
            except:
                print("Invalid input!")
                rainfallData = ""
        totalRainfall += rainfallData
        monthlySum += rainfallData
        annualRainfallDict[i]["rd"].append(rainfallData)
    annualRainfallDict[i]["average"] = monthlySum / annualRainfallDict[i]["l"]

annualAverage = round((totalRainfall / 365), 2)
monthsAboveAverage = 0

for i in range(1,13):
    month = annualRainfallDict[i]
    if month["average"] > annualAverage:
        monthsAboveAverage += 1

print(f"The annual average was {annualAverage}. There were {monthsAboveAverage} months above this average.")