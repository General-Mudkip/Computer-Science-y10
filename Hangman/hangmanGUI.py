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

hm_window.mainloop()