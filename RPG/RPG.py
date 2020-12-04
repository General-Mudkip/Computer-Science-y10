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

class playerState():


    def __init__(self, room, lives):
        self.room = room
        self.lives = lives
        self.endDict = {1:{"name":"Awkward...","unlocked":False, "text":"Well, you weren't supposed to do that."}}

    def unlockEnding(self, ending):
        self.endDict.update({ending:{"unlocked":True}})

class room():
    def __init__(self, puzzle, name, text):
        self.name = name
        self.puzzle = puzzle
        self.text = text

    def assignNeighbours(self, left, right, up, down):
        self.leftNeighbour = left
        self.rightNeighbour = right
        self.upNeighbour = up
        self.downNeighbour = down

    def enterRoom(self, direction):
        pass

    def exitRoom(self, direction):
        pass


startingRoom = room("gGame", "Entrance", "Ho ho ho... welcome to my house of Death!")
hallway1 = room("gGame", "Hallway", "You see a whiteboard on the wall, with a Tic Tac Toe board. Let's play!")
doorway = room("End", "Doorway", "Well, I guess you win?")


player = playerState(startingRoom, 3)

def endingsScreen(endings):
    endingsWin = tk.Tk()
    endingsWin.title("Your Unlocked Endings")
    endingsWin.geometry("600x300")

    awkwardTitle = tk.Label(endingsWin, text = endings[1]["name"], font = helv25, anchor = "w")
    awkwardLabel = tk.Label(endingsWin, text = f"Unlocked: {endings[1]['unlocked']} || {endings[1]['text']}")
    awkwardLabel.grid(row = 1, column = 0)
    awkwardTitle.grid(row = 0, column = 0)

    endingsWin.mainloop()

# Initializes main images
preHeart_img = Image.open("heart.png")
preHeart_img = preHeart_img.resize((60, 60), Image.ANTIALIAS)
heart_img = ImageTk.PhotoImage(preHeart_img)

# Creates the heart labels
heart1 = tk.Label(root, image = heart_img, anchor = "w")
heart2 = tk.Label(root, image = heart_img, anchor = "w")
heart3 = tk.Label(root, image = heart_img, anchor = "w")
roomLabel = tk.Label(root, text = player.room.name, font = helv35)
roomText = tk.Label(root, text = player.room.text, font = helv15)
endingsButton = tk.Button(root, text = "Unlocked Endings", command = lambda: endingsScreen(player.endDict))
tttButton = tk.Button(root, text = "Play Tic Tac Toe", command = tttGame) # Button to start Tic Tac Toe
ggButton = tk.Button(root, text = "Play Number Guesser", command = gGame) # Button to start Guessing Game

# Creates empty canvas spaces
topCanvas = tk.Canvas(root, width = 220, height = 10)

# Displays the created widgets
heart1.grid(row = 0, column = 0)
heart2.grid(row = 0, column = 1)
heart3.grid(row = 0, column = 2)
roomLabel.grid(row = 0, column = 3, padx = 20)
topCanvas.grid(row = 0, column = 4, columnspan = 1)
endingsButton.grid(row = 0, column = 5)
roomText.grid(row = 1, column = 0, columnspan = 4)
#tttButton.grid(row = 1, column = 0, columnspan = 3)
#ggButton.grid(row=2, column = 0, columnspan = 3)

startingRoom.assignNeighbours(False, False, hallway1, doorway)
hallway1.assignNeighbours(False, False, False, startingRoom)

root.mainloop() # Starts main window