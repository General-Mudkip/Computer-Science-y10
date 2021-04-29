import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkFont
import random

hm_window = tk.Tk()
hm_window.title("Hangman || By Bence Redmond")
hm_window.geometry("500x300")

# Creates fonts
helv10 = tkFont.Font(family = "Helvetica", size = 10)
helv15 = tkFont.Font(family = "Helvetica", size = 15)
helv20 = tkFont.Font(family = "Helvetica", size = 17)
helv25 = tkFont.Font(family = "Helvetica", size = 25)
helv35 = tkFont.Font(family = "Helvetica", size = 35)

# Initializes labels

titleLabel = tk.Label(hm_window, text = "Hangman", font = helv25)
subTitle = tk.Label(hm_window, text = "Setting up game...", font = helv15)

# Displays all elements
titleLabel.grid(row = 0, column = 0, sticky = "w")
subTitle.grid(row = 1, column = 0, sticky = "w")

hm_window.mainloop()