def capital_indexes(str):
    capital_indexes = [i for i in str if i.upper() == i]
    return capital_indexes

print(capital_indexes("heLLo"))