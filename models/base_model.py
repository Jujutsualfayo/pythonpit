import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):# str repr of uuidand updated timestamps
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    def __str__(self): # returns the string representation of the dictionary
        return (
            f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        )
    def save(self): # updated the updated at with current datetime
        self.updated_at = datetime.now()
        
    



        
   




      
    