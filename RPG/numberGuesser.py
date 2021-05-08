import tkinter as tk
from tkinter import font as tkFont
import random
import configFile as cf

def guessingGame():

    answerNum = random.randint(1,100)
    print(answerNum)
    global playerAttempts
    playerAttempts = 0

    def submit():
        try:
            pAnswer = inputBox.get()
            pAnswer = int(pAnswer)
            global playerAttempts
            playerAttempts += 1
            if pAnswer < answerNum:
                answerLabel.config(text = "Too low!")
            elif pAnswer > answerNum:
                answerLabel.config(text = "Too high!")
            else:
                answerLabel.config(text = f"Correct! {playerAttempts} guesses.")
                if playerAttempts < 10:
                    cf.gGame_returnVal = 1
                    return 1
                cf.gGame_returnVal = 0
                return 0
                ngWindow.destroy()
        except:
            answerLabel.config(text = "Error Encountered! Guess again.")

    # Initializes main window
    ngWindow = tk.Tk()
    ngWindow.title("Number Guessing Game")
    ngWindow.geometry("170x130")

    # Initializes fonts
    helv25 = tkFont.Font(family = "Helvetica", size = 15)

    # Initializes widgets
    guessingTitle = tk.Label(ngWindow, text = "Guess a Number!", font= helv25)
    answerLabel = tk.Label(ngWindow, text = "Guess...")
    inputBox = tk.Entry(ngWindow, width = 20, borderwidth = 4)
    submitButton = tk.Button(ngWindow, text = "Submit Number", command = submit)

    # Displays widgets
    inputBox.grid(row = 2, column = 0)
    guessingTitle.grid(row = 0, column = 0)
    answerLabel.grid(row = 1, column = 0)
    submitButton.grid(row = 3, column = 0)

    ngWindow.mainloop()
    print("Fin")

if __name__ == '__main__':
    guessingGame()