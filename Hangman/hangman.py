import random
import json

with open("words.json") as words_json:
    words_list = json.load(words_json)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def hangman():
    # Gets a random word from the words list
    ran_word = words_list["data"][random.randint(0,len(words_list["data"])-1)]
    # Seperates each character into an element in a list
    ran_word_list = list(ran_word)
    print(ran_word_list)
    # Creates a duplicate list, except all values are "_"
    entered_list = ["_" for i in ran_word_list]
    print(entered_list)
    guessed_letters = {"complete":[""],"correct":[],"incorrect":[]}
    guesses = ""

                                            # Joins the list back together with spaces between the characters.
    print(f"Welcome to hangman! Here's your word to guess: \n{' '.join(entered_list)}")
    while guesses == "":
        try:
            guesses = int(input("How many guesses would you like?\n"))
            if guesses <= 0:
                print("Invalid number!")
                guesses = ""
            elif guesses > 10:
                print("Ok... that's a bit too big.")
                guesses = ""
            else:
                print(f"You now have {guesses} guesses.\n")
        except:
            print("Error encountered!")
    
    while entered_list != ran_word_list:
        guess = ""
        while guess in guessed_letters["complete"]:
            guess = input("\nWhat's your guess?\n").lower()
            if guess in guessed_letters["complete"]:
                print("You've already guessed that character!")
                guess = ""
            elif guess not in letters:
                print("Invalid character!")
                guess = ""
            
        if guess in ran_word_list:
            print("You guessed correctly!")

            guessed_letters["correct"].append(guess)
            guessed_letters["complete"].append(guess)

            # Counter
            c_ind = 0
            for i in ran_word_list:
                if i == guess:
                    # Gets i's index, and searches only from the most recently check index.
                    index = ran_word_list.index(i, c_ind)
                    entered_list[index] = guess
                c_ind += 1
            if entered_list == ran_word_list:
                print(f"Congrats! You won with {guesses} guesses left.\nThe word was:\n{ran_word}")
                print(f"\nYou made {len(guessed_letters['correct'])} correct guesses:\n{', '.join(guessed_letters['correct'])} \nAnd {len(guessed_letters['incorrect'])} incorrect guesses:\n{', '.join(guessed_letters['incorrect'])}")
        else:
            print("You guessed incorrectly...")
            guesses -= 0
            guessed_letters["incorrect"].append(guess)
            guessed_letters["complete"].append(guess)
            if guesses == 0:
                print(f"Game over! You ran out of guesses.\nThe correct word was: {ran_word}.")
                print(f"\nYou made {len(guessed_letters['correct'])} correct guesses:\n{', '.join(guessed_letters['correct'])} \nAnd {len(guessed_letters['incorrect'])} incorrect guesses:\n{', '.join(guessed_letters['incorrect'])}")
                entered_list = ran_word_list
        if entered_list != ran_word_list:
            print(f"Here's the board at the moment:\n", " ".join(entered_list),f"\nYou currently have {guesses} guesses.")
    play_again = input("Would you like to play again? Y / N\n")
    if play_again.lower() == "y":
        hangman()
    else:
        print("Oh alright then. Goodbye!")


hangman()