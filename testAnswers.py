def figures():
    years = int(input("How many years have you been collecting figures?\n"))
    print(f"You must have {years*4} figures.")


def christmas():
    p1 = float(input("What is the cost of item 1?\n"))
    p2 = float(input("What is the cost of item 2?\n"))
    total = 100 - p1 - p2
    if total > 0:
        print(f"You can afford it with {total}€ to spare.")
    else:
        print(f"You can't afford it, you need {abs(total)}€ more.")

def language():
    score = float(input("What percentage did you get on this exam?\n"))
    if score >= 85:
        grade = "C"
    elif score > 60:
        grade = "B"
    else:
        grade = "A"
    print(f"You got: {grade}!")




language()
