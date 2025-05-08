class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello my name is {self.name}"
def lookup(obj):
        return dir(obj)
    
p =Person("Alfayo")

print(lookup(p))