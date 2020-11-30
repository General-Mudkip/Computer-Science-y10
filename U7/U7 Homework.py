def maxNum():
    numList = []
    for i in range(5):
        num = float(input(f"Enter number {i}: "))
        numList.append(num)
    numList.sort()
    print(numList[4])
