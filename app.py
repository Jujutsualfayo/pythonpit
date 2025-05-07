class Parent:
    def greet(self):
        print("Hello from your parent")
class Child(Parent):
    pass

c = Child()
c.greet()

