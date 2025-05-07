class Parent:
    def greet(self):
        print("Hello from your parent")
class Child(Parent):
    def greet(self):
        print("Hello from child")

c = Child()
c.greet()

