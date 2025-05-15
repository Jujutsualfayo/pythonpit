import uuid
from datetime import datetime

class BaseModel:
    '''Initialize the bmodel with a unique ID and timestamps'''
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    def __str__(self):
        '''Return the f string representation'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        '''Updates the updated_at to current dattime'''
        self.updated_at = datetime.now()
    def to_dict(self):
        """Return dattime objectsin ISO format also return copy of the instances"""
        
        #create a copy of the results instance
        result = self.__dict__.copy()
        #Convert datetime to iso format strings
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        #Add the classname
        result["__class__"] = self.__class__.__name__

        return result
    
