class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Value must be more than zero")
        self.__size = size

    def get_size(self):
        return self.__size
    
sq1 = Square(11)
sq2 = Square (56)

print("Size of sq1 is", sq1.get_size())
print("Size of sq2 is", sq2.get_size())

    