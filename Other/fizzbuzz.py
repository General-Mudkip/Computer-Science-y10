def fizz1():
    for i in range(1,50):
        div3 = i % 3
        div5 = i % 5
        prtStr = ""

        if div3 == 0:
            prtStr += "Fizz"
        if div5 == 0:
            prtStr += "Buzz"
        print(f"{i} {prtStr}")

fizz1()