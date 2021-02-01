import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkFont
from tictactoeGUI import ticTacToe as tttGame
import configFile as cf
import random
import time

# Initializes main window
root = tk.Tk()
root.geometry("720x600")
root.title("RPG - Bence Redmond")

# Creates fonts
helv10 = tkFont.Font(family = "Helvetica", size = 10)
helv15 = tkFont.Font(family = "Helvetica", size = 15)
helv20 = tkFont.Font(family = "Helvetica", size = 17)
helv25 = tkFont.Font(family = "Helvetica", size = 25)
helv35 = tkFont.Font(family = "Helvetica", size = 35)

tooltipList = []

# Function containing all of the tic tac toe code
def ticTacToe():
    # Initializes main window
    global tttWindow
    tttWindow = tk.Toplevel()
    tttWindow.title("Tic Tac Toe")
    tttWindow.geometry("425x650")

    global playerSymbol
    playerSymbol = "x"

    # Creates the board
    # Each upper dictionary represents a row, and each nested dictionary
    # Represents a column. So if printed (as a board would be) this would output:
    #         Column:
    #          1 2 3
    #          _____
    #      1 | x o x
    # Row: 2 | x o x
    #      3 | x o x

    board = {
                1:{1:"-",2:"-",3:"-"},
                2:{1:"-",2:"-",3:"-"},
                3:{1:"-",2:"-",3:"-"}
            }

    # Creates fonts
    helv25 = tkFont.Font(family = "Helvetica", size = 25)
    helv50 = tkFont.Font(family = "Helvetica", size = 50)

    # Initalizes boxes
    b1 = tk.Button(tttWindow, text = board[1][1], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b1,1,1,playerSymbol))
    b2 = tk.Button(tttWindow, text = board[1][2], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b2,1,2,playerSymbol))
    b3 = tk.Button(tttWindow, text = board[1][3], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b3,1,3,playerSymbol))
    b4 = tk.Button(tttWindow, text = board[2][1], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b4,2,1,playerSymbol))
    b5 = tk.Button(tttWindow, text = board[2][2], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b5,2,2,playerSymbol))
    b6 = tk.Button(tttWindow, text = board[2][3], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b6,2,3,playerSymbol))
    b7 = tk.Button(tttWindow, text = board[3][1], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b7,3,1,playerSymbol))
    b8 = tk.Button(tttWindow, text = board[3][2], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b8,3,2,playerSymbol))
    b9 = tk.Button(tttWindow, text = board[3][3], font = helv50, padx = 25, pady = 25, command = lambda: changeSymbol(b9,3,3,playerSymbol))
    # Creates list of the button objects that can be iterated through later
    buttonList = [b1, b2, b3, b4, b5, b6, b7, b8, b9]


    # Creates labels
    turnLabel = tk.Label(tttWindow, text = f"It is {playerSymbol}'s turn.", font = helv25)
    label2 = tk.Label(tttWindow, text = "Pick a slot!")

    # Displays buttons in the 3x3 grid pattern
    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)
    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)
    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

    # Displays labels at the bottom of the screen
    turnLabel.grid(row = 3, column = 0, columnspan = 3) # Displays who's turn it is
    label2.grid(row = 4, column = 0, columnspan = 3) # Displays smaller misc message

    # Changes the symbol, takes the button object for modification, x and y for board dict coords, and symbol for the player symbol
    def changeSymbol(buttonObj, x, y, symbol):
        if board[x][y] != "-": # Checks if the slot is empty or not
            label2.config(text = "Invalid Slot!")
        else:
            board[x][y] = symbol
            buttonObj.config(text = board[x][y], state = "disabled") # Sets the button the player clicked to their symbol and disables it
            if winCheck(board, symbol) == 0:
                global tttWindow
                for i in buttonList: # Iterates through the list of button objects
                    i.config(state = "disabled") # Sets each button to disabled
                label2.config(text = "Close the window to continue!")
                cf.tttGame_returnVal = symbol
                tttWindow.destroy()
                return 
            
            # Modifies the player's symbol
            global playerSymbol
            if symbol == "x":
                playerSymbol = "o"
            else:
                playerSymbol = "x"
            turnLabel.config(text = f"It is {playerSymbol}'s turn!")

    def winCheck(board,symbol):
            # Checks for horizontal wins
            for i in board:
                # Creates set of the values in each row
                rowSet = set(board[i].values())
                # As sets cannot contain duplicate values, a row such as "x o x" will become {"x","o"}
                # We can then check if the row contains only one value (such as {"x"}) and if the value in the set is the player's symbol.
                if len(rowSet) == 1 and playerSymbol in rowSet:
                    turnLabel.config(text = f"{symbol} wins horizontally!")
                    return 0
            # Checks for vertical wins
            boardSet = set()
            for i in range(1,4):
                colSet = set()
                # Have to use range(1,4) since range(1,3) won't go up to 3 for whatever reason.
                for row in range(1,4):
                    colSet.add(board[row][i])
                    boardSet.add(board[row][i])
                # Same as above
                if len(colSet) == 1 and playerSymbol in colSet:
                    turnLabel.config(text = f"{symbol} wins vertically!")
                    return 0
            # Checks for diagonal wins
            diag1 = set(board[1][1]+board[2][2]+board[3][3]) # Top left to bottom right
            diag2 = set(board[1][3]+board[2][2]+board[3][1]) # Top right to bottom left
            # Same check system as above
            if len(diag1) == 1 and playerSymbol in diag1:
                turnLabel.config(text = f"{symbol} wins diagonally!")            
                return 0
            if len(diag2) == 1 and playerSymbol in diag2:
                turnLabel.config(text = f"{symbol} wins diagonally!")
                return 0
            # Checks for draws using boardSet, which will contain all values in the dictionary
            if "-" not in boardSet: # Checks if there are any empty slots left
                turnLabel.config(text = f"It's a draw!")
                return 0

def guessingGame():

    answerNum = random.randint(1,100)
    print(answerNum)
    global playerAttempts
    playerAttempts = 0

    global gGame 
    gGame = True

    def submit():
        try:
            global gGame
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
                cf.gGame_returnVal = 1
                gGame = False
                ngWindow.destroy()
            if playerAttempts >= 10:
                cf.gGame_returnVal = 0
                gGame = False
                ngWindow.destroy()
        except:
            answerLabel.config(text = "Error Encountered! Guess again.")

    # Initializes main window
    global ngWindow
    ngWindow = tk.Toplevel(root)
    ngWindow.title("Number Guessing Game")
    ngWindow.geometry("170x130")

    # Initializes widgets
    guessingTitle = tk.Label(ngWindow, text = "Guess a Number!", font= helv15)
    answerLabel = tk.Label(ngWindow, text = "Guess...")
    inputBox = tk.Entry(ngWindow, width = 20, borderwidth = 4)
    submitButton = tk.Button(ngWindow, text = "Submit Number", command = submit)

    # Displays widgets
    inputBox.grid(row = 2, column = 0)
    guessingTitle.grid(row = 0, column = 0)
    answerLabel.grid(row = 1, column = 0)
    submitButton.grid(row = 3, column = 0)

def codeEnter(code):
    # Initialize main window
    global ceWindow
    ceWindow = tk.Toplevel()
    ceWindow.title("Keypad")
    ceWindow.geometry("233x320")

    # Initialize widgets
    display = tk.Entry(ceWindow, width = 17, borderwidth = 5, font = helv20)
    display.grid(row = 0, column = 0, columnspan = 3)

    def button_click(num):
        newText = display.get() + str(num)
        display.delete(0, tk.END)
        display.insert(0, newText)

    def submit():
        print(code)
        answer = display.get()
        if answer == "":
            display.delete(0, tk.END)
            display.insert(0, "Enter a code!")
            display.update()
            time.sleep(2)
            display.delete(0, tk.END)
        else:
            if answer == code:
                display.delete(0, tk.END)
                display.insert(0, "Correct!")
                display.update()
                time.sleep(2)
                cf.ceGame_returnVal = "correct"
                ceWindow.destroy()
            else:
                if len(answer) == 4:
                    display.delete(0, tk.END)
                    display.insert(0, "Incorrect!")
                    display.update()
                    time.sleep(2)
                    display.delete(0, tk.END)
                elif len(answer) < 4:
                    display.delete(0, tk.END)
                    display.insert(0, "Too short!")
                    display.update()
                    time.sleep(2)
                    display.delete(0, tk.END)
                elif len(answer) > 5:
                    display.delete(0, tk.END)
                    display.insert(0, "Too long!")
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

def displayEnd(ending, endingNo):
    global endScreen
    # Creates the end screen window
    endScreen = tk.Toplevel(root)
    endName = ending["name"]
    endScreen.title(f"New Ending - {endName}")
    endScreen.geometry("550x150")

    # Updates the player's end dictionary
    player.unlockEnding(endingNo)

    # Creates the labels
    endName_label = tk.Label(endScreen, text = f"Ending Reached - {endName}", font = helv25)
    endText_label = tk.Label(endScreen, text = ending["text"], font = helv15)
    end2Text_label = tk.Label(endScreen, text = f"You've now unlocked {player.unlockedEndings}/{len(player.endDict)} endings.")
    restartButton = tk.Button(endScreen, text = "Restart Game", command = lambda: player.resetGame(endScreen), font = helv20) # Button to restart the game

    # Displays widgets
    endName_label.grid(row = 0, column = 0, sticky = "w")
    endText_label.grid(row = 2, column = 0, sticky = "w")
    end2Text_label.grid(row = 1, column = 0, sticky = "w")
    restartButton.grid(row = 3, column= 0, sticky = "w")

def wineGuesser():
    # Python garbage collector goes ahead and gets rid of the image variables if they are local for whatever reason
    global wgWindow, wine1_img, wine2_img, wine3_img
    wgWindow = tk.Toplevel()
    wgWindow.title("Wine Guesser")
    wgWindow.geometry("500x300")

    def submit(choice):
        if choice == random.randint(1,3):
            descLabel.config(text = "You died! Ahhh.")
            descLabel.update()
            time.sleep(2)
            wgWindow.destroy()
            cf.wgGame_returnVal = 0
        else:
            descLabel.config(text = "You chose the wine. Nice job!")
            descLabel.update()
            time.sleep(2)
            wgWindow.destroy()
            cf.wgGame_returnVal = 1

    titleLabel = tk.Label(wgWindow, text = "Wine Guesser", font = helv25)
    descLabel = tk.Label(wgWindow, text = "Choose a poi- wine. Be careful now.", font = helv15)

    # Create wine bottles
    preWine1_img = Image.open("winebottle1.png")
    preWine1_img = preWine1_img.resize((60, 90), Image.ANTIALIAS)
    wine1_img = ImageTk.PhotoImage(preWine1_img)

    preWine2_img = Image.open("winebottle2.png")
    preWine2_img = preWine2_img.resize((60, 90), Image.ANTIALIAS)
    wine2_img = ImageTk.PhotoImage(preWine2_img)

    preWine3_img = Image.open("winebottle3.png")
    preWine3_img = preWine3_img.resize((60, 90), Image.ANTIALIAS)
    wine3_img = ImageTk.PhotoImage(preWine3_img)

    # Creates image labels
    wine1 = tk.Button(wgWindow, image = wine1_img, command = lambda: submit(1))
    wine2 = tk.Button(wgWindow, image = wine2_img, command = lambda: submit(2))
    wine3 = tk.Button(wgWindow, image = wine3_img, command = lambda: submit(3))

    titleLabel.grid(row = 0, column = 0, sticky = "w", columnspan = 3)
    descLabel.grid(row = 1, column = 0, sticky = "w", columnspan = 3)
    wine1.grid(row = 2, column = 0)
    wine2.grid(row = 2, column = 1)
    wine3.grid(row = 2, column = 2)

def multipleChoice():
    global mcWindow, questionNo, correctAnswer
    # Sets up the window
    mcWindow = tk.Toplevel()
    mcWindow.title("Quiz")
    mcWindow.geometry("600x200")

    questionNo = 0
    correctAnswer = 0

    # Dictionary to store the questions (q), answers (answers), and correct answer number (c).
    questionsDict = {1:{"q":"How old am I?", "answers":{1:"I don't know", 2:"INT", 3:"FLOAT", 4:"14"}, "c":4},
                    2:{"q":"What's my name?","answers":{1:"James",2:"Dolt",3:"Bence",4:"Arthur"},"c":3},
                    3:{"q":"What programming language are Operating Systems coded in?","answers":{1:"C",2:"Python",3:"Scratch",4:"Java"},"c":1},
                    4:{"q":"What is the lowest level programming language?","answers":{1:"Assembly",2:"Factory",3:"C",4:"JVM"}, "c":1},
                    5:{"q":"What programming language are websites made in?","answers":{1:"C",2:"Javascript",3:"Java",4:"Python"}, "c":2},
                    6:{"q":"What programming language is used for data science?","answers":{1:"Javascript",2:"Java",3:"Python",4:"Java"}, "c":3}
                    }

    # Read start() first, most variables are initialized there
    def submit(answer):
        global qName, qDesc, questionNo, correctAnswer
        try:
            if answer == questionsDict[qList[questionNo]]["c"]:
                print("Correct!")
                correctAnswer += 1
                qDesc.config(text = "Correct!")
            else:
                print("Incorrect!")
                qDesc.config(text = "Incorrect!")
            questionNo += 1
            qName.config(text = questionsDict[qList[questionNo]]["q"])
            for i in range(1,5):
                buttonDict[i].config(text = questionsDict[qList[questionNo]]["answers"][i])
        except KeyError:
            qDesc.config(text = "End of Game!")
            qName.config(text = f"You got: {correctAnswer}/{len(qList)}")
            qDesc.update()
            qName.update()
            for i in range(1,5):
                buttonDict[i].config(state = "disabled")
            time.sleep(2)
            if correctAnswer >= len(questionsDict)/2:
                cf.mcGame_returnVal = 1
            else:
                cf.mcGame_returnVal = 0
            mcWindow.destroy()
        except IndexError:
            qDesc.config(text = "End of Game!")
            qName.config(text = f"You got: {correctAnswer}/{len(qList)}")
            qDesc.update()
            qName.update()
            for i in range(1,5):
                buttonDict[i].config(state = "disabled")
            time.sleep(2)
            if correctAnswer >= len(questionsDict)/2:
                cf.mcGame_returnVal = 1
            else:
                cf.mcGame_returnVal = 0
            mcWindow.destroy()


    title = tk.Label(mcWindow, text = "Multiple Choice Quiz", font = helv25)
    a1 = tk.Button(mcWindow, font = helv10, command = lambda: submit(1))
    a2 = tk.Button(mcWindow, font = helv10, command = lambda: submit(2))
    a3 = tk.Button(mcWindow, font = helv10, command = lambda: submit(3))
    a4 = tk.Button(mcWindow, font = helv10, command = lambda: submit(4))

    a1.grid(row = 3, column = 0)
    a2.grid(row = 3, column = 1)
    a3.grid(row = 3, column = 2)
    a4.grid(row = 3, column = 3)
    buttonDict = {1:a1,2:a2,3:a3,4:a4}

    def start():
        global qName, qDesc, qList
        qList = list(range(1,len(questionsDict)+1)) # Creates a list from 1 - to the length of the list
        for i in range(len(qList)-3): # Pops all values except for three.
            popNo = random.randint(0,len(qList)-1)
            print(f"Pop: {popNo} || Length: {len(qList)} || List: {qList}")
            qList.pop(popNo)
        qName = tk.Label(mcWindow, text = questionsDict[qList[0]]["q"], font = helv15)
        qName.grid(row = 2, column = 0, sticky = "w", columnspan = 5)
        qDesc = tk.Label(mcWindow, text = "Make your choice!",font = helv15)
        qDesc.grid(row = 1, column = 0, sticky = "w", columnspan = 5)
        for i in range(1,5):
            buttonDict[i].config(text = questionsDict[qList[0]]["answers"][i])

    title.grid(row = 0, column = 0, columnspan = 4)

    start()

def doorGuesser():
    # Python garbage collector goes ahead and gets rid of the image variables if they are local for whatever reason
    global dgWindow, door1_img, door2_img, door3_img
    dgWindow = tk.Toplevel()
    dgWindow.title("Door Guesser")
    dgWindow.geometry("500x300")

    def submit(choice):
        if choice in [1,3]:
            descLabel.config(text = "Wrong door! Try again.")
            descLabel.update()
            time.sleep(2)
            dgWindow.destroy()
            cf.dgGame_returnVal = 0
        else:
            descLabel.config(text = "You chose the right door. Nice job!")
            descLabel.update()
            time.sleep(2)
            dgWindow.destroy()
            cf.dgGame_returnVal = 1

    titleLabel = tk.Label(dgWindow, text = "Door Guesser", font = helv25)
    descLabel = tk.Label(dgWindow, text = "Choose the right door. May or may not lead to death.", font = helv15)

    # Create doors
    preDoor1_img = Image.open("door1.png")
    preDoor1_img = preDoor1_img.resize((60, 90), Image.ANTIALIAS)
    door1_img = ImageTk.PhotoImage(preDoor1_img)

    preDoor2_img = Image.open("door2.jpg")
    preDoor2_img = preDoor2_img.resize((60, 90), Image.ANTIALIAS)
    door2_img = ImageTk.PhotoImage(preDoor2_img)

    preDoor3_img = Image.open("door3.png")
    preDoor3_img = preDoor3_img.resize((60, 90), Image.ANTIALIAS)
    door3_img = ImageTk.PhotoImage(preDoor3_img)

    # Creates image labels
    door1 = tk.Button(dgWindow, image = door1_img, command = lambda: submit(1))
    door2 = tk.Button(dgWindow, image = door2_img, command = lambda: submit(2))
    door3 = tk.Button(dgWindow, image = door3_img, command = lambda: submit(3))

    titleLabel.grid(row = 0, column = 0, sticky = "w", columnspan = 3)
    descLabel.grid(row = 1, column = 0, sticky = "w", columnspan = 3)
    door1.grid(row = 2, column = 0)
    door2.grid(row = 2, column = 1)
    door3.grid(row = 2, column = 2)

def keyGet():
    global kgWindow, key_img
    kgWindow = tk.Toplevel()
    kgWindow.title("Item get!")
    kgWindow.geometry("300x220")

    title = tk.Label(kgWindow, text = "Item Get!", font = helv25)
    subText = tk.Label(kgWindow, text = "You picked up a key!", font = helv20)
    exitButton = tk.Button(kgWindow, text = "Exit", font = helv15, command = kgWindow.destroy)

    preKey_img = Image.open("key.png")
    preKey_img = preKey_img.resize((150, 90), Image.ANTIALIAS)
    key_img = ImageTk.PhotoImage(preKey_img)

    keyLabel = tk.Label(kgWindow, image = key_img)

    title.grid(row = 0, column = 0, sticky = "w")
    subText.grid(row = 1, column = 0, sticky = "w")
    keyLabel.grid(row = 2, column = 0, sticky = "w")
    exitButton.grid(row = 3, column = 0, sticky = "w")

    player.keyGot = 1

def winScene():
    global fWindow
    fWindow = tk.Toplevel()
    fWindow.title("The End")
    fWindow.geometry("400x200")

    titleLabel = tk.Label(fWindow, text = "The End.", font = helv35)
    subText = tk.Label(fWindow, text = "Congratulations on finishing the game!", font = helv20)
    author = tk.Label(fWindow, text = "'RPG' by Bence Redmond")
    exitButton = tk.Button(fWindow, text = "Exit", font = helv20, command = fWindow.destroy)

    titleLabel.grid(row = 0, column = 0, sticky = "w")
    subText.grid(row = 2, column = 0, sticky = "w")
    author.grid(row = 1, column = 0, sticky = "w")
    exitButton.grid(row = 3, column = 0, sticky = "w")

class ToolTip(object):
    # Throws a lot of errors but works fine
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text

        def enter(event):
            self.showTooltip()
        def leave(event):
            self.hideTooltip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def showTooltip(self):
        if self.widget["state"] != "disabled":
            self.tooltipwindow = tw = tk.Toplevel(self.widget)
            tw.wm_overrideredirect(1) # Window without border and no normal means of closing
            tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx(), self.widget.winfo_rooty())) # Sets size of tooltip
            label = tk.Label(tw, text = self.text, background = "#ffffe0", relief = 'solid', borderwidth = 1)
            label.pack() 
            tooltipList.append(self)

    def hideTooltip(self):
        for i in tooltipList:
            if i.widget["state"] == "disabled":
                i.tooltipwindow.destroy()
                tooltipList.remove(self)
        if self.widget["state"] != "disabled" or type(self.tooltipwindow) == "tkinter.TopLevel":
            if self in tooltipList:
                self.tooltipwindow.destroy()
                tooltipList.remove(self)
                self.tooltipwindow = None

# Class to store player information
class playerState():

    def __init__(self, room, lives):
        self.room = room # Stores current room as an object
        self.lives = lives
        self.unlockedEndings = 0 
        # Dictionary to store different end conditions
        self.endDict = {0:{"name":"Death", "unlocked":False, "text":"Expected to be honest.", "room":"N/A", "c":"None!"},
                        1:{"name":"Awkward...","unlocked":False, "text":"Well, you weren't supposed to do that.", "room":"Doorway", "c":"1"},
                        2:{"name":"Scaredy Cat","unlocked":False, "text":"Hide from your fears.", "room":"Closet", "c":"9"},
                        3:{"name":"Relaxation Time","unlocked":False,"text":"Sometimes you just need to sit back and relax.","room":"Theatre", "c":"7"},
                        4:{"name":"Tasty!","unlocked":False, "text":"Too much food...","room":"Food Closet","c":"6"}
                    }
        self.code = ["-","-","-","-"]
        self.keyGot = 0

    def loseLife(self, lost):
        self.heartDict[self.lives].config(image = emptyHeart_img)
        self.lives -= lost
        if self.lives <= 0:
            displayEnd(player.endDict[0], 0)
            self.unlockEnding(0)
            self.lives = 3
            for i in range(1,4):
                self.heartDict[i].config(image = heart_img)


    def resetGame(self, destroyWindow):
        # Closes the end screen window
        destroyWindow.destroy()
        # Resets the the rooms' text and puzzles
        createRooms()
        createNeighbours()
        player.room = startingRoom
        # Reloads the "map"
        startingRoom.initState()

    def unlockEnding(self, ending):
        # Checks if the ending has already been unlocked
        if self.endDict[ending]["unlocked"] != True:
            self.unlockedEndings += 1
        self.endDict[ending].update({"unlocked":True})
        if ending - 1 >= 0:
            self.code[ending-1] = self.endDict[ending]["c"]

# Class used to create the rooms
class room():
    def __init__(self, puzzle, name, text, winText, loseText, code = 0):
        self.name = name
        self.puzzle = puzzle
        self.text = text # Text to display when the player enters a room
        self.loseText = loseText
        self.winText = winText
        self.code = code

    def assignNeighbours(self, left, right, up, down):
        # Stores the information about the room's neighbours, and the button object that leads to that room
        self.neighbours = {"left":{"button":leftArrow, "room":left}, 
                            "right":{"button":rightArrow, "room":right}, 
                            "up":{"button":upArrow, "room":up}, 
                            "down":{"button":downArrow, "room":down}}

    # Loads the room
    def initState(self):
        global secondLabel, interactButton, roomLabel, roomText
        # Edits the text to the appropriate room's
        roomLabel.config(text = player.room.name)
        roomText.config(text = player.room.text)
        # List to iterate through later
        dictList = ["left","right","up","down"]
        print("Initialized")
        for i in dictList:
            neighbour = self.neighbours[i] # Ease of access
            if neighbour["room"] == False: # Checks if there is a neighbouring room in that direction
                neighbour["button"].grid_remove()
                # neighbour["button"].config(state = "disabled", bg = "#ff8080")
            else: # If not, loads appropriately
                neighbour["button"].grid()
                if self.puzzle == "fin": # Checks if the player has completed the puzzle
                    neighbour["button"].config(state = "active", bg = "white")
                    idToolTip = ToolTip(neighbour["button"], text = neighbour["room"].name)
                    print(idToolTip)
                else:
                    if neighbour["room"].puzzle == "fin":
                            neighbour["button"].config(state = "active", bg = "white")
                    else:
                        neighbour["button"].config(state = "disabled", bg = "#ff8080")
        if self.puzzle != "fin": # Checks to see if the interact button needs to be locked or not
            interactButton.config(state = "active", bg = "white")
        else:
            interactButton.config(state = "disabled", bg = "#ff8080")


    def moveRoom(self, direction):
        global roomLabel, roomText, tooltipList
        for i in tooltipList:
            i.tooltipwindow.destroy()
        tooltipList = []
        player.room = self.neighbours[direction]["room"] # Sets the player's current room to the room at that given direction
        roomLabel.config(text = player.room.name) 
        roomText.config(text = player.room.text)
        player.room.initState()


    # Handles puzzle loading and outcome determination
    def interact(self):
        global interactButton, roomText
        interactButton.config(state = "disabled")
        if player.room.puzzle == "gGame":
            guessingGame()
            root.wait_window(ngWindow) # Pauses the following code until the game window has been closed
            returnVal = cf.gGame_returnVal # Ease of use
            if returnVal == 1: 
                player.room.text = player.room.winText
                roomText.config(text = player.room.text) # Edits the room text to be the win text
                interactButton.config(state = "active")
                player.room.puzzle = "fin"
                cf.gGame_returnVal = -1 # Resets cf.gGame_returnVal for future games (after in-game restart)
            elif returnVal == 0:
                interactButton.config(state = "disabled")
                player.room.text = player.room.loseText
                roomText.config(text = player.room.text)
                player.loseLife(1)
            player.room.initState()
            cf.gGame_returnVal = -1
        elif player.room.puzzle == "ttt":
            # Follows same principles as above
            ticTacToe()
            root.wait_window(tttWindow)
            returnVal = cf.tttGame_returnVal
            if returnVal == "x":
                player.room.text = player.room.winText
                roomText.config(text = player.room.text)
                player.room.puzzle = "fin"
            elif returnVal == "o":
                player.room.text = player.room.loseText
                roomText.config(text = player.room.text)
                interactButton.config(state = "active")
            else:
                interactButton.config(state = "active")
            cf.tttGame_returnVal = 0
            player.room.initState()
        elif player.room.puzzle == "code":
            codeEnter(player.room.code)
            root.wait_window(ceWindow)
            returnVal = cf.ceGame_returnVal
            if returnVal == "correct":
                player.room.text = player.room.winText
                roomText.config(text = player.room.text)
                player.room.puzzle = "fin"
            player.room.initState()
        elif player.room.puzzle == "wGame":
            wineGuesser()
            root.wait_window(wgWindow)
            returnVal = cf.wgGame_returnVal
            if returnVal == 1:
                player.room.text = player.room.winText
                roomText.config(text = player.room.text)
                player.room.puzzle = "fin"
            else:
                interactButton.config(state = "disabled")
                player.room.text = player.room.loseText
                roomText.config(text = player.room.text)
                player.loseLife(1)
            cf.wgGame_returnVal = -1
            player.room.initState()
        elif player.room.puzzle == "mc":
            multipleChoice()
            root.wait_window(mcWindow)
            returnVal = cf.mcGame_returnVal
            if returnVal == 1:
                player.room.text = player.room.winText
                roomText.config(text = player.room.text)
                player.room.puzzle = "fin"
            else:
                interactButton.config(state = "disabled")
                player.room.text = player.room.loseText
                roomText.config(text = player.room.text)
                player.loseLife(1)
            cf.mcGame_returnVal = -1
            player.room.initState()
        elif player.room.puzzle == "end":
            winScene()
            root.wait_window(fWindow)
            root.destroy()
        elif player.room.puzzle == "door":
            doorGuesser()
            root.wait_window(dgWindow)
            returnVal = cf.dgGame_returnVal
            if returnVal == 1:
                player.room.text = player.room.winText
                roomText.config(text = player.room.text)
                keyGet()
                root.wait_window(kgWindow)
                player.room.puzzle = "fin"
            else:
                interactButton.config(state = "disabled")
                player.room.text = player.room.loseText
                roomText.config(text = player.room.text)
                player.loseLife(1)
            cf.dgGame_returnVal = -1
            player.room.initState()           
        elif player.room.puzzle == "none":
            player.room.puzzle = "fin"
            roomText.config(text = player.room.winText)
            player.room.initState()
        else:
            # If the puzzle is not any of the above, then it must be an ending.
            displayEnd(player.endDict[player.room.puzzle], player.room.puzzle)

def createRooms():
    # room() takes the puzzle, name of room, text to display when the player enters, text to display when the players loses/wins.
    global startingRoom, hallway1, doorway, kitchen, ballroom, hallway2, bossroom, slide, stairs1, basement, closet, stairs2, cellar, theatre, dining_room, hallway3, kitchen, closet2, hallway4, living_room
    startingRoom = room("door", "Entrance", "Ho ho ho... welcome to my house of Death!", "Hmm, maybe that was a bit too easy.", "Well that was a good effort... down one life!", "1976")
    hallway1 = room("ttt", "Hallway", "You see a whiteboard on the wall, with a Tic Tac Toe board. Let's play!", "I would have been worried if you hadn't won that.", "How did you... lose against yourself?")
    doorway = room(1, "Doorway", "Well, I guess you win?", "N/A", "N/A")
    ballroom = room("mc", "Ballroom", "Pop quiz! No dancing or music unfortunately.", "Maybe I should have made the questions a bit harder.", "You should brush up on your trivia.")
    hallway2 = room("code", "Hallway", "You here a faint hum ahead. Spooky.", "There's no turning back once you go forward.", "Go and explore more. Open up the endings screen to see what you have so far.", "1976")
    bossroom = room("end", "The Exit", "Damn you!", "Begone fool...", "Muahahaha! Try again.")
    slide = room("none", "Slide!", "Down you go!", "N/A", "N/A")
    stairs1 = room("gGame", "Basement Stairs", "The stairs lead down to a very dark room.", "I should stop using these number guessing games.", " Get good.")
    basement = room("none", "Basement", "Ahhhh! I'm joking. Why would I get scared in my own house?", "Well, you've still got a ways to go.", "Hahahahaha.")
    closet = room(2, "Closet", "Just hide and everything will be alright.", "N/A", "N/A")
    stairs2 = room("door", "Deeper Stairs", "These lead deeper down...", "Good luck in the next room. Hehehe...", "Come on. You just have to pick a door.")
    cellar = room("wGame", "Wine Cellar", "Ah, a proud collection. Don't touch anything!", "That was expensive...", "Serves you right!")
    theatre = room(3, "Theatre", "Sometimes it's nice to relax with some popcorn and watch a movie.", "N/A", "N/A")
    dining_room = room("none", "Dining Room", "Good luck finding your way through this maze of tables.", "What do you mean it was just a restaurant?.", "If you stick to the right it might work.")
    hallway3 = room("ttt", "Hallway", "Maybe this will stump you.", "Well, congrats. You've done the bare minimum.", "How...?")
    kitchen = room("none", "Kitchen", "Let's test your cooking skills.", "Ah... I may have forgotten to lay out the food. Forget this.", "How many times have you cooked in your life?")
    closet2 = room(4, "Food Closet", "Eat your problems away.", "N/A", "N/A")
    hallway4 = room("none", "Hallway", "Good luck picking this!", "Darn it. I paid a lot for that lock.", "Your parents raised you well.")
    living_room = room("none", "Living Room", "Let's watch some TV and relax.", "Do you mind getting some food?","Have you never used a remote in your life?")

def createNeighbours():
    global startingRoom, hallway1, doorway, kitchen
    # Assigns the room's neighbours as room objects
    # assignNeighbours(Left, Right, Up, Down)
    startingRoom.assignNeighbours(False, False, hallway1, doorway)
    doorway.assignNeighbours(False, False, startingRoom, False)
    hallway1.assignNeighbours(False, False, ballroom, startingRoom)
    ballroom.assignNeighbours(stairs1, dining_room, hallway2, hallway1)
    hallway2.assignNeighbours(slide, False, bossroom, ballroom)
    bossroom.assignNeighbours(False, False, False, hallway2)
    slide.assignNeighbours(basement, False, False, False)
    stairs1.assignNeighbours(basement, ballroom, False, False)
    basement.assignNeighbours(False, stairs1, closet, stairs2)
    closet.assignNeighbours(False, False, False, basement)
    stairs2.assignNeighbours(False, False, basement, cellar)
    cellar.assignNeighbours(False, theatre, stairs2, False)
    theatre.assignNeighbours(cellar, False, False, False)
    dining_room.assignNeighbours(ballroom, False, hallway3, hallway4)
    hallway3.assignNeighbours(False, False, kitchen, dining_room)
    kitchen.assignNeighbours(False, False, closet2, hallway3)
    closet2.assignNeighbours(False, False, False, kitchen)
    hallway4.assignNeighbours(False, False, dining_room, living_room)
    living_room.assignNeighbours(False, False, hallway4, False)

createRooms()

player = playerState(startingRoom, 3)

# Handles the ending screen window
def endingsScreen(endings):
    global endingsButton
    endingsButton.config(state = "disabled")
    endingsWin = tk.Toplevel()
    endingsWin.title("Your Unlocked Endings")
    endingsWin.geometry("650x500")

    codeText = "".join(player.code)

    endingsTitle = tk.Label(endingsWin, font = helv35, text = f"All Endings || {player.unlockedEndings}/{len(endings)} Unlocked")
    codeLabel = tk.Label(endingsWin, font = helv25, text = f"Code: {codeText}\n---------------------------------------")

    row = 2
    # Used to iterate through the ending dictionary, and display each value there
    # This system doesn't require me to come back and edit when I need to add new endings
    for i in range(0,len(endings)):
        print(endings[i])
        tempTitle = tk.Label(endingsWin, text = endings[i]["name"], font  = helv25, anchor = "w")
        tempLabel = tk.Label(endingsWin, text = f"Unlocked: {endings[i]['unlocked']} || {endings[i]['text']}")
        tempTitle.grid(row = row, column = 0, sticky = "w")
        tempLabel.grid(row = row + 1, column = 0, sticky = "w")
        row += 2

    endingsTitle.grid(row = 0, column = 0, columnspan = 2, sticky = "w")
    codeLabel.grid(row = 1, column = 0, columnspan = 2, sticky = "w")
    root.wait_window(endingsWin) # Waits until the player closes the ending screen
    endingsButton.config(state = "active")

def displayMenu():
    global endingsButton, restartButton
    menuWindow = tk.Toplevel()
    menuWindow.geometry("220x200")
    menuTitle = tk.Label(menuWindow, text = "Menu", font = helv35)
    endingsButton = tk.Button(menuWindow, text = "Unlocked Endings", font = helv20, command = lambda: endingsScreen(player.endDict))
    restartButton = tk.Button(menuWindow, text = "Restart", font = helv20, command = lambda: player.resetGame(menuWindow))
    menuTitle.pack()
    endingsButton.pack()
    restartButton.pack()

# Initializes main images
preHeart_img = Image.open("heart.png")
preHeart_img = preHeart_img.resize((60, 60), Image.ANTIALIAS)
preEmptyHeart_img = Image.open("emptyHeart.png")
preEmptyHeart_img = preEmptyHeart_img.resize((60, 60))
emptyHeart_img = ImageTk.PhotoImage(preEmptyHeart_img)
heart_img = ImageTk.PhotoImage(preHeart_img)

# Creates the heart labels
heart1 = tk.Label(root, image = heart_img, anchor = "w")
heart2 = tk.Label(root, image = heart_img, anchor = "w")
heart3 = tk.Label(root, image = heart_img, anchor = "w")
player.heartDict = {1:heart1, 2:heart2, 3:heart3}


# Creates main text
roomLabel = tk.Label(root, text = player.room.name, font = helv35)
roomText = tk.Label(root, text = player.room.text, font = helv20)
secondLabel = tk.Label(root, text = "Choose a direction to go:", font = helv15)

# Creates buttons
menuButton = tk.Button(root, text = "Menu", font = helv25, borderwidth = 5, command = displayMenu)
upArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "^", font = helv15, command = lambda: player.room.moveRoom("up"))
leftArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "<", font = helv15, command = lambda: player.room.moveRoom("left"))
downArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "v", font = helv15, command = lambda: player.room.moveRoom("down"))
rightArrow = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = ">", font = helv15, command = lambda: player.room.moveRoom("right")) 
interactButton = tk.Button(root, bg = "#ff8080", width = 6, height = 3, state = "disabled", text = "x", font = helv15, command = player.room.interact)
# Creates empty canvas spaces
topCanvas = tk.Canvas(root, width = 140, height = 10)

# Displays the created widgets
heart1.grid(row = 0, column = 0)
heart2.grid(row = 0, column = 1)
heart3.grid(row = 0, column = 2)
roomLabel.grid(row = 0, column = 3, padx = 20)
secondLabel.grid(row = 2, column = 0, columnspan = 3)
topCanvas.grid(row = 0, column = 4, columnspan = 1)
roomText.grid(row = 1, column = 0, columnspan = 8, sticky = "w")

upArrow.grid(row = 3, column = 1)
leftArrow.grid(row = 4, column = 0)
downArrow.grid(row = 5, column = 1)
rightArrow.grid(row = 4, column = 2)
interactButton.grid(row = 4, column = 1)
menuButton.grid(row = 0, column = 5)

createNeighbours()

startingRoom.initState()

root.mainloop() # Starts main window