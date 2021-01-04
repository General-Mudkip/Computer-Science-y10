import tkinter as tk
from tkinter import font as tkFont
import random
import time

code = "1234"

# Initialize main window
ceWindow = tk.Tk()
ceWindow.title("Keypad")
ceWindow.geometry("233x320")

# Creates fonts
helv10 = tkFont.Font(family = "Helvetica", size = 10)
helv15 = tkFont.Font(family = "Helvetica", size = 15)
helv20 = tkFont.Font(family = "Helvetica", size = 17)
helv25 = tkFont.Font(family = "Helvetica", size = 25)
helv35 = tkFont.Font(family = "Helvetica", size = 35)

# Initialize widgets
display = tk.Entry(ceWindow, width = 17, borderwidth = 5, font = helv20)
display.grid(row = 0, column = 0, columnspan = 3)

def button_click(num):
    newText = display.get() + str(num)
    display.delete(0, tk.END)
    display.insert(0, newText)

def submit():
    answer = display.get()
    if answer == code:
        display.delete(0, tk.END)
        display.insert(0, "Correct!")
        display.update()
        time.sleep(2)
        ceWindow.destroy()
    else:
        display.delete(0, tk.END)
        display.insert(0, "Incorrect!")
        display.update()
        time.sleep(2)
        display.delete(0, tk.END)

text = tk.Label(ceWindow, text = "Enter The Code.")
button_1 = tk.Button(ceWindow, text = "1", padx = 30, pady = 20, command = lambda: button_click(1))
button_2 = tk.Button(ceWindow, text = "2", padx = 30, pady = 20, command = lambda: button_click(2))
button_3 = tk.Button(ceWindow, text = "3", padx = 30, pady = 20, command = lambda: button_click(3))
button_4 = tk.Button(ceWindow, text = "4", padx = 30, pady = 20, command = lambda: button_click(4))
button_5 = tk.Button(ceWindow, text = "5", padx = 30, pady = 20, command = lambda: button_click(5))
button_6 = tk.Button(ceWindow, text = "6", padx = 30, pady = 20, command = lambda: button_click(6))
button_7 = tk.Button(ceWindow, text = "7", padx = 30, pady = 20, command = lambda: button_click(7))
button_8 = tk.Button(ceWindow, text = "8", padx = 30, pady = 20, command = lambda: button_click(8))
button_9 = tk.Button(ceWindow, text = "9", padx = 30, pady = 20, command = lambda: button_click(9))
button_0 = tk.Button(ceWindow, text = "0", padx = 30, pady = 20, command = lambda: button_click(0))
submit = tk.Button(ceWindow, text = "Submit", padx = 53, pady = 20, command = submit)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
submit.grid(row=4, column=1, columnspan=2)
text.grid(row = 5, column = 0, columnspan = 4)

ceWindow.mainloop()