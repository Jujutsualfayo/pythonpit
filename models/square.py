from models.rectangles import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)
        @property
        def size(self):
            return self.width
        @size.setter
        def size(self, value):
            self.width = value
            self.height = value
        def __str__(self):
            return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        