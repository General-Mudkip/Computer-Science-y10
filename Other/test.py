import random
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vowels = ["a","e","i","o","u"]
swear = ["cuk"]
counter = 0


def checker():
    for i in range(1000000):
        txt = consonants[random.randint(0,len(consonants)-1)] + vowels[random.randint(0,len(vowels)-1)] + consonants[random.randint(0,len(consonants)-1)]
        if txt in swear:
            return i

counter = 0
for it in range(100):
    counter += checker()
av = counter / 1000
print("Average Iteration: ", av)