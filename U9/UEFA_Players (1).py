players_list = {}

def pretty_print(teams_list):
    for i in teams_list:
        print(f"Player #{i} - Name:{teams_list[i]['name']} ; Age:{teams_list[i]['age']} ; Country:{teams_list[i]['country']}")

def data_getting(players_list,names_list):
    while True:
        choice = 0
        while choice not in ["1","2"]:
            choice = input("Would you like to get information by;\n1. Player Number?\n2. Player Name?\n")
        if choice == "1":
            p_num = input("What player number would you like to get?\n")
            try:
                while int(p_num) not in range(1,11):
                    print("Invalid range! Enter a number between 1 and 11.")
                    p_num = input("What player number would you like to get?\n")
            except BaseException:
                print("Error inputting data.")
                data_getting(players_list)
        
            p_num=int(p_num)
            print(f"\n\nHere's the data for Player #{p_num}:\nName: {players_list[p_num]['name']}\nAge: {players_list[p_num]['age']}\nCounty: {players_list[p_num]['country']}\n\n")

        if choice == "2":
            p_name = input("What player name would you like to get data from?")
            if p_name not in names_list:
                print("Invalid name.")
            else:
                print()
            

for i in range(11):
    try:
        data_entry = input(f"Input the player data for position #{i+1}, in the form 'name,age,country'.\n")
        data_entry = data_entry.split(",")
        # Stores player data by their number.
        # Number { Name ; Age ; Country }
        players_list.update({i+1:{"name":data_entry[0],"age":int(data_entry[1]),"country":data_entry[2]}})
    except BaseException:
        print("Error encountered while entering data.")

pretty_print(players_list)

sum_of_ages = 0
count = 0
lowest_age = 999
highest_age = 0

print("")

for i in players_list:
    count += 1
    cur_age = players_list[i]["age"]
    sum_of_ages += cur_age
    if cur_age > highest_age:
        highest_age = cur_age
        highest_name = players_list[i]["name"]
    if cur_age < lowest_age:
        lowest_age = cur_age
        lowest_name = players_list[i]["name"]

print(f"\nThe oldest player is: {highest_name}, at {highest_age} years old.\nThe youngest player is: {lowest_name}, at {lowest_age} years old.\nThe average age of the team is {sum_of_ages/count}.")

name_list = [players_list[i]["name"] for i in players_list]

data_getting(players_list,name_list)