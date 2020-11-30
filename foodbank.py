total = 0
max = 0
for i in range(5):
    items = int(input(f"How many items did you collect on day {i+1}? \n"))
    total += items
    if items > max:
        largestDay = i+1
        max = items
print(f"You've collected {total} items in total. Your largest collection day was {largestDay}")