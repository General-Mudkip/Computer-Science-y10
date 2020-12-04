import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkFont
from tictactoeGUI import ticTacToe as tttGame
from numberGuesser import guessingGame as gGame

# Initializes main window
root = tk.Tk()
root.geometry("800x600")
root.title("RPG - Bence Redmond")

# Creates fonts
helv10 = tkFont.Font(family  = "Helvetica", size = 10)
helv15 = tkFont.Font(family  = "Helvetica", size = 15)
helv25 = tkFont.Font(family  = "Helvetica", size = 25)
helv35 = tkFont.Font(family  = "Helvetica", size = 35)


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

    def unlockEnding(self, ending):
        self.endDict.update({ending:{"unlocked":True}})

class room():
    def __init__(self, puzzle, name, text):
        self.name = name
        self.puzzle = puzzle
        self.text = text

    def assignNeighbours(self, left, right, up, down):
        self.neighbours = {"left":{"button":leftArrow, "room":left}, 
                            "right":{"button":rightArrow, "room":right}, 
                            "up":{"button":upArrow, "room":up}, 
                            "down":{"button":downArrow, "room":down},
                            "test":"test"}

    def initState(self):
        global secondLabel
        dictList = ["left","right","up","down"]
        for i in dictList:
            if self.neighbours[i]["room"] == False:
                self.neighbours[i]["button"].config(state = "disabled", bg = "#ff8080")
            else:
                self.neighbours[i]["button"].config(state = "active", bg = "white")

    def moveRoom(self, direction):
        global roomLabel
        global roomText
        player.room = self.neighbours[direction]["room"]
        roomLabel.config(text = player.room.name)
        roomText.config(text = player.room.text)
        player.room.initState()


startingRoom = room(gGame, "Entrance", "Ho ho ho... welcome to my house of Death!")
hallway1 = room(gGame, "Hallway", "You see a whiteboard on the wall, with a Tic Tac Toe board. Let's play!")
doorway = room("End", "Doorway", "Well, I guess you win?")


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
roomText = tk.Label(root, text = player.room.text, font = helv15)
secondLabel = tk.Label(root, text = "Choose a direction to go:", font = helv15)

# Creates buttons
endingsButton = tk.Button(root, text = "Unlocked Endings", font = helv15, command = lambda: endingsScreen(player.endDict))
tttButton = tk.Button(root, text = "Play Tic Tac Toe", command = tttGame) # Button to start Tic Tac Toe
ggButton = tk.Button(root, text = "Play Number Guesser", command = gGame) # Button to start Guessing Game
upArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "^", font = helv15, command = lambda: player.room.moveRoom("up"))
leftArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "<", font = helv15, command = lambda: player.room.moveRoom("left"))
downArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "v", font = helv15, command = lambda: player.room.moveRoom("down"))
rightArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = ">", font = helv15, command = lambda: player.room.moveRoom("right")) 

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
roomText.grid(row = 1, column = 0, columnspan = 4, sticky = "w")

upArrow.grid(row = 3, column = 1)
leftArrow.grid(row = 4, column = 0)
downArrow.grid(row = 5, column = 1)
rightArrow.grid(row = 4, column = 2)

#tttButton.grid(row = 1, column = 0, columnspan = 3)
#ggButton.grid(row=2, column = 0, columnspan = 3)

# Assigns the room's neighbours
startingRoom.assignNeighbours(False, False, hallway1, doorway)
doorway.assignNeighbours(False, False, startingRoom, False)
hallway1.assignNeighbours(False, False, False, startingRoom)

startingRoom.initState()

root.mainloop() # Starts main window