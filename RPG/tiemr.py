import time
start_time = time.time()
answer = int(input("What is 2+2?\n"))
if time.time() - start_time > 10:
    print("Too slow! You did it in:", round(time.time() - start_time,2), "seconds.")
else:
    if answer == 4:
        print("Correct! You did it in:", round(time.time() - start_time,2), "seconds.")
    else:
        print("Incorrect! The correct answer was 4.")
