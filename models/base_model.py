import uuid
from datetime import datetime

class BaseModel: #initialize and assign unique id and upd with current datetimes
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    def __str__(self): # Brings abt the str representationof the dictionary
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        )
    def save(self): # updates the  updated at with the current datetime
        self.updated_at = datetime.now()
    def to_dict(self): # returns a dictionary containing values of the dict instance
        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict




        
   




      
    