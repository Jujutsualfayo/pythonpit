class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
    
sq1 = Square(25)
sq2 = Square(36)
print("Square 1 size is", sq1.get_size())
print("Square 2 size is", sq2.get_size())