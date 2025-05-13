from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def validate_integer(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

