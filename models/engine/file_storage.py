import json
from os.path import exists

class FileStorage: # file that handles serialization/deserialization of BaseModel instances
    __file_path = "file.json"
    __objects = {}
    def all(self): # returns all the dictionaries objects
        return FileStorage.__objects
    def new(self, obj): # sets in __objects the obj with key <obj class name>.id
        key = f"{obj.__class.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    def save(self): #serializes the method to dict then to json
        json_objects = {
            key:obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_objects, f)
    def reload(self):
        """Deserializes the JSON file to __objects (if file exists)."""
        if exists(FileStorage.__file_path):
            from models.base_model import BaseModel
            with open(FileStorage.__file_path, 'r') as f:
                loaded_objects = json.load(f)
                for key, obj_dict in loaded_objects.items():
                    FileStorage.__objects[key] = BaseModel(**obj_dict)