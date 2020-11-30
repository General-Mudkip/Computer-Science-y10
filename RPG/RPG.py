import tkinter as tk
from tkinter import font as tkFont
from tictactoeGUI import ticTacToe as tttGame

# Initializes main window
root = tk.Tk()
root.geometry("800x600")
root.title("RPG - Bence Redmond")

# Initializes main images
heart_img = tk.PhotoImage(file = "heart.png")
heart1 = tk.Label(root, image = heart_img)
heart1.pack()


root.mainloop() # Starts main window