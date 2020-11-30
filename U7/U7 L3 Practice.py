dayDiscountFNAC = {"friday":0.75,"saturday":0.70,"sunday":0.50}
dayDiscountWORTEN = {"friday":0.8,"saturday":0.7,"sunday":0.7}

def blackFriday(cost):
    if cost > 100:
        cost = cost * 0.75
    print(f"You're total is: {cost}€")


def blackFriday2():
    day = input("What day is it today? ").lower()
    if not day in dayDiscountFNAC:
        print("Not a valid day!")
        blackFriday2()
    else:
        cost = float(input("Cost of item: "))
        cost = cost * dayDiscountFNAC[day]
        print(f"Your total is: {cost}€")


def blackFriday3():
    day = input("What day is it today? ").lower()
    cost = float(input("Cost: "))
    if cost < 200:
        cost = cost * 0.95
    elif day in dayDiscountWORTEN:
        print("Discount day!")
        cost = cost * dayDiscountWORTEN[day]
    cost = round(cost,2)
    print(f"Your total is: {cost}€")


def blackFriday4():
    totalPrice = 0
    comps = int(input("How many computers do you want to buy? "))
    for i in range(comps):
        cost = float(input(f"#{i} || What is the price of the computer you want to buy? "))
        cost = cost * 0.7
        totalPrice += cost
    totalPrice = round(totalPrice,2)
    print(f"Your total is: {totalPrice}")


def blackFriday5():
    totalProfit = 0
    prodDict = {}
    productNo = int(input("How many types of products were sold? "))
    for i in range(productNo):
        productName = input(f"#{i} || Product name: ")
        productCost = float(input(f"#{i} || Product cost: "))
        productSales = int(input(f"#{i} || Number of units sold: "))
        profit = productCost * productSales
        totalProfit += profit 
        prodDict.update({productName:profit})
    print(f"Sold: {productNo} types of products, and earned {totalProfit}€ total. Dict:")
    print(prodDict)


def blackFriday6():
    totalCost = 0
    productsBought = int(input("How many products did you buy? "))
    for i in range(productsBought):
        prodType = int(input(f" #{i} || Which did you buy? 1. (Lenovo ideapad 330-15ICH 15,6') 2. (Apple iPad 10,2'' 128GB) 3. (LED 32'' Xiaomi Mi TV 4S 32 HD Smart TV)" ))
        if prodType == 1:
            totalCost += 800
            print("+800€ \n")
        elif prodType == 2:
            totalCost += 450
            print("+450€ \n")
        else:
            totalCost += 170
            print("+170€ \n")
    print(f"Total cost: {totalCost}€")

while True:
    #blackFriday(float(input("Cost of item: ")))
    #blackFriday2()
    #blackFriday3()
    #blackFriday4()
    #blackFriday5()
    blackFriday6()