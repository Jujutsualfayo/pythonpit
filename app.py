class Square:
    def __init__(self, size=0):
        self.size = size
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be more than 0")
        self.__size = value