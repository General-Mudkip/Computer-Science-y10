total = 0
maximum = 0
for i in range(5):
    items = int(input(f"How many items did you collect on day {i+1}? \n"))
    total += items
    if items > maximum:
        largestDay = i+1
        maximum = items
print(f"You've collected {total} items in total. Your largest collection day was {largestDay}")