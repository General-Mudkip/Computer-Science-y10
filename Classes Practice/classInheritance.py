class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    
    def speak(self):
        print("What do I say?")

class cat(pet):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.colour}.")

class dog(pet):
    def speak(self):
        print("Bark")


p = pet("Tim", 19)
p.speak()
c = cat("Bill", 34, "Brown")
c.show()
d = dog("Jill", 25)
d.speak()