from tkinter import *

root = Tk()
root.title("Cool GUI")
root.geometry("300x200")

entryBox = Entry(root, bd = 3)
entryBox.grid(row = 0, column = 1)
entryLabel = Label(root, text = "Name")
entryLabel.grid(row = 0, column = 0)

def myClick():
    myLabel = Label(root, text = entryBox.get())
    myLabel.grid(row=2,column=1)

myButton = Button(root, text = "Enter Your Name", command = myClick).grid(row=1,column = 1)

root.mainloop()