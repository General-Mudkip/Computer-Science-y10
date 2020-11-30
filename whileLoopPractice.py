userInput = 0
numSum = 0
counter = 0
while userInput != -1:
    userInput = float(input("Enter a number: "))
    if userInput != -1:
        counter += 1
        numSum += userInput
print(f"The average is: {numSum/counter}")