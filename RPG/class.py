class string():
    def __init__(self, text):
        self.text = text
    
    def uppercase(self):
        self.text = self.text.upper()

var = string("Hello")
var.uppercase()

print(var.text)