import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkFont
from tictactoeGUI import ticTacToe as tttGame
import configFile as cf
import random
import time

# Initializes main window
root = tk.Tk()
root.geometry("800x600")
root.title("RPG - Bence Redmond")

# Creates fonts
helv10 = tkFont.Font(family = "Helvetica", size = 10)
helv15 = tkFont.Font(family = "Helvetica", size = 15)
helv20 = tkFont.Font(family = "Helvetica", size = 17)
helv25 = tkFont.Font(family = "Helvetica", size = 25)
helv35 = tkFont.Font(family = "Helvetica", size = 35)

# Function containing all of the tic tac toe code
def ticTacToe():
    # Initializes main window
    global tttWindow
    tttWindow = tk.Toplevel()
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
                global tttWindow
                for i in buttonList: # Iterates through the list of button objects
                    i.config(state = "disabled") # Sets each button to disabled
                label2.config(text = "Close the window to continue!")
                cf.tttGame_returnVal = symbol
                tttWindow.destroy()
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

def guessingGame():

    answerNum = random.randint(1,100)
    print(answerNum)
    global playerAttempts
    playerAttempts = 0

    global gGame 
    gGame = True

    def submit():
        try:
            pAnswer = inputBox.get()
            pAnswer = int(pAnswer)
            global playerAttempts
            playerAttempts += 1
            if pAnswer < answerNum:
                answerLabel.config(text = "Too low!")
            elif pAnswer > answerNum:
                answerLabel.config(text = "Too high!")
            else:
                answerLabel.config(text = f"Correct! {playerAttempts} guesses.")
                if playerAttempts < 10:
                    cf.gGame_returnVal = 1
                else:
                    cf.gGame_returnVal = 0
                global gGame
                gGame = False
                ngWindow.destroy()
        except:
            answerLabel.config(text = "Error Encountered! Guess again.")

    # Initializes main window
    global ngWindow
    ngWindow = tk.Toplevel(root)
    ngWindow.title("Number Guessing Game")
    ngWindow.geometry("170x130")

    # Initializes widgets
    guessingTitle = tk.Label(ngWindow, text = "Guess a Number!", font= helv15)
    answerLabel = tk.Label(ngWindow, text = "Guess...")
    inputBox = tk.Entry(ngWindow, width = 20, borderwidth = 4)
    submitButton = tk.Button(ngWindow, text = "Submit Number", command = submit)

    # Displays widgets
    inputBox.grid(row = 2, column = 0)
    guessingTitle.grid(row = 0, column = 0)
    answerLabel.grid(row = 1, column = 0)
    submitButton.grid(row = 3, column = 0)

def displayEnd(ending):
    global endScreen
    endScreen = tk.Toplevel(root)
    endName = ending["name"]
    endScreen.title(f"New Ending - {endName}")
    endScreen.geometry("550x150")

    player.unlockEnding(1)

    endName_label = tk.Label(endScreen, text = f"Ending Reached - {endName}", font = helv25)
    endText_label = tk.Label(endScreen, text = ending["text"], font = helv15)
    end2Text_label = tk.Label(endScreen, text = f"You've now unlocked {player.unlockedEndings}/{len(player.endDict)} endings.")
    restartButton = tk.Button(endScreen, text = "Restart Game", command = player.resetGame, font = helv20)

    endName_label.grid(row = 0, column = 0, sticky = "w")
    endText_label.grid(row = 2, column = 0, sticky = "w")
    end2Text_label.grid(row = 1, column = 0, sticky = "w")
    restartButton.grid(row = 3, column= 0, sticky = "w")

# Class to store player information
class playerState():

    def __init__(self, room, lives):
        self.room = room # Stores current room as an object
        self.lives = lives
        self.unlockedEndings = 0 
        # Dictionary to store different end conditions
        self.endDict = {1:{"name":"Awkward...","unlocked":False, "text":"Well, you weren't supposed to do that.", "room":"Doorway"},
                        2:{"name":"Finality","unlocked":False, "text":"You've beaten the game through the main route!", "room":"Placeholder"}
        }

    def loseLife(self, lost):
        self.lives -= lost
        # Code to manage hearts

    def resetGame(self):
        global endScreen
        endScreen.destroy()
        createRooms()
        createNeighbours()
        player.room = startingRoom
        startingRoom.initState()

    def unlockEnding(self, ending):
        if self.endDict[ending]["unlocked"] != True:
            self.unlockedEndings += 1
        self.endDict[ending].update({"unlocked":True})

class room():
    def __init__(self, puzzle, name, text, loseText, winText):
        self.name = name
        self.puzzle = puzzle
        self.text = text
        self.loseText = loseText
        self.winText = winText

    def assignNeighbours(self, left, right, up, down):
        # Stores the information about the room's neighbours, and the button object that leads to that room
        self.neighbours = {"left":{"button":leftArrow, "room":left}, 
                            "right":{"button":rightArrow, "room":right}, 
                            "up":{"button":upArrow, "room":up}, 
                            "down":{"button":downArrow, "room":down},
                            "test":"test"}

    def initState(self):
        global secondLabel, interactButton, roomLabel, roomText
        roomLabel.config(text = player.room.name)
        roomText.config(text = player.room.text)       
        dictList = ["left","right","up","down"]
        print("Initialized")
        for i in dictList:
            neighbour = self.neighbours[i]
            if neighbour["room"] == False:
                neighbour["button"].config(state = "disabled", bg = "#ff8080")
            else:
                if self.puzzle == "fin":
                    neighbour["button"].config(state = "active", bg = "white")
                else:
                    neighbour["button"].config(state = "disabled", bg = "#ff8080")
            if self.puzzle != "fin":    
                interactButton.config(state = "active", bg = "white")
            else:
                interactButton.config(state = "disabled", bg = "#ff8080")


    def moveRoom(self, direction):
        global roomLabel, roomText
        player.room = self.neighbours[direction]["room"]
        roomLabel.config(text = player.room.name)
        roomText.config(text = player.room.text)
        player.room.initState()

    def interact(self):
        global interactButton
        interactButton.config(state = "disabled")
        global roomText
        print(player.room.puzzle)
        if player.room.puzzle == "gGame":
            guessingGame()
            root.wait_window(ngWindow)
            returnVal = cf.gGame_returnVal
            if returnVal == 1:
                roomText.config(text = player.room.winText)
            elif returnVal == 0:
                roomText.config(text = player.room.loseText)
                player.loseLife(1)
            else:
                return
            player.room.puzzle = "fin"
            player.room.initState()
        elif player.room.puzzle == "ttt":
            ticTacToe()
            root.wait_window(tttWindow)
            returnVal = cf.tttGame_returnVal
            if returnVal == "x":
                roomText.config(text = player.room.winText)
            elif returnVal == "o":
                roomText.config(text = player.room.loseText)    
            else:
                return
            player.room.puzzle = "fin"
            player.room.initState()         
        else:
            displayEnd(player.endDict[player.room.puzzle])
            
def createRooms():
    global startingRoom, hallway1, doorway
    startingRoom = room("gGame", "Entrance", "Ho ho ho... welcome to my house of Death!", "Well that was a good effort... down one life!", "Hmm, maybe that was a bit too easy.")
    hallway1 = room("ttt", "Hallway", "You see a whiteboard on the wall, with a Tic Tac Toe board. Let's play!", "How did you... lose against yourself?", "I would have been worried if you hadn't won that.")
    doorway = room(1, "Doorway", "Well, I guess you win?", "N/A", "N/A")

def createNeighbours():
    global startingRoom, hallway1, doorway
    # Assigns the room's neighbours
    startingRoom.assignNeighbours(False, False, hallway1, doorway)
    doorway.assignNeighbours(False, False, startingRoom, False)
    hallway1.assignNeighbours(False, False, False, startingRoom)

createRooms()

player = playerState(startingRoom, 3)

def endingsScreen(endings):
    endingsWin = tk.Tk()
    endingsWin.title("Your Unlocked Endings")
    endingsWin.geometry("600x300")

    endingsTitle = tk.Label(endingsWin, font = helv35, text = f"All Endings || {player.unlockedEndings}/{len(endings)} Unlocked\n---------------------------------------")

    row = 1
    for i in range(1,len(endings)+1):
        print(endings[i])
        tempTitle = tk.Label(endingsWin, text = endings[i]["name"], font  = helv25, anchor = "w")
        tempLabel = tk.Label(endingsWin, text = f"Unlocked: {endings[i]['unlocked']} || {endings[i]['text']}")
        tempTitle.grid(row = row, column = 0, sticky = "w")
        tempLabel.grid(row = row + 1, column = 0, sticky = "w")
        row += 2

    endingsTitle.grid(row = 0, column = 0, columnspan = 2, sticky = "w")

    endingsWin.mainloop()

# Initializes main images
preHeart_img = Image.open("heart.png")
preHeart_img = preHeart_img.resize((60, 60), Image.ANTIALIAS)
heart_img = ImageTk.PhotoImage(preHeart_img)

# Creates the heart labels
heart1 = tk.Label(root, image = heart_img, anchor = "w")
heart2 = tk.Label(root, image = heart_img, anchor = "w")
heart3 = tk.Label(root, image = heart_img, anchor = "w")

# Creates main text
roomLabel = tk.Label(root, text = player.room.name, font = helv35)
roomText = tk.Label(root, text = player.room.text, font = helv20)
secondLabel = tk.Label(root, text = "Choose a direction to go:", font = helv15)

# Creates buttons
endingsButton = tk.Button(root, text = "Unlocked Endings", font = helv15, command = lambda: endingsScreen(player.endDict))
tttButton = tk.Button(root, text = "Play Tic Tac Toe", command = tttGame) # Button to start Tic Tac Toe
ggButton = tk.Button(root, text = "Play Number Guesser", command = guessingGame) # Button to start Guessing Game
upArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "^", font = helv15, command = lambda: player.room.moveRoom("up"))
leftArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "<", font = helv15, command = lambda: player.room.moveRoom("left"))
downArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "v", font = helv15, command = lambda: player.room.moveRoom("down"))
rightArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = ">", font = helv15, command = lambda: player.room.moveRoom("right")) 
interactButton = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "x", font = helv15, command = player.room.interact)

# Creates empty canvas spaces
topCanvas = tk.Canvas(root, width = 160, height = 10)

# Displays the created widgets
heart1.grid(row = 0, column = 0)
heart2.grid(row = 0, column = 1)
heart3.grid(row = 0, column = 2)
roomLabel.grid(row = 0, column = 3, padx = 20)
secondLabel.grid(row = 2, column = 0, columnspan = 3)
topCanvas.grid(row = 0, column = 4, columnspan = 1)
endingsButton.grid(row = 0, column = 5)
roomText.grid(row = 1, column = 0, columnspan = 8, sticky = "w")

upArrow.grid(row = 3, column = 1)
leftArrow.grid(row = 4, column = 0)
downArrow.grid(row = 5, column = 1)
rightArrow.grid(row = 4, column = 2)
interactButton.grid(row = 4, column = 1)

createNeighbours()

startingRoom.initState()

root.mainloop() # Starts main window