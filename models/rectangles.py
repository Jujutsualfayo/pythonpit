from models.base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value <= 0:
            raise ValueError("Value must be more than 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be integer")
        if value <= 0:
            raise ValueError("Value must be more than 0")
        self.__height = value
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value < 0:
            raise ValueError("Value must be more than zero")
        self.__x = value
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be more than 0")
        if value < 0:
            raise ValueError("Value must be more than 0")
        self.__y = value

    def area(self):
        return self.width * self.height
    def display(self):
        for _ in range(self.height):
            print("#" * self.width)
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    def update(self, *args, **kwargs):
        attrs = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < 0:
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    def to_dictionary(self):
        
