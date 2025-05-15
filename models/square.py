from models.rectangles import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        super().__init__(self)
        @property
        def size(self):
            return self.__size
        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("Value must be an integer")
            if value < 0:
                raise ValueError("Value must be more than 0")
            self.size = value
            @property
            def x(self):
                return self.__x
            @x.setter
            def x(self, value):
                if not isinstance(value, int):
                    raise TypeError("Value must be an integer")
                if value < 0:
                    raise ValueError("Value must be more than 0")
                self.x = value
            @property
            def y(self):
                return self.__y
            @y.setter
            def y(self, value):
                if not isinstance(value, int):
                    raise TypeError("Value must be an integer")
                if value < 0:
                    raise ValueError("Value must be more than 0")
                self.y = value