import sys
import random

def ex1():
    mode = int(input("What do you want the numbers to be multiples of?\n"))
    tries = int(input("How many numbers will you input? \n"))
    for i in range(tries):
        num = float(input("Input number: "))
        if num % mode == 0:
            print("Multiple of 5!")
        else:
            print("Not a multiple of 5.")


def bestTimes():
    participants = int(input("How many people participated in the race? \n"))
    partArray = []
    for i in range(participants):
        try:
            time = float(input("Input a time (seconds): "))
            partArray.append(time)
        except:
            print("Error inputing your number!")
    partArray.sort()
    print("The best time was:", partArray[0], ", The second best time was:", partArray[1], ", And the third best time was:", partArray[2])


def stars():
    totalStars = ""
    starNo = int(input("\nWhat would you like to rate this place? (1-5 Stars) \n"))
    if starNo > 5: 
        starNo = 5
    elif starNo < 1:
        starNo = 1
    for i in range(starNo):
        totalStars = totalStars + "*"
    print("You've rated this place: ", totalStars)

while True:
    stars()