class Dog:
    species = "Cannis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
print(Dog.species)

dog1 = Dog("Buddy", 2)
dog2 = Dog("Bruno", 3)

print(dog1.name)
print(dog2.name)