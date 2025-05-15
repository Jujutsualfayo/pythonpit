import json
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"

        if list_objs is None:
            list_dicts = []
        else:
            # convert each object to its dictionary form
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        # convert to JSON string
        json_string = cls.to_json_string(list_dicts)

        # write to file
        with open(filename, "w") as f:
            f.write(json_string)
            

