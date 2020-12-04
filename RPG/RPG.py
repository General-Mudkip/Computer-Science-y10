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
tttButton = tk.Button(root, text = "Play Tic Tac Toe", command = tttGame)
ggButton = tk.Button(root, text = "Play Number Guesser", command = gGame)


# Displays the created widgets
heart1.grid(row = 0, column = 0)
heart2.grid(row = 0, column = 1)
heart3.grid(row = 0, column = 2)
tttButton.grid(row = 1, column = 0, columnspan = 3)
ggButton.grid(row=2, column = 0, columnspan = 3)

root.mainloop() # Starts main window