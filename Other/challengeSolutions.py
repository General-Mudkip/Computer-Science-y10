def capital_indexes(string):
    capital_indexes = [i for i in string if i.upper() == i]
    return capital_indexes

print(capital_indexes("heLLo"))