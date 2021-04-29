import time

timeUnits = {"s":1,"m":60,"h":3600,"d":86400,"w":604800}

thingy=input("Enter a time.\n")
thingyList = thingy.split(" ")
print(thingyList)
try:
    timeScale = int(thingyList[0])
    if thingyList[1].lower() not in timeUnits:
        print("Invalid time period! Please chose from s,m,h,d,w")
    else:
        timeInc = timeUnits[thingyList[1].lower()] * timeScale
        timeToRemind = time.time() + timeInc

        thingyList.pop(0)
        thingyList.pop(1)
        if len(thingyList) != 0:
            reason = " ".join(thingyList)
        print("I will remind you about",reason,"in",timeInc,"seconds.")
except:
    print("Invalid time scale!")