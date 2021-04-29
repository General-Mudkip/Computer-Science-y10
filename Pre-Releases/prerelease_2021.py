def candidatesPrint(candidate_dict):
    for i in candidate_dict:
        if i != "total":
            print(f" - {i}")

def tutorEntry():
    global student_total, candidate_dictionary, candidates_total

    group_name = 0
    while group_name == 0:
        group_name = input("What is the name of your tutor group?\n")
        try:
            group_name = group_name.split(" ")
            if len(group_name) != 2:
                print("Incorrect length! Make sure you seperate the year and group. e.g: 7 A")
                group_name = 0
            else:
                if int(group_name[0]) not in list(range(7,14)):
                    print("Invalid year!")
                    group_name = 0
                else:
                    if group_name[1].lower() not in ["a","b","c","d","e","f"]:
                        print("Invalid group!")
                        group_name = 0
        except:
            print("Error encountered! Try again.")
            group_name = 0
    print("Tutor group successfully entered.")

    student_total = 0
    while student_total == 0:
        try:
            student_total = int(input("How many students are in your tutor group?\n"))
            if student_total not in range(2,36):
                print("Student total out of bounds! Check your entry and try again.")
                student_total = 0
        except:
            student_total = 0
            print("Error encountered!")
    print("Student total successfully entered.")

    candidates_total = 0
    while candidates_total == 0:
        try:
            candidates_total = int(input("How many candidates are in your tutor group?\n"))
            if candidates_total not in range(1,5):
                print("Candidate number out of bounds! Check your entry and try again.")
                candidates_total = 0
        except:
            candidates_total = 0
            print("Error encountered!")
    print("Candidate total successfully entered.")

    candidate_name = ""
    candidate_dictionary = {"total":0}
    for i in range(candidates_total):
        if len(candidate_dictionary) >= 5:
            print("Maximum number of candidates reached!")
            break
        candidate_name = input(f"Enter candidate {i+1}'s name.\n")
        candidate_dictionary.update({candidate_name:0})
    print("Candidate entry completed. Current candidates: ")
    candidatesPrint(candidate_dictionary)
    votingProcess(candidate_dictionary)


def votingProcess(candidate_dict):
    voterID_list = []
    for i in range(student_total):
        voterId = input("\nPlease enter your voter ID.\n")
        if voterId in voterID_list:
            print("This Voter ID has already been used. You will not be allowed to vote.\n")
        else:
            print("Voter ID successfully registered!")
            voterID_list.append(voterId)
            print("Who would you like to vote for? Please chose from:")
            candidatesPrint(candidate_dict)
            vote_entry = 0
            while vote_entry not in candidate_dict:
                vote_entry = input("Please enter the candidate you want to vote for, or 'abstain'.\n")
                if vote_entry.lower() == "abstain":
                    print("You have abstained your vote.")
                    voter_notVoted = 1
                    break
                if vote_entry not in candidate_dict:
                    print("Not a valid candidate. Please enter their name again.")
                if vote_entry == "total":
                    print("Cheeky you. Please enter a valid candidate.")
                    vote_entry = 0
                if vote_entry in candidate_dict:
                    voter_notVoted = 0
            if voter_notVoted == 0:
                print("\nYour vote has been successfully registered!\n")
                candidate_dict.update({vote_entry:candidate_dict[vote_entry]+1})
                candidate_dict.update({"total":candidate_dict["total"]+1})
    print("\n**************** \nVoting Concluded \n****************\n")
    statistics(candidate_dict)

def statistics(candidate_dict):
    # Sorts the dictionary
    sorted_candidates_dict = dict(sorted(candidate_dict.items(), key = lambda item: item[1], reverse = True))
    sorted_candidates_list = [i for i in sorted_candidates_dict if i != "total"]
    print("Here are how the votes stack up:\n")
    for i in sorted_candidates_dict:
        if i != "total":
            percent = (sorted_candidates_dict[i] / sorted_candidates_dict["total"]) * 100
            percent = round(percent,1)
            print(f"#{sorted_candidates_list.index(i) + 1} - {i} - {sorted_candidates_dict[i]} Votes - {percent}% of the vote.")

    sorted_candidates_dict.pop("total")

    count = 0
    tiedList = [sorted_candidates_list[0]]
    for i in sorted_candidates_list:
        try:
            count += 1
            if sorted_candidates_dict[i] == sorted_candidates_dict[sorted_candidates_list[count]]:
                tiedList.append(sorted_candidates_list[count])
            else:
                break
        except:
            pass

    if len(tiedList) > 1:
        print("\n************************\nIt's a tie!\nThe voting will begin again.\n************************\n")
        candidate_dictionary = {"total":0}
        for i in tiedList:
            candidate_dictionary.update({i:0})
        votingProcess(candidate_dictionary)

tutorEntry()