class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Value must be more than zero")
        self.__size = size

    def area(self):
        return self.__size ** 2
    
sq1 = Square(4)
sq2 = Square (8)

print("Area of sq1 is", sq1.area())
print("Area of sq2 is", sq2.area())

    