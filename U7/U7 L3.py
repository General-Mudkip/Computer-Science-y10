def multipleChoice():
    try:
        print("What language are Operating Systems most commonly made in? 1. Java 2. C 3. Python")
        answer = int(input(""))
        if answer == 2:
            print("Correct!")
        else:
            print("Incorrect!")
    except:
        print("Invalid input!")
        multipleChoice()


def parcelCost():
    try:
        print("\nHow heavy is your parsel?")
        weight = int(input(""))
        if weight > 2:
            print("This is not a small parcel!")
        elif weight > 1:
            print("This package will cost $6.55. Hit enter to continue.")
        else:
            print("This package will cost $4.40. Hit enter to continue.")
        weight = input("")
    except:
        print("Invalid input! \n")
        parcelCost()


def RockPaperScissors():
    p1_input = 0
    p2_input = 0
    valid_moves = {"rock","paper","scissors"}
    while not p1_input in valid_moves:
        p1_input = input("Player 1's Move: rock, paper, scissors \n")
        if not p1_input in valid_moves:
            print("Invalid input!")
    while not p2_input in valid_moves:
        p2_input = input("Player 2's Move: rock, paper, scissors \n")
        if not p2_input in valid_moves:
            print("Invalid input!")
    if p1_input == "rock":
        if p2_input == "rock":
            print("Tie!")
        if p2_input == "paper":
            print("Player 2 Wins!")
        else:
            print("Player 1 Wins!")
    elif p1_input == "paper":
        if p2_input == "rock":
            print("Player 1 Wins!")
        elif p2_input == "paper":
            print("Tie!")
        else:
            print("Player 2 Wins!")
    else:
        if p2_input == "rock":
            print("Player 2 Wins!")
        elif p2_input == "paper":
            print("Player 1 Wins!")
        else:
            print("Tie!")


#multipleChoice()
#parcelCost()
RockPaperScissors()