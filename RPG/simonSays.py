import tkinter as tk
from tkinter import font as tkFont
import random
import time

# Doesn't work unfortunately due to how tkinter updates button colours.
# I've tried a few workarounds but can't get past the issue of the mainloop being paused whenever time.sleep() is called.

# Initialize main window
ssWindow = tk.Tk()
ssWindow.title("Simon Says")
ssWindow.geometry("750x484")

# Creates fonts
helv10 = tkFont.Font(family = "Helvetica", size = 10)
helv15 = tkFont.Font(family = "Helvetica", size = 15)
helv20 = tkFont.Font(family = "Helvetica", size = 17)
helv25 = tkFont.Font(family = "Helvetica", size = 25)
helv35 = tkFont.Font(family = "Helvetica", size = 35)

queue = []

def nextRound():
    queue.append(random.randint(1,16))
    for i in panelDict:
        panelDict[i].config(state = "active", bg = "white")
        panelDict[i].update()
    ssWindow.update_idletasks()
    for i in queue:
        time.sleep(0.5)
        panelDict[i].config(bg = "blue")
        panelDict[i].update()
        ssWindow.update_idletasks()
        time.sleep(1)
        panelDict[i].config(bg = "white")
        panelDict[i].update()
        ssWindow.update_idletasks()
    ssWindow.update()

def submit():
    nextRound()


# Initalizes panels
panelDict = {} # Dictionary to store panels
count = 0
for rowI in range(4):
    for columnI in range(4):
        count += 1
        panel = tk.Button(ssWindow, state = "disabled", command = submit, bg = "white", width = 14, height = 7)
        panel.grid(row = rowI, column = columnI)
        panelDict.update({count:panel})

nextRound()

# Initializes labels
title = tk.Label(ssWindow, text = "Simon Says", font = helv35, anchor = "n")
title.grid(row = 0, column = 4, sticky = "nw")

ssWindow.mainloop()