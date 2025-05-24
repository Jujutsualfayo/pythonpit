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
    




        
   




      
    