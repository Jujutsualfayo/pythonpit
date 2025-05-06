class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be more than 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be more than 0")
        self.__height = value
    
    def area(self):
        a = self.__height * self.__width
        return a
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range (self.__height)])
    
    def __repr__(self):
        return f"Rectangle ({self.__width}, {self.__height})"
    
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle##")

    


#test object 
r = Rectangle(5,4)
del r