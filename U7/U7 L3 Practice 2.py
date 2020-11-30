def ex1():
    cost = 3.2 + 5.3
    print(f"You'll have to bring {cost}€")


def ex2():
    pocketMoney = float(input("How much money do you get every month? "))
    iceCost = float(input("How much will the ice cream cost? "))
    for i in range(4):
        i = i
        pocketMoney -= iceCost
    if pocketMoney < 0:
        print(f"You don't have enough! You'll have {pocketMoney}€ by the end.")
    else:
        print(f"You've got enough, with {pocketMoney}€ to spare.")


def ex3():
    friends = int(input("How many friends will come? "))+1
    total = 0
    for i in range(1,friends):
        cost = float(input(f"How much did friend {i}'s ice cream cost? ")) 
        total += cost
    print(f"It will cost {total}€ in total.")


ex3()