import pprint

def conditions():
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    if num1 == num2:
        print("They are equal")
    elif num1 > num2:
        print("Num 1 is bigger")
    elif num2 > num1:
        print("Num 2 is bigger")


def musicChoice():
    music = {"pop":"Ed Sheeran", "rap":"Eminem", "rock":"Kaiser Chefs"}
    while True:
        interest = input(f"What type of music do you like? pop, rap, rock, exit \n")
        if interest == "exit":
            print("Exited")
            break
        if not interest in music:
            print("Invalid choice!")
            continue
        else:
            print("Your recommendation: ", music.get(interest))


def multipleChoiceQuiz():
    score = 0
    print("How do you change a string into an integer? int(), float(), str(), flint()")
    answer = input("")
    if answer == "int()":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print("What's the sign for greater than or equal to? =<, >=, <=, =>")
    answer = input("")
    if answer == ">=":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print("What is the most commonly used language for writing OS? R, Python, C, Java")
    answer = input("")
    if answer == "C":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print("What does CPU stand for? Central Programming Unit, ComPUter, Computer Processing Unit, Central Processing Unit")
    answer = input("")
    if answer == "Central Processing Unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print(f"The quiz is over! Your score: {score}")
    if score == 4:
        print("You're a genius!")
    elif score == 3:
        print("Almost a genius!")
    elif score == 2:
        print("You've got some ways to go!")
    elif score == 1:
        print("Better luck next time!")
    else:
        print("Try harder.")


def newspaper():
    try:
        papers = int(input("How many papers did you deliver each day? "))
        totPapers = papers * 7
        payout = papers * 0.1
        totPayout = payout * 7
        print(f"You delivered {totPapers} total papers, and earned {totPayout}$ this week.")
    except:
        print("Invalid answer!")
        newspaper()


def tournGoals():
    totGoals = 0
    try:
        games = int(input("How many games were played? "))
        for i in range(games):
            newGoals = int(input(f"How many goals were scored in Game {i+1}? "))
            totGoals += newGoals
        average = totGoals / games
        average = round(average,2)
        print(f"There were {games} games, and {totGoals} total goals scored. The average goals scored per game was {average}.")
    except:
        print("Invalid input!")
        tournGoals()

def dictToString(dict):
  return str(dict).replace(', ','\r\n').replace("u'","").replace("'","")[1:-1]


def restBills():
    added = -1
    items = {}
    bill = 0
    while added != 0:
        try:
            nameAdd = input("Item: ")
            added = float(input("New Item Price: "))
            if nameAdd != "0":
                items.update( {nameAdd:added} )
            bill += added
        except:
            print("Invalid Input!")
    print("\n Your Items: \n")
    print(dictToString(items))
    print("Total Cost: ", bill)


def simpleRestBills():
    added = -1
    bill = 0
    while added != 0:
        try:
            added = float(input("New Item Price: "))
            bill += added
        except:
            print("Invalid Input")
    print("Bill: ", bill)


def darts():
    score = 101
    dartCount = 0
    while not score <= 0:
        try:
            negScore = int(input("Number Landed On: "))
            dartCount += 1
            score = score - negScore
            print("Score Until 0: ", score)
        except:
            print("Invalid Input!")
    print("\n Game Over! \n")
    print("Your Score: ", score)
    print("Darts Thrown: ", dartCount)


#musicChoice()
#multipleChoiceQuiz()
#newspaper()
#tournGoals()
#restBills()
#simpleRestBills()
darts()
