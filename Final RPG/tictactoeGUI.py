import tkinter as tk # Module used to create GUIs
from tkinter import font as tkFont 
import configFile

# Function containing all of the tic tac toe code
def ticTacToe():
    # Initializes main window
    tttWindow = tk.Tk()
    tttWindow.title("Tic Tac Toe")
    tttWindow.geometry("425x650")

    global playerSymbol
    playerSymbol = "x"

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

    # Creates fonts
    helv25 = tkFont.Font(family = "Helvetica", size = 25)
    helv50 = tkFont.Font(family = "Helvetica", size = 50)

    # Initalizes boxes
    b1 = tk.Button(tttWindow, text = board[1][1], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b1,1,1,playerSymbol))
    b2 = tk.Button(tttWindow, text = board[1][2], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b2,1,2,playerSymbol))
    b3 = tk.Button(tttWindow, text = board[1][3], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b3,1,3,playerSymbol))
    b4 = tk.Button(tttWindow, text = board[2][1], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b4,2,1,playerSymbol))
    b5 = tk.Button(tttWindow, text = board[2][2], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b5,2,2,playerSymbol))
    b6 = tk.Button(tttWindow, text = board[2][3], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b6,2,3,playerSymbol))
    b7 = tk.Button(tttWindow, text = board[3][1], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b7,3,1,playerSymbol))
    b8 = tk.Button(tttWindow, text = board[3][2], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b8,3,2,playerSymbol))
    b9 = tk.Button(tttWindow, text = board[3][3], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b9,3,3,playerSymbol))
    # Creates list of the button objects that can be iterated through later
    buttonList = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


    # Creates labels
    turnLabel = tk.Label(tttWindow, text = f"It is {playerSymbol}'s turn.", font = helv25)
    label2 = tk.Label(tttWindow, text = "Pick a slot!")

    # Displays buttons in the 3x3 grid pattern
    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)
    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)
    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

    # Displays labels at the bottom of the screen
    turnLabel.grid(row = 3, column = 0, columnspan = 3) # Displays who's turn it is
    label2.grid(row = 4, column = 0, columnspan = 3) # Displays smaller misc message

    # Changes the symbol, takes the button object for modification, x and y for board dict coords, and symbol for the player symbol
    def changeSymbol(buttonObj, x, y, symbol):
        if board[x][y] != "-": # Checks if the slot is empty or not
            label2.config(text = "Invalid Slot!")
        else:
            board[x][y] = symbol
            buttonObj.config(text = board[x][y], state = "disabled") # Sets the button the player clicked to their symbol and disables it
            if winCheck(board, symbol) == 0:
                for i in buttonList: # Iterates through the list of button objects
                    i.config(state = "disabled") # Sets each button to disabled
                label2.config(text = "Close the window to continue!")
                return
            
            # Modifies the player's symbol
            global playerSymbol
            if symbol == "x":
                playerSymbol = "o"
            else:
                playerSymbol = "x"
            turnLabel.config(text = f"It is {playerSymbol}'s turn!")

    def winCheck(board,symbol):
            # Checks for horizontal wins
            for i in board:
                # Creates set of the values in each row
                rowSet = set(board[i].values())
                # As sets cannot contain duplicate values, a row such as "x o x" will become {"x","o"}
                # We can then check if the row contains only one value (such as {"x"}) and if the value in the set is the player's symbol.
                if len(rowSet) == 1 and playerSymbol in rowSet:
                    turnLabel.config(text = f"{symbol} wins horizontally!")
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
                    turnLabel.config(text = f"{symbol} wins vertically!")
                    return 0
            # Checks for diagonal wins
            diag1 = set(board[1][1]+board[2][2]+board[3][3]) # Top left to bottom right
            diag2 = set(board[1][3]+board[2][2]+board[3][1]) # Top right to bottom left
            # Same check system as above
            if len(diag1) == 1 and playerSymbol in diag1:
                turnLabel.config(text = f"{symbol} wins diagonally!")            
                return 0
            if len(diag2) == 1 and playerSymbol in diag2:
                turnLabel.config(text = f"{symbol} wins diagonally!")
                return 0
            # Checks for draws using boardSet, which will contain all values in the dictionary
            if "-" not in boardSet: # Checks if there are any empty slots left
                turnLabel.config(text = f"It's a draw!")
                return 0


    tttWindow.mainloop()

if __name__ == "__main__":
    ticTacToe()