import tkinter as tk
from tkinter import font as tkFont
import random

print(f"Your answer was {1==0}")

def guessingGame():

    answerNum = random.randint(1,100)
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

if __name__ == '__main__':
    guessingGame()