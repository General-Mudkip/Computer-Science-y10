#x = [int(input("Enter a dish: \n")) for i in range(5)]
#print(x)

movieList = [None] * 6
choice = 0
while choice != 5:
    print("Welcome to the filming list!")
    while choice == 0:
        try:
            choice = int(input("1. Reset List\n2. View entire list\n3. View one item\n4. Edit list\n5. Quit\n\n"))
            if choice not in list(range(1,7)):
                print("Invalid choice!")
                choice = 0
        except:
            print("Invalid input!")
            choice = 0
    if choice == 1:
        print("Created new blank film list with 6 films!\n")
        movieList = [None] * 6
    elif choice == 2:
        print("Here’s the current list:\n",movieList)
    elif choice == 3:
        movieChoice = 0
        while movieChoice == 0:
            try:
                movieChoice = int(input("Which movie would you like to view? 1-6\n"))
                if movieChoice not in list(range(1,7)):
                    print("Entry not within bounds!\n")
                    movieChoice = 0
            except:
                print("Invalid input!")
                movieChoice = 0
        print(f"Here’s movie #{movieChoice}:\n{movieList[movieChoice -1]}")
    elif choice == 4:
        movieChoice = 0
        while movieChoice == 0:
            try:
                movieChoice = int(input("Which movie would you like to modify? 1-6\n"))
                if movieChoice not in list(range(1,7)):
                    print("Entry not within bounds!\n")
                    movieChoice = 0
            except:
                print("Invalid input!")
                movieChoice = 0
        print(f"Now modifying movie #{movieChoice}.\n")
        newMovie = input("Please enter the movie name:\n")
        movieList[movieChoice-1] = newMovie
        print(f"Movie #{movieChoice} is now {newMovie}.")
    if choice != 5:
        pause = input("Press enter to continue.")
        choice = 0
print("Program exited!")