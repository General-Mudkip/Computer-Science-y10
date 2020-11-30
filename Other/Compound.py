def compound(init,interest,times):
    interest = (100 + interest) / 100
    final = init * (interest**times)
    return final
    

while True:
    print(compound(float(input("Initial Value: ")),float(input("Interest: ")),float(input("No. Times: "))))
