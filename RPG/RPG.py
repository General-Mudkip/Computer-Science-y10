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

# Class to store player information
class playerState():

    def __init__(self, room, lives):
        self.room = room # Stores current room as an object
        self.lives = lives
        self.unlockedEndings = 0 
        # Dictionary to store different end conditions
        self.endDict = {1:{"name":"Awkward...","unlocked":False, "text":"Well, you weren't supposed to do that."},
                        2:{"name":"Finality","unlocked":False, "text":"You've beaten the game through the main route!"}
        }

    def loseLife(self, lost):
        self.lives -= lost
        # Code to manage hearts

    def startGame(self):
        pass

    def unlockEnding(self, ending):
        self.endDict.update({ending:{"unlocked":True}})

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
        global secondLabel
        global interactButton
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
        global roomLabel
        global roomText
        player.room = self.neighbours[direction]["room"]
        roomLabel.config(text = player.room.name)
        roomText.config(text = player.room.text)
        player.room.initState()

    def interact(self):
        global roomText
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
                

startingRoom = room("gGame", "Entrance", "Ho ho ho... welcome to my house of Death!", "Well that was a good effort... down one life!", "Hmm, maybe that was a bit too easy.")
hallway1 = room("ttt", "Hallway", "You see a whiteboard on the wall, with a Tic Tac Toe board. Let's play!", "How did you... lose against yourself?", "I would have been worried if you hadn't won that.")
doorway = room("end", "Doorway", "Well, I guess you win?", "N/A", "N/A")


player = playerState(startingRoom, 3)

def endingsScreen(endings):
    endingsWin = tk.Tk()
    endingsWin.title("Your Unlocked Endings")
    endingsWin.geometry("600x300")

    endingsTitle = tk.Label(endingsWin, font = helv35, text = f"All Endings || {player.unlockedEndings}/{len(endings)} Unlocked\n---------------------------------------")

    row = 1
    for i in range(1,len(endings)+1):
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

#tttButton.grid(row = 1, column = 0, columnspan = 3)
#ggButton.grid(row=2, column = 0, columnspan = 3)

# Assigns the room's neighbours
startingRoom.assignNeighbours(False, False, hallway1, doorway)
doorway.assignNeighbours(False, False, startingRoom, False)
hallway1.assignNeighbours(False, False, False, startingRoom)

startingRoom.initState()

root.mainloop() # Starts main window