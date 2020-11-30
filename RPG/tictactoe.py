# Tic Tac Toe Function
def tttGame():
    # Creates the board
    # Each upper dictionary represents a row, and each nested dictionary
    # Represents a column. So if printed (as a board would be) this would output:
    #         Column:
    #          1 2 3
    #          _____
    #      1 | x o x
    # Row: 2 | x o x
    #      3 | x o x

    board = {
                1:{1:"-",2:"-",3:"-"},
                2:{1:"-",2:"-",3:"-"},
                3:{1:"-",2:"-",3:"-"}
            }

    ticTacToe = 0

    # Function for printing out the board
    def boardPrint():
        # Iterates through the rows
        for i in board:
            rowPrint = ""
            # Iterates through the columns in that row
            for place in board[i]:
                # Adds the value from the column + row to rowPrint
                rowPrint += board[i][place] + " "
            print(rowPrint)


    # Function to modify the board
    def boardModify():
        rowMod = 0
        # Loops until the user inputs 1, 2, or 3
        while not 1 <= rowMod <= 3:
            try:
                rowMod = int(input("Input row: "))
            except:
                print("Invalid input!")
            if not 1 <= rowMod <= 3:
                print(f"{rowMod}! Please chose a row from 1-3.")
        colMod = 0
        # Same as rowMod code
        while not 1 <= colMod <= 3:
            try:
                colMod = int(input("Input column: "))
            except:
                print("Invalid input!")
            if not 1 <= colMod <= 3:
                print("Invalid column! Please chose a column from 1-3.")
        print(f"Row: {rowMod} || Column: {colMod}")
        # Checks if the selected slot has already been filled
        if board[rowMod][colMod] != "-":
            print("This slot has already been selected! Chose a different slot.")
            boardModify()
        else:
            # Sets the selected slot to the player's symbol
            board[rowMod][colMod] = playerSymbol   
            boardPrint() 

    # Function to send message at the start of each player's turn to prevent the same message being sent every time the function is
    # called. (See above, boardModify() is called again if the selected slot has already been filled.)
    def modStart():
        print(f"\nIt is {playerSymbol}'s turn. \nThe current board looks like this:")
        boardPrint()


    def winCheck(board,symbol):
        # Checks for horizontal wins
        for i in board:
            # Creates set of the values in each row
            rowSet = set(board[i].values())
            # As sets cannot contain duplicate values, a row such as "x o x" will become {"x","o"}
            # We can then check if the row contains only one value (such as {"x"}) and if the value in the set is the player's symbol.
            if len(rowSet) == 1 and playerSymbol in rowSet:
                print(f"{playerSymbol} wins horizontally!")
                return 0
        # Checks for vertical wins
        boardSet = set()
        for i in range(1,4):
            colSet = set()
            # Have to use range(1,4) since range(1,3) won't go up to 3 for whatever reason.
            for row in range(1,4):
                colSet.add(board[row][i])
                boardSet.add(board[row][i])
            # Same as above
            if len(colSet) == 1 and playerSymbol in colSet:
                print(f"{playerSymbol} wins vertically!")
                return 0
        # Checks for diagonal wins
        diag1 = set(board[1][1]+board[2][2]+board[3][3]) # Top left to bottom right
        diag2 = set(board[1][3]+board[2][2]+board[3][1]) # Top right to bottom left
        # Same as above
        if len(diag1) == 1 and playerSymbol in diag1:
            print(f"{playerSymbol} wins diagonally!")
            return 0
        if len(diag2) == 1 and playerSymbol in diag2:
            print(f"{playerSymbol} wins diagonally!")
            return 0
        # Checks for draws
        if "-" not in boardSet:
            print("\nIt's a draw!\n")
            return 0


    print("\n\nWell... Tic Tac Toe is a game that requires multiple players.\nUnfortunately I'm not smart enough to play this so...\nGrab a friend?")
    # Just an interupt between chunks of text to help user readability
    ticTacToe = input("\nPress Enter to Start the Game ")
    ticTacToe = 1
    while ticTacToe == 1:
        # This could likely be shortened, works as is though.
        playerSymbol = "x"
        modStart()
        boardModify()
        # winCheck() will return 0 if a player has won (see above) so this just checks if the selected player has won.
        if winCheck(board,"x") == 0:
            ticTacToe = 0
            break
        playerSymbol = "o"
        modStart()
        boardModify()
        # Same as above check
        if winCheck(board,"o") == 0:
            ticTacToe = 0
            break
    print("\n\n Game Over! \n\n")

tttGame()