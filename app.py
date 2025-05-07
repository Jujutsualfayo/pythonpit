class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an integer")
        if value < 0:
            raise ValueError("Must be above zero")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an integer")
        if value < 0:
            raise ValueError("Must be above zero")
        self.__height = value

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        row = str(self.print_symbol) * self.width
        return "\n".join([row for _ in range(self.height)])
    
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        print("Bye dear rectangle...")
        Rectangle.number_of_instances -= 1