def challengeFx(challenges):
    challengeSelected = 0
    while challengeSelected not in challenges:
        challengeSelected = input(f"What challenge would you like to select? Choose from the following: {challenges}\n")
    if challengeSelected.lower() not in challenges:
        print("Invalid challenge! Choose again.")

    if challengeSelected == "1":
        pass
        # Insert whatever
    elif challengeSelected == "2":
        pass
        # Insert whatever
    else:
        pass
        # Insert whatever
    
    challenges.remove(challengeSelected)
    if len(challenges) == 0:
        print("Game Over!")
    else:
        challengeFx(challenges)

challengeFx(["1","2","3"])