import random
import math

def totalFinder():
    # Init vars
    total = 0
    count = 0
    while total <= 500:
        count += 1
        # Increase total by the count
        total = total + count
    # Total will therefore be the sum of all previous counts
    print(f"Total: {total} Count: {count}")


def weeklyCost():
    # Get the drink cost
    drinkCost = float(input("Enter Drink Cost:"))
    # Get the meal cost
    mealCost = float(input("Enter Meal Cost:"))
    # Set the cost for a day (1 Meal, 2 Drinks per day)
    totalCost = drinkCost * 2 + mealCost
    # Multiply totalCost by 5 to get the total cost every week.
    totalCost = totalCost * 5
    print(totalCost)


def diceGame1():
    # Just to pause it so that it doesn't repeat itself due to losing on the first round
    # New game message
    print(" \n**********************\n New Game! \n********************** \n ")
    playing = 1
    score = 0
    addScore = 0
    while playing == 1:
        # Generate dice values and print them
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        print(f"Roll 1: {dice1} Roll 2: {dice2} Roll 3: {dice3}")
        # Check if all dice are equal
        if dice1 == dice2 == dice3:
            # Set addScore to the sum of the three dice
            addScore = dice1 + dice2 + dice3
            # Increment score by addScore
            score += addScore
            # Print out stats
            print(f"Triple! +{addScore}. Total Score: {score}")
        # Check if any of the 2 dice match
        elif dice1 == dice2 or dice2 == dice3 or dice1 == dice3:
            # Just checking each individual one
            if dice1 == dice2:
                addScore = dice1 + dice2
            if dice2 == dice3:
                addScore = dice2 + dice3
            if dice1 == dice3:
                addScore = dice3 + dice1
            # Add addScore to score and print out stats
            score += addScore
            print(f"Double! +{addScore} Score. Total Score: {score}")
        # If conditions aren't met (3 or 2 match) the player loses
        else:
            print("Game Over! Score: 0")
            # Stops while loop
            playing = 0
            # Skips rest of iteration
            continue
        pInput = input("Go Again? (Y/N)\n")
        # If they do not go again, then it prints out the score and checks if it is a high score.
        if pInput == "N":
            playing = 0
            # Opens up the high score file
            scoreTxt = open("savedScores.txt", "r+")
            # Sets contents to whatever the file contains
            contents = scoreTxt.read()
            # Checks if score is greater than the contents
            if score > int(contents):
                # Writes new high score to file
                scoreTxt.seek(0)
                scoreTxt.write(str(score))
                scoreTxt.truncate()
                # Sends messages
                print("New high score!")
                contents = score
            # Game over message
            print(f"Game Over! Score: {score} Current High-Score: {contents}")


def diceGame2():
    # New game message
    print(" \n**********************\n New Game! \n********************** \n ")
    score = 0
    while playing == 1:
        # Dice roles
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Roll 1: {dice1} Roll 2: {dice2}")
        # Checks if they match
        if dice1 == dice2:
            # If they do, trigger game over
            print("Game Over! Score: 0")
            # Stops while loop
            playing = 0
            continue
        else:
            # If they don't match, then the score is incremented by the sum of the 2 die
            score += dice1 + dice2
        pInput = input("Go Again? (N) \n")
        if pInput == "N":
            # If player doesn't go again, prints score and stops loop
            print(f"Game Over! Score: {score}")
            playing = 0


def guessingGame():
    # Print new game message
    print(" \n**********************\n New Game! \n********************** \n ")
    # Get random number
    answer = random.randint(1,10)
    guess = 0
    # Repeat while the guess is not correct
    while answer != guess:
        # Ask user for guess
        guess = float(input("Enter your guess:"))
    # Once answer == guess, loop will end and print "Correct".
    print("Correct")

# Finds area of a square/rectangle
def squareArea(length1,length2):
        area = length1 * length2
        return area

# Finds area of a triangle
def triangleArea(length1, length2):
    area = length1 * length2
    area = area / 2
    return area

# Finds area of a circle
def circleArea(radius):
    # Uses math.pi to get digits of pi
    area = math.pi * radius ** 2
    return area

# Returns a list of the user's 2 inputs
# def standardInput(inputs = 2):
#    numList = []
#    for i in range(inputs):
#        in1 = float(input(f"Length {i}: "))
#        numList.append(in1)
#    return numList

# Creates a list of the different modes 
modes = ["rectangle","triangle", "circle", "exit"]

def areaSelect():
    while True:
        aMode = 0
        # Repeats while the user's input is not in the 'modes' list
        while not aMode in modes: 
            aMode = input(f"Choose a mode {modes}: ")
        print(f"Selected {aMode} mode.")
        if aMode == "exit":
            # Exits loop
            print("Exited")
            break
        if aMode == "rectangle":
            print(squareArea(float(input("Length 1: ")),float(input("Length 2: "))))
        elif aMode == "triangle":
            print(triangleArea(float(input("Base: ")),float(input("Height: "))))
        elif aMode == "circle":
            print(circleArea(int(input("Radius: "))))


# areaSelect()
