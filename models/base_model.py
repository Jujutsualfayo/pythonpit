import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):# str repr of uuid and updated timestamps, adds features for adding key word arguments
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat)
                elif key != "__class__":
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at
                    storage.new(self)
    def __str__(self): # returns the string representation of the dictionary
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        )
    def save(self): # updated the updated at with current datetime
        self.updated_at = datetime.now()
        storage.save()
    def to_dict(self): # returns a dict containing values of __dict__ of the instance
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat
        obj_dict["updated_at"] = self.updated_at.isoformat
        return obj_dict

    



        
   




      
    