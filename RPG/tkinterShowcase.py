import tkinter as tk
from tkinter import font as tkFont

root = tk.Tk()
root.title("Quiz")
root.geometry("500x200")

# Creates fonts
helv10 = tkFont.Font(family = "Helvetica", size = 10)
helv15 = tkFont.Font(family = "Helvetica", size = 15)
helv20 = tkFont.Font(family = "Helvetica", size = 17)
helv25 = tkFont.Font(family = "Helvetica", size = 25)
helv35 = tkFont.Font(family = "Helvetica", size = 35)

questionNo = 1
correctAnswer = 0

questionsDict = {1:{"q":"What's my Name?", "answers":{1:"Bence", 2:"Idiot", 3:"AMAZING INDIVIDUAL", 4:"GENIUS"}, "c":1},
                 2:{"q":"What's Nina's name?","answers":{1:"HMMM",2:"IDOT",3:"NIAN",4:"UNREADABLE"},"c":3}}

def submit(answer):
    global qName, qDesc, questionNo, correctAnswer
    try:
        if answer == questionsDict[questionNo]["c"]:
            print("CORRECT")
            correctAnswer += 1
            qDesc.config(text = "Correct!")
        else:
            print("NOOOO")
            qDesc.config(text = "Incorrect!")
        questionNo += 1
        qName.config(text = questionsDict[questionNo]["q"])
        for i in range(1,5):
            buttonDict[i].config(text = questionsDict[questionNo]["answers"][i])
    except KeyError:
        qDesc.config(text = "End of Game!")
        qName.config(text = f"You got: {correctAnswer}/{len(questionsDict)}")
        for i in range(1,5):
            buttonDict[i].config(state = "disabled")

title = tk.Label(root, text = "Multiple Choice Quiz", font = helv25)
a1 = tk.Button(root, font = helv10, command = lambda: submit(1))
a2 = tk.Button(root, font = helv10, command = lambda: submit(2))
a3 = tk.Button(root, font = helv10, command = lambda: submit(3))
a4 = tk.Button(root, font = helv10, command = lambda: submit(4))

a1.grid(row = 3, column = 0)
a2.grid(row = 3, column = 1)
a3.grid(row = 3, column = 2)
a4.grid(row = 3, column = 3)

buttonDict = {1:a1,2:a2,3:a3,4:a4}

def start():
    global qName, qDesc
    qName = tk.Label(root, text = questionsDict[1]["q"], font = helv20)
    qName.grid(row = 2, column = 0, sticky = "w", columnspan = 5)
    qDesc = tk.Label(root, text = "Make your choice!",font = helv15)
    qDesc.grid(row = 1, column = 0, sticky = "w", columnspan = 5)
    for i in range(1,5):
        buttonDict[i].config(text = questionsDict[1]["answers"][i])

title.grid(row = 0, column = 0, columnspan = 4)

start()

root.mainloop()