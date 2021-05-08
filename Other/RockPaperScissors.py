import random
from os import system


system('cls')
valid_moves = {"rock":1,"paper":3,"scissors":2}
game_modes = {"BOT","DUEL"}

def score(p1,p2,games,cond):
    if cond == "score":
        print("===============================")
        print(f"Player 1 Score:{p1} \n Player 2 Score: {p2} \n Games Played: {games}")
        if p1 > p2:
            print("Player 1 is in the lead!")
        elif p2 > p1:
            print("Player 2 is in the lead!")
        elif p1 == p2:
            print("It's a tie!")
        print("===============================")
    elif cond == "win":
        print("*******************************")
        print(f"Player 1 Score:{p1} \n Player 2 Score: {p2} \n Games Played: {games}")
        if p1 > p2:
            print("Player 1 Wins!")
        elif p2 > p1:
            print("Player 2 Wins!")
        elif p1 == p2:
            print("It's a tie!")
        print("*******************************")

while True:
    gamesPlayed = 0
    p1_wins = 0
    p2_wins = 0
    p1_input = 0
    p2_input = 0
    playing = str(input("Start Mod? BOT/DUEL: \n"))
    
    while playing != 0 and playing in game_modes:
        while p1_input not in valid_moves:
            p1_input = input("Player 1's Move (rock, paper, scissors): ")
            if p1_input not in valid_moves:
                print("Invalid move!")
        if playing == "DUEL":
            system('cls')
            while p2_input not in valid_moves:
                p2_input = input("Player 2's Move (rock, paper, scissors): ")
                if p2_input not in valid_moves:
                    print("Invalid move!")
        elif playing == "BOT":
            p2_input = random.choice(list(valid_moves))
        p1 = valid_moves.get(p1_input)
        p2 = valid_moves.get(p2_input)
        dif = p1 - p2
        gamesPlayed += 1
        if dif == 0:
            print("Tie!") 
        elif dif in [-1,2]:
            print("Player 1 Wins!")
            p1_wins += 1
            if str(input("Do you wish to continue playing? Y/N\n")) == "N":
                score(p1_wins,p2_wins,gamesPlayed,"win")
                playing = 0
                break
        elif dif in [-2,1]:
            print("Player 2 Wins!")
            p2_wins += 1
            if str(input("Do you wish to continue playing? Y/N\n")) == "N":
                score(p1_wins,p2_wins,gamesPlayed,"win")
                playing = 0
                break
        score(p1_wins,p2_wins,gamesPlayed,"score")
        p1_input = 0
        p2_input = 0