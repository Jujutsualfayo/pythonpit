import json
from os.path import exists

class FileStorage: # file that handles serialization/deserialization of BaseModel instances
    __file_path = "file.json"
    __objects = {}
    def all(self): # returns all the dictionaries objects
        return FileStorage.__objects