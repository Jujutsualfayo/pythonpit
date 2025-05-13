class Base:
    """Base class for managing id attribute in all future classes"""
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """Constructor: assigns id or auto-generates it"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


