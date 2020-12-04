import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkFont
from tictactoeGUI import ticTacToe as tttGame
from numberGuesser import guessingGame as gGame

# Initializes main window
root = tk.Tk()
root.geometry("800x600")
root.title("RPG - Bence Redmond")

# Initializes main images
preHeart_img = Image.open("heart.png")
preHeart_img = preHeart_img.resize((60, 60), Image.ANTIALIAS)
heart_img = ImageTk.PhotoImage(preHeart_img)

# Creates the heart labels
heart1 = tk.Label(root, image = heart_img)
heart2 = tk.Label(root, image = heart_img)
heart3 = tk.Label(root, image = heart_img)
tttButton = tk.Button(root, text = "Play Tic Tac Toe", command = tttGame) # Button to start Tic Tac Toe
ggButton = tk.Button(root, text = "Play Number Guesser", command = gGame) # Button to start Guessing Game


# Displays the created widgets
heart1.grid(row = 0, column = 0)
heart2.grid(row = 0, column = 1)
heart3.grid(row = 0, column = 2)
tttButton.grid(row = 1, column = 0, columnspan = 3)
ggButton.grid(row=2, column = 0, columnspan = 3)

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

    def enterRoom(self):
        pass

    def exitRoom(self):
        pass


startingRoom = room("gGame", "Entrance", "Ho ho ho... welcome to my house of Death!")
hallway1 = room("gGame", "Hallway", "You see a whiteboard on the wall, with a Tic Tac Toe board. Let's play!")
doorway = room("End", "Doorway", "Well, I guess you win?")

startingRoom.assignNeighbours(False, False, hallway1, doorway)
hallway1.assignNeighbours(False, False, False, startingRoom)

root.mainloop() # Starts main window